#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_055_far3_nodewise_verifier import setup_full, finite_roots_signed, cauchy_real  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_090_lock_comp_budget_probe import lock_comp_sum  # noqa: E402
from E73_093_tail_lc_budget_probe import active_cutoff_from_d, local_g_sum  # noqa: E402
from E73_113_possible_set_box_verifier import row_intervals, possible_rows  # noqa: E402


def max_alpha_lock(alpha0, alpha1, L):
    def f(alpha):
        return 4.0 * (1.0 + math.exp(alpha * L)) / alpha

    # The derivative equation is exp(aL)(aL-1)=1.  Include a bisection
    # critical point when it lies in the interval.
    pts = [alpha0, alpha1]
    lo, hi = alpha0, alpha1
    glo = math.exp(lo * L) * (lo * L - 1.0) - 1.0
    ghi = math.exp(hi * L) * (hi * L - 1.0) - 1.0
    if glo * ghi <= 0.0:
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            gmid = math.exp(mid * L) * (mid * L - 1.0) - 1.0
            if glo * gmid <= 0.0:
                hi = mid
                ghi = gmid
            else:
                lo = mid
                glo = gmid
        pts.append(0.5 * (lo + hi))
    return max(f(a) for a in pts)


def finite_diff_sup(values, xs):
    slopes = []
    for a, b, xa, xb in zip(values[:-1], values[1:], xs[:-1], xs[1:]):
        slopes.append(abs(b - a) / max(abs(xb - xa), 1e-300))
    return max(slopes) if slopes else 0.0


def sampled_sup_with_lip(fn, tau0, tau1, grid_n=9):
    taus = np.linspace(tau0, tau1, grid_n)
    vals = [fn(float(tau)) for tau in taus]
    lip = finite_diff_sup(vals, taus)
    radius = 0.5 * (tau1 - tau0) / max(grid_n - 1, 1)
    return max(vals) + lip * radius, max(vals), lip


def far_box_budget(lam, n_modes, alpha0, alpha1, tau0, tau1, m, ncrit=12):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    rows = [
        row_intervals(L, d, xi, roots, alpha0, alpha1, tau0, tau1, gamma, m)
        for gamma in GAMMAS[:ncrit]
    ]
    poss = possible_rows(rows)
    far_worst = sorted(poss, reverse=True, key=lambda row: row["far_up"])[:3]
    s_far = sum(row["far_up"] for row in far_worst)
    main_worst = sorted(poss, reverse=True, key=lambda row: row["budget_up"])[:3]
    main_box = sum(row["budget_up"] for row in main_worst)
    return d, L, xi, rows, poss, s_far, main_box


def out_row_bounds(L, d, xi, roots, alpha0, alpha1, tau0, tau1, m, rows):
    bounds = []
    for row in rows:
        gamma = row["gamma"]
        t = -gamma
        c = abs(cauchy_real(t, d, xi))
        o_up = row["budget_up"] / (L**5)
        # Lower bound by coarse sampling only; this is a pilot term, not a
        # rigorous interval lower bound.
        samples = []
        for alpha in np.linspace(alpha0, alpha1, 5):
            for tau in np.linspace(tau0, tau1, 5):
                a = alpha + 1j * tau
                beta = 1j * gamma - a
                w0 = 1.0 / (2.0 * a)
                wstar = -1.0 / beta
                dist = abs(wstar - w0)
                theta = 0.5
                radius = theta * dist
                major = 1.0 / (abs(beta) * (1.0 - theta) * dist)
                total = 0.0
                for p in range(m):
                    inner = 0.0
                    for rr in range(p, m):
                        inner += math.comb(rr, p) * (abs(w0) ** (rr - p)) * (radius ** (-rr))
                    total += inner / math.factorial(p)
                geom = major * total
                mesh = abs(1.0 - cmath.exp(1j * gamma * L))
                samples.append(math.exp(alpha * L) * geom * mesh * c)
        bounds.append(
            {
                "gamma": gamma,
                "far_low": row["far_low"],
                "far_up": row["far_up"],
                "up": o_up,
                "low_sample": min(samples),
            }
        )
    return bounds


def compatible_top_triples(out_bounds, poss_gammas):
    poss = [row for row in out_bounds if row["gamma"] in poss_gammas]
    triples = []
    for i in range(len(poss)):
        for j in range(i + 1, len(poss)):
            for k in range(j + 1, len(poss)):
                sel = [poss[i], poss[j], poss[k]]
                sel_g = {row["gamma"] for row in sel}
                outside = [row for row in out_bounds if row["gamma"] not in sel_g]
                # Necessary interval-order compatibility for being the top-three
                # FAR rows: no outside row is forced above a selected row.
                max_out_low = max((row["far_low"] for row in outside), default=0.0)
                min_sel_up = min(row["far_up"] for row in sel)
                if max_out_low <= min_sel_up:
                    triples.append(sel)
    return triples


def verify_box(lam, n_modes, alpha0, alpha1, tau0, tau1, m):
    d, L, xi, rows, poss, s_far, main_box = far_box_budget(
        lam, n_modes, alpha0, alpha1, tau0, tau1, m
    )
    nwin = 3
    lock_exp_cut = -8.0
    m_cut = active_cutoff_from_d(d, L)
    a_lock = max_alpha_lock(alpha0, alpha1, L)

    nlc_up, nlc_sample, nlc_lip = sampled_sup_with_lip(
        lambda tau: sum(lock_comp_sum(tau, nwin, d, xi, lock_exp_cut, L)[:2]),
        tau0,
        tau1,
    )
    gloc_up, gloc_sample, gloc_lip = sampled_sup_with_lip(
        lambda tau: local_g_sum(tau, nwin, d, xi, L),
        tau0,
        tau1,
    )

    lock_box = a_lock * s_far * nlc_up
    tail_box = s_far * math.exp(alpha1 * L) * L * L / (m_cut * m_cut) * gloc_up

    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:12]) + 10.0)
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
        total_up = sum(row["up"] for row in out_bounds)
        out_box = total_up

    return {
        "L": L,
        "M": m_cut,
        "main": main_box,
        "sfar": s_far,
        "lock": lock_box,
        "tail": tail_box,
        "out": out_box,
        "nlc_sample": nlc_sample,
        "nlc_lip": nlc_lip,
        "gloc_sample": gloc_sample,
        "gloc_lip": gloc_lip,
        "poss": poss,
        "ntriples": len(triples),
    }


def run():
    print("E73.116 LOCK/TAIL/OUT box-domination pilot")
    print("MAIN/SFAR use E73.112 possible-set boxes.")
    print("NLC/Gloc use sampled tau sup plus finite-difference inflation.")
    print("OUT enumerates interval-order compatible FAR triples and sums row upper bounds outside them.")
    print("This is a pilot for E73.115, not the final interval theorem.")
    print(" lam     L box                         lockB  tailB    outB mainBox nTri status")
    boxes = []
    for tau in [GAMMAS[0], GAMMAS[1]]:
        boxes.append((0.15, 0.25, tau - 0.50, tau + 0.50))
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        for alpha0, alpha1, tau0, tau1 in boxes:
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


if __name__ == "__main__":
    run()
