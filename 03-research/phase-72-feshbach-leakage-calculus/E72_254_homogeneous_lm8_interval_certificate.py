#!/usr/bin/env python3
import numpy as np
from numpy.polynomial import Polynomial


R0_DEG8 = np.array(
    [
        9.9869861120e-01,
        -2.6126797623e00,
        -1.9804311573e01,
        1.2299851184e01,
        2.9969895233e02,
        1.4347637522e01,
        -1.7974700048e03,
        -1.9279016455e02,
        3.7159804900e03,
    ]
)

R1_DEG8 = np.array(
    [
        9.9923237079e-01,
        -1.5396362647e00,
        -8.7556751919e00,
        -5.5335239414e00,
        4.6182864473e01,
        8.4054305754e01,
        3.0021738439e00,
        -7.7401145547e01,
        -4.0848595496e01,
    ]
)


def p_coeff_from_r(r_coeff):
    out = np.zeros(len(r_coeff) + 2)
    out[2:] = r_coeff
    return out


def min_on_interval(poly, lo, hi):
    candidates = [lo, hi, 0.0] if lo <= 0.0 <= hi else [lo, hi]
    for z in poly.deriv().roots():
        if abs(z.imag) < 1.0e-8 and lo <= z.real <= hi:
            candidates.append(float(z.real))
    vals = [(x, float(poly(x))) for x in candidates]
    vals.sort(key=lambda t: t[1])
    return vals[0], vals[:8]


def certify(name, r_coeff, a):
    p = Polynomial(p_coeff_from_r(r_coeff))
    neg_target = Polynomial([0.0, 0.0, 1.0])
    pos_target = Polynomial([0.0, 0.0, (1.0 - a) ** 2])
    neg_diff = p - neg_target
    pos_diff = p - pos_target
    neg_min, neg_vals = min_on_interval(neg_diff, -1.0, 0.0)
    pos_min, pos_vals = min_on_interval(pos_diff, 0.0, 1.0)
    print(f"{name}:")
    print(f"  P(0)={p(0.0):+.12e} P'(0)={p.deriv()(0.0):+.12e}")
    print(f"  min P(u)-u^2 on [-1,0]       at {neg_min[0]:+.12f}: {neg_min[1]:+.12e}")
    print(f"  min P(u)-r^2u^2 on [0,1]     at {pos_min[0]:+.12f}: {pos_min[1]:+.12e}")
    print("  closest neg candidates:")
    for x, y in neg_vals[:4]:
        print(f"    {x:+.12f} {y:+.12e}")
    print("  closest pos candidates:")
    for x, y in pos_vals[:4]:
        print(f"    {x:+.12f} {y:+.12e}")
    return neg_min[1] >= -1.0e-8 and pos_min[1] >= -1.0e-8


def run():
    print("E72.254 homogeneous LM8 interval certificate")
    print("Checks E72.248 P degree 10 homogeneous majorants on full intervals.")
    ok0 = certify("K0 homogeneous Pdeg10", R0_DEG8, 0.70)
    ok1 = certify("K1 homogeneous Pdeg10", R1_DEG8, 0.60)
    print(f"overall {'PASS' if ok0 and ok1 else 'FAIL'}")


if __name__ == "__main__":
    run()
