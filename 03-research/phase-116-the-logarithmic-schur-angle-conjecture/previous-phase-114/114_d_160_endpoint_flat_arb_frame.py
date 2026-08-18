#!/usr/bin/env python3
"""Construct the first endpoint-flat dangerous column with Arb arithmetic.

The basis (1-u^2)^m C_k^(2m+1/2)(u) is built exactly in rational Legendre
coordinates.  A floating eigensolve only selects a direction.  Its last
d-2 basis coordinates are frozen as exact decimal numbers and the first two
are recomputed with Arb so that both Tate moments vanish.  The script then
certifies the m-th derivative norm and the R=4096 Fourier tail bound.

Run with:
  PYTHONPATH=/tmp/d61-flint python3 this_file.py
"""

from __future__ import annotations

from fractions import Fraction
import math
import os
from pathlib import Path

import numpy as np
from flint import arb, ctx


N = int(os.environ.get("D160_N", "170"))
M = int(os.environ.get("D160_M", "20"))
DPS = int(os.environ.get("D160_DPS", "100"))
RTAIL = int(os.environ.get("D160_R", "4096"))
KSEL = int(os.environ.get("D160_K", "1"))
ctx.dps = DPS
assert N > 2 * M + 2
D = N - 2 * M
LAMBDA = Fraction(4 * M + 1, 2)
T = arb(5).log() / 2


def add_scaled(out: list[Fraction], src: list[Fraction], scale: Fraction) -> None:
    for i, value in enumerate(src):
        out[i] += scale * value


def xmul(src: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(N)]
    for n, value in enumerate(src):
        if not value:
            continue
        if n + 1 < N:
            out[n + 1] += value * Fraction(n + 1, 2 * n + 1)
        if n:
            out[n - 1] += value * Fraction(n, 2 * n + 1)
    return out


def one_minus_x2(src: list[Fraction]) -> list[Fraction]:
    xx = xmul(xmul(src))
    return [a - b for a, b in zip(src, xx)]


def gegenbauer_columns() -> list[list[Fraction]]:
    zero = [Fraction(0) for _ in range(N)]
    c0 = zero.copy()
    c0[0] = 1
    cols = [c0]
    if D > 1:
        c1 = zero.copy()
        c1[1] = 2 * LAMBDA
        cols.append(c1)
    for n in range(1, D - 1):
        nxt = [Fraction(0) for _ in range(N)]
        add_scaled(nxt, xmul(cols[-1]), Fraction(2) * (n + LAMBDA) / (n + 1))
        add_scaled(nxt, cols[-2], -Fraction(n + 2 * LAMBDA - 1, n + 1))
        cols.append(nxt)
    for k in range(D):
        for _ in range(M):
            cols[k] = one_minus_x2(cols[k])
    return cols


def legendre_norm2(col: list[Fraction]) -> Fraction:
    return sum((Fraction(2, 2 * n + 1) * a * a for n, a in enumerate(col)), Fraction(0))


def legendre_derivative(col: list[arb]) -> list[arb]:
    out = [arb(0) for _ in range(N)]
    suffix = [arb(0), arb(0)]
    for j in range(N - 1, -1, -1):
        out[j] = (2 * j + 1) * suffix[1 - j % 2]
        suffix[j % 2] += col[j]
    return out


def tate_moment(n: int, sign: int) -> arb:
    k = T / 2
    order = arb(2 * n + 1) / 2
    integ = (2 * arb.pi() / k).sqrt() * k.bessel_i(order)
    if sign < 0 and n % 2:
        integ = -integ
    return (T * arb(2 * n + 1) / 2).sqrt() * integ


print("building exact endpoint-flat Gegenbauer frame", flush=True)
raw = gegenbauer_columns()
norm2_u = [legendre_norm2(col) for col in raw]

# Physical normalized-Legendre coefficient matrix.  The columns are exactly
# orthonormal in L2(-T,T) before interval widening.
basis = [[arb(0) for _ in range(D)] for _ in range(N)]
for k, col in enumerate(raw):
    scale = (T * arb(norm2_u[k].numerator) / norm2_u[k].denominator).sqrt()
    for n, value in enumerate(col):
        if value:
            polynomial_coeff = arb(value.numerator) / value.denominator / scale
            basis[n][k] = polynomial_coeff / (arb(2 * n + 1) / (2 * T)).sqrt()

gp = [tate_moment(n, 1) for n in range(N)]
gm = [tate_moment(n, -1) for n in range(N)]
kp = [sum((gp[n] * basis[n][k] for n in range(N)), arb(0)) for k in range(D)]
km = [sum((gm[n] * basis[n][k] for n in range(N)), arb(0)) for k in range(D)]

# Floating selection in the stable orthonormal flat frame.
wflat = np.array([[float(basis[n][k].mid()) for k in range(D)] for n in range(N)])
kfloat = np.array([[float(x.mid()) for x in kp], [float(x.mid()) for x in km]])
_, _, vh = np.linalg.svd(kfloat, full_matrices=True)
primitive = vh[2:].T
data = np.load(Path(os.environ.get("D160_RITZ", "/tmp/d153_nested170.npz")))
form_path=os.environ.get("D160_FORM")
if form_path:
    fdata=np.load(form_path);ac=np.asarray(fdata[os.environ.get("D160_FORM_KEY","L")])
    if ac.shape==(N-2,N-2):
        vphys=data["vectors"];acenter=vphys@ac@vphys.T
    else:acenter=ac
