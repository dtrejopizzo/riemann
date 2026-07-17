#!/usr/bin/env python3
import sys
import cmath
import numpy as np
from numpy.linalg import eigh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import pi_kernel  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def setup_exact(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    d = 2.0 * np.pi * idx / L
    return d, L, xi


def scalar_terms(b, off_nodes, crit_nodes, d, xi, L):
    terms = []
    for k in crit_nodes:
        gamma = (-1j * k).real
        mesh_res = cmath.exp(1j * gamma * L) - 1.0
        cauchy = np.sum(np.conjugate(xi) / (gamma + d))
        terms.append(pi_kernel(b, k, off_nodes) * mesh_res * cauchy)
    return np.array(terms, dtype=complex)


def run():
    print("E73.160 scalar dual cancellation probe")
    print("Measures termwise l1 versus signed scalar sum in the final CC-PROJ formula.")
    print(" lam     L b      l1B signedB cancelB maxTermB phaseVar")
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        d, L, xi = setup_exact(lam, n_modes)
        off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
        for bi, b in enumerate(off_nodes):
            terms = scalar_terms(b, off_nodes, crit_nodes, d, xi, L)
            l1 = np.sum(np.abs(terms))
            signed = abs(np.sum(terms))
            cancel = signed / max(l1, 1e-300)
            max_term = np.max(np.abs(terms))
            phases = np.angle(terms[np.abs(terms) > 1e-300])
            phase_var = float(np.std(np.unwrap(phases))) if len(phases) else 0.0
            print(
                f"{lam:4d} {L:7.3f} {bi:1d}"
                f" {bexp(l1, L):8.3f}"
                f" {bexp(signed, L):8.3f}"
                f" {bexp(cancel, L):8.3f}"
                f" {bexp(max_term, L):8.3f}"
                f" {phase_var:8.3f}"
            )


if __name__ == "__main__":
    run()
