#!/usr/bin/env python3
import numpy as np
from numpy.polynomial import Polynomial

from E72_252_homogeneous_lm8_extended_stress import R0_DEG8, R1_DEG8


BUFFER = 1.5e-3


def min_on_interval(poly, lo, hi):
    candidates = [lo, hi]
    for z in poly.deriv().roots():
        if abs(z.imag) < 1.0e-8 and lo <= z.real <= hi:
            candidates.append(float(z.real))
    vals = [(x, float(poly(x))) for x in candidates]
    vals.sort(key=lambda t: t[1])
    return vals[0], vals[:8]


def certify_r(name, r_coeff, a):
    r = Polynomial(r_coeff)
    neg_diff = r - Polynomial([1.0])
    pos_diff = r - Polynomial([(1.0 - a) ** 2])
    neg_min, neg_vals = min_on_interval(neg_diff, -1.0, 0.0)
    pos_min, pos_vals = min_on_interval(pos_diff, 0.0, 1.0)
    print(f"{name}:")
    print(f"  R(0)={r(0.0):+.12e} R'(0)={r.deriv()(0.0):+.12e}")
    print(f"  min R(u)-1 on [-1,0]        at {neg_min[0]:+.12f}: {neg_min[1]:+.12e}")
    print(f"  min R(u)-r^2 on [0,1]       at {pos_min[0]:+.12f}: {pos_min[1]:+.12e}")
    print("  closest neg candidates:")
    for x, y in neg_vals[:4]:
        print(f"    {x:+.12f} {y:+.12e}")
    print("  closest pos candidates:")
    for x, y in pos_vals[:4]:
        print(f"    {x:+.12f} {y:+.12e}")
    return neg_min[1] >= -1.0e-8 and pos_min[1] >= -1.0e-8


def run():
    print("E72.256 strict homogeneous LM8 certificate")
    print(f"Checks R inequalities directly with BUFFER={BUFFER:.1e} added to R(0).")
    r0 = R0_DEG8.copy()
    r1 = R1_DEG8.copy()
    r0[0] += BUFFER
    r1[0] += BUFFER
    ok0 = certify_r("K0 strict Rdeg8", r0, 0.70)
    ok1 = certify_r("K1 strict Rdeg8", r1, 0.60)
    print(f"overall {'PASS' if ok0 and ok1 else 'FAIL'}")


if __name__ == "__main__":
    run()
