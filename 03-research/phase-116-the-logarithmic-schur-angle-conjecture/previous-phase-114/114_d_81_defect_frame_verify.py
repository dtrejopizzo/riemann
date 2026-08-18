#!/usr/bin/env python3
"""Exact scalar certificates for the D.81 defect-frame audit."""

from fractions import Fraction


def main():
    # Primitive average at R=2 log 2: eta=4/5.
    a = Fraction(4, 5)
    d2 = 1 - a * a
    assert d2 == Fraction(9, 25)

    # Parseval defect telescope: sum_{j<N}(1-a^2)a^(2j)+a^(2N)=1.
    for n in (1, 2, 5, 12):
        bulk = sum(d2 * a ** (2 * j) for j in range(n))
        assert bulk + a ** (2 * n) == 1

    # Diagonal intertwiner blows up when lambda/a^2>1.
    lam = Fraction(81, 100)
    growth = lam / (a * a)
    assert growth == Fraction(81, 64) > 1
    ratios_sq = [
        (1 - lam) / (4 * d2) * growth ** j
        for j in range(8)
    ]
    assert all(ratios_sq[j + 1] > ratios_sq[j]
               for j in range(len(ratios_sq) - 1))

    # Exact Halmos positive-graph counterexample with rational square roots.
    # lambda=9/25, sqrt(lambda)=3/5, sqrt(1-lambda)=4/5.
    lam2 = Fraction(9, 25)
    sqrt_lam2 = Fraction(3, 5)
    sqrt_one_minus = Fraction(4, 5)
    q = Fraction(1)
    p = Fraction(3, 8)
    landing = sqrt_one_minus * p - sqrt_lam2 * q / 2
    assert landing == 0
    schur_mass = lam2 * q * q / 4
    assert schur_mass == Fraction(9, 100) > 0

    # A finite matrix commutator models the cutoff annulus.
    P = ((Fraction(1), Fraction(0)),
         (Fraction(0), Fraction(0)))
    theta = ((Fraction(0), Fraction(1)),
             (Fraction(1), Fraction(0)))

    def mul(x, y):
        return tuple(tuple(sum(x[i][k] * y[k][j] for k in range(2))
                           for j in range(2)) for i in range(2))

    pt = mul(P, theta)
    tp = mul(theta, P)
    comm = tuple(tuple(pt[i][j] - tp[i][j] for j in range(2))
                 for i in range(2))
    assert comm != ((0, 0), (0, 0))

    print("D81 defect-frame certificates: PASS")
    print("defect square, diagonal growth:", d2, growth)
    print("positive-graph landing/mass:", landing, schur_mass)


if __name__ == "__main__":
    main()
