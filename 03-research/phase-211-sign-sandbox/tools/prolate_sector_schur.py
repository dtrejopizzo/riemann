"""Block-diagonal Schur test on a sector: Delta = blockdiag(M_LL, diag M_kk), C = Delta^{-1/2} M Delta^{-1/2};
if |C - I| <= 1 - eta then M >= eta Delta >= eta min(alpha_L, min_k M_kk/d_k) D.  (NUMERICAL tool)
Usage: T Nb dps KMAX sector(+1/-1)"""
import sys, os, pickle, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as G
T = float(sys.argv[1]); Nb = int(sys.argv[2]); dps = int(sys.argv[3]); KMAX = int(sys.argv[4]); sec = int(sys.argv[5])
D = G.build(T, Nb, dps=dps, verbose=False); mp.mp.dps = dps + 20
P = pickle.load(open(os.path.join(G.CACHE, f'sector_T{T}_N{Nb}_K{KMAX}.pkl'), 'rb')); ks = P['ks']; d = [mp.mpf(x) for x in P['d']]
g = pickle.load(open(os.path.join(G.CACHE, f'sector_g_T{T}_N{Nb}_K{KMAX}.pkl'), 'rb'))['g']
g = [mp.matrix([mp.mpf(x) for x in v]) for v in g]; M = D['Arch'] - D['Pi']; NN = mp.e**(2*mp.mpf(T))
def dot(a, b): return mp.fsum(a[i]*b[i] for i in range(Nb))
def par(v):
    w = mp.matrix(v)
    for j in range(Nb):
        if (j % 2 == 0) != (sec == 1): w[j] = 0
    return w
cls = 0 if sec == 1 else 2
idx = [i for i, k in enumerate(ks) if k % 4 == cls]; U = [par(g[i]) for i in idx]; n = len(idx)
MU = [M*u for u in U]; Mm = mp.matrix(n, n)
for a in range(n):
    for b in range(n): Mm[a, b] = dot(U[a], MU[b])
dd = [d[i] for i in idx]; kk = [ks[i] for i in idx]; L = 3
def isqrt_psd(A):
    E, W = mp.eigsy(A); return W*mp.diag([1/mp.sqrt(e) for e in E])*W.T
print(f"# T={T} 4N={mp.nstr(4*NN,4)} sector {sec:+d}, classes k = {cls} mod 4")
SL = isqrt_psd(Mm[:L, :L]); aL = min(mp.eigsy(isqrt_psd(mp.diag(dd[:L]))*Mm[:L, :L]*isqrt_psd(mp.diag(dd[:L])), eigvals_only=True))
print(f"  alpha_L = lambda_min(M_LL, D_L) = {mp.nstr(aL,4)}")
print("  top k | |X| (low-block coupling) | |O_H| (offdiag in H) | |C-I| | min_H M_kk/d_k | eta*min(alpha_L, min_H)  | true gen-min")
for top in range(L+1, n+1):
    m_ = top; Dl = mp.matrix(m_, m_)
    for a in range(L):
        for b in range(L): Dl[a, b] = SL[a, b]
    for a in range(L, m_): Dl[a, a] = 1/mp.sqrt(Mm[a, a])
    C = Dl*Mm[:m_, :m_]*Dl
    CI = C - mp.eye(m_); nrm = max(abs(e) for e in mp.eigsy(CI, eigvals_only=True))
    X = C[:L, L:m_]; nX = mp.sqrt(max(mp.eigsy(X*X.T, eigvals_only=True)))
    OH = C[L:m_, L:m_] - mp.eye(m_-L); nO = max(abs(e) for e in mp.eigsy(OH, eigvals_only=True)) if m_-L > 1 else 0
    mH = min(Mm[a, a]/dd[a] for a in range(L, m_)); eta = 1 - nrm
    S = isqrt_psd(mp.diag(dd[:m_])); gm = min(mp.eigsy(S*Mm[:m_, :m_]*S, eigvals_only=True))
    print(f"   {kk[top-1]:2d} | {mp.nstr(nX,4)} | {mp.nstr(nO,4)} | {mp.nstr(nrm,4)} | {mp.nstr(mH,4)} | {mp.nstr(eta*min(aL, mH),4)} | {mp.nstr(gm,4)}")
