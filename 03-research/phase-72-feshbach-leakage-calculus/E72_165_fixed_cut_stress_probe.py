#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_158_prime_cell_psd_probe import q_matrix  # noqa: E402
from E72_159_prime_block_psd_probe import psd_part, relative_matrix  # noqa: E402


def two_blocks(lam, idx, L, bq, c_model, cut=0.60):
    n = len(bq.T)
    mats = [np.zeros((n, n)), np.zeros((n, n))]
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            weight = lp * (pm ** -0.5)
            block = 0 if y <= cut * L else 1
            comp = bq.T @ (-weight * q_matrix(idx, L, y)) @ bq
            mats[block] += relative_matrix(comp, c_model)
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return mats


def row(lam, n_modes, cut=0.60, a=0.70, b=0.60):
    idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
    krel = relative_matrix(c_actual - c_model, c_model)
    blocks = two_blocks(lam, idx, L, bq, c_model, cut)
    p0 = psd_part(blocks[0])
    p1 = psd_part(blocks[1])
    residual = krel - a * p0 - b * p1
    dist = norm(residual, "fro")
    return {
        "lam": lam,
        "L": L,
        "dim": len(idx),
        "dist": dist,
        "margin": 1.0 - dist * dist,
        "krel": norm(krel, "fro"),
        "p0": norm(p0, "fro"),
        "p1": norm(p1, "fro"),
        "res_op": norm(residual, 2),
    }


def run():
    print("E72.165 fixed-cut fixed-weight 2B-PSD stress probe")
    print("cut=0.60, a=0.70, b=0.60")
    print(" lam    L   dim   distHS   margin  ||Krel||  ||P0||  ||P1||  opRes")
    windows = [
        (6, 18),
        (8, 24),
        (10, 28),
        (12, 32),
        (14, 36),
        (16, 40),
        (18, 44),
        (20, 48),
    ]
    worst = None
    for lam, n_modes in windows:
        stats = row(lam, n_modes)
        if worst is None or stats["dist"] > worst["dist"]:
            worst = stats
        print(
            f"{lam:4.0f} {stats['L']:5.2f} {stats['dim']:5d} "
            f"{stats['dist']:8.3f} {stats['margin']:8.3f} "
            f"{stats['krel']:8.3f} {stats['p0']:7.3f} "
            f"{stats['p1']:7.3f} {stats['res_op']:6.3f}"
        )
        sys.stdout.flush()
    print(
        f"worst lambda={worst['lam']:.0f} "
        f"dist={worst['dist']:.3f} margin={worst['margin']:.3f}"
    )


if __name__ == "__main__":
    run()
