#!/usr/bin/env python3
"""CERT_DH_001: window form of the Davenport-Heilbronn function F_DH on P_T and interval certificate of negativity.
Template = P47 eq:Aform / CERT_FALSIFIERS 'Method' / LEMMA_E cert_epstein.py, with (C0,K,v) -> (C0^DH, K_{3/4}, v^DH):
  a^DH_T(F) = C0 c(0) + int_0^{2T}(c(0)-c(u))K(u)du + c(0) int_{2T}^inf K - sum_{log n<2T} v_n c(log n)
  C0 = log(5/pi) + psi(3/4) = log5 - log pi - gamma + pi/2 - 3 log2,  K(u) = 2 sum_k e^{-(2k+3/2)u},
  v_n = 2 b_n/sqrt n,  -F'/F = sum b_n n^{-s}  (b_n real, of both signs; recursion b_n = a_n log n - sum_{d|n,d>1} a_d b_{n/d}).
  Comb is a FINITE sum (n < e^{2T}): no comb tail. Levy part: rigorous series + explicit tail (spacing 2).
P_T: supp F in [-T,T], int F e^{+-t/2} = 0 (corpus convention; no pole). Sector 'odd': F odd, only sinh moment.
Usage: python3 cert_dh.py scan sector Mdeg T1,T2,... | cert Tnum Tden sector Mdeg [label]"""
import sys, os, mpmath as mp
from mpmath import iv
from fractions import Fraction as Fr
from math import factorial
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../phase-198-parity-split/scripts'))
from cert_falsifiers import Cpoly, ivf, tate_mom
iv.dps = int(os.environ.get("IVDPS", "60")); mp.mp.dps = int(os.environ.get("DPS", "40"))
NK = 3000; CHI = {1: (1, 0), 2: (0, 1), 3: (0, -1), 4: (-1, 0), 0: (0, 0)}  # (Re chi, Im chi), chi(2)=i
def kappa_iv():
    s5 = iv.sqrt(5); return (iv.sqrt(10 - 2 * s5) - 2) / (s5 - 1)
def a_iv(n, k):   # a_n = Re chi(n) + kappa Im chi(n)
    re, im = CHI[n % 5]; return iv.mpf(re) + k * im
