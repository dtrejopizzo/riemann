#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402
from E72_232_low_edge_subspace_probe import subspace_coords  # noqa: E402
from E72_233_low_two_block_tail_probe import orth_complement  # noqa: E402


WINDOWS = [(32, 72), (36, 80), (40, 88), (48, 104), (56, 120)]
GRID = np.linspace(0.6001, 0.999, 301)


def rel_m(idx, L, bq, chol, u):
    raw = bq.T @ u_matrix(idx, L, u * L) @ bq
    x = solve(chol, raw)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.conj().T)


def high_prime_average(lam, L, k1_func):
    maxn = int(lam * lam)
    total = 0.0
    mass = 0.0
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        while pm <= maxn:
            u = np.log(pm) / L
            if u > 0.60:
                beta = lp * pm ** -0.5
                total += beta * k1_func(u)
                mass += beta
            if pm > maxn // p:
                break
            pm *= p
    return total / mass, total


def run():
    print("E72.253 HOC3/K1 extended stress")
    print("tailFull=||D||op(TrD2+3||C||HS2); no D_+ except comparison to lambda=32.")
    print("lam L dim low tailFull margin TrA13 K1avg primeAvg sumBetaK1 status")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        p = subspace_coords(idx, k, bq, [0, 1])
        r = orth_complement(p, a.shape[0])
        b = p.conj().T @ a @ p
        dmat = r.conj().T @ a @ r
        c = p.conj().T @ a @ r
        low = -float((np.trace(b @ b @ b) + 3.0 * np.trace(b @ c @ c.conj().T)).real)
        vals = eigvalsh(dmat)
        dop = float(max(abs(vals[0]), abs(vals[-1])))
        tail = dop * (float(np.trace(dmat @ dmat).real) + 3.0 * float(norm(c, "fro") ** 2))
        tr3 = float(np.trace(a @ a @ a).real)

        chol = cholesky(c_model)

        def k1_func(u):
            m = rel_m(idx, L, bq, chol, float(u))
            g = p.conj().T @ m @ p
            return float(np.trace(g).real)

        k1_vals = np.array([k1_func(u) for u in GRID])
        k1_avg = float(np.trapezoid(k1_vals, GRID) / (GRID[-1] - GRID[0]))
        prime_avg, sum_beta_k1 = high_prime_average(lam, L, k1_func)
        status = "PASS" if low >= tail and tr3 <= 1.0e-12 and sum_beta_k1 > 0 else "FAIL"
        print(
            f"{lam:3.0f} {L:.6f} {bq.shape[1]:3d} "
            f"{low:.6e} {tail:.6e} {low-tail:+.6e} {tr3:+.6e} "
            f"{k1_avg:+.6e} {prime_avg:+.6e} {sum_beta_k1:+.6e} {status}",
            flush=True,
        )


if __name__ == "__main__":
    run()
