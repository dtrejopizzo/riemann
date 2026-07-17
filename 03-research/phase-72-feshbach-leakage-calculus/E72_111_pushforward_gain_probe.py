#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import solve, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_106_post_main_source_probe import post_main_source  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_107_spectral_divergence_probe import even_weighted_band  # noqa: E402
from E72_109_quadratic_flux_probe import centered_flux  # noqa: E402


def run():
    print("E72.111 post-main pushforward gain probe")
    print(
        " lam   N roots   max||Kk||  max||Zpm||  max||cpm||  "
        "max||short||  max|mass|  maxFlux2"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        factor = 2.0 / (L * np.sqrt(np.exp(L)))
        vals = {
            "kk": 0.0,
            "z": 0.0,
            "c": 0.0,
            "short": 0.0,
            "mass": 0.0,
            "flux": 0.0,
        }
        for tau in roots[:6]:
            kpm, _ = post_main_source(L, n_modes, tau)
            kk = kpm @ k
            zpm = factor * kk
            cpm = bq.T @ (mask * zpm)
            y = solve(c_actual, cpm)
            phi_full = mask * (bq @ y)
            phi_even = even_weighted_band(idx, phi_full, mask)
            mass, flux2, _ = centered_flux(phi_even)
            vals["kk"] = max(vals["kk"], norm(kk))
            vals["z"] = max(vals["z"], norm(zpm))
            vals["c"] = max(vals["c"], norm(cpm))
            vals["short"] = max(vals["short"], norm(phi_full))
            vals["mass"] = max(vals["mass"], abs(mass))
            vals["flux"] = max(vals["flux"], flux2)
        print(
            f"{lam:4.0f} {n_modes:3d} {len(roots):5d} "
            f"{vals['kk']:10.3e} {vals['z']:10.3e} {vals['c']:10.3e} "
            f"{vals['short']:11.3e} {vals['mass']:10.3e} {vals['flux']:9.3e}"
        )


if __name__ == "__main__":
    run()
