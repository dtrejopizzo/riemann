"""(i) sign pattern of A_M(Lambda) off-diagonal by lag; (ii) lambda_min ~ M^-alpha fits; (iii) exact identity on s=m^{-1/2}:
 s^T(Div+Near)s = 2 sum_N N^{-1/2} log N E_M(N), E_M(N) = sum_{m<=M} m^{-1/2} c0(log(N/m))  (uses only Lambda*1=log and the atom sum)."""
import numpy as np, json
from profile import Profile
from am import *
T0 = 0.3; M = 800
P = Profile(T0, 1.0); x = np.log(np.arange(1, M+1)); nmax = int(M*np.exp(2*T0)) + 2
pos, w, ns = lambda_comb(nmax); A = AM(P, x, pos, w)
D = x[:, None] - x[None, :]; off = ~np.eye(M, dtype=bool)
r = {}
for lo, hi in ((0, 2*T0), (2*T0, 1), (1, 2), (2, 4), (4, 8)):
    msk = off & (np.abs(D) > lo) & (np.abs(D) <= hi)
    r[f'lag({lo:.2f},{hi}]'] = dict(frac_pos=float((A.A[msk] > 0).mean()), n=int(msk.sum()), mean=float(A.A[msk].mean()), maxabs=float(np.abs(A.A[msk]).max()))
print('sign pattern of A_M(Lambda) off-diagonal by lag:', json.dumps(r, indent=0))
# (iii)
s = np.arange(1, M+1)**-0.5
lhs = s@(A.Div + A.Near)@s
Ns = np.arange(1, nmax+1); E = np.array([np.sum(s*P.c0(np.log(N) - x)) for N in Ns])
rhs = 2*np.sum(Ns**-0.5*np.log(Ns)*E)
print('identity check: s^T(Div+Near)s = %.12f  vs 2 sum N^-1/2 log N E(N) = %.12f' % (lhs, rhs))
print('E_M(N) (quadrature defect of the Tate integral) for N=2..12:', [(int(N), '%.4f' % E[N-1]) for N in range(2, 13)], ' |E| at N=50,100,400,800:', ['%.2e' % abs(E[N-1]) for N in (50, 100, 400, 800)])
print('contribution 2 N^-1/2 log N E(N) summed over N<=10, <=100, <=800, all:', ['%.4f' % (2*np.sum((Ns**-0.5*np.log(Ns)*E)[:K])) for K in (10, 100, 800, nmax)])
print('Arch on s:', s@A.Arch@s, 'A on s:', s@A.A@s, '||s||^2', s@s)
# (ii) fits
for tag in ('T00.3_b1.0', 'T00.15_b1.0', 'T00.05_b1.0'):
    d = json.load(open(f'../data/main_{tag}.json'))
    Ms = np.array(sorted(int(k) for k in d)); lam = np.array([d[str(m)]['lam_min'] for m in Ms]); fl = np.array([d[str(m)]['floor'] for m in Ms])
    ok = lam > 5*fl
    sl = np.polyfit(np.log(Ms[ok]), np.log(lam[ok]), 1)[0]
    print(tag, 'lambda_min:', ['%d:%.2e' % (m, l) for m, l in zip(Ms, lam)], ' fit exponent (M where lam>5 floor):', round(sl, 2), 'local exponents:', [round(float(-np.log(lam[i+1]/lam[i])/np.log(Ms[i+1]/Ms[i])), 2) for i in range(len(Ms)-1)])
