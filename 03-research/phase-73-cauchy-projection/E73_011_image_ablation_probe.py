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


def basis_cols(off_nodes, crit_nodes, d, L, max_power, keep):
    cols = []
    labels = []
    for ki, k in enumerate(crit_nodes):
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        for bi, beta in enumerate(off_nodes):
            beta2 = beta * beta
            denom = np.array([dm * dm + beta2 for dm in d], dtype=complex)
            for r in range(1, max_power + 1):
                label = (ki, bi, r)
                if keep(label):
                    cols.append(dd / (denom ** r))
                    labels.append(label)
    if not cols:
        return np.zeros((len(d), 0), dtype=complex), []
    return np.column_stack(cols), labels


def projection_distance(image, source, tol=1e-10):
    if image.shape[1] == 0:
        return 1.0, 0, np.inf
    u, s, vh = svd(image, full_matrices=False)
    rank = int(np.sum(s > tol * s[0])) if len(s) else 0
    if rank == 0:
        return 1.0, 0, np.inf
    q = u[:, :rank]
    proj = q @ (q.conj().T @ source)
    rel = norm(source - proj) / max(norm(source), 1e-30)
    cond = float(s[0] / s[rank - 1])
    return rel, rank, cond


def run():
    print("E73.011 image ablation probe")
    print("case             cols rank    condImg      relDist")
    lam, n_modes = 14, 18
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    b = off_nodes[0]
    h, mu, idx, d, L, xi = setup_full(lam, n_modes)
    src = source_vector(b, off_nodes, crit_nodes, d, L)
    aop = h - mu * np.eye(h.shape[0])

    tests = [
        ("all-p2", lambda lab: lab[2] <= 2),
        ("r1-only", lambda lab: lab[2] == 1),
        ("r2-only", lambda lab: lab[2] == 2),
        ("crit0", lambda lab: lab[0] == 0 and lab[2] <= 2),
        ("crit1", lambda lab: lab[0] == 1 and lab[2] <= 2),
        ("crit2", lambda lab: lab[0] == 2 and lab[2] <= 2),
        ("crit3", lambda lab: lab[0] == 3 and lab[2] <= 2),
        ("crit4", lambda lab: lab[0] == 4 and lab[2] <= 2),
        ("off0", lambda lab: lab[1] == 0 and lab[2] <= 2),
        ("off1", lambda lab: lab[1] == 1 and lab[2] <= 2),
        ("off2", lambda lab: lab[1] == 2 and lab[2] <= 2),
        ("crit0+4", lambda lab: lab[0] in (0, 4) and lab[2] <= 2),
        ("off0+1", lambda lab: lab[1] in (0, 1) and lab[2] <= 2),
    ]

    for name, keep in tests:
        basis, labels = basis_cols(off_nodes, crit_nodes, d, L, 2, keep)
        image = aop @ basis
        rel, rank, cond = projection_distance(image, src)
        print(f"{name:14s} {basis.shape[1]:5d} {rank:4d} {cond:10.2e} {rel:10.2e}")


if __name__ == "__main__":
    run()
