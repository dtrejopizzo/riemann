#!/usr/bin/env python3
"""Build the source-defined endpoint-flat promoted split at T=(log 6)/2.

The rectangular pencil chooses a frame in binary64.  Every retained safe
column is then reconstructed in the exact rational Gegenbauer-flat basis and
the two Tate equations are solved again in Arb.  Thus floating point selects
coordinates but does not weaken endpoint flatness or primitiveness.
"""
from fractions import Fraction
import math
import os

import numpy as np
from flint import arb, arb_mat, ctx


N = 200
M = 20
DFLAT = N - 2 * M
DPS = int(os.environ.get("D206_DPS", "300"))
ctx.dps = DPS
T = arb(6).log() / 2
LAMBDA = Fraction(4 * M + 1, 2)


def add_scaled(out, source, scale):
    for i, value in enumerate(source):
        out[i] += scale * value


def xmul(source):
    out = [Fraction(0) for _ in range(N)]
    for n, value in enumerate(source):
        if not value:
            continue
        if n + 1 < N:
            out[n + 1] += value * Fraction(n + 1, 2 * n + 1)
        if n:
            out[n - 1] += value * Fraction(n, 2 * n + 1)
    return out


def one_minus_x2(source):
    twice = xmul(xmul(source))
    return [a - b for a, b in zip(source, twice)]


def gegenbauer_flat_columns():
    zero = [Fraction(0) for _ in range(N)]
    c0 = zero.copy()
    c0[0] = 1
    columns = [c0]
    c1 = zero.copy()
    c1[1] = 2 * LAMBDA
    columns.append(c1)
    for n in range(1, DFLAT - 1):
        nxt = zero.copy()
        add_scaled(nxt, xmul(columns[-1]), Fraction(2) * (n + LAMBDA) / (n + 1))
        add_scaled(nxt, columns[-2], -Fraction(n + 2 * LAMBDA - 1, n + 1))
        columns.append(nxt)
    for k in range(DFLAT):
        for _ in range(M):
            columns[k] = one_minus_x2(columns[k])
    return columns


def tate(n, sign):
    k = T / 2
    integral = (2 * arb.pi() / k).sqrt() * k.bessel_i(arb(2 * n + 1) / 2)
    if sign < 0 and n % 2:
        integral = -integral
    return (T * arb(2 * n + 1) / 2).sqrt() * integral


raw = gegenbauer_flat_columns()
basis = arb_mat(N, DFLAT)
for k, column in enumerate(raw):
    norm2 = sum((Fraction(2, 2 * n + 1) * a * a for n, a in enumerate(column)), Fraction(0))
    scale = (T * arb(norm2.numerator) / norm2.denominator).sqrt()
    for n, value in enumerate(column):
        if value:
            polynomial = arb(value.numerator) / value.denominator / scale
            basis[n, k] = polynomial / (arb(2 * n + 1) / (2 * T)).sqrt()

gp = [tate(n, 1) for n in range(N)]
gm = [tate(n, -1) for n in range(N)]
moments = arb_mat([gp, gm]) * basis
mc = np.array([[float(moments[i, j].mid()) for j in range(DFLAT)] for i in range(2)])
_, _, vh0 = np.linalg.svd(mc, full_matrices=True)
qflat = vh0[2:].T
wc = np.array([[float(basis[i, j].mid()) for j in range(DFLAT)] for i in range(N)])
s0 = wc @ qflat

finite = np.load(os.environ.get("D206_FINITE", "/tmp/t6_complete_operator_legendre.npz"))["C"]
finite = (finite + finite.T) / 2
rect = np.load(os.environ.get("D206_RECT", "/tmp/t6_rect200_260_dps1600.npz"))["C"]
B = s0.T @ finite @ s0
B = (B + B.T) / 2
L = np.linalg.cholesky(B)
linv_t = np.linalg.inv(L.T)
action = rect @ s0 @ linv_t
_, singular, vh = np.linalg.svd(action, full_matrices=True)
square = singular * singular
delta = float(os.environ.get("D206_DELTA", ".219"))
above = int(np.sum(square >= delta))
target = float(os.environ.get("D206_TRACE_TARGET", ".03"))
promote = above
while promote < len(square) and np.sum(square[promote:]) > target:
    promote += 1
print("flat primitive dimension =", s0.shape[1])
print("pencil singular squares first =", square[:20])
print("directions above delta =", above)
print("promotion for remaining band trace <=", target, "=", promote)
print("remaining band trace =", np.sum(square[promote:]))

# Coordinates in the exact flat basis.  The final two-dimensional solve is
# performed separately for every retained safe column.
safe_coordinates = qflat @ linv_t @ vh[promote:].T
nsafe = safe_coordinates.shape[1]
exact_coordinates = arb_mat(DFLAT, nsafe)
head = arb_mat([[moments[0, 0], moments[0, 1]],
                [moments[1, 0], moments[1, 1]]])
for col in range(nsafe):
    for k in range(2, DFLAT):
        exact_coordinates[k, col] = arb(repr(float(safe_coordinates[k, col])))
    rhs = arb_mat([
        [-sum((moments[0, k] * exact_coordinates[k, col]
               for k in range(2, DFLAT)), arb(0))],
        [-sum((moments[1, k] * exact_coordinates[k, col]
               for k in range(2, DFLAT)), arb(0))],
    ])
    solved = head.solve(rhs)
    exact_coordinates[0, col] = solved[0, 0]
    exact_coordinates[1, col] = solved[1, 0]
safe = basis * exact_coordinates
jets = arb_mat([gp, gm]) * safe
assert jets.contains(arb_mat(2, nsafe))

centres = np.array([[float(safe[i, j].mid()) for j in range(nsafe)] for i in range(N)])
radii = np.array([[float(safe[i, j].rad()) + abs(np.spacing(centres[i, j])) / 2
                   for j in range(nsafe)] for i in range(N)])
np.savez(
    os.environ.get("D206_SAVE", "/tmp/t6_exact_flat_promoted_safe.npz"),
    C=centres,
    R=np.nextafter(radii, np.inf),
    singular_values=singular,
    promote=np.array(promote),
    above_delta=np.array(above),
    remaining_band_trace=np.array(np.sum(square[promote:])),
    flat_dimension=np.array(DFLAT - 2),
    safe_dimension=np.array(nsafe),
    endpoint=np.array(6),
    flat_order=np.array(M),
)
print("exact flat/Tate safe frame saved; selection remains diagnostic until interval pencil audit")
