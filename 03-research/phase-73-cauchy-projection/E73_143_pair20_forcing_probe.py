#!/usr/bin/env python3
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E72_349_cfir_row_candidate_probe import p_active, p_infty  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_075_pair_divisibility_verifier import pair_closed  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def active_pair(z, w, idx, d, L, xi):
    total = 0.0 + 0.0j
    for n_pos in range(len(d)):
        total += p_active(z, n_pos, w, idx, d, L) * xi[n_pos]
    return total


def infinite_pair_row(z, w, idx, d, L, xi):
    total = 0.0 + 0.0j
    for n_pos, n_d in enumerate(d):
        total += p_infty(z, n_d, w, L) * xi[n_pos]
    return total


def run():
    print("E73.143 PAIR20 forcing probe")
    print("PairM is the active finite packet, PairInf is the complete-mesh closed packet.")
    print("Need PairM and tail at about L^-20 when inverse loss is L^3.")
    print(" lam     L gamma      pairMB  pairInfB    tailB rowRelInf status")
    sigma = 0.20
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        idx = np.rint(d * L / (2.0 * np.pi)).astype(int)
        for j, gamma in enumerate(GAMMAS[:3]):
            w = -1j * gamma
            z = sigma + 1j * GAMMAS[(j + 1) % 3]
            pair_m = active_pair(z, w, idx, d, L, xi)
            pair_inf_row = infinite_pair_row(z, w, idx, d, L, xi)
            pair_inf_closed = pair_closed(z, w, L, d, xi)
            tail = pair_inf_closed - pair_m
            rel = abs(pair_inf_row - pair_inf_closed) / max(abs(pair_inf_closed), 1e-300)
            ok = bexp(abs(pair_m), L) <= -20.0 and bexp(abs(tail), L) <= -20.0
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(abs(pair_m), L):9.3f} {bexp(abs(pair_inf_closed), L):9.3f}"
                f" {bexp(abs(tail), L):8.3f} {rel:9.2e} {'PASS' if ok else 'FAIL'}"
            )


if __name__ == "__main__":
    run()
