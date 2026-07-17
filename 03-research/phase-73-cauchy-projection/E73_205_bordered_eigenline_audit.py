#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cond, eigh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")

from E71_9_relative_arch_background_probe import build  # noqa: E402


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def audit(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    mu = vals[0]
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    j0 = int(np.argmax(np.abs(xi)))
    ell = np.zeros_like(xi)
    ell[j0] = 1.0 / xi[j0]
    n = len(xi)
    top = np.hstack([h - mu * np.eye(n), -xi[:, None]])
    bot = np.zeros((1, n + 1))
    bot[0, :n] = ell
    J = np.vstack([top, bot])
    F = np.concatenate([(h - mu * np.eye(n)) @ xi, [ell @ xi - 1.0]])
    step = solve(J, F)
    return {
        "L": L,
        "dim": n,
        "gap": vals[1] - vals[0],
        "res": norm(F),
        "cond": cond(J),
        "step": norm(step),
        "mu": mu,
    }


def run():
    print("E73.205 bordered eigenline conditioning audit")
    print("Uses current double matrix; this is a precision-demand audit, not a proof.")
    print(" lam     L  dim    muB    gapB    resB  condB  stepB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28)]:
        row = audit(lam, n_modes)
        L = row["L"]
        print(
            f"{lam:4d} {L:7.3f} {row['dim']:4d}"
            f" {bexp(row['mu'], L):6.2f} {bexp(row['gap'], L):7.2f}"
            f" {bexp(row['res'], L):7.2f} {bexp(row['cond'], L):6.2f}"
            f" {bexp(row['step'], L):7.2f}"
        )


if __name__ == "__main__":
    run()
