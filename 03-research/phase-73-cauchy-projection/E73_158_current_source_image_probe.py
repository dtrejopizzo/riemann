#!/usr/bin/env python3
import sys
import cmath
import numpy as np
from numpy.linalg import eigh, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel, pi_kernel  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def setup_exact(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    d = 2.0 * np.pi * idx / L
    e = h - vals[0] * np.eye(len(idx))
    return e, idx.astype(int), d, L, xi


def source_vector(b, off_nodes, crit_nodes, d, L):
    total = np.zeros(len(d), dtype=complex)
    for k in crit_nodes:
        gamma = (-1j * k).real
        coeff = pi_kernel(b, k, off_nodes)
        total += coeff * np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
    return total


def local_basis(off_nodes, crit_nodes, d, L, max_power=2, include_poly=True):
    cols = []
    labels = []
    for k in crit_nodes:
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        for beta in off_nodes:
            denom = np.array([dm * dm + beta * beta for dm in d], dtype=complex)
            if include_poly:
                cols.append(dd.copy())
                labels.append((k, beta, 0))
            for r in range(1, max_power + 1):
                cols.append(dd / (denom ** r))
                labels.append((k, beta, r))
        if include_poly:
            cols.append((d ** 2) * dd)
            labels.append((k, "poly2", 0))
    return np.column_stack(cols), labels


def image_projector(image, tol=1e-10):
    u, s, _ = svd(image, full_matrices=True)
    if len(s) == 0 or s[0] == 0:
        return u[:, :0], u, 0, np.inf
    rank = int(np.sum(s > tol * s[0]))
    cond = float(s[0] / s[rank - 1]) if rank else np.inf
    return u[:, :rank], u[:, rank:], rank, cond


def run():
    print("E73.158 current source-image scalar residual probe")
    print("Uses exact eigenvector and current larger scales.")
    print("rel=||P_img^perp S||/||S||; xiShare=|<xi,res>|/||res||.")
    print(" lam     L   dim rank  condB   relB xiShareB  srcB  scalarB expScalarB status")
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        e, idx, d, L, xi = setup_exact(lam, n_modes)
        off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
        basis, _ = local_basis(off_nodes, crit_nodes, d, L, max_power=2, include_poly=True)
        image = e @ basis
        u_img, _, rank, cond = image_projector(image)
        for b in off_nodes:
            src = source_vector(b, off_nodes, crit_nodes, d, L)
            resid = src - u_img @ (u_img.conj().T @ src)
            scalar = abs(np.vdot(xi, resid))
            direct = abs(np.vdot(xi, src))
            if abs(scalar - direct) > 1e-7 * max(1.0, direct):
                raise RuntimeError("image residual changed eigenline scalar unexpectedly")
            rel = norm(resid) / max(norm(src), 1e-300)
            xi_share = scalar / max(norm(resid), 1e-300)
            exp_scalar = abs(cmath.exp(b.real * L)) * scalar
            print(
                f"{lam:4d} {L:7.3f} {len(idx):5d} {rank:4d}"
                f" {bexp(cond, L):6.2f}"
                f" {bexp(rel, L):6.2f}"
                f" {bexp(xi_share, L):8.2f}"
                f" {bexp(norm(src), L):6.2f}"
                f" {bexp(scalar, L):8.2f}"
                f" {bexp(exp_scalar, L):10.2f}"
                f" {'PASS' if exp_scalar <= L**6 else 'FAIL'}"
            )


if __name__ == "__main__":
    run()
