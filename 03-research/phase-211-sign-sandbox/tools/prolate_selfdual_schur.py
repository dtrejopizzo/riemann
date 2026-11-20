"""Self-dual sector Schur test (NUMERICAL tool).  Class +1 prolate images h_k = P_+ Pi_T E psi_k (k = 0 mod 4) in the
even sector; M = a_T Gram, D = diag(1 - chi_k) in coefficient coordinates.  Low block L = {0,4,8}: generalized eigenvectors
b (bottom, M/D = alpha_b) and two stiff directions s1, s2 (constraint directions).  The stiff directions are eliminated
exactly in M (Schur), giving on R = {b} + H (H = class +1, 12 <= k <= K) the reduced pair (Mt, Dh), Dh = D evaluated on
r + s*(r).  Reports: alpha_b, stiff ratios, coupling gamma_k = |Mt(b,e_k)|/sqrt(Dh(b) Dh(e_k)) and the same against
sqrt(d_8 d_k), alpha_H = gen-min of (Mt_HH, Dh_HH), Gamma = |Dh_HH^{-1/2} Mt_Hb| / sqrt(Dh(b)), Schur test
Gamma^2 < alpha_b alpha_H, and the true gen-min of (Mt, Dh); then the even-sector spectrum against d_{4j+8}.
Usage: T Nb dps KMAX"""
import sys, os, pickle, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as G
T = float(sys.argv[1]); Nb = int(sys.argv[2]); dps = int(sys.argv[3]); KMAX = int(sys.argv[4])
D = G.build(T, Nb, dps=dps, verbose=False); mp.mp.dps = dps + 20
P = pickle.load(open(os.path.join(G.CACHE, f'sector_T{T}_N{Nb}_K{KMAX}.pkl'), 'rb')); ks = P['ks']; d = [mp.mpf(x) for x in P['d']]
g = pickle.load(open(os.path.join(G.CACHE, f'sector_g_T{T}_N{Nb}_K{KMAX}.pkl'), 'rb'))['g']
g = [mp.matrix([mp.mpf(x) for x in v]) for v in g]; M = D['Arch'] - D['Pi']; NN = mp.e**(2*mp.mpf(T))
def dot(a, b): return mp.fsum(a[i]*b[i] for i in range(Nb))
def ev(v):
    w = mp.matrix(v)
    for j in range(1, Nb, 2): w[j] = 0
    return w
idx = [i for i, k in enumerate(ks) if k % 4 == 0]; U = [ev(g[i]) for i in idx]; n = len(idx)
kk = [ks[i] for i in idx]; dd = [d[i] for i in idx]
MU = [M*u for u in U]; Mm = mp.matrix(n, n)
for a in range(n):
    for b_ in range(n): Mm[a, b_] = dot(U[a], MU[b_])
Dm = mp.diag(dd)
def gen(Ms, Ds):
    m = Ms.rows; S = mp.matrix(m, m); E, W = mp.eigsy(Ds); Si = W*mp.diag([1/mp.sqrt(e) for e in E])*W.T
    E2, W2 = mp.eigsy(Si*Ms*Si); return E2, Si*W2
E3, V3 = gen(Mm[:3, :3], Dm[:3, :3]); o = sorted(range(3), key=lambda i: E3[i])
bvec = V3[:, o[0]]; s1 = V3[:, o[1]]; s2 = V3[:, o[2]]
print(f"# T={T} 4N={mp.nstr(4*NN,4)} class +1 even sector, k = {kk}")
print(f"  low block: alpha_b = {mp.nstr(E3[o[0]],4)}, stiff M/D = {mp.nstr(E3[o[1]],4)}, {mp.nstr(E3[o[2]],4)}")
# basis change: columns b, s1, s2, e_k (k >= 12)
B = mp.zeros(n, n)
for i in range(3): B[i, 0] = bvec[i]; B[i, 1] = s1[i]; B[i, 2] = s2[i]
for j in range(3, n): B[j, j] = 1
Mb = B.T*Mm*B; Db = B.T*Dm*B
Sidx = [1, 2]; Ridx = [0] + list(range(3, n))
MSS = mp.matrix([[Mb[i, j] for j in Sidx] for i in Sidx]); MSSi = mp.inverse(MSS)
def sub(A, I, J): return mp.matrix([[A[i, j] for j in J] for i in I])
MRS = sub(Mb, Ridx, Sidx); Mt = sub(Mb, Ridx, Ridx) - MRS*MSSi*MRS.T
# vectors r + s*(r): s* = -MSS^{-1} MSR r  -> lift matrix Lf (n x |R|) in b-basis
m = len(Ridx); Lf = mp.zeros(n, m)
for c_, i in enumerate(Ridx): Lf[i, c_] = 1
Ss = -MSSi*MRS.T
for a_, i in enumerate(Sidx):
    for c_ in range(m): Lf[i, c_] = Ss[a_, c_]
