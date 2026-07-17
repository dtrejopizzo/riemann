#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_245_curv_quotient_defect import bexp, setup  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def run():
    print("E73.258 transverse eigen-residual audit")
    print("Tests whether eta=(I-P)xi is intrinsically near an eigenvector in ker Q without using h=Qxi small.")
    print(
        " lam      L gamma etaB hB PxiB transResB forceB force/PxiB "
        "scalarMaxB scalar/transB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20), (20, 24)]:
        H, _idx, d, L, mu, xi = setup(lam, n_modes)
        eye = np.eye(len(d), dtype=complex)
        E = H - mu * eye
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            R = eye - P
            h = Q @ xi
            pxi = P @ xi
            eta = R @ xi
            trans_res = R @ E @ eta
            force = -R @ E @ pxi
            scalars = Q @ H @ eta
            scalar_max = np.max(np.abs(scalars))
            print(
                f"{lam:4d} {L:8.3f} {gamma:6.2f}"
                f" {bexp(norm(eta), L):6.2f}"
                f" {bexp(norm(h), L):6.2f}"
                f" {bexp(norm(pxi), L):7.2f}"
                f" {bexp(norm(trans_res), L):10.2f}"
                f" {bexp(norm(force), L):7.2f}"
                f" {bexp(norm(force) / max(norm(pxi), 1e-300), L):10.2f}"
                f" {bexp(scalar_max, L):10.2f}"
                f" {bexp(scalar_max / max(norm(trans_res), 1e-300), L):13.2f}"
            )


if __name__ == "__main__":
    run()
