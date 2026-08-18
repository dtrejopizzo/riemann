#!/usr/bin/env python3
"""Aggregate directed D162 frequency bands and append the D159 tail.

The input NPZ files already include outward Gauss--Bernstein quadrature
errors.  This script only performs interval addition and appends, once, the
polarized endpoint-flat tail from the final cutoff to infinity.
"""

from __future__ import annotations

import math
import os
from pathlib import Path

import numpy as np
from flint import arb, ctx


ctx.dps = int(os.environ.get("D163_DPS", "100"))
M = int(os.environ.get("D163_M", "20"))
SOURCE = Path(os.environ.get(
    "D163_SOURCE", "/tmp/d160_flat_arb_columns5_300.npz"
))
FILES = [Path(x) for x in os.environ.get(
    "D163_FILES",
    "/tmp/d162_flat5_seg0_64.npz,"
    "/tmp/d162_flat5_seg64_512.npz,"
    "/tmp/d162_flat5_seg512_1024.npz,"
    "/tmp/d162_flat5_seg1024_1536.npz,"
    "/tmp/d162_flat5_seg1536_2048.npz",
).split(",")]
OUT = Path(os.environ.get(
    "D163_SAVE", "/tmp/d163_flat5_complete_R2048_Q64.npz"
))


parts = [np.load(path) for path in FILES]
starts = [int(x["start"]) for x in parts]
ends = [int(x["cutoff"]) for x in parts]
assert starts[0] == 0
assert all(ends[j] == starts[j + 1] for j in range(len(parts) - 1))
orders = [int(x["order"]) for x in parts]
R = ends[-1]

shape = parts[0]["C"].shape
assert len(shape) == 3 and shape[0] == 4 and shape[1] == shape[2]
K = shape[1]
total = [[[arb(0) for _ in range(K)] for _ in range(K)] for _ in range(4)]
for part in parts:
    assert part["C"].shape == shape and part["R"].shape == shape
    for j in range(4):
        for a in range(K):
            for b in range(K):
                total[j][a][b] += arb(
                    repr(float(part["C"][j, a, b])),
                    repr(float(part["R"][j, a, b])),
                )

source = np.load(SOURCE)
dn = [arb(repr(float(x))) for x in np.atleast_1d(source["derivative_norm2"])]
assert len(dn) == K
T = arb(5).log() / 2


def diagonal_tail(power: int, a: int) -> arb:
    exponent = 2 * M
    cutoff = arb(R)
    ell = cutoff.log() + 5
    series = arb(0)
    for q in range(power + 1):
        series += (
            math.comb(power, q) * ell ** (power - q) * math.factorial(q)
            / (exponent - 1) ** (q + 1)
        )
    return (
        2 * T * dn[a] / arb.pi()
        * cutoff ** (1 - exponent) * series
    )


centres = np.zeros(shape)
radii = np.zeros(shape)
tail_max = []
for j in range(4):
    diagonal = [diagonal_tail(j + 1, a) for a in range(K)]
    tmax = arb(0)
    for a in range(K):
        for b in range(K):
            # Cauchy--Schwarz for the positive measure
            # |r(tau)|^(j+1) d tau on the omitted frequency region.
            tail = (diagonal[a] * diagonal[b]).sqrt()
            tmax = max(tmax, tail)
            ball = arb(total[j][a][b].mid(), total[j][a][b].rad() + tail.upper())
            centres[j, a, b] = float(ball.mid())
            radii[j, a, b] = float(ball.rad())
    tail_max.append(tmax)

# Binary64 serialization is widened after both midpoint and radius rounding.
saved_radii = np.nextafter(
    radii + np.abs(np.spacing(centres)) / 2,
    np.inf,
)
np.savez(
    OUT,
    C=centres,
    R=saved_radii,
    cutoff=R,
    orders=np.array(orders),
    bands=np.array(list(zip(starts, ends))),
)

for j in range(4):
    # The independently integrated (a,b) and (b,a) balls must meet.
    for a in range(K):
        for b in range(K):
            x = arb(repr(float(centres[j, a, b])), repr(float(saved_radii[j, a, b])))
            y = arb(repr(float(centres[j, b, a])), repr(float(saved_radii[j, b, a])))
            assert not (x.upper() < y.lower() or y.upper() < x.lower())
    print(f"H{j + 1}: max radius={saved_radii[j].max():.6e}, tail<={tail_max[j]}")

assert tail_max[-1] < arb("1e-19")
print("saved", OUT)
print("D163 directed five-column matrix moments INCLUDING TAIL: PASS")
