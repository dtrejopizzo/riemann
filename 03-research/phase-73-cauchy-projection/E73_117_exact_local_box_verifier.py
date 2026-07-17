#!/usr/bin/env python3
import sys
import math

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_090_lock_comp_budget_probe import lock_comp_sum  # noqa: E402
from E73_093_tail_lc_budget_probe import active_cutoff_from_d, local_g_sum  # noqa: E402
from E73_116_box_domination_pilot import (  # noqa: E402
    compatible_top_triples,
    far_box_budget,
    max_alpha_lock,
    out_row_bounds,
)


def local_window_breakpoints(tau0, tau1, pool):
    pts = [tau0, tau1]
    for a, b in zip(pool[:-1], pool[1:]):
        mid = 0.5 * (a + b)
        if tau0 < mid < tau1:
            pts.append(mid)
    pts = sorted(set(round(p, 14) for p in pts))
    probes = []
    for a, b in zip(pts[:-1], pts[1:]):
        probes.append(0.5 * (a + b))
    probes.extend(pts)
    return sorted(set(probes))


def exact_local_sup(fn, tau0, tau1, ncrit=12):
    pool = list(GAMMAS[:ncrit])
    probes = local_window_breakpoints(tau0, tau1, pool)
    vals = [(tau, fn(tau)) for tau in probes]
    return max(v for _, v in vals), vals


def verify_box(lam, n_modes, alpha0, alpha1, tau0, tau1, m):
    d, L, xi, rows, poss, s_far, main_box = far_box_budget(
        lam, n_modes, alpha0, alpha1, tau0, tau1, m
    )
    nwin = 3
    lock_exp_cut = -8.0
    m_cut = active_cutoff_from_d(d, L)
    a_lock = max_alpha_lock(alpha0, alpha1, L)

    nlc_up, nlc_vals = exact_local_sup(
        lambda tau: sum(lock_comp_sum(tau, nwin, d, xi, lock_exp_cut, L)[:2]),
        tau0,
        tau1,
    )
    gloc_up, gloc_vals = exact_local_sup(
        lambda tau: local_g_sum(tau, nwin, d, xi, L),
        tau0,
        tau1,
    )

    lock_box = a_lock * s_far * nlc_up
    tail_box = s_far * math.exp(alpha1 * L) * L * L / (m_cut * m_cut) * gloc_up

    roots = []
    out_bounds = out_row_bounds(L, d, xi, roots, alpha0, alpha1, tau0, tau1, m, rows)
    poss_gammas = {row["gamma"] for row in poss}
    triples = compatible_top_triples(out_bounds, poss_gammas)
    if triples:
        out_box = 0.0
        for triple in triples:
            selected = {row["gamma"] for row in triple}
            tail = sum(row["up"] for row in out_bounds if row["gamma"] not in selected)
            out_box = max(out_box, tail)
    else:
        out_box = sum(row["up"] for row in out_bounds)

    return {
        "L": L,
        "M": m_cut,
        "main": main_box,
        "sfar": s_far,
        "lock": lock_box,
        "tail": tail_box,
        "out": out_box,
        "nlc_up": nlc_up,
        "gloc_up": gloc_up,
        "nlc_probes": len(nlc_vals),
        "gloc_probes": len(gloc_vals),
        "ntriples": len(triples),
    }


def run_case(label, cases):
    print(label)
    print(" lam     L box                         lockB  tailB    outB mainBox nTri status")
    for lam, n_modes, alpha0, alpha1, tau0, tau1 in cases:
        vals = verify_box(lam, n_modes, alpha0, alpha1, tau0, tau1, 3)
        L = vals["L"]
        lock_b = bexp(vals["lock"], L)
        tail_b = bexp(vals["tail"], L)
        out_b = bexp(vals["out"], L)
        ok = lock_b <= -5.0 and tail_b <= -5.0 and out_b <= -9.0 and vals["main"] <= 1.0
        print(
            f"{lam:4d} {L:7.3f} [{alpha0:.2f},{alpha1:.2f}]x[{tau0:5.2f},{tau1:5.2f}]"
            f" {lock_b:7.3f} {tail_b:7.3f} {out_b:7.3f} {vals['main']:7.3e}"
            f" {vals['ntriples']:4d} {'PASS' if ok else 'FAIL'}"
        )


def run():
    print("E73.117 exact-local box verifier")
    print("NLC/Gloc suprema are exact over tau boxes by nearest-zero cell enumeration.")
    print("OUT uses interval-order compatible FAR triples.")
    wide = []
    for tau in [GAMMAS[0], GAMMAS[1]]:
        for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
            wide.append((lam, n_modes, 0.15, 0.25, tau - 0.50, tau + 0.50))
    run_case("Wide boxes", wide)

    low20 = []
    tau = GAMMAS[0]
    for a0, a1 in [(0.15, 0.20), (0.20, 0.25)]:
        for j in range(4):
            t0 = tau - 0.50 + 0.25 * j
            t1 = tau - 0.50 + 0.25 * (j + 1)
            low20.append((20, 24, a0, a1, t0, t1))
    tau = GAMMAS[1]
    for j in range(4):
        t0 = tau - 0.50 + 0.25 * j
        t1 = tau - 0.50 + 0.25 * (j + 1)
        low20.append((20, 24, 0.15, 0.25, t0, t1))
    run_case("Lambda 20 finite subdivision", low20)


if __name__ == "__main__":
    run()

