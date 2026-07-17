#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact, far3_rows  # noqa: E402
from E73_071_packet_mellin_formula_verifier import h0  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_088_local_root_locking_probe import local_window  # noqa: E402
from E73_090_lock_comp_budget_probe import lock_comp_sum  # noqa: E402


def active_cutoff_from_d(d, L):
    idx = np.rint(d * L / (2.0 * math.pi)).astype(int)
    return int(np.max(np.abs(idx)))


def local_g_sum(tau, nwin, d, xi, L):
    total = 0.0
    for gamma in local_window(tau, nwin):
        for w in (1j * gamma, -1j * gamma):
            total += abs(w) * abs(1.0 - cmath.exp(w * L)) * abs(h0(w, d, xi))
    return total


def run():
    sigma = 0.20
    m = 3
    ncrit = 12
    nwin = 3
    lock_exp_cut = -8.0
    print("E73.093 tail LC budget probe")
    print("Compares local G-node tail budget with LOCK/COMP nodal budget.")
    print("Tail scale shown with unit kernel constant: e^(sigma L)L^2/M^2.")
    print(" lam     L tau    M    SFARB    GsumB     NLCB tailSuffB lcTailB ratio")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        M = active_cutoff_from_d(d, L)
        tail_scale = math.exp(sigma * L) * L * L / (M * M)
        for tau in [GAMMAS[0], GAMMAS[1]]:
            _, rows = far3_rows(lam, n_modes, sigma, tau, m, ncrit)
            s_far = sum(row["pref"] for row in rows)
            gsum = local_g_sum(tau, nwin, d, xi, L)
            nlock, ncomp, _ = lock_comp_sum(tau, nwin, d, xi, lock_exp_cut, L)
            nlc = nlock + ncomp
            tail_suff = s_far * tail_scale * gsum
            lc_tail = s_far * tail_scale * nlc * max(GAMMAS[:nwin])
            ratio = tail_suff / max(lc_tail, 1e-300)
            print(
                f"{lam:4d} {L:7.3f} {tau:7.2f} {M:4d}"
                f" {bexp(s_far, L):8.3f} {bexp(gsum, L):8.3f}"
                f" {bexp(nlc, L):8.3f} {bexp(tail_suff, L):9.3f}"
                f" {bexp(lc_tail, L):8.3f} {ratio:7.3f}"
            )


if __name__ == "__main__":
    run()
