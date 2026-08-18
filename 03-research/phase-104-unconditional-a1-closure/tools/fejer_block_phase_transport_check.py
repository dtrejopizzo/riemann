#!/usr/bin/env python3
"""Exact checks for 104_107, Fejer block phase-transport gate.

All algebraic checks use Fraction-valued Gaussian rationals.  The analytic
total-variation estimate is proved in the accompanying document and is not
replaced here by floating-point quadrature.
"""

from fractions import Fraction as F


class G:
    """Gaussian rational with exact arithmetic."""

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
        if d == 0:
            raise ZeroDivisionError
        return G(self.re / d, -self.im / d)

    def __truediv__(self, other):
        other = other if isinstance(other, G) else G(other)
        return self * other.inv()

    def __pow__(self, exponent):
        if exponent < 0:
            return (self.inv()) ** (-exponent)
        out, base, n = G(1), self, exponent
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out

    def __eq__(self, other):
        other = other if isinstance(other, G) else G(other)
        return self.re == other.re and self.im == other.im

    def __repr__(self):
        return f"G({self.re}, {self.im})"


def triangular_weights(length):
    return {
        k: F(length - abs(k), length * length)
        for k in range(-length + 1, length)
    }


def block_transform_direct(z, center, length):
    return sum(
        (weight * (z ** (center + k))
         for k, weight in triangular_weights(length).items()),
        G(0),
    )


def block_transform_closed(z, center, length):
    quotient = (G(1) - z**length) / (length * (G(1) - z))
    return z ** (center - length + 1) * quotient**2


def fejer_laurent(w, degree):
    total = G(degree)
    for d in range(1, degree):
        total += (degree - d) * (w**d + w ** (-d))
    return total


def check_weight_bookkeeping():
    for length in range(1, 31):
        weights = triangular_weights(length)
        assert sum(weights.values(), F(0)) == 1
        assert sum((F(k) * a for k, a in weights.items()), F(0)) == 0
        assert min(weights) == -length + 1
        assert max(weights) == length - 1


def check_closed_transform():
    test_points = (G(F(1, 3), F(1, 5)), G(F(-2, 5), F(1, 7)), G(0, F(1, 2)))
    for z in test_points:
        for length in range(1, 13):
            for center in (length, 2 * length + 1, 2 * length + 3):
                direct = block_transform_direct(z, center, length)
                closed = block_transform_closed(z, center, length)
                assert direct == closed, (z, center, length, direct, closed)


def check_residue_transport_identity():
    w = G(0, F(1, 2))
    rho = G(1) / (G(1) - w)
    assert rho == G(F(4, 5), F(2, 5))
    for length in range(1, 10):
        center = 2 * length + 1
        weights = triangular_weights(length)
        direct = G(0)
        for k, weight in weights.items():
            degree = center + k
            direct += weight * fejer_laurent(w, degree) / (rho * (rho - 1))
        transported = (
            block_transform_closed(w, center, length)
            + block_transform_closed(w.inv(), center, length)
            - 2
        )
        assert direct == transported, (length, direct, transported)


def signed_quartet_formula(length, center):
    assert length % 4 == 0
    w = G(0, F(1, 2))
    transported = (
        block_transform_closed(w, center, length)
        + block_transform_closed(w.inv(), center, length)
    )
    c_l = F((2**length - 1) ** 2, 2 ** (2 * length) * length * length)
    if center == 2 * length + 1:
        expected_real = F(12, 25) * c_l * (
            F(2 ** (3 * length)) - F(1, 2 ** (length + 2))
        )
    elif center == 2 * length + 3:
        expected_real = -F(12, 25) * c_l * (
            F(2 ** (3 * length + 2)) - F(1, 2 ** (length + 4))
        )
    else:
        raise AssertionError("unexpected center")
    assert transported.re == expected_real
    return transported, expected_real


def check_two_signed_exponential_defects():
    for length in range(4, 45, 4):
        plus, plus_real = signed_quartet_formula(length, 2 * length + 1)
        minus, minus_real = signed_quartet_formula(length, 2 * length + 3)
        assert plus_real > 2  # quartet B-defect -Q = 2 Re(T)-4 > 0
        assert minus_real < 0
        q_plus = F(4) - 2 * plus.re
        q_minus = F(4) - 2 * minus.re
        b_defect_plus = -q_plus
        b_defect_minus = -q_minus
        assert b_defect_plus > 0
        assert b_defect_minus < 0


def check_no_interior_filter_zero():
    # Exact instance of the general fact: if |w|<1, then w^L != 1.
    w = G(0, F(1, 2))
    assert w.norm2() < 1
    for length in range(1, 101):
        assert G(1) - w**length != G(0)


def main():
    check_weight_bookkeeping()
    check_closed_transform()
    check_residue_transport_identity()
    check_two_signed_exponential_defects()
    check_no_interior_filter_zero()
    print("PASS: triangular weights are positive, normalized, and centered")
    print("PASS: exact Fejer block transform for 1 <= L <= 12")
    print("PASS: averaged Laurent-Fejer residue equals T(w)+T(w^-1)-2")
    print("PASS: w=i/2 gives both exponential signs for 4 <= L <= 44")
    print("PASS: block multiplier has no zero at the interior falsifier")
    print("STOP: O(N/L+1) phase variation does not transport through residues")


if __name__ == "__main__":
    main()
