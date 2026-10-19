#!/usr/bin/env python3
"""CERT_FALSIFIERS_001: rigorous interval enclosures (mpmath.iv, outward rounding) of the Rayleigh quotient
a_T(F)/||F||^2 (P47 eq:Aform) for explicit test functions F in P_T, F(t)=G(t/T), G a polynomial.
  a_T(F) = C0 c(0) + int_0^{2T}(c(0)-c(u))K(u)du + c(0) int_{2T}^inf K - sum_{n<e^{2T}} v_n c(log n),
  c(u)=int F(t)F(t-u)dt, K(u)=2e^{-u/2}/(1-e^{-2u}), C0=-gamma-pi/2-3log2-log pi, v_n=2a(n)/sqrt n.
Rigour: c(u)=T*sum_r p_r (u/T)^r with p_r exact polynomial algebra (Cpoly, rational) times interval coefficients;
  moments int_0^{2T} u^r K = 2 sum_k int_0^{2T} u^r e^{-a_k u}, a_k=2k+1/2, k<NK exact (lower incomplete gamma,
  positive series with geometric remainder bound or complement form), k>=NK enclosed by integral comparison;
  int_{2T}^inf K = log coth(T/2)+pi-2 atan e^T (P47 thm:S(iii)); Tate moments int x^j e^{cx} by Taylor series
  with explicit remainder. Tate moments are re-imposed EXACTLY: the coefficients of x^0,x^1 (full space) or x^1
  (odd sector) are the interval solution of the linear constraint system; the enclosure is valid for the exact F.
Test G: Galerkin minimiser (mpmath, non-rigorous, only used to choose G), coefficients rationalised (denominator 2^40).
Usage: python3 cert_falsifiers.py"""
import sys, mpmath as mp
from mpmath import iv
from fractions import Fraction as Fr
from math import comb as binom, factorial
iv.dps = 60; mp.mp.dps = 40
NK = 3000
def pp(nmax):
    out = []
    for n in range(2, nmax + 1):
        p = next(q for q in range(2, n + 1) if n % q == 0); r = n
        while r % p == 0: r //= p
        if r == 1: out.append((n, p))
    return out
_c = {}
def Cpoly(j, k):  # int_{-1+s}^{1} x^j (x-s)^k dx = sum_r P[r] s^r, exact rationals
    if (j, k) in _c: return _c[(j, k)]
    P = {}
    for i in range(k + 1):
        c = binom(k, i) * (-1) ** (k - i); m = j + i + 1
        P[k - i] = P.get(k - i, 0) + Fr(c, m)
        for l in range(m + 1): P[k - i + l] = P.get(k - i + l, 0) - Fr(c * binom(m, l) * (-1) ** (m - l), m)
    _c[(j, k)] = P; return P
def ivf(q): return iv.mpf(q.numerator) / q.denominator

def Kmoments(T, R):
    """rigorous mom[r] = int_0^{2T} (u/T)^r K(u) du, r=1..R"""
    L = 2 * T; S = [iv.mpf(0)] * (R + 1)
    for k in range(NK):
        a = iv.mpf(2 * k) + iv.mpf(1) / 2; x = a * L; xm = float(x.b)
        for r in range(1, R + 1):
            # gamma(r+1,x) lower incomplete; int_0^L u^r e^{-au} = gamma(r+1,x)/a^{r+1}
            if xm <= r + 1:   # positive series x^{r+1}e^{-x} sum x^m/((r+1)...(r+1+m))
                term = iv.mpf(1) / (r + 1); s = term; m = 0
                while True:
                    m += 1; term = term * x / (r + 1 + m); s += term
                    if float(term.b) < 1e-70 and m > 2 * xm: break
                # remainder: ratio <= x/(r+m+2) <= 1/2  => remainder <= term
                s = s + iv.mpf([0, float(term.b) * 1.0000001])
                g = x ** (r + 1) * iv.exp(-x) * s
            else:            # complement r!(1 - e^{-x} sum_{i<=r} x^i/i!)
                t = iv.mpf(1); sm = iv.mpf(1)
                for i in range(1, r + 1): t = t * x / i; sm += t
                g = factorial(r) * (1 - iv.exp(-x) * sm)
            S[r] += 2 * g / a ** (r + 1)
    aN = 2 * NK + 0.5
    for r in range(1, R + 1):
        # sum_{k>=NK} 2 r!/a_k^{r+1} in [2r! I, 2r!(I + aN^{-(r+1)})], I = aN^{-r}/(2r); minus incomplete part
        I = iv.mpf(aN) ** (-r) / (2 * r); up = I + iv.mpf(aN) ** (-(r + 1))
        lo_ = 2 * factorial(r) * I; hi_ = 2 * factorial(r) * up
        # neglected e^{-x}sum part for k>=NK: x>=aN*L>=4000>r: bounded by 2 r!(r+1)x^r e^{-x}/r!/a^{r+1} summed: < 1e-1000
        S[r] += iv.mpf([float(lo_.a) * (1 - 1e-12) - 1e-300, float(hi_.b) * (1 + 1e-12)])
    return [None] + [S[r] / T ** r for r in range(1, R + 1)]

