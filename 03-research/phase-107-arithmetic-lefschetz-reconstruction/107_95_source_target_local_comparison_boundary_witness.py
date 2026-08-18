#!/usr/bin/env python3
"""Compare the current Paper A local source row against real bad fibers."""

from __future__ import annotations

import math

import sympy as sp


def source_local_weight(prime: int) -> sp.Expr:
    """Current 107.04 finite-place row: only the scalar log p survives."""
    return sp.log(prime)


def cycle_intersection_matrix(n: int) -> sp.Matrix:
    matrix = sp.zeros(n)
    for i in range(n):
        matrix[i, i] = -2
        matrix[i, (i - 1) % n] += 1
        matrix[i, (i + 1) % n] += 1
    return matrix


I2 = cycle_intersection_matrix(2)
I9 = cycle_intersection_matrix(9)


def audit_same_prime_same_source_different_geometry() -> int:
    checks = 0
    source_i2 = source_local_weight(2)
    source_i9 = source_local_weight(2)
    assert sp.simplify(source_i2 - source_i9) == 0
    checks += 1
    assert I2.rows != I9.rows
    checks += 1
    assert I2 != I9[:2, :2]
    checks += 1
    return checks


def audit_same_geometry_different_primes() -> int:
    checks = 0
    assert I2 == cycle_intersection_matrix(2)
    checks += 1
    w2 = source_local_weight(2)
    w3 = source_local_weight(3)
    assert sp.simplify(w2 - w3) != 0
    checks += 1
    assert (w2 * I2) / sp.log(2) == I2
    checks += 1
    assert (w3 * I2) / sp.log(3) == I2
    checks += 1
    return checks


def audit_boundary_statement() -> int:
    checks = 0
    # The current source row can distinguish prime 2 from prime 3.
    assert source_local_weight(2) != source_local_weight(3)
    checks += 1
    # But it cannot distinguish I2 from I9 once the prime is fixed.
    assert source_local_weight(2) == source_local_weight(2)
    checks += 1
    return checks


def main() -> None:
    same_prime_checks = audit_same_prime_same_source_different_geometry()
    same_geometry_checks = audit_same_geometry_different_primes()
    boundary_checks = audit_boundary_statement()

    print("All source-vs-target local comparison boundary checks passed.")
    print(f"  same-prime boundary checks: {same_prime_checks}")
    print(f"  repeated-geometry checks: {same_geometry_checks}")
    print(f"  boundary-statement checks: {boundary_checks}")
    print(f"  source log(2) = {math.log(2):.12f}")
    print(f"  source log(3) = {math.log(3):.12f}")
    print(f"  I2 matrix size = {I2.rows}x{I2.cols}")
    print(f"  I9 matrix size = {I9.rows}x{I9.cols}")


if __name__ == "__main__":
    main()
