#!/usr/bin/env python3
"""Diagnostic for the sharp physical and compensated sufficient gates.

This is a floating-point diagnostic, not an interval certificate.  It
evaluates the literal displacement forms on

    q_gamma(x) = cos(gamma*x) / cosh(x/2)

using a common spatial grid and the literal von Mangoldt atoms.  The
quantities printed are

    P_PNT  = sum Lambda(n)/sqrt(n) J_log(n) - int exp(u/2) J_u du,
    b_Gamma = int r_Gamma(u) J_u du,
    b_K     = int K(u) J_u du,

and the original and two sufficient gates discussed in 106.135 and
106.138.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


THETA = 499.0 / 2000.0
GAMMA1 = 14.134725141734693790


def von_mangoldt_atoms(limit: int) -> list[tuple[int, float]]:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    atoms: list[tuple[int, float]] = []
    for p in np.flatnonzero(sieve):
        value = int(p)
        while value <= limit:
            atoms.append((value, math.log(int(p))))
            value *= int(p)
    atoms.sort()
    return atoms


def riemann_kernel(x: np.ndarray) -> np.ndarray:
    """Theta expansion normalized by int cosh(x/2) K(x) dx = 1/2."""
    xa = np.abs(x)
    out = np.zeros_like(xa)
    active = xa < 3.7
    y = xa[active]
    e2y = np.exp(2.0 * y)
    for m in range(1, 35):
        out[active] += (
            2.0
            * math.pi
            * m
            * m
            * np.exp(2.5 * y)
            * (2.0 * math.pi * m * m * e2y - 3.0)
            * np.exp(-math.pi * m * m * e2y)
        )
    normalization = np.trapz(np.cosh(x / 2.0) * out, x)
    return out * (0.5 / normalization)


def displacement_energy(
    u: float,
    x: np.ndarray,
    kernel: np.ndarray,
    q: np.ndarray,
) -> float:
    shifted_kernel = np.interp(x - u, x, kernel, left=0.0, right=0.0)
    shifted_q = np.interp(x - u, x, q, left=0.0, right=0.0)
    return float(
        np.trapz(kernel * shifted_kernel * (q - shifted_q) ** 2, x)
    )


def run(dx: float, xmax: float, gamma: float) -> None:
    x = np.arange(-xmax, xmax + dx / 2.0, dx)
    kernel = riemann_kernel(x)
    q = np.cos(gamma * x) / np.cosh(x / 2.0)
    mu_density = 2.0 * np.cosh(x / 2.0) * kernel
    norm = float(np.trapz(q * q * mu_density, x))

    # The overlap vanishes outside |u| <= 2*xmax on this numerical grid.
    u = np.arange(0.0, 2.0 * xmax + dx / 2.0, dx)
    jump = np.empty_like(u)
    jump[0] = 0.0
    for index in range(1, len(u)):
        jump[index] = displacement_energy(u[index], x, kernel, q)

    r_gamma = np.zeros_like(u)
    r_gamma[1:] = np.exp(-2.5 * u[1:]) / (-np.expm1(-2.0 * u[1:]))
    ideal = np.exp(u / 2.0)
    kernel_u = np.interp(u, x[x >= 0.0], kernel[x >= 0.0], left=0.0, right=0.0)

    b_gamma = float(np.trapz(r_gamma * jump, u))
    b_k = float(np.trapz(kernel_u * jump, u))
    ideal_energy = float(np.trapz(ideal * jump, u))

    cutoff = int(math.exp(2.0 * xmax))
    prime_energy = 0.0
    for n, mangoldt in von_mangoldt_atoms(cutoff):
        prime_energy += (
            mangoldt
            / math.sqrt(n)
            * displacement_energy(math.log(n), x, kernel, q)
        )

    p_pnt = prime_energy - ideal_energy
    q_phys = p_pnt + b_gamma
    q_old = p_pnt + THETA * b_gamma
    q_suff = p_pnt + 2.0 * b_k + THETA * b_gamma
    scalar_margin = (1.0 - THETA) * b_gamma - 2.0 * b_k

    print(f"dx={dx:g}, xmax={xmax:g}, gamma={gamma:.15g}, atoms<= {cutoff}")
    print(f"norm       {norm: .15e}")
    print(f"prime      {prime_energy: .15e}")
    print(f"ideal      {ideal_energy: .15e}")
    print(f"P_PNT      {p_pnt: .15e}")
    print(f"b_Gamma    {b_gamma: .15e}")
    print(f"b_K        {b_k: .15e}")
    print(f"Q_phys     {q_phys: .15e}   quotient={q_phys / norm: .15e}")
    print(f"Q_old      {q_old: .15e}   quotient={q_old / norm: .15e}")
    print(f"Q_suff     {q_suff: .15e}   quotient={q_suff / norm: .15e}")
    print(f"Q_phys-Q_suff = {q_phys - q_suff: .15e}")
    print(f"scalar margin = {scalar_margin: .15e}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dx", type=float, default=0.001)
    parser.add_argument("--xmax", type=float, default=4.0)
    parser.add_argument("--gamma", type=float, default=GAMMA1)
    args = parser.parse_args()
    run(args.dx, args.xmax, args.gamma)


if __name__ == "__main__":
    main()