def tate_mom(c, j, Mm=120):  # int_{-1}^{1} x^j e^{cx} dx, |c|<1
    s = iv.mpf(0); f = iv.mpf(1)
    for m in range(Mm + 1):
        if m > 0: f = f * c / m
        if (j + m) % 2 == 0: s += f * 2 / (j + m + 1)
    rem = 4 * float(abs(c).b) ** (Mm + 1) / factorial(Mm + 1)
    return s + iv.mpf([-rem, rem])

def atan_small(y, Mm=400):  # alternating series, 0<y<1, remainder |.| <= y^(2Mm+3)/(2Mm+3)
    s = iv.mpf(0); t = y
    for m in range(Mm + 1):
        s += (-1) ** m * t / (2 * m + 1); t = t * y * y
    rem = float(t.b) / (2 * Mm + 3)
    return s + iv.mpf([-rem, rem])

def setup(T, combspec):
    N = iv.exp(2 * T); nmax = int(float(N.b)) + 1
    cont = [(n, p) for n, p in pp(nmax) if float(iv.log(n).a) < float((2 * T).b)]
    a = {}
    for n, p in cont:
        kind, par = combspec
        if kind == 'Lam': val = iv.log(p)
        elif kind == 'cLam': val = (ivf(par) if isinstance(par, Fr) else iv.mpf(par)) * iv.log(p)
        elif kind == 'delq': val = iv.mpf(0) if n == par else iv.log(p)
        elif kind == 'delp': val = iv.mpf(0) if p == par else iv.log(p)
        a[n] = val
    return cont, a

def quotient(T, g, cont, a, mom, R):
    """g: list of iv coefficients of G (index = power). returns enclosure of a_T(F)/||F||^2"""
    p = [iv.mpf(0)] * (R + 1)
    for j, gj in enumerate(g):
        if isinstance(gj, int): continue
        for k, gk in enumerate(g):
            if isinstance(gk, int): continue
            P = Cpoly(j, k)
            for r, c in P.items(): p[r] += gj * gk * ivf(c)
    p = [T * x for x in p]          # c(Ts) = sum p_r s^r
    c0 = p[0]
    C0 = -iv.euler - iv.pi / 2 - 3 * iv.log(2) - iv.log(iv.pi)
    E = -sum(p[r] * mom[r] for r in range(1, R + 1))
    tailK = iv.log((iv.exp(T) + 1) / (iv.exp(T) - 1)) + 2 * atan_small(iv.exp(-T))
    def cval(u):
        s = u / T; v = iv.mpf(0)
        for r in range(R, -1, -1): v = v * s + p[r]
        return v
    comb = sum(2 * a[n] / iv.sqrt(n) * cval(iv.log(n)) for n, _ in cont)
    return (C0 * c0 + E + c0 * tailK - comb) / c0, c0

def galerkin(T, Mdeg, sector, cont, a, mom):
    """non-rigorous: minimiser over monomials x^j, j<Mdeg (odd j only if sector=='odd'); returns float coeffs"""
    idx = [j for j in range(Mdeg) if sector == 'full' or j % 2 == 1]
    m = lambda z: mp.mpf(z.mid) if hasattr(z, 'mid') else mp.mpf(z)
    Tm = m(T); momm = [None] + [m(z) for z in mom[1:]]
    C0 = mp.digamma(mp.mpf(1) / 4) - mp.log(mp.pi); tail = mp.quad(lambda u: 2*mp.e**(-u/2)/(1-mp.e**(-2*u)), [2*Tm, mp.inf])
    am = {n: m(a[n]) for n, _ in cont}; d = len(idx)
    G = mp.matrix(d, d); A = mp.matrix(d, d)
    for i1, j in enumerate(idx):
        for i2, k in enumerate(idx):
            P = Cpoly(j, k); Q = Cpoly(k, j); pol = {r: (P.get(r, 0) + Q.get(r, 0)) / 2 for r in set(P) | set(Q)}
            q = lambda r: mp.mpf(pol[r].numerator) / pol[r].denominator
            g0 = Tm * q(0) if 0 in pol else 0
            E = -Tm * mp.fsum(q(r) * momm[r] for r in pol if r > 0)
            cb = mp.fsum(2 * am[n] / mp.sqrt(n) * Tm * mp.fsum(q(r) * (mp.log(n) / Tm) ** r for r in pol) for n, _ in cont)
            G[i1, i2] = g0; A[i1, i2] = (C0 + tail) * g0 + E - cb
    cons = []
    if sector == 'full':
        cons.append([mp.quad(lambda x: x ** j * mp.e ** (Tm * x / 2), [-1, 1]) for j in idx])
        cons.append([mp.quad(lambda x: x ** j * mp.e ** (-Tm * x / 2), [-1, 1]) for j in idx])
    else:
        cons.append([mp.quad(lambda x: x ** j * mp.sinh(Tm * x / 2), [-1, 1]) for j in idx])
    nc = len(cons)  # eliminate first nc coordinates
    Cm = mp.matrix(cons); B = Cm[:, :nc] if nc > 1 else mp.matrix([[cons[0][0]]])
    Z = mp.matrix(d, d - nc)
    for c in range(nc, d):
        Z[c, c - nc] = 1
        rhs = mp.matrix([cons[i][c] for i in range(nc)]); sol = mp.lu_solve(B, rhs)
        for i in range(nc): Z[i, c - nc] = -sol[i]
    Gz = Z.T * G * Z; Az = Z.T * A * Z; L = mp.cholesky(Gz); Li = mp.inverse(L)
    S = Li * Az * Li.T; S = (S + S.T) / 2; e, V = mp.eigsy(S)
    i0 = min(range(len(e)), key=lambda i: e[i]); y = Li.T * V[:, i0]; h = Z * y
    nrm = max(abs(h[i]) for i in range(d))
    coef = {j: h[i] / nrm for i, j in enumerate(idx)}
    return e[i0], coef, idx

