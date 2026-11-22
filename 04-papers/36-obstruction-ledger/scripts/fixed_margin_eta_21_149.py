#!/usr/bin/env python3
"""Rigorous fixed-point strong-margin propagation from normalized eta data.

Unlike the n<=20 pilot, this driver never expands a normalized coefficient
as gamma_j and then divides by j!: it carries q(t)=t*zeta(1+t) directly.
"""
from math import comb
from pathlib import Path
import runpy

root = Path(__file__).resolve().parent
eg = runpy.run_path(str(root / "eta_fixed_generator.py"))
em = runpy.run_path(str(root / "stieltjes_em_interval_pilot.py"))
F, S = eg["F"], eg["S"]


def neg(a):
    return F(-a.h, -a.l)


def qfix(a):
    return eg["qf"](a)


def log_series(q):
    """Outward coefficients of log(q), where q[0]=1, in O(M^2)."""
    M = len(q) - 1
    p = [F(0) for _ in range(M + 1)]
    for n in range(1, M + 1):
        v = q[n]
        for k in range(1, n):
            v = v - (p[k] * q[n-k]).mul_int(k).div(n)
        p[n] = v
    return p


def margins(top=149, first=21, K=830, terms=800):
    if not (1 <= first <= top < K):
        raise ValueError("require 1 <= first <= top < K")
    q = eg["q_coeffs"](K, top, terms)
    p = log_series(q)

    old = em["ns"]
    log4 = qfix(old["log4pi"])
    zeta = {k: qfix(v) for k, v in old["zeta"].items() if k <= top}
    for k in range(9, top + 1):
        zeta[k] = qfix(em["zeta_interval"](k))

    out = []
    gamma0 = q[1]
    for n in range(first, top + 1):
        prime = F(0)
        for k in range(1, n + 1):
            prime = prime + p[k].mul_int(n * comb(n-1, k-1))

        arch = F(S) - (gamma0 + log4).mul_int(n).div(2)
        for k in range(2, n + 1):
            mult = (-1 if k % 2 else 1) * comb(n, k) * (2**k - 1)
            arch = arch + zeta[k].mul_int(mult).div(2**k)
        out.append((n, prime + arch.div(2)))
    return out


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=149)
    ap.add_argument("--first", type=int, default=21)
    ap.add_argument("--K", type=int, default=830)
    ap.add_argument("--terms", type=int, default=800)
    a = ap.parse_args()
    for n, m in margins(a.top, a.first, a.K, a.terms):
        # A compact, exact-sign audit: scaled lower/upper decimal prefixes and
        # raw interval width.  Positivity is decided only by the integer lower
        # endpoint.
        print(n, m.l > 0, m.l // 10**(eg["P"]-12),
              m.h // 10**(eg["P"]-12), m.h-m.l)
