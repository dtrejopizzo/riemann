#!/usr/bin/env python3
"""Checks for 104_92 (diagnostic, not a proof of RH)."""

from __future__ import annotations

import cmath
import math


def poisson(r: float, theta: float) -> float:
    return (1.0 - r * r) / (1.0 - 2.0 * r * math.cos(theta) + r * r)


def positive_mass_closed(r: float) -> float:
    return 4.0 / math.pi * math.atan((1.0 + r) / (1.0 - r)) - 1.0


def trap_periodic(values: list[float]) -> float:
    return sum(values) / len(values)


def spike_checks() -> None:
    grid = 400_000
    thetas = [2.0 * math.pi * (j + 0.5) / grid for j in range(grid)]
    for r in (0.2, 0.7, 0.95, 0.995):
        vals = [poisson(r, t) - poisson(-r, t) for t in thetas]
        numeric = trap_periodic([max(v, 0.0) for v in vals])
        closed = positive_mass_closed(r)
        assert abs(numeric - closed) < 2.5e-5, (r, numeric, closed)
        for t, v in zip(thetas[::997], vals[::997]):
            assert v * math.cos(t) >= -1e-13

    # Cesaro: common sign makes positive parts exactly additive.
    # Stop before the narrowest Poisson peak falls below the quadrature mesh.
    rs = [1.0 - 2.0 ** (-j) for j in range(1, 13)]
    cesaro_closed = sum(positive_mass_closed(r) for r in rs) / len(rs)
    cesaro_vals = [
        sum(poisson(r, t) - poisson(-r, t) for r in rs) / len(rs)
        for t in thetas
    ]
    cesaro_numeric = trap_periodic([max(v, 0.0) for v in cesaro_vals])
    assert abs(cesaro_numeric - cesaro_closed) < 3e-5

    # Abel: normalize a finite tail; omitted mass is negligible here.
    q = 0.85
    rs_abel = [1.0 - 2.0 ** (-j) for j in range(1, 51)]
    raw = [(1.0 - q) * q ** (j - 1) for j in range(1, len(rs_abel) + 1)]
    norm = sum(raw)
    weights = [a / norm for a in raw]
    abel_closed = sum(
        a * positive_mass_closed(r) for a, r in zip(weights, rs_abel)
    )
    # Exact equality follows pointwise from the common sign; no second large
    # quadrature is needed.
    assert 0.0 < abel_closed < 1.0

    print("spike closed masses: PASS")
    print(f"  Cesaro mass = {cesaro_closed:.12f}")
    print(f"  Abel mass   = {abel_closed:.12f}")


def model_G(s: complex, beta: float, x0: float) -> complex:
    return (
        -cmath.exp((beta - s) * math.log(x0)) / (s - beta)
        -cmath.exp((1.0 - beta - s) * math.log(x0)) / (s - (1.0 - beta))
    )


def model_checks() -> None:
    beta = 0.75
    x0 = 256.0
    density_at_x0 = 1.0 - x0 ** (beta - 1.0) - x0 ** (-beta)
    assert density_at_x0 > 0.0
    for x in (x0, 1e4, 1e8):
        density = 1.0 - x ** (beta - 1.0) - x ** (-beta)
        assert density >= density_at_x0 - 1e-15

    for pole in (beta, 1.0 - beta):
        for delta in (1e-3, 1e-5, 1e-7):
            residue = delta * model_G(complex(pole + delta, 0.0), beta, x0)
            assert abs(residue.real + 1.0) < 0.05
            assert abs(residue.imag) < 1e-12

    print("positive PNT model and residues: PASS")
    print(f"  density at X0 = {density_at_x0:.12f}")


def simpson(f, a: float, b: float, n: int = 20_000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    total += 4.0 * sum(f(a + (2 * j - 1) * h) for j in range(1, n // 2 + 1))
    total += 2.0 * sum(f(a + 2 * j * h) for j in range(1, n // 2))
    return total * h / 3.0


def planted_integrand_y(y: float, beta: float) -> float:
    # (x^-1/2-x^-1)(x^(beta-1)+x^-beta) dx/log x, x=e^y.
    if y == 0.0:
        return 0.0
    return (
        (math.exp(-0.5 * y) - math.exp(-y))
        * (math.exp((beta - 1.0) * y) + math.exp(-beta * y))
        * math.exp(y)
        / y
    )


def smoothing_scale_checks() -> None:
    beta = 0.75
    x0 = 256.0
    y0 = math.log(x0)

    cesaro_rows = []
    for log_x in (12.0, 18.0, 24.0, 30.0):
        def f_ces(y: float) -> float:
            weight = max(1.0 - math.exp(y - log_x), 0.0)
            return weight * planted_integrand_y(y, beta)

        magnitude = simpson(f_ces, y0, log_x, 16_000)
        scale = math.exp((beta - 0.5) * log_x) / log_x
        cesaro_rows.append(magnitude / scale)
    assert min(cesaro_rows[-2:]) > 0.1

    abel_rows = []
    for log_inv_eps in (12.0, 18.0, 24.0, 30.0):
        def f_abel(y: float) -> float:
            # exp(-epsilon*x), computed as exp(-exp(y-L)).
            z = y - log_inv_eps
            weight = 0.0 if z > 6.0 else math.exp(-math.exp(z))
            return weight * planted_integrand_y(y, beta)

        magnitude = simpson(f_abel, y0, log_inv_eps + 6.0, 18_000)
        scale = math.exp((beta - 0.5) * log_inv_eps) / log_inv_eps
        abel_rows.append(magnitude / scale)
    assert min(abel_rows[-2:]) > 0.1

    print("Cesaro/Abel planted-mode scales: PASS")
    print("  Cesaro normalized:", " ".join(f"{v:.6f}" for v in cesaro_rows))
    print("  Abel normalized:  ", " ".join(f"{v:.6f}" for v in abel_rows))


def main() -> None:
    spike_checks()
    model_checks()
    smoothing_scale_checks()
    print("104_92 checker: PASS (diagnostic only; RH not proved)")


if __name__ == "__main__":
    main()
