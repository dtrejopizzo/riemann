#!/usr/bin/env python3
"""Diagnostic spectrum of the positive flag reference from 104_30.

This is deliberately *not* a certificate.  The Li coefficients are extracted
in float64 by a Cauchy/FFT computation at two radii.  Agreement between the
two radii is only a necessary stability check: both evaluations share the
same Borwein zeta implementation, FFT arithmetic, and floating-point model.

For a fixed base M, the coordinate basis is

    b_0 = g_M,  b_r = phi_{M+r-1}  (r >= 1),

and the positive reference is diagonal:

    A_flag = diag(A_M, Delta A_M, Delta A_{M+1}, ...).

The renormalised prime--pole limit Q has Q[g_n] = A_n-lambda_n.  The script
builds each finite section

    K = A_flag^(-1/2) Q A_flag^(-1/2),

checks the exact telescoping identities numerically, computes its spectrum,
and computes the spectral mass of every hard-edge prefix u_n in
[threshold, infinity).
"""

from __future__ import annotations

import argparse
import math
import os
import sys
from dataclasses import dataclass

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
P103_TOOLS = os.path.normpath(
    os.path.join(HERE, "..", "..", "phase-103-direct-a1-closure", "tools")
)
sys.path.insert(0, P103_TOOLS)

from arch_and_margin import lambda_arch  # noqa: E402
from zeta_tools import li_lambda  # noqa: E402


@dataclass
class FlagSection:
    """Matrices in the coefficient basis (g_M, phi_M, ..., phi_{N-1})."""

    base: int
    top: int
    q: np.ndarray
    q_form: np.ndarray
    a_diag: np.ndarray
    whitened: np.ndarray


def toeplitz_coefficients(b: np.ndarray) -> np.ndarray:
    """q_0=B_1, q_d=(B_{d+1}-2B_d+B_{d-1})/2 for d>=1."""
    top = len(b) - 1
    q = np.empty(top, dtype=float)
    q[0] = b[1]
    if top > 1:
        d = np.arange(1, top)
        q[1:] = 0.5 * (b[d + 1] - 2.0 * b[d] + b[d - 1])
    return q


def build_flag_section(a: np.ndarray, b: np.ndarray, base: int, top: int) -> FlagSection:
    if not (1 <= base <= top < len(a)):
        raise ValueError("need 1 <= base <= top and A,B through top")

    q = toeplitz_coefficients(b)
    dim = 1 + top - base
    q_form = np.empty((dim, dim), dtype=float)
    q_form[0, 0] = b[base]

    tail = np.arange(base, top, dtype=int)
    if tail.size:
        # Q(g_M,phi_k)=sum_{d=k-M+1}^k q_d.
        cross = np.array(
            [np.sum(q[k - base + 1 : k + 1]) for k in tail], dtype=float
        )
        cross_telescoped = 0.5 * (
            (b[tail + 1] - b[tail])
            - (b[tail - base + 1] - b[tail - base])
        )
        if not np.allclose(cross, cross_telescoped, rtol=2e-10, atol=2e-10):
            raise AssertionError("g_M--phi_k cross-term index mismatch")
        q_form[0, 1:] = cross
        q_form[1:, 0] = cross
        distances = np.abs(tail[:, None] - tail[None, :])
        q_form[1:, 1:] = q[distances]

    a_diag = np.empty(dim, dtype=float)
    a_diag[0] = a[base]
    if tail.size:
        a_diag[1:] = a[tail + 1] - a[tail]
    if np.any(a_diag <= 0.0):
        bad = int(np.flatnonzero(a_diag <= 0.0)[0])
        raise ArithmeticError(f"A_flag is not positive at coordinate {bad}")

    roots = np.sqrt(a_diag)
    whitened = q_form / np.outer(roots, roots)
    whitened = 0.5 * (whitened + whitened.T)

    # Telescoping checks on every prefix in this finite section.
    for n in range(base, top + 1):
        x = np.zeros(dim)
        x[: 1 + n - base] = 1.0
        q_value = float(x @ q_form @ x)
        a_value = float(np.dot(a_diag, x * x))
        if not math.isclose(q_value, b[n], rel_tol=2e-10, abs_tol=2e-10):
            raise AssertionError(("Q telescoping", n, q_value, b[n]))
        if not math.isclose(a_value, a[n], rel_tol=2e-13, abs_tol=2e-13):
            raise AssertionError(("A telescoping", n, a_value, a[n]))

    return FlagSection(base, top, q, q_form, a_diag, whitened)


