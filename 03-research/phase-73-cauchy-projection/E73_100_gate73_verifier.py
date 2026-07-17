#!/usr/bin/env python3
import sys
import math

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_051_far_tail_quant_probe import terms  # noqa: E402
from E73_055_far3_nodewise_verifier import certificate_rows  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact, far3_rows  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_090_lock_comp_budget_probe import lock_comp_sum  # noqa: E402
from E73_093_tail_lc_budget_probe import active_cutoff_from_d, local_g_sum  # noqa: E402


def gate_values(lam, n_modes, sigma, tau, m, ncrit=12, nwin=3):
    d, L, xi, _ = setup_exact(lam, n_modes)
    _, far_rows = far3_rows(lam, n_modes, sigma, tau, m, ncrit)
    s_far = sum(row["pref"] for row in far_rows)

    # Gate 1: LOCK-COMP-BUD with the same crude coefficient constant as E73.090.
    nlock, ncomp, tags = lock_comp_sum(tau, nwin, d, xi, -8.0, L)
    nlc = nlock + ncomp
    lock_const = 4.0 * (1.0 + math.exp(sigma * L)) / sigma
    lock_budget = lock_const * s_far * nlc

    # Gate 2: TAIL-LC-BUD with unit compact kernel constant.
    M = active_cutoff_from_d(d, L)
    tail_scale = math.exp(sigma * L) * L * L / (M * M)
    tail_budget = s_far * tail_scale * local_g_sum(tau, nwin, d, xi, L)

    # Gate 3: finite OUT-FAR complement.  OUT-HIGH is analytic E72.394, not numerically added here.
    _, out_rows = terms(lam, n_modes, sigma, tau, m, ncrit)
    selected = sorted(out_rows, reverse=True, key=lambda row: row[1])[:3]
    ids = {row[2] for row in selected}
    out_budget = sum(row[0] for row in out_rows if row[2] not in ids)

    # Gate 4: FAR3-MAIN-RAT.
    _, cert_rows = certificate_rows(lam, n_modes, sigma, tau, m, ncrit)
    main_budget = sum(row["term"] for row in cert_rows if row["part"] == "main")

    return {
        "L": L,
        "M": M,
        "lock": lock_budget,
        "tail": tail_budget,
        "out": out_budget,
        "main": main_budget,
        "tags": ",".join(tags),
    }


def run():
    print("E73.100 unified GATE-73 verifier")
    print("Targets: LOCK<=L^-5, TAIL<=L^-5, OUT<=L^-9, MAIN<=L^-5.")
    print("OUT is the finite FAR complement; OUT-HIGH is the analytic E72.394 tail.")
    print(" lam     L tau    M    lockB  tailB    outB   mainB status tags")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            vals = gate_values(lam, n_modes, sigma, tau, m)
            L = vals["L"]
            lock_b = bexp(vals["lock"], L)
            tail_b = bexp(vals["tail"], L)
            out_b = bexp(vals["out"], L)
            main_b = bexp(vals["main"], L)
            ok = lock_b <= -5.0 and tail_b <= -5.0 and out_b <= -9.0 and main_b <= -5.0
            print(
                f"{lam:4d} {L:7.3f} {tau:7.2f} {vals['M']:4d}"
                f" {lock_b:8.3f} {tail_b:7.3f} {out_b:7.3f} {main_b:7.3f}"
                f" {'PASS' if ok else 'FAIL':>6s} {vals['tags']}"
            )


if __name__ == "__main__":
    run()
