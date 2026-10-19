#!/usr/bin/env python3
"""LEMMA_E_EPSTEIN_001: window form of the Epstein zeta Z_Q, Q=x^2+5y^2, and interval certificates of negativity.
Lambda_Q(s) = (sqrt20/2pi)^s Gamma(s) Z_Q(s) = 1/2 * 20^{s/2} Gamma_R(s) Gamma_R(s+1) Z_Q(s) = Lambda_Q(1-s).
Window form (same template as P47 eq:Aform, Gamma_R(s) -> Gamma_R(s)Gamma_R(s+1), conductor 20):
  a^Q_T(F) = C0Q c(0) + int_0^{2T}(c(0)-c(u))KQ(u)du + c(0) int_{2T}^inf KQ - sum_{log n<2T} vQ_n c(log n),
  KQ(u) = 1/sinh(u/2) = 2 sum_k e^{-(k+1/2)u}  (= K_{1/4}+K_{3/4}),  int_{2T}^inf KQ = 2 log coth(T/2),
  C0Q = log 20 + psi(1/4)+psi(3/4) - 2 log pi = log 20 - 2gamma - 6log2 - 2log pi,  vQ_n = 2 Lambda_Q(n)/sqrt n.
P_T: F supported in [-T,T], int F e^{+-t/2} = 0 (poles of Lambda_Q at s=0,1, exactly as for zeta).
Rigour as in phase-198 cert_falsifiers.py (mpmath.iv, outward rounding); Lambda_Q(n) exact (sum of rational*log p).
Usage: python3 cert_epstein.py scan | cert T_num T_den sector Mdeg"""
import sys, os, json, mpmath as mp
from mpmath import iv
from fractions import Fraction as Fr
from math import factorial
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../phase-198-parity-split/scripts'))
from cert_falsifiers import Cpoly, ivf, tate_mom
iv.dps = int(os.environ.get("IVDPS", "60")); mp.mp.dps = int(os.environ.get("DPS", "40"))
NK = 6000
LQ = {int(n): {int(p): Fr(q) for p, q in d.items()} for n, d in
      json.load(open(os.path.join(os.path.dirname(__file__), 'lambdaQ_exact.json'))).items()}
def _kron20(n):
    from sympy import jacobi_symbol
    return 0 if n % 2 == 0 or n % 5 == 0 else jacobi_symbol(-20 % n, n) if n > 1 else 1
def _LK(nmax):  # Dedekind zeta of Q(sqrt-5): Lambda_K(p^k) = log p (1 + chi_-20(p)^k)
    from sympy import factorint
    out = {}
    for n in range(2, nmax + 1):
        f = factorint(n)
        if len(f) == 1:
            p, k = list(f.items())[0]; c = 1 + (0 if p in (2, 5) else _kron20(p)) ** k
            if c: out[n] = {p: Fr(c)}
    return out
COMB = os.environ.get('COMB', 'Q')   # Q | K | Qprime (Lambda_Q on prime powers only) | Kcomp (Lambda_K + composite part of Lambda_Q)
if COMB != 'Q':
    from sympy import factorint as _fi
    _K = _LK(max(LQ)); _comp = {n: d for n, d in LQ.items() if len(_fi(n)) > 1}
    LQ = {'K': _K, 'Qprime': {n: d for n, d in LQ.items() if len(_fi(n)) == 1}, 'Kcomp': {**_K, **_comp}}[COMB]

def Kmoments(T, R):
    """rigorous int_0^{2T} (u/T)^r KQ(u) du, KQ = 2 sum_k e^{-(k+1/2)u}"""
    L = 2 * T; S = [iv.mpf(0)] * (R + 1)
    for k in range(NK):
        a = iv.mpf(k) + iv.mpf(1) / 2; x = a * L; xm = float(x.b)
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
    aN = NK + 0.5   # sum_{k>=NK} 2 r!/a_k^{r+1}, a_k spacing 1, decreasing: in [2r! aN^{-r}/r, 2r!(aN^{-r}/r + aN^{-r-1})]
    for r in range(1, R + 1):
        I = iv.mpf(aN) ** (-r) / r; lo_ = 2 * factorial(r) * I; hi_ = 2 * factorial(r) * (I + iv.mpf(aN) ** (-(r + 1)))
        S[r] += iv.mpf([float(lo_.a) * (1 - 1e-12) - 1e-300, float(hi_.b) * (1 + 1e-12)])
    return [None] + [S[r] / T ** r for r in range(1, R + 1)]

def contacts(T):
    out = []
    for n in sorted(LQ):
        if float(iv.log(n).a) < float((2 * T).b):
            assert float(iv.log(n).b) < float((2 * T).a), 'contact undecided'
            out.append(n)
    return out
def LamQ_iv(n): return sum(ivf(q) * iv.log(p) for p, q in LQ[n].items())

def quotient(T, g, cont, mom, R, pieces=False):
    p = [iv.mpf(0)] * (R + 1)
    for j, gj in enumerate(g):
        if isinstance(gj, int): continue
        for k, gk in enumerate(g):
            if isinstance(gk, int): continue
            for r, c in Cpoly(j, k).items(): p[r] += gj * gk * ivf(c)
    p = [T * x for x in p]; c0 = p[0]
    C0Q = iv.log(20) - 2 * iv.euler - 6 * iv.log(2) - 2 * iv.log(iv.pi)
    E = -sum(p[r] * mom[r] for r in range(1, R + 1))
    tailK = 2 * iv.log((iv.exp(T) + 1) / (iv.exp(T) - 1))
    def cval(u):
        s = u / T; v = iv.mpf(0)
        for r in range(R, -1, -1): v = v * s + p[r]
        return v
    terms = {n: 2 * LamQ_iv(n) / iv.sqrt(n) * cval(iv.log(n)) for n in cont}
    comb = sum(terms.values()) if terms else iv.mpf(0)
    Q = (C0Q * c0 + E + c0 * tailK - comb) / c0
    if pieces: return Q, c0, {'const': C0Q, 'levy': (E + c0 * tailK) / c0, 'comb': comb / c0, 'terms': {n: t / c0 for n, t in terms.items()}}
    return Q, c0

