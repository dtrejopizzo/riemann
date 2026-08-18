#!/usr/bin/env python3
"""Finite diagnostics for 104_73_BERNSTEIN_PRESSURE_WIDTH_GATE.md.

This checks the exact scalar identities and asymptotic models.  It is not
a proof of the block theorem and does not verify RH.
"""

from __future__ import annotations

import math


def softplus(x: float) -> float:
    return max(0.0, x) + math.log1p(math.exp(-abs(x)))


def phi(delta: float, tau: float) -> float:
    return softplus(delta) - softplus(delta - tau)


def simpson_integral(func, a: float, b: float, steps: int = 200000) -> float:
    if steps % 2:
        steps += 1
    h = (b - a) / steps
    total = func(a) + func(b)
    total += 4.0 * sum(func(a + h * k) for k in range(1, steps, 2))
    total += 2.0 * sum(func(a + h * k) for k in range(2, steps, 2))
    return total * h / 3.0


def bernstein_integral(delta: float, tau: float) -> float:
    z = math.exp(delta)
    inv_q = math.exp(tau)

    def integrand(t: float) -> float:
        if t == 0.0:
            return 0.0
        return (-math.expm1(-t * z)) * (math.exp(-t) - math.exp(-inv_q * t)) / t

    # All test parameters have an exponentially negligible tail past 40.
    return simpson_integral(integrand, 0.0, 40.0, 40000)


def check_bernstein() -> None:
    for tau in (0.2, 1.0, 2.5):
        q = math.exp(-tau)
        for delta in (-4.0, -1.0, 0.0, 1.0, 4.0):
            lhs = phi(delta, tau)
            rhs = bernstein_integral(delta, tau)
            assert math.isclose(lhs, rhs, rel_tol=1e-7, abs_tol=2e-9)

        for z in (0.01, 0.2, 1.0, 5.0, 100.0):
            for k in range(1, 8):
                bracket = (1.0 / (1.0 + z) ** k
                           - q**k / (1.0 + q * z) ** k)
                assert bracket > 0.0


def check_mellin_bound() -> None:
    for tau in (0.1, 0.7, 3.0, 8.0):
        for alpha in (0.1, 0.3, 0.7, 1.0):
            coeff = math.gamma(alpha) * (-math.expm1(-alpha * tau)) / tau
            for delta in (k / 2.0 for k in range(-30, 31)):
                lhs = phi(delta, tau) / tau
                rhs = coeff * math.exp(alpha * delta)
                assert lhs <= rhs * (1.0 + 2e-14) + 2e-14


def logistic_prime(x: float) -> float:
    if abs(x) > 350.0:
        return 0.0
    return 1.0 / (4.0 * math.cosh(x / 2.0) ** 2)


def logistic(x: float) -> float:
    if x >= 0.0:
        return 1.0 / (1.0 + math.exp(-x))
    ex = math.exp(x)
    return ex / (1.0 + ex)


def normalized_pressure_derivative(delta: float, tau: float) -> float:
    return (logistic(delta) - logistic(delta - tau)) / tau


def effective_width(tau: float) -> float:
    return tau / math.tanh(tau / 4.0)


def check_curvature() -> None:
    for tau in (0.2, 1.0, 4.0):
        exact_lipschitz = 1.0 / effective_width(tau)
        assert math.isclose(
            normalized_pressure_derivative(tau / 2.0, tau),
            exact_lipschitz,
            rel_tol=2e-15,
            abs_tol=2e-15,
        )
        for k in range(-200, 201):
            delta = tau / 2.0 + k / 10.0
            derivative = normalized_pressure_derivative(delta, tau)
            assert 0.0 < derivative <= exact_lipschitz * (1.0 + 2e-15)

        for delta in (-10.0, -1.0, 0.0, tau / 2.0 - 0.01):
            assert logistic_prime(delta) - logistic_prime(delta - tau) > 0.0
        assert abs(logistic_prime(tau / 2.0) - logistic_prime(-tau / 2.0)) < 1e-15
        for delta in (tau / 2.0 + 0.01, tau + 1.0, tau + 10.0):
            assert logistic_prime(delta) - logistic_prime(delta - tau) < 0.0


