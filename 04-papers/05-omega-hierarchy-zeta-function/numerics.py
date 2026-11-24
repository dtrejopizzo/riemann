#!/usr/bin/env python3
"""Computations reported in Section 8 of the paper.

Usage:  python3 numerics.py            (prints the tables; part (c) takes several minutes)

(a) S_N(z) = sum_{n<=N} z^omega(n)/n for z = 1/4, 1, 4, 9 and N <= 2*10^6:
    least-squares slope of log S_N(z) against loglog N on 30 log-spaced
    values of N in [3*10^4, 2*10^6]; the ratio S_N(z)/(log N)^z at N = 2*10^6
    compared with the constant C(z); the same ratio for the squarefree sum
    compared with C^flat(z); mean of omega under the weight z^omega(n)/n.
(b) Level variances V_j = (1/2) sum_{p in L_j} 1/p for primes p <= 10^7.
(c) Maximum of G(t) = sum_{p<=X} cos(t log p)/sqrt(p) over unit windows
    [t0 + 10 i, t0 + 10 i + 1], i = 0..199, t0 = 10^7, sampling step 0.002.
"""
import math
import numpy as np

MERTENS = 0.2614972128476428


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def omega_and_squarefree(n):
    om = np.zeros(n + 1, dtype=np.int8)
    sqf = np.ones(n + 1, dtype=bool)
    for p in primes_upto(n):
        om[p::p] += 1
        if p * p <= n:
            sqf[p * p::p * p] = False
    return om, sqf


def euler_constant(z, flat=False, P=10 ** 7):
    """C(z) or C^flat(z): product over p <= P, tail corrected to first order."""
    p = primes_upto(P).astype(np.float64)
    if flat:
        logs = z * np.log1p(-1 / p) + np.log1p(z / p)
        tail = -(z * (z + 1) / 2)          # sum_{p>P} of -(z(z+1)/2)/p^2
    else:
        logs = z * np.log1p(-1 / p) + np.log1p(z / (p - 1))
        tail = z * (1 - z) / 2             # sum_{p>P} of (z(1-z)/2)/p^2
    tail *= 1 / (P * math.log(P))          # sum_{p>P} 1/p^2 ~ 1/(P log P)
    return math.exp(logs.sum() + tail) / math.gamma(z + 1)


def part_a():
    N = 2 * 10 ** 6
    om, sqf = omega_and_squarefree(N)
    n = np.arange(1, N + 1, dtype=np.float64)
    omf = om[1:].astype(np.float64)
    Ns = np.unique(np.round(np.exp(np.linspace(math.log(3e4), math.log(N), 30))).astype(int))
    x = np.log(np.log(Ns))
    lam = math.log(math.log(N))
    print("(a) N = 2e6, loglog N = %.4f" % lam)
    print("   z     slope   S_N/(logN)^z   C(z)       flat ratio  C^flat(z)   mean omega  z*loglogN")
    for z in (0.25, 1.0, 4.0, 9.0):
        w = z ** omf / n
        cs = np.cumsum(w)
        slope = np.polyfit(x, np.log(cs[Ns - 1]), 1)[0]
        ratio = cs[-1] / math.log(N) ** z
        flat = (w * sqf[1:]).sum() / math.log(N) ** z
        mean = (w * omf).sum() / cs[-1]
        print("  %5.2f  %6.3f  %12.5g  %10.5g  %10.5g  %10.5g  %8.3f  %8.3f"
              % (z, slope, ratio, euler_constant(z), flat, euler_constant(z, True), mean, z * lam))


def part_b():
    X = 10 ** 7
    p = primes_upto(X).astype(np.float64)
    lev = np.floor(np.log(np.log(p))).astype(int)
    print("(b) X = 1e7, loglog X = %.4f" % math.log(math.log(X)))
    for j in sorted(set(lev.tolist())):
        print("   level %2d: V_j = %.4f  (%d primes)" % (j, 0.5 * (1 / p[lev == j]).sum(), (lev == j).sum()))
    print("   total V = %.4f ; (loglog X + M)/2 = %.4f"
          % (0.5 * (1 / p).sum(), 0.5 * (math.log(math.log(X)) + MERTENS)))


def part_c():
    t0, step, nwin = 1e7, 0.002, 200
    h = np.arange(0.0, 1.0 + step / 2, step)
    print("(c) unit windows [1e7+10i, 1e7+10i+1], i<200, step 0.002")
    print("   X        2V      mean max  sd max   mean max/2V   (LL - 0.75 LLL)/2V")
    for X in (2 * 10 ** 3, 2 * 10 ** 4, 2 * 10 ** 5):
        p = primes_upto(X).astype(np.float64)
        lp, a = np.log(p), 1 / np.sqrt(p)
        V = 0.5 * (1 / p).sum()
        mx = np.empty(nwin)
        for i in range(nwin):
            t = t0 + 10 * i + h
            g = np.zeros_like(t)
            for c in range(0, len(p), 2000):
                g += np.cos(np.outer(t, lp[c:c + 2000])) @ a[c:c + 2000]
            mx[i] = g.max()
        LL = math.log(math.log(X))
        print("   %7d  %.4f  %.4f    %.4f   %.3f         %.3f"
              % (X, 2 * V, mx.mean(), mx.std(), mx.mean() / (2 * V), (LL - 0.75 * math.log(LL)) / (2 * V)))


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
