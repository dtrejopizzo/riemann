#!/usr/bin/env python3
"""E78.140 - kernel-derived quasimode trial vectors.

Candidates (from E78.139 sec 6, item (i)/(iii)):

  C1: u_N(m) = sum_{p^k<=maxn} log(p) * p^{-k/2} * cos(2*pi*m*(k log p)/L)
  C2: u_N(m) = sum_{p^k<=maxn} p^{-k/2} * cos(2*pi*m*(k log p)/L)          (no log p)
  C3: u_N(m) = sum_{p^k<=maxn} log(p) * p^{-k/2} * (1 - k log p / L)
                                * cos(2*pi*m*(k log p)/L)                  (full diag kernel)

For each candidate, build u_N on the inner index set -N+1..N-1, apply the
inner-block operator A_N = H[1:-1,1:-1] (build_mp, lambda=6), and measure
eps_N = ||A_N u_N|| / ||u_N||.

Grid: L in {4,6,8} (via lam=6, matching build_mp's L=2log(lam) -- NOTE:
build_mp fixes L = 2*log(lam); to test L in {4,6,8} we vary lam accordingly,
lam = exp(L/2)), N=6..16 step 2, dps=70, both builds (zeta, planted falsifier).
"""

import json
import sys
import time

import mpmath as mp

sys.path.insert(0, "/Users/dt/riemann/03-research/phase-76-normalized-adjugate-arithmetic-lock")
from P76_002_mp_entry_audit import build_mp, primes_upto, vec_norm

PLANTED = ("14.134725141734693790", "0.30", "5.0")


def build_u(idx, L, lam, variant):
    maxn = int(lam * lam)
    primes = primes_upto(maxn)
    vals = {}
    for m in idx:
        s = mp.mpf(0)
        for p in primes:
            lp = mp.log(p)
            pm, exponent = p, 1
            while pm <= maxn:
                y = exponent * lp
                pw = mp.power(pm, mp.mpf("-0.5"))
                ang = mp.cos(2 * mp.pi * m * y / L)
                if variant == "C1":
                    s += lp * pw * ang
                elif variant == "C2":
                    s += pw * ang
                elif variant == "C3":
                    s += lp * pw * (1 - y / L) * ang
                else:
                    raise ValueError(variant)
                pm *= p
                exponent += 1
        vals[m] = s
    v = mp.matrix([vals[m] for m in idx])
    return v


def run_one(lam_target_L, n_modes, dps, variant, planted=None):
    # lam such that L = 2 log(lam) = lam_target_L
    lam = mp.e ** (mp.mpf(lam_target_L) / 2)
    mp.mp.dps = dps
    H, idx, L = build_mp(lam, n_modes, dps, planted=planted)
    inner_idx = idx[1:-1]
    inner = H[1:-1, 1:-1]
    u = build_u(inner_idx, L, lam, variant)
    nu = vec_norm(u)
    Au = inner * u
    nAu = vec_norm(Au)
    eps = nAu / nu
    rayleigh = (u.T * Au)[0] / (nu * nu)
    return {
        "L_target": lam_target_L,
        "L_actual": mp.nstr(L, 15),
        "N": n_modes,
        "dps": dps,
        "variant": variant,
        "norm_u": mp.nstr(nu, 15),
        "norm_Au": mp.nstr(nAu, 15),
        "eps_N": mp.nstr(eps, 15),
        "rayleigh_N": mp.nstr(rayleigh, 15),
    }


def main():
    dps = 70
    Ls = [4, 6, 8]
    Ns = [6, 8, 10, 12, 14, 16]
    variants = ["C1", "C2", "C3"]
    results = {"zeta": [], "planted": []}
    t0 = time.time()
    for variant in variants:
        for L in Ls:
            for N in Ns:
                r = run_one(L, N, dps, variant, planted=None)
                results["zeta"].append(r)
                print("zeta", variant, "L=", L, "N=", N, "eps=", r["eps_N"],
                      "t=", round(time.time() - t0, 1), flush=True)
                r2 = run_one(L, N, dps, variant, planted=PLANTED)
                results["planted"].append(r2)
                print("plant", variant, "L=", L, "N=", N, "eps=", r2["eps_N"],
                      "t=", round(time.time() - t0, 1), flush=True)
    with open(
        "/Users/dt/riemann/03-research/phase-78-build-neutral-lp-and-ident/E78_140_kernel_quasimode_results.json",
        "w",
    ) as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()
