#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def orient(x):
    x = (x + x[::-1]) / 2.0
    x = x / norm(x)
    if x[len(x) // 2] < 0:
        x = -x
    return x


def setup(lam, n_modes):
    hz, idx, L = build(lam, n_modes, include_arith=True)
    ha, _, _ = build(lam, n_modes, include_arith=False)
    wz, vz = eigh(hz)
    wa, va = eigh(ha)
    xz = orient(vz[:, 0])
    xa = orient(va[:, 0])
    if np.dot(xz, xa) < 0:
        xz = -xz
    d = 2.0 * np.pi * idx / L
    return hz, ha, wz[0], wa, va, d, L, xz, xa


def reduced_first_order_delta(ha_vals, ha_vecs, va0, perturb):
    # For H(eps)=H_arch+eps*V, first-order eigenvector correction:
    # delta x = - sum_{j>0} v_j <v_j,Vv0>/(lambda_j-lambda_0).
    out = np.zeros_like(va0)
    lam0 = ha_vals[0]
    source = perturb @ va0
    for j in range(1, len(ha_vals)):
        vj = ha_vecs[:, j]
        out += -vj * (np.dot(vj, source) / (ha_vals[j] - lam0))
    return out


def cauchy(t, d, x):
    return float(np.sum(x / (t - d)))


def run():
    print("E73.131 eigenvector perturbation CSV probe")
    print("Tests first-order arch resolvent prediction for delta xi and C_delta.")
    print(" lam     L gamma     archB trueDelB predDelB  errDelB zetaPredB")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        hz, ha, muz, wa, va, d, L, xz, xa = setup(lam, n_modes)
        perturb = hz - ha
        delta_pred = reduced_first_order_delta(wa, va, xa, perturb)
        # Fix normalization gauge: compare in the tangent plane to xa.
        delta_true = xz - xa
        delta_true = delta_true - xa * np.dot(xa, delta_true)
        for gamma in GAMMAS[:3]:
            t = -gamma
            arch = cauchy(t, d, xa)
            true_del = cauchy(t, d, delta_true)
            pred_del = cauchy(t, d, delta_pred)
            err_del = true_del - pred_del
            zeta_pred = arch + pred_del
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(abs(arch), L):8.3f} {bexp(abs(true_del), L):8.3f}"
                f" {bexp(abs(pred_del), L):8.3f} {bexp(abs(err_del), L):8.3f}"
                f" {bexp(abs(zeta_pred), L):10.3f}"
            )


if __name__ == "__main__":
    run()

