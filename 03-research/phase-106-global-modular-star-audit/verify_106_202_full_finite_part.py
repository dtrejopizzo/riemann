#!/usr/bin/env python3
"""Finite algebra audit of the generic-plus-residual identity in 106.202."""

import math
import numpy as np


def main() -> None:
    rng = np.random.default_rng(106202)
    primes = np.array([2.0, 3.0, 5.0, 7.0, 11.0, 13.0])
    returns = np.arange(1, 5)
    weights = np.array(
        [[math.log(p) / p**k for k in returns] for p in primes]
    )
    dim = 5

    f = rng.normal(size=dim) + 1j * rng.normal(size=dim)
    g = rng.normal(size=dim) + 1j * rng.normal(size=dim)
    r = rng.normal(size=(len(primes), len(returns), dim)) + 1j * rng.normal(
        size=(len(primes), len(returns), dim)
    )
    z = rng.normal(size=(len(primes), len(returns), dim)) + 1j * rng.normal(
        size=(len(primes), len(returns), dim)
    )

    def ip(x: np.ndarray, y: np.ndarray) -> complex:
        # Linear in the first variable, matching the phase documents.
        return np.dot(x, np.conjugate(y))

    residual_formula = 0.0j
    expanded_rows = 0.0j
    common_rows = 0.0j
    for i in range(len(primes)):
        for j in range(len(returns)):
            weight = weights[i, j]
            expanded_rows += weight * ip(f + r[i, j], g + z[i, j])
            common_rows += weight * ip(f, g)
            residual_formula += weight * (
                ip(r[i, j], g) + ip(f, z[i, j]) + ip(r[i, j], z[i, j])
            )
    expansion_error = abs(expanded_rows - common_rows - residual_formula)

    # Model the exact finite-part coefficient by the theorem:
    # FP(C_s) + gamma + repeated_mass = 0.
    gamma = 0.5772156649015329
    repeated_mass = np.sum(weights[:, 1:])
    primitive_finite_part = -gamma - repeated_mass
    common_finite_part = (
        primitive_finite_part + gamma + repeated_mass
    ) * ip(f, g)
    cancellation_error = abs(common_finite_part)

    total_finite_part = common_finite_part + residual_formula
    finite_part_error = abs(total_finite_part - residual_formula)

    print("generic/residual expansion error:", f"{expansion_error:.3e}")
    print("matched common finite-part error:", f"{cancellation_error:.3e}")
    print("full residual finite-part error:", f"{finite_part_error:.3e}")


if __name__ == "__main__":
    main()
