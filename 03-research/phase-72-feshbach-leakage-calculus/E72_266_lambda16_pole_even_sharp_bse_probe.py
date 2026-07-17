#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_193_lm8_asrp_probe import split_energy  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


TARGET = 0.9409


def contribution(vals, a):
    return np.where(vals >= 0.0, ((1.0 - a) ** 2) * vals * vals, vals * vals)


def summarize(vals, a, name):
    contrib = contribution(vals, a)
    order = np.argsort(contrib)[::-1]
    print(f"{name}: n={len(vals)} op={max(abs(vals)):.12e} energy={np.sum(contrib):.12e}")
    print(f"  neg_count={np.sum(vals < 0)} pos_count={np.sum(vals >= 0)}")
    print("  top contributions: idx eigen contribution")
    for j in order[:12]:
        print(f"    {j:3d} {vals[j]:+.16e} {contrib[j]:.16e}")


def run():
    print("E72.266 lambda=16 pole-even sharp BSE probe")
    print("Finite transition-window spectral certificate target.")
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(16, 40)
    k0, k1 = two_blocks(16, idx, L, eb, c_model, 0.60)
    v0 = eigvalsh(k0)
    v1 = eigvalsh(k1)
    e0 = float(np.sum(contribution(v0, 0.70)))
    e1 = float(np.sum(contribution(v1, 0.60)))
    total = e0 + e1
    print(f"L={L:.16e} dim={len(v0)} poleEvenLeak={even_leak:.3e}")
    print(f"E0={e0:.16e}")
    print(f"E1={e1:.16e}")
    print(f"BSE={total:.16e}")
    print(f"TARGET={TARGET:.16e}")
    print(f"slack={TARGET-total:+.16e}")
    summarize(v0, 0.70, "K0")
    summarize(v1, 0.60, "K1")


if __name__ == "__main__":
    run()
