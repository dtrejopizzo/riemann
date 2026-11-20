"""prop:ext-consol(b) on the prolate span with the gauge-minimised leakage (NUMERICAL tool).
leak(f0+phi) = a^T D a + 2 a^T D J beta + |phi|^2 - sum_k chi_k (J beta)_k^2,  phi = sum beta_j p_j (inner Legendre basis
on [-1/lam, 1/lam]); minimising over beta gives D_g = D - D J H^{-1} J^T D, H = I - J^T diag(chi) J (all k <= KMAX).
Window side: a_T(sum a_k E psi_k) on {A(Ef) = B(Ef) = 0} (no projection), sine-Galerkin.
Usage: python3 prolate_gauge.py T Nb dps KMAX MIN"""
import sys, os, pickle, mpmath as mp, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as G
T = float(sys.argv[1]); Nb = int(sys.argv[2]); dps = int(sys.argv[3]); KMAX = int(sys.argv[4]); MIN = int(sys.argv[5])
D = G.build(T, Nb, dps=dps, verbose=False)
mp.mp.dps = 2*dps + 40
P = pickle.load(open(os.path.join(G.CACHE, f'sector_T{T}_N{Nb}_K{KMAX}.pkl'), 'rb'))
ks = P['ks']; d = [mp.mpf(x) for x in P['d']]; nP = len(ks)
V = [mp.matrix([mp.mpf(x) for x in r]) for r in P['C']]
Tm = mp.mpf(T); lam = mp.exp(Tm); NN = lam**2; c = 2*mp.pi*NN
# prolates again (same construction as prolate_sector.py)
K = int(float(c)) + KMAX + 80; kl = list(range(0, K, 2)); m = len(kl)
dg = [k*(k+1) + c**2*mp.mpf(2*k*(k+1)-1)/((2*k+3)*(2*k-1)) for k in kl]
of = [c**2*mp.mpf((k+2)*(k+1))/((2*k+3)*mp.sqrt(mp.mpf((2*k+1)*(2*k+5)))) for k in kl[:-1]]
Md = np.diag([float(x) for x in dg]) + np.diag([float(x) for x in of], 1) + np.diag([float(x) for x in of], -1)
ev = sorted(np.linalg.eigvalsh(Md))[:nP]
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
        Ax = [dg[i]*xn[i] + (of[i]*xn[i+1] if i < m-1 else 0) + (of[i-1]*xn[i-1] if i > 0 else 0) for i in range(m)]
        if it >= 3: sh = mp.fsum(a*b for a, b in zip(Ax, xn))
        x = xn
    return x
De = [inviter(mp.mpf(e0) - mp.mpf(10)**(-9)*(1+abs(e0))) for e0 in ev]
xs, ws = G.gl_nodes(80); h = 1/lam
def leg(x, kmax):
    v = [mp.mpf(1), x]
    for k in range(2, kmax+1): v.append(((2*k-1)*x*v[-1]-(k-1)*v[-2])/k)
    return v
J = mp.matrix(nP, MIN)
for x, w in zip(xs, ws):
    u = h*x; X = u/lam
    lv = leg(X, kl[-1]); psi = [mp.fsum(Dd[i]*mp.sqrt(kl[i]+mp.mpf(1)/2)*lv[kl[i]] for i in range(m))/mp.sqrt(lam) for Dd in De]
    li = leg(x, 2*MIN)
    pj = [mp.sqrt(mp.mpf(4*j+1)/(2*h))*li[2*j] for j in range(MIN)]
    for k in range(nP):
        for j in range(MIN): J[k, j] += w*h*psi[k]*pj[j]
chi = [1-x for x in d]
H = mp.eye(MIN)
for k in range(nP):
    for a in range(MIN):
        for b in range(MIN): H[a, b] -= chi[k]*J[k, a]*J[k, b]
print(f"# T={T} N={mp.nstr(NN,5)} 4N={mp.nstr(4*NN,4)} lambda_min(H) = {mp.nstr(min(mp.eigsy(H, eigvals_only=True)),4)} (inner c = 2pi)")
DJ = mp.matrix(nP, MIN)
for k in range(nP):
    for j in range(MIN): DJ[k, j] = d[k]*J[k, j]
Dg = mp.diag(d) - DJ*mp.inverse(H)*DJ.T
Mw = D['Arch'] - D['Pi']; MV = [Mw*v for v in V]
def dot(a, b): return mp.fsum(a[i]*b[i] for i in range(Nb))
Mf = mp.matrix(nP, nP)
for i in range(nP):
    for j in range(i, nP): Mf[i, j] = Mf[j, i] = dot(V[i], MV[j])
Cc = mp.matrix(2, nP)
for i in range(nP): Cc[0, i] = dot(D['A'], V[i]); Cc[1, i] = dot(D['B'], V[i])
lamA = G.lambda_A(D)[0]
def report(idx, lab):
    print(f"## {lab}")
    print("  top k | n | lambda_min(D_g)/min d | gen.min (W, leak) | gen.min (W, gauge-min leak) | W-bottom/lambda_A")
    for t in range(3, len(idx)+1):
        I = idx[:t]; n = len(I)
        Ms = mp.matrix(n, n); Ds = mp.matrix(n, n); Dp = mp.matrix(n, n); Cs = mp.matrix(2, n)
        for a in range(n):
            Cs[0, a] = Cc[0, I[a]]; Cs[1, a] = Cc[1, I[a]]; Dp[a, a] = d[I[a]]
            for b in range(n): Ms[a, b] = Mf[I[a], I[b]]; Ds[a, b] = Dg[I[a], I[b]]
        Q, R = mp.qr(Cs.T, mode='full'); Z = Q[:, 2:]
        Mz = Z.T*Ms*Z; Dz = Z.T*Ds*Z; Dpz = Z.T*Dp*Z
        def gmin(A_, B_):
            E, W = mp.eigsy(B_)
            if min(E) <= 0: return mp.nan
            S = W*mp.diag([1/mp.sqrt(e) for e in E])*W.T; return min(mp.eigsy(S*A_*S, eigvals_only=True))
        Ez = mp.eigsy(Dz, eigvals_only=True)
        wb = min(mp.eigsy(Mz, eigvals_only=True))
        print(f"   {ks[I[-1]]:2d} | {n-2} | {mp.nstr(min(Ez)/min(d[i] for i in I),4)} | {mp.nstr(gmin(Mz, Dpz),4)} | {mp.nstr(gmin(Mz, Dz),4)} | {mp.nstr(wb/lamA,4)}")
report(list(range(nP)), "all even prolates (both sectors), constraints A(Ef)=B(Ef)=0")
report([i for i in range(nP) if ks[i] % 4 == 0], "class +1 only (k = 0 mod 4)")