def certify(label, T, combspec, sector, Mdeg):
    cont, a = setup(T, combspec)
    R = 2 * Mdeg + 2
    mom = Kmoments(T, R)
    ev, coef, idx = galerkin(T, Mdeg, sector, cont, a, mom)
    den = 2 ** 40
    fixed = [0, 1] if sector == 'full' else [1]
    g0 = [Fr(0)] * Mdeg
    for j in idx:
        if j not in fixed: g0[j] = Fr(int(mp.nint(coef[j] * den)), den)
    # re-impose Tate moments exactly: full: int G e^{+-Tx/2}=0 ; odd: int G sinh(Tx/2)=0
    if sector == 'full':
        cp, cm = T / 2, -T / 2
        r1 = -sum(ivf(g0[j]) * tate_mom(cp, j) for j in range(Mdeg) if g0[j] != 0)
        r2 = -sum(ivf(g0[j]) * tate_mom(cm, j) for j in range(Mdeg) if g0[j] != 0)
        a11, a12, a21, a22 = tate_mom(cp, 0), tate_mom(cp, 1), tate_mom(cm, 0), tate_mom(cm, 1)
        det = a11 * a22 - a12 * a21
        al = (r1 * a22 - a12 * r2) / det; be = (a11 * r2 - a21 * r1) / det
        g = [ivf(x) if x != 0 else 0 for x in g0]; g[0] = al; g[1] = be
    else:
        sh = lambda j: (tate_mom(T / 2, j) - tate_mom(-T / 2, j)) / 2
        r1 = -sum(ivf(g0[j]) * sh(j) for j in range(Mdeg) if g0[j] != 0)
        g = [ivf(x) if x != 0 else 0 for x in g0]; g[1] = r1 / sh(1)
    Q, c0 = quotient(T, g, cont, a, mom, R)
    ok = float(Q.b) < 0
    print(f"{label}: T in [{mp.nstr(mp.mpf(T.a),12)},{mp.nstr(mp.mpf(T.b),12)}] {sector} deg<{Mdeg} contacts={[n for n,_ in cont]} "
          f"Galerkin~{mp.nstr(ev,8)} | CERT a_T(F)/||F||^2 in [{mp.nstr(mp.mpf(Q.a),10)}, {mp.nstr(mp.mpf(Q.b),10)}] "
          f"width {mp.nstr(mp.mpf(Q.b-Q.a),2)} {'NEGATIVE: PROVED' if ok else 'NOT CERTIFIED'}", flush=True)
    return ok

if __name__ == '__main__':
    h5 = iv.log(5) / 2
    jobs = [
        ("Y1 delete q=3, T=0.75", iv.mpf(3) / 4, ('delq', 3), 'full', 14),
        ("Y1 delete q=3, T=1/2log5+0.01", h5 + iv.mpf(1) / 100, ('delq', 3), 'full', 14),
        ("Y1 top-layer delete q=7, T=1", iv.mpf(1), ('delq', 7), 'full', 14),
        ("Y1 top-layer delete q=8, T=log3", iv.log(3), ('delq', 8), 'full', 14),
        ("AA odd, zero comb, T=1/2log5", h5, ('cLam', 0), 'odd', 24),
        ("AA odd, zero comb, T=1", iv.mpf(1), ('cLam', 0), 'odd', 24),
        ("AA odd, a_2 (p=2 deleted), T=1", iv.mpf(1), ('delp', 2), 'odd', 24),
        ("AA odd, 2Lambda, T=1", iv.mpf(1), ('cLam', 2), 'odd', 24),
        ("AA odd, a_3 (p=3 deleted), T=1/2log5", h5, ('delp', 3), 'odd', 24),
        ("AA odd, 1.15Lambda, T=1", iv.mpf(1), ('cLam', Fr(115, 100)), 'odd', 24),
    ]
    sel = sys.argv[1:] and [int(x) for x in sys.argv[1].split(',')]
    for i, jb in enumerate(jobs):
        if not sel or i in sel: certify(*jb)
