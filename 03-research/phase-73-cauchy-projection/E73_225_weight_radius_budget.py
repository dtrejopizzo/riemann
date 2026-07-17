#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build, primes_upto  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_201_mp_finite_assembly_probe import mp_exp_int, mp_y_exp_int  # noqa: E402
from E73_210_psi_asymptotic_budget import psi_remainder_bound, trigamma_remainder_bound  # noqa: E402
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


def unit_mode_work_size(omega, kind, L, lam, R=80):
    om = mp.mpf(str(float(omega)))
    total_abs = mp.mpf("0")
    ops = 0
    for alpha in [mp.mpf("0.5"), mp.mpf("-0.5")]:
        a = alpha + 1j * om
        total_abs += abs(mp_exp_int(a, L)) if kind == "c" else abs(mp_y_exp_int(a, L))
        ops += 1
    for r in range(R):
        a = -(2 * r + mp.mpf("0.5")) + 1j * om
        total_abs += abs(mp_exp_int(a, L)) if kind == "c" else abs(mp_y_exp_int(a, L))
        ops += 1
        if kind == "c":
            total_abs += abs(mp_exp_int(-(2 * r + mp.mpf("1.0")), L))
            ops += 1
    if kind == "c":
        total_abs += abs(mp.mpf("0.5") * mp.log(mp.tanh(mp.mpf(L) / 2)))
        total_abs += abs(mp.mpf("1"))
        ops += 2
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        q = p
        k = 1
        while q <= maxn:
            y = mp.mpf(str(k * lp))
            weight = mp.mpf(str(lp)) * mp.power(q, mp.mpf("-0.5"))
            sample = mp.mpf("1") if kind == "c" else y
            total_abs += weight * sample
            ops += 1
            if q > maxn // p:
                break
            q *= p
            k += 1
    return total_abs, ops


def weight_radius(omega, kind, L, lam, csec=mp.mpf("1e6"), digits=80, R=80, K=16):
    unit = mp.power(10, -digits)
    total_abs, ops = unit_mode_work_size(omega, kind, L, lam, R=R)
    finite = 10 * ops * total_abs * unit
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
    return finite + csec * psi + exp_tail, finite, csec * psi, exp_tail


def bexp(z, L):
    return math.log(max(float(abs(z)), 1e-300)) / math.log(L)


def run():
    print("E73.225 weight radius budget")
    print("Estimates sum |c|rad(W)+sum |l|rad(V) using finite rounding plus Bernoulli tails.")
    print(" lam     L    N gamma row csec radWB radVB sumCradWB sumLradVB totalB centerScaleB ratio")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for row_id in range(2):
                const_map, linear_map = coefficient_maps(q[row_id], idx, d, L)
                max_rw = mp.mpf("0")
                max_rv = mp.mpf("0")
                cache = {}
                for csec in [mp.mpf(1), mp.mpf("1e6")]:
                    sum_crw = mp.mpf("0")
                    sum_lrv = mp.mpf("0")
                    coeff_scale = mp.mpf("0")
                    for om, vec in const_map.items():
                        key = (float(om), "c", str(csec))
                        rw = cache.setdefault(key, weight_radius(om, "c", L, lam, csec=csec)[0])
                        max_rw = max(max_rw, rw)
                        c = abs(vec @ eta)
                        coeff_scale += mp.mpf(str(c))
                        sum_crw += mp.mpf(str(c)) * rw
                    for om, vec in linear_map.items():
                        key = (float(om), "l", str(csec))
                        rv = cache.setdefault(key, weight_radius(om, "l", L, lam, csec=csec)[0])
                        max_rv = max(max_rv, rv)
                        ell = abs(vec @ eta)
                        coeff_scale += mp.mpf(str(ell))
                        sum_lrv += mp.mpf(str(ell)) * rv
                    total = sum_crw + sum_lrv
                    # Center scale is only a denominator sanity proxy here: l1 coefficients times O(1) weight.
                    scale = max(coeff_scale, mp.mpf("1e-300"))
                    print(
                        f"{lam:4d} {L:7.3f} {n_modes:4d} {gamma:7.2f} {row_id:3d}"
                        f" {mp.nstr(csec, 3):>4s} {bexp(max_rw, L):7.2f}"
                        f" {bexp(max_rv, L):7.2f} {bexp(sum_crw, L):10.2f}"
                        f" {bexp(sum_lrv, L):10.2f} {bexp(total, L):7.2f}"
                        f" {bexp(scale, L):12.2f} {float(total / scale):8.1e}"
                    )


if __name__ == "__main__":
    run()
