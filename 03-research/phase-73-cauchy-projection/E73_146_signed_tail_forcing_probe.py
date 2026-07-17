#!/usr/bin/env python3
import itertools
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E72_349_cfir_row_candidate_probe import p_active, p_infty  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_077_pair_coefficient_budget_probe import coeffs, bexp  # noqa: E402


def active_pair(z, w, idx, d, L, xi):
    return sum(p_active(z, n_pos, w, idx, d, L) * xi[n_pos] for n_pos in range(len(d)))


def infinity_pair_row(z, w, d, L, xi):
    return sum(p_infty(z, n_d, w, L) * xi[n_pos] for n_pos, n_d in enumerate(d))


def coeff_matrix(zs, w, L):
    return np.array([coeffs(z, w, L) for z in zs], dtype=complex)


def forced_l1(mat, rhs):
    sol = np.linalg.solve(mat, rhs)
    return abs(sol[0]) + abs(sol[1])


def best_rows(lam, n_modes, gamma, nrows=6, sigma=0.20):
    d, L, xi, _ = setup_exact(lam, n_modes)
    idx = np.rint(d * L / (2.0 * np.pi)).astype(int)
    w = -1j * gamma
    candidates = [sigma + 1j * g for g in GAMMAS[:nrows]]
    best = None
    for z1, z2 in itertools.combinations(candidates, 2):
        mat = coeff_matrix([z1, z2], w, L)
        if abs(np.linalg.det(mat)) < 1e-300:
            continue
        active = np.array([active_pair(z1, w, idx, d, L, xi), active_pair(z2, w, idx, d, L, xi)])
        inf = np.array([infinity_pair_row(z1, w, d, L, xi), infinity_pair_row(z2, w, d, L, xi)])
        tail = inf - active
        signed = active + tail
        signed_margin = -bexp(forced_l1(mat, signed), L)
        rec = (signed_margin, mat, active, tail, signed, z1.imag, z2.imag, L)
        if best is None or rec[0] > best[0]:
            best = rec
    return best


def run():
    print("E73.146 signed-tail forcing probe")
    print("Tail is computed directly as p_infty-row minus p_active-row, not via H0 divisor values.")
    print("Margins are -log_L ||M^-1 rhs||_1; need signedMargin>=17.")
    print(" lam     L gamma   activeM    tailM  signedM      z1      z2 status")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        for gamma in GAMMAS[:3]:
            signed_margin, mat, active, tail, signed, z1, z2, L = best_rows(lam, n_modes, gamma)
            active_margin = -bexp(forced_l1(mat, active), L)
            tail_margin = -bexp(forced_l1(mat, tail), L)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {active_margin:9.3f} {tail_margin:8.3f}"
                f" {signed_margin:8.3f} {z1:7.2f} {z2:7.2f}"
                f" {'PASS' if signed_margin >= 17.0 else 'FAIL'}"
            )


if __name__ == "__main__":
    run()
