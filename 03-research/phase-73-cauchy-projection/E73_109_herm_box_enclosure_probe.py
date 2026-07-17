#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_055_far3_nodewise_verifier import setup_full, finite_roots_signed, hermite_kernel_bound, cauchy_real  # noqa: E402


def grid_values(alpha0, alpha1, tau0, tau1, gamma, m, grid_n):
    alphas = np.linspace(alpha0, alpha1, grid_n)
    taus = np.linspace(tau0, tau1, grid_n)
    vals = []
    for alpha in alphas:
        for tau in taus:
            vals.append(hermite_kernel_bound(alpha + 1j * tau, 1j * gamma, m))
    return np.array(vals)


def finite_diff_lip(alpha0, alpha1, tau0, tau1, gamma, m, grid_n):
    alphas = np.linspace(alpha0, alpha1, grid_n)
    taus = np.linspace(tau0, tau1, grid_n)
    max_lip = 0.0
    h_alpha = max((alpha1 - alpha0) / max(grid_n - 1, 1), 1e-12)
    h_tau = max((tau1 - tau0) / max(grid_n - 1, 1), 1e-12)
    values = {}
    for ia, alpha in enumerate(alphas):
        for it, tau in enumerate(taus):
            values[(ia, it)] = hermite_kernel_bound(alpha + 1j * tau, 1j * gamma, m)
    for ia in range(grid_n):
        for it in range(grid_n):
            v = values[(ia, it)]
            if ia + 1 < grid_n:
                max_lip = max(max_lip, abs(values[(ia + 1, it)] - v) / h_alpha)
            if it + 1 < grid_n:
                max_lip = max(max_lip, abs(values[(ia, it + 1)] - v) / h_tau)
    # Safety inflation for unobserved curvature between grid points.
    return 4.0 * max_lip


def herm_box_upper(alpha0, alpha1, tau0, tau1, gamma, m, grid_n=9):
    vals = grid_values(alpha0, alpha1, tau0, tau1, gamma, m, grid_n)
    sampled_sup = float(np.max(vals))
    lip = finite_diff_lip(alpha0, alpha1, tau0, tau1, gamma, m, grid_n)
    h_alpha = (alpha1 - alpha0) / max(grid_n - 1, 1)
    h_tau = (tau1 - tau0) / max(grid_n - 1, 1)
    radius = 0.5 * math.hypot(h_alpha, h_tau)
    upper = sampled_sup + lip * radius
    return upper, sampled_sup, lip, radius


def box_far_certificate(lam, n_modes, alpha0, alpha1, tau0, tau1, m, ncrit=12, grid_n=9):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    rows = []
    for j, gamma in enumerate(GAMMAS[:ncrit]):
        g_up, g_sample, lip, radius = herm_box_upper(alpha0, alpha1, tau0, tau1, gamma, m, grid_n)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        w_up = math.exp(alpha1 * L) * g_up * mesh
        t = -gamma
        c = abs(cauchy_real(t, d, xi))
        r = float(np.min(np.abs(t - roots))) if len(roots) else 1.0
        rows.append(
            {
                "j": j,
                "gamma": gamma,
                "w_up": w_up,
                "far_up": w_up * r,
                "budget_up": (L**5) * w_up * c,
                "g_up": g_up,
                "g_sample": g_sample,
                "lip": lip,
                "radius": radius,
            }
        )
    selected = sorted(rows, reverse=True, key=lambda row: row["far_up"])[:3]
    budget = sum(row["budget_up"] for row in selected)
    return L, selected, budget


def run():
    print("E73.109 HERM-BOX enclosure probe")
    print("Grid+inflated-Lipschitz upper enclosure for G_theta,m over cluster boxes.")
    print(" lam     L box                         selected        CmainUp  maxInfl status")
    boxes = []
    for tau in [GAMMAS[0], GAMMAS[1]]:
        boxes.append((0.18, 0.22, tau - 0.20, tau + 0.20))
        boxes.append((0.15, 0.25, tau - 0.50, tau + 0.50))
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        for alpha0, alpha1, tau0, tau1 in boxes:
            L, selected, budget = box_far_certificate(lam, n_modes, alpha0, alpha1, tau0, tau1, 3)
            names = ",".join(f"{row['gamma']:.1f}" for row in selected)
            infl = max(row["g_up"] / max(row["g_sample"], 1e-300) for row in selected)
            ok = budget <= 1.0
            print(
                f"{lam:4d} {L:7.3f} [{alpha0:.2f},{alpha1:.2f}]x[{tau0:5.2f},{tau1:5.2f}]"
                f" {names:17s} {budget:8.3e} {infl:8.3f} {'PASS' if ok else 'FAIL'}"
            )


if __name__ == "__main__":
    run()
