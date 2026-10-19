#!/usr/bin/env python3
"""Numerical falsifier for R161_026's Gamma-pole/Hankel identities."""

import numpy as np
from numpy.polynomial.legendre import leggauss


def source(t):
    return (1.0 + 0.3 * t - 0.2 * t**2) * np.cos(1.7 * t)


def moment_energy(T, delta, order=500, modes=180):
    nodes, weights = leggauss(order)
    t = T * nodes
    w = T * weights
    f = source(t)
    indices = np.arange(1, modes + 1, dtype=float)
    a = 2.0 * indices + 0.5
    moments = np.exp(-np.outer(a, t)) @ (w * f)
    damping = np.exp(-2.0 * a * (T + delta))
    b = np.sum(damping * np.abs(moments) ** 2)
    d = np.sum(a * damping * np.abs(moments) ** 2)
    return b, d, t, w, f


def hankel_energy(T, delta, t, w, f):
    v = 2.0 * T + 2.0 * delta + t[:, None] + t[None, :]
    r = np.exp(-2.0 * v)
    k = np.exp(-2.5 * v) / (1.0 - r)
    # -d/dv [exp(-5v/2)/(1-exp(-2v))]
    minus_k_prime = k * (2.5 + 2.0 * r / (1.0 - r))
    fw = w * f
    b = np.vdot(fw, k @ fw).real
    d = np.vdot(fw, minus_k_prime @ fw).real
    return b, d


def main():
    T = 0.91
    delta = 0.23
    b_mom, d_mom, t, w, f = moment_energy(T, delta)
    b_han, d_han = hankel_energy(T, delta, t, w, f)

    h = 2.0e-5
    b_plus, *_ = moment_energy(T, delta + h)
    b_minus, *_ = moment_energy(T, delta - h)
    derivative = (b_plus - b_minus) / (2.0 * h)

    delta0 = np.log(2.0) / 4.0
    _, d_delta0, *_ = moment_energy(T, delta0)

    # R161_025 uses 2^{-m}; this differs from exp(-2 a_m delta0)
    # by the constant 2^{1/4}.
    nodes, weights = leggauss(500)
    tt = T * nodes
    ww = T * weights
    ff = source(tt)
    indices = np.arange(1, 181, dtype=float)
    aa = 2.0 * indices + 0.5
    kk = np.exp(-np.outer(aa, tt)) @ (ww * ff)
    d_old = np.sum(2.0 ** (-indices) * aa * np.exp(-2.0 * aa * T) * kk**2)

    checks = {
        "B moment/Hankel": abs(b_mom - b_han) / max(1.0, abs(b_mom)),
        "D moment/Hankel": abs(d_mom - d_han) / max(1.0, abs(d_mom)),
        "dB=-2D": abs(derivative + 2.0 * d_mom) / max(1.0, abs(2.0 * d_mom)),
        "old=2^(1/4) shifted": abs(d_old - 2.0 ** 0.25 * d_delta0)
        / max(1.0, abs(d_old)),
    }

    for name, error in checks.items():
        print(f"{name}: relative error {error:.3e}")
        assert error < 2.0e-8, name
    print("PASS: Gamma residue energy equals the Hankel boundary derivative")


if __name__ == "__main__":
    main()
