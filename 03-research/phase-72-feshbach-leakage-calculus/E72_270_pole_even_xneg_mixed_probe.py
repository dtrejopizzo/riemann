#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_181_chebyshev_abs_schedule_probe import signed_coeff, eval_cheb_matrix_scaled  # noqa: E402
from E72_182_adaptive_margin_probe import even_degree_for_margin  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


WINDOWS = [(16, 40), (20, 48), (24, 56)]
CUTS = [0.55, 0.60, 0.65]
DEGREES = [8, 16, 32, "auto"]


def cross_for(k0, k1, degree):
    if degree == "auto":
        degree = even_degree_for_margin(k0.shape[0], 0.03)
    n_terms = max(1, int(degree) // 2)
    c0 = signed_coeff(0.70, 0.90, n_terms)
    c1 = signed_coeff(0.60, 0.60, n_terms)
    g0 = eval_cheb_matrix_scaled(k0, c0, 0.90)
    g1 = eval_cheb_matrix_scaled(k1, c1, 0.60)
    return float(2.0 * np.trace(g0 @ g1))


def prepare():
    rows = []
    for lam, n_modes in WINDOWS:
        idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
        rows.append((lam, L, idx, eb, c_model))
        print(f"prepared lambda={lam:.0f}", flush=True)
    return rows


def run():
    print("E72.270 pole-even XNEG/mixed probe")
    print("Corrected geometry; reports cross=2Tr(G0G1). Negative supports XNEG.")
    rows = prepare()
    for cut in CUTS:
        print(f"-- cut={cut:.2f}")
        print("lam op0 op1 " + " ".join(f"D{d}" for d in DEGREES))
        max_cross = {d: -np.inf for d in DEGREES}
        for lam, L, idx, eb, c_model in rows:
            k0, k1 = two_blocks(lam, idx, L, eb, c_model, cut)
            v0 = eigvalsh(k0)
            v1 = eigvalsh(k1)
            vals = []
            for degree in DEGREES:
                cross = cross_for(k0, k1, degree)
                max_cross[degree] = max(max_cross[degree], cross)
                vals.append(cross)
            print(
                f"{lam:3.0f} {max(abs(v0)):.3e} {max(abs(v1)):.3e} "
                + " ".join(f"{v:+.6e}" for v in vals),
                flush=True,
            )
        print("maxCross " + " ".join(f"D{d}:{max_cross[d]:+.6e}" for d in DEGREES), flush=True)


if __name__ == "__main__":
    run()
