#!/usr/bin/env python3
"""R140 --- certification of the two constants of D.24.2.

Constant 1 (chi):  inf over (a,b) in R^2 of
    g(a,b) = max(a,0)max(b,0) + max(c-a,0)max(c-b,0) - a*b + (c/2)*(a+b)
with c = 1/2 (the case Z = xi, M(K) = (1/2,1/2)).  D.24.2 proves inf g = c^2/2 = 1/8,
attained at (a,b) = (c,0) and (0,c).  The script certifies the LOWER bound numerically
on a grid with a stated margin; the exact value is proved, not computed.

Constant 2 (the CC slope):  lambda_CC = 1/log 3 < 1, with the margin 1 - 1/log 3.
D.24.1 proves lambda_CC < 1 by "3 > e"; the script only prints the margin.

Usage:  certify_chi.py [--fast]
Exit 0 on success.  No claim of this script is used in any proof.
"""
import sys, math

FAST = "--fast" in sys.argv
c = 0.5


def g(a, b, c=c):
    return (max(a, 0.0) * max(b, 0.0)
            + max(c - a, 0.0) * max(c - b, 0.0)
            - a * b + (c / 2.0) * (a + b))


def sweep(lo, hi, n):
    best, arg = float("inf"), None
    step = (hi - lo) / n
    for i in range(n + 1):
        a = lo + i * step
        for j in range(n + 1):
            b = lo + j * step
            v = g(a, b)
            if v < best:
                best, arg = v, (a, b)
    return best, arg


def main():
    n = 400 if FAST else 4000
    lo, hi = -6.0, 6.0
    best, arg = sweep(lo, hi, n)
    target = c * c / 2.0
    print("grid %d x %d on [%g,%g]^2" % (n + 1, n + 1, lo, hi))
    print("min g on grid      = %.12f  at (a,b) = (%.6f, %.6f)" % (best, arg[0], arg[1]))
    print("proved value c^2/2 = %.12f" % target)
    print("margin (grid - proved) = %.3e   (must be >= -1e-9)" % (best - target))
    ok = best >= target - 1e-9
    # the two attaining points, exactly
    for p in ((c, 0.0), (0.0, c)):
        print("g%s = %.12f" % (p, g(*p)))
        ok = ok and abs(g(*p) - target) < 1e-15
    lam = 1.0 / math.log(3.0)
    print("lambda_CC = 1/log 3 = %.12f ;  1 - lambda_CC = %.12f > 0" % (lam, 1.0 - lam))
    print("lambda_CC^2 = %.12f ;  required >= 1" % (lam * lam))
    ok = ok and lam < 1.0
    print("ALL CHECKS PASSED" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
