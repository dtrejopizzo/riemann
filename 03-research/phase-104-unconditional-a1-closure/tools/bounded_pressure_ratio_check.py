#!/usr/bin/env python3
"""Numerical diagnostics for 104_72_BOUNDED_PRESSURE_RATIO_ATTACK.md.

This is a diagnostic checker, not a proof of the asymptotic theorems and
not a verification of RH.  It tests the exact finite identities, the
sharp sensitivity constant, the off-line quartet, and the diagonal scale.
"""

from __future__ import annotations

import math


def softplus(y: float) -> float:
    """Stable log(1+exp(y))."""
    return max(0.0, y) + math.log1p(math.exp(-abs(y)))


def g_tau(x: float, tau: float) -> float:
    return (softplus(-x) - softplus(-x - tau)) / tau


def log_ratio_from_delta(delta: float, tau: float) -> float:
    """log R_tau(C,Q), with delta=Q-C, evaluated stably."""
    return softplus(delta) - softplus(delta - tau)


def log_ratio_from_channels(c_value: float, q_value: float, tau: float) -> float:
    """Stable channel form of log R_tau(C,Q)."""
    return log_ratio_from_delta(q_value - c_value, tau)


def sensitivity(z: float, tau: float) -> float:
    q = math.exp(-tau)
    return (1.0 - q) * z / ((1.0 + z) * (1.0 + q * z))


def quartet_g(n: int, tau: float) -> float:
    """Fermi observable for 4-2 Re((2i)^n+(2i)^(-n))."""
    residue = n % 4
    if residue == 0:
        # For n above the floating-point exponential range the answer is
        # already 1 to machine precision.
        if n > 500:
            return 1.0
        qn = 4.0 - 2.0 * (2.0**n + 2.0 ** (-n))
    elif residue == 2:
        if n > 500:
            return 0.0
        qn = 4.0 + 2.0 * (2.0**n + 2.0 ** (-n))
    else:
        qn = 4.0
    return g_tau(qn + math.log(n + 1.0), tau)


def check_pressure_identities() -> None:
    for tau in (0.2, 1.0, 3.0):
        for x in (-100.0, -8.0, -0.3, 0.0, 2.0, 80.0):
            g = g_tau(x, tau)
            delta = -x
            lr = log_ratio_from_delta(delta, tau)
            assert -2e-14 <= g <= 1.0 + 2e-14
            assert math.isclose(tau * g, lr, rel_tol=2e-13, abs_tol=2e-13)
            ratio = math.exp(lr)
            assert 1.0 - 2e-14 <= ratio <= math.exp(tau) + 2e-13

        z_star = math.exp(tau / 2.0)
        sharp = math.tanh(tau / 4.0)
        assert math.isclose(
            sensitivity(z_star, tau), sharp, rel_tol=3e-15, abs_tol=3e-15
        )
        # A logarithmic grid confirms that the stationary value is maximal.
        grid_max = max(sensitivity(math.exp(k / 20.0), tau) for k in range(-800, 801))
        assert grid_max <= sharp * (1.0 + 2e-4)
        assert sharp / tau < 0.25


def check_rh_model_bound() -> None:
    # lambda_n=0 is an extremal model for the elementary RH-side estimate.
    tau = 1.3
    for length in (8, 30, 100, 300):
        start = length * length
        total = sum(g_tau(math.log(n + 1.0), tau) for n in range(start, start + length))
        bound = length / (tau * (length * length + 1.0))
        assert 0.0 <= total <= bound * (1.0 + 2e-14)


def check_common_shift_and_separation() -> None:
    tau = 1.1
    # R_tau depends only on Q-C, even when the common channel is huge.
    for common in (-1e12, -100.0, 0.0, 100.0, 1e12):
        for delta in (-30.0, -2.0, 0.0, 2.0, 30.0):
            shifted = log_ratio_from_channels(common, common + delta, tau)
            unshifted = log_ratio_from_channels(0.0, delta, tau)
            assert math.isclose(shifted, unshifted, rel_tol=0.0, abs_tol=2e-5)

    low_limit = 1.0
    high_limit = math.exp(tau)
    for a in (4.0, 8.0, 16.0, 32.0):
        low = math.exp(log_ratio_from_delta(-a, tau))
        high = math.exp(log_ratio_from_delta(a, tau))
        assert low >= low_limit and high <= high_limit
    assert abs(math.exp(log_ratio_from_delta(-32.0, tau)) - low_limit) < 1e-13
    assert abs(math.exp(log_ratio_from_delta(32.0, tau)) - high_limit) < 1e-12


def check_quartet() -> None:
    tau = 0.9
    errors = []
    for length in (20, 40, 80, 160, 320):
        start = length * length
        total = sum(quartet_g(n, tau) for n in range(start, start + length))
        density = total / length
        errors.append(abs(density - 0.25))
        assert 0.0 <= total <= length
    # The non-multiple-of-four contribution tends to zero and the counting
    # error is O(1/L).
    assert errors[-1] < 0.004
    assert errors[-1] <= errors[0] + 1e-14


def check_diagonal_scale() -> None:
    eta = 1.0 / 100.0 - math.log(200.0 / 199.0)
    assert eta > 0.0049
    assert eta < 0.0050

    for x in (70, 200, 500, 1000):
        eps = math.exp(-x / 100.0)
        exact_log = x * math.log((1.0 - eps) / eps)
        equivalent_log = x * (x / 100.0 + math.log1p(-eps))
        assert math.isclose(exact_log, equivalent_log, rel_tol=2e-15, abs_tol=2e-12)
        assert exact_log <= x * x / 100.0
        # The correction x*log(1-e^{-x/100}) tends to zero.
        if x == 1000:
            assert abs(exact_log - x * x / 100.0) < 0.05

    # Resolving an additive transition of size O(1) against a channel with
    # log-size X^2/100 costs exp(-X^2/100+O(1)).  Compare logarithms only.
    x = 1000.0
    log_relative_transition = -x * x / 100.0
    log_relative_saturated = log_relative_transition + math.log(x)
    assert log_relative_transition < log_relative_saturated < -9900.0


def main() -> None:
    check_pressure_identities()
    check_rh_model_bound()
    check_common_shift_and_separation()
    check_quartet()
    check_diagonal_scale()
    print("bounded pressure ratio: exact finite checks passed")
    print("sharp log-activity sensitivity: tanh(tau/4)")
    print("off-line quartet block density -> 1/4")
    print("diagonal transition cost: exp(-X^2/100+O(1))")
    print("STATUS: diagnostic only; no A1/RH claim")


if __name__ == "__main__":
    main()
