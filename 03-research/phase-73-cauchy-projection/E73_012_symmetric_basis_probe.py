#!/usr/bin/env python3
import sys
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


def symmetric_basis(off_nodes, crit_nodes, d, L, crit_choice, max_power):
    cols = []
    # Symmetric denominator product over off nodes.
    prod = np.ones(len(d), dtype=complex)
    for beta in off_nodes:
        prod *= np.array([dm * dm + beta * beta for dm in d], dtype=complex)
    for ki in crit_choice:
        k = crit_nodes[ki]
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        for r in range(1, max_power + 1):
            cols.append(dd / (prod ** r))
        # Add numerator powers to compensate product degree.
        for q in range(1, 4):
            cols.append((d ** (2 * q)) * dd / prod)
    return np.column_stack(cols)


def projection_distance(image, source, tol=1e-10):
    u, s, vh = svd(image, full_matrices=False)
    rank = int(np.sum(s > tol * s[0])) if len(s) else 0
    if rank == 0:
        return 1.0, 0, np.inf
    q = u[:, :rank]
    proj = q @ (q.conj().T @ source)
    rel = norm(source - proj) / max(norm(source), 1e-30)
    return rel, rank, float(s[0] / s[rank - 1])


def run():
    print("E73.012 symmetric basis probe")
    print(" lam     L   dim  crits  cols rank    condImg      relDist")
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    b = off_nodes[0]
    choices = [("end", [0, 4]), ("all", [0, 1, 2, 3, 4])]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        h, mu, idx, d, L, xi = setup_full(lam, n_modes)
        src = source_vector(b, off_nodes, crit_nodes, d, L)
        aop = h - mu * np.eye(h.shape[0])
        for name, choice in choices:
            basis = symmetric_basis(off_nodes, crit_nodes, d, L, choice, max_power=2)
            rel, rank, cond = projection_distance(aop @ basis, src)
            print(
                f"{lam:4.0f} {L:7.3f} {len(idx):5d} {name:>5s} "
                f"{basis.shape[1]:5d} {rank:4d} {cond:10.2e} {rel:10.2e}"
            )


if __name__ == "__main__":
    run()
