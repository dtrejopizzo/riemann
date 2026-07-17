#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_166_residual_sign_gram_probe import spectral_parts  # noqa: E402


def block_stats(k, a):
    p, n = spectral_parts(k)
    phs2 = norm(p, "fro") ** 2
    nhs2 = norm(n, "fro") ** 2
    hs2 = phs2 + nhs2
    signed_abs = phs2 - nhs2
    energy = ((1.0 - a) ** 2) * phs2 + nhs2
    pos_frac = phs2 / max(hs2, 1e-30)
    return hs2, phs2, nhs2, signed_abs, energy, pos_frac


def run():
    print("E72.168 trace asymmetry probe")
    print("cut=0.60, weights a0=0.70,a1=0.60")
    print(" lam    L  block   HS2    pos2    neg2  posFrac  sigAbs    E")
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
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        for name, mat, weight in [("K0", k0, 0.70), ("K1", k1, 0.60)]:
            hs2, phs2, nhs2, signed_abs, energy, pos_frac = block_stats(mat, weight)
            print(
                f"{lam:4.0f} {L:5.2f} {name:>5s} "
                f"{hs2:6.3f} {phs2:7.3f} {nhs2:7.3f} "
                f"{pos_frac:8.3f} {signed_abs:7.3f} {energy:6.3f}"
            )
        sys.stdout.flush()


if __name__ == "__main__":
    run()