Dh = Lf.T*Db*Lf
d8 = dd[2]
print("   k | M~_kk/D^_kk | gamma_k (vs D^) | |M~(b,e_k)|/sqrt(D^(b) d_k) | D^_kk/d_k")
for c_ in range(1, m):
    k = kk[Ridx[c_]]; dk = dd[Ridx[c_]]
    print(f"  {k:2d} | {mp.nstr(Mt[c_,c_]/Dh[c_,c_],4)} | {mp.nstr(abs(Mt[0,c_])/mp.sqrt(Dh[0,0]*Dh[c_,c_]),4)} | {mp.nstr(abs(Mt[0,c_])/mp.sqrt(Dh[0,0]*dk),4)} | {mp.nstr(Dh[c_,c_]/dk,4)}")
print(f"  D^(b)/d_8 = {mp.nstr(Dh[0,0]/d8,4)}, M~(b)/D^(b) = {mp.nstr(Mt[0,0]/Dh[0,0],4)}")
print("  top k | alpha_H | Gamma | Gamma^2/(alpha_b alpha_H) | Schur bound | true gen-min (Mt, Dh)")
ab = Mt[0, 0]/Dh[0, 0]
for top in range(2, m+1):
    H = list(range(1, top)); MH = sub(Mt, H, H); DH = sub(Dh, H, H)
    EH, _ = gen(MH, DH); aH = min(EH)
    E, W = mp.eigsy(DH); Si = W*mp.diag([1/mp.sqrt(e) for e in E])*W.T
    x = Si*sub(Mt, H, [0]); Gam = mp.sqrt(mp.fsum(t**2 for t in x))/mp.sqrt(Dh[0, 0])
    # 2x2 Schur bound for the gen-min: min eig of [[ab, Gam],[Gam, aH]]
    tr = ab + aH; det = ab*aH - Gam**2; bound = (tr - mp.sqrt(tr**2 - 4*det))/2
    Ea, _ = gen(sub(Mt, range(top), range(top)), sub(Dh, range(top), range(top)))
    print(f"   {kk[Ridx[top-1]]:2d} | {mp.nstr(aH,4)} | {mp.nstr(Gam,4)} | {mp.nstr(Gam**2/(ab*aH),4)} | {mp.nstr(bound,4)} | {mp.nstr(min(Ea),4)}")

# three-level split: LM = {b} + {12 <= k <= 4N}, HI = {k > 4N}
cut = max(c_ for c_ in range(m) if kk[Ridx[c_]] <= 4*NN) + 1
def opn(A):
    return mp.sqrt(max(mp.eigsy(A*A.T, eigvals_only=True)))
def isq(A):
    E, W = mp.eigsy(A); return W*mp.diag([1/mp.sqrt(e) for e in E])*W.T
LM = list(range(cut)); kap_lm = min(gen(sub(Mt, LM, LM), sub(Dh, LM, LM))[0])
print(f"  three-level: LM = b + k <= {kk[Ridx[cut-1]]}: kappa_LM = {mp.nstr(kap_lm,4)}")
print("  top k | alpha_HI | Gamma' (LM-HI, D-normalised op norm) | Gamma'^2/(kappa_LM alpha_HI) | 2x2 bound | true gen-min")
for top in range(cut+1, m+1):
    HI = list(range(cut, top)); aHI = min(gen(sub(Mt, HI, HI), sub(Dh, HI, HI))[0])
    X = isq(sub(Dh, HI, HI))*sub(Mt, HI, LM)*isq(sub(Dh, LM, LM)); Gp = opn(X)
    tr = kap_lm + aHI; det = kap_lm*aHI - Gp**2; bound = (tr - mp.sqrt(tr**2 - 4*det))/2
    tg = min(gen(sub(Mt, range(top), range(top)), sub(Dh, range(top), range(top)))[0])
    print(f"   {kk[Ridx[top-1]]:2d} | {mp.nstr(aHI,4)} | {mp.nstr(Gp,4)} | {mp.nstr(Gp**2/(kap_lm*aHI),4)} | {mp.nstr(bound,4)} | {mp.nstr(tg,4)}")
ev5 = G.bottom_eigs(D, 'ev', k=5)
evs = ev5[0] if isinstance(ev5, tuple) else ev5
print("  even-sector spectrum vs d_{4j+8}: ", [(j, mp.nstr(evs[j], 4), mp.nstr(evs[j]/dd[j+2], 4)) for j in range(min(5, len(evs), n-2))])
