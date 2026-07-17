#!/usr/bin/env python3
"""Compare the exact boundary Fourier density with Riemann's Xi kernel."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import entire_transfer, right_transfer_data


def riemann_phi(u):
    u = abs(u)
    total = mp.mpf(0)
    for n in range(1, 80):
        term = (
            2 * mp.pi**2 * n**4 * mp.exp(9 * u)
            - 3 * mp.pi * n**2 * mp.exp(5 * u)
        ) * mp.exp(-mp.pi * n**2 * mp.exp(4 * u))
        total += term
        if n > 3 and abs(term) < mp.mpf("1e-70"):
            break
    return total


def boundary_density(t, mesh_idx, y, L, mass):
    raw = -mp.fsum(
        mp.mpf("0.5") * ((-1) ** n) * yn * mp.exp(-2j * mp.pi * n * t / L)
        for n, yn in zip(mesh_idx, y)
    )
    return raw / mass


def run():
    mp.mp.dps = 60
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 60)
    s0 = mp.mpf("0.5")
    xi0 = mp.mpf("0.5") * s0 * (s0 - 1) * mp.pi ** (-s0 / 2) * mp.gamma(s0 / 2) * mp.zeta(s0)

    print("P76.027 boundary density vs normalized Riemann kernel, lambda=6")
    print("N      L1err       WL1(.6)     oddL1       edgeMass")
    for n_modes in (6, 7, 8, 9, 10, 11, 12):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        db, inner, x = right_transfer_data(H, idx)
        y = [x[j] for j in range(x.rows)] + [mp.mpf(-1)]
        mesh_idx = inner + [db]
        mass = entire_transfer(mp.mpf(0), db, inner, x, L)

        def g(t):
            return boundary_density(t, mesh_idx, y, L, mass)

        def target(t):
            return riemann_phi(t) / xi0

        intervals = [-L / 2, -mp.mpf("0.75"), 0, mp.mpf("0.75"), L / 2]
        l1 = mp.quad(lambda t: abs(g(t) - target(t)), intervals)
        wl1 = mp.quad(lambda t: mp.exp(mp.mpf("0.6") * abs(t)) * abs(g(t) - target(t)), intervals)
        odd = mp.quad(lambda t: abs(g(t) - g(-t)) / 2, [0, mp.mpf("0.75"), L / 2]) * 2
        edge = mp.quad(lambda t: abs(g(t)), [-L / 2, -L / 2 + mp.mpf("0.15")])
        edge += mp.quad(lambda t: abs(g(t)), [L / 2 - mp.mpf("0.15"), L / 2])
        # Add the omitted target tail; it is tiny here but makes the metric global.
        tail = 2 * mp.quad(lambda t: target(t), [L / 2, mp.mpf("2.5")])
        l1 += tail
        wl1 += 2 * mp.quad(
            lambda t: mp.exp(mp.mpf("0.6") * t) * target(t),
            [L / 2, mp.mpf("2.5")],
        )
        print(
            f"{n_modes:2d} {mp.nstr(l1,9):>12} {mp.nstr(wl1,9):>12}"
            f" {mp.nstr(odd,9):>12} {mp.nstr(edge,9):>12}"
        )


if __name__ == "__main__":
    run()
