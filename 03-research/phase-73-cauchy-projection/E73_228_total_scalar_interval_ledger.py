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
from E73_201_mp_finite_assembly_probe import mp_arch_closed_digamma, mp_prime_modes  # noqa: E402
from E73_219_scalar_transcell_budget import EPSH_B, RHO_B  # noqa: E402
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
    return H, idx.astype(int), d, L, xi


def closed_center(const_map, linear_map, eta, L, lam):
    const = {om: vec @ eta for om, vec in const_map.items()}
    linear = {om: vec @ eta for om, vec in linear_map.items()}
    return mp_arch_closed_digamma(const, linear, L, 80) - mp_prime_modes(const, linear, L, lam)


def bexp(z, L):
    return math.log(max(float(abs(z)), 1e-300)) / math.log(L)


def run():
    print("E73.228 total scalar interval ledger")
    print("Combines R_etaH + R_coeff + R_weight around the closed center.")
    print(
        " lam     L    N Csec gamma row centerB RetaHB RcoeffB RweightB "
        "RtotalB ratio dominant"
    )
    weight_cache = {}
    wrad_cache = {}
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        H, idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(idx), dtype=complex)
        for csec_label in ["1", "1e6"]:
            rho_eta = float(L ** RHO_B[(lam, csec_label)])
            epsH = float(L ** EPSH_B[(lam, csec_label)])
            csec = mp.mpf(1) if csec_label == "1" else mp.mpf("1e6")
            for gamma in GAMMAS[:2]:
                q = cauchy_rows(-1j * gamma, d)
                eta = (ident - projector(q)) @ xi
                eta_norm = norm(eta)
                for row_id in range(2):
                    row = q[row_id]
                    const_map, linear_map = coefficient_maps(row, idx, d, L)
                    center = closed_center(const_map, linear_map, eta, L, lam)
                    r_eta = norm(row @ H) * rho_eta + norm(row) * epsH * eta_norm + norm(row) * epsH * rho_eta
                    r_coeff = mp.mpf("0")
                    r_weight = mp.mpf("0")
                    for kind, maps in [("c", const_map), ("l", linear_map)]:
                        for om, vec in maps.items():
                            wkey = (lam, float(L), float(om), kind)
                            w = weight_cache.setdefault(wkey, weight(lam, L, om, kind))
                            rad_coeff = mp.mpf(str(norm(vec) * rho_eta))
                            coeff = mp.mpf(str(abs(vec @ eta)))
                            r_coeff += abs(w) * rad_coeff
                            rkey = (lam, float(L), float(om), kind, csec_label)
                            rw = wrad_cache.setdefault(
                                rkey, native_weight_radius(om, kind, L, lam, csec=csec)[0]
                            )
                            r_weight += coeff * rw
                    r_total = mp.mpf(str(r_eta)) + r_coeff + r_weight
                    pieces = {
                        "etaH": mp.mpf(str(r_eta)),
                        "coeff": r_coeff,
                        "weight": r_weight,
                    }
                    dominant = max(pieces, key=pieces.get)
                    ratio = r_total / max(abs(center), mp.mpf("1e-300"))
                    print(
                        f"{lam:4d} {L:7.3f} {n_modes:4d} {csec_label:>4s}"
                        f" {gamma:7.2f} {row_id:3d}"
                        f" {bexp(center, L):7.2f} {bexp(r_eta, L):7.2f}"
                        f" {bexp(r_coeff, L):8.2f} {bexp(r_weight, L):8.2f}"
                        f" {bexp(r_total, L):8.2f} {float(ratio):8.1e}"
                        f" {dominant}"
                    )


if __name__ == "__main__":
    run()
