#!/usr/bin/env python3
import sys
import cmath
import numpy as np
from scipy.integrate import quad

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402


def phi(a, L):
    if abs(a) < 1e-10:
        return L + 0.5 * a * L * L
    return (cmath.exp(a * L) - 1.0) / a


def phi_array(a, L):
    a = np.asarray(a, dtype=complex)
    out = (np.exp(a * L) - 1.0) / a
    small = np.abs(a) < 1e-10
    if np.any(small):
        out[small] = L + 0.5 * a[small] * L * L
    return out


def h0(z, d, xi):
    return np.sum(xi / (z + 1j * d))


def hplus(z, y, d, xi):
    return np.sum(xi * np.exp(1j * d * y) / (z + 1j * d))


def hminus(z, y, d, xi):
    return np.sum(xi * np.exp(-1j * d * y) / (z + 1j * d))


def b_packet(z, y, L, d, xi):
    return 1j * (
        (cmath.exp(z * (L - y)) - cmath.exp(z * y)) * h0(z, d, xi)
        - hplus(z, y, d, xi)
        + cmath.exp(z * L) * hminus(z, y, d, xi)
    )


def mellin_quad(z, w, L, d, xi):
    def real_part(y):
        return (cmath.exp(w * y) * b_packet(z, y, L, d, xi)).real

    def imag_part(y):
        return (cmath.exp(w * y) * b_packet(z, y, L, d, xi)).imag

    re, _ = quad(real_part, 0.0, L, limit=300, epsabs=1e-10, epsrel=1e-10)
    im, _ = quad(imag_part, 0.0, L, limit=300, epsabs=1e-10, epsrel=1e-10)
    return re + 1j * im


def mellin_closed(z, w, L, d, xi):
    hz = h0(z, d, xi)
    term0 = 1j * hz * (cmath.exp(z * L) * phi(w - z, L) - phi(w + z, L))
    termp = -1j * np.sum(xi * phi_array(w + 1j * d, L) / (z + 1j * d))
    termm = 1j * cmath.exp(z * L) * np.sum(xi * phi_array(w - 1j * d, L) / (z + 1j * d))
    return term0 + termp + termm


def run():
    print("E73.071 packet Mellin formula verifier")
    print("Compares quadrature of M_B with the closed formula from E73.070.")
    print(" lam     L       z        w        absErr      relErr")
    tests = [
        (16, 20, 0.20 + 14.134725j, 0.10 + 3.0j),
        (16, 20, 0.20 + 21.022040j, -0.10 + 2.0j),
        (20, 24, 0.20 + 14.134725j, 0.00 + 4.0j),
        (24, 28, 0.20 + 21.022040j, 0.15 + 1.0j),
    ]
    for lam, n_modes, z, w in tests:
        d, L, xi, _ = setup_exact(lam, n_modes)
        q = mellin_quad(z, w, L, d, xi)
        c = mellin_closed(z, w, L, d, xi)
        err = abs(q - c)
        rel = err / max(abs(q), abs(c), 1e-300)
        print(f"{lam:4d} {L:7.3f} {z.imag:8.3f} {w.real:+.2f}{w.imag:+.2f}i {err:11.3e} {rel:11.3e}")


if __name__ == "__main__":
    run()
