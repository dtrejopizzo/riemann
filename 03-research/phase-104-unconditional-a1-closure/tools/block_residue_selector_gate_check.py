#!/usr/bin/env python3
"""Exact checks for 104_106 (Fraction + Gaussian rationals only)."""

from fractions import Fraction as F
from itertools import product


class G:
    def __init__(self, re=0, im=0):
        self.re = F(re)
        self.im = F(im)

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
        return G(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    __rmul__ = __mul__

    def inv(self):
        den = self.re * self.re + self.im * self.im
        assert den != 0
        return G(self.re / den, -self.im / den)

    def __truediv__(self, other):
        return self * as_g(other).inv()

    def __pow__(self, n):
        if n < 0:
            return (self.inv()) ** (-n)
        out = G(1)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def __eq__(self, other):
        other = as_g(other)
        return self.re == other.re and self.im == other.im

    def __repr__(self):
        return f"G({self.re}, {self.im})"


def as_g(x):
    return x if isinstance(x, G) else G(x)


def poly(coeffs, z):
    out = G(0)
    power = G(1)
    for a in coeffs:
        out += a * power
        power *= z
    return out


def residue_term(w, n):
    return w**n + w ** (-n) - 2


def fejer_laurent(w, n):
    out = G(n)
    for d in range(1, n):
        out += (n - d) * (w**d + w ** (-d))
    return out


def quartet_li(w, n):
    """4 - 2 Re(w^n+w^-n), an exact rational for rational Gaussian w."""
    return F(4) - 2 * (w**n + w ** (-n)).re


def main():
    w = G(0, F(1, 2))
    rho = (G(1) - w).inv()
    assert rho == G(F(4, 5), F(2, 5))

    # (3): F_n(w)/[rho(rho-1)] = w^n+w^-n-2.
    for n in range(1, 31):
        lhs = fejer_laurent(w, n) / (rho * (rho - 1))
        assert lhs == residue_term(w, n)

    # (5): arbitrary finite filter.
    for N in range(1, 8):
        for coeffs in ([F(1), F(2), F(3)], [F(2, 5), F(0), F(7, 3), F(1)]):
            direct = sum((a * residue_term(w, N + j) for j, a in enumerate(coeffs)), G())
            filtered = (
                w**N * poly(coeffs, w)
                + w ** (-N) * poly(coeffs, w.inv())
                - 2 * sum(coeffs)
            )
            assert direct == filtered

    # Box and one-sided triangular formulas (7)--(8).
    for L in range(1, 11):
        box = [F(1, L)] * L
        tri = [F(2 * (L - j), L * (L + 1)) for j in range(L)]
        assert sum(box) == 1 and sum(tri) == 1
        for N in range(1, 8):
            for coeffs in (box, tri):
                direct = sum((a * residue_term(w, N + j) for j, a in enumerate(coeffs)), G())
                closed = w**N * poly(coeffs, w) + w ** (-N) * poly(coeffs, w.inv()) - 2
                assert direct == closed

    # Symmetric Fejer formula (9)--(10).
    for L in range(1, 9):
        weights = {j: F(L - abs(j), L * L) for j in range(-L + 1, L)}
        assert sum(weights.values()) == 1
        k_w = sum((a * w**j for j, a in weights.items()), G())
        assert k_w == sum((a * w ** (-j) for j, a in weights.items()), G())
        for N in range(L, L + 5):
            direct = sum((a * residue_term(w, N + j) for j, a in weights.items()), G())
            closed = k_w * (w**N + w ** (-N)) - 2
            assert direct == closed

    # Selector dualities (14)--(15) on exact rational samples.
    samples = [F(-3, 2), F(0), F(7, 5), F(-9, 4), F(2)]
    cube_values = []
    for bits in product((F(0), F(1)), repeat=len(samples)):
        cube_values.append(sum(a * x for a, x in zip(bits, samples)))
    assert max(cube_values) == sum(max(F(0), x) for x in samples)
    assert max(samples) == max(sum(a * x for a, x in zip(bits, samples))
                               for bits in product((F(0), F(1)), repeat=len(samples))
                               if sum(bits) == 1)

    # Rational quartet falsifier (21)--(22), arbitrarily far boxes.
    for k in range(0, 31):
        N = 4 * k + 2
        qn = quartet_li(w, N)
        assert qn > 2 ** (N + 1)
        box_sum = sum(quartet_li(w, N + j) for j in range(4))
        expected = F(16) - 6 * 2**N + F(3, 2) * F(1, 2**N)
        assert box_sum == expected
        assert box_sum < 0

    # Every deterministic block [L^2,L^2+L-1], L>=4, contains a
    # q_n-positive class n=2 mod 4 in its last four positions.
    for L in range(4, 101):
        lo, hi = L * L, L * L + L - 1
        candidates = [n for n in range(max(lo, hi - 3), hi + 1) if n % 4 == 2]
        assert len(candidates) == 1
        n = candidates[0]
        assert quartet_li(w, n) > 2 ** (n + 1)

    print("PASS 104_106 block-residue selector gate")
    print("checked: residue/filter identities, box/Cesaro/Fejer, selector duality")
    print("checked: signed four-block falsifier through N=122 and deterministic blocks")


if __name__ == "__main__":
    main()