def hard_edge_unit(a_diag: np.ndarray, base: int, n: int) -> np.ndarray:
    """A_flag-normalised coordinate vector of g_n."""
    count = 1 + n - base
    u = np.zeros_like(a_diag)
    u[:count] = np.sqrt(a_diag[:count])
    u /= np.linalg.norm(u)
    return u


def ray_statistics(
    section: FlagSection, b: np.ndarray, a: np.ndarray, threshold: float
) -> tuple[np.ndarray, np.ndarray, list[dict[str, float]]]:
    eigenvalues, eigenvectors = np.linalg.eigh(section.whitened)
    high = eigenvalues >= threshold
    rows: list[dict[str, float]] = []
    for n in range(section.base, section.top + 1):
        u = hard_edge_unit(section.a_diag, section.base, n)
        coeff = eigenvectors.T @ u
        weights = coeff * coeff
        expectation = float(u @ section.whitened @ u)
        target = float(b[n] / a[n])
        if not math.isclose(expectation, target, rel_tol=3e-10, abs_tol=3e-10):
            raise AssertionError(("whitened expectation", n, expectation, target))
        rows.append(
            {
                "n": float(n),
                "expectation": expectation,
                "mass_high": float(np.sum(weights[high])),
                "excess_high": float(
                    np.sum(np.maximum(eigenvalues - threshold, 0.0) * weights)
                ),
                "top_overlap": float(weights[-1]),
            }
        )
    return eigenvalues, eigenvectors, rows


def matrix_bounds(section: FlagSection) -> tuple[float, float, float]:
    """Gershgorin upper edge, absolute row norm, weighted Schur bound."""
    k = section.whitened
    abs_rows = np.sum(np.abs(k), axis=1)
    gershgorin_upper = np.max(np.diag(k) + abs_rows - np.abs(np.diag(k)))
    absolute_row = np.max(abs_rows)

    # Schur weights p_i=sqrt(a_i):
    # p_i^{-1} sum_j |K_ij|p_j = a_i^{-1} sum_j |Q_ij|.
    schur = np.max(np.sum(np.abs(section.q_form), axis=1) / section.a_diag)
    return float(gershgorin_upper), float(absolute_row), float(schur)


