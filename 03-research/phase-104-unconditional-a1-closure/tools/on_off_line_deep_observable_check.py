#!/usr/bin/env python3
"""Exact/diagnostic checks for 104_81.

Exact checks use integers or Fraction.  The final density table is only a
finite diagnostic; the limits themselves are proved in 104_81.
"""

from fractions import Fraction
from math import exp, isqrt, log, log1p, sqrt


def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def mobius(n):
    x = n
    count = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def necklace(d, alphabet):
    total = sum(mobius(e) * alphabet ** (d // e) for e in divisors(d))
    assert total % d == 0
    return total // d


def pi_plus(d):
    value = necklace(d, 4) + necklace(d, 1)
    if d % 2 == 0:
        value += necklace(d // 2, 4)
    if d % 4 == 0:
        value -= necklace(d // 4, 16)
    return value


def pi_minus(d):
    return (
        necklace(d, 6)
        + necklace(d, 1)
        - necklace(d, 3)
        - necklace(d, 2)
    )


def psi_from_pi(k, pi):
    return sum(d * pi(d) for d in divisors(k))


def psi_plus_closed(k):
    oscillatory = 0
    if k % 2 == 0:
        oscillatory = 2 * (2 ** k) * ((-1) ** (k // 2))
    return 4 ** k + 1 - oscillatory


def psi_minus_closed(k):
    return 6 ** k + 1 - 3 ** k - 2 ** k


def zplus(t):
    return (1 + 4 * t * t) / ((1 - t) * (1 - 4 * t))


def zminus(t):
    return ((1 - 3 * t) * (1 - 2 * t)) / ((1 - t) * (1 - 6 * t))


def cos_quarter_turn(n):
    return (1, 0, -1, 0)[n % 4]


def critical_ell(n):
    return 4 - 4 * cos_quarter_turn(n)


def exterior_ell(n, r):
    return Fraction(4) - 2 * (r ** n + r ** (-n)) * cos_quarter_turn(n)


def harmonic_number(x):
    return sum(1.0 / n for n in range(1, x + 1))


def exterior_deep_density(x, r):
    """Stable log-domain evaluation of the deep event for 4 | n."""
    log_r = log(float(r))
    threshold = sqrt(x)
    mass = 0.0
    for n in range(4, x + 1, 4):
        a = n * log_r
        # b = log(2(R^n+R^-n))
        b = log(2.0) + a + log1p(exp(-2.0 * a))
        correction = 4.0 + log(n + 1.0)
        ratio = correction * exp(-b)
        if ratio >= 1.0:
            continue
        log_left = b + log1p(-ratio)
        if log_left >= threshold:
            mass += 1.0 / n
    return mass / harmonic_number(x)


def main():
    # Finite on-line control: exact cycle and no negative value.
    critical = [critical_ell(n) for n in range(1, 17)]
    assert set(critical) == {0, 4, 8}
    assert min(critical) == 0

    # Finite off-line control: only one residue class is negative.
    r = Fraction(201, 200)
    for n in range(1, 81):
        value = exterior_ell(n, r)
        if n % 4 == 0:
            assert value < 0
        else:
            assert value > 0

    # The exponential diagonal regulator is dominated for this R.
    rate = log(float(r)) - 0.01
    assert rate < 0.0
    diagonal_logs = [log(x) + x * rate for x in (1000, 5000, 10000)]
    assert diagonal_logs[0] > diagonal_logs[1] > diagonal_logs[2]

    # Both formal Euler products have nonnegative integral prime counts.
    plus_values = [pi_plus(d) for d in range(1, 81)]
    minus_values = [pi_minus(d) for d in range(1, 81)]
    assert all(isinstance(v, int) and v >= 0 for v in plus_values)
    assert all(isinstance(v, int) and v >= 0 for v in minus_values)

    # Logarithmic derivatives reproduce the claimed Mangoldt masses.
    for k in range(1, 61):
        assert psi_from_pi(k, pi_plus) == psi_plus_closed(k)
        assert psi_from_pi(k, pi_minus) == psi_minus_closed(k)

    # Exact functional equations at rational test points.
    for t in (Fraction(1, 10), Fraction(2, 7), Fraction(3, 20)):
        assert zplus(Fraction(1, 4) / t) == zplus(t)
    for t in (Fraction(1, 12), Fraction(2, 9), Fraction(3, 20)):
        assert zminus(Fraction(1, 6) / t) == zminus(t)

    # Diagnostic only: convergence to 1/8 is logarithmically slow.
    xs = (160_000, 640_000, 2_560_000)
    densities = [exterior_deep_density(x, r) for x in xs]
    assert 0.0 < densities[0] < densities[1] < densities[2] < 0.125

    print("PASS: critical quartet deep density = 0 exactly")
    print("PASS: exterior quartet has the predicted negative residue class")
    print("PASS: diagonal perturbation exponent log(R)-1/100 < 0")
    print("PASS: pi_d^+, pi_d^- are nonnegative for 1 <= d <= 80")
    print("PASS: both Mangoldt identities hold for 1 <= k <= 60")
    print("PASS: both rational functional equations hold exactly")
    print("pi_d^+ (d=1..8):", plus_values[:8])
    print("pi_d^- (d=1..8):", minus_values[:8])
    for x, density in zip(xs, densities):
        print(f"diagnostic X={x}: D_X={density:.12f}")
    print("THEOREM VALUES: on-line = 0, off-line quartet = 1/8,")
    print("                Euler off-line model = 1/4")


if __name__ == "__main__":
    main()

