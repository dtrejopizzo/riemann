#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_69_hpac_certificate_probe import finite_roots, hpac_matrix  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def decompose(lam, n_modes, s=10.0 + 0.2j, root_count=4):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    d = 2.0 * np.pi * idx / L
    roots = finite_roots(xi, d)[:root_count]
    a = eb.T @ (s / (s * s - d * d))
    xi_even = eb.T @ xi
    a_perp = a - xi_even * np.vdot(xi_even, a) / np.vdot(xi_even, xi_even)

    rows = []
    for tau in roots:
        alpha = 0.5 + 1j * tau
        s_tau = 2.0 * tau / (tau * tau - d * d)
        b_full = eb.T @ (hpac_matrix(idx, L, tau) @ xi)
        b_const = eb.T @ (2.0 * xi)
        b_res = eb.T @ (1j * alpha * s_tau * xi)
        rel_simpl = norm(b_full - b_const - b_res) / max(norm(b_full), 1e-30)

        full = np.vdot(a, solve(c_actual, b_full))
        left_perp = np.vdot(a_perp, solve(c_actual, b_full))
        res_only = np.vdot(a, solve(c_actual, b_res))
        rows.append((tau, rel_simpl, full, left_perp, res_only))
    return L, abs(np.vdot(xi_even, a)), rows


def run():
    print("E72.275 pole-even HPAC gauge probe")
    print("At finite roots: A(tau)xi = 2xi + i(1/2+i tau)S_tau xi.")
    print("The left gauge a_perp=a-xi<xi,a> kills the constant 2xi without using old Q=I-kk*.")
    print("lam L roots |<xi,a>| maxSimpl maxFull maxLeftPerp maxResOnly")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56)]:
        L, xi_a, rows = decompose(lam, n_modes)
        simpl = np.array([r[1] for r in rows])
        full = np.array([abs(r[2]) for r in rows])
        left = np.array([abs(r[3]) for r in rows])
        res = np.array([abs(r[4]) for r in rows])
        print(
            f"{lam:3.0f} {L:.6f} {len(rows):5d} {xi_a:.6e} "
            f"{np.max(simpl):.3e} {np.max(full):.6e} "
            f"{np.max(left):.6e} {np.max(res):.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
