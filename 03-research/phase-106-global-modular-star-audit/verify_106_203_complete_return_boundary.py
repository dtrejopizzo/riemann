#!/usr/bin/env python3
"""Finite audit of the complete-return charged Tate boundary in 106.203."""

import math

import numpy as np


def prime_returns(limit: int) -> list[tuple[int, int]]:
    primes = (2, 3, 5, 7, 11, 13)
    rows: list[tuple[int, int]] = []
    for prime in primes:
        power = prime
        exponent = 1
        while power <= limit:
            rows.append((prime, exponent))
            exponent += 1
            power *= prime
    return rows


def main() -> None:
    limit = 40
    coefficient_dim = 4
    rows = prime_returns(limit)
    row_count = len(rows)

    block_dim = 2 * coefficient_dim
    total_dim = row_count * block_dim
    boundary_dim = 2 * coefficient_dim

    metric = np.zeros((total_dim, total_dim))
    complex_structure = np.zeros((total_dim, total_dim))
    boundary = np.zeros((boundary_dim, total_dim))
    generic = np.zeros((total_dim, boundary_dim))

    expected_mass = 0.0
    for row, (prime, exponent) in enumerate(rows):
        log_prime = math.log(prime)
        c_prime = 2.0 * math.pi / log_prime
        alpha = math.sqrt(log_prime / c_prime) * prime ** (-0.5 * exponent)
        expected_mass += log_prime / prime**exponent

        start = row * block_dim
        x_slice = slice(start, start + coefficient_dim)
        y_slice = slice(start + coefficient_dim, start + block_dim)

        metric[x_slice, x_slice] = c_prime * np.eye(coefficient_dim)
        metric[y_slice, y_slice] = (1.0 / c_prime) * np.eye(coefficient_dim)
        complex_structure[x_slice, y_slice] = -(1.0 / c_prime) * np.eye(
            coefficient_dim
        )
        complex_structure[y_slice, x_slice] = c_prime * np.eye(coefficient_dim)

        # Boundary coordinates are (R J v, R v).
        boundary[:coefficient_dim, x_slice] = c_prime * alpha * np.eye(
            coefficient_dim
        )
        boundary[coefficient_dim:, y_slice] = alpha * np.eye(coefficient_dim)

        generic[x_slice, :coefficient_dim] = alpha * np.eye(coefficient_dim)
        generic[y_slice, coefficient_dim:] = c_prime * alpha * np.eye(
            coefficient_dim
        )

    boundary_complex_structure = np.block(
        [
            [np.zeros((coefficient_dim, coefficient_dim)), -np.eye(coefficient_dim)],
            [np.eye(coefficient_dim), np.zeros((coefficient_dim, coefficient_dim))],
        ]
    )

    adjoint_error = np.linalg.norm(generic.T @ metric - boundary)
    gram_error = np.linalg.norm(
        generic.T @ metric @ generic - expected_mass * np.eye(boundary_dim)
    )
    hodge_square_error = np.linalg.norm(
        complex_structure @ complex_structure + np.eye(total_dim)
    )
    hodge_isometry_error = np.linalg.norm(
        complex_structure.T @ metric @ complex_structure - metric
    )
    generic_hodge_error = np.linalg.norm(
        complex_structure @ generic - generic @ boundary_complex_structure
    )
    boundary_hodge_error = np.linalg.norm(
        boundary @ complex_structure
        - boundary_complex_structure @ boundary
    )

    # Audit the charged Gamma Schur metric on a diagonal spectral sample.
    frequencies = np.array([-2.3, -0.4, 0.7, 2.8])
    gamma_times = np.array([0.11, 0.37, 1.1, 2.4])
    gamma_weights = np.exp(-gamma_times / 2.0) / (
        1.0 - np.exp(-2.0 * gamma_times)
    )
    kappa = 1.3
    compliance_values = []
    for prime, exponent in rows:
        charge = exponent * math.log(prime)
        multiplier = kappa + np.sum(
            4.0
            * gamma_weights[:, None]
            * (
                1.0
                - np.cos(
                    gamma_times[:, None]
                    * (frequencies[None, :] - charge)
                )
            ),
            axis=0,
        )
        compliance_values.append(multiplier)
    compliance = np.asarray(compliance_values)
    positivity_margin = float(np.min(compliance))

    print("complete-return adjoint error:", f"{adjoint_error:.3e}")
    print("complete-return Gram error:", f"{gram_error:.3e}")
    print("Tate Hodge square error:", f"{hodge_square_error:.3e}")
    print("Tate Hodge isometry error:", f"{hodge_isometry_error:.3e}")
    print("generic-plane Hodge error:", f"{generic_hodge_error:.3e}")
    print("boundary Hodge error:", f"{boundary_hodge_error:.3e}")
    print("charged compliance minimum:", f"{positivity_margin:.6e}")


if __name__ == "__main__":
    main()
