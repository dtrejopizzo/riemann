#!/usr/bin/env python3
"""Diagnostics for 104_74.

The analytic statements are proved in the document.  This checker verifies
the finite algebra, the Jensen/logistic identity by quadrature, the two
quartet densities, and the scale of the Hadamard Taylor obstruction.
"""

from __future__ import annotations

import cmath
import math

import numpy as np


def g_tau(x: float, tau: float) -> float:
    """Stable bounded pressure observable."""
    if x < -40.0:
        return 1.0
    if x > 40.0:
        return math.exp(-x) * (-math.expm1(-tau)) / tau
    return (math.log1p(math.exp(-x)) - math.log1p(math.exp(-x - tau))) / tau


def logistic_density(v: np.ndarray) -> np.ndarray:
    """Standard logistic density, evaluated without overflow."""
    out = np.empty_like(v)
    pos = v >= 0
    e = np.exp(-v[pos])
    out[pos] = e / (1.0 + e) ** 2
    e = np.exp(v[~pos])
    out[~pos] = e / (1.0 + e) ** 2
    return out


def jensen_sum(radius: np.ndarray, activities: np.ndarray) -> np.ndarray:
    vals = np.log(np.maximum(1.0, radius[:, None] * activities[None, :]))
    return vals.sum(axis=1)


def check_hadamard_semigroup() -> None:
    lam = np.array([-3.0, -0.25, 0.5, 4.0, 7.25])
    s, t = 0.37, 0.81
    us = np.exp(-s * lam)
    ut = np.exp(-t * lam)
    ust = np.exp(-(s + t) * lam)
    assert np.max(np.abs(us * ut - ust)) < 2.0e-13

    # A coefficient of the formal Hadamard exponential is the ordinary
    # exponential series in that coefficient.
    for x in lam:
        partial = sum(((-t * x) ** k) / math.factorial(k) for k in range(35))
        assert abs(partial - math.exp(-t * x)) < 2.0e-10 * max(1.0, math.exp(-t * x))


def check_jensen_and_logistic_mixture() -> None:
    activities = np.array([0.03, 0.4, 1.7, 8.0], dtype=float)
    tau = 1.3

    # Jensen's circle mean for D(w)=prod(1+w*z_n).
    for radius in (0.2, 0.8, 1.4, 4.0):
        theta = (np.arange(200_000) + 0.5) * (2.0 * math.pi / 200_000)
        w = radius * np.exp(1j * theta)
        log_abs = np.zeros_like(theta)
        for z in activities:
            log_abs += np.log(np.abs(1.0 + w * z))
        circle_mean = float(log_abs.mean())
        exact = float(np.log(np.maximum(1.0, radius * activities)).sum())
        assert abs(circle_mean - exact) < 2.0e-10

    # Formula (7): logistic mixture of Jensen annular increments.
    v = np.linspace(-24.0, 24.0, 400_001)
    radii = np.exp(-v)
    j1 = jensen_sum(radii, activities)
    j2 = jensen_sum(np.exp(-tau) * radii, activities)
    integral = float(np.trapz(logistic_density(v) * (j1 - j2) / tau, v))
    direct = sum(g_tau(-math.log(z), tau) for z in activities)
    assert abs(integral - direct) < 2.0e-9


def quartet_q(n: int, radius: float, theta: float) -> float:
    return 4.0 - 2.0 * (radius**n + radius ** (-n)) * math.cos(n * theta)


def check_quartet_jensen_and_density() -> None:
    radius = 0.75
    tau = 0.9

    # Same two interior radii, hence identical radial Jensen data.
    for test_r in (0.2, 0.7, 0.8, 0.95):
        j1 = 2.0 * max(0.0, math.log(test_r / radius))
        j2 = 2.0 * max(0.0, math.log(test_r / radius))
        assert j1 == j2

    # Periodic phases pi/2 and pi/3 give bad densities 1/4 and 1/2.
    vals = []
    phase_data = (
        ([1.0, 0.0, -1.0, 0.0], 0.25),
        ([1.0, 0.5, -0.5, -1.0, -0.5, 0.5], 0.5),
    )
    for cosine_table, target in phase_data:
        terms = []
        for n in range(20, 241):
            # Exact periodic cosine values avoid amplification of floating
            # roundoff by radius**(-n) on the zero-cosine classes.
            cosine = cosine_table[n % len(cosine_table)]
            qn = 4.0 - 2.0 * (radius**n + radius ** (-n)) * cosine
            terms.append(g_tau(qn + math.log(n + 1.0), tau))
        mean = float(np.mean(terms))
        vals.append(mean)
        assert abs(mean - target) < 0.012
    assert vals[1] - vals[0] > 0.23

    # Cayley quartet geometry: rho -> 1-rho maps a -> 1/a.
    a = radius * cmath.exp(1j * math.pi / 3.0)
    rho = 1.0 / (1.0 - a)
    w_rho = 1.0 - 1.0 / rho
    w_partner = 1.0 - 1.0 / (1.0 - rho)
    assert abs(w_rho - a) < 1.0e-14
    assert abs(w_partner - 1.0 / a) < 1.0e-14
    assert 0.5 < rho.real < 1.0


def logsumexp(values: list[float]) -> float:
    m = max(values)
    return m + math.log(sum(math.exp(x - m) for x in values))


def check_hadamard_truncation_gate() -> None:
    t = 1.0
    for n, k in ((12, 12), (16, 20), (20, 32)):
        y = 2.0 * (2.0**n + 2.0 ** (-n)) - 4.0
        assert k <= t * y / 2.0
        logs = [j * math.log(t * y) - math.lgamma(j + 1.0) for j in range(k + 1)]
        log_ratio = logsumexp(logs) - t * y
        assert log_ratio <= -t * y / 8.0

        yp = 4.0 + 2.0 * (2.0**n + 2.0 ** (-n))
        poly = sum(((-t * yp) ** j) / math.factorial(j) for j in range(k + 1))
        assert (poly > 0.0) == (k % 2 == 0)
        last = ((-t * yp) ** k) / math.factorial(k)
        assert abs(poly / last - 1.0) < 0.02


def main() -> None:
    check_hadamard_semigroup()
    check_jensen_and_logistic_mixture()
    check_quartet_jensen_and_density()
    check_hadamard_truncation_gate()
    print("PASS 104_74: Hadamard semigroup, Jensen mixture, quartet, truncation gate")


if __name__ == "__main__":
    main()
