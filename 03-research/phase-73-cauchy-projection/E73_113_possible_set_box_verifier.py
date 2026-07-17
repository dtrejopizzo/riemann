#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_055_far3_nodewise_verifier import setup_full, finite_roots_signed, hermite_kernel_bound, cauchy_real  # noqa: E402
from E73_111_herm_box_derivative_probe import herm_box_upper_derivative  # noqa: E402


def herm_box_lower_sample(alpha0, alpha1, tau0, tau1, gamma, m, grid_n=5):
    vals = []
    for alpha in np.linspace(alpha0, alpha1, grid_n):
        for tau in np.linspace(tau0, tau1, grid_n):
            vals.append(hermite_kernel_bound(alpha + 1j * tau, 1j * gamma, m))
    return float(min(vals))


def row_intervals(L, d, xi, roots, alpha0, alpha1, tau0, tau1, gamma, m):
    g_up, _ = herm_box_upper_derivative(alpha0, alpha1, tau0, tau1, gamma, m)
    g_low = herm_box_lower_sample(alpha0, alpha1, tau0, tau1, gamma, m)
    mesh = abs(1.0 - cmath.exp(1j * gamma * L))
    t = -gamma
    c = abs(cauchy_real(t, d, xi))
    r = float(np.min(np.abs(t - roots))) if len(roots) else 1.0
    w_up = math.exp(alpha1 * L) * g_up * mesh
    w_low = math.exp(alpha0 * L) * g_low * mesh
    return {
        "gamma": gamma,
        "far_low": w_low * r,
        "far_up": w_up * r,
        "budget_up": (L**5) * w_up * c,
    }


def possible_rows(rows):
    possible = []
    for row in rows:
        strictly_above = sum(1 for other in rows if other["far_low"] > row["far_up"])
        if strictly_above < 3:
            possible.append(row)
    return possible


def verify_box(lam, n_modes, alpha0, alpha1, tau0, tau1, m, ncrit=12):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    rows = [
        row_intervals(L, d, xi, roots, alpha0, alpha1, tau0, tau1, gamma, m)
        for gamma in GAMMAS[:ncrit]
    ]
    poss = possible_rows(rows)
    worst_three = sorted(poss, reverse=True, key=lambda row: row["budget_up"])[:3]
    budget = sum(row["budget_up"] for row in worst_three)
    return L, poss, worst_three, budget


def run():
    print("E73.113 possible-set box verifier")
    print("Uses FAR interval possible set P3 and sums the three largest B_k^+ budgets.")
    print(" lam     L box                         |P3| possible             worst3              budget status")
    boxes = []
    for tau in [GAMMAS[0], GAMMAS[1]]:
        boxes.append((0.18, 0.22, tau - 0.20, tau + 0.20))
        boxes.append((0.15, 0.25, tau - 0.50, tau + 0.50))
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        for alpha0, alpha1, tau0, tau1 in boxes:
            L, poss, worst, budget = verify_box(lam, n_modes, alpha0, alpha1, tau0, tau1, 3)
            poss_s = ",".join(f"{row['gamma']:.1f}" for row in sorted(poss, key=lambda r: r["gamma"]))
            worst_s = ",".join(f"{row['gamma']:.1f}" for row in worst)
            print(
                f"{lam:4d} {L:7.3f} [{alpha0:.2f},{alpha1:.2f}]x[{tau0:5.2f},{tau1:5.2f}]"
                f" {len(poss):4d} {poss_s:20s} {worst_s:20s} {budget:8.3e}"
                f" {'PASS' if budget <= 1.0 else 'FAIL'}"
            )


if __name__ == "__main__":
    run()
