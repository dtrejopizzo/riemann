#!/usr/bin/env python3
import sys

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_055_far3_nodewise_verifier import certificate_rows  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def run():
    print("E73.097 FAR3 main budget probe")
    print("Reports the three main rational WCS terms selected by FAR score.")
    print(" lam     L tau    mainB   maxB   gapToL5  gamma:termB list")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28), (28, 32)]:
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rows = certificate_rows(lam, n_modes, sigma, tau, m, 12)
            main_rows = [row for row in rows if row["part"] == "main"]
            main = sum(row["term"] for row in main_rows)
            max_term = max(row["term"] for row in main_rows)
            parts = ",".join(f"{row['gamma']:.1f}:{bexp(row['term'], L):.3f}" for row in main_rows)
            print(
                f"{lam:4d} {L:7.3f} {tau:7.2f}"
                f" {bexp(main, L):8.3f} {bexp(max_term, L):7.3f}"
                f" {bexp(main, L) + 5.0:8.3f} {parts}"
            )


if __name__ == "__main__":
    run()
