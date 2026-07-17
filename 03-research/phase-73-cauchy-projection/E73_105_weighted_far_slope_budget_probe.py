#!/usr/bin/env python3
import sys

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_102_far3_tradeoff_probe import selected_rows  # noqa: E402


def run():
    print("E73.105 weighted FAR-SLOPE budget probe")
    print("Reports node budgets b_k=L^5 FAR_k Q_k and total C_main=sum b_k.")
    print(" lam     L tau       Cmain   maxb  gamma:b list")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28), (28, 32), (32, 36)]:
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rows = selected_rows(lam, n_modes, sigma, tau, m, 12)
            budgets = [(row["gamma"], (L**5) * row["term"]) for row in rows]
            total = sum(b for _, b in budgets)
            maxb = max(b for _, b in budgets)
            parts = ",".join(f"{g:.1f}:{b:.3e}" for g, b in budgets)
            print(f"{lam:4d} {L:7.3f} {tau:7.2f} {total:11.3e} {maxb:9.3e} {parts}")


if __name__ == "__main__":
    run()
