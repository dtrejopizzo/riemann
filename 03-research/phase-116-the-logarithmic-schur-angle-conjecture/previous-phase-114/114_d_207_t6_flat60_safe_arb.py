#!/usr/bin/env python3
"""Directed finite safe block for the source-defined flat-60 splitting.

The subspace is E_(60,200) intersected with the two exact Tate equations.
The Gegenbauer frame retains (1-u^2)^60 symbolically in rational
Legendre coordinates.  Binary64 is used only to choose a basis of the
two-equation kernel and a whitening congruence.  Gamma, moments, and the
finite safe quadratic form are evaluated in Arb.
"""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import math
import os
from pathlib import Path

import numpy as np
from flint import arb, arb_mat, ctx


HERE = Path(__file__).resolve().parent
N = 200
M = 60
D = N - 2 * M
S = D - 2
DPS = int(os.environ.get("D207_DPS", "1100"))
ctx.dps = DPS
T = arb(6).log() / 2
LAMBDA = Fraction(4 * M + 1, 2)


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
        nxt = zero.copy()
        add_scaled(nxt, xmul(cols[-1]), Fraction(2) * (n + LAMBDA) / (n + 1))
        add_scaled(nxt, cols[-2], -Fraction(n + 2 * LAMBDA - 1, n + 1))
        cols.append(nxt)
    for k in range(D):
        for _ in range(M):
            cols[k] = one_minus_x2(cols[k])
    return cols


def legendre_norm2(col: list[Fraction]) -> Fraction:
    return sum(
        (Fraction(2, 2 * n + 1) * a * a for n, a in enumerate(col)),
        Fraction(0),
    )


def tate(n: int, sign: int) -> arb:
    k = T / 2
    integ = (2 * arb.pi() / k).sqrt() * k.bessel_i(arb(2 * n + 1) / 2)
    if sign < 0 and n % 2:
        integ = -integ
    return (T * arb(2 * n + 1) / 2).sqrt() * integ


def centre(X: arb_mat) -> np.ndarray:
    return np.array(
        [[float(X[i, j].mid()) for j in range(X.ncols())]
         for i in range(X.nrows())]
    )


def gershgorin_positive(X: arb_mat) -> float:
    lower = []
    for i in range(X.nrows()):
        radius = sum(
            (abs(X[i, j]) for j in range(X.ncols()) if i != j),
            arb(0),
        )
        lower.append(X[i, i] - radius)
    worst = min(float(x.lower()) for x in lower)
    print("directed whitened Gershgorin minimum", worst, flush=True)
    assert all(x.lower() > 0 for x in lower)
    return worst


