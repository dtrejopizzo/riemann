#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import setup, sample_packet  # noqa: E402


def weighted_d2_gate(ts, bs, c):
    pos = ts >= 0
    xs = ts[pos]
    b = bs[pos]
    h = xs[1] - xs[0]
    b1 = np.gradient(b, h)
    b2 = np.gradient(b1, h)
    weight = np.exp(c * xs)
    d0 = float(np.trapezoid(weight * np.abs(b), xs))
    d1 = float(np.trapezoid(weight * np.abs(b1), xs))
    d2 = float(np.trapezoid(weight * np.abs(b2), xs))
    return d0, d1, d2, d0 + d1 + d2


def run():
    print("E72.389 D2BV packet probe")
    print(" lam    L    dim     M      D0        D1        D2        D2BV      scaled4   scaled5")
    z = 0.25 + 1.0j
    c = 0.65
    sigma = z.real
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16), (14, 18)]:
        idx, d, L, xi = setup(lam, n_modes)
        ts, bs = sample_packet(z, idx, d, L, xi, 8001)
        d0, d1, d2, total = weighted_d2_gate(ts, bs, c)
        scale4 = math.exp((c + sigma) * L) * max(L, 1.0) ** 4
        scale5 = math.exp((c + sigma) * L) * max(L, 1.0) ** 5
        print(
            f"{lam:4.0f} {L:6.3f} {len(idx):5d} {int(np.max(np.abs(idx))):5d} "
            f"{d0:9.3e} {d1:9.3e} {d2:9.3e} {total:9.3e} "
            f"{total/scale4:9.3e} {total/scale5:9.3e}"
        )


if __name__ == "__main__":
    run()