else:acenter = data["A"]
compressed = primitive.T @ wflat.T @ acenter @ wflat @ primitive
compressed = (compressed + compressed.T) / 2
evals, evecs = np.linalg.eigh(compressed)
selectors = primitive @ evecs[:, :KSEL]
print("floating flat Ritz values =", evals[:6], flush=True)

# Freeze coordinates 2..D-1 and solve the exact two-by-two Tate system.
y = [[arb(0) for _ in range(KSEL)] for _ in range(D)]
for k in range(2, D):
    for a in range(KSEL):
        y[k][a] = arb(repr(float(selectors[k, a])))
det = kp[0] * km[1] - kp[1] * km[0]
for a in range(KSEL):
    rhs_p = -sum((kp[k] * y[k][a] for k in range(2, D)), arb(0))
    rhs_m = -sum((km[k] * y[k][a] for k in range(2, D)), arb(0))
    y[0][a] = (rhs_p * km[1] - kp[1] * rhs_m) / det
    y[1][a] = (kp[0] * rhs_m - rhs_p * km[0]) / det

coeff = [[sum((basis[n][k] * y[k][a] for k in range(D)), arb(0))
          for a in range(KSEL)] for n in range(N)]
gram = [[sum((coeff[n][a] * coeff[n][b] for n in range(N)), arb(0))
         for b in range(KSEL)] for a in range(KSEL)]
moment_p = [sum((gp[n] * coeff[n][a] for n in range(N)), arb(0))
            for a in range(KSEL)]
moment_m = [sum((gm[n] * coeff[n][a] for n in range(N)), arb(0))
            for a in range(KSEL)]
assert all(x.contains(0) for x in moment_p + moment_m)
assert all(gram[a][a] > arb("0.99") and gram[a][a] < arb("1.01")
           for a in range(KSEL))

# Build the combined polynomial Legendre coefficients, differentiate M
# times exactly in the Legendre recurrence, and enclose its L2 norm.
poly = [[arb(0) for _ in range(KSEL)] for _ in range(N)]
for k in range(D):
    scale = (T * arb(norm2_u[k].numerator) / norm2_u[k].denominator).sqrt()
    for n, value in enumerate(raw[k]):
        if value:
            for a in range(KSEL):
                poly[n][a] += y[k][a] * arb(value.numerator) / value.denominator / scale
derivative_norm2 = []
for a in range(KSEL):
    der = [poly[n][a] for n in range(N)]
    for _ in range(M):
        der = legendre_derivative(der)
    derivative_norm2.append(sum(
        (2 * der[n] * der[n] / (2 * n + 1) for n in range(N)), arb(0)
    ) * T ** (1 - 2 * M))

# Exact endpoint derivative data for the fast finite Fourier formula.  The
# first M rows are set to literal zero from the retained factor, rather than
# recovered by subtracting expanded coefficients.
endpoint_minus = [[arb(0) for _ in range(KSEL)] for _ in range(N)]
endpoint_plus = [[arb(0) for _ in range(KSEL)] for _ in range(N)]
for a in range(KSEL):
    running = [poly[n][a] for n in range(N)]
    for r in range(N):
        if r >= M:
            endpoint_plus[r][a] = sum(running, arb(0)) / T**r
            endpoint_minus[r][a] = sum(
                ((-1 if n % 2 else 1) * running[n] for n in range(N)), arb(0)
            ) / T**r
        running = legendre_derivative(running)

def moment_tail(power: int, aidx: int) -> arb:
    a = 2 * M
    r = arb(RTAIL)
    ell = r.log() + 5
    series = arb(0)
    for j in range(power + 1):
        series += (
            math.comb(power, j)
            * ell ** (power - j)
            * math.factorial(j)
            / (a - 1) ** (j + 1)
        )
    return 2 * T * derivative_norm2[aidx] / arb.pi() * r ** (1 - a) * series


tails = [[moment_tail(j, a) for j in range(1, 5)] for a in range(KSEL)]
if RTAIL >= 4096:
    assert all(row[-1] < arb(os.environ.get("D160_TAIL_MAX","2e-27")) for row in tails)
elif RTAIL >= 1024:
    assert all(row[-1] < arb("2e-15") for row in tails)
print("two Tate moments =", moment_p, moment_m)
print("column Gram =", gram)
print("m-th derivative norm^2 =", derivative_norm2)
print("R=4096 moment tails =", tails)

save = os.environ.get("D160_SAVE", "/tmp/d160_flat_arb_column.npz")
centres = np.array([[float(coeff[n][a].mid()) for a in range(KSEL)] for n in range(N)])
radii = np.array([[float(coeff[n][a].rad()) for a in range(KSEL)] for n in range(N)])
saved_radii = (
    np.nextafter(radii, np.inf)
    + np.abs(np.spacing(centres)) / 2
    + np.nextafter(0.0, 1.0)
)
if KSEL == 1:
    centres, saved_radii = centres[:, 0], saved_radii[:, 0]
    el = np.array([str(endpoint_minus[n][0]) for n in range(N)])
    er = np.array([str(endpoint_plus[n][0]) for n in range(N)])
    dn = np.nextafter(float(derivative_norm2[0].upper()), np.inf)
else:
    el = np.array([[str(endpoint_minus[n][a]) for a in range(KSEL)] for n in range(N)])
    er = np.array([[str(endpoint_plus[n][a]) for a in range(KSEL)] for n in range(N)])
    dn = np.nextafter(
        np.array([float(x.upper()) for x in derivative_norm2]),
        np.inf,
    )
np.savez(save, C=centres, R=saved_radii, derivative_norm2=dn, EL=el, ER=er)
print("saved directed flat column enclosure to", save)
print("D160 endpoint-flat Arb frame and tail: PASS")
