#!/usr/bin/env python3
"""Audit the exact inhomogeneous Loewner remainder for the coupled generator."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_011_loewner_identity_probe import symbols
from P76_012_loewner_remainder_probe import lagrange_value


def coupled_data(H, idx, L, lam):
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    inner = idx[1:-1]
    nodes = [2 * mp.pi * n / L for n in inner]
    node_symbols = [symbols(d, L, lam) for d in nodes]
    svec = mp.matrix([data[0] for data in node_symbols])
    one = mp.matrix([1 for _ in nodes])
    u = A ** -1 * svec
    v = A ** -1 * one
    db = 2 * mp.pi * idx[-1] / L
    sb = symbols(db, L, lam)[0]
    Rb = mp.diag([1 / (d - db) for d in nodes])
    source = svec - sb * one
    p = (v.T * Rb * source)[0]
    q = (u.T * Rb * source)[0]
    aa = 2 / L + 4 * p / L**2
    bb = -2 * sb / L - 4 * q / L**2
    h = aa * u + bb * v
    f = aa * svec + bb * one
    return mu, nodes, node_symbols, h, f


def run():
    mp.mp.dps = 80
    lam = mp.mpf(6)
    print("P76.043 coupled inhomogeneous Loewner remainder, z=i")
    print("N          |R|        |LCIh|       |LIf/2|          |E|       nodeErr")
    for n_modes in (5, 6, 7, 8, 9):
        H, idx, L = build_mp(6, n_modes, 80)
        mu, nodes, node_symbols, h, f = coupled_data(H, idx, L, lam)
        z = mp.mpc(0, 1)
        sz, cz, _ = symbols(z, L, lam)
        hz = mp.fsum(h[j] / (z - nodes[j]) for j in range(len(nodes)))
        ms = mp.fsum(node_symbols[j][0] * h[j] / (z - nodes[j]) for j in range(len(nodes)))
        rvalue = sz * hz - ms
        ih = lagrange_value(z, nodes, [h[j] for j in range(len(nodes))])
        iff = lagrange_value(z, nodes, [f[j] for j in range(len(nodes))])
        homogeneous = L * (cz - mu / 2) * ih
        source_term = L * iff / 2
        residual = rvalue - homogeneous + source_term

        # Verify the nodal law directly from the Loewner action.
        worst_node = mp.mpf(0)
        for j, dj in enumerate(nodes):
            loew = node_symbols[j][2] * h[j]
            for k, dk in enumerate(nodes):
                if j != k:
                    loew += (node_symbols[j][0] - node_symbols[k][0]) * h[k] / (dj - dk)
            expected = L * (node_symbols[j][1] - mu / 2) * h[j] - L * f[j] / 2
            worst_node = max(worst_node, abs(loew - expected))
        print(
            f"{n_modes:2d} {mp.nstr(abs(rvalue),9):>12} {mp.nstr(abs(homogeneous),9):>13}"
            f" {mp.nstr(abs(source_term),9):>13} {mp.nstr(abs(residual),9):>12}"
            f" {mp.nstr(worst_node,5):>13}"
        )


if __name__ == "__main__":
    run()
