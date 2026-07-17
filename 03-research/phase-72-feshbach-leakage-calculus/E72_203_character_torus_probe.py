#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, eigvalsh, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


def relative_matrix_raw(mat, c_model):
    chol = cholesky(c_model)
    x = solve(chol, mat)
    return solve(chol, x.T).T


def signed_data(lam, idx, L, bq, c_model, cut=0.60, block_id=0):
    ans = []
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            bid = 0 if y <= cut * L else 1
            if bid == block_id:
                beta = lp * (pm ** -0.5)
                u = u_matrix(idx, L, y)
                ap = relative_matrix_raw(bq.T @ (-beta * u) @ bq, c_model)
                # Store only plus cell; the character evaluation adds adjoint partner.
                ans.append((y, ap))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return ans


def eval_character(data, t):
    out = np.zeros_like(data[0][1], dtype=complex)
    for y, ap in data:
        z = np.exp(1j * t * y)
        out += z * ap + np.conj(z) * ap.conj().T
    return 0.5 * (out + out.conj().T)


def scan_block(data, ts):
    vals = []
    for t in ts:
        ev = eigvalsh(eval_character(data, t))
        vals.append((float(np.max(np.abs(ev))), t, float(ev[0]), float(ev[-1])))
    return max(vals, key=lambda x: x[0]), vals[0]


def run():
    print("E72.203 character torus norm probe")
    print("scans chi_t(n)=exp(i t log n); t=0 is augmentation")
    print("lam block op_t0 maxOp t_at_max minEig maxEig passNTCbound")
    ts = np.linspace(0.0, 40.0, 401)
    for lam, n_modes in [(12, 32), (16, 40), (20, 48), (24, 56)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block_id, bound in [(0, 0.90), (1, 0.60)]:
            data = signed_data(lam, idx, L, bq, c_model, 0.60, block_id)
            worst, at0 = scan_block(data, ts)
            print(
                f"{lam:3.0f} {block_id:5d} {at0[0]:6.3f} {worst[0]:6.3f} "
                f"{worst[1]:7.3f} {worst[2]:+7.3f} {worst[3]:+7.3f} "
                f"{'YES' if worst[0] < bound else 'NO'}"
            )


if __name__ == "__main__":
    run()
