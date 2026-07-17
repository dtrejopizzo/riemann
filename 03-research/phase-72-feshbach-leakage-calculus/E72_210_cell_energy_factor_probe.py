#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56)]


def raw_rel_norm2(idx, L, bq, chol, y):
    u = u_matrix(idx, L, y)
    raw = bq.T @ u @ bq
    x = solve(chol, raw)
    rel = solve(chol, x.T).T
    return float(norm(rel, "fro") ** 2)


def cells(lam, idx, L, bq, c_model, cut=0.60):
    ans = []
    chol = cholesky(c_model)
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            beta2 = (lp * (pm ** -0.5)) ** 2
            geom = raw_rel_norm2(idx, L, bq, chol, y)
            block = 0 if y <= cut * L else 1
            ans.append((pm, y, y / L, block, beta2, geom, 2.0 * beta2 * geom))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans


def run():
    print("E72.210 cell energy factor probe")
    print("Res2 cell = 2 (Lambda(n)^2/n) * Geom_x(log n)")
    print("lam block cells Res2 beta2Sum geomMean geomMax topCell topFrac")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        rows = cells(lam, idx, L, bq, c_model)
        for block in [0, 1]:
            br = [r for r in rows if r[3] == block]
            res = sum(r[6] for r in br)
            bsum = sum(r[4] for r in br)
            gmean = sum(r[4] * r[5] for r in br) / max(bsum, 1e-300)
            gmax = max(r[5] for r in br)
            top = max(br, key=lambda r: r[6])
            print(
                f"{lam:3.0f} {block:5d} {len(br):5d} {res:.6e} "
                f"{bsum:.6e} {gmean:.6e} {gmax:.6e} "
                f"{top[0]:4d}@{top[2]:.3f} {top[6]/res:.3f}",
                flush=True,
            )

    print("\nTop cells at lambda=24")
    idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(24, 56)
    rows = cells(24, idx, L, bq, c_model)
    rows.sort(reverse=True, key=lambda r: r[6])
    print("rank n y/L block beta2 geom cellRes fracTotal")
    total = sum(r[6] for r in rows)
    for rank, r in enumerate(rows[:16], start=1):
        print(
            f"{rank:2d} {r[0]:4d} {r[2]:.3f} {r[3]:1d} "
            f"{r[4]:.3e} {r[5]:.3e} {r[6]:.3e} {r[6]/total:.3f}"
        )


if __name__ == "__main__":
    run()
