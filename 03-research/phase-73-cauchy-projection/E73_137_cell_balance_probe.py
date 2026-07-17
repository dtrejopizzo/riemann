#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm
from scipy.integrate import quad

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402

GAMMA_E = 0.5772156649015329
LOG4PI = np.log(4 * np.pi)


def make_q(m, n, L):
    if m == n:
        return lambda y: 2 * (1 - y / L) * np.cos(2 * np.pi * n * y / L) if 0 <= y <= L else 0.0
    c = 1.0 / (np.pi * (n - m))
    return lambda y: (np.sin(2 * np.pi * m * y / L) - np.sin(2 * np.pi * n * y / L)) * c if 0 <= y <= L else 0.0


def primes_upto(n):
    sieve = np.ones(n + 1, bool)
    sieve[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    return np.nonzero(sieve)[0]


def entry_parts(m, n, L, lam, primes):
    q = make_q(m, n, L)
    q0 = q(0.0)
    w02, _ = quad(lambda y: q(y) * (np.exp(y / 2) + np.exp(-y / 2)), 0, L, limit=200)

    def wri(y):
        if y < 1e-9:
            h = 1e-6
            return ((q(h) - q(0.0)) / h + q0 / 2) / 2.0
        return (np.exp(y / 2) * q(y) - q0) / (2 * np.sinh(y))

    wra, _ = quad(wri, 0, L, limit=200)
    wrb = q0 * 0.5 * np.log(np.tanh(L / 2))
    wr = 0.5 * (LOG4PI + GAMMA_E) * q0 + wra + wrb

    arith = 0.0
    maxn = int(lam * lam)
    for p in primes:
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            arith += lp * (pm ** -0.5) * q(me * lp)
            pm *= p
            me += 1
    return w02, wr, arith


def build_parts(lam, n_modes):
    L = 2.0 * np.log(lam)
    idx = np.arange(-n_modes, n_modes + 1)
    n = len(idx)
    w02 = np.zeros((n, n))
    wr = np.zeros((n, n))
    prime = np.zeros((n, n))
    primes = primes_upto(int(lam * lam))
    for a in range(n):
        for b in range(a, n):
            x, y, z = entry_parts(idx[a], idx[b], L, lam, primes)
            w02[a, b] = w02[b, a] = x
            wr[a, b] = wr[b, a] = y
            prime[a, b] = prime[b, a] = z
    h = w02 - wr - prime
    d = 2.0 * np.pi * idx / L
    return h, w02, wr, prime, d, L


def orient(x):
    x = (x + x[::-1]) / 2.0
    x = x / norm(x)
    if x[len(x) // 2] < 0:
        x = -x
    return x


def run():
    print("E73.137 cell balance probe")
    print("Measures <e,W02 xi>, <e,WR xi>, <e,Prime xi> for normalized critical rows.")
    print(" lam     L gamma      evalB    W02B     WRB  PrimeB balanceB cancelB")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28)]:
        h, w02, wr, prime, d, L = build_parts(lam, n_modes)
        vals, vecs = eigh(h)
        xi = orient(vecs[:, 0])
        mu = vals[0]
        for gamma in GAMMAS[:3]:
            k = 1.0 / (-gamma - d)
            e = k / norm(k)
            ev = float(np.dot(e, xi))
            a = float(np.dot(e, w02 @ xi))
            b = float(np.dot(e, wr @ xi))
            c = float(np.dot(e, prime @ xi))
            bal = a - b - c - mu * ev
            denom = abs(a) + abs(b) + abs(c)
            cancel = abs(a - b - c) / max(denom, 1e-300)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(abs(ev), L):8.3f} {bexp(abs(a), L):8.3f}"
                f" {bexp(abs(b), L):7.3f} {bexp(abs(c), L):7.3f}"
                f" {bexp(abs(bal), L):8.3f} {bexp(cancel, L):7.3f}"
            )


if __name__ == "__main__":
    run()

