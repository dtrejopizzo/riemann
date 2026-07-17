#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh
from numpy.polynomial import Polynomial

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_193_lm8_asrp_probe import split_energy  # noqa: E402
from E72_252_homogeneous_lm8_extended_stress import R0_DEG8, R1_DEG8, eval_hom  # noqa: E402
from E72_256_strict_homogeneous_lm8_certificate import BUFFER  # noqa: E402


TARGET = 0.9409
WINDOWS = [(16, 40), (32, 72), (56, 120)]


def min_on_interval(poly, lo, hi):
    candidates = [lo, hi]
    for z in poly.deriv().roots():
        if abs(z.imag) < 1.0e-8 and lo <= z.real <= hi:
            candidates.append(float(z.real))
    vals = [(x, float(poly(x))) for x in candidates]
    vals.sort(key=lambda t: t[1])
    return vals[0]


def certify_r(r_coeff, a):
    r = Polynomial(r_coeff)
    neg_min = min_on_interval(r - Polynomial([1.0]), -1.0, 0.0)
    pos_min = min_on_interval(r - Polynomial([(1.0 - a) ** 2]), 0.0, 1.0)
    return neg_min, pos_min


def collect_rows():
    rows = []
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        v0 = eigvalsh(k0)
        v1 = eigvalsh(k1)
        exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)
        rows.append((lam, exact, v0, v1))
        print(f"prepared lambda={lam:.0f}", flush=True)
    return rows


def stress_env(r0, r1, prepared):
    worst = (-np.inf, None)
    rows = []
    for lam, exact, v0, v1 in prepared:
        env = eval_hom(v0, 0.90, r0) + eval_hom(v1, 0.60, r1)
        worst = max(worst, (env, lam), key=lambda x: x[0])
        rows.append((lam, exact, env, TARGET - env))
    return worst, rows


def run():
    print("E72.258 rational strict LM8 probe")
    print("Rounding strict buffered R coefficients to decimal rational grids.")
    base0 = R0_DEG8.copy()
    base1 = R1_DEG8.copy()
    base0[0] += BUFFER
    base1[0] += BUFFER
    prepared = collect_rows()
    print("decimals min0neg min0pos min1neg min1pos worstEnv worstLam pass")
    for decimals in [12, 10, 8, 6]:
        r0 = np.round(base0, decimals=decimals)
        r1 = np.round(base1, decimals=decimals)
        n0, p0 = certify_r(r0, 0.70)
        n1, p1 = certify_r(r1, 0.60)
        ok_interval = n0[1] >= -1.0e-8 and p0[1] >= -1.0e-8 and n1[1] >= -1.0e-8 and p1[1] >= -1.0e-8
        worst, rows = stress_env(r0, r1, prepared)
        ok_stress = worst[0] < TARGET
        print(
            f"{decimals:8d} {n0[1]:+.6e} {p0[1]:+.6e} {n1[1]:+.6e} {p1[1]:+.6e} "
            f"{worst[0]:.6e} {worst[1]:3.0f} {'YES' if ok_interval and ok_stress else 'NO'}",
            flush=True,
        )
        for lam, exact, env, slack in rows:
            print(f"  {lam:3.0f} exact={exact:.6e} env={env:.6e} slack={slack:+.6e}", flush=True)
        print("  R0=" + " ".join(f"{c:.{decimals}f}" for c in r0))
        print("  R1=" + " ".join(f"{c:.{decimals}f}" for c in r1))


if __name__ == "__main__":
    run()
