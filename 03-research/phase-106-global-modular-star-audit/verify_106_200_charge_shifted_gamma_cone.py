#!/usr/bin/env python3
"""Finite audit of the charged Gamma connection and cone quotient."""

import numpy as np


def main() -> None:
    rng = np.random.default_rng(106200)
    frequencies = np.array([-2.7, -0.9, 0.2, 1.8, 4.1])
    charges = np.log(np.array([1.0, 2.0, 3.0, 5.0]))
    gamma_times = np.array([0.08, 0.24, 0.7, 1.6, 3.5])
    gamma_weights = np.exp(-gamma_times / 2.0) / (
        1.0 - np.exp(-2.0 * gamma_times)
    )
    kappa = 1.25

    total_energy = (
        frequencies[None, :] - charges[:, None]
    ).reshape(-1)
    rows = []
    for time, weight in zip(gamma_times, gamma_weights):
        rows.append(
            np.sqrt(2.0 * weight)
            * np.diag(1.0 - np.exp(1j * time * total_energy))
        )
    gamma_gradient = np.vstack(rows)
    full_boundary = np.vstack(
        [np.sqrt(kappa) * np.eye(total_energy.size), gamma_gradient]
    )
    compliance = full_boundary.conj().T @ full_boundary
    expected = kappa + np.sum(
        4.0
        * gamma_weights[:, None]
        * (1.0 - np.cos(gamma_times[:, None] * total_energy[None, :])),
        axis=0,
    )
    multiplier_error = np.linalg.norm(compliance - np.diag(expected))

    inverse = np.linalg.inv(compliance)
    right_inverse = full_boundary @ inverse
    right_inverse_error = np.linalg.norm(
        full_boundary.conj().T @ right_inverse - np.eye(total_energy.size)
    )

    boundary = rng.normal(size=(total_energy.size, 3)) + 1j * rng.normal(
        size=(total_energy.size, 3)
    )
    lift = right_inverse @ boundary
    schur_error = np.linalg.norm(
        lift.conj().T @ lift - boundary.conj().T @ inverse @ boundary
    )

    # Finite co-diagonal quotient: P d = 0 is the cone-map identity.
    domain_dim = 5
    target_dim = 17
    co_diagonal = rng.normal(size=(target_dim, domain_dim)) + 1j * rng.normal(
        size=(target_dim, domain_dim)
    )
    gram_inverse = np.linalg.inv(co_diagonal.conj().T @ co_diagonal)
    quotient_projection = (
        np.eye(target_dim)
        - co_diagonal @ gram_inverse @ co_diagonal.conj().T
    )
    cone_annihilation_error = np.linalg.norm(
        quotient_projection @ co_diagonal
    )

    defect = rng.normal(size=target_dim) + 1j * rng.normal(size=target_dim)
    defect_class_norm = np.linalg.norm(quotient_projection @ defect)

    print("charge-shifted multiplier error:", f"{multiplier_error:.3e}")
    print("charged right-inverse error:", f"{right_inverse_error:.3e}")
    print("charged Schur-metric error:", f"{schur_error:.3e}")
    print("co-diagonal cone annihilation error:", f"{cone_annihilation_error:.3e}")
    print("generic defect class norm:", f"{defect_class_norm:.6e}")


if __name__ == "__main__":
    main()
