#!/usr/bin/env python3
import cmath
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel, pi_kernel  # noqa: E402


def setup_exact(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    phase = np.sign(np.real(np.vdot(xi, np.ones_like(xi))))
    if phase == 0:
        phase = 1.0
    xi = phase * xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual, vals[0], idx.astype(int), d, L, xi


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
                cols.append(dd / (denom ** r))
                labels.append(("rat", ki, bi, r))
        for q in endpoint_powers:
            cols.append((d ** (2 * q)) * dd)
            labels.append(("endpoint", ki, -1, q))
    return np.column_stack(cols), labels


def exact_source_coeffs(b, off_nodes, crit_nodes, labels):
    coeff = np.zeros(len(labels), dtype=complex)
    for j, label in enumerate(labels):
        kind, ki, _, _ = label
        if kind == "cauchy0":
            coeff[j] = pi_kernel(b, crit_nodes[ki], off_nodes)
    return coeff


def cauchy_values(xi, crit_nodes, d, L):
    vals = []
    for k in crit_nodes:
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        vals.append(np.vdot(xi, dd))
    return np.array(vals, dtype=complex)


def label_masks(labels):
    principal = np.array([lab[0] != "endpoint" for lab in labels], dtype=bool)
    cauchy0_idx = [j for j, lab in enumerate(labels) if lab[0] == "cauchy0"]
    return principal, cauchy0_idx


def solve_in_basis(basis, target):
    coeff, *_ = lstsq(basis, target, rcond=None)
    resid = target - basis @ coeff
    rel = norm(resid) / max(norm(target), 1e-30)
    return coeff, rel


def safe_cos(a, b):
    den = norm(a) * norm(b)
    if den == 0:
        return 0.0
    return float(abs(np.vdot(a, b)) / den)


def run_case(lam, n_modes):
    h, mu, idx, d, L, xi = setup_exact(lam, n_modes)
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    prim, _ = canonical_basis(off_nodes, crit_nodes, d, L, max_power=2, endpoint_powers=[1])
    src_basis, slabels = canonical_basis(off_nodes, crit_nodes, d, L, max_power=3, endpoint_powers=[1, 2])
    principal, cauchy0_idx = label_masks(slabels)

    image = (h - mu * np.eye(h.shape[0])) @ prim
    bcols = []
    for j in range(image.shape[1]):
        coeff, _ = solve_in_basis(src_basis, image[:, j])
        bcols.append(coeff)
    coeff_action = np.column_stack(bcols)
    principal_action = coeff_action[principal, :]
    cvals = cauchy_values(xi, crit_nodes, d, L)

    rows = []
    for b in off_nodes:
        source_coeff = exact_source_coeffs(b, off_nodes, crit_nodes, slabels)
        pi_vec = source_coeff[cauchy0_idx]
        y, *_ = lstsq(principal_action, source_coeff[principal], rcond=None)
        residual_coeff = source_coeff - coeff_action @ y
        delta = residual_coeff[cauchy0_idx]

        scalar_pi = np.vdot(pi_vec, np.conj(cvals))
        scalar_delta = np.vdot(delta, np.conj(cvals))
        # Direct mesh convention: sum_j coeff_j <xi, basis_j>.
        scalar_pi = np.sum(pi_vec * cvals)
        scalar_delta = np.sum(delta * cvals)
        exp_pi = abs(cmath.exp(b.real * L) * scalar_pi)
        exp_delta = abs(cmath.exp(b.real * L) * scalar_delta)

        rows.append(
            {
                "b": b,
                "deltaNormRatio": norm(delta) / max(norm(pi_vec), 1e-30),
                "deltaCosPi": safe_cos(delta, pi_vec),
                "deltaMaxRatio": float(np.max(np.abs(delta)) / max(np.max(np.abs(pi_vec)), 1e-30)),
                "expPi": exp_pi,
                "expDelta": exp_delta,
                "scalarRatio": exp_delta / max(exp_pi, 1e-300),
            }
        )
    return {"lam": lam, "L": L, "dim": len(idx), "rows": rows}


def run():
    print("E73.164 cauchy0 delta probe")
    print("Compares canonical cauchy0 defect delta against original Pi source coefficients.")
    print(" lam     L   dim      bRe  ||d||/||Pi|| cos(d,Pi) maxRatio      expPi   expDelta scalarRatio")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24), (24, 28)]:
        out = run_case(lam, n_modes)
        for row in out["rows"]:
            print(
                f"{out['lam']:4d} {out['L']:7.3f} {out['dim']:5d} {row['b'].real:8.3f} "
                f"{row['deltaNormRatio']:12.3e} {row['deltaCosPi']:9.3f} "
                f"{row['deltaMaxRatio']:8.3e} {row['expPi']:10.3e} "
                f"{row['expDelta']:10.3e} {row['scalarRatio']:11.3e}"
            )


if __name__ == "__main__":
    run()