def check_block_transport() -> None:
    for tau in (0.3, 2.0, 10.0):
        left = (-3.0, -0.2, 0.7, 4.0)
        right = (-2.7, -0.4, 1.1, 3.8)
        observed = abs(sum(
            (phi(x, tau) - phi(y, tau)) / tau
            for x, y in zip(left, right)
        ))
        bound = (1.0 / effective_width(tau)
                 * sum(abs(x - y) for x, y in zip(left, right)))
        assert observed <= bound * (1.0 + 2e-14) + 2e-14

    # The exact effective scale stays finite as tau -> 0 and is
    # asymptotic to tau as tau -> infinity.
    assert math.isclose(effective_width(1e-6), 4.0,
                        rel_tol=1e-12, abs_tol=1e-12)
    assert math.isclose(effective_width(100.0) / 100.0, 1.0,
                        rel_tol=1e-12, abs_tol=1e-12)


def quartet_lambda(n: int) -> float:
    residue = n % 4
    if n > 500:
        if residue == 0:
            return -math.inf
        if residue == 2:
            return math.inf
        return 4.0
    if residue == 0:
        return 4.0 - 2.0 * (2.0**n + 2.0 ** (-n))
    if residue == 2:
        return 4.0 + 2.0 * (2.0**n + 2.0 ** (-n))
    return 4.0


def normalized_pressure(x: float, tau: float) -> float:
    if x == -math.inf:
        return 1.0
    if x == math.inf:
        return 0.0
    return phi(-x, tau) / tau


def check_variable_width_quartet() -> None:
    # tau_L=exp(sqrt(X_L)) is subexponential in the degree and still sees
    # exactly the density 1/4 of negative quartet excursions.
    errors = []
    for length in (20, 40, 80, 160, 320):
        start = length * length
        tau = math.exp(math.sqrt(start))
        total = 0.0
        for n in range(start, start + length):
            lam = quartet_lambda(n)
            x = lam + math.log(n + 1.0) if math.isfinite(lam) else lam
            total += normalized_pressure(x, tau)
        errors.append(abs(total / length - 0.25))
    assert errors[-1] < 0.004


def check_width_pole_scale() -> None:
    for x in (300.0, 600.0, 1000.0):
        # Since X_L=L^2+L-1, log L=(1/2+o(1))log X_L.  Transporting
        # the full L-site block costs this additional harmless factor.
        log_length = 0.5 * math.log(x)
        log_width_detecting = math.sqrt(x)
        log_relative = (-x * x / 100.0 + log_width_detecting
                        - log_length)
        assert log_relative / (x * x) < -0.0098

        # Even a vanishing raw width has effective width -> 4, so the
        # same leading quadratic precision wall remains.
        log_relative_small_width = (-x * x / 100.0 + math.log(4.0)
                                    - log_length)
        assert log_relative_small_width / (x * x) < -0.0099

        log_tau_polar = x * x / 100.0 - math.sqrt(x)
        for log_r in (0.001, 0.1, 1.0):
            assert x * log_r - log_tau_polar < 0.0


def main() -> None:
    check_bernstein()
    check_mellin_bound()
    check_curvature()
    check_block_transport()
    check_variable_width_quartet()
    check_width_pole_scale()
    print("Bernstein pressure representation: finite checks passed")
    print("Mellin linearisation returns exponential Li moments")
    print("exact block transport width tau/tanh(tau/4): passed")
    print("variable-width quartet density -> 1/4")
    print("detecting width leaves relative cost exp(-X^2/100+o(X))")
    print("STATUS: gate only; no A1/RH claim")


if __name__ == "__main__":
    main()
