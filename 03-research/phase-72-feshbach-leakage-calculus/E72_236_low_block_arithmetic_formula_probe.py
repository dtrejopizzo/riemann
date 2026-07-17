#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402
from E72_232_low_edge_subspace_probe import subspace_coords  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def high_sums(lam, L, cut=0.60):
    out = {
        "s0": 0.0,
        "s1mu": 0.0,
        "sc": 0.0,
        "ss": 0.0,
        "sc1": 0.0,
        "ss1": 0.0,
        "count": 0,
    }
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        while pm <= maxn:
            u = np.log(pm) / L
            if u > cut:
                beta = lp * pm ** -0.5
                phase = 2.0 * np.pi * u
                out["s0"] += beta
                out["s1mu"] += beta * (1.0 - u)
                out["sc"] += beta * np.cos(phase)
                out["ss"] += beta * np.sin(phase)
                out["sc1"] += beta * (1.0 - u) * np.cos(phase)
                out["ss1"] += beta * (1.0 - u) * np.sin(phase)
                out["count"] += 1
            if pm > maxn // p:
                break
            pm *= p
    return out


def run():
    print("E72.236 low-block arithmetic formula probe")
    print("B=P01 A_1 P01 in an orthonormal Q-projected {0,1} basis")
    print("lam cnt B00 B01 B11 eig0 eig1 TrB3 s0 s1mu sc ss sc1 ss1")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        p = subspace_coords(idx, k, bq, [0, 1])
        b = p.conj().T @ a @ p
        vals = eigvalsh(b)
        trb3 = float(np.trace(b @ b @ b).real)
        hs = high_sums(lam, L)
        print(
            f"{lam:3.0f} {hs['count']:3d} "
            f"{b[0,0].real:+.6e} {b[0,1].real:+.6e} {b[1,1].real:+.6e} "
            f"{vals[0]:+.6e} {vals[-1]:+.6e} {trb3:+.6e} "
            f"{hs['s0']:.6e} {hs['s1mu']:.6e} {hs['sc']:+.6e} {hs['ss']:+.6e} "
            f"{hs['sc1']:+.6e} {hs['ss1']:+.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
