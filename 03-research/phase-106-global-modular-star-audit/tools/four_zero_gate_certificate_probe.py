#!/usr/bin/env python3
"""High-accuracy fixed-witness probe for the 106.139 compensated gate.

The arithmetic and continuous pieces are evaluated with the *theoretical*
theta kernel (no numerical renormalisation).  Composite Simpson weights are
used in both variables.  The aligned displacement grid is evaluated by FFT
correlations; literal prime-power displacements are evaluated directly.

This file deliberately calls itself a probe: the accompanying note records
the analytic tail and quadrature budgets, but a formally outward evaluation
of the four zero boxes and of the finite Simpson sum is still required before
the output can be called a machine certificate.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


THETA = 499.0 / 2000.0
GAMMAS = np.array(
    [
        14.134725141734693790457251983562470270784257115699,
        21.022039638771554992628479593896902777334340524903,
        25.010857580145688763213790992562821818659549672558,
        30.424876125859513210311897530584091320181560023715,
    ]
)
COEFFICIENTS = np.array([4.0, -15.0, 16.0, -5.0])


def simpson_weights(size: int) -> np.ndarray:
    if size % 2 != 1:
        raise ValueError("Simpson grid needs an odd number of points")
    weights = np.ones(size)
    weights[1:-1:2] = 4.0
    weights[2:-1:2] = 2.0
    return weights / 3.0


def theta_kernel(x: np.ndarray, terms: int = 12) -> np.ndarray:
    """Exact normalization K=sum k_m from 106.40, truncated at ``terms``."""
    y = np.abs(x)
    e2y = np.exp(2.0 * y)
    out = np.zeros_like(x)
    for m in range(1, terms + 1):
        mm = float(m * m)
        out += (
            math.pi
            * mm
            * np.exp(2.5 * y)
            * (2.0 * math.pi * mm * e2y - 3.0)
            * np.exp(-math.pi * mm * e2y)
        )
    # The full-line normalization used in 106.31 has int cosh(x/2)K(x)dx=1/2.
    # The positive-half-line atom convention of 106.40 carries half this mass.
    return 2.0 * out


def von_mangoldt_atoms(limit: int) -> list[tuple[int, float]]:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    atoms: list[tuple[int, float]] = []
    for p0 in np.flatnonzero(sieve):
        p = int(p0)
        value = p
        while value <= limit:
            atoms.append((value, math.log(p)))
            value *= p
    atoms.sort()
    return atoms


def fft_convolution(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    target = len(left) + len(right) - 1
    nfft = 1
    while nfft < target:
        nfft *= 2
    return np.fft.irfft(
        np.fft.rfft(left, nfft) * np.fft.rfft(right, nfft), nfft
    )[:target]


def positive_lag_correlations(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    """Return sum_i left[i] right[i-j], j=0,...,size-1."""
    size = len(left)
    full = fft_convolution(left, right[::-1])
    return full[size - 1 : size - 1 + size]


def aligned_jump_grid(
    kernel: np.ndarray, q: np.ndarray, weights: np.ndarray, dx: float
) -> np.ndarray:
    first = positive_lag_correlations(weights * kernel * q * q, kernel)
    second = positive_lag_correlations(weights * kernel, kernel * q * q)
    cross = positive_lag_correlations(weights * kernel * q, kernel * q)
    out = dx * (first + second - 2.0 * cross)
    out[0] = 0.0
    return out


def jump_at(
    u: float,
    x: np.ndarray,
    kernel: np.ndarray,
    q: np.ndarray,
    weights: np.ndarray,
    dx: float,
) -> float:
    shifted_kernel = theta_kernel(x - u)
    shifted_f = sum(
        coefficient * np.cos(gamma * (x - u))
        for coefficient, gamma in zip(COEFFICIENTS, GAMMAS)
    )
    shifted_q = shifted_f / np.cosh((x - u) / 2.0)
    return float(
        dx
        * np.sum(
            weights
            * kernel
            * shifted_kernel
            * (q - shifted_q) ** 2
        )
    )


def run(step: float, xmax: float) -> None:
    count = int(round(2.0 * xmax / step))
    if count % 2:
        count += 1
    step = 2.0 * xmax / count
    x = np.linspace(-xmax, xmax, count + 1)
    weights = simpson_weights(len(x))
    kernel = theta_kernel(x)
    f = sum(
        coefficient * np.cos(gamma * x)
        for coefficient, gamma in zip(COEFFICIENTS, GAMMAS)
    )
    q = f / np.cosh(x / 2.0)

    c_k = step * np.sum(weights * np.cosh(x / 2.0) * kernel)
    norm = step * np.sum(weights * 2.0 * np.cosh(x / 2.0) * kernel * q * q)

    jump = aligned_jump_grid(kernel, q, weights, step)
    u = np.arange(len(jump)) * step
    u_weights = simpson_weights(len(u))
    r_gamma = np.zeros_like(u)
    r_gamma[1:] = np.exp(-2.5 * u[1:]) / (-np.expm1(-2.0 * u[1:]))
    # r_gamma J has removable value zero at u=0.
    b_gamma = step * np.sum(u_weights * r_gamma * jump)
    ideal = step * np.sum(u_weights * np.exp(u / 2.0) * jump)
    b_k = step * np.sum(u_weights * theta_kernel(u) * jump)

    atoms = von_mangoldt_atoms(int(math.exp(2.0 * xmax)))
    prime = 0.0
    for n, logp in atoms:
        prime += logp / math.sqrt(n) * jump_at(
            math.log(n), x, kernel, q, weights, step
        )

    p_pnt = prime - ideal
    q_phys = p_pnt + b_gamma
    q_suff = p_pnt + 2.0 * b_k + THETA * b_gamma
    print(f"step={step:.17g}; xmax={xmax:g}; nodes={len(x)}; atoms={len(atoms)}")
    print(f"int hK     {c_k: .16e}  (target 0.5)")
    print(f"norm       {norm: .16e}")
    print(f"prime      {prime: .16e}")
    print(f"ideal      {ideal: .16e}")
    print(f"b_Gamma    {b_gamma: .16e}")
    print(f"b_K        {b_k: .16e}")
    print(f"Q_phys     {q_phys: .16e}")
    print(f"Q_suff     {q_suff: .16e}")
    print(f"Q_suff/norm {q_suff / norm: .16e}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", type=float, default=0.0005)
    parser.add_argument("--xmax", type=float, default=4.0)
    args = parser.parse_args()
    run(args.step, args.xmax)


if __name__ == "__main__":
    main()
