#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    mu = vals[0]
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h.astype(complex), float(mu), d, L, xi.astype(complex)


def source_basis(off_nodes, crit_nodes, d, L, max_power, endpoint_power):
    cols = []
    labels = []
    for ki, k in enumerate(crit_nodes):
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        cols.append(dd)
        labels.append(("cauchy0", ki, -1, 0))
        for bi, beta in enumerate(off_nodes):
            denom = np.array([dm * dm + beta * beta for dm in d], dtype=complex)
            for r in range(1, max_power + 1):
                cols.append(dd / (denom**r))
                labels.append(("rat", ki, bi, r))
        for q in range(1, endpoint_power + 1):
            cols.append((d ** (2 * q)) * dd)
            labels.append(("endpoint", ki, -1, q))
    return np.column_stack(cols), labels


def effective_rank(mat, reltol=1e-12):
    s = svd(mat, compute_uv=False, full_matrices=False)
    if len(s) == 0 or s[0] == 0:
        return 0, np.inf
    rank = int(np.sum(s > reltol * s[0]))
    cond = float(s[0] / s[rank - 1]) if rank else np.inf
    return rank, cond


def run():
    print("E73.282 source basis saturation probe")
    print("Increases rational/endpoint atoms and measures exact generated-image and APR-row representation.")
    print("If exact symbolic closure is nearby, imageRel and rhoCoeffErrB should improve coherently.")
    print(
        " lam      L rMax eMax cols rank condB imageRel genCoeffB "
        "rhoFitRel centerB coeffCenterB rhoCoeffErrB"
    )
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        h, mu, d, L, xi = setup(lam, n_modes)
        e = h - mu * np.eye(h.shape[0], dtype=complex)
        prim, _ = source_basis(off_nodes, crit_nodes, d, L, max_power=2, endpoint_power=1)
        image = e @ prim
        gamma = GAMMAS[0]
        q = cauchy_rows(-1j * gamma, d)
        rproj = np.eye(len(d), dtype=complex) - projector(q)
        rho = q[0] @ h @ rproj
        center = rho @ xi
        for rmax, emax in [(3, 2), (4, 3), (5, 4), (6, 5), (8, 6)]:
            src, _labels = source_basis(off_nodes, crit_nodes, d, L, max_power=rmax, endpoint_power=emax)
            rank, cond = effective_rank(src, reltol=1e-12)
            rels = []
            coeff_cols = []
            for j in range(image.shape[1]):
                coeff, *_ = lstsq(src, image[:, j], rcond=None)
                coeff_cols.append(coeff)
                rels.append(norm(image[:, j] - src @ coeff) / max(norm(image[:, j]), 1e-30))
            action = np.column_stack(coeff_cols)
            gen_coeff_pair = (xi.conj().T @ src) @ action
            c, *_ = lstsq(src, rho, rcond=None)
            rho_fit = src @ c
            coeff_center = (xi.conj().T @ src) @ c
            rho_err = abs(coeff_center - center)
            print(
                f"{lam:4d} {L:8.3f} {rmax:4d} {emax:4d}"
                f" {src.shape[1]:4d} {rank:4d} {bexp(cond,L):6.2f}"
                f" {max(rels):8.1e} {bexp(norm(gen_coeff_pair),L):9.2f}"
                f" {norm(rho-rho_fit)/max(norm(rho),1e-30):9.1e}"
                f" {bexp(center,L):8.2f} {bexp(coeff_center,L):12.2f}"
                f" {bexp(rho_err,L):12.2f}"
            )


if __name__ == "__main__":
    run()
