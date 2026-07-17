#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm

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
    return idx.astype(int), d, L, xi.astype(complex)


def loewner_kernel(row, d, freqs, Wg, Ug, L):
    wmap = {float(o): Wg[k] for k, o in enumerate(freqs)}
    umap = {float(o): Ug[k] for k, o in enumerate(freqs)}
    n = len(d)
    f = np.array([wmap[float(d[j])] - wmap[float(-d[j])] for j in range(n)], dtype=complex)
    u = np.array([umap[float(d[j])] + umap[float(-d[j])] for j in range(n)], dtype=complex)
    lam = np.zeros((n, n), dtype=complex)
    for j in range(n):
        for b in range(n):
            if j == b:
                continue
            lam[j, b] = (f[j] - f[b]) / (d[j] - d[b])
    return row * u - (row @ lam) / (1j * L)


def run():
    print("E73.292 Loewner kernel probe")
    print("Checks K = r diag(Ueven) - (1/(iL)) r Lambda_Wodd.")
    print(" lam     L gamma row relErr pairDirectB pairLoewB pairErrB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
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
                k0 = kernel_explicit(row, idx, d, freqs, Wg, Ug)
                k1 = loewner_kernel(row, d, freqs, Wg, Ug, L)
                rel = norm(k0 - k1) / max(norm(k0), 1e-300)
                p0 = np.dot(eta, k0)
                p1 = np.dot(eta, k1)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                    f" {rel:7.1e} {bexp(p0,L):11.2f} {bexp(p1,L):9.2f}"
                    f" {bexp(p0-p1,L):8.2f}"
                )


if __name__ == "__main__":
    run()
