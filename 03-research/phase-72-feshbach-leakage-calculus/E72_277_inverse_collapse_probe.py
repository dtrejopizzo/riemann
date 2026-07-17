#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_69_hpac_certificate_probe import finite_roots  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def inverse_collapse(lam, n_modes, hmax=8.0, s=10.0 + 0.2j):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    d = 2.0 * np.pi * idx / L
    roots = finite_roots(xi, d, hmax=hmax)
    xi_even = eb.T @ xi
    a = eb.T @ (s / (s * s - d * d))
    a_perp = a - xi_even * np.vdot(xi_even, a) / np.vdot(xi_even, xi_even)
    mu = float((np.vdot(xi_even, c_actual @ xi_even) / np.vdot(xi_even, xi_even)).real)

    rows = []
    for tau in roots:
        alpha = 0.5 + 1j * tau
        s_diag = 2.0 * tau / (tau * tau - d * d)
        s_even = eb.T @ (s_diag[:, None] * eb)
        s_xi = s_even @ xi_even
        comm_xi = c_actual @ s_xi - s_even @ (c_actual @ xi_even)

        lhs = 1j * alpha * np.vdot(a_perp, solve(c_actual, s_xi))
        diag = 1j * alpha * (np.vdot(a_perp, s_xi) / mu)
        comm = -1j * alpha * (np.vdot(a_perp, solve(c_actual, comm_xi)) / mu)
        rel = abs(lhs - diag - comm) / max(abs(lhs), 1e-30)
        rows.append((tau, lhs, diag, comm, rel))
    return L, mu, rows


def run():
    print("E72.277 inverse-collapse probe")
    print("Exact identity: <a,C^-1 Sxi> = mu^-1<a,Sxi> - mu^-1<a,C^-1[C,S]xi>.")
    print("Residual includes the factor i alpha(tau).")
    print("lam L roots mu maxR maxDiag maxComm maxRel")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        L, mu, rows = inverse_collapse(lam, n_modes)
        lhs = np.array([abs(r[1]) for r in rows])
        diag = np.array([abs(r[2]) for r in rows])
        comm = np.array([abs(r[3]) for r in rows])
        rel = np.array([r[4] for r in rows])
        print(
            f"{lam:3.0f} {L:.6f} {len(rows):5d} {mu:.6e} "
            f"{(np.max(lhs) if len(lhs) else np.nan):.6e} "
            f"{(np.max(diag) if len(diag) else np.nan):.6e} "
            f"{(np.max(comm) if len(comm) else np.nan):.6e} "
            f"{(np.max(rel) if len(rel) else np.nan):.3e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
