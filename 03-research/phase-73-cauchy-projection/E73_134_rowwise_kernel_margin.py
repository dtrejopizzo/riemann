#!/usr/bin/env python3
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact, cauchy_real  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def row_stats(d, xi, gamma):
    row = 1.0 / (-gamma - d)
    row_norm = float(np.linalg.norm(row))
    c = abs(cauchy_real(-gamma, d, xi))
    normalized = c / max(row_norm, 1e-300)
    return row_norm, normalized, c


def run():
    print("E73.134 rowwise kernel margin")
    print("p=log||k||/logL, q=-log|<xi,e>|/logL, csvExp=log|C|/logL.")
    print("Need q-p >= 17 for CSV_17.")
    print(" lam     L gamma      pRow      qNorm   q-p    csvExp status")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        for gamma in GAMMAS[:3]:
            row_norm, normalized, c = row_stats(d, xi, gamma)
            p = bexp(row_norm, L)
            q = -bexp(normalized, L)
            margin = q - p
            csv_exp = bexp(c, L)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {p:9.3f} {q:10.3f} {margin:6.3f}"
                f" {csv_exp:9.3f} {'PASS' if margin >= 17.0 else 'FAIL'}"
            )


if __name__ == "__main__":
    run()

