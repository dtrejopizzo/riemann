#!/usr/bin/env python3
"""Stable directed V200 certificate at T=log(6)/2.

The numerical eigensystem is used only to choose a frame.  Both Tate jets
are then imposed in Arb.  Gamma and the delicate contact rows are evaluated
natively in Arb.  The 196-dimensional safe block is whitened once, and only
a 2 by 2 Schur complement remains.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from flint import arb, arb_mat, ctx


HERE = Path(__file__).resolve().parent
N = 200
ND = 2
NS = N - 2 - ND
QG = N + 4
DPS = int(os.environ.get("D199_DPS", "160"))
ctx.dps = DPS
T = arb(6).log() / 2


def sub(X: arb_mat, r0: int, r1: int, c0: int, c1: int) -> arb_mat:
    return arb_mat([[X[i, j] for j in range(c0, c1)] for i in range(r0, r1)])


def center(X: arb_mat) -> np.ndarray:
    return np.array(
        [[float(X[i, j].mid()) for j in range(X.ncols())]
         for i in range(X.nrows())]
    )


def float_ball(c: float, r: float) -> arb:
    rr = np.nextafter(float(r), np.inf) + abs(np.spacing(float(c))) / 2
    rr += np.nextafter(0.0, 1.0)
    return arb(repr(float(c)), repr(float(rr)))


def tate(n: int, sign: int) -> arb:
    k = T / 2
    integ = (2 * arb.pi() / k).sqrt() * k.bessel_i(arb(2 * n + 1) / 2)
    if sign < 0 and n % 2:
        integ = -integ
    return (T * arb(2 * n + 1) / 2).sqrt() * integ


def legvals(x: arb, nmax: int) -> list[arb]:
    out = [arb(1)]
    if nmax == 1:
        return out
    out.append(x)
    for n in range(1, nmax - 1):
        out.append(((2 * n + 1) * x * out[-1] - n * out[-2]) / (n + 1))
    return out


def gauss_rule() -> tuple[list[arb], list[arb]]:
    """Directed QG-node Gauss rule; exact for every product below."""
    directed = [arb.legendre_p_root(QG, k, weight=True) for k in range(QG)]
    roots = [pair[0] for pair in directed]
    weights = [pair[1] for pair in directed]
    mass_error = abs(sum(weights, arb(0)) - 2)
    print("Gauss mass error", mass_error, flush=True)
    assert mass_error < arb("1e-55")
    return roots, weights


def native_contact_on_delicate(D: arb_mat) -> arb_mat:
    """Return C*D with all 2,3,4,5 contacts, natively in Arb."""
    roots, weights = gauss_rule()
    U = arb_mat(N, ND)
    contacts = ((2, arb(2).log()), (3, arb(3).log()),
                (4, arb(2).log()), (5, arb(5).log()))
    norms = [(arb(2 * i + 1) / 2).sqrt() for i in range(N)]
    for nn, lam in contacts:
        shift = arb(nn).log()
        d = shift / T
        mid = -d / 2
        half = 1 - d / 2
        coefficient = lam / arb(nn).sqrt()
        for iq, (node, weight) in enumerate(zip(roots, weights)):
            u = mid + half * node
            vx = legvals(u, N)
            vy = legvals(u + d, N)
            for i in range(N):
                vx[i] *= norms[i]
                vy[i] *= norms[i]
            dx = [sum((D[i, j] * vx[i] for i in range(N)), arb(0))
                  for j in range(ND)]
            dy = [sum((D[i, j] * vy[i] for i in range(N)), arb(0))
                  for j in range(ND)]
            scale = -coefficient * half * weight
            for i in range(N):
                for j in range(ND):
                    U[i, j] += scale * (vx[i] * dy[j] + vy[i] * dx[j])
        print("native contact", nn, "complete", flush=True)
    return U


def gershgorin_positive(X: arb_mat, name: str) -> list[arb]:
    margins = []
    for i in range(X.nrows()):
        off = sum((abs(X[i, j]) for j in range(X.ncols()) if j != i), arb(0))
        margins.append(X[i, i] - off)
    worst = min(margins, key=lambda z: float(z.lower()))
    print(name, "directed Gershgorin margin", worst, flush=True)
    assert all(x.lower() > 0 for x in margins)
    return margins


def main() -> None:
    # The binary centre chooses the frame only.  It is never used for the
    # final quadratic entries.
    approx_path = os.environ.get(
        "D199_APPROX", "/tmp/t6_complete_operator_legendre.npz"
    )
    approx = np.load(approx_path)["C"]
    approx = (approx + approx.T) / 2

    gp = [tate(i, 1) for i in range(N)]
    gm = [tate(i, -1) for i in range(N)]
    Hc = np.array([[float(x.mid()) for x in gp],
                   [float(x.mid()) for x in gm]])
    _, _, vh = np.linalg.svd(Hc, full_matrices=True)
    Q0 = vh[2:].T
    evals, vectors = np.linalg.eigh(Q0.T @ approx @ Q0)
    X0 = Q0 @ vectors
    print("primitive centre eigenvalues", evals[:8], flush=True)
    assert evals[2] > 1.0e-11

    # Freeze only the numerical tails and solve the two Tate equations in
    # Arb.  Every column of X is therefore exactly primitive.
    head = arb_mat([[gp[0], gp[1]], [gm[0], gm[1]]])
    X = arb_mat(N, N - 2)
    for col in range(N - 2):
        tail = [arb(repr(float(X0[i, col]))) for i in range(2, N)]
        rhs = arb_mat([
            [-sum((gp[i] * tail[i - 2] for i in range(2, N)), arb(0))],
            [-sum((gm[i] * tail[i - 2] for i in range(2, N)), arb(0))],
        ])
        solved = head.solve(rhs)
        X[0, col], X[1, col] = solved[0, 0], solved[1, 0]
        for i in range(2, N):
            X[i, col] = tail[i - 2]
    jet_residual = arb_mat([gp, gm]) * X
    assert jet_residual.contains(arb_mat(2, N - 2))
    bad_x = [(i, j) for i in range(N) for j in range(N - 2)
             if not X[i, j].is_finite()]
    assert not bad_x, f"nonfinite primitive frame entries: {bad_x[:3]}"
    max_xrad = max((X[i, j].rad() for i in range(N)
                    for j in range(N - 2)), key=lambda z: float(z))
    print("primitive frame max radius", max_xrad, flush=True)
    print("exact two-Tate graph: PASS", flush=True)

    # Complete Gamma and scalar part, without contact serialization.
    spec = importlib.util.spec_from_file_location(
        "d147", HERE / "114_d_147_hurwitz_gamma_arb.py"
    )
    d147 = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(d147)
    gamma = d147.exact_gamma_block(N, DPS, T)
    m0 = arb.pi().log() + arb.const_euler() + arb.pi() / 2 + 3 * arb(2).log()
    Bbase = X.transpose() * gamma * X - m0 * (X.transpose() * X)
    bad_base = [(i, j) for i in range(N - 2) for j in range(N - 2)
                if not Bbase[i, j].is_finite()]
    if bad_base:
        print("first nonfinite Gamma-base entry", bad_base[0],
              Bbase[bad_base[0][0], bad_base[0][1]], flush=True)
    assert not bad_base, f"nonfinite Gamma projection entries: {bad_base[:3]}"
    max_brad = max((Bbase[i, j].rad() for i in range(N - 2)
                    for j in range(N - 2)), key=lambda z: float(z))
    max_bmid = max((abs(Bbase[i, j].mid()) for i in range(N - 2)
                    for j in range(N - 2)), key=lambda z: float(z))
    print("Gamma-base max midpoint/radius", max_bmid, max_brad, flush=True)
    print("exact Gamma projection complete", flush=True)

    D = sub(X, 0, N, 0, ND)
    S = sub(X, 0, N, ND, N - 2)

    # The serialized contact enclosure is used on the safe block through a
    # Loewner error budget, not through a dependency-heavy interval matrix
    # product.  The delicate rows remain wholly native.
    contact_file = np.load(
        os.environ.get("D199_CONTACT", "/tmp/d185_contacts6_arb.npz")
    )
    assert int(contact_file["endpoint"]) == 6
    contact_center_array = contact_file["C"]
    contact_radius_array = contact_file["R"]
    Ccenter = arb_mat(N, N)
    for i in range(N):
        for j in range(N):
            Ccenter[i, j] = arb(repr(float(contact_center_array[i, j])))
    Bss_center = (
        sub(Bbase, ND, N - 2, ND, N - 2)
        + S.transpose() * Ccenter * S
    )

    # If |C-Ccenter|<=R entrywise, then
    # |S^*(C-Ccenter)S|<=|S|^T R |S| entrywise.  Its maximum row sum is an
    # operator-norm bound.  Binary summation is inflated by 1e-6, vastly
    # above Higham's gamma_200 while remaining far below the safe gap.
    Sc = center(S)
    Sr = np.array([[float(S[i, j].rad()) + abs(np.spacing(Sc[i, j])) / 2
                    for j in range(NS)] for i in range(N)])
    Sabs = np.abs(Sc) + Sr
    Rcontact = np.nextafter(
        contact_radius_array + np.abs(np.spacing(contact_center_array)) / 2,
        np.inf,
    )
    Econtact = Sabs.T @ Rcontact @ Sabs
    delta_float = np.nextafter(
        1.000001 * float(np.max(np.sum(Econtact, axis=1))), np.inf
    )
    delta = arb(repr(delta_float))
    print("safe contact Loewner error delta", delta, flush=True)
    Bss = Bss_center
    for i in range(NS):
        Bss[i, i] -= delta

    # Native contact applied only to the two delicate vectors supplies all
    # entries needed for the exact Schur complement.
    CD = native_contact_on_delicate(D)
    Bdd = sub(Bbase, 0, ND, 0, ND) + D.transpose() * CD
    Bds = sub(Bbase, 0, ND, ND, N - 2) + CD.transpose() * S

    # One whitening of the safe block.  P is merely an exact decimal
    # congruence chosen from the midpoint Cholesky factor.
    css = center(Bss)
    css = (css + css.T) / 2
    print("safe centre first eigenvalues", np.linalg.eigvalsh(css)[:5], flush=True)
    L = np.linalg.cholesky(css)
    P0 = np.linalg.inv(L.T)
    P = arb_mat([[arb(repr(float(P0[i, j]))) for j in range(NS)]
                 for i in range(NS)])
    Qsafe = P.transpose() * Bss * P
    gershgorin_positive(Qsafe, "safe196")

    C = Bds * P
    K = Bdd - C * Qsafe.inv() * C.transpose()
    K = (K + K.transpose()) / 2
    print("delicate Schur block", K, flush=True)
    det = K.det()
    print("delicate leading entry", K[0, 0], flush=True)
    print("delicate determinant", det, flush=True)
    assert K[0, 0].lower() > 0
    assert det.lower() > 0

    np.savez(
        os.environ.get("D199_SAVE", "/tmp/t6_whitened_native_schur.npz"),
        primitive_eigenvalues=evals,
        safe_gershgorin=np.array([float(x.lower()) for x in
                                  gershgorin_positive(Qsafe, "safe196-repeat")]),
        schur_center=center(K),
        schur_radius=np.array([[float(K[i, j].rad()) for j in range(ND)]
                               for i in range(ND)]),
        schur_det=np.array([float(det.mid()), float(det.rad())]),
    )
    print("PASS T6 V200: exact jets, native delicate contacts, stable Schur", flush=True)


if __name__ == "__main__":
    main()
