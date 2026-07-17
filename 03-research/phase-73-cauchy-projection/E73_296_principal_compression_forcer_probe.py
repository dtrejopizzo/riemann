#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvals, inv, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_245_curv_quotient_defect import bexp, setup  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def run():
    print("E73.296 principal compression forcer probe")
    print("Tests whether muI-A is small as a 2x2 matrix, not only on h=Qxi.")
    print(
        " lam     L gamma opB sminB detB eigGapB hB vectB relVect "
        "center0B center1B"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20), (20, 24)]:
        H, _idx, d, L, mu, xi = setup(lam, n_modes)
        eye = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            G = inv(Q @ Q.conj().T)
            P = projector(Q)
            R = eye - P
            A = Q @ H @ Q.conj().T @ G
            M = mu * np.eye(2, dtype=complex) - A
            h = Q @ xi
            vect = M @ h
            centers = Q @ H @ R @ xi
            sing = svd(M, compute_uv=False)
            ev = eigvals(A)
            eig_gap = min(abs(mu - ev[0]), abs(mu - ev[1]))
            rel_vect = norm(vect) / max(norm(M) * norm(h), 1e-300)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(norm(M),L):5.2f} {bexp(min(sing),L):6.2f}"
                f" {bexp(np.linalg.det(M),L):5.2f} {bexp(eig_gap,L):8.2f}"
                f" {bexp(norm(h),L):4.2f} {bexp(norm(vect),L):6.2f}"
                f" {rel_vect:7.1e}"
                f" {bexp(centers[0],L):8.2f} {bexp(centers[1],L):8.2f}"
            )


if __name__ == "__main__":
    run()