def galerkin(T, Mdeg, sector, cont):
    idx = [j for j in range(Mdeg) if sector == 'full' or j % 2 == 1]
    Tm = mp.mpf(T.mid) if hasattr(T, 'mid') else mp.mpf(T)
    KQ = lambda u: 1 / mp.sinh(u / 2)
    mom = [None] + [mp.quad(lambda u: (u / Tm) ** r * KQ(u), [0, Tm, 2 * Tm]) for r in range(1, 2 * Mdeg + 2)]
    C0 = mp.log(20) - 2 * mp.euler - 6 * mp.log(2) - 2 * mp.log(mp.pi); tail = 2 * mp.log(mp.coth(Tm / 2))
    am = {n: mp.mpf(float(0)) + sum(mp.mpf(q.numerator) / q.denominator * mp.log(pr) for pr, q in LQ[n].items()) for n in cont}
    d = len(idx); G = mp.matrix(d, d); A = mp.matrix(d, d)
    for i1, j in enumerate(idx):
        for i2, k in enumerate(idx):
            P = Cpoly(j, k); Q = Cpoly(k, j); pol = {r: (P.get(r, 0) + Q.get(r, 0)) / 2 for r in set(P) | set(Q)}
            q = lambda r: mp.mpf(pol[r].numerator) / pol[r].denominator
            g0 = Tm * q(0) if 0 in pol else 0
            E = -Tm * mp.fsum(q(r) * mom[r] for r in pol if r > 0)
            cb = mp.fsum(2 * am[n] / mp.sqrt(n) * Tm * mp.fsum(q(r) * (mp.log(n) / Tm) ** r for r in pol) for n in cont)
            G[i1, i2] = g0; A[i1, i2] = (C0 + tail) * g0 + E - cb
    if sector == 'full':
        cons = [[mp.quad(lambda x: x ** j * mp.e ** (s * Tm * x / 2), [-1, 1]) for j in idx] for s in (1, -1)]
    else:
        cons = [[mp.quad(lambda x: x ** j * mp.sinh(Tm * x / 2), [-1, 1]) for j in idx]]
    nc = len(cons); Cm = mp.matrix(cons); B = Cm[:, :nc]
    Z = mp.matrix(d, d - nc)
    for c in range(nc, d):
        Z[c, c - nc] = 1; sol = mp.lu_solve(B, mp.matrix([cons[i][c] for i in range(nc)]))
        for i in range(nc): Z[i, c - nc] = -sol[i]
    Gz = Z.T * G * Z; Az = Z.T * A * Z; L = mp.cholesky(Gz); Li = mp.inverse(L)
    S = Li * Az * Li.T; S = (S + S.T) / 2; e, V = mp.eigsy(S)
    i0 = min(range(len(e)), key=lambda i: e[i]); h = Z * (Li.T * V[:, i0])
    nrm = max(abs(h[i]) for i in range(d))
    return e[i0], {j: h[i] / nrm for i, j in enumerate(idx)}, idx

def certify(T, sector, Mdeg, label=''):
    cont = contacts(T); R = 2 * Mdeg + 2; mom = Kmoments(T, R)
    ev, coef, idx = galerkin(T, Mdeg, sector, cont)
    den = 2 ** int(os.environ.get("DENBITS", "40")); fixed = [0, 1] if sector == 'full' else [1]
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
    print(f"{label} T~{mp.nstr(mp.mpf(T.mid),12)} {sector} deg<{Mdeg} contacts={cont} Galerkin~{mp.nstr(ev,10)} | CERT "
          f"aQ_T(F)/||F||^2 in [{mp.nstr(mp.mpf(Q.a),12)}, {mp.nstr(mp.mpf(Q.b),12)}] "
          f"{'NEGATIVE: PROVED' if float(Q.b) < 0 else 'not negative'} | pieces const {f(pc['const'])} levy {f(pc['levy'])} "
          f"comb {f(pc['comb'])} terms { {n: f(t) for n, t in pc['terms'].items()} }", flush=True)
    print('  G numerators (rational) (x^0..):', [str(x) for x in g0], flush=True)
    return Q

def scan_value(T, sector, Mdeg):
    return galerkin(iv.mpf(T), Mdeg, sector, contacts(iv.mpf(T)))[0]

if __name__ == '__main__':
    if sys.argv[1] == 'scan':
        sec = sys.argv[2]; Md = int(sys.argv[3])
        for Tv in [float(x) for x in sys.argv[4].split(',')]:
            mp.mp.dps = int(os.environ.get("DPS", "40"))
            print(sec, Md, Tv, mp.nstr(scan_value(Tv, sec, Md), 10), flush=True)
    else:
        T = iv.mpf(int(sys.argv[2])) / int(sys.argv[3]); certify(T, sys.argv[4], int(sys.argv[5]), sys.argv[6] if len(sys.argv) > 6 else '')
