#!/usr/bin/env python3
"""Exact checks for 104_59 (pre-log majorisation gate).

All polynomial and interval decisions use ``Fraction``.  The checker verifies
that the first genuinely curved Laguerre test (n=4) reverses Schur direction,
including on logarithms of integers, and that the real divisor selector has
opposite first-moment orientations at N=2 and N=30.

It does not evaluate A1, Li coefficients, zeta zeros, or RH.
"""

from fractions import Fraction as F


def poly_eval(coeffs: tuple[F, ...], x: F) -> F:
    out = F(0)
    for coefficient in reversed(coeffs):
        out = out * x + coefficient
    return out


def poly_scale_argument(coeffs: tuple[F, ...], scale: int) -> dict[int, F]:
    """Coefficients of p(scale*l) as a polynomial in the formal variable l."""
    return {degree: coefficient * scale**degree
            for degree, coefficient in enumerate(coeffs)
            if coefficient}


def poly_linear_combination(
    terms: tuple[tuple[int, dict[int, F]], ...]
) -> dict[int, F]:
    out: dict[int, F] = {}
    for multiplier, polynomial in terms:
        for degree, coefficient in polynomial.items():
            out[degree] = out.get(degree, F(0)) + multiplier * coefficient
    return {degree: coefficient for degree, coefficient in out.items() if coefficient}


def laguerre_schur_reversal() -> None:
    # phi_4(x)=L_3^(1)(x)-4=-6x+2x^2-x^3/6.
    phi4 = (F(0), F(-6), F(2), F(-1, 6))

    # For a spread (a-h,a+h) versus (a,a), the former majorizes the latter.
    # At a=1,h=1 Schur-convex orientation is positive.
    low = poly_eval(phi4, F(0)) + poly_eval(phi4, F(2)) \
        - 2 * poly_eval(phi4, F(1))
    assert low == 3

    # At a=5,h=1 the same majorization has the opposite orientation.
    high = poly_eval(phi4, F(4)) + poly_eval(phi4, F(6)) \
        - 2 * poly_eval(phi4, F(5))
    assert high == -1

    # The same reversal lies on the log-integer lattice.  With l=log 2:
    # (log 1,log 4) majorizes (log 2,log 2), giving l^2(4-l).
    low_log = poly_linear_combination((
        (1, poly_scale_argument(phi4, 0)),
        (1, poly_scale_argument(phi4, 2)),
        (-2, poly_scale_argument(phi4, 1)),
    ))
    assert low_log == {2: F(4), 3: F(-1)}

    # (log 64,log 256) majorizes (log 128,log 128), giving
    # l^2(4-7l), which is negative because e<3 and 3^4<2^7.
    high_log = poly_linear_combination((
        (1, poly_scale_argument(phi4, 6)),
        (1, poly_scale_argument(phi4, 8)),
        (-2, poly_scale_argument(phi4, 7)),
    ))
    assert high_log == {2: F(4), 3: F(-7)}
    assert 3**4 < 2**7


def mass_vector_permutation_obstruction() -> None:
    # A Schur functional of an unlabeled probability vector is invariant under
    # permutations.  For supports (0,l), phi_2(x)=L_1^(1)(x)-2=-x.
    p = (F(3, 4), F(1, 4))
    q = tuple(reversed(p))
    assert sorted(p) == sorted(q)

    # Record the coefficient of the formal positive number l=log 2.
    moment_p_over_l = -p[1]
    moment_q_over_l = -q[1]
    assert moment_p_over_l == F(-1, 4)
    assert moment_q_over_l == F(-3, 4)
    assert moment_p_over_l - moment_q_over_l == F(1, 2)


def log_interval(n: int, terms: int = 48) -> tuple[F, F]:
    """Outward rational interval for log(n), using the atanh series."""
    if n <= 0:
        raise ValueError("n must be positive")
    z = F(n - 1, n + 1)
    partial = F(0)
    for j in range(terms + 1):
        partial += F(2) * z ** (2 * j + 1) / (2 * j + 1)
    remainder = F(2) * z ** (2 * terms + 3) / (
        (2 * terms + 3) * (1 - z * z)
    )
    return partial, partial + remainder


def interval_add(x: tuple[F, F], y: tuple[F, F]) -> tuple[F, F]:
    return x[0] + y[0], x[1] + y[1]


def interval_sub(x: tuple[F, F], y: tuple[F, F]) -> tuple[F, F]:
    return x[0] - y[1], x[1] - y[0]


def interval_mul(x: tuple[F, F], y: tuple[F, F]) -> tuple[F, F]:
    products = (x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1])
    return min(products), max(products)


def actual_divisor_selector_reversal() -> None:
    # For N=2, 2 log(N)(E log D - log(N)/2)=(log 2)^2>0.
    log2 = log_interval(2)
    q2 = interval_mul(log2, log2)
    assert q2[0] > 0

    # For squarefree N=30, the same numerator is
    # a^2+b^2+c^2-2ab-2ac-2bc, a=log2,b=log3,c=log5.
    a, b, c = log_interval(2), log_interval(3), log_interval(5)
    squares = interval_add(interval_mul(a, a), interval_mul(b, b))
    squares = interval_add(squares, interval_mul(c, c))
    pairs = interval_add(interval_mul(a, b), interval_mul(a, c))
    pairs = interval_add(pairs, interval_mul(b, c))
    q30 = interval_sub(squares, (2 * pairs[0], 2 * pairs[1]))
    assert q30[1] < 0


def main() -> None:
    laguerre_schur_reversal()
    mass_vector_permutation_obstruction()
    actual_divisor_selector_reversal()
    print("pre-log majorisation gate: PASS")
    print("  phi_4 Schur spread: +3 at center 1, -1 at center 5")
    print("  log-integer spreads: l^2(4-l)>0 and l^2(4-7l)<0")
    print("  probability-vector permutation loses the labeled Laguerre moment")
    print("  real divisor selector vs uniform: positive at N=2, negative at N=30")
    print("  no claim about A1 or RH")


if __name__ == "__main__":
    main()
