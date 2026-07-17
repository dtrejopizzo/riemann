#!/usr/bin/env python3
"""Sample boundary-kernel norms along cutoffs with increasing N/L."""

import math

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import entire_transfer, right_transfer_data
from P76_027_boundary_kernel_probe import boundary_density, riemann_phi


def trap(values, step):
    return step * (sum(values) - (values[0] + values[-1]) / 2)


def run():
    mp.mp.dps = 50
    s0 = mp.mpf("0.5")
    xi0 = mp.mpf("0.5") * s0 * (s0 - 1) * mp.pi ** (-s0 / 2) * mp.gamma(s0 / 2) * mp.zeta(s0)
    print("P76.028 cofinal sampled boundary-kernel audit")
    print("lambda N N/L L1sample WL1sample oddSample edgeSample")
    for lam in (4, 6, 8):
        Lf = 2 * math.log(lam)
        n_modes = max(8, math.ceil(Lf * Lf + 4))
        H, idx, L = build_mp(lam, n_modes, 50)
        db, inner, x = right_transfer_data(H, idx)
        y = [x[j] for j in range(x.rows)] + [mp.mpf(-1)]
        mesh_idx = inner + [db]
        mass = entire_transfer(mp.mpf(0), db, inner, x, L)
        count = 401
        ts = [-L / 2 + L * j / (count - 1) for j in range(count)]
        step = L / (count - 1)
        gs = [boundary_density(t, mesh_idx, y, L, mass) for t in ts]
        targets = [riemann_phi(t) / xi0 for t in ts]
        errors = [abs(g - target) for g, target in zip(gs, targets)]
        weighted = [mp.exp(mp.mpf("0.6") * abs(t)) * e for t, e in zip(ts, errors)]
        odd = [abs(gs[j] - gs[-1-j]) / 2 for j in range(count)]
        edge = [abs(gs[j]) if abs(ts[j]) >= L / 2 - mp.mpf("0.15") else 0 for j in range(count)]
        print(
            f"{lam:6d} {n_modes:2d} {mp.nstr(n_modes/L,6):>8}"
            f" {mp.nstr(trap(errors,step),8):>10} {mp.nstr(trap(weighted,step),8):>10}"
            f" {mp.nstr(trap(odd,step),8):>10} {mp.nstr(trap(edge,step),8):>10}"
        )


if __name__ == "__main__":
    run()
