#!/usr/bin/env python3
"""Resolve the three signed terms in the canonical Loewner remainder."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_011_loewner_identity_probe import symbols


GAMMA_TEXT = "14.134725141734693790"


def lagrange_value(z, nodes, values):
    total = mp.mpc(0)
    for j, node in enumerate(nodes):
        cardinal = mp.mpf(1)
        for k, other in enumerate(nodes):
            if k != j:
                cardinal *= (z - other) / (node - other)
        total += values[j] * cardinal
    return total


def run_case(n_modes):
    H, idx, L = build_mp(6, n_modes, 60)
    vals, vecs = mp.eigsy(H)
    mu = vals[0]
    xi = vecs[:, 0]
    nodes = [2 * mp.pi * n / L for n in idx]
    node_symbols = [symbols(d, L, mp.mpf(6)) for d in nodes]
    gamma = mp.mpf(GAMMA_TEXT)
    sg, _, _ = symbols(gamma, L, mp.mpf(6))

    c = sum(xi[j] / (gamma - nodes[j]) for j in range(len(nodes)))
    ms = sum(node_symbols[j][0] * xi[j] / (gamma - nodes[j]) for j in range(len(nodes)))
    nodal_r = [L * (node_symbols[j][1] - mu / 2) * xi[j] for j in range(len(nodes))]
    interp = lagrange_value(gamma, nodes, nodal_r)
    rvalue = sg * c - ms
    remainder = rvalue - interp
    closure = ms + interp + remainder

    print(
        f"{n_modes:2d} {mp.nstr(abs(c),8):>12} {mp.nstr(abs(ms),8):>12}"
        f" {mp.nstr(abs(interp),8):>12} {mp.nstr(abs(remainder),8):>12}"
        f" {mp.nstr(abs(closure),8):>12} {mp.nstr(abs(sg*c),8):>12}"
    )


def run():
    mp.mp.dps = 60
    print("P76.012 canonical Loewner remainder")
    print("N          |c|         |mS|         |IR|        |D G|       |sum|       |S c|")
    for n_modes in (3, 4, 5, 6, 8, 9):
        run_case(n_modes)


if __name__ == "__main__":
    run()
