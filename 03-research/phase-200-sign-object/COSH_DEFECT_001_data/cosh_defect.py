"""COSH_DEFECT_001 (phase 200, round 8). NUMERICAL except for the exact coefficient arithmetic.
(1) Exact b_n of y = 1/2 log(L_psi/zeta_K); exact Lambda_cosh; quadratic part 1/2 log n (b*b)(n).
(2) Lemma E witness (T=8/5): c(log n)/c(0) of the certified vector; Q_g[b], total defect, R4.
(3) Multiplicative Hankel matrix H_{mn} = w_g(mn) on the support of b; eigenvalues.
(4) Indefiniteness in g: max/min of g -> Q_g[b]/||g||^2 over P_T (Legendre, float).
(5) Mori extremal mu=15: Q_{g*}[b] vs defect."""
import os, sys, ast, json, numpy as np, mpmath as mp
from fractions import Fraction as Fr
from sympy import factorint, jacobi_symbol
HERE = os.path.dirname(os.path.abspath(__file__)); LE = os.path.join(HERE, '../LEMMA_E_EPSTEIN_001_data')
sys.path.insert(0, LE); os.chdir(LE); os.environ.setdefault('IVDPS', '60')
import cert_epstein as C
from cert_epstein import iv, ivf, tate_mom, Cpoly
NMAX = 200
def chi(D, n):
    if D == -4: return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
    if D == 5: return 0 if n % 5 == 0 else int(jacobi_symbol(n, 5))
    return C._kron20(n)
def logcoef(kind, n):  # coefficient of n^{-s} in log L, as Fraction
    f = factorint(n)
    if len(f) != 1: return Fr(0)
    p, k = list(f.items())[0]
    if kind == 'K': c = 1 + (0 if p in (2, 5) else int(C._kron20(p))) ** k
    else: c = chi(-4, p) ** k + chi(5, p) ** k
    return Fr(c, k)
b = {n: (logcoef('psi', n) - logcoef('K', n)) / 2 for n in range(2, NMAX + 1)}
b = {n: v for n, v in b.items() if v != 0}
print('b_n (n<=50):', {n: str(v) for n, v in b.items() if n <= 50})
def conv(x, y):
    out = {}
    for m, u in x.items():
        for n, v in y.items():
            if m * n <= NMAX: out[m * n] = out.get(m * n, 0) + u * v
    return out
bb = conv(b, b); b4 = conv(bb, bb); b6 = conv(b4, bb)
# log cosh y = y^2/2 - y^4/12 + y^6/45 - ... ; Lambda_cosh(n) = log n * [coef of n^-s in log cosh y]
def lam_order(j):
    poly = {2: (bb, Fr(1, 2)), 4: (b4, Fr(-1, 12)), 6: (b6, Fr(1, 45))}[j]
    return {n: float(poly[1] * v) * np.log(n) for n, v in poly[0].items()}
L2, L4, L6 = lam_order(2), lam_order(4), lam_order(6)
# exact Lambda_cosh = Lambda_Q - (Lambda_K + Lambda_psi)/2
LK = C._LK(NMAX)
def val(d): return sum(float(q) * np.log(p) for p, q in d.items())
Lcosh = {}
for n in range(2, NMAX + 1):
    lq = val(C.LQ[n]) if n in C.LQ else 0.0; lk = val(LK[n]) if n in LK else 0.0
    lp = float(logcoef('psi', n)) * np.log(n) if len(factorint(n)) == 1 else 0.0
    v = lq - (lk + lp) / 2
    if abs(v) > 1e-12: Lcosh[n] = v
err = max(abs(Lcosh.get(n, 0) - L2.get(n, 0) - L4.get(n, 0) - L6.get(n, 0)) for n in range(2, 64))
print('check Lambda_cosh = orders 2+4+6 for n<64: max err', err)
print('Lambda_cosh (n<=30):', {n: round(v, 4) for n, v in Lcosh.items() if n <= 30})
print('order-2 part (n<=30):', {n: round(v, 4) for n, v in L2.items() if n <= 30})
# ---- (2) witness T = 8/5
txt = open('cert_T1.6_full49.txt').read()
g0 = [Fr(x) for x in ast.literal_eval(txt.split('(x^0..):')[1].strip())]
T = iv.mpf(8) / 5; Mdeg = len(g0); R = 2 * Mdeg + 2; cp, cm = T / 2, -T / 2
r1 = -sum(ivf(g0[j]) * tate_mom(cp, j) for j in range(Mdeg) if g0[j] != 0)
r2 = -sum(ivf(g0[j]) * tate_mom(cm, j) for j in range(Mdeg) if g0[j] != 0)
a11, a12, a21, a22 = tate_mom(cp, 0), tate_mom(cp, 1), tate_mom(cm, 0), tate_mom(cm, 1); det = a11 * a22 - a12 * a21
g = [ivf(x) if x != 0 else 0 for x in g0]; g[0] = (r1 * a22 - a12 * r2) / det; g[1] = (a11 * r2 - a21 * r1) / det
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
    return v / c0
ns = [n for n in range(2, 25)]
cn = {n: float(cval(iv.log(n)).mid) for n in ns}
print('c(log n)/c(0) witness:', {n: round(v, 5) for n, v in cn.items()})
def pair(L): return -sum(2 * L[n] / np.sqrt(n) * cn[n] for n in L if n <= 24)
D_exact = pair(Lcosh); D2 = pair(L2); D4 = pair(L4); D6 = pair(L6)
print('defect D (exact Lambda_cosh) = %.6f' % D_exact)
print('-Q_g[b] (order 2) = %.6f ; order 4 = %.6f ; order 6 = %.6f ; R4 := -D - Q = %.6f' % (D2, D4, D6, -D_exact + D2))
print('order-2 terms per n:', {n: round(-2 * L2[n] / np.sqrt(n) * cn[n], 5) for n in L2 if n <= 24})
print('order-4 terms per n:', {n: round(-2 * L4[n] / np.sqrt(n) * cn[n], 5) for n in L4 if n <= 24})
# ---- (3) Hankel matrix on support of b with m*n <= 24
S = [n for n in sorted(b) if n <= 12]
w = lambda n: np.log(n) / np.sqrt(n) * cn[n] if n <= 24 else 0.0
H = np.array([[w(m * n) for n in S] for m in S])
print('Hankel support', S); print(np.round(H, 4)); print('eigs', np.round(np.linalg.eigvalsh(H), 4))
bv = np.array([float(b[n]) for n in S]); print('b^T H b =', bv @ H @ bv, '(= Q_g[b] up to terms with mn>24)')
