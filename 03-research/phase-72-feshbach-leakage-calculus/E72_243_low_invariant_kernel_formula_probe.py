#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402
from E72_232_low_edge_subspace_probe import subspace_coords  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72), (36, 80)]


def high_cells(lam, L, cut=0.60):
    maxn = int(lam * lam)
    out = []
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        while pm <= maxn:
            u = np.log(pm) / L
            if u > cut:
                out.append((pm, lp * pm ** -0.5, u))
            if pm > maxn // p:
                break
            pm *= p
    return out


def rel_m(idx, L, bq, chol, u):
    raw = bq.T @ u_matrix(idx, L, u * L) @ bq
    x = solve(chol, raw)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.conj().T)


def run():
    print("E72.243 low invariant kernel formula probe")
    print("A_1=-sum beta M_u; B=P A_1 P. Checks tB and sB from K1,K2 sums.")
    print("lam cells tDirect tKernel errT sDirect sKernel errS minK1 maxK1 minK2diag maxK2diag")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        chol = cholesky(c_model)
        p = subspace_coords(idx, k, bq, [0, 1])
        cells = high_cells(lam, L)
        blocks = []
        k1s = []
        for _, beta, u in cells:
            mu = rel_m(idx, L, bq, chol, u)
            bu = p.conj().T @ mu @ p
            blocks.append((beta, bu))
            k1s.append(float(np.trace(bu).real))
        t_kernel = -sum(beta * float(np.trace(bu).real) for beta, bu in blocks)
        s_kernel = 0.0
        for beta_a, ba in blocks:
            for beta_b, bb in blocks:
                s_kernel += beta_a * beta_b * float(np.trace(ba @ bb).real)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        b = p.conj().T @ a @ p
        t_direct = float(np.trace(b).real)
        s_direct = float(np.trace(b @ b).real)
        k2diag = [float(np.trace(bu @ bu).real) for _, bu in blocks]
        print(
            f"{lam:3.0f} {len(cells):5d} "
            f"{t_direct:+.6e} {t_kernel:+.6e} {abs(t_direct-t_kernel):.1e} "
            f"{s_direct:.6e} {s_kernel:.6e} {abs(s_direct-s_kernel):.1e} "
            f"{min(k1s):+.3e} {max(k1s):+.3e} "
            f"{min(k2diag):.3e} {max(k2diag):.3e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
