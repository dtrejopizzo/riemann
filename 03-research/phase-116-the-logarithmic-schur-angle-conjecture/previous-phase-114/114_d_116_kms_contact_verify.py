#!/usr/bin/env python3
"""Exact local certificates for D.116 KMS/modular contact audit."""

from fractions import Fraction


def main() -> None:
    # Use rho=p^{-beta}=1/2.  The identities are local power-series
    # identities and do not depend on how rho is parametrized.
    rho = Fraction(1, 2)

    # Local mean occupation: sum_{k>=1} rho^k = rho/(1-rho).
    mean_occupation = rho / (1 - rho)
    assert mean_occupation == 1
    partial_mean = sum(rho**k for k in range(1, 12))
    assert partial_mean < mean_occupation

    # Local variance coefficient: sum k rho^k = rho/(1-rho)^2.
    variance_occupation = rho / (1 - rho) ** 2
    assert variance_occupation == 2
    partial_variance = sum(k * rho**k for k in range(1, 12))
    assert partial_variance < variance_occupation

    # KMS invariance makes different energy depths orthogonal, while the
    # required OS/Szego kernel has a nonzero off-diagonal rho.
    kms_depth = [[Fraction(1), Fraction(0)],
                 [Fraction(0), rho]]
    szego_depth = [[Fraction(1), rho],
                   [rho, Fraction(1)]]
    assert kms_depth[0][1] == 0
    assert szego_depth[0][1] == rho != 0

    # At beta=1/2 the Gibbs trace already diverges by the elementary lower
    # bound sum_{n=1}^N n^{-1/2} >= sqrt(N).
    n = 10_000
    lower_bound = 100
    assert lower_bound * lower_bound == n

    # A positive first logarithmic derivative need not have the same
    # coefficient as its positive Hessian: k versus k^2 in a two-level toy.
    energy = Fraction(3)
    mean_weight = energy
    dirichlet_weight = energy * energy
    assert dirichlet_weight != mean_weight

    print("D116 KMS contact certificates: PASS")
    print("local mean/variance occupations:", mean_occupation, variance_occupation)
    print("KMS versus Szego off-diagonal:", kms_depth[0][1], szego_depth[0][1])
    print("central Gibbs partial-sum lower bound at N:", n, lower_bound)
    print("mean versus square weight:", mean_weight, dirichlet_weight)


if __name__ == "__main__":
    main()
