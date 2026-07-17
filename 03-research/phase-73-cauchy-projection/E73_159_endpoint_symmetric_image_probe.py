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
        total += pi_kernel(b, k, off_nodes) * np.array(
            [dd_kernel(-gamma, dm, L) for dm in d], dtype=complex
        )
    return total


def symmetric_denominator(off_nodes, d):
    den = np.ones(len(d), dtype=complex)
    for beta in off_nodes:
        den *= d * d + beta * beta
    return den


def endpoint_symmetric_basis(off_nodes, crit_nodes, d, L, mode):
    # Endpoint critical families: first and last critical height in the window.
    endpoint_nodes = [crit_nodes[0], crit_nodes[-1]]
    den = symmetric_denominator(off_nodes, d)
    cols = []
    for k in endpoint_nodes:
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        if mode == "poly":
            cols.extend([dd, d * dd, (d ** 2) * dd])
        elif mode == "sym1":
            cols.extend([dd, dd / den, (d ** 2) * dd / den])
        elif mode == "sym2":
            cols.extend([dd, d * dd, (d ** 2) * dd, dd / den, d * dd / den, (d ** 2) * dd / den])
        elif mode == "sympow":
            cols.extend([dd, dd / den, dd / (den ** 2), (d ** 2) * dd / den])
        else:
            raise ValueError(mode)
    return np.column_stack(cols)


def image_stats(e, basis, src, xi):
    image = e @ basis
    u, s, _ = svd(image, full_matrices=False)
    if len(s) == 0 or s[0] == 0:
        return 1.0, 0, np.inf, abs(np.vdot(xi, src))
    rank = int(np.sum(s > 1e-10 * s[0]))
    q = u[:, :rank]
    resid = src - q @ (q.conj().T @ src)
    rel = norm(resid) / max(norm(src), 1e-300)
    scalar = abs(np.vdot(xi, resid))
    cond = float(s[0] / s[rank - 1]) if rank else np.inf
    return rel, rank, cond, scalar


def run():
    print("E73.159 endpoint symmetric image probe")
    print("Tests canonical endpoint-critical bases with symmetric off-node denominator.")
    print(" lam     L mode   cols rank  condB   relB scalarB expScalarB")
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    modes = ["poly", "sym1", "sym2", "sympow"]
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        e, idx, d, L, xi = setup_exact(lam, n_modes)
        off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
        b = off_nodes[0]
        src = source_vector(b, off_nodes, crit_nodes, d, L)
        for mode in modes:
            basis = endpoint_symmetric_basis(off_nodes, crit_nodes, d, L, mode)
            rel, rank, cond, scalar = image_stats(e, basis, src, xi)
            exp_scalar = abs(cmath.exp(b.real * L)) * scalar
            print(
                f"{lam:4d} {L:7.3f} {mode:6s} {basis.shape[1]:5d} {rank:4d}"
                f" {bexp(cond, L):6.2f}"
                f" {bexp(rel, L):6.2f}"
                f" {bexp(scalar, L):8.2f}"
                f" {bexp(exp_scalar, L):10.2f}"
            )


if __name__ == "__main__":
    run()
