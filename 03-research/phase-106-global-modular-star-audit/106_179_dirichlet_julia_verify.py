#!/usr/bin/env python3
"""Float64 verification of the identities in 106.179.

This checks a noncommuting finite return family. It is a diagnostic for
the exact functional-calculus identities, not a positivity certificate
for the global CCM form.
"""

from __future__ import annotations

import numpy as np


def hermitian_function(matrix: np.ndarray, function) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * function(values)) @ vectors.conj().T


def main() -> None:
    rng = np.random.default_rng(106179)
    dimension = 7

    returns = []
    weights = []
    for weight in (0.7, 1.1, 0.4, 0.9):
        z = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
            size=(dimension, dimension)
        )
        q, r = np.linalg.qr(z)
        phases = np.diag(r).copy()
        phases /= np.abs(phases)
        unitary = q @ np.diag(np.conj(phases))
        returns.extend((unitary, unitary.conj().T))
        weights.extend((weight, weight))

    c_value = float(sum(weights))
    a_value = sum(weight * unitary for weight, unitary in zip(weights, returns))
    t_value = a_value / c_value
    t_value = 0.5 * (t_value + t_value.conj().T)
    defect = hermitian_function(
        t_value, lambda x: np.sqrt(np.maximum(0.0, 1.0 - x * x))
    )
    defect_inverse = hermitian_function(
        t_value,
        lambda x: 1.0 / np.sqrt(np.maximum(1.0e-30, 1.0 - x * x)),
    )

    julia = np.block([[t_value, defect], [defect, -t_value]])
    k_minus = -(np.eye(dimension) + t_value) @ defect_inverse
    embedding = np.vstack((np.eye(dimension), k_minus))

    q_scalar = 0.5 * c_value * (np.eye(dimension) - t_value) @ (
        np.eye(dimension) - t_value
    )
    q_weight = np.block(
        [[q_scalar, np.zeros_like(q_scalar)], [np.zeros_like(q_scalar), q_scalar]]
    )

    graph_error = np.linalg.norm(julia @ embedding + embedding, ord="fro")
    pulled = embedding.conj().T @ q_weight @ embedding
    energy = c_value * (np.eye(dimension) - t_value)
    metric_error = np.linalg.norm(pulled - energy, ord="fro")

    shell_energy = sum(
        0.5
        * weight
        * (np.eye(dimension) - unitary).conj().T
        @ (np.eye(dimension) - unitary)
        for weight, unitary in zip(weights, returns)
    )
    shell_error = np.linalg.norm(shell_energy - energy, ord="fro")

    print(f"negative-graph invariance error : {graph_error:.3e}")
    print(f"Dirichlet pullback error       : {metric_error:.3e}")
    print(f"return-shell assembly error    : {shell_error:.3e}")

    if max(graph_error, metric_error, shell_error) > 2.0e-11:
        raise SystemExit("FAIL: a 106.179 identity exceeded tolerance")
    print("PASS: weighted Julia graph equals the full return Dirichlet metric.")


if __name__ == "__main__":
    main()
