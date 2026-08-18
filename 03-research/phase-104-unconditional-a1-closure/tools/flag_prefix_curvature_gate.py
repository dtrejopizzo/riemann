#!/usr/bin/env python3
"""Outward fixed-point audit of the weak flag-curvature attack.

This script uses the certified Hasse/eta generator from Phase 103.  It
encloses

    H_n = lambda_n - (501/2002) A_n
        = lambda_n^prime + (1501/2002) A_n

and tests the proposed sufficient curvature inequality Delta^2 H_m >= 0.
No floating-point number enters an asserted sign.

It also evaluates the adjacent two-dimensional flag Schur determinant

    T_n = 4 H_n d_n - (H_n + d_n - H_{n+1})^2,
    d_n = (1501/2002) Delta A_n + gamma,

which is reported only as a finite certificate/diagnostic.  Positivity of
T_n at one index is not a uniform theorem.
"""

from __future__ import annotations

import argparse
from math import comb
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
P103 = HERE.parent.parent / "phase-103-direct-a1-closure" / "tools"
eg = runpy.run_path(str(P103 / "eta_fixed_generator.py"))
em = runpy.run_path(str(P103 / "stieltjes_em_interval_pilot.py"))

F, S = eg["F"], eg["S"]


def qfix(interval):
    return eg["qf"](interval)


def log_series(q):
    """Outward coefficients of log(q), for q[0]=1."""
    top = len(q) - 1
    p = [F(0) for _ in range(top + 1)]
    for n in range(1, top + 1):
        value = q[n]
        for k in range(1, n):
            value = value - (p[k] * q[n - k]).mul_int(k).div(n)
        p[n] = value
    return p


def li_parts(top: int, K: int, terms: int):
    """Return outward intervals (A_n, lambda_n^prime, H_n), 0<=n<=top."""
    q = eg["q_coeffs"](K, top, terms)
    p = log_series(q)

    old = em["ns"]
    log4 = qfix(old["log4pi"])
    zeta = {k: qfix(v) for k, v in old["zeta"].items() if k <= top}
    for k in range(9, top + 1):
        zeta[k] = qfix(em["zeta_interval"](k))

    arch = [F(0) for _ in range(top + 1)]
    prime = [F(0) for _ in range(top + 1)]
    margin = [F(0) for _ in range(top + 1)]
    gamma0 = q[1]

    for n in range(1, top + 1):
        pn = F(0)
        for k in range(1, n + 1):
            pn = pn + p[k].mul_int(n * comb(n - 1, k - 1))

        an = F(S) - (gamma0 + log4).mul_int(n).div(2)
        for k in range(2, n + 1):
            multiplier = (-1 if k % 2 else 1) * comb(n, k) * (2**k - 1)
            an = an + zeta[k].mul_int(multiplier).div(2**k)

        arch[n] = an
        prime[n] = pn
        margin[n] = pn + an.mul_int(1501).div(2002)

    return gamma0, arch, prime, margin


def decimal_units(raw: int, digits: int = 15) -> str:
    """Format an integer number of 10^-digits units."""
    sign = "-" if raw < 0 else ""
    raw = abs(raw)
    text = str(raw).rjust(digits + 1, "0")
    return f"{sign}{text[:-digits]}.{text[-digits:]}"


def show_interval(label: str, value) -> None:
    width = value.h - value.l
    digits = 15
    scale = 10 ** (eg["P"] - digits)
    lower = value.l // scale
    upper = -((-value.h) // scale)
    print(
        f"{label}: [{decimal_units(lower, digits)}, "
        f"{decimal_units(upper, digits)}] "
        f"raw_width_digits={len(str(width))}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=int, default=219)
    parser.add_argument("--K", type=int, default=850)
    parser.add_argument("--terms", type=int, default=820)
    args = parser.parse_args()

    if args.index < 1 or args.index + 2 >= args.K:
        raise SystemExit("require 1 <= index and index+2 < K")

    top = args.index + 2
    gamma0, arch, _, margin = li_parts(top, args.K, args.terms)
    m = args.index

    curvature = margin[m + 2] - margin[m + 1].mul_int(2) + margin[m]

    # The local Schur test is placed at n=m.  Its exact flag diagonal is
    # d_n=kappa*Delta A_n - B_1=kappa*Delta A_n+gamma.
    delta_a = arch[m + 1] - arch[m]
    d = delta_a.mul_int(1501).div(2002) + gamma0
    cross_twice = margin[m] + d - margin[m + 1]
    schur = (margin[m] * d).mul_int(4) - cross_twice * cross_twice

    print("OUTWARD FIXED-POINT CERTIFICATE; no float is used for signs")
    print(f"index={m} K={args.K} terms={args.terms} scale=10^{eg['P']}")
    show_interval(f"H_{m}", margin[m])
    show_interval(f"H_{m + 1}", margin[m + 1])
    show_interval(f"H_{m + 2}", margin[m + 2])
    show_interval(f"Delta^2 H_{m}", curvature)
    print("curvature_strictly_negative", curvature.h < 0)
    show_interval(f"d_{m}", d)
    show_interval(f"T_{m}", schur)
    print("local_schur_strictly_positive", schur.l > 0)

    if curvature.h >= 0:
        raise SystemExit("FAIL: requested negative-curvature certificate did not close")
    if schur.l <= 0:
        raise SystemExit("FAIL: adjacent local Schur diagnostic is not certified positive")
    print("PASS")


if __name__ == "__main__":
    main()
