#!/usr/bin/env python3
"""Exact certificates for the D.84 bilateral boundary audit."""

from fractions import Fraction


def main():
    # Rational unitary colligation.
    T, G, H, R = (Fraction(3, 5), Fraction(4, 5),
                   Fraction(-4, 5), Fraction(3, 5))

    # Finite bilateral energy telescopes exactly.
    inputs = {
        -2: Fraction(1), -1: Fraction(-2), 0: Fraction(3, 2),
        1: Fraction(1, 3), 2: Fraction(-1, 2)
    }
    x = {-2: Fraction(7, 4)}
    ys = {}
    for n in range(-2, 3):
        u = inputs[n]
        ys[n] = H * x[n] + R * u
        x[n + 1] = T * x[n] + G * u
        assert x[n] ** 2 + u ** 2 == x[n + 1] ** 2 + ys[n] ** 2
    lhs = sum(ys[n] ** 2 - inputs[n] ** 2 for n in range(-2, 3))
    rhs = x[-2] ** 2 - x[3] ** 2
    assert lhs == rhs

    # Finite prime feedthrough is product (1-1/p) and decreases.
    primes = (2, 3, 5, 7, 11, 13)
    products = []
    c = Fraction(1)
    for p in primes:
        c *= Fraction(p - 1, p)
        products.append(c)
    assert all(products[j + 1] < products[j]
               for j in range(len(products) - 1))
    assert products[-1] == Fraction(192, 1001)

    # Any map through two jets has matrix rank at most two.  Its 3x3
    # determinant vanishes, whereas an identity edge has rank three.
    A = [[Fraction(1), Fraction(2)],
         [Fraction(0), Fraction(1)],
         [Fraction(3), Fraction(-1)]]
    M = [[Fraction(2), Fraction(0), Fraction(1)],
         [Fraction(1), Fraction(1), Fraction(-2)]]
    E = [[sum(A[i][k] * M[k][j] for k in range(2))
          for j in range(3)] for i in range(3)]

    def det3(a):
        return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
                - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
                + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))

    assert det3(E) == 0
    identity3 = [[Fraction(1 if i == j else 0) for j in range(3)]
                 for i in range(3)]
    assert det3(identity3) == 1

    # Killing two polar scalars does not kill an independent residual state.
    polar_minus = polar_plus = Fraction(0)
    residual_minus = Fraction(2)
    residual_plus = Fraction(3)
    boundary = (polar_minus ** 2 + residual_minus ** 2
                - polar_plus ** 2 - residual_plus ** 2)
    assert boundary == -5 != 0

    # Local v_r Toeplitz block is nonnormal.  The (0,1) entry of
    # r^2(P_h-P_e0), for r=3/5 and h=(4/5)(1,r,...), is nonzero.
    rr = Fraction(3, 5)
    h0 = Fraction(4, 5)
    h1 = h0 * rr
    nonnormal_01 = rr * rr * h0 * h1
    assert nonnormal_01 == Fraction(432, 3125) != 0

    print("D84 bilateral/Tate-boundary certificates: PASS")
    print("energy boundary:", lhs, rhs)
    print("finite prime feedthroughs:", products)
    print("nonpolar boundary after jet cancellation:", boundary)
    print("local Toeplitz nonnormal (0,1):", nonnormal_01)


if __name__ == "__main__":
    main()
