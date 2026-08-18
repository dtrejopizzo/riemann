#!/usr/bin/env python3
"""Finite audit of the neighboring-prime resolvent proposal.

The calculation is deliberately restricted to the Omega=1 layer.  It checks
the identities that any infinite-dimensional proof would have to preserve:

* detailed balance of the neighboring-prime generator;
* self-adjointness of S and C=i[X,S] in L^2(pi_epsilon);
* vanishing of <Cg,g> for a real Laguerre vector;
* failure of the unprojected Poisson compatibility condition;
* solvability after projection away from the layer constants;
* recovery of a non-zero commutator form after a complex phase twist.

This is a diagnostic, not a certificate for A1.
"""

from __future__ import annotations

import math
import numpy as np


def first_primes(count: int) -> np.ndarray:
    limit = max(32, int(count * (math.log(count + 2) + math.log(math.log(count + 3))) * 2.0))
    while True:
        sieve = bytearray(b"\x01") * (limit + 1)
        sieve[:2] = b"\x00\x00"
        for k in range(2, int(limit**0.5) + 1):
            if sieve[k]:
                sieve[k * k : limit + 1 : k] = b"\x00" * (((limit - k * k) // k) + 1)
        primes = np.fromiter((k for k in range(2, limit + 1) if sieve[k]), dtype=float)
        if len(primes) >= count:
            return primes[:count]
        limit *= 2


def laguerre(degree: int, alpha: float, x: np.ndarray) -> np.ndarray:
    if degree == 0:
        return np.ones_like(x)
    lm1 = np.ones_like(x)
    l0 = alpha + 1.0 - x
    if degree == 1:
        return l0
    for k in range(1, degree):
        lp1 = ((2.0 * k + alpha + 1.0 - x) * l0 - (k + alpha) * lm1) / (k + 1.0)
        lm1, l0 = l0, lp1
    return l0


def build_neighbor_generator(primes: np.ndarray, epsilon: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    exponent = 1.0 + epsilon
    alpha = exponent / 2.0
    weights = primes ** (-exponent)
    pi = weights / weights.sum()
    x = np.log(primes)
    size = len(primes)
    s = np.zeros((size, size), dtype=float)
    for j in range(size - 1):
        gap = x[j + 1] - x[j]
        edge_scale = 1.0 / (gap * gap)
        forward = edge_scale * (primes[j] / primes[j + 1]) ** alpha
        backward = edge_scale * (primes[j + 1] / primes[j]) ** alpha
        s[j, j + 1] = forward
        s[j + 1, j] = backward
    s[np.diag_indices(size)] = -s.sum(axis=1)
    return s, pi, x


def weighted_inner(pi: np.ndarray, f: np.ndarray, g: np.ndarray) -> complex:
    return np.vdot(f, pi * g)


def projected_poisson(s: np.ndarray, pi: np.ndarray, rhs: np.ndarray) -> tuple[np.ndarray, float]:
    projected = rhs - np.ones_like(rhs) * np.sum(pi * rhs)
    size = len(pi)
    augmented = np.block(
        [
            [-s.astype(complex), np.ones((size, 1), dtype=complex)],
            [pi.reshape(1, size).astype(complex), np.zeros((1, 1), dtype=complex)],
        ]
    )
    target = np.concatenate([projected, np.zeros(1, dtype=complex)])
    solution = np.linalg.solve(augmented, target)[:size]
    residual = np.linalg.norm((-s) @ solution - projected)
    return solution, float(residual)


def run_case(size: int, epsilon: float, n: int, tau: float) -> None:
    primes = first_primes(size)
    s, pi, x = build_neighbor_generator(primes, epsilon)
    xop = np.diag(x)
    c = 1j * (xop @ s - s @ xop)
    g = laguerre(n - 1, 1.0, x)

    db_error = np.max(np.abs(pi[:, None] * s - (pi[:, None] * s).T))
    s_adjoint = np.max(np.abs(pi[:, None] * s - (pi[:, None] * s).T))
    c_adjoint = np.max(np.abs(pi[:, None] * c - np.conjugate((pi[:, None] * c).T)))
    real_cross = weighted_inner(pi, g, c @ g)
    compatibility = np.sum(pi * (c @ g))
    h, poisson_error = projected_poisson(s, pi, c @ g)
    projected_i3 = weighted_inner(pi, h, c @ g - compatibility)

    twisted = np.exp(1j * tau * x) * g
    twisted_cross = weighted_inner(pi, twisted, c @ twisted)

    root_pi = np.sqrt(pi)
    sym = root_pi[:, None] * (-s) / root_pi[None, :]
    eigenvalues = np.linalg.eigvalsh((sym + sym.T) / 2.0)
    positive = eigenvalues[eigenvalues > 1e-10]
    gap = positive[0] if len(positive) else float("nan")

    print(f"J={size:3d} epsilon={epsilon:.3f} n={n:3d} tau={tau:.3f}")
    print(f"  detailed_balance_error = {db_error:.3e}")
    print(f"  S_adjoint_error        = {s_adjoint:.3e}")
    print(f"  C_adjoint_error        = {c_adjoint:.3e}")
    print(f"  real_cross             = {real_cross.real:+.3e}{real_cross.imag:+.3e}i")
    print(f"  poisson_compatibility  = {compatibility.real:+.3e}{compatibility.imag:+.3e}i")
    print(f"  projected_poisson_err  = {poisson_error:.3e}")
    print(f"  projected_I3           = {projected_i3.real:+.6e}{projected_i3.imag:+.3e}i")
    print(f"  twisted_cross          = {twisted_cross.real:+.6e}{twisted_cross.imag:+.3e}i")
    print(f"  finite_layer_gap       = {gap:.6e}")

    assert db_error < 1e-10
    assert s_adjoint < 1e-10
    assert c_adjoint < 1e-9
    assert abs(real_cross) < 1e-8
    assert poisson_error < 1e-8
    assert projected_i3.real >= -1e-8


def main() -> None:
    for size in (12, 24, 48):
        run_case(size=size, epsilon=0.5, n=8, tau=0.2)
    print("PASS: neighboring-prime projected-resolvent audit")


if __name__ == "__main__":
    main()
