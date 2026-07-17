#!/usr/bin/env python3
"""Audit displacement-generator moments of the canonical shell response w."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_011_loewner_identity_probe import symbols
from P76_051_jacobi_minor_probe import bordered


def run():
    mp.mp.dps = 100
    max_modes = 9
    Hmax, idxmax, L = build_mp(6, max_modes, 100)
    z0 = mp.mpc(0, 1)
    print("P76.055 shell response generator moments")
    print("N ||w|| |1Tw|/||w|| |sTw|/(||s||||w||) shellForce/norm")
    for n_modes in (5, 6, 7, 8):
        off_big = max_modes - (n_modes + 1)
        Hbig = Hmax[off_big : Hmax.rows - off_big, off_big : Hmax.cols - off_big]
        idxbig = idxmax[off_big : len(idxmax) - off_big]
        B0 = bordered(Hbig, idxbig, L, z0)
        G = B0 ** -1
        last = B0.rows - 1
        C = [0, last]
        D = [0, B0.rows - 2]
        R0 = mp.matrix([[G[i, j] for j in D] for i in C])
        a = mp.matrix([G[i, last] for i in C])
        selected = mp.matrix(B0.rows, 2)
        for i in range(B0.rows):
            for j in range(2):
                selected[i, j] = G[i, D[j]]
        w = selected * (R0 ** -1) * a
        modes = idxbig[1:-1] + [idxbig[-1]]
        svec = mp.matrix([symbols(2 * mp.pi * k / L, L, mp.mpf(6))[0] for k in modes])
        wn = mp.sqrt(mp.fsum(abs(w[j]) ** 2 for j in range(w.rows)))
        sn = mp.sqrt(mp.fsum(abs(svec[j]) ** 2 for j in range(svec.rows)))
        one_moment = abs(mp.fsum(w[j] for j in range(w.rows))) / wn
        s_moment = abs((svec.T * w)[0]) / (sn * wn)
        forcing = B0 * w
        fn = mp.sqrt(mp.fsum(abs(forcing[j]) ** 2 for j in range(forcing.rows))) / wn
        print(
            f"{n_modes:2d} {mp.nstr(wn,8):>10} {mp.nstr(one_moment,8):>14}"
            f" {mp.nstr(s_moment,8):>20} {mp.nstr(fn,8):>17}"
        )


if __name__ == "__main__":
    run()
