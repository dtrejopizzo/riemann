"""LEMMA_13_1_CUMULANT_001 (NUMERICO). D=-20 (h=2), witness T=8/5.
(1) D from Lambda_def (comb) ; (2) normalization check of zero side with zeta ; (3) off-line zeros of Z_Q up to TMAX and their
contribution to D ; (4) indefiniteness of D on P_T (modulated test, Thm 13.1(a)); (5) Jensen check on real axis."""
import os, sys, numpy as np, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from witness import h, cval, C, Tf
from sympy import factorint
from fractions import Fraction as Fr
from sympy import jacobi_symbol
NMAX = 60
def chi(Dd, n):
    if Dd == -4: return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
    if Dd == 5: return 0 if n % 5 == 0 else int(jacobi_symbol(n, 5))
    return C._kron20(n)
def logcoef(kind, n):
    f = factorint(n)
    if len(f) != 1: return Fr(0)
    pp, k = list(f.items())[0]
    if kind == 'K': c = 1 + (0 if pp in (2, 5) else int(C._kron20(pp))) ** k
    else: c = chi(-4, pp) ** k + chi(5, pp) ** k
    return Fr(c, k)
LK = C._LK(NMAX)
def val(d): return sum(float(q) * np.log(pp) for pp, q in d.items())
Lcosh = {}
for n in range(2, NMAX + 1):
    lq = val(C.LQ[n]) if n in C.LQ else 0.0; lk = val(LK[n]) if n in LK else 0.0
    lp = float(logcoef('psi', n)) * np.log(n) if len(factorint(n)) == 1 else 0.0
    v = lq - (lk + lp) / 2
    if abs(v) > 1e-12: Lcosh[n] = v
# (1) defect from comb: Lambda_def = Lambda_Q - (Lambda_K + Lambda_psi)/2
D = -sum(2 * v / np.sqrt(n) * cval(np.log(n)) for n, v in Lcosh.items() if np.log(n) < 2 * Tf)
print('(1) D_T(F)/||F||^2 from comb = %.6f' % D)
# (2) zeta check: a^zeta via template vs sum over zeros
mp.mp.dps = 20
UU = __import__('witness').U; WW = __import__('witness').W; CU = __import__('witness').CU
K14 = 2 * np.exp(-UU / 2) / (1 - np.exp(-2 * UU))
lev = float(((1 - CU) * K14 * WW).sum() + mp.quad(lambda u: 2 * mp.exp(-u / 2) / (1 - mp.exp(-2 * u)), [2 * Tf, mp.inf]))
C0z = float(mp.digamma(0.25) - mp.log(mp.pi))
combz = -sum(2 * np.log(pf) / np.sqrt(n) * cval(np.log(n)) for n in range(2, 25) for pf in [list(factorint(n))[0]] if len(factorint(n)) == 1)
az = C0z + lev + combz
print('(2) a^zeta template: C0 %.6f levy %.6f comb %.6f total %.6f' % (C0z, lev, combz, az))
NZ = int(sys.argv[1]) if len(sys.argv) > 1 else 600
gz = np.array([float(mp.im(mp.zetazero(k))) for k in range(1, NZ + 1)])
hz = h(gz).real
for N in (50, 100, 200, 400, NZ):
    print('    sum over first %4d zeta zeros (both signs): %.6f' % (N, 2 * hz[:N].sum()))
tt = np.linspace(gz[-1], 6000, 60000); ht = np.concatenate([h(x).real for x in np.array_split(tt, 120)]); tail = 2 * np.trapz(ht * np.log(tt / (2 * np.pi)) / (2 * np.pi), tt)
print('    + smoothed-density tail beyond gamma_N (to 2e4): %.6f -> %.6f' % (tail, 2 * hz.sum() + tail))
print('    h(t) samples:', {t: round(float(h(t).real[0]), 6) for t in (0, 2, 5, 10, 15.67, 30, 60, 100)})
# (3) off-line zeros of Z_Q
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../LEMMA_E_EPSTEIN_001_data'))
from zeros_epstein import Z
mp.mp.dps = 20
TMAX = float(sys.argv[2]) if len(sys.argv) > 2 else 60
found = []
t = 0.5
while t < TMAX:
    for sg in (0.6, 0.75, 0.9, 1.05, 1.2):
        try: r = mp.findroot(Z, mp.mpc(sg, t), tol=1e-18, maxsteps=50)
        except Exception: continue
        if 0.505 < r.real < 2.5 and 0 < r.imag < TMAX and all(abs(r - f) > 1e-6 for f in found): found.append(r)
    t += 0.25
found.sort(key=lambda r: float(r.imag))
tot = 0
print('(3) off-line zeros of Z_Q (Re>1/2, 0<t<%g), Newton grid:' % TMAX)
for r in found:
    gm = complex(float(r.imag), -(float(r.real) - 0.5))   # rho = 1/2 + i gamma
    quad = 2 * (h(gm)[0] + h(gm.conjugate())[0]).real     # rho, 1-conj(rho), and their conjugates (-gamma)
    online = 4 * h(gm.real)[0].real                        # same 4 zeros put on the line at height t
    tot += quad
    print('    rho = %s : quadruple contribution %.6f ; same zeros on the line %.6f ; excess %.6f' % (mp.nstr(r, 12), quad, online, quad - online))
print('    total off-line quadruples = %.6f  vs D = %.6f  (ratio %.4f)' % (tot, D, tot / D))
# (4) Theorem 13.1(a): modulated indicator F_lambda = 1_{[-T,T]} cos(lambda t): D(F_l)/||F_l||^2 -> (1/2)sum a_n c_1(l_n) cos(lambda l_n)/(T)
ln = {n: np.log(n) for n in Lcosh if np.log(n) < 2 * Tf}
def Dmod(lam):
    return sum(-2 * v / np.sqrt(n) * (2 * Tf - ln[n]) * np.cos(lam * ln[n]) for n, v in Lcosh.items() if n in ln) / (2 * Tf)
lams = np.linspace(0, 200, 20001); vals = np.array([Dmod(l) for l in lams])
print('(4) limit symbol of D on modulated indicators, lambda in [0,200]: max %.4f  min %.4f  mean %.5f' % (vals.max(), vals.min(), vals.mean()))
# (5) Jensen on the real axis: K(sigma) = log cosh y(sigma) >= 0, and the coefficient series
for sg in (1.2, 1.5, 2, 3):
    yv = 0.5 * mp.log((Z(sg) * 0 + mp.dirichlet(sg, __import__('zeros_epstein').ch[-4]) * mp.dirichlet(sg, __import__('zeros_epstein').ch[5])) / (mp.zeta(sg) * mp.dirichlet(sg, __import__('zeros_epstein').ch[-20])))
    print('(5) sigma=%.1f  y=%s  log cosh y=%s >= 0' % (sg, mp.nstr(yv, 8), mp.nstr(mp.log(mp.cosh(yv)), 8)))
