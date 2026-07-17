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
from E73_223_coefficient_ball_budget import coefficient_maps, cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402
from E73_227_native_ball_weight_radius import native_weight_radius  # noqa: E402


mp.mp.dps = 80


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def rho_model(L, lam):
    # Conservative extrapolation from the certified C_sec=1e6 radii in E73.217.
    # This probe is diagnostic; a theorem must prove this bound.
    known = {8: -45.98, 10: -43.11, 12: -41.26}
    if lam in known:
        return float(L ** known[lam])
    # Mild continuation of the observed log_L exponent drift.
    exp = -41.26 + 0.95 * (12 - lam)
    return float(L ** exp)


def bexp(z, L):
    return math.log(max(float(abs(z)), 1e-300)) / math.log(L)


def run():
    print("E73.231 uniform scaling probe")
    print("Diagnostic closed scalar wrapper beyond certified windows; rho is extrapolated.")
    print(" lam     L    N gamma row centerB RclosedB ratio maxW_B sumCoeffB rhoB")
    wcache = {}
    rcache = {}
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (14, 12), (16, 14), (18, 16)]:
        idx, d, L, xi = setup(lam, n_modes)
        rho = rho_model(L, lam)
        ident = np.eye(len(idx), dtype=complex)
        for gamma in [GAMMAS[0]]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for row_id in [0]:
                const_map, linear_map = coefficient_maps(q[row_id], idx, d, L)
                center = mp.mpc(0)
                r_closed = mp.mpf("0")
                max_w = mp.mpf("0")
                sum_coeff = mp.mpf("0")
                for kind, maps in [("c", const_map), ("l", linear_map)]:
                    for om, vec in maps.items():
                        coeff = vec @ eta
                        rc = mp.mpf(str(norm(vec) * rho))
                        wkey = (lam, float(L), float(om), kind)
                        wc = wcache.setdefault(wkey, weight(lam, L, om, kind))
                        rkey = (lam, float(L), float(om), kind)
                        rw = rcache.setdefault(rkey, native_weight_radius(om, kind, L, lam, csec=mp.mpf("1e6"))[0])
                        center += mp.mpc(coeff) * wc
                        r_closed += abs(wc) * rc + mp.mpf(str(abs(coeff))) * rw + rc * rw
                        max_w = max(max_w, abs(wc))
                        sum_coeff += mp.mpf(str(abs(coeff)))
                ratio = r_closed / max(abs(center), mp.mpf("1e-300"))
                print(
                    f"{lam:4d} {L:7.3f} {n_modes:4d} {gamma:7.2f} {row_id:3d}"
                    f" {bexp(center, L):7.2f} {bexp(r_closed, L):8.2f}"
                    f" {float(ratio):8.1e} {bexp(max_w, L):7.2f}"
                    f" {bexp(sum_coeff, L):9.2f} {bexp(rho, L):6.2f}"
                )


if __name__ == "__main__":
    run()
