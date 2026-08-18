#!/usr/bin/env python3
"""Check the exact Q2 dispersion identities and the rational countergate.

This script is an algebraic regression check.  Floating-point random rows
are diagnostic only; the three-point countergate is evaluated with exact
fractions.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np


def moments(nodes: np.ndarray, weights: np.ndarray) -> np.ndarray:
    return np.array(
        [np.sum(weights * nodes**power) for power in range(4)],
        dtype=float,
    )


def check_random_rows() -> None:
    rng = np.random.default_rng(10697)
    for size in range(2, 9):
        for _ in range(50):
            nodes = np.sort(4.0 * rng.random(size))
            weights = rng.random(size)
            m0, m1, m2, m3 = moments(nodes, weights)
            dispersion = m0 * m2 - m1 * m1
            cost = (m0 + m1) * (m2 + m3) - (m1 + m2) ** 2

            pair_dispersion = 0.0
            pair_cost = 0.0
            for i in range(size):
                for j in range(size):
                    term = 0.5 * weights[i] * weights[j] * (
                        nodes[i] - nodes[j]
                    ) ** 2
                    pair_dispersion += term
                    pair_cost += term * (1.0 + nodes[i]) * (
                        1.0 + nodes[j]
                    )

            scale = max(1.0, abs(cost), abs(dispersion))
            if abs(pair_dispersion - dispersion) > 2.0e-13 * scale:
                raise RuntimeError("dispersion pair identity failed")
            if abs(pair_cost - cost) > 2.0e-13 * scale:
                raise RuntimeError("adaptive-cost pair identity failed")

            q1 = m0 * m0 / (m0 + m1)
            q2 = q1 + dispersion**2 / ((m0 + m1) * cost)
            hankel = np.array(
                [[m0 + m1, m1 + m2], [m1 + m2, m2 + m3]]
            )
            response = np.array([m0, m1])
            direct = float(response @ np.linalg.solve(hankel, response))
            if abs(q2 - direct) > 2.0e-12 * max(1.0, abs(q2)):
                raise RuntimeError("Q2 formula failed")


def check_exact_countergate() -> None:
    m0, m1, m2, m3 = [Fraction(value, 13) for value in (36, 72, 168, 432)]
    delta = Fraction(649, 650)
    q1 = m0 * m0 / (m0 + m1)
    dispersion = m0 * m2 - m1 * m1
    cost = (m0 + m1) * (m2 + m3) - (m1 + m2) ** 2
    q2 = q1 + dispersion**2 / ((m0 + m1) * cost)
    exact_gain = Fraction(1, 1)
    lhs = dispersion**2
    rhs = (delta - q1) * (m0 + m1) * cost

    assert q1 == Fraction(12, 13)
    assert q2 == Fraction(324, 325)
    assert q2 < delta < exact_gain
    assert lhs == Fraction(746496, 28561)
    assert rhs == Fraction(762048, 28561)
    assert lhs < rhs

    print("exact countergate")
    print(f"  Q1={q1}")
    print(f"  Q2={q2} < delta={delta} < G={exact_gain}")
    print(f"  boxed sides: {lhs} < {rhs}")


def main() -> None:
    check_random_rows()
    print("random spectral pair identities: PASS")
    check_exact_countergate()


if __name__ == "__main__":
    main()
