#!/usr/bin/env python3
"""Finite checks for 104_56.

This script checks only finite algebra and periodic counts:

* the orientation u = rho/(rho-1) on the rational quartet u=2i;
* the quartet contribution Q_4=-225/8;
* the Fejer identity for the dominant phase family;
* a periodic example whose possible negative-density bound is below 1%;
* syndeticity of the corresponding periodic return set.

The compact-group theorem and the analytic remainder estimates are proved
in 104_56; floating-point output here is diagnostic, not a certificate for
RH or A1.
"""

from fractions import Fraction
from math import asin, cos, floor, pi, sin, sqrt


Q = Fraction
Pair = tuple[Fraction, Fraction]


def cadd(z: Pair, w: Pair) -> Pair:
    return z[0] + w[0], z[1] + w[1]


def csub(z: Pair, w: Pair) -> Pair:
    return z[0] - w[0], z[1] - w[1]


def cmul(z: Pair, w: Pair) -> Pair:
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def cdiv(z: Pair, w: Pair) -> Pair:
    den = w[0] * w[0] + w[1] * w[1]
    return (
        (z[0] * w[0] + z[1] * w[1]) / den,
        (z[1] * w[0] - z[0] * w[1]) / den,
    )


def cpow(z: Pair, n: int) -> Pair:
    out = (Q(1), Q(0))
    base = z
    k = n
    while k:
        if k & 1:
            out = cmul(out, base)
        base = cmul(base, base)
        k //= 2
    return out


def rational_orientation_check() -> None:
    one = (Q(1), Q(0))
    u = (Q(0), Q(2))
    rho = cdiv(u, csub(u, one))
    assert rho == (Q(4, 5), Q(-2, 5))
    assert rho[0] > Q(1, 2)

    mate = csub(one, rho)
    u_mate = cdiv(mate, csub(mate, one))
    inv_u = cdiv(one, u)
    assert u_mate == inv_u == (Q(0), Q(-1, 2))

    orbit_u = [
        (Q(0), Q(2)),
        (Q(0), Q(-2)),
        (Q(0), Q(1, 2)),
        (Q(0), Q(-1, 2)),
    ]
    power_sum = (Q(0), Q(0))
    for point in orbit_u:
        power_sum = cadd(power_sum, cpow(point, 4))
    q4 = Q(4) - power_sum[0]
    assert power_sum[1] == 0
    assert q4 == Q(-225, 8)


def fejer_value(k_order: int, x: float) -> float:
    den = sin(x / 2.0)
    if abs(den) < 1.0e-15:
        return float(k_order)
    num = sin(k_order * x / 2.0)
    return (num / den) ** 2 / k_order


def fejer_identity_check() -> None:
    k_order = 64
    q_modulus = 1009
    for n in (0, 1, 17, 201, 503):
        x = 2.0 * pi * n / q_modulus
        lhs = 2.0 * sum(
            (k_order - k) * cos(k * x) for k in range(1, k_order)
        )
        rhs = k_order * (fejer_value(k_order, x) - 1.0)
        scale = max(1.0, abs(lhs), abs(rhs))
        assert abs(lhs - rhs) <= 2.0e-10 * scale


def sparse_periodic_return_check() -> tuple[float, float, int]:
    k_order = 4096
    q_modulus = 1_000_003
    threshold_angle = asin(1.0 / sqrt(k_order))
    radius = floor(q_modulus * threshold_angle / pi)

    # F_K >= 1 implies circular distance to 0 is at most this radius.
    possible_count = 2 * radius + 1
    possible_density = possible_count / q_modulus
    analytic_bound = 2.0 * threshold_angle / pi + 1.0 / q_modulus
    assert possible_density <= analytic_bound + 1.0e-15
    assert analytic_bound < 0.01

    # Count the actual strict return set using the O(1) Fejer formula.
    returns: list[int] = []
    for n in range(q_modulus):
        x = 2.0 * pi * n / q_modulus
        if fejer_value(k_order, x) > 1.0 + 1.0e-11:
            returns.append(n)
    assert returns
    assert len(returns) <= possible_count

    gaps = [
        returns[j + 1] - returns[j] for j in range(len(returns) - 1)
    ]
    gaps.append(q_modulus + returns[0] - returns[-1])
    max_gap = max(gaps)
    assert max_gap < q_modulus

    # The synthetic zeros rho=u/(u-1) lie in 1/2<Re rho<1.
    theta = 2.0 * pi / q_modulus
    r_outer = 1.0 + 0.25 * theta * theta
    assert 1.0 < r_outer < 1.0 / cos(theta)
    assert r_outer * cos(theta) < 1.0

    return len(returns) / q_modulus, analytic_bound, max_gap


def main() -> None:
    rational_orientation_check()
    fejer_identity_check()
    density, bound, max_gap = sparse_periodic_return_check()
    print("rational orientation and Q_4=-225/8: PASS")
    print("finite Fejer identity: PASS")
    print(
        "periodic dominant returns: "
        f"density={density:.8f}, bound={bound:.8f}, max_gap={max_gap}"
    )
    print("density below 1% and periodic syndeticity: PASS")


if __name__ == "__main__":
    main()
