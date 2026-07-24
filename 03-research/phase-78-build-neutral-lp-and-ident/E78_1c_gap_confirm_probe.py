#!/usr/bin/env python3
"""E78.1c - Confirm the ground-gap dichotomy at N=16 and tie to BTG energy.

For each build and section N:
  - parity-split, report even/odd sector bottoms and the global ground gap g_N;
  - g_N^zeta expected to keep collapsing geometrically; g_N^plant expected to
    plateau near 0.137.
Also reports the ratio g_N / g_{N-2} to expose geometric vs plateau behaviour.

Reuses P76.002 build_mp verbatim.
"""

import sys
import mpmath as mp

sys.path.insert(
    0,
    "/Users/dt/riemann/03-research/phase-76-normalized-adjugate-arithmetic-lock",
)
from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E78_1b_low_spectrum_probe import parity_blocks, low  # noqa: E402

PLANT = ("14.134725141734693790", "0.30", "5.0")


def run():
    dps = 70
    mp.mp.dps = dps
    for build_name, planted in (("zeta", None), ("plant", PLANT)):
        print(f"===== build={build_name} dps={dps} =====")
        prev = None
        for n_modes in (12, 14, 16):
            H, idx, L = build_mp(6, n_modes, dps, planted=planted)
            He, Ho = parity_blocks(H, idx)
            ve, _ = mp.eigsy(He)
            vo, _ = mp.eigsy(Ho)
            e0 = low(ve, 1)[0]
            o0 = low(vo, 1)[0]
            allb = sorted([e0, o0])
            ground = allb[0]
            second = allb[1]
            gap = second - ground
            ratio = "" if prev is None else mp.nstr(gap / prev, 6)
            print(
                f"N={n_modes:2d} even0={mp.nstr(e0,8)} odd0={mp.nstr(o0,8)} "
                f"ground={mp.nstr(ground,8)} gap={mp.nstr(gap,8)} gap/prevgap={ratio}"
            )
            prev = gap


if __name__ == "__main__":
    run()
