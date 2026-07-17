#!/usr/bin/env python3
import math
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import coefficient_maps, cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / np.linalg.norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E73.303 spectral distribution normal form")
    print("T_eta=sum c_delta + i sum l_delta' so <T,W>=sum cW+sum lV.")
    print(" lam      L gamma row centerB T1B TomB Tom2B derivB")
    cache = {}
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(Q)) @ xi
            for row_id in range(2):
                const_map, linear_map = coefficient_maps(Q[row_id], idx, d, L)
                center = 0j
                # Distribution moments: <T,phi> = sum c phi - i sum l phi'
                # because <delta',phi>=-phi'.  For phi(omega)=omega^k.
                t1 = 0j
                tom = 0j
                tom2 = 0j
                deriv = 0j
                for om, vec in const_map.items():
                    coeff = vec @ eta
                    w = complex(cache.setdefault((lam, float(L), float(om), "c"), weight(lam, L, om, "c")))
                    center += coeff * w
                    t1 += coeff
                    tom += coeff * om
                    tom2 += coeff * om * om
                    deriv += 1j * om * coeff
                for om, vec in linear_map.items():
                    coeff = vec @ eta
                    v = complex(cache.setdefault((lam, float(L), float(om), "l"), weight(lam, L, om, "l")))
                    center += coeff * v
                    # i*l*delta' contributes -i*l*phi'(om)
                    tom += -1j * coeff
                    tom2 += -2j * om * coeff
                    deriv += coeff
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(center, L):8.2f} {bexp(t1, L):7.2f}"
                    f" {bexp(tom, L):7.2f} {bexp(tom2, L):7.2f}"
                    f" {bexp(deriv, L):7.2f}"
                )


if __name__ == "__main__":
    run()
