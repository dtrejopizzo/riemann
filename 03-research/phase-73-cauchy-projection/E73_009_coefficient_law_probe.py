#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, lstsq, norm

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
    labels = []
    for ki, k in enumerate(crit_nodes):
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        for bi, beta in enumerate(off_nodes):
            beta2 = beta * beta
            denom = np.array([dm * dm + beta2 for dm in d], dtype=complex)
            for r in range(1, max_power + 1):
                cols.append(dd / (denom ** r))
                labels.append((ki, bi, r))
    return np.column_stack(cols), labels


def coeffs_for_case(lam, n_modes, off_nodes, crit_nodes, b, max_power):
    h, mu, idx, d, L, xi = setup_full(lam, n_modes)
    src = source_vector(b, off_nodes, crit_nodes, d, L)
    basis, labels = ratdd_basis(off_nodes, crit_nodes, d, L, max_power)
    image = (h - mu * np.eye(h.shape[0])) @ basis
    coeffs, *_ = lstsq(image, src, rcond=None)
    rel = norm(src - image @ coeffs) / norm(src)
    return L, labels, coeffs, rel


def run():
    print("E73.009 coefficient law probe")
    print("Dominant normalized coefficients for pwr=2 structured primitive")
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    b = off_nodes[0]
    cases = [(8, 12), (10, 14), (12, 16), (14, 18)]
    all_rows = []
    labels_ref = None
    for lam, n_modes in cases:
        L, labels, coeffs, rel = coeffs_for_case(lam, n_modes, off_nodes, crit_nodes, b, 2)
        if labels_ref is None:
            labels_ref = labels
        mags = np.abs(coeffs)
        top = np.argsort(-mags)[:8]
        print(f"\nlam={lam} L={L:.3f} relDef={rel:.3e}")
        print(" rank  label(crit,off,r)       coeff                  coeff/L")
        for rank, j in enumerate(top, 1):
            c = coeffs[j]
            print(
                f"{rank:5d} {labels[j]!s:18s} "
                f"{c.real:+.4e}{c.imag:+.4e}j "
                f"{(c/L).real:+.4e}{(c/L).imag:+.4e}j"
            )
        all_rows.append(coeffs)

    # Stability of coefficient directions after normalizing by vector norm.
    print("\ncosine similarity of coefficient vectors")
    vecs = [c / max(norm(c), 1e-30) for c in all_rows]
    for i in range(len(vecs) - 1):
        sim = abs(np.vdot(vecs[i], vecs[i + 1]))
        print(f"case {i}->{i+1}: {sim:.6f}")


if __name__ == "__main__":
    run()
