#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact, far3_rows, finite_roots, cauchy_real  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_084_weighted_hwin_probe import hwin  # noqa: E402
from E73_088_local_root_locking_probe import derivative_abs_bound, local_window  # noqa: E402


def h0_abs_at_gamma(gamma, d, xi):
    return abs(cauchy_real(-gamma, d, xi))


def lock_comp_sum(tau, nwin, d, xi, lock_exp_cut, L):
    roots = finite_roots(d, xi, hmax=60.0)
    nlock = 0.0
    ncomp = 0.0
    tags = []
    for gamma in local_window(tau, nwin):
        t0 = -gamma
        root = roots[int(np.argmin(np.abs(roots - t0)))]
        dist = abs(t0 - root)
        der = derivative_abs_bound(t0, root, d, xi)
        actual = h0_abs_at_gamma(gamma, d, xi)
        # Use a scale-invariant diagnostic cutoff only to split the budget.  The theorem uses
        # the sum N_lock+N_comp, so this classification is not used to improve the bound.
        if dist > 0 and bexp(dist, L) <= lock_exp_cut:
            nlock += dist * der
            tags.append(f"{gamma:.2f}:L")
        else:
            ncomp += actual
            tags.append(f"{gamma:.2f}:C")
    # Paired window contributes both +gamma and -gamma; in the real-even harness these are equal.
    return 2.0 * nlock, 2.0 * ncomp, tags


def run():
    sigma = 0.20
    m = 3
    ncrit = 12
    nwin = 3
    lock_exp_cut = -8.0
    print("E73.090 LOCK/COMP budget probe")
    print("Compares exact LOCAL-HWIN with the Theorem 89.3 sufficient budget.")
    print(" lock cutoff: dist <= L^-8; paired +/- contribution included")
    print(" lam     L tau      SFARB   NlockB   NcompB  suffB  exactB  ratio tags")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        coeff_const = 4.0 * (1.0 + math.exp(sigma * L)) / sigma
        for tau in [GAMMAS[0], GAMMAS[1]]:
            _, rows = far3_rows(lam, n_modes, sigma, tau, m, ncrit)
            s_far = sum(row["pref"] for row in rows)
            nlock, ncomp, tags = lock_comp_sum(tau, nwin, d, xi, lock_exp_cut, L)
            suff = coeff_const * s_far * (nlock + ncomp)
            exact = 0.0
            ws = [1j * g for g in local_window(tau, nwin)]
            for row in rows:
                exact += row["pref"] * hwin(sigma + 1j * row["gamma"], ws, L, d, xi)
            ratio = suff / max(exact, 1e-300)
            print(
                f"{lam:4d} {L:7.3f} {tau:7.2f}"
                f" {bexp(s_far, L):8.3f} {bexp(nlock, L):8.3f}"
                f" {bexp(ncomp, L):8.3f} {bexp(suff, L):7.3f}"
                f" {bexp(exact, L):7.3f} {ratio:7.2e} "
                + ",".join(tags)
            )


if __name__ == "__main__":
    run()
