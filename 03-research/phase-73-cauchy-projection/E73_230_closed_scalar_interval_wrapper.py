#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_219_scalar_transcell_budget import RHO_B  # noqa: E402
from E73_223_coefficient_ball_budget import coefficient_maps, cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402
from E73_227_native_ball_weight_radius import native_weight_radius  # noqa: E402


mp.mp.dps = 100


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def bexp(z, L):
    return math.log(max(float(abs(z)), 1e-300)) / math.log(L)


def run():
    print("E73.230 closed scalar interval wrapper")
    print("Uses only the closed coefficient/weight representation: no matrix-route double counting.")
    print(" lam     L    N Csec gamma row centerB RcoeffB RweightB RprodB RclosedB ratio")
    weight_cache = {}
    wrad_cache = {}
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(idx), dtype=complex)
        for csec_label in ["1", "1e6"]:
            rho_eta = float(L ** RHO_B[(lam, csec_label)])
            csec = mp.mpf(1) if csec_label == "1" else mp.mpf("1e6")
            for gamma in GAMMAS[:2]:
                q = cauchy_rows(-1j * gamma, d)
                eta = (ident - projector(q)) @ xi
                for row_id in range(2):
                    const_map, linear_map = coefficient_maps(q[row_id], idx, d, L)
                    center = mp.mpc(0)
                    r_coeff = mp.mpf("0")
                    r_weight = mp.mpf("0")
                    r_prod = mp.mpf("0")
                    for kind, maps in [("c", const_map), ("l", linear_map)]:
                        for om, vec in maps.items():
                            coeff_center = vec @ eta
                            coeff_rad = mp.mpf(str(norm(vec) * rho_eta))
                            wkey = (lam, float(L), float(om), kind)
                            w_center = weight_cache.setdefault(wkey, weight(lam, L, om, kind))
                            rkey = (lam, float(L), float(om), kind, csec_label)
                            w_rad = wrad_cache.setdefault(
                                rkey, native_weight_radius(om, kind, L, lam, csec=csec)[0]
                            )
                            center += mp.mpc(coeff_center) * w_center
                            r_coeff += abs(w_center) * coeff_rad
                            r_weight += mp.mpf(str(abs(coeff_center))) * w_rad
                            r_prod += coeff_rad * w_rad
                    r_closed = r_coeff + r_weight + r_prod
                    ratio = r_closed / max(abs(center), mp.mpf("1e-300"))
                    print(
                        f"{lam:4d} {L:7.3f} {n_modes:4d} {csec_label:>4s}"
                        f" {gamma:7.2f} {row_id:3d}"
                        f" {bexp(center, L):7.2f} {bexp(r_coeff, L):8.2f}"
                        f" {bexp(r_weight, L):8.2f} {bexp(r_prod, L):7.2f}"
                        f" {bexp(r_closed, L):8.2f} {float(ratio):8.1e}"
                    )


if __name__ == "__main__":
    run()
