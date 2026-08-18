#!/usr/bin/env python3
"""Diagnostics for the folded signed-measure coordinate of 106.65.

This script is not an interval certificate.  It computes the canonical
Hadamard finite-part primitives

    S1(U) = FP sigma((0,U]),
    S2(U) = integral_0^U S1(v) dv,

and the displacement profile J_u of an exact four-zero complement vector.
Only NumPy is required.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve()
REPO = HERE.parents[3]
ZEROS = REPO / "06-grafico" / "zeros_10000.txt"


def prime_power_atoms(limit: int) -> tuple[np.ndarray, np.ndarray]:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False

    atoms: list[tuple[float, float]] = []
    for p0 in np.flatnonzero(sieve):
        p = int(p0)
        logp = math.log(p)
        value = p
        while value <= limit:
            atoms.append((math.log(value), logp / math.sqrt(value)))
            if value > limit // p:
                break
            value *= p
    atoms.sort()
    return (
        np.array([item[0] for item in atoms]),
        np.array([item[1] for item in atoms]),
    )


def gamma_fp_primitive_one(u: np.ndarray) -> np.ndarray:
    y = np.exp(-u / 2.0)
    return (
        -0.5 * np.log((1.0 + y) / (1.0 - y))
        - np.arctan(y)
        + math.log(2.0)
        + math.pi / 4.0
    )


def cumulative_trapezoid(values: np.ndarray, grid: np.ndarray) -> np.ndarray:
    result = np.empty_like(values)
    # G_1(u) = (1/2) log u + O(u) at the origin.
    eps = grid[0]
    result[0] = 0.5 * eps * (math.log(eps) - 1.0)
    increments = 0.5 * (values[1:] + values[:-1]) * np.diff(grid)
    result[1:] = result[0] + np.cumsum(increments)
    return result


def signed_primitives(
    grid: np.ndarray, atom_u: np.ndarray, atom_weight: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    cumulative = np.cumsum(atom_weight)
    cumulative_u = np.cumsum(atom_weight * atom_u)
    indices = np.searchsorted(atom_u, grid, side="right")
    p1 = np.zeros_like(grid)
    pu = np.zeros_like(grid)
    active = indices > 0
    p1[active] = cumulative[indices[active] - 1]
    pu[active] = cumulative_u[indices[active] - 1]
    p2 = grid * p1 - pu

    g1 = gamma_fp_primitive_one(grid)
    g2 = cumulative_trapezoid(g1, grid)
    s1 = p1 + g1 - 4.0 * np.sinh(grid / 2.0)
    s2 = p2 + g2 - 8.0 * (np.cosh(grid / 2.0) - 1.0)
    return s1, s2


def riemann_kernel(x: np.ndarray) -> np.ndarray:
    xa = np.abs(x)
    out = np.zeros_like(xa)
    active = xa < 3.0
    y = xa[active]
    e2y = np.exp(2.0 * y)
    for m in range(1, 30):
        out[active] += (
            math.pi
            * m
            * m
            * np.exp(2.5 * y)
            * (2.0 * math.pi * m * m * e2y - 3.0)
            * np.exp(-math.pi * m * m * e2y)
        )
    out *= 0.5 / np.trapz(np.cosh(x / 2.0) * out, x)
    return out


def displacement_profile(
    x: np.ndarray, k: np.ndarray, q: np.ndarray, u_grid: np.ndarray
) -> np.ndarray:
    result = np.empty_like(u_grid)
    for index, u in enumerate(u_grid):
        shifted_k = np.interp(x - u, x, k, left=0.0, right=0.0)
        shifted_q = np.interp(x - u, x, q, left=0.0, right=0.0)
        result[index] = np.trapz(
            k * shifted_k * (q - shifted_q) ** 2, x
        )
    return result


def run(limit: int, points: int, dx: float, du: float) -> None:
    maximum_u = math.log(limit)
    atom_u, atom_weight = prime_power_atoms(limit)
    primitive_grid = np.linspace(1.0e-5, maximum_u, points)
    s1, s2 = signed_primitives(primitive_grid, atom_u, atom_weight)

    print(f"prime-power cutoff={limit}; U_max={maximum_u:.9f}")
    print(
        "S1 canonical FP min/max:",
        f"{s1.min():.9f} at {primitive_grid[s1.argmin()]:.6f};",
        f"{s1.max():.9f} at {primitive_grid[s1.argmax()]:.6f}",
    )
    print(
        "S2 canonical FP min/max:",
        f"{s2.min():.9f} at {primitive_grid[s2.argmin()]:.6f};",
        f"{s2.max():.9f} at {primitive_grid[s2.argmax()]:.6f}",
    )

    x = np.arange(-3.2, 3.2 + dx / 2.0, dx)
    k = riemann_kernel(x)
    h = np.cosh(x / 2.0)
    ordinates = np.loadtxt(ZEROS)[:4]
    coefficients = np.array([1.0, -2.0, 2.0, -1.0])
    q = coefficients @ (np.cos(ordinates[:, None] * x) / h)
    u_grid = np.arange(0.0, 6.4 + du / 2.0, du)
    j = displacement_profile(x, k, q, u_grid)
    j1 = np.gradient(j, du)
    j2 = np.gradient(j1, du)
    tolerance_one = 1.0e-5 * max(1.0, np.max(np.abs(j1)))
    tolerance_two = 1.0e-5 * max(1.0, np.max(np.abs(j2)))
    print(
        "J profile:",
        f"max={j.max():.9e} at u={u_grid[j.argmax()]:.6f};",
        f"J(0)={j[0]:.3e}; J(end)={j[-1]:.3e}",
    )
    print(
        "derivative sign counts:",
        f"J'>0 {np.count_nonzero(j1 > tolerance_one)},",
        f"J'<0 {np.count_nonzero(j1 < -tolerance_one)},",
        f"J''>0 {np.count_nonzero(j2 > tolerance_two)},",
        f"J''<0 {np.count_nonzero(j2 < -tolerance_two)}",
    )

    positive_u = u_grid[1:]
    gamma_density = np.exp(-positive_u / 2.0) / (
        -np.expm1(-2.0 * positive_u)
    )
    continuous = np.trapz(
        j[1:] * (gamma_density - 2.0 * np.cosh(positive_u / 2.0)),
        positive_u,
    )
    retained = atom_u <= u_grid[-1]
    atomic = float(
        np.sum(
            atom_weight[retained]
            * np.interp(atom_u[retained], u_grid, j)
        )
    )
    print(
        "direct defect pieces:",
        f"continuous={continuous:.12f};",
        f"atomic={atomic:.12f};",
        f"total={continuous + atomic:.12f}",
    )

    s1_on_u = np.interp(positive_u, primitive_grid, s1)
    s2_on_u = np.interp(positive_u, primitive_grid, s2)
    first_rising = np.trapz(
        np.where(j1[1:] > 0.0, -j1[1:] * s1_on_u, 0.0), positive_u
    )
    first_falling = np.trapz(
        np.where(j1[1:] < 0.0, -j1[1:] * s1_on_u, 0.0), positive_u
    )
    second_positive = np.trapz(
        np.where(j2[1:] > 0.0, j2[1:] * s2_on_u, 0.0), positive_u
    )
    second_negative = np.trapz(
        np.where(j2[1:] < 0.0, j2[1:] * s2_on_u, 0.0), positive_u
    )
    print(
        "first-primitive slope split:",
        f"rising={first_rising:.12f}; falling={first_falling:.12f};",
        f"sum={first_rising + first_falling:.12f}",
    )
    print(
        "second-primitive curvature split:",
        f"J''>0={second_positive:.12f}; J''<0={second_negative:.12f};",
        f"sum={second_positive + second_negative:.12f}",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=2_000_000)
    parser.add_argument("--points", type=int, default=40000)
    parser.add_argument("--dx", type=float, default=0.001)
    parser.add_argument("--du", type=float, default=0.002)
    args = parser.parse_args()
    run(args.limit, args.points, args.dx, args.du)


if __name__ == "__main__":
    main()
