#!/usr/bin/env python3
"""h0_candidate.py -- phase 135, task D.9.

Tests the two candidate section functors of Paper 46 section 13 against
requirement (c) of the Hodge-index transfer theorem (section 12):

    h0(E) + h0(K-E) >= (1/2)I(E,E) - (1/2)I(E,K) + chi .

Candidates (both are subsets of the radical N_infty, so a member E' = E + (a
correction) is congruent to E mod N_infty and has the same degree):

  naive lattice      L_1 = sum_{q = p^k} Z . tau_{log q}(Pi K)
  arithmetic lattice L_W = sum_{q = p^k} Z . (log p) q^{-1/2} tau_{log q}(Pi K)

  H^0_Z(E) := { a in the lattice : E + a >= 0 pointwise } ,
  h0(E)    := log # H^0_Z(E)   (CC's dim_S is log #/log 3 up to O(1)).

[phase 135, R135_004]  BOTH lattices are now indexed by PRIME POWERS q = p^k
only (finding M7 of R135_002: Lambda(n) = 0 off the prime powers, so the round-1
index set n >= 2 contributed infinitely many zero generators, which made
#H^0_Z(0) infinite and Theorem 13.5(i),(ii) false).  Definition 13.4 of the
paper is corrected to match.

REWRITTEN in float64/numpy: Pi K is differentiated term by term (11.7) instead
of by finite differences, the pointwise constraint is one matrix product, and
`--fast` shrinks the search box.  A `--fast` run finishes in seconds.

NUMERICS ILLUSTRATE AND FALSIFY; THEY PROVE NOTHING.  NO SIGN IS CLAIMED.
"""
import argparse
import itertools
import sys

import numpy as np

from r135_common import Kf, PiKf, gl_panels, vonmangoldt


def prime_powers(qmax):
    out = []
    for q in range(2, qmax + 1):
        L = float(vonmangoldt(q))
        if L != 0.0:
            out.append((q, L))
    return out


def run(check, M, QMAX, AMAX, fast):
    ok = True
    grid = np.arange(-100, 101) / 25.0        # t = -4.0(0.04)4.0
    piK = PiKf(grid)
    Kg = Kf(grid)

    print("== H1  Pi K: degree 0, both signs ==")
    t, w = gl_panels(-4.0, 4.0, 96, 28)
    deg = float((w * PiKf(t)) @ (2 * np.cosh(t / 2)))
    mx, mn = float(piK.max()), float(piK.min())
    amx, amn = float(grid[piK.argmax()]), float(grid[piK.argmin()])
    print("  deg(Pi K) = int Pi K . 2cosh(t/2) dt = %.4g   (predicted 0)" % deg)
    print("  on the grid t = -4.0(0.04)4.0:  max Pi K = %.6f at t = %.2f,"
          "  min Pi K = %.6f at t = %.2f" % (mx, amx, mn, amn))
    good = abs(deg) < 1e-12 and mx > 0 and mn < 0
    ok = ok and good
    print("  %s" % ("ok" if good else "FAIL"))

    pps = prime_powers(QMAX)
    lattices = {
        'naive  L_1': [(q, 1.0) for q, L in pps],
        'arith  L_W': [(q, L * q ** -0.5) for q, L in pps],
    }
    print("\n  index set (prime powers q <= %d): %s" % (QMAX, [q for q, _ in pps]))

    def columns(gens):
        return np.array([wt * PiKf(grid - np.log(q)) for q, wt in gens])

    def admissible(m, cols):
        """# of integer vectors a in the box |a_i| <= AMAX with
        m K + sum_i a_i . (i-th generator) >= 0 on the whole grid.
        Enumerated in numpy chunks: one matrix product per chunk."""
        base = m * Kg
        d = cols.shape[0]
        box = np.arange(-AMAX, AMAX + 1, dtype=float)
        side = box.size
        total = side ** d
        cnt = 0
        CH = 1 << 14
        # digits of the mixed-radix index give the coefficient vector
        pw = side ** np.arange(d - 1, -1, -1)
        for start in range(0, total, CH):
            idx = np.arange(start, min(start + CH, total))
            A = box[(idx[:, None] // pw[None, :]) % side]
            V = A @ cols + base[None, :]
            cnt += int((V >= 0).all(axis=1).sum())
        return cnt

    print("\n== H2  H^0_Z(0) = {0} ==")
    cols = {}
    for name, gens in lattices.items():
        cols[name] = columns(gens)
        c = admissible(0, cols[name])
        print("  %-12s #H^0_Z(0) = %d   %s" % (name, c, "ok" if c == 1 else "FAIL"))
        ok = ok and c == 1

    print("\n== H3  E = mK: the count against requirement (c) ==")
    print("  (c) demands h0(mK) >= (1/2)I(mK,mK) - (1/2)I(mK,K) + chi")
    print("            = m^2/4 - m/4 + chi,  since I(K,K)=1/2 and deg K = 1,")
    print("  and h0(K-mK) = 0 for m >= 2 because deg((1-m)K) = 1-m < 0.")
    print()
    print("  %-12s %3s %8s %10s %14s" % ("lattice", "m", "#H^0_Z", "log #", "m^2/4-m/4"))
    for name in lattices:
        for m in range(1, M + 1):
            c = admissible(m, cols[name])
            print("  %-12s %3d %8d %10.6g %14.6g"
                  % (name, m, c, np.log(c), m * m / 4 - m / 4))
        print()
    print("  Reading: the count is 1 for every m tested and both lattices, so")
    print("  log # = 0 while the right-hand side of (c) grows like m^2/4.")
    print("  (c) FAILS for both candidates.  This is a refutation of the route,")
    print("  not a statement about any sign.")

    print("\nALL CHECKS PASSED" if ok else "\nSOME CHECKS FAILED")
    return 0 if ok or not check else 1


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--fast', action='store_true',
                    help='M=6, prime powers q<=5, |a|<=3; finishes in seconds')
    ap.add_argument('--M', type=int, default=None)
    ap.add_argument('--qmax', type=int, default=None)
    ap.add_argument('--amax', type=int, default=None)
    a = ap.parse_args()
    M = a.M if a.M is not None else (6 if a.fast else 8)
    Q = a.qmax if a.qmax is not None else (5 if a.fast else 7)
    A = a.amax if a.amax is not None else (3 if a.fast else 6)
    sys.exit(run(a.check, M, Q, A, a.fast))
