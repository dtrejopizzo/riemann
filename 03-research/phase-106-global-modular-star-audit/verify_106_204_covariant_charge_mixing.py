#!/usr/bin/env python3
"""Finite spectral-grid audit of the covariant charge-mixing boundary."""

import math

import numpy as np


def cauchy_weight(gamma: np.ndarray) -> np.ndarray:
    return 1.0 / (2.0 * math.pi * (gamma * gamma + 0.25))


def gamma_multiplier(gamma: np.ndarray) -> np.ndarray:
    times = np.array([0.07, 0.23, 0.61, 1.4, 3.2])
    weights = np.exp(-times / 2.0) / (1.0 - np.exp(-2.0 * times))
    return 1.4 + np.sum(
        4.0
        * weights[:, None]
        * (1.0 - np.cos(times[:, None] * gamma[None, :])),
        axis=0,
    )


def main() -> None:
    rng = np.random.default_rng(106204)
    gamma = np.linspace(-8.0, 8.0, 257)
    common_weight = cauchy_weight(gamma)
    common_metric = np.diag(common_weight)
    common_generator = np.diag(gamma)
    lengths = np.array([math.log(2.0), 2.0 * math.log(2.0), math.log(3.0)])

    unitarity_error = 0.0
    intertwining_error = 0.0
    functional_calculus_error = 0.0
    shifts: list[np.ndarray] = []
    source_metrics: list[np.ndarray] = []
    source_generators: list[np.ndarray] = []
    compliance = np.diag(1.0 / gamma_multiplier(gamma))

    for length in lengths:
        eta = gamma + length
        source_weight = cauchy_weight(eta)
        source_metric = np.diag(source_weight)
        source_generator = np.diag(eta)
        shift = np.diag(np.sqrt(source_weight / common_weight))
        shift_adjoint = (
            np.linalg.inv(source_metric) @ shift.T @ common_metric
        )

        unitarity_error = max(
            unitarity_error,
            np.linalg.norm(shift_adjoint @ shift - np.eye(gamma.size)),
        )
        intertwining_error = max(
            intertwining_error,
            np.linalg.norm(
                shift @ (source_generator - length * np.eye(gamma.size))
                - common_generator @ shift
            ),
        )

        diagonal_pullback = shift_adjoint @ compliance @ shift
        expected_pullback = np.diag(1.0 / gamma_multiplier(eta - length))
        functional_calculus_error = max(
            functional_calculus_error,
            np.linalg.norm(diagonal_pullback - expected_pullback),
        )
        shifts.append(shift)
        source_metrics.append(source_metric)
        source_generators.append(source_generator)

    # Check that the single common-boundary square contains the full cross
    # terms and agrees with its expanded block kernel.
    vectors = [
        rng.normal(size=gamma.size) + 1j * rng.normal(size=gamma.size)
        for _ in lengths
    ]
    alphas = np.array([0.31, 0.19, 0.27])
    boundary_value = sum(
        alpha * shift @ vector
        for alpha, shift, vector in zip(alphas, shifts, vectors)
    )
    joint_energy = np.vdot(boundary_value, common_metric @ compliance @ boundary_value)
    expanded_energy = 0.0j
    off_diagonal_energy = 0.0j
    for i in range(len(lengths)):
        for j in range(len(lengths)):
            term = (
                alphas[i]
                * alphas[j]
                * np.vdot(
                    vectors[i],
                    shifts[i].T
                    @ common_metric
                    @ compliance
                    @ shifts[j]
                    @ vectors[j],
                )
            )
            expanded_energy += term
            if i != j:
                off_diagonal_energy += term
    cross_expansion_error = abs(joint_energy - expanded_energy)

    print("spectral-shift unitarity error:", f"{unitarity_error:.3e}")
    print("charge dephasing intertwiner error:", f"{intertwining_error:.3e}")
    print("shifted Gamma calculus error:", f"{functional_calculus_error:.3e}")
    print("joint Schur cross-expansion error:", f"{cross_expansion_error:.3e}")
    print("off-diagonal coupling magnitude:", f"{abs(off_diagonal_energy):.6e}")


if __name__ == "__main__":
    main()
