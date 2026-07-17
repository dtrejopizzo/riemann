#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import setup, sample_packet, packet_B  # noqa: E402


def run():
    print("E72.384 BV-K packet reduction probe")
    print(" lam    L       BVdirect    DBVbound    ratio   scaledDBV")
    z = 0.25 + 1.0j
    c = 0.65
    sigma = z.real
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16), (14, 18)]:
        idx, d, L, xi = setup(lam, n_modes)
        ts, bs = sample_packet(z, idx, d, L, xi, 4001)
        vals = np.exp(c * ts) * bs
        bv_direct = float(np.sum(np.abs(np.diff(vals))))
        pos = ts >= 0
        xs = ts[pos]
        bpos = bs[pos]
        h = xs[1] - xs[0]
        deriv = np.gradient(bpos, h)
        dbv = 2 * abs(packet_B(0.0, z, idx, d, L, xi)) + 2 * float(
            np.trapezoid(np.exp(c * xs) * np.abs(deriv), xs)
        )
        ratio = bv_direct / dbv if dbv else float("nan")
        scaled = dbv / (math.exp((c + sigma) * L) * max(L, 1.0))
        print(f"{lam:4.0f} {L:7.3f} {bv_direct:11.3e} {dbv:11.3e} {ratio:7.3f} {scaled:11.3e}")


if __name__ == "__main__":
    run()
