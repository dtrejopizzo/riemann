#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-74-hilbert-eigenline-cancellation")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402
from E74_002_closed_mesh_action_probe import hilbert_mesh  # noqa: E402


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, float(L), xi


def true_weights(lam, L, d, cache):
    wodd = np.array(
        [
            complex(cache.setdefault((lam, float(L), float(x), "c"), weight(lam, L, x, "c")))
            - complex(cache.setdefault((lam, float(L), float(-x), "c"), weight(lam, L, -x, "c")))
            for x in d
        ],
        dtype=complex,
    )
    ueven = np.array(
        [
            (
                complex(cache.setdefault((lam, float(L), float(x), "c"), weight(lam, L, x, "c")))
                - complex(cache.setdefault((lam, float(L), float(x), "l"), weight(lam, L, x, "l"))) / L
            )
            + (
                complex(cache.setdefault((lam, float(L), float(-x), "c"), weight(lam, L, -x, "c")))
                - complex(cache.setdefault((lam, float(L), float(-x), "l"), weight(lam, L, -x, "l"))) / L
            )
            for x in d
        ],
        dtype=complex,
    )
    return wodd, ueven


def hpr_scalar(A, r, eta, wodd, ueven):
    diag = np.sum(eta * r * ueven)
    left = np.sum(wodd * r * (A @ eta))
    right = np.sum(wodd * eta * (A @ r))
    return diag + left + right


def ker_sample(q, target_norm, seed):
    rng = np.random.default_rng(seed)
    z = rng.normal(size=q.shape[1]) + 1j * rng.normal(size=q.shape[1])
    r = (np.eye(q.shape[1], dtype=complex) - projector(q)) @ z
    return target_norm * r / max(norm(r), 1e-300)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E74.14 certification and falsifiers")
    print("zeta eta should cancel; random ker(Q) and random symbols should not.")
    print("DH/planted controls are recorded in E74.014 as required external harness work.")
    print(" lam      L gamma row zetaB randKerMedB randSymMedB sepKer sepSym")
    cache = {}
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        A = hilbert_mesh(idx)
        I = np.eye(len(idx), dtype=complex)
        wodd, ueven = true_weights(lam, L, d, cache)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(q)) @ xi
            eta_norm = norm(eta)
            for row_id in range(2):
                r = q[row_id]
                zeta_val = abs(hpr_scalar(A, r, eta, wodd, ueven))
                ker_vals = []
                sym_vals = []
                for s in range(16):
                    v = ker_sample(q, eta_norm, 71000 + 101 * lam + 17 * row_id + s)
                    ker_vals.append(abs(hpr_scalar(A, r, v, wodd, ueven)))
                    rng = np.random.default_rng(81000 + 103 * lam + 19 * row_id + s)
                    rw = rng.normal(size=len(idx)) + 1j * rng.normal(size=len(idx))
                    ru = rng.normal(size=len(idx)) + 1j * rng.normal(size=len(idx))
                    sym_vals.append(abs(hpr_scalar(A, r, eta, rw, ru)))
                ker_med = float(np.median(ker_vals))
                sym_med = float(np.median(sym_vals))
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(zeta_val, L):6.2f}"
                    f" {bexp(ker_med, L):11.2f}"
                    f" {bexp(sym_med, L):11.2f}"
                    f" {bexp(zeta_val / max(ker_med, 1e-300), L):6.2f}"
                    f" {bexp(zeta_val / max(sym_med, 1e-300), L):6.2f}"
                )


if __name__ == "__main__":
    run()
