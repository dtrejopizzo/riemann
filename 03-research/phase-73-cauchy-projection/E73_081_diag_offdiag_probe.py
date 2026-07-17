#!/usr/bin/env python3
import sys
import math

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_071_packet_mellin_formula_verifier import h0  # noqa: E402
from E73_077_pair_coefficient_budget_probe import coeffs, bexp  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def split_budget(z, ws, L, d, xi, q):
    delta = L ** (-q)
    diag = 0.0
    off = 0.0
    diag_count = 0
    for w in ws:
        a, b = coeffs(z, w, L)
        term = abs(a * h0(w, d, xi)) + abs(b * h0(-w, d, xi))
        if abs(w - z) <= delta or abs(w + z) <= delta:
            diag += term
            diag_count += 1
        else:
            off += term
    return diag, off, diag_count, delta


def run():
    print("E73.081 diagonal/off-diagonal factor probe")
    print("Splits coefficient-weighted H0 budget for critical zero windows.")
    print(" lam     L   zIm   q    diag#   diagB    offB    totalB   delta")
    ws = [1j * g for g in GAMMAS[:8]]
    for lam, n_modes in [(16, 20), (20, 24), (24, 28)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        for z_im in [GAMMAS[0], GAMMAS[1], 17.30]:
            z = 0.20 + 1j * z_im
            for q in [0.0, 1.0, 2.0]:
                diag, off, cnt, delta = split_budget(z, ws, L, d, xi, q)
                print(
                    f"{lam:4d} {L:7.3f} {z_im:6.2f} {q:3.1f}"
                    f" {cnt:7d} {bexp(diag, L):8.3f} {bexp(off, L):8.3f}"
                    f" {bexp(diag + off, L):8.3f} {delta:8.2e}"
                )


if __name__ == "__main__":
    run()
