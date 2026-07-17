#!/usr/bin/env python3
"""Expose the finite invariants needed for polynomial Schur-transfer bounds."""

import sys

import numpy as np
from numpy.linalg import det, eigvals, inv, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows  # noqa: E402


def bexp(x, L):
    return np.log(max(float(abs(x)), 1e-300)) / np.log(L)


def run():
    print("E74.18 Schur-transfer invariant audit")
    print("K=mu G-A, T=K G^-1, det(T)=det(K)/det(G), T^-1=G K^-1.")
    print("isoErr measures distance of T/L from its best scalar multiple of I.")
    print(" lam      L gamma mu/L compLo compHi detTB minTB invTB isoErr eig(T/L)")
    cases = [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24), (24, 28), (28, 32)]
    for lam, n_modes in cases:
        h, idx, L = build(lam, n_modes, include_arith=True)
        mu = np.linalg.eigvalsh(h)[0]
        d = 2.0 * np.pi * idx / L
        for gamma in GAMMAS[:3]:
            q = cauchy_rows(-1j * gamma, d)
            g = q @ q.conj().T
            a = q @ h @ q.conj().T
            k = mu * g - a
            t = k @ inv(g)
            # G^{-1/2} A G^{-1/2} is the Hermitian compression of H to
            # Row(Q); its eigenvalues are the basis-independent comparison.
            gv, gu = np.linalg.eigh(g)
            gih = gu @ np.diag(gv ** -0.5) @ gu.conj().T
            comp = np.linalg.eigvalsh(gih @ a @ gih) / L
            sing = svd(t, compute_uv=False)
            scalar = np.trace(t / L) / 2.0
            iso = norm(t / L - scalar * np.eye(2), 2)
            ev = eigvals(t / L)
            det_identity = abs(det(t) - det(k) / det(g))
            if det_identity > 1e-7 * max(abs(det(t)), 1.0):
                raise RuntimeError("determinant identity lost numerically")
            print(
                f"{lam:4d} {L:8.3f} {gamma:6.2f}"
                f" {mu/L:6.3f} {comp[0]:6.3f} {comp[1]:6.3f}"
                f" {bexp(det(t),L):5.2f} {bexp(sing[-1],L):5.2f}"
                f" {bexp(norm(inv(t),2),L):5.2f} {iso:7.1e}"
                f" {ev[0].real:6.3f},{ev[1].real:6.3f}"
            )


if __name__ == "__main__":
    run()
