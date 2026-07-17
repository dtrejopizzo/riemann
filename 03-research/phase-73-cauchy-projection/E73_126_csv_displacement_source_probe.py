#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, lstsq, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    if xi[len(xi) // 2] < 0:
        xi = -xi
    d = 2.0 * np.pi * idx / L
    mu = vals[0]
    return h, mu, d, L, xi


def source_basis(d, gamma, max_power=3):
    cols = []
    labels = []
    den1 = d + gamma
    cols.append(1.0 / den1)
    labels.append("1/(d+g)")
    den2 = d * d + gamma * gamma
    for r in range(max_power + 1):
        cols.append((d ** r) / den2)
        labels.append(f"d^{r}/quad")
    for q in range(1, max_power + 2):
        cols.append(1.0 / (den2 ** q))
        labels.append(f"quad^-{q}")
        cols.append(d / (den2 ** q))
        labels.append(f"d*quad^-{q}")
    # Endpoint/low polynomial modes.
    for r in range(5):
        cols.append((d / max(np.max(np.abs(d)), 1.0)) ** r)
        labels.append(f"poly{r}")
    S = np.column_stack(cols)
    return S, labels


def probe(lam, n_modes, gamma):
    h, mu, d, L, xi = setup(lam, n_modes)
    A = h - mu * np.eye(len(d))
    S, labels = source_basis(d, gamma)
    AS = A @ S
    k = 1.0 / (-gamma - d)
    coeff, *_ = lstsq(AS, k, rcond=1e-12)
    approx = AS @ coeff
    resid = k - approx
    scalar_before = abs(float(np.dot(xi, k)))
    scalar_after = abs(float(np.dot(xi, resid)))
    ambient_rel = norm(resid) / max(norm(k), 1e-300)
    return L, scalar_before, scalar_after, ambient_rel, len(labels)


def run():
    print("E73.126 CSV displacement source probe")
    print("Projects k_gamma onto (C_E-mu) applied to rational source vectors.")
    print("Success channel is scalar residual <xi,resid>, not ambient norm.")
    print(" lam     L gamma    beforeB   afterB ambientB nsrc status")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        for gamma in [GAMMAS[0], GAMMAS[1], GAMMAS[2]]:
            L, before, after, ambient, nsrc = probe(lam, n_modes, gamma)
            ok = bexp(after, L) <= -17.0
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(before, L):9.3f} {bexp(after, L):8.3f}"
                f" {bexp(ambient, L):8.3f} {nsrc:4d} {'PASS' if ok else 'FAIL'}"
            )


if __name__ == "__main__":
    run()

