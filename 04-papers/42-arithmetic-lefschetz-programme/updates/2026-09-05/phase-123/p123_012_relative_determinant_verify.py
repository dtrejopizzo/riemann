#!/usr/bin/env python3
"""Finite trace-class determinant regression for P123.012."""

import numpy as np


rng = np.random.default_rng(123012)


def expm_hermitian(a):
    vals, vecs = np.linalg.eigh(a)
    return (vecs * np.exp(vals)) @ vecs.conj().T


for _ in range(8):
    x = rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5))
    a = (x + x.conj().T) / 7
    y = rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5))
    b = (y + y.conj().T) / 9

    # det(exp A)=exp(Tr A).
    assert abs(np.linalg.det(expm_hermitian(a)) - np.exp(np.trace(a))) < 1e-9

    # Multiplicativity of Fredholm determinants of exponentials does not
    # require A and B to commute.
    lhs = np.linalg.det(expm_hermitian(a) @ expm_hermitian(b))
    rhs = np.exp(np.trace(a) + np.trace(b))
    assert abs(lhs - rhs) < 1e-8

    # Similarity/gauge invariance of the trace determinant.
    u, _ = np.linalg.qr(rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5)))
    gauged = u @ a @ u.conj().T
    assert abs(np.trace(gauged) - np.trace(a)) < 1e-10

print("P123.012 trace exponential/additivity/gauge identities: PASS")

