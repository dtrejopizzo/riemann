"""Shared: witness F (T=8/5, cert_T1.6_full49) -> c(u)/c(0) on [0,2T] as float values at Gauss-Legendre nodes."""
import os, sys, ast, numpy as np, mpmath as mp
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__)); LE = os.path.join(HERE, '../LEMMA_E_EPSTEIN_001_data')
sys.path.insert(0, LE); _cwd = os.getcwd(); os.chdir(LE); os.environ.setdefault('IVDPS', '60')
import cert_epstein as C
from cert_epstein import iv, ivf, tate_mom, Cpoly
txt = open('cert_T1.6_full49.txt').read(); os.chdir(_cwd)
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
Tf = 1.6
def cval(u):
    s = iv.mpf(u) / T; v = iv.mpf(0)
    for r in range(R, -1, -1): v = v * s + p[r]
    return float((v / c0).mid)
NQ = 3000
xg, wg = np.polynomial.legendre.leggauss(NQ)
U = (xg + 1) * Tf; W = wg * Tf          # nodes on [0, 2T]
CU = np.array([cval(u) for u in U])
def h(gam):  # h(gamma) = int_R c(u) e^{i gamma u} du, c even, normalized c(0)=1 (= ||F||^2 = 1)
    gam = np.atleast_1d(np.asarray(gam, dtype=complex))
    return 2 * (np.cos(np.outer(gam, U)) * (W * CU)).sum(axis=1)
