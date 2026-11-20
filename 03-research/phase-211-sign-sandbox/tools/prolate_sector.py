"""Sine coefficients of E psi_k (all even prolates k <= KMAX of [-lam, lam], c = 2 pi N) on I_T, with the exact
defects d_k = 1 - chi_k from chi_k = (c/2pi) (int phi_k)^2 / phi_k(0)^2.  python-flint arb for the quadrature.
Usage: python3 prolate_sector.py T Nb dps KMAX   -> cache/sector_T{T}_N{Nb}_K{KMAX}.pkl   (NUMERICAL tool)"""
import sys, os, time, pickle, mpmath as mp
from flint import arb, arb_mat, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as G
T = float(sys.argv[1]); Nb = int(sys.argv[2]); dps = int(sys.argv[3]); KMAX = int(sys.argv[4])
dps2 = 2 * dps + 40
mp.mp.dps = dps2; ctx.prec = int(dps2 * 3.33) + 20
Tm = mp.mpf(T); lam = mp.exp(Tm); NN = lam ** 2; c = 2 * mp.pi * NN
# --- prolates (even), Legendre coefficients, inverse iteration with many steps
K = int(float(c)) + KMAX + 80
ks = list(range(0, K, 2)); m = len(ks)
dg = [k*(k+1) + c**2*mp.mpf(2*k*(k+1)-1)/((2*k+3)*(2*k-1)) for k in ks]
of = [c**2*mp.mpf((k+2)*(k+1))/((2*k+3)*mp.sqrt(mp.mpf((2*k+1)*(2*k+5)))) for k in ks[:-1]]
import numpy as np
Md = np.diag([float(x) for x in dg]) + np.diag([float(x) for x in of], 1) + np.diag([float(x) for x in of], -1)
ev = sorted(np.linalg.eigvalsh(Md))[:KMAX//2 + 1]
def inviter(sh, its=30):
    x = [mp.mpf(1)/(i+1) for i in range(m)]
    for it in range(its):
        cp = [mp.mpf(0)]*m; dp = [mp.mpf(0)]*m
        a0 = dg[0]-sh; cp[0] = of[0]/a0; dp[0] = x[0]/a0
        for i in range(1, m):
            den = dg[i]-sh-of[i-1]*cp[i-1]
            if i < m-1: cp[i] = of[i]/den
            dp[i] = (x[i]-of[i-1]*dp[i-1])/den
        y = [mp.mpf(0)]*m; y[-1] = dp[-1]
        for i in range(m-2, -1, -1): y[i] = dp[i]-cp[i]*y[i+1]
        nr = mp.sqrt(mp.fsum(t*t for t in y)); xn = [t/nr for t in y]
        if xn[0] < 0: xn = [-t for t in xn]
        # Rayleigh-quotient shift update for fast convergence
        Ax = [dg[i]*xn[i] + (of[i]*xn[i+1] if i < m-1 else 0) + (of[i-1]*xn[i-1] if i > 0 else 0) for i in range(m)]
        rq = mp.fsum(a*b for a, b in zip(Ax, xn))
        if it >= 3: sh = rq
        x = xn
    return x
De = []
for e0 in ev:
    De.append(inviter(mp.mpf(e0) - mp.mpf(10)**(-9)*(1+abs(e0))))
P0 = []  # Pbar_k(0)
for k in ks:
    P0.append(mp.sqrt(k+mp.mpf(1)/2) * (mp.mpf(0) if k % 2 else mp.binomial(k, k//2) * (-1)**(k//2) / mp.mpf(2)**k))
dk = []
for D_ in De:
    phi0 = mp.fsum(a*b for a, b in zip(D_, P0)); intphi = mp.sqrt(2) * D_[0]
    chi = c/(2*mp.pi) * intphi**2 / phi0**2; dk.append(1 - chi)
print("d_k:", [mp.nstr(x, 5) for x in dk], flush=True)
nP = len(De)
# --- quadrature in arb
A = lambda x: arb(mp.nstr(x, dps2 + 5))
DeA = arb_mat(nP, m)
for i in range(nP):
    for j in range(m): DeA[i, j] = A(De[i][j])
sq = [A(mp.sqrt(k + mp.mpf(1)/2)) for k in ks]
with mp.workdps(dps2): xs, ws = G.gl_nodes(40)
xsA = [A(x) for x in xs]; wsA = [A(w) for w in ws]
TA = A(Tm); lamA = A(lam); sT = 1 / TA.sqrt()
bps = sorted(set([-Tm, Tm] + [Tm - mp.log(n) for n in range(2, int(NN) + 1) if Tm - mp.log(n) > -Tm]))
nodes = []; wts = []
for a, b in zip(bps[:-1], bps[1:]):
    npan = int(float((b-a)/0.04)) + 1; h = (b-a)/npan
    for p in range(npan):
        lo = A(a + p*h); hA = A(h)
        for x, w in zip(xsA, wsA):
            nodes.append(lo + hA*(x+1)/2); wts.append(w*hA/2)
Q = len(nodes); kdeg = ks[-1]
t0 = time.time()
L = arb_mat(m, Q); nrm2 = None
for q, t in enumerate(nodes):
    et = t.exp(); acc = [arb(0)]*m; n = 1
    while True:
        u = n*et/lamA
        if not (u < 1): break
        p0, p1 = arb(1), u; vals = [p0]
        for k in range(1, kdeg+1):
            if k >= 2: p0, p1 = p1, ((2*k-1)*u*p1 - (k-1)*p0)/k
            if k % 2 == 0: vals.append(p1)
        for i in range(m): acc[i] += vals[i]
        n += 1
    e2 = (t/2).exp()
    for i in range(m): L[i, q] = acc[i]*sq[i]*e2
print("legendre", round(time.time()-t0, 1), "s, Q =", Q, flush=True)
Gv = DeA * L      # nP x Q : values of E psi_k at the nodes
S = arb_mat(Q, Nb)
for q, t in enumerate(nodes):
    for j in range(Nb):
        S[q, j] = wts[q] * (A(mp.pi)*(j+1)*(t+TA)/(2*TA)).sin() * sT
C = Gv * S
nrm = [sum((Gv[i, q]**2 * wts[q] for q in range(Q)), arb(0)) for i in range(nP)]
print("total", round(time.time()-t0, 1), "s", flush=True)
s = lambda x: x.mid().str(dps + 15, radius=False)
out = dict(T=T, Nb=Nb, ks=[2*i for i in range(nP)], d=[mp.nstr(x, 30) for x in dk],
           C=[[s(C[i, j]) for j in range(Nb)] for i in range(nP)], nrm=[s(x) for x in nrm],
           rad=max(float(C[i, j].rad()) for i in range(nP) for j in range(Nb)))
pickle.dump(out, open(os.path.join(G.CACHE, f'sector_T{T}_N{Nb}_K{KMAX}.pkl'), 'wb'))
print("max radius", out['rad'])
