#!/usr/bin/env python3
"""Diagnostics for 106.22.

The script uses only the Python standard library.  Floating-point output is
diagnostic; the displayed series tails have explicit elementary bounds in
the accompanying note.
"""

from __future__ import annotations

import math


EULER_GAMMA = 0.577215664901532860606512090082402431
C_STAR = EULER_GAMMA + math.pi / 2 + 3 * math.log(2) + math.log(math.pi) - 4


def tail_two_nu(L: float, tol: float = 1e-16) -> float:
    """Return 2 integral_L^infinity nu_*(du) by its positive series."""
    total = 0.0
    k = 0
    while True:
        alpha = 2.5 + 2 * k
        term = 2 * math.exp(-alpha * L) / alpha
        total += term
        if term < tol * max(1.0, total):
            return total
        k += 1


def short_budget(L: float) -> float:
    return tail_two_nu(L) - C_STAR + 4 * math.expm1(L / 2)


def bisect_root(fun, lo: float, hi: float, steps: int = 80) -> float:
    flo = fun(lo)
    fhi = fun(hi)
    if flo * fhi > 0:
        raise ValueError("root is not bracketed")
    for _ in range(steps):
        mid = (lo + hi) / 2
        fm = fun(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def prime_power_weights(limit: int):
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    out = []
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        m = p
        while m <= limit:
            out.append((math.log(m), math.log(p) / math.sqrt(m), m))
            m *= p
    return sorted(out)


def gamma_character_energy(omega: float, terms: int = 1_000_000):
    total = 0.0
    for k in range(terms):
        alpha = 2.5 + 2 * k
        total += 2 * omega * omega / (alpha * (alpha * alpha + omega * omega))
    # Integral comparison for the positive decreasing tail.
    error_bound = omega * omega / (2 * (2 * terms + 0.5) ** 2)
    return total, error_bound


def character_quadrature(L: float, omega: float):
    weights = prime_power_weights(int(math.exp(L) + 1e-12))
    weights = [(a, w, m) for a, w, m in weights if a <= L + 1e-12]
    mass = sum(w for _, w, _ in weights)
    atoms = sum(w * 2 * (1 - math.cos(omega * a)) for a, w, _ in weights)
    energy, error = gamma_character_energy(omega)
    z = 0.5 + 1j * omega
    exp_zL = math.exp(z.real * L) * complex(math.cos(z.imag * L), math.sin(z.imag * L))
    continuous = 4 * math.expm1(L / 2) - 2 * ((exp_zL - 1) / z).real
    scalar = C_STAR + 2 * mass - 4 * math.expm1(L / 2)
    value = energy + atoms - continuous - scalar
    return value, error, [m for _, _, m in weights]


def residual_barycenter(L: float, include_endpoint: bool = False):
    weights = prime_power_weights(max(2, int(math.exp(L) + 1e-12)))
    if include_endpoint:
        weights = [(a, w, m) for a, w, m in weights if a <= L + 1e-12]
    else:
        weights = [(a, w, m) for a, w, m in weights if a < L - 1e-12]
    V = 2 * math.expm1(L / 2)
    P = math.exp(L / 2) * (2 * L - 4) + 4
    S = sum(w for _, w, _ in weights)
    M = sum(a * w for a, w, _ in weights)
    residual = V - S
    barycenter = (P - M) / residual
    return residual, barycenter, [m for _, _, m in weights]


def main() -> None:
    density_cross = bisect_root(
        lambda L: math.exp(-3 * L) + math.exp(-2 * L) - 1,
        0.1,
        0.5,
    )
    short_root = bisect_root(short_budget, 0.1, 0.2)
    print(f"c_* = {C_STAR:.15f}")
    print(f"density crossover L_c = {density_cross:.15f}")
    print(f"short-support root L_s = {short_root:.15f}")
    print(f"B(0.14) = {short_budget(0.14):.15f}")

    L = 1.78
    omega = math.pi / (2 * L)
    value, error, atoms = character_quadrature(L, omega)
    print("\nCND character stop gate")
    print(f"L = {L}, omega = pi/(2L), G(L)=2M")
    print(f"literal prime powers = {atoms}")
    print(f"metric quadrature / M = {value:.15f}")
    print(f"Gamma-series tail bound = {error:.3e}")

    print("\nResidual barycenter gate")
    for L, endpoint in [(0.5, False), (math.log(2), True)]:
        residual, barycenter, atoms = residual_barycenter(L, endpoint)
        print(
            f"L={L:.15f}, atoms={atoms}, residual={residual:.15f}, "
            f"required barycenter={barycenter:.15f}"
        )


if __name__ == "__main__":
    main()

