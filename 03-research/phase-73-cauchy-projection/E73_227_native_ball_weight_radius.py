#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import GAMMA, LOG4PI, build, primes_upto  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_210_psi_asymptotic_budget import psi_remainder_bound, trigamma_remainder_bound  # noqa: E402
from E73_215_native_ball_entry_probe import CBall, ball_exp, ball_exp_int, ball_y_exp_int, point  # noqa: E402
from E73_223_coefficient_ball_budget import coefficient_maps, cauchy_rows, projector  # noqa: E402


mp.mp.dps = 100


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def add_unit_mode_integral(total, omega, kind, alpha, L, unit, sign=1):
    a = point(mp.mpf(alpha) + 1j * mp.mpf(str(float(omega))), unit)
    if kind == "c":
        return total + sign * ball_exp_int(a, L, unit)
    return total + sign * ball_y_exp_int(a, L, unit)


def native_finite_weight_ball(omega, kind, L, lam, digits=100, R=80):
    unit = mp.power(10, -digits)
    om = mp.mpf(str(float(omega)))
    total = CBall(0, 0)
    total = add_unit_mode_integral(total, om, kind, mp.mpf("0.5"), L, unit, sign=1)
    total = add_unit_mode_integral(total, om, kind, mp.mpf("-0.5"), L, unit, sign=1)

    wra = CBall(0, 0)
    for r in range(R):
        wra = add_unit_mode_integral(wra, om, kind, -(2 * r + mp.mpf("0.5")), L, unit, sign=1)
        if kind == "c":
            wra -= ball_exp_int(point(-(2 * r + mp.mpf("1.0")), unit), L, unit)

    wr = wra
    if kind == "c":
        wr += point(mp.mpf("0.5") * (LOG4PI + GAMMA), unit)
        wr += point(mp.mpf("0.5") * mp.log(mp.tanh(mp.mpf(L) / 2)), unit)
    arch_elem = total - wr

    prime = CBall(0, 0)
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        q = p
        k = 1
        while q <= maxn:
            y = mp.mpf(str(k * lp))
            weight = point(mp.mpf(str(lp)) * mp.power(q, mp.mpf("-0.5")), unit)
            phase = ball_exp(point(1j * om, unit) * point(y, unit), unit)
            sample = phase if kind == "c" else point(y, unit) * phase
            prime += weight * sample
            if q > maxn // p:
                break
            q *= p
            k += 1
    return arch_elem - prime


def native_weight_radius(omega, kind, L, lam, csec=mp.mpf("1e6"), digits=100, R=80, K=16):
    finite_ball = native_finite_weight_ball(omega, kind, L, lam, digits=digits, R=R)
    om = mp.mpf(str(float(omega)))
    z = mp.mpf(R) + mp.mpf("0.25") - 0.5j * om
    if kind == "c":
        psi = mp.mpf("0.5") * (
            psi_remainder_bound(mp.mpf(R) + mp.mpf("0.5"), K) + psi_remainder_bound(z, K)
        )
        exp_tail = mp.e ** (-(2 * R + mp.mpf("0.5")) * mp.mpf(L))
    else:
        psi = mp.mpf("0.25") * trigamma_remainder_bound(z, K)
        exp_tail = (1 + mp.mpf(L)) * mp.e ** (-(2 * R + mp.mpf("0.5")) * mp.mpf(L))
    return finite_ball.r + csec * psi + exp_tail, finite_ball.r, csec * psi, exp_tail


def bexp(z, L):
    return math.log(max(float(abs(z)), 1e-300)) / math.log(L)


def run():
    print("E73.227 native-ball weight radius budget")
    print("Replaces E73.225 finite-rounding heuristic by native complex-ball propagation.")
    print(" lam     L    N gamma row csec maxFinWB maxPsiWB totalB scaleB ratio")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for row_id in range(2):
                const_map, linear_map = coefficient_maps(q[row_id], idx, d, L)
                for csec in [mp.mpf(1), mp.mpf("1e6")]:
                    total = mp.mpf("0")
                    scale = mp.mpf("0")
                    max_fin = mp.mpf("0")
                    max_psi = mp.mpf("0")
                    cache = {}
                    for kind, maps in [("c", const_map), ("l", linear_map)]:
                        for om, vec in maps.items():
                            key = (float(om), kind, str(csec))
                            rad, finite, psi, _exp = cache.setdefault(
                                key, native_weight_radius(om, kind, L, lam, csec=csec)
                            )
                            coeff = mp.mpf(str(abs(vec @ eta)))
                            total += coeff * rad
                            scale += coeff
                            max_fin = max(max_fin, finite)
                            max_psi = max(max_psi, psi)
                    print(
                        f"{lam:4d} {L:7.3f} {n_modes:4d} {gamma:7.2f} {row_id:3d}"
                        f" {mp.nstr(csec, 3):>4s} {bexp(max_fin, L):9.2f}"
                        f" {bexp(max_psi, L):9.2f} {bexp(total, L):7.2f}"
                        f" {bexp(scale, L):7.2f} {float(total / max(scale, mp.mpf('1e-300'))):8.1e}"
                    )


if __name__ == "__main__":
    run()
