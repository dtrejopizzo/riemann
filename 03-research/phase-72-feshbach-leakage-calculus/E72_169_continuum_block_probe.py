#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_158_prime_cell_psd_probe import q_matrix  # noqa: E402
from E72_159_prime_block_psd_probe import relative_matrix  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_168_trace_asymmetry_probe import block_stats  # noqa: E402


def continuum_block(idx, L, y0, y1, nodes=240):
    xs, ws = np.polynomial.legendre.leggauss(nodes)
    mid = 0.5 * (y0 + y1)
    rad = 0.5 * (y1 - y0)
    mat = np.zeros((len(idx), len(idx)))
    for x, w in zip(xs, ws):
        y = mid + rad * x
        mat += w * np.exp(y / 2.0) * q_matrix(idx, L, y)
    return -rad * mat


def run():
    print("E72.169 continuum block comparison")
    print("continuum block = -int_I exp(y/2) Q_y dy, cut=0.60")
    print(" lam    L block  ||Kp-Kc||  Eprime   Econt  Hcont  Scont/H")
    for lam, n_modes in [
        (6, 18),
        (8, 24),
        (10, 28),
        (12, 32),
        (14, 36),
        (16, 40),
        (18, 44),
        (20, 48),
    ]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        prime_blocks = two_blocks(lam, idx, L, bq, c_model, 0.60)
        raw0 = continuum_block(idx, L, 0.0, 0.60 * L)
        raw1 = continuum_block(idx, L, 0.60 * L, L)
        cont_blocks = [
            relative_matrix(bq.T @ raw0 @ bq, c_model),
            relative_matrix(bq.T @ raw1 @ bq, c_model),
        ]
        for name, kp, kc, weight in [
            ("K0", prime_blocks[0], cont_blocks[0], 0.70),
            ("K1", prime_blocks[1], cont_blocks[1], 0.60),
        ]:
            _, _, _, _, ep, _ = block_stats(kp, weight)
            hc, pc, nc, sc, ec, _ = block_stats(kc, weight)
            print(
                f"{lam:4.0f} {L:5.2f} {name:>5s} "
                f"{norm(kp-kc,'fro'):10.3f} {ep:8.3f} {ec:7.3f} "
                f"{hc:6.3f} {sc/max(hc,1e-30):8.3f}"
            )
        sys.stdout.flush()


if __name__ == "__main__":
    run()
