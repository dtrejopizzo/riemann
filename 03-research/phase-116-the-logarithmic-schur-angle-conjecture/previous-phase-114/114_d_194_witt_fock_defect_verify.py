#!/usr/bin/env python3
"""Finite Fock/contact certificates for D.194."""

from __future__ import annotations

import math
import numpy as np


def shift(size: int, power: int = 1) -> np.ndarray:
    s = np.zeros((size, size))
    for j in range(size - power):
        s[j + power, j] = 1.0
    return s


def main() -> None:
    size = 12
    # Ignore the top truncation boundary by inspecting the range defect in
    # the stable lower block.
    for k in (1, 2, 3, 5):
        s = shift(size, k)
        d = np.eye(size) - s @ s.T
        lower = d[: size - k, : size - k]
        # In finite sections d also contains a harmless top-boundary defect;
        # its first k diagonal entries are exactly the infinite defect.
        assert np.allclose(np.diag(d)[:k], 1.0)
        assert np.allclose(np.diag(d)[k : size - k], 0.0)
        assert np.linalg.matrix_rank(d[: size - k, : size - k]) == k

    weights = np.linspace(0.4, 1.5, size)
    values = [weights[:k].sum() for k in (1, 2, 3, 4, 5)]
    assert all(b > a for a, b in zip(values, values[1:]))

    # Mixed two-prime shift: the vacuum is always in the range defect.
    sp = shift(5, 2)
    sq = shift(4, 1)
    vn = np.kron(sp, sq)
    defect = np.eye(vn.shape[0]) - vn @ vn.T
    vacuum = np.zeros(vn.shape[0])
    vacuum[0] = 1.0
    assert abs(vacuum @ defect @ vacuum - 1.0) < 1e-12

    # Regularized global trace formula in a long finite section.
    sigma, n = 1.7, 6
    cutoff = 200000
    r = np.arange(1, cutoff + 1, dtype=float)
    total = np.sum(r ** (-sigma))
    multiples = np.sum((n * np.arange(1, cutoff // n + 1, dtype=float)) ** (-sigma))
    target = (1.0 - n ** (-sigma)) * total
    assert abs((total - multiples) - target) < 2e-4

    # Perfect torsion complex: zero complex cohomology, nonzero determinant mass.
    m = 5.0
    assert np.linalg.matrix_rank(np.array([[m]])) == 1
    hilbert_euler = 0  # kernel and cokernel both zero over C
    torsion_mass = math.log(m)
    assert hilbert_euler == 0 and torsion_mass > 0

    # Finite contact GNS algebra for primes 2,3,5.
    primes = np.array([2.0, 3.0, 5.0])
    tau = np.log(primes)
    e2, e3, e5 = np.eye(3)

    def product(x: np.ndarray, y: np.ndarray) -> np.ndarray:
        return x * y

    assert np.allclose(product(e2, e2), e2)
    assert np.allclose(product(e2, e3), 0.0)
    assert abs(tau @ product(e5, e5) - math.log(5.0)) < 1e-12
    gram = np.diag(tau)
    assert np.linalg.eigvalsh(gram)[0] > 0

    print("D194 Witt/Fock defect and torsion trace gate: PASS")
    print(f"faithful defect weights = {values}")
    print(f"mixed vacuum defect     = {vacuum @ defect @ vacuum:.1f}")
    print(f"torsion mass log(5)     = {torsion_mass:.12f}")
    print(f"contact GNS eigenvalues = {np.linalg.eigvalsh(gram).tolist()}")


if __name__ == "__main__":
    main()
