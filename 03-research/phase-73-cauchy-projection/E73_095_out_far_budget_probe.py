#!/usr/bin/env python3
import sys

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_051_far_tail_quant_probe import terms  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def run():
    print("E73.095 OUT-FAR finite-window budget probe")
    print("Tail is the WCS contribution outside the FAR3 selected rows, inside finite K_L.")
    print(" lam     L tau nK      totalB    main3B    tailB  tailFracB  farGammas")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        for ncrit in [6, 8, 10, 12]:
            for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
                L, rows = terms(lam, n_modes, sigma, tau, m, ncrit)
                total = sum(row[0] for row in rows)
                selected = sorted(rows, reverse=True, key=lambda row: row[1])[:3]
                ids = {row[2] for row in selected}
                main = sum(row[0] for row in rows if row[2] in ids)
                tail = sum(row[0] for row in rows if row[2] not in ids)
                frac = tail / max(total, 1e-300)
                gammas = ",".join(f"{row[2]:.1f}" for row in selected)
                print(
                    f"{lam:4d} {L:7.3f} {tau:7.2f} {ncrit:2d}"
                    f" {bexp(total, L):10.3f} {bexp(main, L):9.3f}"
                    f" {bexp(tail, L):8.3f} {bexp(frac, L):10.3f} {gammas}"
                )


if __name__ == "__main__":
    run()