def main() -> None:
    print("building exact flat-60 Gegenbauer columns", flush=True)
    raw = gegenbauer_columns()
    norm2 = [legendre_norm2(col) for col in raw]
    W = arb_mat(N, D)
    for k, col in enumerate(raw):
        scale = (
            T * arb(norm2[k].numerator) / norm2[k].denominator
        ).sqrt()
        for n, value in enumerate(col):
            if value:
                polynomial = arb(value.numerator) / value.denominator / scale
                W[n, k] = polynomial / (arb(2 * n + 1) / (2 * T)).sqrt()

    gp = [tate(n, 1) for n in range(N)]
    gm = [tate(n, -1) for n in range(N)]
    kp = arb_mat([[sum((gp[n] * W[n, k] for n in range(N)), arb(0))
                   for k in range(D)]])
    km = arb_mat([[sum((gm[n] * W[n, k] for n in range(N)), arb(0))
                   for k in range(D)]])
    Kcentre = np.vstack((centre(kp), centre(km)))
    _, _, vh = np.linalg.svd(Kcentre, full_matrices=True)
    selector = vh[2:].T

    # Freeze coordinates 2: and solve both Tate equations exactly in Arb.
    Y = arb_mat(D, S)
    head = arb_mat([[kp[0, 0], kp[0, 1]], [km[0, 0], km[0, 1]]])
    for col in range(S):
        for k in range(2, D):
            Y[k, col] = arb(repr(float(selector[k, col])))
        rhs = arb_mat([
            [-sum((kp[0, k] * Y[k, col] for k in range(2, D)), arb(0))],
            [-sum((km[0, k] * Y[k, col] for k in range(2, D)), arb(0))],
        ])
        solved = head.solve(rhs)
        Y[0, col], Y[1, col] = solved[0, 0], solved[1, 0]
    frame = W * Y
    moments = arb_mat([gp, gm]) * frame
    assert moments.contains(arb_mat(2, S))
    print("exact two-Tate flat frame: PASS", flush=True)

    gram = frame.transpose() * frame
    gc = centre(gram)
    print(
        "flat frame Gram centre eigenvalues",
        np.linalg.eigvalsh((gc + gc.T) / 2)[[0, -1]],
        flush=True,
    )

    spec = importlib.util.spec_from_file_location(
        "d147", HERE / "114_d_147_hurwitz_gamma_arb.py"
    )
    d147 = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(d147)
    gamma = d147.exact_gamma_block(N, DPS, T)
    m0 = arb.pi().log() + arb.const_euler() + arb.pi() / 2 + 3 * arb(2).log()
    base = frame.transpose() * gamma * frame - m0 * gram
    print("exact Gamma projection complete", flush=True)

    contact = np.load("/tmp/d185_contacts6_arb.npz")
    Cc = contact["C"]
    Cr = contact["R"]
    C = arb_mat([[arb(repr(float(Cc[i, j]))) for j in range(N)]
                 for i in range(N)])
    safe_centre = base + frame.transpose() * C * frame

    Fc = centre(frame)
    Fr = np.array([[float(frame[i, j].rad()) for j in range(S)]
                   for i in range(N)])
    Fabs = np.abs(Fc) + Fr + np.abs(np.spacing(Fc)) / 2
    Rcontact = np.nextafter(
        Cr + np.abs(np.spacing(Cc)) / 2,
        np.inf,
    )
    error = Fabs.T @ Rcontact @ Fabs
    delta_float = np.nextafter(
        1.000001 * float(np.max(np.sum(error, axis=1))),
        np.inf,
    )
    delta = arb(repr(delta_float))
    safe_lower = safe_centre
    for i in range(S):
        safe_lower[i, i] -= delta
    print("contact Loewner error", delta, flush=True)

    midpoint = centre(safe_lower)
    midpoint = (midpoint + midpoint.T) / 2
    print(
        "safe finite midpoint eigenvalues",
        np.linalg.eigvalsh(midpoint)[[0, -1]],
        flush=True,
    )
    chol = np.linalg.cholesky(midpoint)
    P0 = np.linalg.inv(chol.T)
    P = arb_mat([[arb(repr(float(P0[i, j]))) for j in range(S)]
                 for i in range(S)])
    whitened = P.transpose() * safe_lower * P
    margin = gershgorin_positive(whitened)

    save = os.environ.get("D207_SAVE", "/tmp/t6_flat60_safe_arb.npz")
    fc = centre(frame)
    fr = np.array([[float(frame[i, j].rad()) for j in range(S)]
                   for i in range(N)])
    bc = centre(safe_lower)
    br = np.array([[float(safe_lower[i, j].rad()) for j in range(S)]
                   for i in range(S)])
    np.savez(
        save,
        frame_c=fc,
        frame_r=np.nextafter(fr + np.abs(np.spacing(fc)) / 2, np.inf),
        safe_c=bc,
        safe_r=np.nextafter(br + np.abs(np.spacing(bc)) / 2, np.inf),
        whitener=P0,
        contact_delta=np.array(delta_float),
        gershgorin_margin=np.array(margin),
        N=np.array(N),
        M=np.array(M),
        dimension=np.array(S),
        digits=np.array(DPS),
    )
    print("saved", save)
    print("D207 DIRECTED FLAT-60 FINITE SAFE BLOCK: PASS")


if __name__ == "__main__":
    main()
