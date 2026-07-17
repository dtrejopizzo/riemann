#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import setup, sample_packet  # noqa: E402


def weighted_bv(ts, bs, c):
    vals = np.exp(c * ts) * bs
    return float(np.sum(np.abs(np.diff(vals))))


def run():
    print("E72.383 natural-height BV probe")
    print(" lam    L      sigma    c      BVc        scaledBV    horizScale")
    z = 0.25 + 1.0j
    sigma = z.real
    c = 0.65
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16), (14, 18)]:
        idx, d, L, xi = setup(lam, n_modes)
        ts, bs = sample_packet(z, idx, d, L, xi, 3001)
        bv = weighted_bv(ts, bs, c)
        scaled = bv / (math.exp((c + sigma) * L) * max(L, 1.0))
        # Horizontal after T=e^L, ignoring log T and powers:
        horiz = bv / math.exp(L)
        print(f"{lam:4.0f} {L:7.3f} {sigma:8.3f} {c:6.3f} {bv:10.3e} {scaled:10.3e} {horiz:10.3e}")


if __name__ == "__main__":
    run()
