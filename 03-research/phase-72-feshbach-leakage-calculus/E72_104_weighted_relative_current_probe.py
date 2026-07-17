#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_91_low_band_cofactor_probe import transport_vector  # noqa: E402


def m_prime(f, d, tau):
    return -np.dot(1 / (tau - d) ** 2, f)


def weighted_values(d, root_vec, k, L, bq, ce, roots, s, hcut):
    mask = (np.abs(d) <= hcut).astype(float)
    a = bq.T @ (s / (s * s - d * d))
    vals = []
    vals_abs = []
    for tau in roots:
        c_tau = bq.T @ (mask * transport_vector(d, k, L, tau))
        d2 = np.vdot(a, solve(ce, c_tau))
        w = 1 / m_prime(root_vec, d, tau)
        vals.append(w * d2)
        vals_abs.append(abs(w * d2))
    return np.array(vals, dtype=complex), np.array(vals_abs, dtype=float)


def run():
    s_values = [5 + 0.2j, 10 + 0.2j, 15 + 0.2j]
    hcut = 18
    hmax = 10.0
    print("E72.104 derivative-weighted relative current probe")
    print(" lam   N     s rootsA rootsM  |wSumA-wSumM|  sumAbsW  relRatio")
    for lam, n_modes in [(8, 24), (10, 26), (12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        roots_a = finite_roots(xi, d, hmax=hmax)
        roots_m = finite_roots(k, d, hmax=hmax)
        for s in s_values:
            vals_a, abs_a = weighted_values(d, xi, k, L, bq, c_actual, roots_a, s, hcut)
            vals_m, abs_m = weighted_values(d, k, k, L, bq, c_model, roots_m, s, hcut)
            defect = abs(np.sum(vals_a) - np.sum(vals_m))
            ceiling = np.sum(abs_a) + np.sum(abs_m)
            rel = defect / max(ceiling, 1e-30)
            print(
                f"{lam:4.0f} {n_modes:3d} {s.real:5.1f} "
                f"{len(roots_a):6d} {len(roots_m):6d} "
                f"{defect:14.3e} {ceiling:8.3e} {rel:9.3e}"
            )


if __name__ == "__main__":
    run()
