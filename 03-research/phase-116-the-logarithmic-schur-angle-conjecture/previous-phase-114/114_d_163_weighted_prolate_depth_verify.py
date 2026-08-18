#!/usr/bin/env python3
"""Checks for D.163 weighted prolate/depth identities.

This verifies the finite Poisson grouping of every p^k, the exact Gamma
recentering, the rank-two Tate-deflated Paley--Wiener kernel, and the
minimum-norm comparison/annular Birman--Schwinger identities in directed
finite-dimensional models.  It does not assume the norm-one inequality.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


mp.mp.dps = 70


def pw_kernel(T: mp.mpf, z: complex, w: complex) -> complex:
    d = z - mp.conj(w)
    if abs(d) < mp.mpf("1e-60"):
        return T / mp.pi
    return mp.sin(T * d) / (mp.pi * d)


def main() -> None:
    # Exact finite Frobenius-depth / Poisson grouping.
    T = mp.mpf("2.37")
    tau = mp.mpf("1.184")
    for p in (2, 3, 5, 7, 11):
        K = int(mp.floor(2 * T / mp.log(p)))
        if not K:
            continue
        rho = 1 / mp.sqrt(p)
        z = rho * mp.e ** (1j * tau * mp.log(p))
        finite_poisson = 2 * mp.re(z * (1 - z**K) / (1 - z))
        depth_sum = 2 * mp.fsum(
            rho**k * mp.cos(k * tau * mp.log(p))
            for k in range(1, K + 1)
        )
        assert abs(finite_poisson - depth_sum) < mp.mpf("1e-65")

    # Exact 5/4 -> 1/4 Gamma recurrence after Tate centering.
    beta = mp.log(mp.pi) - mp.digamma(mp.mpf("1.25"))
    for x in (mp.mpf("0"), mp.mpf(".3"), mp.mpf("2.1"), mp.mpf("17")):
        h = mp.re(mp.digamma(mp.mpf("1.25") + 0.5j * x)) - mp.digamma(
            mp.mpf("1.25")
        )
        centred = h - beta - 1 / (x * x + mp.mpf(".25"))
        direct = mp.re(mp.digamma(mp.mpf(".25") + 0.5j * x)) - mp.log(mp.pi)
        assert abs(centred - direct) < mp.mpf("1e-64")

    # Tate-deflated reproducing kernel vanishes at both evaluation points.
    a = [0.5j, -0.5j]
    gram = mp.matrix([[pw_kernel(T, x, y) for y in a] for x in a])
    gram_inv = gram**-1

    def k0(z, w):
        kz = mp.matrix([[pw_kernel(T, z, x) for x in a]])
        # Column K(a_i,w) is the conjugate transpose of K(w,a_i).
        kaw = mp.matrix([[pw_kernel(T, x, w)] for x in a])
        return pw_kernel(T, z, w) - (kz * gram_inv * kaw)[0]

    for z in (-3.2, -0.7, 0.0, 1.4, 4.1):
        assert abs(k0(z, a[0])) < mp.mpf("1e-60")
        assert abs(k0(z, a[1])) < mp.mpf("1e-60")

    real_nodes = [mp.mpf(-2), mp.mpf(-.3), mp.mpf(.8), mp.mpf(2.7)]
    deflated_gram = mp.matrix(
        [[mp.re(k0(x, y)) for y in real_nodes] for x in real_nodes]
    )
    eig = mp.eigsy(deflated_gram, eigvals_only=True)
    assert min(eig) > -mp.mpf("1e-60")

    # Minimum-norm comparison and weighted generalized eigenvalue.
    rng = np.random.default_rng(163)
    X = rng.normal(size=(11, 5)) + 1j * rng.normal(size=(11, 5))
    Y = rng.normal(size=(9, 5)) + 1j * rng.normal(size=(9, 5))
    R = X.conj().T @ X
    load = Y.conj().T @ Y
    C = Y @ np.linalg.solve(R, X.conj().T)
    assert np.linalg.norm(C @ X - Y) < 1.0e-12
    evals_R, vecs_R = np.linalg.eigh(R)
    Rmhalf = (vecs_R / np.sqrt(evals_R)) @ vecs_R.conj().T
    kappa = np.linalg.eigvalsh(Rmhalf @ load @ Rmhalf)[-1]
    assert abs(np.linalg.norm(C, 2) ** 2 - kappa) < 2.0e-12

    # Annular Schur/Birman--Schwinger equivalence on a positive reference.
    Z = rng.normal(size=(8, 8))
    reference = Z.T @ Z + 2.0 * np.eye(8)
    J = rng.normal(size=(3, 8))
    weight = 0.17
    schur_k = weight * J @ np.linalg.solve(reference, J.T)
    lhs = reference - weight * J.T @ J
    # Congruence says precisely: lhs >= 0 iff top(schur_k) <= 1.
    sign_lhs = np.linalg.eigvalsh(lhs)[0] >= -1.0e-12
    sign_k = np.linalg.eigvalsh(schur_k)[-1] <= 1 + 1.0e-12
    assert sign_lhs == sign_k

    print("D163 weighted prolate/depth identities: PASS")
    print("beta =", mp.nstr(beta, 22))
    print("Tate-deflated kernel minimum eigenvalue =", mp.nstr(min(eig), 8))
    print("finite comparison norm^2 =", f"{kappa:.12g}")
    print("annular top capacity =", f"{np.linalg.eigvalsh(schur_k)[-1]:.12g}")


if __name__ == "__main__":
    main()
