#!/usr/bin/env python3
# ======================================================================================
# Phase 71 / E71.9 -- relative determinant with archimedean/free background.
#
# E71.8 showed that the all-root product is distorted by finite-section background roots.
# The first zero-independent background candidate is the same CCM finite construction with the
# prime-power term removed.  This script compares:
#
#   D_rel(t) = D_zeta_all(t) / D_arch_all(t)
#
# against Xi(t)/Xi(0), below the first zeta zero.
# ======================================================================================
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from scipy.optimize import brentq

mp.mp.dps = 40
GAMMA = 0.5772156649015329
LOG4PI = np.log(4 * np.pi)
ZEROS = np.array([14.134725,21.022040,25.010858,30.424876,32.935062,37.586178,40.918719,
                  43.327073,48.005151,49.773832])

def Xi_norm(t):
    s = mp.mpf("0.5") + 1j * mp.mpf(str(t))
    xi = mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    s0 = mp.mpf("0.5")
    xi0 = mp.mpf("0.5") * s0 * (s0 - 1) * mp.power(mp.pi, -s0 / 2) * mp.gamma(s0 / 2) * mp.zeta(s0)
    return float(mp.re(xi / xi0))

def make_q(m, n, L):
    if m == n:
        return lambda y: 2 * (1 - y / L) * np.cos(2 * np.pi * n * y / L) if 0 <= y <= L else 0.0
    c = 1.0 / (np.pi * (n - m))
    return lambda y: (np.sin(2 * np.pi * m * y / L) - np.sin(2 * np.pi * n * y / L)) * c if 0 <= y <= L else 0.0

def primes_upto(n):
    sieve = np.ones(n + 1, bool)
    sieve[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    return np.nonzero(sieve)[0]

def QW_entry(m, n, L, lam, include_arith=True):
    q = make_q(m, n, L)
    q0 = q(0.0)
    W02, _ = quad(lambda y: q(y) * (np.exp(y / 2) + np.exp(-y / 2)), 0, L, limit=200)

    def wri(y):
        if y < 1e-9:
            h = 1e-6
            return ((q(h) - q(0.0)) / h + q0 / 2) / 2.0
        return (np.exp(y / 2) * q(y) - q0) / (2 * np.sinh(y))

    WRa, _ = quad(wri, 0, L, limit=200)
    WRb = q0 * 0.5 * np.log(np.tanh(L / 2))
    WR = 0.5 * (LOG4PI + GAMMA) * q0 + WRa + WRb

    arith = 0.0
    if include_arith:
        maxn = int(lam * lam)
        for p in primes_upto(maxn):
            lp = np.log(p)
            pm = p
            me = 1
            while pm <= maxn:
                arith += lp * (pm ** -0.5) * q(me * lp)
                pm *= p
                me += 1
    return W02 - WR - arith

def build(lam, N, include_arith=True):
    L = 2.0 * np.log(lam)
    idx = np.arange(-N, N + 1)
    M = np.zeros((len(idx), len(idx)))
    for a in range(len(idx)):
        for b in range(a, len(idx)):
            v = QW_entry(idx[a], idx[b], L, lam, include_arith=include_arith)
            M[a, b] = v
            M[b, a] = v
    return M, idx, L

def roots_from_matrix(M, idx, L, hmax=55):
    _, V = np.linalg.eigh(M)
    xi = V[:, 0]
    xi = (xi + xi[::-1]) / 2
    d = 2 * np.pi * idx / L
    order = np.argsort(d)
    d = d[order]
    xi = xi[order]

    def f(s):
        return np.sum(xi / (s - d))

    roots = []
    for i in range(len(d) - 1):
        a, b = d[i] + 1e-7, d[i + 1] - 1e-7
        if a >= b:
            continue
        try:
            if np.isfinite(f(a)) and np.isfinite(f(b)) and f(a) * f(b) < 0:
                roots.append(brentq(f, a, b, xtol=1e-11))
        except Exception:
            pass
    roots = np.array(roots)
    return np.sort(roots[(roots > 1) & (roots < hmax)])

def product_values(ts, roots):
    roots = np.asarray([r for r in roots if r > 1e-9], dtype=float)
    vals = []
    for t in ts:
        vals.append(float(np.prod(1.0 - (t * t) / (roots * roots))))
    return np.array(vals)

def rel_errors(vals, target):
    err = vals - target
    return np.linalg.norm(err) / np.linalg.norm(target), np.max(np.abs(err)) / np.max(np.abs(target))

def run(lam=5.0, Ns=(18, 40), hmax=55, tmax=12.0):
    ts = np.linspace(0.0, tmax, 160)
    target = np.array([Xi_norm(t) for t in ts], dtype=float)
    print(f"grid: [0,{tmax}] below first zero, hmax={hmax}")
    print("   N  #zeta #arch      all_relL2     rel_relL2    rel_relSup")
    for N in Ns:
        Mz, idx, L = build(lam, N, include_arith=True)
        Ma, _, _ = build(lam, N, include_arith=False)
        rz = roots_from_matrix(Mz, idx, L, hmax=hmax)
        ra = roots_from_matrix(Ma, idx, L, hmax=hmax)
        Dz = product_values(ts, rz)
        Da = product_values(ts, ra)
        Drel = Dz / Da
        all_l2, _ = rel_errors(Dz, target)
        rel_l2, rel_sup = rel_errors(Drel, target)
        print(f"{N:4d} {len(rz):6d} {len(ra):6d} {all_l2:14.6e} {rel_l2:13.6e} {rel_sup:13.6e}")
        print(f"      zeta roots[:10]={np.array2string(rz[:10], precision=4)}")
        print(f"      arch roots[:10]={np.array2string(ra[:10], precision=4)}")

if __name__ == "__main__":
    print("=" * 90)
    print(" E71.9 -- relative determinant with arch/free background")
    print("=" * 90)
    run()
    print("\nREADING")
    print("  If D_zeta/D_arch improves strongly, the background is mostly archimedean/window.")
    print("  If it fails, the spurious roots are not removed by the arch-free determinant alone.")
