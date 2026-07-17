#!/usr/bin/env python3
import sys

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_102_far3_tradeoff_probe import selected_rows  # noqa: E402


def run():
    print("E73.104 FAR-SLOPE verifier")
    print("Checks sufficient split: sum FAR<=L^6 and max Q<=L^-11.")
    print(" lam     L tau    farSumB  maxQB  productB  directB status")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28), (28, 32)]:
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rows = selected_rows(lam, n_modes, sigma, tau, m, 12)
            far_sum = sum(row["far"] for row in rows)
            max_q = max(row["q"] for row in rows)
            product = far_sum * max_q
            direct = sum(row["term"] for row in rows)
            far_b = bexp(far_sum, L)
            q_b = bexp(max_q, L)
            prod_b = bexp(product, L)
            direct_b = bexp(direct, L)
            ok = far_b <= 6.0 and q_b <= -11.0 and prod_b <= -5.0
            print(
                f"{lam:4d} {L:7.3f} {tau:7.2f}"
                f" {far_b:9.3f} {q_b:7.3f} {prod_b:9.3f} {direct_b:8.3f}"
                f" {'PASS' if ok else 'FAIL':>6s}"
            )


if __name__ == "__main__":
    run()
