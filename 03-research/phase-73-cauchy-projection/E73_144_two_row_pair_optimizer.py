#!/usr/bin/env python3
import itertools
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E72_349_cfir_row_candidate_probe import p_active  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_077_pair_coefficient_budget_probe import coeffs, bexp  # noqa: E402


def active_pair(z, w, idx, d, L, xi):
    return sum(p_active(z, n_pos, w, idx, d, L) * xi[n_pos] for n_pos in range(len(d)))


def coeff_matrix(zs, w, L):
    return np.array([coeffs(z, w, L) for z in zs], dtype=complex)


def best_case(lam, n_modes, gamma, nrows=6, sigma=0.20):
    d, L, xi, _ = setup_exact(lam, n_modes)
    idx = np.rint(d * L / (2.0 * np.pi)).astype(int)
    w = -1j * gamma
    candidates = [sigma + 1j * g for g in GAMMAS[:nrows]]
    best = None
    for z1, z2 in itertools.combinations(candidates, 2):
        mat = coeff_matrix([z1, z2], w, L)
        if abs(np.linalg.det(mat)) < 1e-300:
            continue
        rhs = np.array([active_pair(z1, w, idx, d, L, xi), active_pair(z2, w, idx, d, L, xi)])
        forced = np.linalg.solve(mat, rhs)
        forced_l1 = abs(forced[0]) + abs(forced[1])
        amp = np.linalg.norm(np.linalg.inv(mat), ord=2)
        pair_norm = np.linalg.norm(rhs)
        margin = -bexp(forced_l1, L)
        rec = (margin, amp, pair_norm, z1.imag, z2.imag, forced_l1)
        if best is None or rec[0] > best[0]:
            best = rec
    return L, best


def run():
    print("E73.144 two-row PAIR optimizer")
    print("Optimizes two z-rows for active PairM forcing of H0(w),H0(-w).")
    print("margin=-log_L ||M^-1 PairM||_1; need margin>=17.")
    print(" lam     L gamma    margin    ampB  pairNormB      z1      z2 status")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        for gamma in GAMMAS[:3]:
            L, best = best_case(lam, n_modes, gamma)
            margin, amp, pair_norm, z1, z2, forced_l1 = best
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {margin:9.3f} {bexp(amp, L):7.3f}"
                f" {bexp(pair_norm, L):10.3f} {z1:7.2f} {z2:7.2f}"
                f" {'PASS' if margin >= 17.0 else 'FAIL'}"
            )


if __name__ == "__main__":
    run()
