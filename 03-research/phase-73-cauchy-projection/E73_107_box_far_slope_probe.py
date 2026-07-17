#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_055_far3_nodewise_verifier import setup_full, finite_roots_signed, hermite_kernel_bound, cauchy_real  # noqa: E402


def box_points(alpha0, alpha1, tau0, tau1):
    ac = 0.5 * (alpha0 + alpha1)
    tc = 0.5 * (tau0 + tau1)
    return [
        (alpha0, tau0),
        (alpha0, tau1),
        (alpha1, tau0),
        (alpha1, tau1),
        (ac, tc),
    ]


def row_data(L, d, xi, roots, alpha, tau, m, ncrit):
    a = alpha + 1j * tau
    rows = []
    for j, gamma in enumerate(GAMMAS[:ncrit]):
        t = -gamma
        geom = hermite_kernel_bound(a, 1j * gamma, m)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        w = math.exp(alpha * L) * geom * mesh
        c = abs(cauchy_real(t, d, xi))
        r = float(np.min(np.abs(t - roots))) if len(roots) else 1.0
        far = w * r
        term = w * c
        rows.append({"j": j, "gamma": gamma, "far": far, "term": term})
    rows.sort(reverse=True, key=lambda row: row["far"])
    return rows


def certify_box(lam, n_modes, alpha0, alpha1, tau0, tau1, m, ncrit=12):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    possible_sets = {}
    worst_budget = 0.0
    worst_far_gap = float("inf")
    for alpha, tau in box_points(alpha0, alpha1, tau0, tau1):
        rows = row_data(L, d, xi, roots, alpha, tau, m, ncrit)
        selected = rows[:3]
        key = tuple(sorted(row["j"] for row in selected))
        possible_sets.setdefault(key, []).append((alpha, tau))
        budget = (L**5) * sum(row["term"] for row in selected)
        worst_budget = max(worst_budget, budget)
        gap = selected[-1]["far"] / max(rows[3]["far"], 1e-300)
        worst_far_gap = min(worst_far_gap, gap)
    return L, possible_sets, worst_budget, worst_far_gap


def run():
    print("E73.107 box FAR-SLOPE probe")
    print("Samples box corners+center; reports possible FAR3 sets, worst L^5 main budget, FAR gap.")
    print(" lam     L alphaBox       tauBox          sets  CmainMax   farGap  status")
    boxes = []
    for tau in [GAMMAS[0], GAMMAS[1]]:
        boxes.append((0.18, 0.22, tau - 0.20, tau + 0.20))
        boxes.append((0.15, 0.25, tau - 0.50, tau + 0.50))
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        for alpha0, alpha1, tau0, tau1 in boxes:
            L, sets, budget, gap = certify_box(lam, n_modes, alpha0, alpha1, tau0, tau1, 3)
            set_str = ";".join(
                ",".join(f"{GAMMAS[j]:.1f}" for j in key) for key in sorted(sets)
            )
            ok = budget <= 1.0 and gap > 1.0
            print(
                f"{lam:4d} {L:7.3f} [{alpha0:.2f},{alpha1:.2f}]"
                f" [{tau0:6.2f},{tau1:6.2f}] {set_str:18s}"
                f" {budget:9.3e} {gap:8.3f} {'PASS' if ok else 'FAIL'}"
            )


if __name__ == "__main__":
    run()
