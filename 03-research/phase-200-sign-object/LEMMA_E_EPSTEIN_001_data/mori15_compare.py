"""LEMMA_E_EPSTEIN_001 task 3 (NUMERICO, double precision + FFT autocorrelation): evaluate the complete Weil form
(with pole term, Mori convention of MORI15_EXTREMAL_001_pieces.py) of zeta and of Z_Q on Mori's even extremal g* (mu=15).
W(g) = C0 c(0) + int_0^inf (c(0)-c(u)) K(u) du + 2AB - sum_n 2a(n)/sqrt(n) c(log n), A,B = int g e^{+-x/2}.
zeta: C0 = psi(1/4)-log pi, K = 2e^{-u/2}/(1-e^{-2u}), a = Lambda.   Z_Q: C0Q = log20-2gamma-6log2-2log pi, KQ = 1/sinh(u/2), a = Lambda_Q."""
import json, numpy as np, mpmath as mp, os, sys
from numpy.polynomial import legendre as leg
sys.path.insert(0, os.path.dirname(__file__))
D = os.path.join(os.path.dirname(__file__), '../../phase-199-frontier-pattern/proof-L-sharp/MORI15_EXTREMAL_001_data')
E = json.load(open(os.path.join(D, 'p0_eig.json'))); v = np.array([float(x) for x in E['vectors'][0]])
Lh = np.log(15) / 2; N = 1664; coef = np.zeros(N)
for t, j in enumerate(range(0, N, 2)): coef[j] = v[t] * np.sqrt((2 * j + 1) / (2 * Lh))
M = 2 ** 16; x = np.linspace(-Lh, Lh, M + 1); h = x[1] - x[0]; g = leg.legval(x / Lh, coef)
w = np.full(M + 1, h); w[0] = w[-1] = h / 2
n2 = np.sum(w * g * g); A = np.sum(w * g * np.exp(x / 2)); B = np.sum(w * g * np.exp(-x / 2))
F = np.fft.rfft(g * np.sqrt(w), 4 * M); c = np.fft.irfft(np.abs(F) ** 2, 4 * M)[:M + 1]  # c(k h)
F2 = np.fft.rfft(g, 4 * M); c = np.fft.irfft(np.abs(F2) ** 2, 4 * M)[:M + 1] * h  # trapezoid-equivalent (g ~ 0 at edges)
u = np.arange(M + 1) * h
def cint(t): return np.interp(t, u, c)
LZ = {n: float(mp.log(p)) for n, p in {2: 2, 3: 3, 4: 2, 5: 5, 7: 7, 8: 2, 9: 3, 11: 11, 13: 13}.items()}
from epstein_coeffs import val as LQv
def form(C0, K, Ktail, lam):
    integ = np.zeros_like(u); integ[1:] = (c[0] - c[1:]) * K(u[1:])
    levy = np.trapz(integ, u) + c[0] * Ktail
    comb = {n: 2 * a / np.sqrt(n) * cint(np.log(n)) for n, a in lam.items() if np.log(n) < 2 * Lh and a != 0}
    tot = C0 * c[0] + levy + 2 * A * B - sum(comb.values())
    return dict(arch_const=C0 * c[0], levy=levy, pole=2 * A * B, comb=sum(comb.values()), terms=comb, total=tot)
C0z = float(mp.digamma(0.25) - mp.log(mp.pi)); C0q = float(mp.log(20) - 2 * mp.euler - 6 * mp.log(2) - 2 * mp.log(mp.pi))
tz = float(mp.quad(lambda s: 2 * mp.e ** (-s / 2) / (1 - mp.e ** (-2 * s)), [2 * Lh, mp.inf]))
tq = float(2 * mp.log(mp.coth(Lh / 2)))
Rz = form(C0z, lambda s: 2 * np.exp(-s / 2) / (1 - np.exp(-2 * s)), tz, LZ)
Rq = form(C0q, lambda s: 1 / np.sinh(s / 2), tq, {n: LQv[n] for n in LQv if n < 15})
print('||g*||^2 =', n2, ' A=B =', A, B)
for name, R in (('zeta', Rz), ('Epstein Q', Rq)):
    print(name, {k: (v if k != 'terms' else {n: '%.6e' % t for n, t in v.items()}) for k, v in R.items()})
# hybrid decompositions: which piece breaks the cancellation
print('Delta(arch const) =', Rq['arch_const'] - Rz['arch_const'], ' Delta(levy) =', Rq['levy'] - Rz['levy'],
      ' Delta(comb, enters with minus) =', -(Rq['comb'] - Rz['comb']))
print('zeta arch + Epstein comb  =', Rz['arch_const'] + Rz['levy'] + Rz['pole'] - Rq['comb'])
print('Epstein arch + zeta comb  =', Rq['arch_const'] + Rq['levy'] + Rq['pole'] - Rz['comb'])
# same archimedean data, Euler comb: Dedekind zeta of Q(sqrt-5) and the genus L-function L_psi = L(chi_-4)L(chi_5)
import cert_epstein as CE
LK = {n: sum(float(q) * np.log(p) for p, q in d.items()) for n, d in CE._LK(20).items()}
def chi(D, n):
    import sympy
    if D == -4: return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
    return 0 if n % 5 == 0 else int(sympy.jacobi_symbol(n, 5))
from sympy import factorint
Lpsi = {}
for n in range(2, 16):
    f = factorint(n)
    if len(f) == 1:
        p, k = list(f.items())[0]; Lpsi[n] = (chi(-4, p) ** k + chi(5, p) ** k) * np.log(p)
RK = form(C0q, lambda s: 1 / np.sinh(s / 2), tq, LK); Rp = form(C0q, lambda s: 1 / np.sinh(s / 2), tq, Lpsi)
print('zeta_K on g*:', RK['total'], 'comb', RK['comb'], '| L_psi on g*:', Rp['total'], 'comb', Rp['comb'],
      '| mean', (RK['total'] + Rp['total']) / 2, '| cosh defect Q - mean', Rq['total'] - (RK['total'] + Rp['total']) / 2)
