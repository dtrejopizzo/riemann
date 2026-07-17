#!/usr/bin/env python3
from fractions import Fraction
import sys

import numpy as np
from numpy.linalg import eigvalsh
from numpy.polynomial import Polynomial

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_193_lm8_asrp_probe import split_energy  # noqa: E402
from E72_248_homogeneous_lm8_probe import eval_hom  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


TARGET = 0.9409
WINDOWS = [(20, 48), (24, 56)]

# E72.263, R degree 8 stable pole-even fit.
R0_BASE = np.array(
    [
        9.9902884873e-01,
        -1.9514292338e00,
        -1.8253403605e01,
        -8.5297082916e00,
        2.6356605613e02,
        2.1058093811e02,
        -1.5488260398e03,
        -7.4663940140e02,
        3.2475435437e03,
    ]
)

R1_BASE = np.array(
    [
        9.9874673938e-01,
        -2.5131201071e00,
        -1.3197719671e01,
        2.1797818446e01,
        1.2775742495e02,
        -1.3558570957e02,
        -3.4870221311e02,
        1.9700896920e02,
        3.2577191198e02,
    ]
)


def min_on_interval(poly, lo, hi):
    candidates = [lo, hi]
    for z in poly.deriv().roots():
        if abs(z.imag) < 1.0e-8 and lo <= z.real <= hi:
            candidates.append(float(z.real))
    vals = [(x, float(poly(x))) for x in candidates]
    vals.sort(key=lambda t: t[1])
    return vals[0]


def certify_float(r_coeff, a):
    r = Polynomial(r_coeff)
    neg = min_on_interval(r - Polynomial([1.0]), -1.0, 0.0)
    pos = min_on_interval(r - Polynomial([(1.0 - a) ** 2]), 0.0, 1.0)
    return neg, pos


def collect_rows():
    rows = []
    for lam, n_modes in WINDOWS:
        idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, eb, c_model, 0.60)
        v0 = eigvalsh(k0)
        v1 = eigvalsh(k1)
        exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)
        rows.append((lam, L, exact, v0, v1))
        print(f"prepared lambda={lam:.0f} exact={exact:.6e}", flush=True)
    return rows


def run():
    print("E72.264 pole-even stable rational LM8 probe")
    print("Rationalizes/certifies the E72.263 R-degree-8 stable envelope for lambda>=20 tests.")
    rows = collect_rows()
    print("buffer decimals min0neg min0pos min1neg min1pos worstEnv worstLam pass")
    for buffer in [0.002, 0.003, 0.005, 0.008]:
        base0 = R0_BASE.copy()
        base1 = R1_BASE.copy()
        base0[0] += buffer
        base1[0] += buffer
        for decimals in [8, 6]:
            r0 = np.round(base0, decimals=decimals)
            r1 = np.round(base1, decimals=decimals)
            n0, p0 = certify_float(r0, 0.70)
            n1, p1 = certify_float(r1, 0.60)
            ok_interval = n0[1] >= -1e-9 and p0[1] >= -1e-9 and n1[1] >= -1e-9 and p1[1] >= -1e-9
            worst = (-np.inf, None)
            out_rows = []
            for lam, L, exact, v0, v1 in rows:
                env = eval_hom(v0, 0.90, r0) + eval_hom(v1, 0.60, r1)
                worst = max(worst, (env, lam), key=lambda x: x[0])
                out_rows.append((lam, exact, env, TARGET - env))
            ok_stress = worst[0] < TARGET
            print(
                f"{buffer:.3f} {decimals:2d} {n0[1]:+.6e} {p0[1]:+.6e} "
                f"{n1[1]:+.6e} {p1[1]:+.6e} {worst[0]:.6e} {worst[1]:3.0f} "
                f"{'YES' if ok_interval and ok_stress else 'NO'}",
                flush=True,
            )
            for lam, exact, env, slack in out_rows:
                print(f"  {lam:3.0f} exact={exact:.6e} env={env:.6e} slack={slack:+.6e}")
            print("  R0=" + " ".join(f"{c:.{decimals}f}" for c in r0))
            print("  R1=" + " ".join(f"{c:.{decimals}f}" for c in r1))


if __name__ == "__main__":
    run()
