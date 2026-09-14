#!/usr/bin/env python3
"""Fast directed contact matrix for log(5)/2 on V260.

This is algebraically D.100 with the same certified Gauss rule.  The only
change is to assemble each outer-product sum as an ``arb_mat`` product
instead of O(Q N^2) Python-level ball operations.
"""

from __future__ import annotations

import math
import os

import numpy as np
from flint import arb, arb_mat, ctx
from numpy.polynomial.legendre import leggauss


ctx.prec = int(os.environ.get("P3_CONTACT_PREC", "768"))
N = int(os.environ.get("P3_CONTACT_N", "260"))
Q = N + 4
assert Q % 2 == 0


def legvals(x: arb, count: int) -> list[arb]:
    out = [arb(1)]
    if count == 1:
        return out
    out.append(x)
    for n in range(1, count - 1):
        out.append(((2 * n + 1) * x * out[-1] - n * out[-2]) / (n + 1))
    return out


def p_q(x: arb) -> arb:
    return legvals(x, Q + 1)[-1]


approx = leggauss(Q)[0]
positive: list[arb] = []
for index, root in enumerate(approx[Q // 2:]):
    lo = arb(repr(root - 1e-10))
    hi = arb(repr(root + 1e-10))
    flo = p_q(lo)
    fhi = p_q(hi)
    assert (flo < 0 or flo > 0) and (fhi < 0 or fhi > 0)
    assert (flo < 0) != (fhi < 0)
    for _ in range(min(760, int(0.72 * ctx.prec))):
        mid = (lo + hi) / 2
        fm = p_q(mid)
        if not (fm < 0 or fm > 0):
            break
        if (fm < 0) == (flo < 0):
            lo, flo = mid, fm
        else:
            hi = mid
    mid = (lo + hi) / 2
    positive.append(arb(mid.mid(), (hi - lo) / 2 + mid.rad()))
    if (index + 1) % 40 == 0:
        print("certified positive roots", index + 1, flush=True)

roots = [-x for x in reversed(positive)] + positive
weights: list[arb] = []
for x in roots:
    vals = legvals(x, Q + 1)
    derivative = Q * (x * vals[Q] - vals[Q - 1]) / (x * x - 1)
    weights.append(2 / ((1 - x * x) * derivative * derivative))
mass_error = abs(sum(weights, arb(0)) - 2)
print("Gauss mass enclosure error", mass_error, flush=True)
assert mass_error < arb("1e-100")

T = arb(5).log() / 2
total = arb_mat(N, N)
contacts = ((2, arb(2).log()), (3, arb(3).log()), (4, arb(2).log()))
normalization = [(arb(2 * i + 1) / 2).sqrt() for i in range(N)]

for integer, mangoldt in contacts:
    shift = arb(integer).log()
    coefficient = mangoldt / arb(integer).sqrt()
    displacement = shift / T
    midpoint = -displacement / 2
    half = 1 - displacement / 2
    left = arb_mat(Q, N)
    right = arb_mat(Q, N)
    for row, (node, weight) in enumerate(zip(roots, weights)):
        u = midpoint + half * node
        vx = legvals(u, N)
        vy = legvals(u + displacement, N)
        scale = (half * weight).sqrt()
        for col in range(N):
            left[row, col] = scale * normalization[col] * vx[col]
            right[row, col] = scale * normalization[col] * vy[col]
    block = left.transpose() * right
    total -= coefficient * (block + block.transpose())
    print("assembled directed contact", integer, flush=True)

centre = np.array([[float(total[i, j].mid()) for j in range(N)] for i in range(N)])
native_radii = np.array([[float(total[i, j].rad()) for j in range(N)] for i in range(N)])
print("maximum native radius", native_radii.max(), flush=True)
assert native_radii.max() < 1e-100
# The saved centre is rounded to binary64.  Add half an ulp so the serialized
# pair still encloses the native Arb ball.  This serialization radius is
# necessarily about 1e-16 for order-one entries; it is not the Arb error.
radii = np.nextafter(native_radii + np.abs(np.spacing(centre)) / 2, np.inf)
save = os.environ.get("P3_CONTACT_SAVE", "/tmp/p3_log5_contacts260_fast_arb.npz")
np.savez(save, C=centre, R=radii, endpoint=np.array(5), N=np.array(N),
         bits=np.array(ctx.prec))
print("maximum serialized radius", radii.max(), flush=True)
print("saved", save)
print("P3 LOG5 V260 DIRECTED CONTACTS: PASS")
