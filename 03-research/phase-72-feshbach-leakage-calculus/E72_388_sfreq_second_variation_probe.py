#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import setup, sample_packet  # noqa: E402


def second_variation(ts, bs, c):
    vals = np.exp(c * ts) * bs
    h = ts[1] - ts[0]
    deriv = np.gradient(vals, h)
    # Split at zero to include the derivative jump explicitly.
    neg = ts < 0
    pos = ts > 0
    var_neg = float(np.sum(np.abs(np.diff(deriv[neg])))) if np.sum(neg) > 2 else 0.0
    var_pos = float(np.sum(np.abs(np.diff(deriv[pos])))) if np.sum(pos) > 2 else 0.0
    iz = np.argmin(np.abs(ts))
    jump = abs(deriv[iz + 1] - deriv[iz - 1]) if 0 < iz < len(ts) - 1 else 0.0
    return var_neg + var_pos + jump


def run():
    print("E72.388 SFREQ second-variation probe")
    print(" lam    L      V2          V2scaled    T=e^L      V2/T")
    z = 0.25 + 1.0j
    c = 0.65
    sigma = z.real
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16), (14, 18)]:
        idx, d, L, xi = setup(lam, n_modes)
        ts, bs = sample_packet(z, idx, d, L, xi, 6001)
        v2 = second_variation(ts, bs, c)
        scale = math.exp((c + sigma) * L) * max(L, 1.0) ** 3
        T = math.exp(L)
        print(f"{lam:4.0f} {L:7.3f} {v2:11.3e} {v2/scale:11.3e} {T:10.1f} {v2/T:11.3e}")


if __name__ == "__main__":
    run()
