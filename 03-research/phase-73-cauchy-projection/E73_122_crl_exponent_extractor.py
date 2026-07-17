#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_088_local_root_locking_probe import derivative_abs_bound, local_window  # noqa: E402
from E73_090_lock_comp_budget_probe import lock_comp_sum  # noqa: E402
from E73_093_tail_lc_budget_probe import active_cutoff_from_d, local_g_sum  # noqa: E402
from E73_116_box_domination_pilot import far_box_budget, out_row_bounds, compatible_top_triples  # noqa: E402
from E73_117_exact_local_box_verifier import exact_local_sup  # noqa: E402
from E73_069_exact_far3_row_probe import finite_roots, cauchy_real  # noqa: E402


def crl_rows(d, L, xi, tau, nwin=3):
    roots = finite_roots(d, xi, hmax=60.0)
    rows = []
    for gamma in local_window(tau, nwin):
        t0 = -gamma
        root = roots[int(np.argmin(np.abs(roots - t0)))]
        dist = abs(t0 - root)
        der = derivative_abs_bound(t0, root, d, xi)
        actual = abs(cauchy_real(t0, d, xi))
        rows.append({"gamma": gamma, "dist": dist, "der": der, "actual": actual})
    return rows


def box_metrics(lam, n_modes, alpha0, alpha1, tau0, tau1, m):
    d, L, xi, rows, poss, sfar, main = far_box_budget(lam, n_modes, alpha0, alpha1, tau0, tau1, m)
    nwin = 3
    nlc, _ = exact_local_sup(lambda tau: sum(lock_comp_sum(tau, nwin, d, xi, -8.0, L)[:2]), tau0, tau1)
    gloc, _ = exact_local_sup(lambda tau: local_g_sum(tau, nwin, d, xi, L), tau0, tau1)
    out_bounds = out_row_bounds(L, d, xi, [], alpha0, alpha1, tau0, tau1, m, rows)
    poss_gammas = {row["gamma"] for row in poss}
    triples = compatible_top_triples(out_bounds, poss_gammas)
    if triples:
        out = 0.0
        for triple in triples:
            selected = {row["gamma"] for row in triple}
            out = max(out, sum(row["up"] for row in out_bounds if row["gamma"] not in selected))
    else:
        out = sum(row["up"] for row in out_bounds)

    tau_c = 0.5 * (tau0 + tau1)
    crl = crl_rows(d, L, xi, tau_c, nwin)
    max_dist = max(row["dist"] for row in crl)
    max_der = max(row["der"] for row in crl)
    max_actual = max(row["actual"] for row in crl)
    m_cut = active_cutoff_from_d(d, L)
    return {
        "L": L,
        "M": m_cut,
        "sfar": sfar,
        "nlc": nlc,
        "gloc": gloc,
        "main": main,
        "out": out,
        "dist": max_dist,
        "der": max_der,
        "actual": max_actual,
        "ntriples": len(triples),
    }


def run():
    print("E73.122 CRL exponent extractor")
    print("Standard wide boxes only; exponents are log(value)/log(L).")
    print(
        " lam     L tau      distB    derB      CB   SFARB    NLCB   GlocB"
        "   main   outB nTri"
    )
    for tau in [GAMMAS[0], GAMMAS[1]]:
        for lam, n_modes in [(20, 24), (24, 28), (28, 32), (32, 36)]:
            vals = box_metrics(lam, n_modes, 0.15, 0.25, tau - 0.50, tau + 0.50, 3)
            L = vals["L"]
            print(
                f"{lam:4d} {L:7.3f} {tau:7.2f}"
                f" {bexp(vals['dist'], L):8.3f} {bexp(vals['der'], L):7.3f}"
                f" {bexp(vals['actual'], L):7.3f} {bexp(vals['sfar'], L):7.3f}"
                f" {bexp(vals['nlc'], L):7.3f} {bexp(vals['gloc'], L):7.3f}"
                f" {vals['main']:7.3e} {bexp(vals['out'], L):7.3f} {vals['ntriples']:4d}"
            )


if __name__ == "__main__":
    run()

