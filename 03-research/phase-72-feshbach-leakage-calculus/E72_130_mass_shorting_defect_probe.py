#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_107_spectral_divergence_probe import even_weighted_band  # noqa: E402
from E72_112_operator_split_probe import lk_matrix, sigma_packet  # noqa: E402


def run():
    print("E72.130 mass shorting defect probe")
    print(" lam   L roots  max preMass  max qMass  max postMass  post/pre  post/q")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        lk = lk_matrix(d, k)
        factor = 2.0 / (L * np.sqrt(np.exp(L)))
        max_pre = 0.0
        max_q = 0.0
        max_post = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            zpm = factor * (lk @ y)
            pre_even = even_weighted_band(idx, mask * zpm, mask)
            pre_mass = abs(np.sum(pre_even))
            cpm = bq.T @ (mask * zpm)
            q_full = mask * (bq @ cpm)
            q_even = even_weighted_band(idx, q_full, mask)
            q_mass = abs(np.sum(q_even))
            phi_full = mask * (bq @ solve(c_actual, cpm))
            phi_even = even_weighted_band(idx, phi_full, mask)
            post_mass = abs(np.sum(phi_even))
            max_pre = max(max_pre, pre_mass)
            max_q = max(max_q, q_mass)
            max_post = max(max_post, post_mass)
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{max_pre:11.3e} {max_q:10.3e} {max_post:12.3e} "
            f"{max_post/max(max_pre,1e-30):9.3e} {max_post/max(max_q,1e-30):8.3e}"
        )


if __name__ == "__main__":
    run()
