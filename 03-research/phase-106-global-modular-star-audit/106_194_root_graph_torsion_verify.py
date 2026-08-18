#!/usr/bin/env python3
"""Checks the finite root-graph torsion identity of 106.194."""

from __future__ import annotations

import math

import numpy as np


def laplacian(n: int) -> np.ndarray:
    out = 2.0 * np.eye(n)
    for j in range(n):
        out[j, (j + 1) % n] -= 1.0
        out[j, (j - 1) % n] -= 1.0
    return out


def pseudo_det(a: np.ndarray) -> float:
    eig = np.linalg.eigvalsh(a)
    positive = eig[eig > 1e-10]
    return float(np.prod(positive))


def main() -> None:
    for m, p, k in ((5, 2, 1), (5, 2, 2), (4, 3, 1), (3, 5, 1)):
        n0 = m * p ** (k - 1)
        n1 = m * p**k
        torsion = 0.5 * math.log(pseudo_det(laplacian(n1)) / pseudo_det(laplacian(n0)))

        omega = np.ones(n1) / math.sqrt(n1)
        eta = np.zeros(n1)
        eta[np.arange(m) * p**k] = 1.0 / math.sqrt(m)
        overlap = float(np.dot(omega, eta))

        expected_overlap = p ** (-k / 2)
        expected_product = math.log(p) * expected_overlap
        print(
            f"m={m} p={p} k={k} "
            f"torsion_error={abs(torsion-math.log(p)):.3e} "
            f"overlap_error={abs(overlap-expected_overlap):.3e} "
            f"product_error={abs(torsion*overlap-expected_product):.3e}"
        )


if __name__ == "__main__":
    main()