def selected_rows(rows: list[dict[str, float]]) -> list[dict[str, float]]:
    if len(rows) <= 8:
        return rows
    indices = sorted({0, 1, len(rows) // 4, len(rows) // 2,
                      3 * len(rows) // 4, len(rows) - 2, len(rows) - 1})
    return [rows[index] for index in indices]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=int, default=150)
    parser.add_argument("--nmax", type=int, default=300)
    parser.add_argument("--sections", type=int, nargs="*", default=None)
    parser.add_argument("--radius-a", type=float, default=0.985)
    parser.add_argument("--radius-b", type=float, default=0.975)
    parser.add_argument("--fft-power", type=int, default=18)
    parser.add_argument("--threshold", type=float, default=0.75)
    parser.add_argument(
        "--all-rays", action="store_true", help="print every n rather than selected rays"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.nmax < args.base:
        raise SystemExit("--nmax must be at least --base")
    fft_size = 1 << args.fft_power

    print("DIAGNOSTIC ONLY: float64 Cauchy/FFT Li coefficients; not a certificate")
    print("Double-radius agreement cannot detect shared systematic error.\n")
    print(
        f"base={args.base} nmax={args.nmax} radii=({args.radius_a},"
        f" {args.radius_b}) FFT={fft_size} threshold={args.threshold:.12g}"
    )
    exact_c = 501.0 / 2002.0
    print(
        f"scale-free ceiling 3/4={0.75:.12f}; "
        f"104_26 concrete ceiling 1-501/2002={1.0-exact_c:.12f}\n"
    )

    a = np.zeros(args.nmax + 1, dtype=float)
    for n in range(1, args.nmax + 1):
        a[n] = lambda_arch(n)

    lam_a = li_lambda(args.nmax, r=args.radius_a, M=fft_size)
    lam_b = li_lambda(args.nmax, r=args.radius_b, M=fft_size)
    disagreement = np.abs(lam_a - lam_b)
    worst = int(np.argmax(disagreement)) + 1
    print(
        "extraction stability: "
        f"max |lambda_a-lambda_b|={disagreement[worst-1]:.6e} at n={worst}"
    )

    b_a = np.zeros(args.nmax + 1, dtype=float)
    b_b = np.zeros(args.nmax + 1, dtype=float)
    b_a[1:] = a[1:] - lam_a
    b_b[1:] = a[1:] - lam_b

    sections = args.sections
    if sections is None:
        sections = [min(args.nmax, n) for n in (200, 250, args.nmax)]
    sections = sorted({n for n in sections if args.base <= n <= args.nmax})
    if args.nmax not in sections:
        sections.append(args.nmax)

    for top in sections:
        sec_a = build_flag_section(a, b_a, args.base, top)
        sec_b = build_flag_section(a, b_b, args.base, top)
        eig_a, _, rows_a = ray_statistics(sec_a, b_a, a, args.threshold)
        eig_b, _, rows_b = ray_statistics(sec_b, b_b, a, args.threshold)
        gersh, abs_row, schur = matrix_bounds(sec_a)

        mass_delta = max(
            abs(left["mass_high"] - right["mass_high"])
            for left, right in zip(rows_a, rows_b)
        )
        expectation_delta = max(
            abs(left["expectation"] - right["expectation"])
            for left, right in zip(rows_a, rows_b)
        )
        max_mass = max(rows_a, key=lambda row: row["mass_high"])
        max_excess = max(rows_a, key=lambda row: row["excess_high"])

        print(f"\nSECTION [{args.base},{top}] dimension={len(sec_a.a_diag)}")
        print(
            f"  spectrum radius-a: [{eig_a[0]: .12e}, {eig_a[-1]: .12e}]"
        )
        print(
            f"  spectrum radius-b: [{eig_b[0]: .12e}, {eig_b[-1]: .12e}]"
        )
        print(
            f"  spectral stability: max |eig_a-eig_b|="
            f"{np.max(np.abs(eig_a-eig_b)):.6e}, "
            f"max |K_a-K_b|={np.max(np.abs(sec_a.whitened-sec_b.whitened)):.6e}"
        )
        print(
            f"  q_0={sec_a.q[0]: .12e}  (theoretical limit -gamma); "
            f"sum_{{d<{top}}}|q_d|={np.sum(np.abs(sec_a.q[:top])):.12e}"
        )
        print(
            f"  upper bounds: Gershgorin={gersh:.12e}, "
            f"absolute-row={abs_row:.12e}, weighted-Schur={schur:.12e}"
        )
        print(
            f"  max mass [{args.threshold:g},inf)={max_mass['mass_high']:.6e} "
            f"at n={int(max_mass['n'])}; max excess moment="
            f"{max_excess['excess_high']:.6e} at n={int(max_excess['n'])}"
        )
        print(
            f"  radius stability over rays: max expectation delta={expectation_delta:.6e}, "
            f"max high-mass delta={mass_delta:.6e}"
        )
        print("  ray       Q/A              high-mass        excess            top-overlap")
        shown = rows_a if args.all_rays else selected_rows(rows_a)
        for row in shown:
            print(
                f"  {int(row['n']):4d}  {row['expectation']: .12e}  "
                f"{row['mass_high']:.12e}  {row['excess_high']:.12e}  "
                f"{row['top_overlap']:.12e}"
            )

    print("\nPASS: all finite-section telescoping and whitening identities checked")
    print("STOP: every displayed Q coefficient contains Delta^2(A-lambda);")
    print("      numerical Gershgorin/Schur bounds are not unconditional estimates.")


if __name__ == "__main__":
    main()
