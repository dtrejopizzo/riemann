#!/usr/bin/env python3
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_084_weighted_hwin_probe import hwin  # noqa: E402
from E73_116_box_domination_pilot import compatible_top_triples, far_box_budget, out_row_bounds  # noqa: E402
from E73_117_exact_local_box_verifier import local_window_breakpoints  # noqa: E402


def exact_lock_for_triple(L, d, xi, triple, alpha, ws):
    total = 0.0
    for row in triple:
        gamma = row["gamma"]
        z = alpha + 1j * gamma
        # Use the row prefactor upper already certified on the box.
        pref_up = row["up"] / max(abs(sum(xi / (-gamma - d))), 1e-300)
        total += pref_up * hwin(z, ws, L, d, xi)
    return total


def verify_low_box(lam, n_modes, alpha0, alpha1, tau0, tau1, m, grid_alpha=9):
    d, L, xi, rows, poss, _, main_box = far_box_budget(
        lam, n_modes, alpha0, alpha1, tau0, tau1, m
    )
    out_bounds = out_row_bounds(L, d, xi, [], alpha0, alpha1, tau0, tau1, m, rows)
    poss_gammas = {row["gamma"] for row in poss}
    triples = compatible_top_triples(out_bounds, poss_gammas)
    if not triples:
        return L, main_box, 0, float("inf")

    taus = local_window_breakpoints(tau0, tau1, list(GAMMAS[:12]))
    alphas = np.linspace(alpha0, alpha1, grid_alpha)
    worst = 0.0
    for tau in taus:
        ws_g = sorted(list(GAMMAS[:12]), key=lambda g: (abs(g - tau), g))[:3]
        ws = [1j * g for g in ws_g]
        for alpha in alphas:
            for triple in triples:
                worst = max(worst, exact_lock_for_triple(L, d, xi, triple, alpha, ws))
    return L, main_box, len(triples), worst


def run():
    print("E73.118 low-scale exact LOCK base probe")
    print("Uses exact HWIN on compatible FAR triples; alpha is gridded, tau windows exact.")
    print("This is a base-case probe, not yet an interval alpha certificate.")
    print(" lam     L box                         lockExactB mainBox nTri status")
    for tau in [GAMMAS[0], GAMMAS[1]]:
        L, main_box, ntri, lock = verify_low_box(16, 20, 0.15, 0.25, tau - 0.50, tau + 0.50, 3)
        lock_b = bexp(lock, L)
        ok = lock_b <= -5.0 and main_box <= 1.0
        print(
            f"{16:4d} {L:7.3f} [{0.15:.2f},{0.25:.2f}]x[{tau-0.50:5.2f},{tau+0.50:5.2f}]"
            f" {lock_b:10.3f} {main_box:7.3e} {ntri:4d} {'PASS' if ok else 'FAIL'}"
        )


if __name__ == "__main__":
    run()
