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


def canonical_basis(off_nodes, crit_nodes, d, L, max_power, endpoint_powers):
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
        for q in endpoint_powers:
            cols.append((d ** (2 * q)) * dd)
            labels.append(("endpoint", ki, -1, q))
    return np.column_stack(cols), labels


def action_matrix(src_basis, h, mu, off_nodes, crit_nodes, d, L):
    prim, plabels = canonical_basis(off_nodes, crit_nodes, d, L, max_power=2, endpoint_powers=[1])
    image = (h - mu * np.eye(h.shape[0], dtype=complex)) @ prim
    cols = []
    rels = []
    for j in range(image.shape[1]):
        coeff, *_ = lstsq(src_basis, image[:, j], rcond=None)
        cols.append(coeff)
        rels.append(norm(image[:, j] - src_basis @ coeff) / max(norm(image[:, j]), 1e-30))
    return np.column_stack(cols), plabels, max(rels)


def orth_basis(mat, reltol=1e-8):
    u, s, _vh = svd(mat, full_matrices=False)
    if len(s) == 0 or s[0] == 0:
        return np.zeros((mat.shape[0], 0), dtype=complex), s
    rank = int(np.sum(s > reltol * s[0]))
    return u[:, :rank], s


def row_project(row, basis):
    if basis.shape[1] == 0:
        return np.zeros_like(row)
    return (row @ basis) @ basis.conj().T


def run():
    print("E73.280 coupled pairing graph probe")
    print("Studies ell(c)=<xi,S c> against generated action columns and APR coefficient vectors.")
    print("kerDist: distance of APR coefficient vector to ker(ell) within canonical coordinates.")
    print("genEllB: size of ell on generated action columns; graphCancel tests ell(c-m)+ell(m).")
    print(
        " lam      L gamma row fitRel imageRel rS rM ellNormB genEllB centerB "
        "kerDist graphErrB bestGenB residB"
    )
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20)]:
        h, mu, d, L, xi = setup(lam, n_modes)
        src, labels = canonical_basis(off_nodes, crit_nodes, d, L, max_power=3, endpoint_powers=[1, 2])
        action, _plabels, image_rel = action_matrix(src, h, mu, off_nodes, crit_nodes, d, L)
        qsrc, ssrc = orth_basis(src, reltol=1e-10)
        qact, sact = orth_basis(action, reltol=1e-6)
        ell = xi.conj().T @ src
        ell_norm = norm(ell)
        gen_ell = ell @ action
        # Kernel of ell in coefficient coordinates.  Distance of c to ker(ell)
        # equals |ell(c)|/||ell|| in Euclidean coefficient norm.
        for gamma in GAMMAS[:3]:
            q = cauchy_rows(-1j * gamma, d)
            r = np.eye(len(d), dtype=complex) - projector(q)
            for row in range(2):
                rho = q[row] @ h @ r
                c, *_ = lstsq(src, rho, rcond=None)
                fit = src @ c
                fit_rel = norm(rho - fit) / max(norm(rho), 1e-30)
                center = ell @ c
                kerdist = abs(center) / max(ell_norm * norm(c), 1e-300)
                # Best generated component in coefficient norm, then exact scalar split.
                m = row_project(c, qact)
                u = c - m
                graph_err = abs((ell @ m) + (ell @ u) - center)
                best_gen = ell @ m
                resid = ell @ u
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row:3d}"
                    f" {fit_rel:7.1e} {image_rel:8.1e} {qsrc.shape[1]:3d} {qact.shape[1]:3d}"
                    f" {bexp(ell_norm,L):8.2f} {bexp(norm(gen_ell),L):8.2f}"
                    f" {bexp(center,L):8.2f} {kerdist:8.1e}"
                    f" {bexp(graph_err,L):9.2f} {bexp(best_gen,L):8.2f}"
                    f" {bexp(resid,L):7.2f}"
                )


if __name__ == "__main__":
    run()
