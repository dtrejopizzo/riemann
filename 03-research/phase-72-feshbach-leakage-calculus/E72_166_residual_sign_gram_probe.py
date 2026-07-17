#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_159_prime_block_psd_probe import relative_matrix  # noqa: E402


def spectral_parts(mat):
    vals, vecs = np.linalg.eigh(mat)
    pos = np.maximum(vals, 0.0)
    neg = np.minimum(vals, 0.0)
    return (vecs * pos) @ vecs.T, (vecs * neg) @ vecs.T


def hs_inner(a, b):
    return float(np.sum(a * b))


def row(lam, n_modes, cut=0.60, a=0.70, b=0.60):
    idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
    krel = relative_matrix(c_actual - c_model, c_model)
    k0, k1 = two_blocks(lam, idx, L, bq, c_model, cut)
    p0, n0 = spectral_parts(k0)
    p1, n1 = spectral_parts(k1)
    pieces = [
        ("r0p", (1.0 - a) * p0),
        ("n0", n0),
        ("r1p", (1.0 - b) * p1),
        ("n1", n1),
    ]
    residual = sum(mat for _, mat in pieces)
    norms = {name: norm(mat, "fro") for name, mat in pieces}
    diag_energy = sum(v * v for v in norms.values())
    cross_energy = 0.0
    min_cos = 1.0
    max_cos = -1.0
    for i, (_, mi) in enumerate(pieces):
        for _, mj in pieces[i + 1 :]:
            ni = norm(mi, "fro")
            nj = norm(mj, "fro")
            ip = hs_inner(mi, mj)
            cross_energy += 2.0 * ip
            if ni * nj > 1e-30:
                cos = ip / (ni * nj)
                min_cos = min(min_cos, cos)
                max_cos = max(max_cos, cos)
    return {
        "lam": lam,
        "L": L,
        "dist": norm(krel - a * p0 - b * p1, "fro"),
        "res": norm(residual, "fro"),
        "diag": diag_energy,
        "cross": cross_energy,
        "cancel": -cross_energy / max(diag_energy, 1e-30),
        "min_cos": min_cos,
        "max_cos": max_cos,
        **norms,
    }


def run():
    print("E72.166 residual sign-Gram probe")
    print("cut=0.60, a=0.70, b=0.60")
    print(
        " lam    L   dist  diagE  crossE  cancel "
        " ||r0p|| ||n0|| ||r1p|| ||n1||  minCos maxCos"
    )
    for lam, n_modes in [
        (6, 18),
        (8, 24),
        (10, 28),
        (12, 32),
        (14, 36),
        (16, 40),
        (18, 44),
        (20, 48),
        (22, 52),
        (24, 56),
    ]:
        s = row(lam, n_modes)
        print(
            f"{lam:4.0f} {s['L']:5.2f} {s['dist']:6.3f} "
            f"{s['diag']:6.3f} {s['cross']:7.3f} {s['cancel']:7.3f} "
            f"{s['r0p']:7.3f} {s['n0']:6.3f} {s['r1p']:7.3f} {s['n1']:6.3f} "
            f"{s['min_cos']:7.3f} {s['max_cos']:6.3f}"
        )
        sys.stdout.flush()


if __name__ == "__main__":
    run()
