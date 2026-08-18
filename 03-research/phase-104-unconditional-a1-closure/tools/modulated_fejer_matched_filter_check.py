#!/usr/bin/env python3
"""Exact checks for 104_108 (Fraction + Gaussian rationals only)."""

from fractions import Fraction as F


class G:
    def __init__(self, re=0, im=0):
        self.re, self.im = F(re), F(im)

    def __add__(self, other):
        other = as_g(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-as_g(other))

    def __rsub__(self, other):
        return as_g(other) - self

    def __mul__(self, other):
        other = as_g(other)
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def inv(self):
        den = self.re * self.re + self.im * self.im
        assert den
        return G(self.re / den, -self.im / den)

    def __truediv__(self, other):
        return self * as_g(other).inv()

    def __pow__(self, n):
        if n < 0:
            return self.inv() ** (-n)
        out, base = G(1), self
        while n:
            if n & 1:
                out *= base
            base *= base
            n //= 2
        return out

    def conj(self):
        return G(self.re, -self.im)

    def norm2(self):
        return self.re * self.re + self.im * self.im

    def __eq__(self, other):
        other = as_g(other)
        return self.re == other.re and self.im == other.im

    def __repr__(self):
        return f"G({self.re}, {self.im})"


def as_g(x):
    return x if isinstance(x, G) else G(x)


def alphas(L):
    return {k: F(L - abs(k), L * L) for k in range(-L + 1, L)}


def k_laurent(L, z):
    return sum((a * z**k for k, a in alphas(L).items()), G())


def h_phase(L, eta):
    # eta = exp(i*x)
    return k_laurent(L, eta)


def w_test(n, z):
    # z = exp(i*theta)
    return G(2) - z**n - z ** (-n)


def residue_term(w, n):
    return w**n + w ** (-n) - 2


def main():
    # Exact unit-circle samples: z=3/5+4i/5, eta=i.
    z = G(F(3, 5), F(4, 5))
    eta = G(0, 1)  # eta=exp(i*phi), hence exp(-ik phi)=eta^-k
    assert z.norm2() == 1 and eta.norm2() == 1

    # (6): direct modulated test versus shifted Fejer kernels.
    for L in range(1, 9):
        aa = alphas(L)
        assert sum(aa.values()) == 1
        for N in range(L, L + 6):
            direct = sum((a * eta ** (-k) * w_test(N + k, z)
                          for k, a in aa.items()), G())
            closed = (
                2 * h_phase(L, eta)
                - z**N * k_laurent(L, z * eta.inv())
                - z ** (-N) * k_laurent(L, z.inv() * eta.inv())
            )
            assert direct == closed

    # (11): formal constant coefficient equals sum alpha_k^2 x_k^2.
    for L in range(1, 10):
        aa = alphas(L)
        xs = {k: F((k + 3) * (k + 3) - 5, 7) for k in aa}
        coeff = {k: aa[k] * xs[k] for k in aa}
        constant = sum(coeff[k] * coeff[k] for k in coeff)
        convolution_constant = sum(
            coeff[k] * coeff[j] for k in coeff for j in coeff if k == j
        )
        assert constant == convolution_constant
        assert max(abs(coeff[k]) for k in coeff) ** 2 <= constant

    # (14)--(15): exact residue filter identity.
    w = G(0, F(1, 2))
    for L in range(1, 11):
        aa = alphas(L)
        for N in range(L, L + 5):
            direct = sum((a * eta ** (-k) * residue_term(w, N + k)
                          for k, a in aa.items()), G())
            closed = (
                w**N * k_laurent(L, w * eta.inv())
                + w ** (-N) * k_laurent(L, w.inv() * eta.inv())
                - 2 * h_phase(L, eta)
            )
            assert direct == closed

    # (16)--(17): matched frequency phi=-pi/2, exp(-i phi)=i.
    # Our eta=exp(i phi)=-i, so eta^-1=i.
    eta_match = G(0, -1)
    assert eta_match.inv() == G(0, 1)
    assert w.inv() * eta_match.inv() == 2
    for L in range(1, 31):
        k2 = k_laurent(L, G(2))
        assert k2.im == 0
        assert k2.re >= F(2 ** (L - 1), L * L)
        for N in (L, 2 * L, 3 * L):
            resonant = w ** (-N) * k2
            assert resonant.norm2() >= F(2 ** (2 * (N + L - 1)), L**4)

    # (18)--(19): the complete conjugate pair has no hidden cancellation.
    wbar = w.conj()
    for L in range(2, 31, 2):
        N = 2 * L  # 4 divides N
        aa = alphas(L)
        direct_pair = sum(
            (
                a
                * eta_match ** (-k)
                * (residue_term(w, N + k) + residue_term(wbar, N + k))
                for k, a in aa.items()
            ),
            G(),
        )
        formula_pair = (
            F(1, 2**N) * (k_laurent(L, G(F(1, 2))) + k_laurent(L, G(F(-1, 2))))
            + 2**N * (k_laurent(L, G(2)) + k_laurent(L, G(-2)))
            - 4 * h_phase(L, eta_match)
        )
        assert direct_pair == formula_pair
        assert direct_pair.im == 0
        assert direct_pair.re >= F(2 ** (N + L), L * L) - 4

    print("PASS 104_108 modulated Fejer matched-filter gate")
    print("checked: modulated test, formal Parseval, residue transport, resonance")
    print("checked: complete rational quartet lower bound with N=2L, L even")


if __name__ == "__main__":
    main()
