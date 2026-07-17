#!/usr/bin/env python3
import numpy as np
from numpy.polynomial import Polynomial


C0 = np.array(
    [
        3.50034658e-04,
        -2.17140111e-02,
        5.06181442e-01,
        -2.40156964e00,
        2.26914715e00,
        1.58637022e01,
        -2.58235301e01,
        -4.46069341e01,
        8.28566327e01,
    ]
)

C1 = np.array(
    [
        4.02779245e-04,
        -2.42377245e-02,
        5.83688352e-01,
        -1.70388740e00,
        -6.15242967e-02,
        5.77037550e00,
        3.65678602e00,
        -4.46225038e00,
        -3.59935285e00,
    ]
)

# Small buffer for between-grid LP slack. Costs less than 0.002 in the tested dimensions.
C0[0] += 2.0e-5
C1[0] += 2.0e-5


def min_on_interval(coeff, shift_coeff, lo, hi):
    poly = Polynomial(coeff) - Polynomial(shift_coeff)
    candidates = [lo, hi]
    for z in poly.deriv().roots():
        if abs(z.imag) < 1e-9 and lo <= z.real <= hi:
            candidates.append(float(z.real))
    vals = [(x, float(poly(x))) for x in candidates]
    return min(vals, key=lambda t: t[1]), vals


def certify(name, coeff, a):
    r2 = (1.0 - a) ** 2
    neg_shift = np.zeros(len(coeff))
    neg_shift[2] = 1.0
    pos_shift = np.zeros(len(coeff))
    pos_shift[2] = r2
    neg_min, _ = min_on_interval(coeff, neg_shift, -1.0, 0.0)
    pos_min, _ = min_on_interval(coeff, pos_shift, 0.0, 1.0)
    print(f"{name}:")
    print(f"  min p(u)-u^2 on [-1,0]       at {neg_min[0]:+.12f}: {neg_min[1]:+.12e}")
    print(f"  min p(u)-r^2 u^2 on [0,1]    at {pos_min[0]:+.12f}: {pos_min[1]:+.12e}")
    if neg_min[1] < -1e-8 or pos_min[1] < -1e-8:
        raise SystemExit(f"{name} failed")


def run():
    print("E72.192 low-moment envelope certificate")
    certify("K0 degree-8 envelope", C0, 0.70)
    certify("K1 degree-8 envelope", C1, 0.60)
    print("certificate: degree-8 envelopes majorize split energy on [-1,1]")


if __name__ == "__main__":
    run()
