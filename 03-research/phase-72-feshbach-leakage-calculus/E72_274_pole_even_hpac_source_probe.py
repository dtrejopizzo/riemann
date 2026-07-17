#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_69_hpac_certificate_probe import finite_roots, hpac_matrix  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402
from E72_273_pole_even_bordered_minor_identity import bordered_pairing  # noqa: E402


def hpac_values(lam, n_modes, s=10.0 + 0.2j, root_count=4):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    d = 2.0 * np.pi * idx / L
    roots = finite_roots(xi, d)[:root_count]
    a = eb.T @ (s / (s * s - d * d))
    out = []
    for tau in roots:
        source_xi = eb.T @ (hpac_matrix(idx, L, tau) @ xi)
        direct = np.vdot(a, solve(c_actual, source_xi))
        minor = bordered_pairing(c_actual, a, source_xi)
        out.append((tau, direct, minor))
    return L, roots, out


def run():
    print("E72.274 pole-even HPAC source probe")
    print("Uses source b_tau=B_even^T A_x(tau) xi_x; no Q=I-kk* and no old h=k-xi.")
    print("lam L roots max|F| values minorRel")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56)]:
        L, roots, rows = hpac_values(lam, n_modes)
        vals = np.array([abs(v) for _, v, _ in rows])
        rels = [abs(v - m) / max(abs(v), 1e-30) for _, v, m in rows]
        val_str = "[" + " ".join(f"{v:.3e}" for v in vals) + "]"
        print(
            f"{lam:3.0f} {L:.6f} {len(roots):5d} "
            f"{(np.max(vals) if len(vals) else np.nan):.6e} {val_str} "
            f"{(max(rels) if rels else np.nan):.3e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
