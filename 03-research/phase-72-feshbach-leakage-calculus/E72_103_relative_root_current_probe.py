#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_91_low_band_cofactor_probe import transport_vector  # noqa: E402


def d2_list(d, k, L, bq, ce, roots, s, hcut):
    mask = (np.abs(d) <= hcut).astype(float)
    a = bq.T @ (s / (s * s - d * d))
    vals = []
    for tau in roots:
        c_tau = bq.T @ (mask * transport_vector(d, k, L, tau))
        vals.append(np.vdot(a, solve(ce, c_tau)))
    return np.array(vals, dtype=complex)


def run():
    s_values = [5 + 0.2j, 10 + 0.2j, 15 + 0.2j]
    hcut = 18
    hmax = 10.0
    print("E72.103 relative root-current D2 probe")
    print(" lam   N     s rootsA rootsM  |sumA-sumM|   sumAbsA   sumAbsM   relRatio")
    for lam, n_modes in [(8, 24), (10, 26), (12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        roots_a = finite_roots(xi, d, hmax=hmax)
        roots_m = finite_roots(k, d, hmax=hmax)
        for s in s_values:
            vals_a = d2_list(d, k, L, bq, c_actual, roots_a, s, hcut)
            vals_m = d2_list(d, k, L, bq, c_model, roots_m, s, hcut)
            sum_a = np.sum(vals_a)
            sum_m = np.sum(vals_m)
            abs_a = np.sum(np.abs(vals_a))
            abs_m = np.sum(np.abs(vals_m))
            rel = abs(sum_a - sum_m) / max(abs_a + abs_m, 1e-30)
            print(
                f"{lam:4.0f} {n_modes:3d} {s.real:5.1f} "
                f"{len(roots_a):6d} {len(roots_m):6d} "
                f"{abs(sum_a-sum_m):12.3e} {abs_a:9.3e} {abs_m:9.3e} {rel:10.3e}"
            )


if __name__ == "__main__":
    run()
