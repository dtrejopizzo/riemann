"""LEMMA_12_1_H3_001 (phase 200, round 13). D=-23, h=3. Exact arithmetic (Fraction) of r_Q, Lambda_Q, Lambda_K, Lambda_L;
pairing with the T=8/5 witness from Lemma E (certified vector cert_T1.6_full49.txt + Tate correction). NUMERICAL (float at the end)."""
import os, sys, ast, numpy as np
from fractions import Fraction as Fr
from math import isqrt
from sympy import factorint, jacobi_symbol
HERE = os.path.dirname(os.path.abspath(__file__)); LE = os.path.join(HERE, '../LEMMA_E_EPSTEIN_001_data')
sys.path.insert(0, LE); os.chdir(LE); os.environ.setdefault('IVDPS', '60')
import cert_epstein as C
from cert_epstein import iv, ivf, tate_mom, Cpoly
NMAX = 2000
def rQ(a, b, c, N):
    r = [0] * (N + 1); B = isqrt(4 * N) + 3
    for x in range(-B, B + 1):
        for y in range(-B, B + 1):
            v = a * x * x + b * x * y + c * y * y
            if 0 < v <= N: r[v] += 1
    return r
r1 = rQ(1, 1, 6, NMAX); r2 = rQ(2, 1, 3, NMAX); r3 = rQ(2, -1, 3, NMAX)
assert r2 == r3
chi = lambda n: 0 if n % 23 == 0 else int(jacobi_symbol(n % 23, 23))  # kronecker(-23,n)=(n/23) for n odd; check 2 below
def kr(n):  # kronecker symbol (-23/n), multiplicative
    out = 1
    for p, k in factorint(n).items():
        if p == 2: v = 1   # -23 = 1 mod 8
        else: v = chi(p)
        out *= v ** k
    return out
