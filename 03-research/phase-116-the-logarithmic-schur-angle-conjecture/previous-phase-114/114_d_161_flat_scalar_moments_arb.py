#!/usr/bin/env python3
"""Directed complete-multiplier moments of the D.160 flat column.

D.160 supplies an Arb enclosure of an exactly Tate-primitive polynomial
with twenty vanishing endpoint jets.  This script integrates the complete
joint prime-power--Gamma multiplier on [0,R] and appends the analytic tail
from D.159.  The default small R is a smoke test; the endpoint certificate
uses D161_R=4096.

Run:
  PYTHONPATH=/tmp/d61-flint D161_R=10 python3 this_file.py
"""

from __future__ import annotations

import math
import os
from pathlib import Path

import numpy as np
from flint import acb, arb, ctx


N = int(os.environ.get("D161_N", "170"))
DPS = int(os.environ.get("D161_DPS", "60"))
RMAX = int(os.environ.get("D161_R", "10"))
RSTART = int(os.environ.get("D161_START", "0"))
STEP = int(os.environ.get("D161_STEP", "1"))
MFLAT = int(os.environ.get("D161_M", "20"))
ENDPOINT_SWITCH = int(os.environ.get("D161_ENDPOINT_SWITCH", "64"))
POWERS = [int(x) for x in os.environ.get("D161_POWERS", "1,2,3,4").split(",")]
QUIET = os.environ.get("D161_QUIET", "0") == "1"
ctx.dps = DPS

source = np.load(Path(os.environ.get("D161_COLUMN", "/tmp/d160_flat_arb_column.npz")))
coeff = [arb(repr(float(c)), repr(float(r))) for c, r in zip(source["C"], source["R"])]
derivative_norm2 = arb(repr(float(source["derivative_norm2"])))
endpoint_left = [arb(str(x)) for x in source["EL"]]
endpoint_right = [arb(str(x)) for x in source["ER"]]

T = arb(5).log() / 2
quarter = arb(1) / 4
phase_minus = [acb(1), acb(0, -1), acb(-1), acb(0, 1)]
phase_plus = [acb(1), acb(0, 1), acb(-1), acb(0, -1)]
roots = [arb(2 * n + 1).sqrt() for n in range(N)]


def spherical_sequence_hypergeom(x: acb) -> list[acb]:
    out = []
    odd_double_factorial = 1
    for n in range(N):
        if n:
            odd_double_factorial *= 2 * n + 1
        out.append(
            x**n
            / odd_double_factorial
            * (-x * x / 4).hypgeom_0f1(arb(2 * n + 3) / 2)
        )
    return out


def spherical_sequence_bessel(x: acb) -> list[acb]:
    pref = (acb(arb.pi()) / (2 * x)).sqrt()
    return [pref * x.bessel_j(arb(2 * n + 1) / 2) for n in range(N)]


def fhat_pair(tau: acb) -> tuple[acb, acb]:
    if tau.real > ENDPOINT_SWITCH:
        # Exact finite integration-by-parts expansion.  D.160 stores the
        # first M endpoint derivatives as literal zero, so this route keeps
        # the endpoint-flat gain algebraic.  At the switch 64 the largest
        # cancelling term is about 1e75; the 100-digit D.160 source retains
        # more than twenty guard digits in the final Fourier value.
        ip = acb(0, 1)
        eplus = (ip * tau * T).exp()
        eminus = (-ip * tau * T).exp()
        forward = acb(0)
        for r in range(MFLAT, N):
            forward += (
                acb(endpoint_left[r]) * eplus
                - acb(endpoint_right[r]) * eminus
            ) / (ip * tau) ** (r + 1)
        # Substitute -tau in the same finite identity.
        backward = acb(0)
        for r in range(MFLAT, N):
            backward += (
                acb(endpoint_left[r]) * eminus
                - acb(endpoint_right[r]) * eplus
            ) / (-ip * tau) ** (r + 1)
        return forward, backward

    x = acb(T) * tau
    # On integration balls strictly contained in the right half-plane the
    # Bessel representation is faster.  The entire 0F1 representation
    # handles the first segment, including tau=0, without a removable-hole
    # estimate.
    if tau.real > 0:
        seq = spherical_sequence_bessel(x)
    else:
        seq = spherical_sequence_hypergeom(x)
    forward = acb(0)
    backward = acb(0)
    for n in range(N):
        term = acb(coeff[n] * roots[n]) * seq[n]
        forward += phase_minus[n % 4] * term
        # j_n(-x)=(-1)^n j_n(x), hence the phase changes from (-i)^n
        # to i^n without a second special-function evaluation.
        backward += phase_plus[n % 4] * term
    scale = acb((2 * T).sqrt())
    return scale * forward, scale * backward


def multiplier(tau: acb) -> acb:
    ip = acb(0, 1)
    value = ((acb(quarter) + ip * tau / 2).digamma()
             + (acb(quarter) - ip * tau / 2).digamma()) / 2
    value -= acb(arb.pi().log())
    for n, lam in ((2, arb(2).log()), (3, arb(3).log()), (4, arb(2).log())):
        value -= 2 * acb(lam / arb(n).sqrt()) * (tau * arb(n).log()).cos()
    return value


def integrand(tau: acb, analytic: bool, power: int) -> acb:
    forward, backward = fhat_pair(tau)
    return multiplier(tau) ** power * forward * backward / acb(arb.pi())


def tail(power: int) -> arb:
    if RMAX < 150:
        return arb(0)
    a = 2 * MFLAT
    r = arb(RMAX)
    ell = r.log() + 5
    series = arb(0)
    for j in range(power + 1):
        series += (
            math.comb(power, j)
            * ell ** (power - j)
            * math.factorial(j)
            / (a - 1) ** (j + 1)
        )
    return 2 * T * derivative_norm2 / arb.pi() * r ** (1 - a) * series


out = Path(os.environ.get(
    "D161_SAVE", f"/tmp/d161_flat_moments_{RSTART}_{RMAX}.npz"
))
centres = np.full(4, np.nan)
radii = np.full(4, np.nan)
for power in POWERS:
    total = acb(0)
    for left in range(RSTART, RMAX, STEP):
        right = min(RMAX, left + STEP)
        piece = acb.integral(
            lambda z, analytic: integrand(z, analytic, power),
            arb(left),
            arb(right),
            abs_tol=arb(10) ** (-(DPS // 3)),
            rel_tol=arb(10) ** (-(DPS // 3)),
            depth_limit=45,
            eval_limit=300000,
        )
        total += piece
        if not QUIET:
            print("power,segment =", power, left, right, "partial =", total, flush=True)
    assert total.imag.contains(0)
    real = total.real
    tbound = tail(power) if RSTART == 0 else arb(0)
    if RSTART == 0 and RMAX >= 150:
        real = arb(real.mid(), real.rad() + tbound.upper())
    centres[power - 1] = float(real.mid())
    radii[power - 1] = float(real.rad())
    print(f"H{power} complete enclosure =", real, "tail <=", tbound, flush=True)

np.savez(out, C=centres, R=np.nextafter(radii, np.inf), cutoff=RMAX)
print("saved", out)
if RSTART == 0 and RMAX >= 150:
    print("D161 directed flat scalar moments INCLUDING TAIL: PASS")
else:
    print("D161 directed flat scalar finite-range smoke test: PASS")
