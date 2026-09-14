#!/usr/bin/env python3
"""Finite matrix regression checks for the source effective cone."""

import numpy as np


rng = np.random.default_rng(123010)


def square(x):
    return x.conj().T @ x


xs = [rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5)) for _ in range(4)]
positive = sum((square(x) for x in xs), np.zeros((5, 5), dtype=complex))

assert np.linalg.norm(positive - positive.conj().T) < 1e-11
assert np.linalg.eigvalsh(positive).min() > -1e-11

# Unitary multiplier conjugation preserves sums of squares.
q, _ = np.linalg.qr(rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5)))
conjugated = q.conj().T @ positive @ q
factorized = sum((square(x @ q) for x in xs), np.zeros((5, 5), dtype=complex))
assert np.linalg.norm(conjugated - factorized) < 1e-10
assert np.linalg.eigvalsh(conjugated).min() > -1e-11

# Properness of the finite faithful model.
if np.linalg.eigvalsh(positive).max() > 1e-9:
    assert np.linalg.eigvalsh(-positive).min() < -1e-9

print("P123.010 source square cone/conjugation/properness: PASS")

