#!/usr/bin/env python3
"""Two-cell periodic boundary graph counterexample for D.197."""

from __future__ import annotations

import numpy as np


def project_off(weight: np.ndarray, seed: np.ndarray) -> np.ndarray:
    return seed - weight * (np.vdot(weight, seed) / np.vdot(weight, weight))


def main() -> None:
    r = 0.39
    m = 80
    u = np.linspace(0.0, 1.7, m, endpoint=False)
    w_plus = np.exp(u / 2)
    w_minus = np.exp(-u / 2)

    g_plus = project_off(w_plus, np.sin(3.1 * u) + 0.2 * np.cos(7.0 * u))
    g_minus = project_off(w_minus, np.cos(4.3 * u) - 0.1 * np.sin(8.0 * u))
    assert abs(np.vdot(w_plus, g_plus)) < 1e-11
    assert abs(np.vdot(w_minus, g_minus)) < 1e-11

    denom = 1.0 / r - r
    f1 = (g_plus - g_minus) / denom
    f0 = ((1.0 / r) * g_minus - r * g_plus) / denom
    recovered_plus = f0 + (1.0 / r) * f1
    recovered_minus = f0 + r * f1
    assert np.linalg.norm(recovered_plus - g_plus) < 1e-12
    assert np.linalg.norm(recovered_minus - g_minus) < 1e-12

    # Coordinate-axis primitive images give both signs.
    f1_pos = g_plus / denom
    f0_pos = -r * g_plus / denom
    bplus_pos = f0_pos + (1.0 / r) * f1_pos
    bminus_pos = f0_pos + r * f1_pos
    assert np.linalg.norm(bplus_pos - g_plus) < 1e-12
    assert np.linalg.norm(bminus_pos) < 1e-12
    q_pos = r * np.vdot(bplus_pos, bplus_pos).real

    f1_neg = -g_minus / denom
    f0_neg = (1.0 / r) * g_minus / denom
    bplus_neg = f0_neg + (1.0 / r) * f1_neg
    bminus_neg = f0_neg + r * f1_neg
    assert np.linalg.norm(bplus_neg) < 1e-12
    assert np.linalg.norm(bminus_neg - g_minus) < 1e-12
    q_neg = -(1.0 / r) * np.vdot(bminus_neg, bminus_neg).real
    assert q_pos > 0 > q_neg

    trace_matrix = np.array([[1.0, 1.0 / r], [1.0, r]])
    assert abs(np.linalg.det(trace_matrix)) > 1e-3

    print("D197 periodic boundary graph audit: PASS")
    print(f"trace determinant       = {np.linalg.det(trace_matrix):.12f}")
    print(f"primitive positive axis = {q_pos:.6e}")
    print(f"primitive negative axis = {q_neg:.6e}")
    print(f"joint reconstruction    = {np.linalg.norm(recovered_plus-g_plus)+np.linalg.norm(recovered_minus-g_minus):.3e}")


if __name__ == "__main__":
    main()
