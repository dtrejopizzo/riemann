#!/usr/bin/env python3
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_69_hpac_certificate_probe import finite_roots  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def cauchy_factor_profile(lam, n_modes, hmax=8.0, s=10.0 + 0.2j):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    d = 2.0 * np.pi * idx / L
    roots = finite_roots(xi, d, hmax=hmax)
    z = np.conjugate(s)

    rows = []
    for tau in roots:
        f_z = z / (z * z - d * d)
        s_tau = 2.0 * tau / (tau * tau - d * d)
        direct = np.sum(f_z * s_tau * xi) - np.sum(f_z * xi) * np.sum(s_tau * xi * xi)

        m_z = np.sum(xi / (z * z - d * d))
        v_tau = np.sum(s_tau * xi * xi)
        bracket = -2.0 * tau / (z * z - tau * tau) - v_tau
        factored = z * m_z * bracket

        root_null = np.sum(xi / (tau - d))
        even_null = np.sum(xi / (tau + d))
        rel = abs(direct - factored) / max(abs(direct), 1e-30)
        rows.append((tau, direct, factored, m_z, bracket, root_null, even_null, rel))
    return L, rows


def run():
    print("E72.278 Cauchy-factor identity probe")
    print("Identity: <a_s^perp,S_tau xi> = z M_x(z)(-2tau/(z^2-tau^2)-V_x(tau)), z=conj(s).")
    print("Roots are restricted to the fixed compact window 0<tau<=8.")
    print("lam L roots maxRel maxInner maxM maxBracket maxRootNull")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        L, rows = cauchy_factor_profile(lam, n_modes)
        rel = np.array([r[7] for r in rows])
        inner = np.array([abs(r[1]) for r in rows])
        m_z = np.array([abs(r[3]) for r in rows])
        bracket = np.array([abs(r[4]) for r in rows])
        nulls = np.array([max(abs(r[5]), abs(r[6])) for r in rows])
        print(
            f"{lam:3.0f} {L:.6f} {len(rows):5d} "
            f"{(np.max(rel) if len(rel) else np.nan):.3e} "
            f"{(np.max(inner) if len(inner) else np.nan):.6e} "
            f"{(np.max(m_z) if len(m_z) else np.nan):.6e} "
            f"{(np.max(bracket) if len(bracket) else np.nan):.6e} "
            f"{(np.max(nulls) if len(nulls) else np.nan):.3e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