rK = [0] + [sum(kr(d) for d in range(1, n + 1) if n % d == 0) for n in range(1, NMAX + 1)]  # #ideals of norm n
aL = [0] + [(r1[n] - r2[n]) // 2 for n in range(1, NMAX + 1)]
# checks: Z_Q1 = (2/3)(zeta_K + 2L), Z_Q2 = (2/3)(zeta_K - L)  (w=2,h=3; L real since chi(abar)=conj chi(a))
assert all(3 * r1[n] == 2 * (rK[n] + 2 * aL[n]) for n in range(1, NMAX + 1))
assert all(3 * r2[n] == 2 * (rK[n] - aL[n]) for n in range(1, NMAX + 1))
# eta(z)eta(23z) coefficients (CITED identity, checked here)
M = 400; poly = [0] * (M + 1); poly[0] = 1
def mul1(k):  # multiply by (1-q^k)
    for i in range(M, k - 1, -1): poly[i] -= poly[i - k]
for n in range(1, M + 1): mul1(n)
for n in range(1, M // 23 + 1): mul1(23 * n)
eta = [0] + poly[:M]  # q * prod
assert all(eta[n] == aL[n] for n in range(1, M + 1)), 'eta mismatch'
print('checks OK: Z_Q1=(2/3)(zK+2L), Z_Q2=(2/3)(zK-L), L=eta(z)eta(23z) coeffs to', M)
print('r_Q1(n<=30):', r1[1:31]); print('r_Q2(n<=30):', r2[1:31]); print('a_L(n<=30):', aL[1:31])
# ---- log-derivative on generalized Dirichlet series (frequencies Fraction q>=1), truncated at QMAX
QMAX = Fr(25)
def logderiv(coef):  # coef: dict n->int, returns (m0, {q: Lambda(q) as float}) with -Z'/Z = log m0 + sum Lambda(q) q^-s
    m0 = min(n for n, v in coef.items() if v); a0 = coef[m0]
    E = {Fr(n, m0): Fr(v, a0) for n, v in coef.items() if v and n != m0 and Fr(n, m0) <= QMAX}
    logB = {}; P = {Fr(1): Fr(1)}
    for k in range(1, 40):
        Pn = {}
        for q1, u in P.items():
            for q2, v in E.items():
                q = q1 * q2
                if q <= QMAX: Pn[q] = Pn.get(q, 0) + u * v
        P = Pn
        if not P: break
        for q, v in P.items(): logB[q] = logB.get(q, 0) + Fr((-1) ** (k + 1), k) * v
    return m0, {q: float(v) * np.log(float(q)) for q, v in logB.items() if v != 0}, logB
coefK = {n: rK[n] for n in range(1, 30)}; coefL = {n: aL[n] for n in range(1, 30)}
coef1 = {n: r1[n] for n in range(1, 30)}; coef2 = {n: r2[n] for n in range(1, 30)}
_, LamK, lK = logderiv(coefK); _, LamL, lL = logderiv(coefL)
_, Lam1, l1 = logderiv(coef1); m02, Lam2, l2 = logderiv(coef2)
print('Lambda_K:', {str(q): round(v, 4) for q, v in sorted(LamK.items())})
print('Lambda_L:', {str(q): round(v, 4) for q, v in sorted(LamL.items())})
print('Lambda_Q1:', {str(q): round(v, 4) for q, v in sorted(Lam1.items())})
print('m0(Q2)=', m02, 'Lambda_Q2 (q=n/2^k):', {str(q): round(v, 4) for q, v in sorted(Lam2.items())})
# ---- witness (identical to COSH_DEFECT_001)
txt = open('cert_T1.6_full49.txt').read()
g0 = [Fr(x) for x in ast.literal_eval(txt.split('(x^0..):')[1].strip())]
T = iv.mpf(8) / 5; Mdeg = len(g0); R = 2 * Mdeg + 2; cp, cm = T / 2, -T / 2
r1_ = -sum(ivf(g0[j]) * tate_mom(cp, j) for j in range(Mdeg) if g0[j] != 0)
r2_ = -sum(ivf(g0[j]) * tate_mom(cm, j) for j in range(Mdeg) if g0[j] != 0)
a11, a12, a21, a22 = tate_mom(cp, 0), tate_mom(cp, 1), tate_mom(cm, 0), tate_mom(cm, 1); det = a11 * a22 - a12 * a21
g = [ivf(x) if x != 0 else 0 for x in g0]; g[0] = (r1_ * a22 - a12 * r2_) / det; g[1] = (a11 * r2_ - a21 * r1_) / det
mom = C.Kmoments(T, R)
_, _, pcs = C.quotient(T, g, [], mom, R, pieces=True)
levy = float(pcs['levy'].mid)
C0 = float((iv.log(23) - 2 * iv.euler - 6 * iv.log(2) - 2 * iv.log(iv.pi)).mid)
p = [iv.mpf(0)] * (R + 1)
for j, gj in enumerate(g):
    if isinstance(gj, int): continue
    for k, gk in enumerate(g):
        if isinstance(gk, int): continue
        for r, c in Cpoly(j, k).items(): p[r] += gj * gk * ivf(c)
p = [T * x for x in p]; c0 = p[0]
def cval(u):
    s = u / T; v = iv.mpf(0)
    for r in range(R, -1, -1): v = v * s + p[r]
    return float((v / c0).mid)
cache = {}
def cq(q):
    if q not in cache: cache[q] = cval(iv.log(iv.mpf(q.numerator) / q.denominator)) if q < Fr(int(np.exp(3.2) * 1000), 1000) else 0.0
    return cache[q]
def comb(Lam): return sum(2 * v / np.sqrt(float(q)) * cq(q) for q, v in Lam.items() if float(q) < np.exp(3.2))
def form(Lam, m0=1): return C0 + levy - 2 * np.log(m0) - comb(Lam)
aK, aL_, a1, a2 = form(LamK), form(LamL), form(Lam1), form(Lam2, m02)
base = aK / 3 + 2 * aL_ / 3
print('C0=%.6f levy=%.6f' % (C0, levy))
print('a^K=%.6f a^L=%.6f base(1/3 K+2/3 L)=%.6f' % (aK, aL_, base))
print('a^Q1=%.6f  D1=a^Q1-base=%.6f' % (a1, a1 - base))
print('a^Q2=%.6f  D2=a^Q2-base=%.6f ; a^Q2-a^K=%.6f' % (a2, a2 - base, a2 - aK))
# ---- order expansion for principal class: y = log L - log zeta_K (Dirichlet series in n), X in {2/3 (K-slot? ) }
# (zK+2L)/3 = zK^{1/3} L^{2/3} * E[e^{yX}], X = -2/3 (prob 1/3, slot K), +1/3 (prob 2/3, slot L), y = log L - log zK
yv = {q: lL.get(q, 0) - lK.get(q, 0) for q in set(lL) | set(lK)}; yv = {q: v for q, v in yv.items() if v}
print('y = log L - log zeta_K coefs:', {str(q): str(v) for q, v in sorted(yv.items())})
def conv(x, z):
    o = {}
    for a, u in x.items():
        for b, v in z.items():
            if a * b <= QMAX: o[a * b] = o.get(a * b, 0) + u * v
    return o
# cumulants of X: k2 = 2/9, k3 = E[X^3] = 1/3(-8/27)+2/3(1/27) = -2/27, k4 = E X^4 - 3 k2^2 = (1/3)(16/81)+(2/3)(1/81) - 3*4/81 = 18/243 - 12/81 = -18/243
yp = {1: yv}
for j in range(2, 9): yp[j] = conv(yp[j - 1], yv)
# exact cumulant series: log E[e^{tX}] coefficients via series
from sympy import symbols, exp, log, series, Rational
t = symbols('t'); cg = series(log(Rational(1, 3) * exp(-Rational(2, 3) * t) + Rational(2, 3) * exp(Rational(1, 3) * t)), t, 0, 9).removeO()
kap = {j: Fr(str(cg.coeff(t, j))) for j in range(1, 9)}; print('cumulant-gen coeffs kappa_j/j!:', {j: str(v) for j, v in kap.items()})
ordr = {j: {q: float(kap[j] * v) * np.log(float(q)) for q, v in yp[j].items() if kap[j] != 0} for j in range(1, 9)}
recon = {}
for j in ordr:
    for q, v in ordr[j].items(): recon[q] = recon.get(q, 0) + v
Ldef1 = {q: Lam1.get(q, 0) - (LamK.get(q, 0) / 3 + 2 * LamL.get(q, 0) / 3) for q in set(Lam1) | set(LamK) | set(LamL)}
print('check Lambda_def1 = sum orders, max err:', max(abs(Ldef1.get(q, 0) - recon.get(q, 0)) for q in set(Ldef1) | set(recon)))
D1parts = {j: -comb(ordr[j]) for j in ordr}
print('D1 by order:', {j: round(v, 6) for j, v in D1parts.items()})
print('order-2 terms per n:', {str(q): round(-2 * v / np.sqrt(float(q)) * cq(q), 5) for q, v in sorted(ordr[2].items()) if float(q) < np.exp(3.2)})
print('Lambda_def1 per n:', {str(q): round(v, 4) for q, v in sorted(Ldef1.items()) if abs(v) > 1e-12})
# Hankel form for principal: Q^(3)_g[y] = (2/9) sum_{m,n} y_m y_n w(mn)  (b := y/3 * sqrt2 ... ) ; also variance form (1/h) sum_chi <y_chi*y_chi,w>
w = lambda q: np.log(float(q)) / np.sqrt(float(q)) * cq(q)
S = sorted(q for q in yv if q <= 12)
H = np.array([[w(a * b) if float(a * b) < np.exp(3.2) else 0 for b in S] for a in S])
yvec = np.array([float(yv[q]) for q in S])
print('support', [str(q) for q in S], 'eigs', np.round(np.linalg.eigvalsh(H), 4), 'k2*y^T H y =', float(kap[2]) * 2 * (yvec @ H @ yvec) / 2)
# ---- non-principal: (zK - L)/3 = zK^{1/3}L^{2/3} * E[s(X) e^{yX}], weights chibar(C) = (1, -1/2, -1/2): log(1/3 e^{-2y/3} - 1/3 e^{y/3})
Ldef2 = {q: Lam2.get(q, 0) - (LamK.get(q, 0) / 3 + 2 * LamL.get(q, 0) / 3) for q in set(Lam2) | set(LamK) | set(LamL)}
print('Lambda_def2 per q (+ constant log 2 at q=1):', {str(q): round(v, 4) for q, v in sorted(Ldef2.items()) if abs(v) > 1e-12})
print('D2 split: -2log2 =%.6f ; comb part=%.6f' % (-2 * np.log(2), -comb(Ldef2)))
# linear leading: zK - L = -(e^{y}-1) zK ; M = -y; log(-y) = log(b_2 2^-s) + log(1 + y'/b_2...) handled exactly above
