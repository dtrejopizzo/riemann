#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def relative_cell(idx, L, bq, c_model, nval):
    chol = cholesky(c_model)
    y = np.log(nval)
    raw = bq.T @ u_matrix(idx, L, y) @ bq
    x = solve(chol, raw)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.conj().T)


def prime_powers(lam):
    maxn = int(lam * lam)
    out = []
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            out.append((pm, lp * pm ** -0.5, me, p))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return out


def run():
    print("E72.227 cellwise cubic sign probe")
    print("M_n=relative compressed U_logn cell before the -Lambda(n)/sqrt(n) sign")
    print("For A_n=-beta M_n, high block wants Tr(A_n^3)<=0, i.e. Tr(M_n^3)>=0")
    print("lam block cells minTrM3 maxTrM3 badCells sumCellTrA3 sumAggTrA3 crossFrac worstN")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block in [0, 1]:
            mats = []
            trs_m = []
            trs_a = []
            bad = []
            for nval, beta, me, p in prime_powers(lam):
                u = np.log(nval) / L
                bid = 0 if u <= 0.60 else 1
                if bid != block:
                    continue
                m = relative_cell(idx, L, bq, c_model, nval)
                a = -beta * m
                tm = float(np.real(np.trace(m @ m @ m)))
                ta = float(np.real(np.trace(a @ a @ a)))
                mats.append(a)
                trs_m.append(tm)
                trs_a.append(ta)
                if (block == 1 and ta > 1.0e-12) or (block == 0 and ta < -1.0e-12):
                    bad.append((abs(ta), nval, ta, tm))
            agg = sum(mats, np.zeros_like(mats[0])) if mats else None
            sum_cell = float(np.sum(trs_a))
            agg_tr = float(np.real(np.trace(agg @ agg @ agg))) if agg is not None else 0.0
            cross = (agg_tr - sum_cell) / max(abs(agg_tr), 1.0e-30)
            worst = max(bad)[1] if bad else "-"
            print(
                f"{lam:3.0f} {block:5d} {len(mats):5d} "
                f"{min(trs_m):+.3e} {max(trs_m):+.3e} {len(bad):8d} "
                f"{sum_cell:+.6e} {agg_tr:+.6e} {cross:+.3e} {worst}",
                flush=True,
            )


if __name__ == "__main__":
    run()
