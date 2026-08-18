#!/usr/bin/env python3
"""Finite-dimensional Douglas--Julia identities for D.169."""
import numpy as np


def psqrt(a):
    d, u = np.linalg.eigh((a + a.T) / 2)
    return u @ np.diag(np.sqrt(np.maximum(d, 0))) @ u.T


def main():
    rng = np.random.default_rng(169)
    u, _ = np.linalg.qr(rng.normal(size=(5, 5)))
    v, _ = np.linalg.qr(rng.normal(size=(5, 5)))
    C = u @ np.diag([.99, .8, .5, .2, .0]) @ v.T
    D = np.eye(5) - C.T @ C
    Dc = np.eye(5) - C @ C.T
    Dh = psqrt(D)
    Dch = psqrt(Dc)
    J = np.block([[C, Dch], [Dh, -C.T]])
    assert np.linalg.norm(J.T @ J - np.eye(10)) < 2e-13

    W = rng.normal(size=(5, 2)) / 4
    z = Dh @ W
    c = np.linalg.norm(W, 2) ** 2
    assert np.linalg.eigvalsh(c * D - z @ z.T).min() > -2e-13
    block = np.block([[c * np.eye(2), z.T], [z, D]])
    assert np.linalg.eigvalsh(block).min() > -2e-13
    assert np.linalg.eigvalsh(c * np.eye(2) - z.T @ np.linalg.inv(D) @ z).min() > -2e-13

    # Same ambient norm, arbitrarily large Douglas factor norm.
    vals = []
    for eps in (1e-2, 1e-6, 1e-10):
        De = np.diag([eps, 1.0])
        ze = np.array([[1.0], [0.0]])
        vals.append(float((ze.T @ np.linalg.inv(De) @ ze)[0, 0]))
    assert vals[2] > 1e9 and vals[0] < 101
    print("defect factor norms squared =", vals)
    print("D169 Douglas--Julia defect-range gate: PASS")


if __name__ == "__main__":
    main()
