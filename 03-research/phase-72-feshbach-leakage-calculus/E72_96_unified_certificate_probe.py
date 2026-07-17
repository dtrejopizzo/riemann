#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402
from E72_91_low_band_cofactor_probe import transport_vector  # noqa: E402


def ccgd_tail(idx, d, bq, ce, s, hcut):
    a = bq.T @ (s / (s * s - d * d))
    y = solve(ce, a)
    g = bq @ y
    mask_tail = (np.abs(d) > hcut).astype(float)
    tail_direct = np.sum(mask_tail * np.abs(g) ** 2) / max(norm(g) ** 2, 1e-30)
    k_h = bq.T @ (mask_tail[:, None] * bq)
    tail_quad = np.vdot(y, k_h @ y).real / max(np.vdot(y, y).real, 1e-30)
    return tail_direct, tail_quad, g


def fbrt_defects(d, k, L, bq, ce, s, hcut, roots):
    r_even = s / (s * s - d * d)
    mask = (np.abs(d) <= hcut).astype(float)
    vals = []
    for tau in roots:
        z_tau = transport_vector(d, k, L, tau)
        c_tau = bq.T @ (mask * z_tau)
        phi = bq @ solve(ce, c_tau)
        stieltjes = np.vdot(r_even, phi)
        vals.append(stieltjes)
    vals = np.array(vals, dtype=complex)
    if len(vals) == 0:
        return np.nan, np.nan
    return np.max(np.abs(vals)), np.sqrt(np.mean(np.abs(vals) ** 2))


def run():
    s_values = [5 + 0.2j, 10 + 0.2j, 15 + 0.2j]
    hcuts = [12, 18, 24]
    root_window = 10.0
    print("E72.96 unified finite certificate probe")
    print("   lam    N      s Hcut roots    CCGD     CCGDdiff    maxFBRT    rmsFBRT")
    for lam, n_modes in [(12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
        roots = finite_roots(xi, d, hmax=root_window)
        for s in s_values:
            for hcut in hcuts:
                tail_direct, tail_quad, _ = ccgd_tail(idx, d, bq, ce, s, hcut)
                max_fbrt, rms_fbrt = fbrt_defects(d, k, L, bq, ce, s, hcut, roots)
                print(
                    f"{lam:6.1f} {n_modes:4d} {s.real:6.1f} {hcut:4.0f} "
                    f"{len(roots):5d} {tail_quad:8.2e} "
                    f"{abs(tail_direct-tail_quad):11.1e} "
                    f"{max_fbrt:10.3e} {rms_fbrt:10.3e}"
                )


if __name__ == "__main__":
    run()
