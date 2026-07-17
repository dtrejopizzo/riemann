#!/usr/bin/env python3
import numpy as np
from numpy.polynomial import Polynomial


C0 = np.array(
    [
        2.12200031e-04,
        -1.87315328e-02,
        5.64917316e-01,
        -2.60009842e00,
        -8.38952814e-01,
        2.40721725e01,
        1.49065920e01,
        -1.31292043e02,
        -1.10226327e02,
        2.64094802e02,
        2.83941640e02,
    ]
)
C0[0] += 2.0e-5

C1 = np.array(
    [
        1.76903019e-04,
        -1.49388103e-02,
        5.50772702e-01,
        -3.06215769e00,
        2.24212256e00,
        4.54706077e01,
        -2.43435904e01,
        -4.32440178e02,
        -1.19363939e02,
        1.68337525e03,
        1.80123037e03,
    ]
)
C1[0] += 2.0e-5


def min_on_interval(coeff, shift_coeff, lo, hi):
    poly = Polynomial(coeff) - Polynomial(shift_coeff)
    der = poly.deriv()
    candidates = [lo, hi]
    for z in der.roots():
        if abs(z.imag) < 1e-8 and lo <= z.real <= hi:
            candidates.append(float(z.real))
    vals = [(x, float(poly(x))) for x in candidates]
    return min(vals, key=lambda t: t[1]), vals


def certify(name, coeff, a, m_bound):
    r2 = (1.0 - a) ** 2
    # p(t) >= t^2 on [-M,0].
    neg_shift = np.zeros(len(coeff))
    neg_shift[2] = 1.0
    # p(t) >= r^2 t^2 on [0,M].
    pos_shift = np.zeros(len(coeff))
    pos_shift[2] = r2
    neg_min, neg_vals = min_on_interval(coeff, neg_shift, -m_bound, 0.0)
    pos_min, pos_vals = min_on_interval(coeff, pos_shift, 0.0, m_bound)
    print(f"{name}: interval=[-{m_bound},{m_bound}], a={a}")
    print(f"  min p(t)-t^2 on [-M,0]      at {neg_min[0]: .12f}: {neg_min[1]: .12e}")
    print(f"  min p(t)-r^2 t^2 on [0,M]   at {pos_min[0]: .12f}: {pos_min[1]: .12e}")
    if neg_min[1] < -1e-7 or pos_min[1] < -1e-7:
        raise SystemExit(f"{name} majorant failed")


def run():
    print("E72.172 polynomial majorant certificate")
    certify("K0", C0, 0.70, 0.90)
    certify("K1", C1, 0.60, 0.60)
    print("certificate: both fixed polynomials majorize the split quadratic on their intervals")


if __name__ == "__main__":
    run()
