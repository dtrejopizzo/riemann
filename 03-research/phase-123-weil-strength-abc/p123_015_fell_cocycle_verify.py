#!/usr/bin/env python3
"""Finite group-extension regression for the lift-twisted Fell product."""


# 0 -> {0,5} -> Z/10 -> Z/5 -> 0.
MOD_G = 10
MOD_Q = 5


def section(u):
    return u % MOD_Q


def cocycle(u, v):
    return (section(u) + section(v) - section((u + v) % MOD_Q)) % MOD_G


for u in range(MOD_Q):
    for v in range(MOD_Q):
        assert cocycle(u, v) in (0, 5)
        for w in range(MOD_Q):
            lhs = (cocycle(u, v) + cocycle((u + v) % MOD_Q, w)) % MOD_G
            rhs = (cocycle(v, w) + cocycle(u, (v + w) % MOD_Q)) % MOD_G
            assert lhs == rhs


# A changed section differs by a gauge-valued 1-cochain.
def b(u):
    return 5 if u in (2, 3) else 0


def section2(u):
    return (section(u) + b(u)) % MOD_G


def cocycle2(u, v):
    return (section2(u) + section2(v) - section2((u + v) % MOD_Q)) % MOD_G


for u in range(MOD_Q):
    for v in range(MOD_Q):
        coboundary = (b(u) + b(v) - b((u + v) % MOD_Q)) % MOD_G
        assert cocycle2(u, v) == (cocycle(u, v) + coboundary) % MOD_G

        # In the quotient representation every gauge value is one, so both
        # cocycles disappear and ordinary convolution remains.
        assert cocycle(u, v) in (0, 5)
        assert cocycle2(u, v) in (0, 5)

print("P123.015 Fell cocycle/splitting/gauge-quotient identities: PASS")

