#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402
from E72_88_finite_band_transport_probe import transport_residual  # noqa: E402


def run():
    s = 10 + 0.2j
    hcuts = [12, 18, 24]
    root_window = 10.0
    print("E72.90 finite-band root transport scaling probe")
    print("   lam    N Hcut roots     max|R_H|      rms|R_H|   tail-energy")
    for lam, n_modes in [(8, 24), (10, 26), (12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
        a = bq.T @ (s / (s * s - d * d))
        g = bq @ solve(ce, a)
        total = norm(g) ** 2
        roots = finite_roots(xi, d, hmax=root_window)
        for hcut in hcuts:
            mask = (np.abs(d) <= hcut).astype(float)
            g_band = mask * g
            vals = np.array([transport_residual(g_band, d, k, L, tau) for tau in roots])
            tail_energy = np.sum((1 - mask) * np.abs(g) ** 2) / total
            if len(vals) == 0:
                maxv = np.nan
                rms = np.nan
            else:
                maxv = np.max(np.abs(vals))
                rms = np.sqrt(np.mean(np.abs(vals) ** 2))
            print(
                f"{lam:6.1f} {n_modes:4d} {hcut:4.0f} {len(vals):5d} "
                f"{maxv:12.3e} {rms:12.3e} {tail_energy:13.3e}"
            )


if __name__ == "__main__":
    run()
