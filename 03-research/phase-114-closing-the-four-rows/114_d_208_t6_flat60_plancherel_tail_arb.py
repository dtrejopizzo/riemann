#!/usr/bin/env python3
"""Directed full-multiplier tail bound for the exact flat-60 safe space.

This avoids differentiating the endpoint expansion term by term.  On the
full line the completed operator is the Fourier multiplier W, and hence
Plancherel controls the weighted sixtieth derivative.  The first sixty
endpoint jets vanish exactly.  One further integration by parts gives an
integrable high-frequency majorant.  All scalar inequalities below are
outward-rounded Arb inequalities; binary64 is used only for the frozen
whitening congruence already certified by D207.
"""
from __future__ import annotations

import math
import os
import numpy as np
from flint import arb, arb_mat, ctx


ctx.dps = int(os.environ.get("D208_DPS", "250"))
N = 200
M = 60
NCUT = int(os.environ.get("D208_NCUT", "600"))
assert NCUT > M
T = arb(6).log() / 2
R = arb(os.environ.get("D208_R", "1e8"))


def amat(c: np.ndarray, r: np.ndarray) -> arb_mat:
    return arb_mat([
        [arb(repr(float(c[i, j])), repr(float(r[i, j])))
         for j in range(c.shape[1])]
        for i in range(c.shape[0])
    ])


def legendre_derivative(columns: list[list[arb]]) -> list[list[arb]]:
    """Differentiate standard Legendre-series columns with respect to t."""
    degree = len(columns)
    width = len(columns[0])
    out = [[arb(0) for _ in range(width)] for _ in range(degree - 1)]
    # P_n'(u)=sum_{k<n, n-k odd}(2k+1)P_k(u), and u=t/T.
    for k in range(degree - 1):
        factor = arb(2 * k + 1) / T
        for n in range(k + 1, degree, 2):
            for j in range(width):
                out[k][j] += factor * columns[n][j]
    return out


def upper(x: arb) -> arb:
    return x.upper()


z = np.load(os.environ.get("D208_SOURCE", "/tmp/t6_flat60_safe_arb.npz"))
N = int(z["N"])
assert int(z["M"]) == M
frame = amat(z["frame_c"], z["frame_r"])
P0 = np.asarray(z["whitener"])
P = arb_mat([[arb(repr(float(P0[i, j]))) for j in range(P0.shape[1])]
             for i in range(P0.shape[0])])
frame = frame * P
width = frame.ncols()

# Convert physical orthonormal coefficients into standard P_n(t/T)
# coefficients, then differentiate exactly in the Legendre basis.
cols = [[frame[n, j] * (arb(2 * n + 1) / (2 * T)).sqrt()
         for j in range(width)] for n in range(N)]
for _ in range(M):
    cols = legendre_derivative(cols)
d60 = cols
d61 = legendre_derivative(d60)


def l2_norm2(columns: list[list[arb]]) -> list[arb]:
    ans = []
    for j in range(width):
        value = sum((2 * T / arb(2 * k + 1) * columns[k][j] ** 2
                     for k in range(len(columns))), arb(0))
        ans.append(upper(value))
    return ans


n60 = l2_norm2(d60)
n61 = l2_norm2(d61)
ep = []
for j in range(width):
    plus = sum((d60[k][j] for k in range(len(d60))), arb(0))
    minus = sum(((-1 if k % 2 else 1) * d60[k][j]
                 for k in range(len(d60))), arb(0))
    ep.append(upper(abs(plus)) + upper(abs(minus)))

# On the real axis the recurrence for digamma shifted by 20, its elementary
# asymptotic remainder, log(pi), and the four active contacts imply
# |W(tau)| <= log(|tau|+21)+31.  This is the same deliberately rounded
# majorant used by D162 on the larger strip |Im tau|<=0.4.
WR = (R + 21).log() + 31
C = arb(31) + (1 + arb(21) / R).log()
logR = R.log()
high_integral = ((logR + C) ** 2 + 2 * (logR + C) + 2) / R

jdiag = []
for j in range(width):
    boundary = ep[j] + (2 * T * n61[j]).sqrt()
    # Both frequency half-lines and the 1/(2*pi) Plancherel convention give
    # high_integral/pi.
    value = WR ** 2 * n60[j] + boundary ** 2 * high_integral / arb.pi()
    jdiag.append(upper(value))
trace_j = sum(jdiag, arb(0))

# D207 proves P^* B P >= g I by directed Gershgorin.
g = arb(repr(float(z["gershgorin_margin"])))
normalized_j = trace_j / g

# Sharp associated-Legendre coefficient (540! / 660!) T^120, evaluated as
# a product so no floating factorial enters the certificate.
csharp = T ** (2 * M)
for k in range(NCUT - M + 1, NCUT + M + 1):
    csharp /= k
tail = upper(csharp * normalized_j)

print("dimension =", width)
print("W low-frequency majorant =", WR)
print("trace J60 upper =", trace_j)
print("normalized J60 upper =", normalized_j)
print("sharp coefficient =", csharp)
print(f"post-{NCUT} tail trace upper =", tail)
target = arb(os.environ.get("D208_TARGET", "0.05"))
assert tail < target

np.savez(
    os.environ.get("D208_SAVE", "/tmp/t6_flat60_plancherel_tail_arb.npz"),
    trace_j_upper=np.array(str(trace_j.upper())),
    normalized_j_upper=np.array(str(normalized_j.upper())),
    csharp_upper=np.array(str(csharp.upper())),
    tail_upper=np.array(float(tail.upper())),
    cutoff=np.array(NCUT), order=np.array(M), radius=np.array(float(R)),
    dimension=np.array(width), digits=np.array(ctx.dps),
)
print(f"D208 DIRECTED COMPLETE-MULTIPLIER POST-{NCUT} TAIL: PASS")
