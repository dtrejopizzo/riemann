#!/usr/bin/env python3
"""Finite-fiber audit of the charged multiplier/rank dichotomy in 106.205."""

import math

import numpy as np


def gamma_symbol(gamma: np.ndarray) -> np.ndarray:
    times = np.array([0.09, 0.31, 0.83, 1.9, 4.0])
    weights = np.exp(-times / 2.0) / (1.0 - np.exp(-2.0 * times))
    return np.sum(
        4.0
        * weights[:, None]
        * (1.0 - np.cos(times[:, None] * gamma[None, :])),
        axis=0,
    )


def main() -> None:
    gamma = np.linspace(-30.0, 30.0, 4001)
    charges = np.log(np.array([1.0, 2.0, 3.0, 4.0, 5.0, 7.0]))
    kappa = 1.17
    charged = np.vstack([kappa + gamma_symbol(gamma - charge) for charge in charges])

    minimum = float(np.min(charged))
    inverse_bound_error = max(0.0, float(np.max(1.0 / charged) - 1.0 / kappa))

    # A common co-diagonal has exactly one structural direction at every
    # frequency.  Its orthogonal complement has rank q-1 independently of
    # the Gamma values.
    weights = np.array([0.41, 0.27, 0.19, 0.13, 0.09, 0.07])
    vector = np.sqrt(weights / np.sum(weights))
    projection = np.eye(charges.size) - np.outer(vector, vector)
    projection_idempotence_error = np.linalg.norm(projection @ projection - projection)
    projection_eigenvalues = np.linalg.eigvalsh(projection)
    transverse_rank = int(np.sum(projection_eigenvalues > 1.0e-10))

    # The positive charged compliance followed by the transverse quotient
    # has one zero singular value for structural reasons and no additional
    # near-zero singular value caused by the Gamma block.
    sample_indices = np.linspace(0, gamma.size - 1, 31, dtype=int)
    second_singular_floor = float("inf")
    zero_singular_ceiling = 0.0
    for index in sample_indices:
        square_root = np.diag(np.sqrt(charged[:, index]))
        singular_values = np.linalg.svd(projection @ square_root, compute_uv=False)
        singular_values.sort()
        zero_singular_ceiling = max(zero_singular_ceiling, singular_values[0])
        second_singular_floor = min(second_singular_floor, singular_values[1])

    print("charged compliance minimum:", f"{minimum:.6e}")
    print("uniform inverse-bound excess:", f"{inverse_bound_error:.3e}")
    print("co-diagonal projection error:", f"{projection_idempotence_error:.3e}")
    print("structural transverse rank:", transverse_rank)
    print("structural zero singular ceiling:", f"{zero_singular_ceiling:.3e}")
    print("nonzero transverse singular floor:", f"{second_singular_floor:.6e}")


if __name__ == "__main__":
    main()
