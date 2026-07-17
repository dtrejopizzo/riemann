#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_195_finite_frequency_certificate_probe import cauchy_rows  # noqa: E402
from E73_193_balanced_ramp_probe import functional, r0, r1  # noqa: E402
from E73_297_curvature_operator_probe import q_cell_second  # noqa: E402


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h.astype(complex), idx.astype(int), d, L, xi


def numerical_rank_from_singular_values(s, frac):
    total = float(np.sum(s * s))
    if total == 0.0:
        return 0
    accum = np.cumsum(s * s) / total
    return int(np.searchsorted(accum, frac) + 1)


def run():
    print("E73.298 balanced curvature rank audit")
    print("Rows are q_a (Q_y''+alpha_L(y)J) R_w sampled over y.")
    print("This tests only a shortcut; failure means CURV-ABEL remains full-kernel signed.")
    print(
        " lam     L gamma row n samp r90 r99 r999 tail4 tail8 "
        "scalarProj4 scalarProj8 rowNormRatio"
    )
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h, idx, d, L, xi = setup(lam, n_modes)
        f0 = functional(lambda y: r0(y, L), 1.0, L, lam)
        f1 = functional(lambda y: r1(y, L), 0.0, L, lam)
        c_bal = -f0 / f1
        n = len(d)
        eye = np.eye(n, dtype=complex)
        J = np.ones((n, n), dtype=complex)
        ys = np.linspace(0.02 * L, 0.98 * L, 96)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            R = eye - projector(q)
            eta = R @ xi
            for row_id in range(2):
                row = q[row_id]
                rows = []
                scalars = []
                full_norms = []
                for y in ys:
                    alpha = (2.0 / L) * (-2.0 / L + c_bal * (2.0 - 6.0 * y / L))
                    curv = q_cell_second(idx, d, y, L) + alpha * J
                    r = row @ curv @ R
                    rows.append(r)
                    scalars.append(r @ xi)
                    full_norms.append(norm(row @ curv))
                mat = np.vstack(rows)
                s = svd(mat, compute_uv=False)
                total = float(np.sum(s * s))
                tail4 = float(np.sum(s[4:] * s[4:]) / total) if total else 0.0
                tail8 = float(np.sum(s[8:] * s[8:]) / total) if total else 0.0
                r90 = numerical_rank_from_singular_values(s, 0.90)
                r99 = numerical_rank_from_singular_values(s, 0.99)
                r999 = numerical_rank_from_singular_values(s, 0.999)

                u, ss, vh = svd(mat, full_matrices=False)
                scalar_vec = np.array(scalars)
                scalar_norm = norm(scalar_vec)
                proj_vals = []
                for rank in (4, 8):
                    basis = vh[:rank].conj().T
                    coeff = basis.conj().T @ xi
                    approx = (mat @ basis) @ coeff
                    resid = norm(scalar_vec - approx) / max(scalar_norm, 1e-300)
                    proj_vals.append(float(resid))
                row_norm_ratio = float(norm(mat, "fro") / max(norm(full_norms), 1e-300))
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                    f" {n:3d} {len(ys):4d} {r90:3d} {r99:3d} {r999:4d}"
                    f" {tail4:8.2e} {tail8:8.2e}"
                    f" {proj_vals[0]:11.2e} {proj_vals[1]:11.2e}"
                    f" {row_norm_ratio:11.2e}"
                )


if __name__ == "__main__":
    run()
