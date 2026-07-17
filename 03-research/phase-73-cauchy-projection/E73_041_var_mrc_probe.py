#!/usr/bin/env python3
import sys
import cmath
import math
import numpy as np
from numpy.linalg import eigh, norm
from scipy.optimize import brentq, minimize_scalar

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return d, L, xi


def cauchy_real(t, d, xi):
    return float(np.sum(xi / (t - d)))


def cauchy_prime(t, d, xi):
    return float(-np.sum(xi / ((t - d) ** 2)))


def finite_roots(d, xi, hmax):
    roots = []
    ds = np.sort(d)
    for left_pole, right_pole in zip(ds[:-1], ds[1:]):
        left = left_pole + 1e-8
        right = right_pole - 1e-8
        if right <= left:
            continue
        try:
            fa = cauchy_real(left, d, xi)
            fb = cauchy_real(right, d, xi)
            if np.isfinite(fa) and np.isfinite(fb) and fa * fb < 0:
                root = brentq(lambda x: cauchy_real(x, d, xi), left, right, xtol=1e-13)
                if -hmax <= root <= hmax:
                    roots.append(root)
        except Exception:
            pass
    return np.array(sorted(roots))


def hermite_kernel_bound(a, k, m, theta=0.5):
    beta = k - a
    w0 = 1.0 / (2.0 * a)
    wstar = -1.0 / beta
    dist = abs(wstar - w0)
    radius = theta * dist
    major = 1.0 / (abs(beta) * (1.0 - theta) * dist)
    total = 0.0
    for p in range(m):
        inner = 0.0
        for rr in range(p, m):
            inner += math.comb(rr, p) * (abs(w0) ** (rr - p)) * (radius ** (-rr))
        total += inner / math.factorial(p)
    return major * total


def sup_abs_derivative_segment(root, gamma, d, xi):
    left = min(root, gamma)
    right = max(root, gamma)
    if right - left <= 1e-14:
        return abs(cauchy_prime((left + right) / 2.0, d, xi))
    values = [abs(cauchy_prime(left, d, xi)), abs(cauchy_prime(right, d, xi))]
    grid = np.linspace(left, right, 17)
    for a, b in zip(grid[:-1], grid[1:]):
        if b - a <= 1e-14:
            continue
        res = minimize_scalar(lambda t: -abs(cauchy_prime(t, d, xi)), bounds=(a, b), method="bounded")
        if res.success:
            values.append(-float(res.fun))
    return max(values)


def abs_derivative_segment(root, gamma, d, xi):
    left = min(root, gamma)
    right = max(root, gamma)
    if left == right:
        return 0.0
    min_dist = np.inf
    for pole in d:
        if left <= pole <= right:
            return np.inf
        min_dist = min(min_dist, abs(left - pole), abs(right - pole))
    if min_dist <= 0:
        return np.inf
    return float(np.sum(np.abs(xi)) / (min_dist**2))


def budgets_for_case(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots(d, xi, hmax=max(GAMMAS[:ncrit]) + 10)
    a = sigma + 1j * tau
    point_total = 0.0
    abs_total = 0.0
    var_total = 0.0
    actual_total = 0.0
    var_wins = 0
    for gamma_pos in GAMMAS[:ncrit]:
        gamma = -gamma_pos
        k = 1j * gamma_pos
        weight = math.exp(sigma * L) * hermite_kernel_bound(a, k, m) * abs(1.0 - cmath.exp(1j * gamma_pos * L))
        actual = abs(cauchy_real(gamma, d, xi))
        if len(roots):
            root = roots[int(np.argmin(np.abs(roots - gamma)))]
            dist = abs(gamma - root)
            point = actual
            abs_def = min(actual, abs_derivative_segment(root, gamma, d, xi) * dist)
            var_def = min(actual, sup_abs_derivative_segment(root, gamma, d, xi) * dist)
            if var_def < actual:
                var_wins += 1
        else:
            point = actual
            abs_def = actual
            var_def = actual
        point_total += weight * point
        abs_total += weight * abs_def
        var_total += weight * var_def
        actual_total += weight * actual
    return {
        "lam": lam,
        "L": L,
        "sigma": sigma,
        "tau": tau,
        "m": m,
        "ncrit": ncrit,
        "roots": len(roots),
        "point": point_total,
        "abs": abs_total,
        "var": var_total,
        "actual": actual_total,
        "var_wins": var_wins,
    }


def run():
    print("E73.041 VAR-MRC probe")
    print("Compares trivial, incoherent derivative, and signed-variation derivative budgets.")
    print(" lam     L sigma     tau  m roots varWins      actual      absDeriv      varDeriv   var/act")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.05, GAMMAS[0], 2), (0.10, GAMMAS[0], 2), (0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            row = budgets_for_case(lam, n_modes, sigma, tau, m, 6)
            print(
                f"{row['lam']:4d} {row['L']:7.3f} {row['sigma']:5.2f} {row['tau']:7.2f}"
                f" {row['m']:2d} {row['roots']:5d} {row['var_wins']:7d}"
                f" {row['actual']:11.3e} {row['abs']:13.3e} {row['var']:13.3e}"
                f" {row['var']/max(row['actual'], 1e-300):9.2e}"
            )


if __name__ == "__main__":
    run()
