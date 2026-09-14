#!/usr/bin/env python3
"""Targeted diagnostic for the canonical endpoint-mismatch identity.

This does not test row (d).  It tests whether equation (18) in
P3_FINITE_HORIZON_STORAGE_GATE.md is even the correct exact factorization
on a window where positivity is already certified.
"""

import numpy as np
from scipy.special import loggamma, digamma


def primitive_potential(t: np.ndarray, radius: float) -> tuple[np.ndarray, np.ndarray]:
    """Return G and L_0 G for G=(1-(t/r)^2)^4_+."""
    x = t / radius
    inside = np.abs(x) < 1.0
    g = np.zeros_like(t)
    f = np.zeros_like(t)
    y = x[inside]
    g[inside] = (1.0 - y * y) ** 4
    # d^2/dt^2 (1-(t/r)^2)^4
    g_second = (-8.0 + 72.0 * y**2 - 120.0 * y**4 + 56.0 * y**6) / radius**2
    f[inside] = -g_second + 0.25 * g[inside]
    return g, f


def theta_symbol(tau: np.ndarray, primes: tuple[int, ...]) -> np.ndarray:
    q_plus = 0.25 + 0.5j * tau
    q_minus = 0.25 - 0.5j * tau
    theta = np.exp(-1j * tau * np.log(np.pi) + loggamma(q_plus) - loggamma(q_minus))
    for prime in primes:
        a = np.log(prime)
        r = prime ** -0.5
        z = np.exp(1j * a * tau)
        c = ((z - r) / (1.0 - r * z)) / z
        theta /= c
    return theta


def a_symbol(tau: np.ndarray, primes: tuple[int, ...]) -> np.ndarray:
    ans = np.real(digamma(0.25 + 0.5j * tau)) - np.log(np.pi)
    for prime in primes:
        a = np.log(prime)
        r = prime ** -0.5
        poisson = (1.0 - r * r) / np.abs(1.0 - r * np.exp(1j * a * tau)) ** 2
        ans += a * (1.0 - poisson)
    return ans


def run(points: int = 2**17, half_box: float = 32.0) -> None:
    window = np.log(2.0)
    radius = 0.72 * window
    primes = (2, 3)
    dt = 2.0 * half_box / points
    t = -half_box + dt * np.arange(points)
    tau = 2.0 * np.pi * np.fft.fftfreq(points, d=dt)
    _, f = primitive_potential(t, radius)
    theta = theta_symbol(tau, primes)

    # Positive-sign Fourier transform: Fhat = integral exp(+i tau t)f(t)dt.
    # The global phase from the shifted grid cancels when transforming back.
    u = np.fft.fft(theta * np.fft.ifft(f))

    right = t > window
    left = t < -window
    interior = ~(right | left)
    r_vec = np.zeros(points, dtype=complex)
    ell_vec = np.zeros(points, dtype=complex)
    r_vec[right] = np.sqrt(t[right] - window) * u[right]
    ell_vec[left] = np.sqrt(-t[left] - window) * u[left]

    # On the symmetric periodic grid, reflection t -> -t is index n -> -n.
    reflected_r = np.roll(r_vec[::-1], 1)
    d_vec = reflected_r - ell_vec
    endpoint_square = dt * np.vdot(d_vec, d_vec).real

    time_supply = dt * np.sum(t * (np.abs(u) ** 2 - np.abs(f) ** 2)).real
    fhat = dt * points * np.fft.ifft(f)
    spectral_supply = np.sum(a_symbol(tau, primes) * np.abs(fhat) ** 2).real / (
        2.0 * half_box
    )

    u0 = np.where(interior, u, 0.0)
    r_int = dt * (
        np.sum(t * np.abs(u0) ** 2)
        - np.sum(t * np.abs(f) ** 2)
        + window * (np.sum(np.abs(u[right]) ** 2) - np.sum(np.abs(u[left]) ** 2))
    ).real
    rhs_18 = dt * (
        2.0 * np.vdot(ell_vec, ell_vec).real
        - 2.0 * np.vdot(reflected_r, ell_vec).real
    )

    print(f"points={points} half_box={half_box}")
    print(f"max modulus defect={np.max(np.abs(np.abs(theta)-1.0)):.3e}")
    print(f"time supply={time_supply:.15e}")
    print(f"spectral supply={spectral_supply:.15e}")
    print(f"endpoint square={endpoint_square:.15e}")
    print(f"square residual={time_supply-endpoint_square:.15e}")
    print(f"R_int={r_int:.15e}")
    print(f"rhs(18)={rhs_18:.15e}")
    print(f"trace residual={r_int-rhs_18:.15e}")


if __name__ == "__main__":
    run()
