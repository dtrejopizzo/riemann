#!/usr/bin/env python3
"""Test whether critical Cauchy cancellation extends to confluent jets."""

import sys

import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def bexp(x, L):
    return np.log(max(float(abs(x)), 1e-300)) / np.log(L)


def jet_rows(gamma, d, max_order):
    # Two reflected resolvents and their normalized derivatives.  Factorials
    # are omitted because max_order is fixed and only L-scaling is tested.
    return [
        np.vstack([(1j * (d - gamma)) ** (-r), (1j * (d + gamma)) ** (-r)])
        for r in range(1, max_order + 1)
    ]


def run():
    print("E74.21 critical Cauchy-jet bootstrap audit")
    print("Each j_r is ||Q^(r)xi|| after row normalization; tiny j1 but large higher jets rejects neighborhood regularity.")
    print(" lam      L gamma   j1B   j2B   j3B   j4B   j5B random1B")
    rng = np.random.default_rng(74021)
    for lam, n_modes in [(12, 20), (16, 24), (20, 28), (24, 32)]:
        h, idx, L = build(lam, n_modes, include_arith=True)
        vals, vecs = eigh(h)
        xi = vecs[:, 0].astype(complex)
        xi /= norm(xi)
        random = rng.normal(size=len(idx)) + 1j * rng.normal(size=len(idx))
        random /= norm(random)
        d = 2.0 * np.pi * idx / L
        for gamma in GAMMAS[:3]:
            rows = jet_rows(gamma, d, 5)
            jets = []
            for q in rows:
                qn = q / np.maximum(np.linalg.norm(q, axis=1, keepdims=True), 1e-300)
                jets.append(norm(qn @ xi))
            q1 = rows[0] / np.maximum(np.linalg.norm(rows[0], axis=1, keepdims=True), 1e-300)
            random1 = norm(q1 @ random)
            print(
                f"{lam:4d} {L:8.3f} {gamma:6.2f}"
                + "".join(f" {bexp(v,L):5.2f}" for v in jets)
                + f" {bexp(random1,L):8.2f}"
            )


if __name__ == "__main__":
    run()
