#!/usr/bin/env python3
import sys
import cmath
import math
import numpy as np
from numpy.linalg import eigh, norm
from scipy.optimize import brentq

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


def finite_roots(d, xi, hmax):
    roots = []
    brackets = []
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
                    brackets.append((left_pole, right_pole))
        except Exception:
            pass
    order = np.argsort(roots)
    return np.array(roots)[order], [brackets[i] for i in order]


def hermite_kernel_bound(a, k, m, theta=0.5):
    beta = k - a
    w0 = 1.0 / (2.0 * a)
    wstar = -1.0 / beta
    d = abs(wstar - w0)
    r = theta * d
    mr = 1.0 / (abs(beta) * (1.0 - theta) * d)
    total = 0.0
    for p in range(m):
        inner = 0.0
        for rr in range(p, m):
            inner += math.comb(rr, p) * (abs(w0) ** (rr - p)) * (r ** (-rr))
        total += inner / math.factorial(p)
    return mr * total


def local_slope_numeric(root, gamma, d, xi):
    # Exact local slope at the sampled point: |C(gamma)| / |gamma-root|.
    # This is not a proof envelope on an interval; it is the sharp diagnostic for the optimized gate.
    dist = abs(gamma - root)
    if dist == 0:
        return 0.0
    return abs(cauchy_real(gamma, d, xi)) / dist


def derivative_envelope_segment(root, gamma, d, xi):
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


def optimized_root_defect(gamma, d, xi, roots, brackets):
    trivial = abs(cauchy_real(gamma, d, xi))
    if len(roots) == 0:
        return trivial, trivial, np.nan, trivial, "triv"
    j = int(np.argmin(np.abs(roots - gamma)))
    root = roots[j]
    slope = local_slope_numeric(root, gamma, d, xi)
    point_defect = slope * abs(gamma - root)
    interval_defect = derivative_envelope_segment(root, gamma, d, xi) * abs(gamma - root)
    if interval_defect <= trivial:
        return point_defect, interval_defect, root, trivial, "root"
    return point_defect, trivial, root, trivial, "triv"


def row_for_case(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi = setup_full(lam, n_modes)
    roots, brackets = finite_roots(d, xi, hmax=max(GAMMAS[:ncrit]) + 10)
    a = sigma + 1j * tau
    point_total = 0.0
    interval_total = 0.0
    actual_factor = 0.0
    root_count = 0
    best_terms = []
    for gamma in GAMMAS[:ncrit]:
        k = 1j * gamma
        w = hermite_kernel_bound(a, k, m)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        point_rdef, interval_rdef, root, trivial, mode = optimized_root_defect(-gamma, d, xi, roots, brackets)
        point_term = math.exp(sigma * L) * w * mesh * point_rdef
        interval_term = math.exp(sigma * L) * w * mesh * interval_rdef
        actual = math.exp(sigma * L) * w * mesh * trivial
        point_total += point_term
        interval_total += interval_term
        actual_factor += actual
        if mode == "root":
            root_count += 1
        best_terms.append((interval_term, gamma, mesh, interval_rdef, root, mode))
    best_terms.sort(reverse=True, key=lambda x: x[0])
    return {
        "lam": lam,
        "L": L,
        "sigma": sigma,
        "tau": tau,
        "m": m,
        "ncrit": ncrit,
        "roots": len(roots),
        "point_total": point_total,
        "interval_total": interval_total,
        "actual": actual_factor,
        "root_count": root_count,
        "top": best_terms[0],
    }


def run():
    print("E73.040 optimized mesh-root covering probe")
    print("Uses stable real Cauchy roots and the explicit E73.037 Hermite bound.")
    print("pointDiag is tautological; intervalMRC uses a non-circular derivative envelope.")
    print(
        " lam     L sigma     tau  m nK roots rootUse  pointDiag intervalMRC"
        "     actual  int/act   topGamma    topMesh     topR mode"
    )
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.05, GAMMAS[0], 2), (0.10, GAMMAS[0], 2), (0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            row = row_for_case(lam, n_modes, sigma, tau, m, 6)
            top_term, top_gamma, top_mesh, top_r, top_root, top_mode = row["top"]
            print(
                f"{row['lam']:4d} {row['L']:7.3f} {row['sigma']:5.2f} {row['tau']:7.2f}"
                f" {row['m']:2d} {row['ncrit']:2d} {row['roots']:5d} {row['root_count']:7d}"
                f" {row['point_total']:10.3e} {row['interval_total']:10.3e}"
                f" {row['actual']:10.3e} {row['interval_total']/max(row['actual'], 1e-300):8.2e}"
                f" {top_gamma:10.3f} {top_mesh:10.3e} {top_r:9.3e} {top_mode:>4s}"
            )


if __name__ == "__main__":
    run()
