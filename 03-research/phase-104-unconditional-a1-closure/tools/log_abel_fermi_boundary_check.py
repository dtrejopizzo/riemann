#!/usr/bin/env python3
"""Diagnostics for 104_64.

This is not a proof of any limiting statement.  It checks:

* the off-line quartet Abel--Fermi mean tends toward 1/4;
* the harmonic mass of 4 | n below h^{-beta} tends toward beta/4;
* the sharp-transition proxy for the high-frequency correction tends
  toward alpha/8.

Only the standard library is used.
"""

from __future__ import annotations

import math


def logistic(y: float) -> float:
    if y >= 40.0:
        return math.exp(-y)
    if y <= -40.0:
        return 1.0 - math.exp(y)
    return 1.0 / (1.0 + math.exp(y))


def quartet_fermi_term(n: int, t: float = 1.0) -> float:
    r = n % 4
    if r in (1, 3):
        qn = 4.0
    elif n > 500:
        return 1.0 if r == 0 else 0.0
    else:
        power = math.ldexp(1.0, n)
        if r == 0:
            qn = 4.0 - 2.0 * (power + 1.0 / power)
        else:
            qn = 4.0 + 2.0 * (power + 1.0 / power)
    return logistic(t * (qn + math.log(n + 1.0)))


def abel_fermi(h: float, t: float = 1.0) -> float:
    # e^{-h n}<e^{-35} beyond this point; the omitted weighted tail is
    # negligible on the diagnostic scale.
    nmax = math.ceil(35.0 / h)
    numerator = 0.0
    for n in range(1, nmax + 1):
        numerator += math.exp(-h * n) * quartet_fermi_term(n, t) / n
    return numerator / (-math.log1p(-math.exp(-h)))


def progression_mass(h: float, beta: float) -> float:
    nmax = int(h ** (-beta))
    total = 0.0
    for n in range(4, nmax + 1, 4):
        total += math.exp(-h * n) / n
    return total / (-math.log1p(-math.exp(-h)))


def boundary_proxy(h: float, alpha: float, t: float = 1.0) -> float:
    # delta=exp(-h^{-alpha}); delta*t*Y_n crosses one at
    # n approximately h^{-alpha}/log(2).  On the low-n side J_n(delta)
    # tends to J_n(0)=tanh(tY_n/2)/2; on the high-n side it tends to zero.
    ncrit = int(h ** (-alpha) / math.log(2.0))
    total = 0.0
    for n in range(4, ncrit + 1, 4):
        if n > 50:
            j0 = 0.5
        else:
            power = math.ldexp(1.0, n)
            y = 2.0 * (power + 1.0 / power) - 4.0 - math.log(n + 1.0)
            j0 = 0.5 * math.tanh(t * y / 2.0)
        total += math.exp(-h * n) * j0 / n
    return total / (-math.log1p(-math.exp(-h)))


def main() -> None:
    hs = (0.02, 0.01, 0.005, 0.002, 0.001)
    print("quartet Abel--Fermi mean (target 0.25)")
    for h in hs:
        print(f"  h={h:7g}  value={abel_fermi(h):.9f}")

    scale_hs = (1e-3, 1e-4, 1e-5, 1e-6)
    print("\nharmonic progression law (targets beta/4)")
    for beta in (0.25, 0.5, 0.75):
        values = [progression_mass(h, beta) for h in scale_hs]
        print(
            f"  beta={beta:.2f} target={beta/4:.6f}  "
            + " ".join(f"{value:.6f}" for value in values)
        )

    print("\ndouble-log boundary proxy (targets alpha/8)")
    for alpha in (0.25, 0.5, 0.75):
        values = [boundary_proxy(h, alpha) for h in scale_hs]
        print(
            f"  alpha={alpha:.2f} target={alpha/8:.6f}  "
            + " ".join(f"{value:.6f}" for value in values)
        )

    # Exact structural checks for the quartet.
    for n in range(4, 65, 4):
        power = 1 << n
        y = 2.0 * (power + 1.0 / power) - 4.0 - math.log(n + 1.0)
        assert y >= power
    assert abs(sum(1.0 / n for n in range(4, 401, 4))
               - 0.25 * sum(1.0 / k for k in range(1, 101))) < 1e-14
    print("\nPASS")


if __name__ == "__main__":
    main()
