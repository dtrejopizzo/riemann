#!/usr/bin/env python3
"""Exact-rational Euler--Maclaurin pilot for gamma_j and zeta(k).

No float is used.  This is intentionally a pilot (default j<=20): it
constructs its Stieltjes intervals rather than accepting decimal tables.
The formulas and remainder are printed/used with Fraction arithmetic.
"""
from fractions import Fraction
from math import factorial
from pathlib import Path
import runpy

base = Path(__file__).resolve().parents[2] / "phase-102-omega7-closure-campaign" / "RH-MASTER-CONTEXT" / "tools" / "omega7_point4_interval_verify.py"
ns = runpy.run_path(str(base))
I, as_i = ns["I"], ns["as_i"]


def ipow(x, n):
    out = I(1)
    while n:
        if n & 1:
            out = out * x
        x = x * x
        n //= 2
    return out


def log_rational(q, terms=60):
    """Rigorous atanh enclosure of log(q), q a positive Fraction."""
    if q <= 0:
        raise ValueError
    e = 0
    while q >= 2:
        q /= 2; e += 1
    while q < 1:
        q *= 2; e -= 1
    y = (q - 1) / (q + 1)             # 0 <= y <= 1/3
    total = Fraction(0)
    p = y
    for r in range(terms):
        total += p / (2*r + 1)
        p *= y*y
    lo = 2*total
    # geometric bound for the omitted odd tail
    hi = lo + 2*p / ((2*terms + 1) * (1-y*y))
    l2 = log2_interval(terms)
    return I(lo, hi) + e*l2


_LOG2 = None
def log2_interval(terms):
    global _LOG2
    if _LOG2 is None:
        y = Fraction(1, 3); total = Fraction(0); p = y
        for r in range(terms):
            total += p/(2*r+1); p *= y*y
        lo = 2*total
        _LOG2 = I(lo, lo + 2*p/((2*terms+1)*(1-y*y)))
    return _LOG2


def bernoulli_even(rmax):
    a = [Fraction(0) for _ in range(2*rmax+1)]
    out = {}
    for m in range(2*rmax+1):
        a[m] = Fraction(1, m+1)
        for j in range(m, 0, -1):
            a[j-1] = j*(a[j-1]-a[j])
        if m and m % 2 == 0:
            out[m] = a[0]
    return out


_POLY = {}
def derivative_poly(j, q):
    if (j, q) in _POLY:
        return _POLY[j, q]
    p = [0]*(j+1); p[j] = 1
    for step in range(q):
        nxt = [0]*(j+1)
        for l, c in enumerate(p):
            if l: nxt[l-1] += l*c
            nxt[l] -= (step+1)*c
        p = nxt
    _POLY[j, q] = p
    return p


def poly_eval_interval(p, x):
    out = I(0)
    for c in reversed(p):
        out = out*x + c
    return out


def integral_abs_poly(p, q, N, logN):
    """Upper bound integral_N^inf x^(-q-1) sum |c_l| log(x)^l dx."""
    ans = Fraction(0)
    L = logN.hi
    for l, c in enumerate(p):
        if not c: continue
        inner = Fraction(0)
        for a in range(l+1):
            inner += Fraction(factorial(l), factorial(l-a)*q**(a+1))*L**(l-a)
        ans += abs(c)*inner
    return ans / Fraction(N**q)


class EMContext:
    """Exact data shared by all Stieltjes enclosures at fixed N,R,K."""
    def __init__(self, N=32, R=8, log_terms=40, max_j=20):
        self.N, self.R = N, R
        self.logs = [I(0)] + [log_rational(Fraction(k), log_terms)
                              for k in range(1, N+1)]
        self.B = bernoulli_even(R)
        self.pow = [[I(1) for _ in range(max_j+2)] for _ in range(N+1)]
        for k in range(1, N+1):
            for j in range(1, max_j+2):
                self.pow[k][j] = self.pow[k][j-1] * self.logs[k]


def gamma_interval(j, N=32, R=8, log_terms=40, ctx=None):
    """EM enclosure, with |B_{2R}(x)| <= 4(2R)!/6^(2R)."""
    if ctx is None:
        ctx = EMContext(N, R, log_terms, j)
    if (N, R) != (ctx.N, ctx.R) or j+1 >= len(ctx.pow[0]):
        raise ValueError("context does not cover requested parameters")
    logs = ctx.logs
    A = I(0)
    for k in range(1, N+1):
        A += ctx.pow[k][j] / k
    LN = logs[N]
    A -= ctx.pow[N][j+1] / (j+1)
    val = A - ctx.pow[N][j] / (2*N)
    for r in range(1, R+1):
        q = 2*r-1
        val -= Fraction(ctx.B[2*r], factorial(2*r)*N**(q+1)) * poly_eval_interval(derivative_poly(j,q), LN)
    p = derivative_poly(j, 2*R)
    err = Fraction(4, 6**(2*R))*integral_abs_poly(p, 2*R, N, LN)
    return I(val.lo-err, val.hi+err)


def zeta_interval(k, M=256):
    s = sum((Fraction(1, m**k) for m in range(1, M+1)), Fraction(0))
    return I(s + Fraction(1, (k-1)*(M+1)**(k-1)), s + Fraction(1, (k-1)*M**(k-1)))


def main():
    # Pilot: constructs, rather than imports, all new constants needed to n=20.
    # The deliberately modest parameters are enough to test the proof chain,
    # not claimed to be an efficient n=149 production configuration.
    gamma = ns["gamma"]
    zeta = ns["zeta"]
    import sys
    top = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    first = int(sys.argv[2]) if len(sys.argv) > 2 else 9
    if not 9 <= top <= 20:
        raise SystemExit("usage: stieltjes_em_interval_pilot.py [9..20]")
    ctx = EMContext(max_j=top)
    for j in range(8, top+1):
        g = gamma_interval(j, ctx=ctx)
        gamma.append(g)
        print("gamma", j, g.dec(18), "width<", g.width() < Fraction(1,10**18))
    for k in range(9, top+1):
        z = zeta_interval(k)
        zeta[k] = z
        print("zeta", k, z.dec(18))
    for n in range(first, top+1):
        arch = ns["lambda_arch"](n)
        margin = ns["lambda_prime"](n) + arch/2
        print("margin", n, margin.dec(12), "positive=", margin.lo > 0)

if __name__ == "__main__":
    main()
