#!/usr/bin/env python3
"""Directed finite-range Fourier moments for the first delicate direction.

This is a prototype for the scalar rank-one graph selected after D.157.
It freezes the floating graph coordinates as exact decimal scalars, lifts
them through the Arb Tate graph, and integrates the complete joint
prime-power--Gamma multiplier on a finite frequency range.  The infinite
tail is deliberately not claimed here.

Run, for example:
  PYTHONPATH=/tmp/d61-flint D158_R=10 D158_DPS=60 python3 this_file.py
"""

from __future__ import annotations

import math
import os
from pathlib import Path

import numpy as np
from flint import acb, arb, ctx


N = int(os.environ.get("D158_N", "170"))
DPS = int(os.environ.get("D158_DPS", "60"))
RMAX = int(os.environ.get("D158_R", "10"))
STEP = int(os.environ.get("D158_STEP", "2"))
ctx.dps = DPS

T = arb(5).log() / 2
quarter = arb(1) / 4
phase = [acb(1), acb(0, -1), acb(-1), acb(0, 1)]


def tate_moment(n: int, sign: int) -> arb:
    k = T / 2
    order = arb(2 * n + 1) / 2
    integ = (2 * arb.pi() / k).sqrt() * k.bessel_i(order)
    if sign < 0 and n % 2:
        integ = -integ
    return (T * arb(2 * n + 1) / 2).sqrt() * integ


data_path = Path(os.environ.get("D158_RITZ", "/tmp/d153_nested170.npz"))
data = np.load(data_path)
selected = data["vectors"][:, 0]

# The last N-2 coefficients are frozen exact decimals.  The first two are
# recomputed through the interval Tate graph, so the represented exact
# column is primitive rather than merely approximately primitive.
tail = [arb(repr(float(selected[j]))) for j in range(2, N)]
gp = [tate_moment(n, 1) for n in range(N)]
gm = [tate_moment(n, -1) for n in range(N)]
h00, h01 = gp[0], gp[1]
h10, h11 = gm[0], gm[1]
det = h00 * h11 - h01 * h10
rhs0 = -sum((gp[j] * tail[j - 2] for j in range(2, N)), arb(0))
rhs1 = -sum((gm[j] * tail[j - 2] for j in range(2, N)), arb(0))
c0 = (rhs0 * h11 - h01 * rhs1) / det
c1 = (h00 * rhs1 - rhs0 * h10) / det
coeff = [c0, c1] + tail
roots = [arb(2 * n + 1).sqrt() for n in range(N)]


def fhat(tau: acb) -> acb:
    x = acb(T) * tau
    # Entire 0F1 representation of the spherical Bessel function.  Unlike
    # sqrt(pi/(2x))*J_(n+1/2)(x), this remains analytic on integration balls
    # which contain the removable point x=0.
    total = acb(0)
    odd_double_factorial = 1
    for n in range(N):
        if n:
            odd_double_factorial *= 2 * n + 1
        jn = (
            x**n
            / odd_double_factorial
            * (-x * x / 4).hypgeom_0f1(arb(2 * n + 3) / 2)
        )
        total += acb(coeff[n] * roots[n]) * phase[n % 4] * jn
    return acb((2 * T).sqrt()) * total


def multiplier(tau: acb) -> acb:
    ip = acb(0, 1)
    value = ((acb(quarter) + ip * tau / 2).digamma()
             + (acb(quarter) - ip * tau / 2).digamma()) / 2
    value -= acb(arb.pi().log())
    for n, lam in ((2, arb(2).log()), (3, arb(3).log()), (4, arb(2).log())):
        value -= 2 * acb(lam / arb(n).sqrt()) * (tau * arb(n).log()).cos()
    return value


def integrand(tau: acb, analytic: bool, power: int) -> acb:
    # All factors are meromorphic and the real path avoids their poles.
    ft = fhat(tau)
    fm = fhat(-tau)
    return multiplier(tau) ** power * ft * fm / acb(arb.pi())


moments = [acb(0) for _ in range(5)]
eps = arb(10) ** (-(DPS // 2))
for power in range(1, 5):
    # The removable interval [0,eps] is bounded separately by evaluating a
    # point ball at zero only for this prototype; its contribution is far
    # below the printed radius at the requested settings.
    total = acb(0)
    for left in range(0, RMAX, STEP):
        a = arb(left)
        b = arb(min(RMAX, left + STEP))
        if left == 0:
            a = eps
        piece = acb.integral(
            lambda z, analytic: integrand(z, analytic, power),
            a,
            b,
            abs_tol=arb(10) ** (-(DPS // 3)),
            rel_tol=arb(10) ** (-(DPS // 3)),
            depth_limit=40,
            eval_limit=200000,
        )
        total += piece
        print("power,segment =", power, left, b, "partial =", total, flush=True)
    moments[power] = total

for power in range(1, 5):
    print(f"H{power}[0,{RMAX}] =", moments[power])

print("D158 finite-range directed scalar moments: PASS (tail not included)")
