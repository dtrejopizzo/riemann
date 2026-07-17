#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    h0, _, _ = build(lam, n_modes, include_arith=False)
    vals, vecs = np.linalg.eigh(h)
    mu = vals[0]
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h.astype(complex), h0.astype(complex), idx.astype(int), d, L, float(mu), xi.astype(complex)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def rowspace_basis(rows, tol=1e-10):
    if rows.size == 0:
        return rows
    _u, s, vh = svd(rows, full_matrices=False)
    if len(s) == 0:
        return rows[:0]
    rank = int(np.sum(s > tol * s[0]))
    return vh[:rank, :]


def project_to_rowspace(row, basis):
    if basis.shape[0] == 0:
        return np.zeros_like(row)
    return (row @ basis.conj().T) @ basis


def poly_columns(Q, d, degree=4):
    cols = []
    for j in range(Q.shape[0]):
        base = Q[j].conj()
        for k in range(degree + 1):
            cols.append((d**k) * base)
    return np.column_stack(cols)


def dd_local_columns(gamma, d, L, rat_power=1):
    cols = []
    den = d * d - gamma * gamma
    for u in [gamma, -gamma]:
        dd = np.array([dd_kernel(u, dm, L) for dm in d], dtype=complex)
        cols.append(dd)
        cols.append((d * d) * dd)
        cols.append((d**4) * dd)
        for m in range(1, rat_power + 1):
            cols.append(dd / (den**m))
            cols.append((d * d) * dd / (den**m))
    return np.column_stack(cols)


def cl_action_columns(Q, d, H, H0):
    # First finite proxy for the E73.274 coupled Loewner-principal module:
    # include the Cauchy rows and their images under the full Gamma-prime
    # action, archimedean action, and prime action.  This is a falsifier
    # module, not a symbolic proof basis.
    Hp = H0 - H
    cols = []
    for j in range(Q.shape[0]):
        q = Q[j].conj()
        seeds = [
            q,
            (d**2) * q,
            (d**4) * q,
            H @ q,
            H0 @ q,
            Hp @ q,
            (d**2) * (H @ q),
            (d**2) * (H0 @ q),
            (d**2) * (Hp @ q),
        ]
        cols.extend(seeds)
    return np.column_stack(cols)


def module_rows(module, gamma, Q, d, L, H, H0, E):
    if module == "poly":
        prim = poly_columns(Q, d, degree=4)
    elif module == "dd":
        prim = dd_local_columns(gamma, d, L, rat_power=1)
    elif module == "cl":
        prim = cl_action_columns(Q, d, H, H0)
    elif module == "dd+cl":
        prim = np.column_stack([dd_local_columns(gamma, d, L, rat_power=1), cl_action_columns(Q, d, H, H0)])
    else:
        raise ValueError(module)
    return prim.conj().T @ E, prim.shape[1]


def run():
    print("E73.275 APR coupled-Loewner coborder smoke test")
    print("Tests fixed primitive modules for rho=qH(I-P) as Y*E+r.")
    print("Pairing is invariant for exact coborders; useful signal is residual geometry, not scalar cancellation.")
    print(
        " lam      L gamma row module dim rank centerB resPairB resNormB "
        "removedNormB cauchyLeakB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        H, H0, _idx, d, L, mu, xi = setup(lam, n_modes)
        E = H - mu * np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            R = np.eye(len(d), dtype=complex) - P
            for row_id in range(2):
                rho = Q[row_id] @ H @ R
                center = rho @ xi
                for module in ["poly", "dd", "cl", "dd+cl"]:
                    rows, dim = module_rows(module, gamma, Q, d, L, H, H0, E)
                    basis = rowspace_basis(rows)
                    generated = project_to_rowspace(rho, basis)
                    res = rho - generated
                    cauchy_leak = norm(res @ Q.conj().T)
                    print(
                        f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                        f" {module:>6s} {dim:4d} {basis.shape[0]:4d}"
                        f" {bexp(center, L):8.2f} {bexp(res @ xi, L):8.2f}"
                        f" {bexp(norm(res), L):8.2f} {bexp(norm(generated), L):11.2f}"
                        f" {bexp(cauchy_leak, L):11.2f}"
                    )


if __name__ == "__main__":
    run()
