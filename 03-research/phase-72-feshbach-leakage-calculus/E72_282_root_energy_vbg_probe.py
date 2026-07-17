#!/usr/bin/env python3
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_69_hpac_certificate_probe import finite_roots  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def root_energy_profile(lam, n_modes, hmax=8.0):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    d = 2.0 * np.pi * idx / L
    roots = finite_roots(xi, d, hmax=hmax)
    rows = []
    for tau in roots:
        e_minus = np.sum((xi / (tau - d)) ** 2)
        e_plus = np.sum((xi / (tau + d)) ** 2)
        s_tau = 1.0 / (tau - d) + 1.0 / (tau + d)
        rows.append((tau, e_minus, e_plus, np.linalg.norm(s_tau * xi), abs(np.sum(xi / (tau - d)))))
    return L, rows


def run():
    print("E72.282 root-energy VBG probe")
    print("E_-(tau)=sum (xi_n/(tau-d_n))^2, E_+(tau)=sum (xi_n/(tau+d_n))^2.")
    print("VBG follows from ||S_tau xi|| <= sqrt(E_-)+sqrt(E_+) = O(L).")
    print("lam L roots maxE- maxE+ max||Sxi|| sqrtMaxE/L maxRootNull")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        L, rows = root_energy_profile(lam, n_modes)
        em = np.array([r[1] for r in rows])
        ep = np.array([r[2] for r in rows])
        sx = np.array([r[3] for r in rows])
        null = np.array([r[4] for r in rows])
        max_e = max(np.max(em), np.max(ep)) if len(rows) else np.nan
        print(
            f"{lam:3.0f} {L:.6f} {len(rows):5d} "
            f"{(np.max(em) if len(em) else np.nan):.6e} "
            f"{(np.max(ep) if len(ep) else np.nan):.6e} "
            f"{(np.max(sx) if len(sx) else np.nan):.6e} "
            f"{(np.sqrt(max_e) / L if len(rows) else np.nan):.6e} "
            f"{(np.max(null) if len(null) else np.nan):.3e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
