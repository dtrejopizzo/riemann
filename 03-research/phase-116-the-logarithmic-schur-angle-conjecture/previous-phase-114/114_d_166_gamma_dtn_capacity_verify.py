#!/usr/bin/env python3
"""Numerical audit of the explicit pure-Gamma DtN lower bound."""
import mpmath as mp


mp.mp.dps = 60
A = mp.mpf(5) / 4
C0 = mp.mpf(1) / 2


def h(x):
    return mp.re(mp.digamma(A + 0.5j * x) - mp.digamma(A))


def lower(logn):
    # Evaluate directly from log N so astronomical N never overflows.
    n_inv = mp.exp(-logn)
    ell = mp.log1p(n_inv)
    t = mp.log(mp.exp(logn) + 1) / 2
    L = mp.log(1 / ell)
    R = 1 / (ell * L**4)
    gap = (1 - 2 * C0 / mp.pi) * h(C0 / t)
    cap = 1 / (mp.sqrt(2 * ell * R / (mp.pi * gap)) + 1 / mp.sqrt(h(R)))**2
    return L, R, gap, cap


def main():
    old = mp.mpf(0)
    for logn in map(mp.mpf, (20, 50, 100, 200, 500, 1000)):
        L, R, gap, cap = lower(logn)
        assert L > 0 and R > 0 and gap > 0 and cap > old
        old = cap
        print("logN=%4d  cap/logN=%s  logR=%s" % (
            int(logn), mp.nstr(cap / logn, 10), mp.nstr(mp.log(R), 10)))
    # The displayed ratios tend to one, as proved analytically in D.166.
    assert lower(mp.mpf(1000))[3] / 1000 > mp.mpf("0.84")
    print("D166 pure-Gamma DtN capacity audit: PASS")


if __name__ == "__main__":
    main()