_B = {}
def b_iv(nmax):
    k = kappa_iv()
    for n in range(2, nmax + 1):
        if n in _B: continue
        _B[n] = a_iv(n, k) * iv.log(n) - sum((a_iv(d, k) * _B[n // d] for d in range(2, n) if n % d == 0), iv.mpf(0))
    return _B
def C0_iv(): return iv.log(5) - iv.log(iv.pi) - iv.euler + iv.pi / 2 - 3 * iv.log(2)
def Kmoments(T, R):
    """rigorous int_0^{2T} (u/T)^r K(u) du, K = 2 sum_k e^{-(2k+3/2)u}"""
    L = 2 * T; S = [iv.mpf(0)] * (R + 1)
    for kk in range(NK):
        a = iv.mpf(2 * kk) + iv.mpf(3) / 2; x = a * L; xm = float(x.b)
        for r in range(1, R + 1):
            if xm <= r + 1:
                term = iv.mpf(1) / (r + 1); s = term; m = 0
                while True:
                    m += 1; term = term * x / (r + 1 + m); s += term
                    if float(term.b) < 1e-70 and m > 2 * xm: break
                s = s + iv.mpf([0, float(term.b) * 1.0000001])
                g = x ** (r + 1) * iv.exp(-x) * s
            else:
                t = iv.mpf(1); sm = iv.mpf(1)
                for i in range(1, r + 1): t = t * x / i; sm += t
                g = factorial(r) * (1 - iv.exp(-x) * sm)
            S[r] += 2 * g / a ** (r + 1)
    aN = 2 * NK + 1.5   # sum_{k>=NK} 2 r!/a_k^{r+1}, spacing 2: in [2r! aN^{-r}/(2r), 2r!(aN^{-r}/(2r) + aN^{-r-1})]
    for r in range(1, R + 1):
        I = iv.mpf(aN) ** (-r) / (2 * r); lo_ = 2 * factorial(r) * I; hi_ = 2 * factorial(r) * (I + iv.mpf(aN) ** (-(r + 1)))
        S[r] += iv.mpf([float(lo_.a) * (1 - 1e-12) - 1e-300, float(hi_.b) * (1 + 1e-12)])
    return [None] + [S[r] / T ** r for r in range(1, R + 1)]
def tailK_iv(T, M=400):   # int_{2T}^inf K = 2 sum_k e^{-2T a_k}/a_k ; remainder <= 2 e^{-2T a_M}/(a_M (1-e^{-4T}))
    s = iv.mpf(0)
    for kk in range(M):
        a = iv.mpf(2 * kk) + iv.mpf(3) / 2; s += 2 * iv.exp(-2 * T * a) / a
    aM = iv.mpf(2 * M) + iv.mpf(3) / 2; rem = 2 * iv.exp(-2 * T * aM) / (aM * (1 - iv.exp(-4 * T)))
    return s + iv.mpf([0, float(rem.b)])
def contacts(T):
    nmax = int(float(iv.exp(2 * T).b)) + 1; out = []
    for n in range(2, nmax + 1):
        if float(iv.log(n).a) < float((2 * T).b):
            assert float(iv.log(n).b) < float((2 * T).a), 'contact undecided'
            out.append(n)
    return out
def quotient(T, g, cont, mom, R, pieces=False):
    B = b_iv(max(cont) if cont else 2)
    p = [iv.mpf(0)] * (R + 1)
    for j, gj in enumerate(g):
        if isinstance(gj, int): continue
        for k, gk in enumerate(g):
            if isinstance(gk, int): continue
            for r, c in Cpoly(j, k).items(): p[r] += gj * gk * ivf(c)
    p = [T * x for x in p]; c0 = p[0]
    E = -sum(p[r] * mom[r] for r in range(1, R + 1)); tK = tailK_iv(T)
    def cval(u):
        s = u / T; v = iv.mpf(0)
        for r in range(R, -1, -1): v = v * s + p[r]
        return v
    terms = {n: 2 * B[n] / iv.sqrt(n) * cval(iv.log(n)) for n in cont}
    comb = sum(terms.values()) if terms else iv.mpf(0)
    Q = (C0_iv() * c0 + E + c0 * tK - comb) / c0
    return Q, c0, {'const': C0_iv(), 'levy': (E + c0 * tK) / c0, 'comb': comb / c0, 'terms': {n: t / c0 for n, t in terms.items()}}
def galerkin(Tm, Mdeg, sector, cont):
    idx = [j for j in range(Mdeg) if sector == 'full' or j % 2 == 1]
    K = lambda u: 2 * mp.exp(-1.5 * u) / (1 - mp.exp(-2 * u))
    mom = [None] + [mp.quad(lambda u: (u / Tm) ** r * K(u), [0, Tm, 2 * Tm]) for r in range(1, 2 * Mdeg + 2)]
    s5 = mp.sqrt(5); kap = (mp.sqrt(10 - 2 * s5) - 2) / (s5 - 1)
    bb = {}
    for n in range(2, (max(cont) if cont else 2) + 1):
        re, im = CHI[n % 5]
        bb[n] = (re + kap * im) * mp.log(n) - mp.fsum((CHI[d % 5][0] + kap * CHI[d % 5][1]) * bb[n // d] for d in range(2, n) if n % d == 0)
    C0 = mp.log(5 / mp.pi) + mp.digamma(mp.mpf(3) / 4)
    tail = mp.quad(K, [2 * Tm, mp.inf])
    d = len(idx); G = mp.matrix(d, d); A = mp.matrix(d, d)
    for i1, j in enumerate(idx):
        for i2, k in enumerate(idx):
            P = Cpoly(j, k); Q = Cpoly(k, j); pol = {r: (P.get(r, 0) + Q.get(r, 0)) / 2 for r in set(P) | set(Q)}
            q = lambda r: mp.mpf(pol[r].numerator) / pol[r].denominator
            g0 = Tm * q(0) if 0 in pol else 0
            E = -Tm * mp.fsum(q(r) * mom[r] for r in pol if r > 0)
            cb = mp.fsum(2 * bb[n] / mp.sqrt(n) * Tm * mp.fsum(q(r) * (mp.log(n) / Tm) ** r for r in pol) for n in cont)
            G[i1, i2] = g0; A[i1, i2] = (C0 + tail) * g0 + E - cb
    if sector == 'full':
        cons = [[mp.quad(lambda x: x ** j * mp.e ** (s * Tm * x / 2), [-1, 1]) for j in idx] for s in (1, -1)]
    else:
        cons = [[mp.quad(lambda x: x ** j * mp.sinh(Tm * x / 2), [-1, 1]) for j in idx]]
    if sector.endswith('free'): cons = []   # variant without P_T moment conditions
    nc = len(cons); Z = mp.eye(d) if nc == 0 else mp.matrix(d, d - nc)
    if nc:
        Bm = mp.matrix(cons)[:, :nc]
        for c in range(nc, d):
            Z[c, c - nc] = 1; sol = mp.lu_solve(Bm, mp.matrix([cons[i][c] for i in range(nc)]))
            for i in range(nc): Z[i, c - nc] = -sol[i]
    Gz = Z.T * G * Z; Az = Z.T * A * Z; L = mp.cholesky(Gz); Li = mp.inverse(L)
    S = Li * Az * Li.T; S = (S + S.T) / 2; e, V = mp.eigsy(S)
    i0 = min(range(len(e)), key=lambda i: e[i]); h = Z * (Li.T * V[:, i0])
    nrm = max(abs(h[i]) for i in range(d))
    return e[i0], {j: h[i] / nrm for i, j in enumerate(idx)}, idx
def certify(T, Tm, sector, Mdeg, label=''):
    cont = contacts(T); R = 2 * Mdeg + 2; mom = Kmoments(T, R)
    ev, coef, idx = galerkin(Tm, Mdeg, sector, cont)
    nb = int(os.environ.get("DENBITS", "60")); den = 2 ** nb; fixed = [0, 1] if sector == 'full' else [1]
    g0 = [Fr(0)] * Mdeg
    for j in idx:
        if j not in fixed: g0[j] = Fr(int(mp.nint(coef[j] * den)), den)
    if sector == 'full':
        cp, cm = T / 2, -T / 2
        r1 = -sum(ivf(g0[j]) * tate_mom(cp, j) for j in range(Mdeg) if g0[j] != 0)
        r2 = -sum(ivf(g0[j]) * tate_mom(cm, j) for j in range(Mdeg) if g0[j] != 0)
        a11, a12, a21, a22 = tate_mom(cp, 0), tate_mom(cp, 1), tate_mom(cm, 0), tate_mom(cm, 1)
        det = a11 * a22 - a12 * a21
        g = [ivf(x) if x != 0 else 0 for x in g0]; g[0] = (r1 * a22 - a12 * r2) / det; g[1] = (a11 * r2 - a21 * r1) / det
    else:
        sh = lambda j: (tate_mom(T / 2, j) - tate_mom(-T / 2, j)) / 2
        r1 = -sum(ivf(g0[j]) * sh(j) for j in range(Mdeg) if g0[j] != 0)
        g = [ivf(x) if x != 0 else 0 for x in g0]; g[1] = r1 / sh(1)
    Q, c0, pc = quotient(T, g, cont, mom, R, pieces=True)
    f = lambda z: mp.nstr(mp.mpf(z.mid), 10)
    print(f"{label} T={mp.nstr(mp.mpf(T.mid),12)} {sector} deg<{Mdeg} #contacts={len(cont)} Galerkin~{mp.nstr(ev,10)} | CERT "
          f"aDH_T(F)/||F||^2 in [{mp.nstr(mp.mpf(Q.a),15)}, {mp.nstr(mp.mpf(Q.b),15)}] "
          f"{'NEGATIVE: PROVED' if float(Q.b) < 0 else 'not negative'} | const {f(pc['const'])} levy {f(pc['levy'])} comb {f(pc['comb'])}", flush=True)
    print(f'  G(x)=sum g_j x^j, F(t)=G(t/T); numerators over 2^{nb}; g_1 solved in intervals from the sinh condition (full: g_0,g_1):')
    print('  ', [str(x) for x in g0], flush=True)
    return Q
if __name__ == '__main__':
    if sys.argv[1] == 'scan':
        sec = sys.argv[2]; Md = int(sys.argv[3])
        for Tv in [mp.mpf(x) for x in sys.argv[4].split(',')]:
            print(sec, Md, mp.nstr(Tv, 8), mp.nstr(galerkin(Tv, Md, sec, contacts(iv.mpf(str(Tv))))[0], 10), flush=True)
    else:
        T = iv.mpf(int(sys.argv[2])) / int(sys.argv[3]); Tm = mp.mpf(int(sys.argv[2])) / int(sys.argv[3])
        certify(T, Tm, sys.argv[4], int(sys.argv[5]), sys.argv[6] if len(sys.argv) > 6 else '')
