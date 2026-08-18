#!/usr/bin/env python3
"""Finite spectral audit of the operator-valued pushout in 106.198."""

import numpy as np


def main():
    rng = np.random.default_rng(106198)
    dim = 8
    kappa = 1.3

    # A finite Gamma gradient with several real translation times.
    frequencies = np.linspace(-3.0, 4.0, dim)
    times = np.array([0.12, 0.37, 0.9, 1.8, 3.2])
    weights = np.exp(-times / 2.0) / (1.0 - np.exp(-2.0 * times))
    rows = []
    for time, weight in zip(times, weights):
        rows.append(np.sqrt(2.0 * weight) * np.diag(1.0 - np.exp(1j * time * frequencies)))
    gamma_gradient = np.vstack(rows)

    # The scalar finite-part row is sqrt(kappa) I.
    full_boundary = np.vstack([np.sqrt(kappa) * np.eye(dim), gamma_gradient])
    k_gamma = full_boundary.conj().T @ full_boundary
    expected_multiplier = kappa + np.sum(
        4.0 * weights[:, None] * (1.0 - np.cos(times[:, None] * frequencies[None, :])),
        axis=0,
    )
    multiplier_error = np.linalg.norm(k_gamma - np.diag(expected_multiplier))

    inverse = np.linalg.inv(k_gamma)
    right_inverse = full_boundary @ inverse
    right_inverse_error = np.linalg.norm(full_boundary.conj().T @ right_inverse - np.eye(dim))

    boundary = rng.normal(size=(dim, 4)) + 1j * rng.normal(size=(dim, 4))
    lift = -right_inverse @ boundary
    lift_energy = lift.conj().T @ lift
    schur_energy = boundary.conj().T @ inverse @ boundary
    schur_error = np.linalg.norm(lift_energy - schur_energy)

    print("Gamma multiplier error:", f"{multiplier_error:.3e}")
    print("minimum right-inverse error:", f"{right_inverse_error:.3e}")
    print("operator Schur-metric error:", f"{schur_error:.3e}")


if __name__ == "__main__":
    main()
