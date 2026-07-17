#!/usr/bin/env python3
import sys
import math
import cmath

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_069_exact_far3_row_probe import setup_exact, far3_rows  # noqa: E402
from E73_071_packet_mellin_formula_verifier import h0  # noqa: E402
from E73_077_pair_coefficient_budget_probe import coeffs, bexp  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def hwin(z, ws, L, d, xi):
    total = 0.0
    for w in ws:
        a, b = coeffs(z, w, L)
        total += abs(a * h0(w, d, xi)) + abs(b * h0(-w, d, xi))
    return total


def run():
    print("E73.084 weighted HWIN probe")
    print("Compares Pref*HWIN with direct Pref*|H0(z)| on FAR3 rows.")
    print(" lam     L tau nwin   gamma   directB    hwinB  prefHwinB  ratio")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            _, rows = far3_rows(lam, n_modes, sigma, tau, m, 12)
            for nwin in [3, 5, 8]:
                ws = [1j * g for g in GAMMAS[:nwin]]
                for row in rows:
                    z = sigma + 1j * row["gamma"]
                    direct = row["pref"] * abs(h0(z, d, xi))
                    hv = hwin(z, ws, L, d, xi)
                    weighted = row["pref"] * hv
                    ratio = weighted / max(direct, 1e-300)
                    print(
                        f"{lam:4d} {L:7.3f} {tau:7.2f} {nwin:4d}"
                        f" {row['gamma']:7.2f} {bexp(direct, L):9.3f}"
                        f" {bexp(hv, L):8.3f} {bexp(weighted, L):10.3f}"
                        f" {ratio:9.3e}"
                    )


if __name__ == "__main__":
    run()
