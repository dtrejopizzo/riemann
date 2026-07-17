#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import setup, sample_packet  # noqa: E402


def bilateral_transform(ts, bs, tau):
    vals = np.exp(1j * tau * ts) * bs
    return np.trapezoid(vals, ts)


def second_variation_unweighted(ts, bs):
    h = ts[1] - ts[0]
    deriv = np.gradient(bs, h)
    neg = ts < 0
    pos = ts > 0
    var_neg = float(np.sum(np.abs(np.diff(deriv[neg])))) if np.sum(neg) > 2 else 0.0
    var_pos = float(np.sum(np.abs(np.diff(deriv[pos])))) if np.sum(pos) > 2 else 0.0
    iz = np.argmin(np.abs(ts))
    jump = abs(deriv[iz + 1] - deriv[iz - 1]) if 0 < iz < len(ts) - 1 else 0.0
    return var_neg + var_pos + jump


def run():
    print("E72.394 outside-zero high-frequency probe")
    print(" lam     L       V2        tau      |F(i tau)|   tau^2|F|/V2")
    z = 0.25 + 1.0j
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        idx, d, L, xi = setup(lam, n_modes)
        ts, bs = sample_packet(z, idx, d, L, xi, 12001)
        v2 = second_variation_unweighted(ts, bs)
        for mult in (8, 12, 16):
            tau = mult * math.exp(L / 2.0)
            f = bilateral_transform(ts, bs, tau)
            scaled = tau * tau * abs(f) / max(v2, 1e-30)
            print(f"{lam:4.0f} {L:7.3f} {v2:9.3e} {tau:9.2f} {abs(f):12.3e} {scaled:12.3e}")


if __name__ == "__main__":
    run()
