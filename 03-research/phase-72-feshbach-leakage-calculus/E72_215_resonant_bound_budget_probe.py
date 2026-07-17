#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64)]


def rows(lam, idx, L, bq, c_model, cut=0.60):
    chol = cholesky(c_model)
    minc = float(eigvalsh(c_model)[0])
    maxn = int(lam * lam)
    ans = []
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            beta2 = (lp * pm**-0.5) ** 2
            u = u_matrix(idx, L, y)
            raw = bq.T @ u @ bq
            x = solve(chol, raw)
            rel = solve(chol, x.T).T
            geom = float(norm(rel, "fro") ** 2)
            raw_hs = float(norm(raw, "fro") ** 2)
            block = 0 if y <= cut * L else 1
            ans.append((block, beta2, geom, raw_hs, y / L, pm))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans, minc


def run():
    print("E72.215 resonant bound budget probe")
    print("actual=2sum beta2*geom; coercive=2sum beta2*raw/minC^2")
    print("univ(K)=2*K/L^2 sum beta2 with K=3,6,12")
    print("lam block actual coercive ratio K3 K6 K12 beta2sum")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        rs, minc = rows(lam, idx, L, bq, c_model)
        for block in [0, 1]:
            br = [r for r in rs if r[0] == block]
            beta2sum = sum(r[1] for r in br)
            actual = 2.0 * sum(r[1] * r[2] for r in br)
            coercive = 2.0 * sum(r[1] * r[3] / (minc * minc) for r in br)
            bounds = [2.0 * k * beta2sum / (L * L) for k in [3.0, 6.0, 12.0]]
            print(
                f"{lam:3.0f} {block:5d} {actual:.6e} {coercive:.6e} "
                f"{coercive/actual:.2f} "
                + " ".join(f"{b:.6e}" for b in bounds)
                + f" {beta2sum:.6e}",
                flush=True,
            )


if __name__ == "__main__":
    run()
