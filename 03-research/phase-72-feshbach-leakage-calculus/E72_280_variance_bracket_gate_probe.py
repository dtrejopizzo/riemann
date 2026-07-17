#!/usr/bin/env python3
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_69_hpac_certificate_probe import finite_roots  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def bracket_gate_profile(lam, n_modes, hmax=8.0):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    d = 2.0 * np.pi * idx / L
    roots = finite_roots(xi, d, hmax=hmax)
    rows = []
    for tau in roots:
        s_tau = 2.0 * tau / (tau * tau - d * d)
        v_tau = np.sum(s_tau * xi * xi)
        rows.append((tau, abs(v_tau), np.linalg.norm(s_tau * xi), np.max(np.abs(s_tau))))
    return L, rows


def run():
    print("E72.280 variance-bracket gate probe")
    print("Measures V_x(tau)=<xi,S_tau xi>, ||S_tau xi||, and ||S_tau||op on roots 0<tau<=8.")
    print("lam L roots maxV max||Sxi|| max||S||op maxV/L max||Sxi||/L")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        L, rows = bracket_gate_profile(lam, n_modes)
        v = np.array([r[1] for r in rows])
        sx = np.array([r[2] for r in rows])
        op = np.array([r[3] for r in rows])
        print(
            f"{lam:3.0f} {L:.6f} {len(rows):5d} "
            f"{(np.max(v) if len(v) else np.nan):.6e} "
            f"{(np.max(sx) if len(sx) else np.nan):.6e} "
            f"{(np.max(op) if len(op) else np.nan):.6e} "
            f"{(np.max(v) / L if len(v) else np.nan):.6e} "
            f"{(np.max(sx) / L if len(sx) else np.nan):.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
