#!/usr/bin/env python3
"""Diagnostic for finite prime-midpoint response kernels.

The exact linear-algebra statement tested here is independent of this
floating-point calculation: if a Hermitian form has more negative
directions than a response map has rows, its response kernel contains a
negative vector.  The script evaluates that obstruction for the literal
Gamma-only zero-mode Gram and the midpoint rows A_p of 106.73.

It also prints the midpoint response of the *adaptive* Schur residual for
the stable finite-head transitions used in 106.80--106.81.  Those rows are
diagnostics only; they do not certify a uniform arithmetic lower bound.
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
    is_prime,
    riemann_kernel,
    source_gram,
)


def setup(dx: float, span: int):
    x = np.arange(-3.2, 3.2 + dx / 2.0, dx)
    kernel = riemann_kernel(x)
    measure = 2.0 * np.cosh(x / 2.0) * kernel
    sqrt_weight = np.sqrt(measure * dx)
    active = sqrt_weight > 1.0e-140
    ordinates = np.loadtxt(ZEROS)[:span]
    raw = (
        np.cos(ordinates[:, None] * x) / np.cosh(x[None, :] / 2.0)
    ).T
    orthogonal, triangular = np.linalg.qr(
        raw[active] * sqrt_weight[active, None], mode="reduced"
    )
    basis = np.zeros_like(raw)
    basis[active] = orthogonal / sqrt_weight[active, None]
    return x, kernel, ordinates, triangular, basis


def midpoint_rows(
    ordinates: np.ndarray,
    triangular: np.ndarray,
    primes: list[int],
    span: int,
) -> np.ndarray:
    rows = []
    for prime in primes:
        midpoint = 0.5 * math.log(prime)
        raw_row = (
            2.0
            * ordinates[:span]
            * np.sin(ordinates[:span] * midpoint)
            + math.tanh(midpoint / 2.0)
            * np.cos(ordinates[:span] * midpoint)
        )
        # basis = raw @ triangular^{-1}
        rows.append(
            np.linalg.solve(triangular[:span, :span].T, raw_row)
        )
    return np.asarray(rows)


def null_restriction(
    form: np.ndarray, response: np.ndarray, tolerance: float
) -> tuple[int, int, float, float]:
    _, singular, right = np.linalg.svd(response, full_matrices=True)
    threshold = tolerance * singular[0] if singular.size else tolerance
    rank = int(np.sum(singular > threshold))
    null_basis = right[rank:].T
    if null_basis.shape[1] == 0:
        return rank, 0, math.nan, math.nan
    restricted = null_basis.T @ form @ null_basis
    values, vectors = np.linalg.eigh(restricted)
    witness = null_basis @ vectors[:, 0]
    relative_residual = float(
        np.linalg.norm(response @ witness)
        / max(np.linalg.norm(response, 2) * np.linalg.norm(witness), 1.0e-300)
    )
    return rank, null_basis.shape[1], float(values[0]), relative_residual


def run(dx: float, span: int, maximum_k: int, tolerance: float) -> None:
    x, kernel, ordinates, triangular, basis = setup(dx, span)
    gamma_defect = source_gram(x, dx, kernel, basis, 1) - 0.5 * np.eye(span)
    negative_index = int(np.sum(np.linalg.eigvalsh(gamma_defect) < 0.0))
    primes = [n for n in range(2, 1000) if is_prime(n)][:maximum_k]
    responses = midpoint_rows(ordinates, triangular, primes, span)

    print(
        f"dx={dx:g}; span={span}; Gamma negative index={negative_index}"
    )
    print("K rank null-dim min(H|ker T_K) relative-response")
    for count in range(1, maximum_k + 1):
        rank, nullity, minimum, residual = null_restriction(
            gamma_defect, responses[:count], tolerance
        )
        print(
            f"{count:2d} {rank:4d} {nullity:8d} "
            f"{minimum: .12e} {residual: .3e}"
        )

    print("\nNatural adaptive Schur residuals")
    print("M head sigma0 min(A) first-prime |A_p(q*)|/||q*||")
    for dimension, head in ((4, 1), (7, 2), (12, 3), (16, 4)):
        if dimension > span:
            continue
        defect = (
            source_gram(x, dx, kernel, basis[:, :dimension], head)
            - 0.5 * np.eye(dimension)
        )
        old = defect[:-1, :-1]
        cross = defect[:-1, -1]
        coefficients = np.concatenate(
            (-np.linalg.solve(old, cross), np.array([1.0]))
        )
        sigma = float(coefficients @ defect @ coefficients)
        next_prime = next(prime for prime in primes if prime > head)
        row = midpoint_rows(
            ordinates, triangular, [next_prime], dimension
        )[0]
        normalized_response = abs(float(row @ coefficients)) / np.linalg.norm(
            coefficients
        )
        print(
            f"{dimension:2d} {head:4d} {sigma: .9e} "
            f"{np.linalg.eigvalsh(old)[0]: .9e} {next_prime:11d} "
            f"{normalized_response: .9e}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dx", type=float, default=0.001)
    parser.add_argument("--span", type=int, default=24)
    parser.add_argument("--max-k", type=int, default=15)
    parser.add_argument("--svd-tolerance", type=float, default=1.0e-11)
    args = parser.parse_args()
    run(args.dx, args.span, args.max_k, args.svd_tolerance)


if __name__ == "__main__":
    main()
