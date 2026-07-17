#!/usr/bin/env python3
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_69_hpac_certificate_probe import finite_roots  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def squared_stieltjes_check(lam, n_modes, hmax=8.0):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    d = 2.0 * np.pi * idx / L
    p = xi * xi
    roots = finite_roots(xi, d, hmax=hmax)
    rows = []
    for tau in roots:
        s_tau = 2.0 * tau / (tau * tau - d * d)
        v_direct = np.sum(p * s_tau)
        n_direct = np.sum(p * s_tau * s_tau)

        w_plus = np.sum(p / (tau - d))
        w_minus = np.sum(p / (-tau - d))
        wp_plus = -np.sum(p / (tau - d) ** 2)
        wp_minus = -np.sum(p / (-tau - d) ** 2)

        v_id = w_plus - w_minus
        n_id = -wp_plus - wp_minus + v_direct / tau
        err_v = abs(v_direct - v_id) / max(abs(v_direct), 1e-30)
        err_n = abs(n_direct - n_id) / max(abs(n_direct), 1e-30)
        rows.append((tau, err_v, err_n, abs(v_direct), np.sqrt(abs(n_direct))))
    return L, rows


def run():
    print("E72.281 squared-Stieltjes VBG probe")
    print("W(t)=sum xi_n^2/(t-d_n): V=W(tau)-W(-tau), ||S_tau xi||^2=-W'(tau)-W'(-tau)+V/tau.")
    print("lam L roots maxErrV maxErrNorm2 maxV max||Sxi||")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56)]:
        L, rows = squared_stieltjes_check(lam, n_modes)
        err_v = np.array([r[1] for r in rows])
        err_n = np.array([r[2] for r in rows])
        v = np.array([r[3] for r in rows])
        sx = np.array([r[4] for r in rows])
        print(
            f"{lam:3.0f} {L:.6f} {len(rows):5d} "
            f"{(np.max(err_v) if len(err_v) else np.nan):.3e} "
            f"{(np.max(err_n) if len(err_n) else np.nan):.3e} "
            f"{(np.max(v) if len(v) else np.nan):.6e} "
            f"{(np.max(sx) if len(sx) else np.nan):.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
