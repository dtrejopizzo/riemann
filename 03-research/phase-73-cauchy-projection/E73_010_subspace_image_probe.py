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
from E73_003_critical_source_probe import pi_kernel, dd_kernel  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual, vals[0], idx.astype(int), d, L, xi


def source_vector(b, off_nodes, crit_nodes, d, L):
    out = []
    for dm in d:
        sb = 0j
        for k in crit_nodes:
            gamma = (-1j * k).real
            sb += pi_kernel(b, k, off_nodes) * dd_kernel(-gamma, dm, L)
        out.append(sb)
    return np.array(out, dtype=complex)


def ratdd_basis(off_nodes, crit_nodes, d, L, max_power):
    cols = []
    for k in crit_nodes:
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        for beta in off_nodes:
            beta2 = beta * beta
            denom = np.array([dm * dm + beta2 for dm in d], dtype=complex)
            for r in range(1, max_power + 1):
                cols.append(dd / (denom ** r))
    return np.column_stack(cols)


def projection_distance(image, source, tol=1e-10):
    u, s, vh = svd(image, full_matrices=False)
    if len(s) == 0:
        return 1.0, 0, 0.0
    rank = int(np.sum(s > tol * s[0]))
    q = u[:, :rank]
    proj = q @ (q.conj().T @ source)
    rel = norm(source - proj) / max(norm(source), 1e-30)
    cond = float(s[0] / s[rank - 1]) if rank else np.inf
    return rel, rank, cond


def run():
    print("E73.010 structured image subspace probe")
    print(" lam     L   dim  pwr  cols rank    condImg      relDist    eigSrc     expEig")
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    b = off_nodes[0]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        h, mu, idx, d, L, xi = setup_full(lam, n_modes)
        src = source_vector(b, off_nodes, crit_nodes, d, L)
        eig = abs(np.vdot(xi, src))
        exp_eig = abs(cmath.exp(b.real * L)) * eig
        for pwr in (1, 2, 3):
            basis = ratdd_basis(off_nodes, crit_nodes, d, L, pwr)
            image = (h - mu * np.eye(h.shape[0])) @ basis
            rel, rank, cond = projection_distance(image, src)
            print(
                f"{lam:4.0f} {L:7.3f} {len(idx):5d} {pwr:4d} {basis.shape[1]:5d} "
                f"{rank:4d} {cond:10.2e} {rel:10.2e} {eig:9.2e} {exp_eig:9.2e}"
            )


if __name__ == "__main__":
    run()
