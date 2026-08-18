#!/usr/bin/env python3
"""Finite checks for 104_77 (not a proof of the asymptotic statements)."""

from fractions import Fraction
from math import log, log1p, sqrt


def quartet(n: int) -> Fraction:
    """q_n for w=2i, evaluated exactly by residue class."""
    if n % 2:
        return Fraction(4)
    sign = 1 if n % 4 == 0 else -1
    return Fraction(4) - 2 * sign * (Fraction(2**n) + Fraction(1, 2**n))


def continued_ray(r: float) -> float:
    return (
        4.0 * r / (1.0 - r)
        + 8.0 * r * r / (1.0 + 4.0 * r * r)
        + 2.0 * r * r / (4.0 + r * r)
    )


def taylor_ray(r: Fraction, terms: int) -> Fraction:
    return sum((quartet(n) * r**n for n in range(1, terms + 1)), Fraction(0))


def deep_log_density(X: int) -> float:
    """Stable log-domain evaluation of the quartet deep event."""
    threshold = sqrt(X)
    harmonic = 0.0
    selected = 0.0
    for n in range(1, X + 1):
        weight = 1.0 / n
        harmonic += weight
        if n % 4:
            continue
        # -q_n = 2^(n+1) - 4 + 2^(1-n).  Evaluate
        # log(-q_n-log(n+1)) without ever forming 2^(n+1).
        if n < 32:
            neg_q = float(-quartet(n))
            if neg_q > 0.0 and log(neg_q - log(n + 1.0)) >= threshold:
                selected += weight
        else:
            lead_log = (n + 1) * log(2.0)
            relative_correction = (
                -4.0 + 2.0 ** (1 - n) - log(n + 1.0)
            ) * 2.0 ** (-(n + 1))
            event_log = lead_log + log1p(relative_correction)
            if event_log >= threshold:
                selected += weight
    return selected / harmonic


def main() -> None:
    # The rational continuation agrees with the Taylor series inside |z|<1/2.
    for r in (Fraction(1, 10), Fraction(1, 4), Fraction(2, 5)):
        exact_cont = continued_ray(float(r))
        approx = float(taylor_ray(r, 160))
        assert abs(exact_cont - approx) < 2e-12

    # It remains positive after crossing the convergence radius.
    for r in (0.1, 0.49, 0.51, 0.75, 0.9, 0.99):
        assert continued_ray(r) > 0.0

    # Exact signs and exponential size on residue classes.
    for n in range(4, 80, 4):
        assert quartet(n) < 0
        assert -quartet(n) > 2**n
    for n in range(2, 80, 4):
        assert quartet(n) > 0
    for n in range(1, 80, 2):
        assert quartet(n) == 4

    vals = [(X, deep_log_density(X)) for X in (10_000, 100_000, 1_000_000)]
    # Convergence is logarithmically slow, but the error must decrease and
    # the last value must already be close to 1/8.
    errs = [abs(v - 0.125) for _, v in vals]
    assert errs[2] < errs[1] < errs[0]
    assert errs[2] < 0.03

    print("quartet deep densities:", " ".join(f"X={x}: {v:.9f}" for x, v in vals))
    print("PASS 104_77: positive Euler ray, interior quartet, deep-tail density")


if __name__ == "__main__":
    main()
