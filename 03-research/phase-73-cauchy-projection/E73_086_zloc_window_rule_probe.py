#!/usr/bin/env python3
import sys

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact, far3_rows  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_084_weighted_hwin_probe import hwin  # noqa: E402


def nearest_gammas(center, nwin, pool):
    return sorted(pool, key=lambda g: (abs(g - center), g))[:nwin]


def window(rule, tau, eval_gamma, nwin, far_gammas, pool):
    if rule == "prefix":
        return list(pool[:nwin])
    if rule == "tau-near":
        return nearest_gammas(tau, nwin, pool)
    if rule == "eval-near":
        return nearest_gammas(eval_gamma, nwin, pool)
    if rule == "far-set":
        return list(far_gammas[:nwin])
    raise ValueError(rule)


def run():
    rules = ["prefix", "tau-near", "eval-near", "far-set"]
    cases = [(16, 20), (18, 22), (20, 24), (24, 28)]
    pool = list(GAMMAS[:12])
    print("E73.086 Zloc window-rule probe")
    print("Compares weighted HWIN under non-optimized window rules.")
    print("prefix   = first n zero nodes; tau-near = nearest to off-line cluster height")
    print("eval-near= nearest to FAR evaluation row; far-set = the FAR3 rows themselves")
    print(" lam     L tau rule      nwin     sumB     maxB   worst_gamma   window")
    for lam, n_modes in cases:
        d, L, xi, _ = setup_exact(lam, n_modes)
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            _, rows = far3_rows(lam, n_modes, sigma, tau, m, 12)
            far_gammas = [row["gamma"] for row in rows]
            for rule in rules:
                for nwin in [3, 5]:
                    total = 0.0
                    worst = (0.0, None, None)
                    for row in rows:
                        ws_real = window(rule, tau, row["gamma"], nwin, far_gammas, pool)
                        ws = [1j * g for g in ws_real]
                        weighted = row["pref"] * hwin(
                            sigma + 1j * row["gamma"], ws, L, d, xi
                        )
                        total += weighted
                        if weighted > worst[0]:
                            worst = (weighted, row["gamma"], ws_real)
                    print(
                        f"{lam:4d} {L:7.3f} {tau:7.2f} {rule:9s} {nwin:4d}"
                        f" {bexp(total, L):8.3f} {bexp(worst[0], L):8.3f}"
                        f" {worst[1]:12.2f} "
                        + ",".join(f"{g:.2f}" for g in worst[2])
                    )


if __name__ == "__main__":
    run()
