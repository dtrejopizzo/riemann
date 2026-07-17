#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, inv, lstsq, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_195_finite_frequency_certificate_probe import cauchy_rows  # noqa: E402
from E73_287_closed_weight_formula_probe import closed_V, closed_W  # noqa: E402
from E73_290_diag_off_kernel_probe import kernel_explicit, projector  # noqa: E402


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h.astype(complex), idx.astype(int), d, L, xi.astype(complex)


def project_span(q, vector):
    coeff, *_ = lstsq(q.T, vector, rcond=None)
    pred = q.T @ coeff
    return pred, coeff


def run():
    print("E73.291 kernel-row identity probe")
    print("Tests whether K-DIAGOFF equals qH modulo the Cauchy gauge rowspace.")
    print("rawRel=||K-qH||/||qH||; modRel removes span{q_w,q_-w}.")
    print(
        " lam     L gamma row rawRel modRel pairKB rowHB pairErrB gaugePairB resPairB"
    )
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h, idx, d, L, xi = setup(lam, n_modes)
        freqs = np.array(sorted(set([float(x) for x in d] + [float(-x) for x in d])), dtype=float)
        W = np.array([closed_W(o, L, lam) for o in freqs], dtype=complex)
        V = np.array([closed_V(o, L, lam) for o in freqs], dtype=complex)
        Wg = W - np.mean(W)
        Ug = (W - V / L) - np.mean(W - V / L)
        ident = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for row_id in range(2):
                row = q[row_id]
                ker = kernel_explicit(row, idx, d, freqs, Wg, Ug)
                row_h = row @ h
                diff = ker - row_h
                pred, _coeff = project_span(q, diff)
                resid = diff - pred
                raw_rel = norm(diff) / max(norm(row_h), 1e-300)
                mod_rel = norm(resid) / max(norm(row_h), 1e-300)
                pair_k = np.dot(eta, ker)
                pair_h = np.dot(row_h, eta)
                pair_err = pair_k - pair_h
                gauge_pair = np.dot(eta, pred)
                res_pair = np.dot(eta, resid)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                    f" {raw_rel:7.1e} {mod_rel:7.1e}"
                    f" {bexp(pair_k,L):7.2f} {bexp(pair_h,L):6.2f}"
                    f" {bexp(pair_err,L):8.2f}"
                    f" {bexp(gauge_pair,L):10.2f} {bexp(res_pair,L):8.2f}"
                )


if __name__ == "__main__":
    run()
