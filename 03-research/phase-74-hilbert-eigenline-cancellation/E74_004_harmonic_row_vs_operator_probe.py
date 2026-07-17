#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-74-hilbert-eigenline-cancellation")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402
from E74_002_closed_mesh_action_probe import harmonic_symbol, hilbert_mesh  # noqa: E402


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h.astype(complex), idx.astype(int), d, L, xi


def weights(lam, L, d, cache):
    Wodd = np.array(
        [
            complex(cache.setdefault((lam, float(L), float(x), "c"), weight(lam, L, x, "c")))
            - complex(cache.setdefault((lam, float(L), float(-x), "c"), weight(lam, L, -x, "c")))
            for x in d
        ],
        dtype=complex,
    )
    Ueven = np.array(
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
    return Wodd, Ueven


def project_span(q, vector):
    coeff, *_ = lstsq(q.T, vector, rcond=None)
    pred = q.T @ coeff
    return pred


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E74.4 harmonic row vs operator row")
    print("Checks K_HS = r M_U + r M_W(A+H_beta) equals r H_L modulo Cauchy gauge.")
    print(" lam      L gamma row rawRel modRel pairHSB pairHB pairErrB gaugePairB resPairB")
    cache = {}
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28)]:
        h, idx, d, L, xi = setup(lam, n_modes)
        A = hilbert_mesh(idx)
        Wodd, Ueven = weights(lam, L, d, cache)
        I = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(q)) @ xi
            alpha = gamma * L / (2.0 * math.pi)
            for row_id, beta in [(0, alpha), (1, -alpha)]:
                r = q[row_id]
                Hsym = harmonic_symbol(idx, beta)
                row_hs = r * Ueven + (r * Wodd) @ A + r * Wodd * Hsym
                row_h = r @ h
                diff = row_hs - row_h
                gauge = project_span(q, diff)
                resid = diff - gauge
                raw_rel = norm(diff) / max(norm(row_h), 1e-300)
                mod_rel = norm(resid) / max(norm(row_h), 1e-300)
                pair_hs = np.dot(row_hs, eta)
                pair_h = np.dot(row_h, eta)
                pair_err = pair_hs - pair_h
                gauge_pair = np.dot(gauge, eta)
                res_pair = np.dot(resid, eta)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {raw_rel:7.1e} {mod_rel:7.1e}"
                    f" {bexp(pair_hs, L):8.2f}"
                    f" {bexp(pair_h, L):6.2f}"
                    f" {bexp(pair_err, L):8.2f}"
                    f" {bexp(gauge_pair, L):10.2f}"
                    f" {bexp(res_pair, L):8.2f}"
                )


if __name__ == "__main__":
    run()
