#!/usr/bin/env python3
import sys

import numpy as np
from scipy.special import polygamma

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import GAMMA, LOG4PI, primes_upto  # noqa: E402
from E73_195_finite_frequency_certificate_probe import functional_scalar  # noqa: E402


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def exp_int(a, L):
    if abs(a) < 1e-12:
        return L + 0j
    return (np.exp(a * L) - 1.0) / a


def y_exp_int(a, L):
    if abs(a) < 1e-12:
        return 0.5 * L * L + 0j
    return (np.exp(a * L) * (a * L - 1.0) + 1.0) / (a * a)


def y2_exp_int(a, L):
    if abs(a) < 1e-12:
        return L**3 / 3.0 + 0j
    ea = np.exp(a * L)
    return ea * (L * L / a - 2 * L / (a * a) + 2 / (a**3)) - 2 / (a**3)


def odd_square_tail(r_terms):
    return 0.25 * float(polygamma(1, r_terms + 0.5))


def odd_cube_tail(r_terms):
    return -0.0625 * float(polygamma(2, r_terms + 0.5))


def arch_W(omega, L, r_terms=2500, accel=True):
    # This is the Dirichlet representative used by functional_scalar:
    # W02 - int e^(y/2)B(y)/(2sinh y) dy.  The full Weil representative
    # differs on the W-block by terms proportional to B(0), hence by a
    # constant gauge on W_omega when restricted to sum c_omega=0 packets.
    b0 = 1.0 + 0j
    bp0 = 1j * omega
    bpp0 = -(omega * omega)
    c1 = bp0 + 0.5 * b0
    c2 = 0.5 * bpp0 + 0.5 * bp0 + 0.125 * b0
    w02 = exp_int(0.5 + 1j * omega, L) + exp_int(-0.5 + 1j * omega, L)
    wra = 0j
    for r in range(r_terms):
        wra += exp_int(-(2 * r + 0.5) + 1j * omega, L)
    if accel:
        wra += c1 * odd_square_tail(r_terms)
        wra += 2.0 * c2 * odd_cube_tail(r_terms)
    return w02 - wra


def arch_V(omega, L, r_terms=2500, accel=True):
    # B(y)=y exp(i omega y).  B(0)=0, B'(0)=1, B''(0)=2 i omega.
    b0 = 0.0 + 0j
    bp0 = 1.0 + 0j
    bpp0 = 2j * omega
    c1 = bp0 + 0.5 * b0
    c2 = 0.5 * bpp0 + 0.5 * bp0 + 0.125 * b0
    w02 = y_exp_int(0.5 + 1j * omega, L) + y_exp_int(-0.5 + 1j * omega, L)
    wra = 0j
    for r in range(r_terms):
        wra += y_exp_int(-(2 * r + 0.5) + 1j * omega, L)
        # b0=0, so the subtraction term vanishes.
    if accel:
        wra += c1 * odd_square_tail(r_terms)
        wra += 2.0 * c2 * odd_cube_tail(r_terms)
    wr = wra
    return w02 - wr


def prime_W(omega, L, lam):
    total = 0j
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        n = p
        k = 1
        while n <= maxn:
            y = k * lp
            total += lp * n ** -0.5 * np.exp(1j * omega * y)
            if n > maxn // p:
                break
            n *= p
            k += 1
    return total


def prime_V(omega, L, lam):
    total = 0j
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        n = p
        k = 1
        while n <= maxn:
            y = k * lp
            total += lp * n ** -0.5 * y * np.exp(1j * omega * y)
            if n > maxn // p:
                break
            n *= p
            k += 1
    return total


def closed_W(omega, L, lam):
    return arch_W(omega, L) - prime_W(omega, L, lam)


def closed_V(omega, L, lam):
    return arch_V(omega, L) - prime_V(omega, L, lam)


def run():
    print("E73.287 closed weight formula probe")
    print("Compares closed arch/prime formulas for W,V against functional_scalar basis evaluation.")
    print("Werr is raw; WgErr subtracts the constant W-gauge, irrelevant when sum c=0.")
    print(" lam     L omega WerrB WgErrB VerrB WB VB archWB archVB primeWB primeVB")
    for lam in [12, 16, 20]:
        L = 2.0 * np.log(lam)
        freqs = [0.0, 2.0 * np.pi / L, 4.0 * np.pi / L, -2.0 * np.pi / L]
        w_diffs = []
        for omega in freqs:
            w_diffs.append(
                closed_W(omega, L, lam)
                - functional_scalar(lambda y, o=omega: np.exp(1j * o * y), 1j * omega, L, lam)
            )
        w_gauge = sum(w_diffs) / len(w_diffs)
        for omega in freqs:
            w_closed = closed_W(omega, L, lam)
            v_closed = closed_V(omega, L, lam)
            w_ref = functional_scalar(lambda y, o=omega: np.exp(1j * o * y), 1j * omega, L, lam)
            v_ref = functional_scalar(lambda y, o=omega: y * np.exp(1j * o * y), 1.0 + 0j, L, lam)
            print(
                f"{lam:4d} {L:7.3f} {omega:7.3f}"
                f" {bexp(w_closed-w_ref,L):6.2f} {bexp(w_closed-w_ref-w_gauge,L):7.2f}"
                f" {bexp(v_closed-v_ref,L):6.2f}"
                f" {bexp(w_closed,L):6.2f} {bexp(v_closed,L):6.2f}"
                f" {bexp(arch_W(omega,L),L):7.2f} {bexp(arch_V(omega,L),L):7.2f}"
                f" {bexp(prime_W(omega,L,lam),L):8.2f} {bexp(prime_V(omega,L,lam),L):8.2f}"
            )


if __name__ == "__main__":
    run()
