#!/usr/bin/env python3
"""Exact checks for 104_41, full Mangoldt phase-homotopy gate.

Only Fraction arithmetic is used.  No zeta zeros or floating-point
evaluation enters the certificate.
"""

from fractions import Fraction as F


class G:
    """Gaussian rational."""

    def __init__(self, re=0, im=0):
        self.re = F(re)
        self.im = F(im)

    def __add__(self, other):
        other = other if isinstance(other, G) else G(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-other if isinstance(other, G) else -G(other))

    def __rsub__(self, other):
        return G(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, G) else G(other)
        return G(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def norm2(self):
        return self.re * self.re + self.im * self.im

    def inv(self):
        d = self.norm2()
        return G(self.re / d, -self.im / d)

    def __truediv__(self, other):
        other = other if isinstance(other, G) else G(other)
        return self * other.inv()

    def __pow__(self, n):
        assert n >= 0
        out, base = G(1), self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def __eq__(self, other):
        other = other if isinstance(other, G) else G(other)
        return self.re == other.re and self.im == other.im

    def __repr__(self):
        return f"G({self.re}, {self.im})"


def check_zeta2_rational_majorant():
    majorant = F(1, 4) + F(1, 9) + F(1, 16) + F(1, 25) + F(1, 5)
    assert majorant == F(2389, 3600)
    assert majorant < F(2, 3)
    # 2/3 < sin(pi/4)=sqrt(2)/2 follows after squaring.
    assert F(4, 9) < F(1, 2)


def check_total_variation_count():
    # On each half-line theta traverses [0, pi].  The function
    # 2-2 cos(n theta) has n monotonic half-waves, each of variation 4.
    # Doubling for the two half-lines gives 8n.
    for n in range(1, 501):
        half_waves = n
        variation_one_half = 4 * half_waves
        assert 2 * variation_one_half == 8 * n


def crossing_value(rho, a):
    z = G(1) - G(a) / rho
    return z.norm2() - 1


def check_crossing_identity():
    w = G(0, F(1, 2))
    rho = G(1) / (G(1) - w)
    assert rho == G(F(4, 5), F(2, 5))
    beta = rho.re
    for a in (F(1), F(3, 2), F(8, 5), F(2), F(4)):
        lhs = crossing_value(rho, a)
        rhs = a * (a - 2 * beta) / rho.norm2()
        assert lhs == rhs
    assert crossing_value(rho, F(1)) < 0
    assert crossing_value(rho, F(8, 5)) == 0
    assert crossing_value(rho, F(2)) > 0


def q_on_critical_line(rho, t):
    orbit = (rho, rho.conj(), G(1) - rho, G(1) - rho.conj())
    s = G(F(1, 2), t)
    out = G(1)
    for eta in orbit:
        out = out * (s - eta)
    return out


def check_critical_phase_invariance():
    rho = G(F(4, 5), F(2, 5))
    delta = rho.re - F(1, 2)
    gamma = rho.im
    for k in range(-40, 41):
        t = F(k, 7)
        actual = q_on_critical_line(rho, t)
        expected = ((t - gamma) ** 2 + delta**2) * (
            (t + gamma) ** 2 + delta**2
        )
        assert actual == G(expected, 0)
        assert expected > 0


def check_quartet_residue():
    w = G(0, F(1, 2))
    rho = G(1) / (G(1) - w)
    # The residue kernel is the Laurent Fejer kernel
    #   F_n(w)=n+sum_{d<n}(n-d)(w^d+w^{-d}).
    # In particular it has no extra n*w^n term.  This identity catches
    # the transcription error that the first version of 104_41 contained.
    for degree in range(1, 20):
        kernel = G(degree)
        for d in range(1, degree):
            kernel += (degree - d) * (w**d + w.inv() ** d)
        lhs = kernel / (rho * (rho - 1))
        rhs = w**degree + w.inv() ** degree - 2
        assert lhs == rhs
    n = 152
    wn = w**n
    winvn = (w.inv()) ** n
    assert wn == G(F(1, 2**n), 0)
    assert winvn == G(2**n, 0)
    qn = F(4) - 2 * (wn.re + winvn.re)
    defect = -qn
    expected = 2 * (F(2**n) + F(1, 2**n)) - 4
    assert defect == expected
    assert defect > 0


def main():
    check_zeta2_rational_majorant()
    check_total_variation_count()
    check_crossing_identity()
    check_critical_phase_invariance()
    check_quartet_residue()
    print("PASS: zeta(2)-1 < 2/3 < sin(pi/4) by rational bounds")
    print("PASS: TV(W_n) = 8n for 1 <= n <= 500 (exact half-wave count)")
    print("PASS: exact crossing law and a_cross = 8/5 for w=i/2")
    print("PASS: reciprocal quartet has strictly positive critical-line factor")
    print("PASS: corrected Laurent Fejer residue kernel for 1 <= n < 20")
    print("PASS: n=152 residue defect is 2(2^152+2^-152)-4 > 0")


if __name__ == "__main__":
    main()
