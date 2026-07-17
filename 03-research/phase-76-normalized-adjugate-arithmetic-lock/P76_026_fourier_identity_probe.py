#!/usr/bin/env python3
"""Verify the exact Fourier representation of the boundary characteristic."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import entire_transfer, right_transfer_data


def run():
    mp.mp.dps = 60
    H, idx, L = build_mp(6, 9, 60)
    db, inner, x = right_transfer_data(H, idx)
    y = [x[j] for j in range(x.rows)] + [mp.mpf(-1)]
    mesh_idx = inner + [db]

    def density(t):
        return -mp.fsum(
            mp.mpf("0.5") * ((-1) ** n) * yn * mp.exp(-2j * mp.pi * n * t / L)
            for n, yn in zip(mesh_idx, y)
        )

    print("P76.026 Fourier identity")
    for z in (mp.mpf("0"), mp.mpf("3.25"), mp.mpc("4.0", "0.3"), -mp.mpc(0, "1.0")):
        direct = entire_transfer(z, db, inner, x, L)
        integral = mp.quad(lambda t: mp.exp(1j * z * t) * density(t), [-L / 2, L / 2])
        scale = max(mp.mpf(1), abs(direct), abs(integral))
        print(mp.nstr(z, 8), mp.nstr(abs(direct - integral) / scale, 8))


if __name__ == "__main__":
    run()
