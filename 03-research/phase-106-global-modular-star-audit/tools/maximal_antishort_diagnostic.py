#!/usr/bin/env python3
"""Diagnostic for the maximal anti-short of a finite prime head.

The retained system is Gamma only and the omitted tail is all literal
prime-power atoms.  The test vector is the exact four-zero complement mode
from 106.62.  Even derivatives of the theta kernel are evaluated by an
analytic polynomial recurrence, not by finite differences.

This is a floating-point diagnostic, not an interval certificate.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parent))

from finite_head_mean_periodic_gram import (  # noqa: E402
    ZEROS,
    riemann_kernel,
    source_gram,
)


def next_derivative_polynomial(polynomial: np.ndarray) -> np.ndarray:
    """Apply D=2t d/dt to t^(5/4) exp(-t) P(t)."""
    alpha = 5.0 / 4.0
    derivative = np.arange(1, len(polynomial)) * polynomial[1:]
    result = np.zeros(len(polynomial) + 1)
    result[1 : len(derivative) + 1] += 2.0 * derivative
    result[: len(polynomial)] += 2.0 * alpha * polynomial
    result[1 : len(polynomial) + 1] -= 2.0 * polynomial
    return result


def kernel_even_derivatives(
    x: np.ndarray, maximum_radical: int
) -> list[np.ndarray]:
    polynomials = [np.array([-3.0, 2.0])]
    for _ in range(2 * maximum_radical):
        polynomials.append(next_derivative_polynomial(polynomials[-1]))

    absolute_x = np.abs(x)
    active = absolute_x < 3.0
    y = absolute_x[active]
    exponential = np.exp(2.0 * y)
    raw: list[np.ndarray] = []
    for order in range(2 * maximum_radical + 1):
        value = np.zeros_like(x)
        polynomial = polynomials[order]
        for m in range(1, 30):
            t = math.pi * m * m * exponential
            base = math.pi * m * m * np.exp(2.5 * y - t)
            value[active] += base * np.polynomial.polynomial.polyval(
                t, polynomial
            )
        raw.append(value)

    h = np.cosh(x / 2.0)
    scale = 0.5 / np.trapz(h * raw[0], x)
    return [scale * value for value in raw]


def run(
    dx: float, head: int, maximum_radical: int, maximum_zero_span: int
) -> None:
    maximum_x = 3.2
    x = np.arange(-maximum_x, maximum_x, dx)
    k = riemann_kernel(x)
    h = np.cosh(x / 2.0)
    mu = 2.0 * h * k

    ordinates = np.loadtxt(ZEROS)[:4]
    q4 = np.array([1.0, -2.0, 2.0, -1.0]) @ (
        np.cos(ordinates[:, None] * x) / h
    )

    derivatives = kernel_even_derivatives(x, maximum_radical)
    columns = [q4]
    active = k > 1.0e-150
    for order in range(1, maximum_radical + 1):
        radical = np.zeros_like(x)
        radical[active] = (
            derivatives[2 * order][active] / k[active]
            - 4.0 ** (-order)
        )
        columns.append(radical)
    q = np.column_stack(columns)

    means = q.T @ (mu * dx)
    norm = q.T @ (q * (mu * dx)[:, None]) - np.outer(means, means)
    gamma = source_gram(x, dx, k, q, 1)
    full = source_gram(x, dx, k, q, head)
    tail = full - gamma
    full_defect = full - 0.5 * norm
    gamma_defect = gamma - 0.5 * norm

    print(f"dx={dx:g}; complete numerical prime head={head}")
    print(
        "q4 defects:",
        f"Gamma={gamma_defect[0, 0]:.12f};",
        f"full={full_defect[0, 0]:.12f};",
        f"prime tail={tail[0, 0]:.12f}",
    )
    relative_residual = (
        np.diag(full_defect)[1:] / np.diag(tail)[1:]
    )
    print("relative full-radical residuals:", relative_residual)

    print("M  min(correlation Gram)  tail short       anti-short")
    print(f"0  {'-':>21}  {tail[0,0]: .12f}  {gamma_defect[0,0]: .12f}")
    for dimension in range(1, maximum_radical + 1):
        tail_rr = tail[1 : dimension + 1, 1 : dimension + 1]
        diagonal = np.sqrt(np.diag(tail_rr))
        correlation = tail_rr / diagonal[:, None] / diagonal[None, :]
        tail_rq = tail[1 : dimension + 1, 0] / diagonal
        short = tail[0, 0] - tail_rq @ np.linalg.solve(
            correlation, tail_rq
        )
        anti_short = full_defect[0, 0] - short
        print(
            f"{dimension:d}  {np.linalg.eigvalsh(correlation)[0]: .12f}"
            f"  {short: .12f}  {anti_short: .12f}"
        )

    # A separate, preconditioned audit on growing zero-mode spans.  Raw
    # radical columns are normalized before QR; otherwise their rapidly
    # increasing theta-polynomial scales hide the actual subspace.  The
    # order of projection matters: first orthonormalize the *actual*
    # radical space, then project the zero modes into its orthogonal
    # complement.  Projecting the radicals away from the zero modes would
    # change the negative subspace and would not compute an anti-short.
    square_root_weight = np.sqrt(mu * dx)
    qr_active = square_root_weight > 1.0e-100
    span = min(maximum_zero_span, len(np.loadtxt(ZEROS)))
    all_ordinates = np.loadtxt(ZEROS)[:span]
    raw_zero = (np.cos(all_ordinates[:, None] * x) / h).T
    radical_columns = q[:, 1:].copy()
    for index in range(radical_columns.shape[1]):
        radical_columns[:, index] -= radical_columns[:, index] @ (mu * dx)
        radical_columns[:, index] /= math.sqrt(
            radical_columns[:, index]
            @ (radical_columns[:, index] * (mu * dx))
        )
    radical_u, radical_r = np.linalg.qr(
        radical_columns[qr_active]
        * square_root_weight[qr_active, None],
        mode="reduced",
    )
    radical_modes = np.zeros_like(radical_columns)
    radical_modes[qr_active] = (
        radical_u / square_root_weight[qr_active, None]
    )

    print(
        "growing-span conditioning:",
        f"radical orthogonality={np.linalg.norm(radical_modes.T @ (radical_modes * (mu * dx)[:, None]) - np.eye(maximum_radical)):.3e};",
        f"smallest preconditioned radical QR diagonal={np.min(np.abs(np.diag(radical_r))):.3e}",
    )
    print("span  radicals  minimum anti-short  negative count")
    for radical_dimension in range(0, maximum_radical + 1, 2):
        radical_block = radical_modes[:, :radical_dimension]
        zero_residual = raw_zero.copy()
        if radical_dimension:
            zero_residual -= radical_block @ (
                radical_block.T @ (raw_zero * (mu * dx)[:, None])
            )
        zero_u, zero_r = np.linalg.qr(
            zero_residual[qr_active]
            * square_root_weight[qr_active, None],
            mode="reduced",
        )
        zero_modes = np.zeros_like(raw_zero)
        zero_modes[qr_active] = (
            zero_u / square_root_weight[qr_active, None]
        )

        combined = np.column_stack((zero_modes, radical_block))
        combined_norm = combined.T @ (combined * (mu * dx)[:, None])
        combined_gamma = source_gram(x, dx, k, combined, 1)
        combined_defect = combined_gamma - 0.5 * combined_norm
        combined_defect = (combined_defect + combined_defect.T) / 2.0
        radical_start = span
        if radical_dimension:
            negative = combined_defect[
                radical_start:, radical_start:
            ]
            largest_radical = np.linalg.eigvalsh(negative)[-1]
        else:
            largest_radical = float("nan")
        print(
            f"M={radical_dimension:2d}; combined orthogonality="
            f"{np.linalg.norm(combined_norm - np.eye(span + radical_dimension)):.3e}; "
            f"largest radical eigenvalue={largest_radical:.3e}"
        )

        for zero_span in (4, 10, 20, 40):
            if zero_span > span:
                continue
            block = combined_defect[:zero_span, :zero_span].copy()
            if radical_dimension:
                cross = combined_defect[
                    :zero_span, radical_start:
                ]
                block -= cross @ np.linalg.solve(negative, cross.T)
            eigenvalues = np.linalg.eigvalsh((block + block.T) / 2.0)
            print(
                f"{zero_span:4d}  {radical_dimension:8d}"
                f"  {eigenvalues[0]: .12f}"
                f"  {np.count_nonzero(eigenvalues < -1.0e-7):5d}"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dx", type=float, default=0.0005)
    parser.add_argument("--head", type=int, default=1000)
    parser.add_argument("--radicals", type=int, default=12)
    parser.add_argument("--zero-span", type=int, default=40)
    args = parser.parse_args()
    run(args.dx, args.head, args.radicals, args.zero_span)


if __name__ == "__main__":
    main()
