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
from E73_289_diag_off_weight_relation_probe import arr, split_packet_modes  # noqa: E402


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
    return idx.astype(int), d, L, xi.astype(complex)


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def cauchy_span_projection(q, vector):
    coeff, *_ = lstsq(q.T, vector, rcond=None)
    pred = q.T @ coeff
    return pred, coeff


def kernel_explicit(row, idx, d, freqs, Wg, Ug):
    wmap = {float(o): Wg[k] for k, o in enumerate(freqs)}
    umap = {float(o): Ug[k] for k, o in enumerate(freqs)}
    n = len(idx)
    wodd = np.array([wmap[float(d[j])] - wmap[float(-d[j])] for j in range(n)], dtype=complex)
    ueven = np.array([umap[float(d[j])] + umap[float(-d[j])] for j in range(n)], dtype=complex)
    ker = np.zeros(n, dtype=complex)
    for b in range(n):
        ker[b] += row[b] * ueven[b]
        for a in range(n):
            if a == b:
                continue
            den = np.pi * (idx[b] - idx[a])
            ker[b] += row[a] * (wodd[a] - wodd[b]) / (2j * den)
    return ker


def run():
    print("E73.290 diag/off explicit kernel probe")
    print("Builds K_b so that <coff,W'>+<cdiag,U'> = sum_b eta_b K_b exactly.")
    print("spanRel projects K onto the two Cauchy rows; resEta is the part still seen by eta.")
    print(
        " lam     L gamma row directB kernelB errB spanRel spanEtaB resEtaB etaOrthB KB"
    )
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        freqs = np.array(sorted(set([float(x) for x in d] + [float(-x) for x in d])), dtype=float)
        W = np.array([closed_W(o, L, lam) for o in freqs], dtype=complex)
        V = np.array([closed_V(o, L, lam) for o in freqs], dtype=complex)
        Wg = W - np.mean(W)
        Ug = (W - V / L) - np.mean(W - V / L)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (np.eye(len(d), dtype=complex) - projector(q)) @ xi
            eta_orth = norm(q @ eta)
            for row_id in range(2):
                row = q[row_id]
                cdiag_m, coff_m = split_packet_modes(row, idx, d, eta, L)
                cdiag = arr(cdiag_m, freqs)
                coff = arr(coff_m, freqs)
                direct = np.dot(coff, Wg) + np.dot(cdiag, Ug)
                ker = kernel_explicit(row, idx, d, freqs, Wg, Ug)
                via_kernel = np.dot(eta, ker)
                pred, _coeff = cauchy_span_projection(q, ker)
                resid = ker - pred
                span_rel = norm(resid) / max(norm(ker), 1e-300)
                span_eta = np.dot(eta, pred)
                res_eta = np.dot(eta, resid)
                err = direct - via_kernel
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                    f" {bexp(direct,L):7.2f} {bexp(via_kernel,L):7.2f}"
                    f" {bexp(err,L):6.2f} {span_rel:7.1e}"
                    f" {bexp(span_eta,L):8.2f} {bexp(res_eta,L):7.2f}"
                    f" {bexp(eta_orth,L):8.2f} {bexp(norm(ker),L):5.2f}"
                )


if __name__ == "__main__":
    run()
