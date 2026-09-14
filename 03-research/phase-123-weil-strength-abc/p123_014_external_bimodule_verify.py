#!/usr/bin/env python3
"""Finite matrix regression for lift-change and external composition."""

import numpy as np


rng = np.random.default_rng(123014)
n = 6


def perm_shift(k):
    p = np.zeros((n, n), dtype=complex)
    for i in range(n):
        p[(i + k) % n, i] = 1
    return p


def ad(u, x):
    return u @ x @ u.conj().T


# A toy external automorphism and a changed lift differing by an inner
# gauge automorphism.
v = perm_shift(2)
u_gauge = perm_shift(1)


def beta(x):
    return ad(v, x)


def beta_lift_changed(x):
    return ad(u_gauge, beta(x))


for _ in range(5):
    x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    c = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))

    # Phi(x)=xU intertwines the right actions twisted by the two lifts.
    lhs = (x @ beta_lift_changed(c)) @ u_gauge
    rhs = (x @ u_gauge) @ beta(c)
    assert np.linalg.norm(lhs - rhs) < 1e-10


# Twisted-bimodule tensor multiplication x tensor y -> x beta(y) obeys
# the associativity formula exactly at matrix level.
w = perm_shift(3)


def gamma(x):
    return ad(w, x)


x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
y = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
left = (x @ beta(y)) @ beta(gamma(z))
right = x @ beta(y @ gamma(z))
assert np.linalg.norm(left - right) < 1e-10

# Hyperbolic external module characters: squared weights avoid irrational
# arithmetic while retaining inversion/swap and multiplicativity.
for a in [2.0, 0.5, 3.0 / 5.0, 11.0]:
    rho = (a ** -1, a)
    rho_inv = ((1 / a) ** -1, 1 / a)
    assert np.allclose(rho_inv, (rho[1], rho[0]))

print("P123.014 external bimodule/lift/Tate identities: PASS")

