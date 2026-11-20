"""(HR) on admissible prolate data, consistent version (NUMERICAL tool).
Test functions f = sum a_k psi_k (even prolates of [-lam, lam], c = 2 pi N, k <= KMAX) restricted to the ADMISSIBLE
subspace of def:ext together with E f in P_T:  f(lam) = 0, f(0) = 0, Ff(0) = int f = 0, A(Ef) = B(Ef) = 0.
Numerator  M = W_T(Ef) on the FULL image (both parities, no projection: Ef is already in P_T).
Denominator D_g = gauge-minimised leakage, gauge = even phi supported in |x| < 1/lam with phi(0) = int phi = 0
(Legendre basis, MIN functions, the two gauge conditions imposed), D_g = D - D J H^{-1} J^T D.
Blocks: LM = k <= 4N, HI = 4N < k <= K; constraints imposed inside each block for the two-block Schur test.
Environment KTOP caps the high block (resolution).  Optional 6th argument w in {L, 0.99, 1.01, a3} (falsifier).  Usage: python3 prolate_gauge_adm.py T Nb dps KMAX MIN [w]"""
import sys, os, pickle, mpmath as mp, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as G
T = float(sys.argv[1]); Nb = int(sys.argv[2]); dps = int(sys.argv[3]); KMAX = int(sys.argv[4]); MIN = int(sys.argv[5])
WARG = sys.argv[6] if len(sys.argv) > 6 else 'L'
D = G.build(T, Nb, dps=dps, verbose=False)
mp.mp.dps = dps + 30
P = pickle.load(open(os.path.join(G.CACHE, f'sector_T{T}_N{Nb}_K{KMAX}.pkl'), 'rb'))
ks = P['ks']; d = [mp.mpf(x) for x in P['d']]; nP = len(ks)
V = mp.matrix(Nb, nP)
for i, r in enumerate(P['C']):
    for j in range(Nb): V[j, i] = mp.mpf(r[j])
Tm = mp.mpf(T); lam = mp.exp(Tm); NN = lam**2; c = 2*mp.pi*NN; FN = 4*NN
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
def leg(x, kmax):
    v = [mp.mpf(1), x]
    for k in range(2, kmax+1): v.append(((2*k-1)*x*v[-1]-(k-1)*v[-2])/k)
    return v
L0 = leg(mp.mpf(0), kl[-1])
psl = [mp.fsum(Dd[i]*mp.sqrt(kl[i]+mp.mpf(1)/2) for i in range(m))/mp.sqrt(lam) for Dd in De]          # psi_k(lam)
ps0 = [mp.fsum(Dd[i]*mp.sqrt(kl[i]+mp.mpf(1)/2)*L0[kl[i]] for i in range(m))/mp.sqrt(lam) for Dd in De]  # psi_k(0)
psI = [Dd[0]*mp.sqrt(2*lam) for Dd in De]                                                                # int psi_k
# gauge overlaps
xs, ws = G.gl_nodes(max(80, 4*MIN)); h = 1/lam
J0 = mp.matrix(nP, MIN)
for x, w in zip(xs, ws):
    lv = leg(h*x/lam, kl[-1]); psi = [mp.fsum(Dd[i]*mp.sqrt(kl[i]+mp.mpf(1)/2)*lv[kl[i]] for i in range(m))/mp.sqrt(lam) for Dd in De]
    li = leg(x, 2*MIN); pj = [mp.sqrt(mp.mpf(4*j+1)/(2*h))*li[2*j] for j in range(MIN)]
    for k in range(nP):
        for j in range(MIN): J0[k, j] += w*h*psi[k]*pj[j]
Lz = leg(mp.mpf(0), 2*MIN)
Cg = mp.matrix(MIN, 2); Cg[0, 0] = 1
for j in range(MIN): Cg[j, 1] = mp.sqrt(mp.mpf(4*j+1)/(2*h))*Lz[2*j]
Qg, _ = mp.qr(Cg, mode='full'); Bg = Qg[:, 2:]; J = J0*Bg; MG = MIN - 2
chi = [1-x for x in d]
H = mp.eye(MG)
for k in range(nP):
    for a in range(MG):
        for b in range(MG): H[a, b] -= chi[k]*J[k, a]*J[k, b]
DJ = mp.matrix(nP, MG)
for k in range(nP):
    for j in range(MG): DJ[k, j] = d[k]*J[k, j]
Dg = mp.diag(d) - DJ*mp.inverse(H)*DJ.T
print(f"# T={T} N={mp.nstr(NN,5)} 4N={mp.nstr(FN,4)} Nb={Nb} KMAX={KMAX} MIN={MIN} w={WARG}  lambda_min(H)={mp.nstr(min(mp.eigsy(H, eigvals_only=True)),4)}", flush=True)
def atoms_pi(atoms):
    L = 2*D['T']; al = [k*mp.pi/L for k in range(1, Nb+1)]; Pm = mp.matrix(Nb, Nb)
    for j in range(1, Nb+1):
        for k in range(j, Nb+1):
            Pm[j-1, k-1] = Pm[k-1, j-1] = mp.fsum(w*G._c_sym(j, k, x, L, al) for x, w in atoms)
    return Pm
if WARG == 'L': Pw = D['Pi']
elif WARG == 'a3': Pw = D['Pi'] - atoms_pi([(mp.log(2**a), 2*mp.log(2)/mp.sqrt(2**a)) for a in range(1, 8) if a*mp.log(2) < 2*D['T']])
else: Pw = mp.mpf(WARG)*D['Pi']
Mw = D['Arch'] - Pw
if os.environ.get('FASTMUL'):   # same products in python-flint at the same working precision (much faster at large Nb)
    from flint import arb_mat, ctx as fctx
    fctx.prec = int(mp.mp.dps*3.33) + 20
    toA = lambda A: arb_mat([[mp.nstr(A[i, j], mp.mp.dps) for j in range(A.cols)] for i in range(A.rows)])
    Vf = toA(V); Mf_ = Vf.transpose()*toA(Mw)*Vf; Gf_ = Vf.transpose()*Vf
    back = lambda X: mp.matrix([[mp.mpf(X[i, j].mid().str(mp.mp.dps, radius=False)) for j in range(X.ncols())] for i in range(X.nrows())])
    Mf = back(Mf_); Gf = back(Gf_)
else:
    Mf = V.T*Mw*V; Gf = V.T*V
Arow = mp.matrix(1, Nb); Brow = mp.matrix(1, Nb)
for j in range(Nb): Arow[0, j] = D['A'][j]; Brow[0, j] = D['B'][j]
AV = Arow*V; BV = Brow*V
# LAMA: Galerkin lambda_A supplied from a smaller-Nb run (it converges fast in Nb; the mp eigensolve at Nb >= 200
# exceeds the 15-minute budget).  Used only as the normalisation of the last two Schur columns.  Default: computed.
lamA = mp.mpf(os.environ['LAMA']) if os.environ.get('LAMA') else G.lambda_A(D)[0]
print(f"  lambda_A(Lambda) = {mp.nstr(lamA,5)}, d_8 = {mp.nstr(d[4],5)}, lambda_A/d_8 = {mp.nstr(lamA/d[4],4)}", flush=True)
def sub(A, I, Jx): return mp.matrix([[A[i, j] for j in Jx] for i in I])
def isq(A):
    E, W = mp.eigsy(A); return W*mp.diag([1/mp.sqrt(e) for e in E])*W.T
def gen(Ms, Ds):
    Si = isq(Ds); E2, W2 = mp.eigsy(Si*Ms*Si); return E2, Si*W2
def gmin(Ms, Ds):
    E = mp.eigsy(Ds, eigvals_only=True)
    if min(E) <= 0: return mp.nan
    return min(gen(Ms, Ds)[0])
def opn(A): return mp.sqrt(max(mp.eigsy(A*A.T, eigvals_only=True)))
def nullZ(I):
    C = mp.matrix(len(I), 5)
    for a, i in enumerate(I):
        C[a, 0] = psl[i]; C[a, 1] = ps0[i]; C[a, 2] = psI[i]; C[a, 3] = AV[0, i]; C[a, 4] = BV[0, i]
    # normalise columns, then full QR: the last len(I) - 5 columns span a subspace of the null space
    for col in range(5):
        nr = mp.sqrt(mp.fsum(C[a, col]**2 for a in range(len(I))))
        for a in range(len(I)): C[a, col] /= nr
    Q_, _ = mp.qr(C, mode='full'); return Q_[:, 5:]
def blk(I, Z): return Z.T*sub(Mf, I, I)*Z, Z.T*sub(Dg, I, I)*Z, Z.T*sub(Gf, I, I)*Z
STEP = int(os.environ.get('STEP', 1))      # evaluate every STEP-th index only (time budget at large Nb)
KTOP = int(os.environ.get('KTOP', KMAX))   # resolution cap: Galerkin images are reliable only for k <~ 0.4 Nb (see ROUND_010_A §2)
lo = [i for i in range(nP) if ks[i] <= FN]; hiall = [i for i in range(nP) if FN < ks[i] <= KTOP]
for lab, cls in (("all even k", lambda k: True), ("class +1", lambda k: k % 4 == 0)):
    hi = [i for i in hiall if cls(ks[i])]
    print(f"## (HR)(a) admissible high block, {lab}: top k | dim | alpha_HI = inf W/l_g | inf W/|F|^2 | inf W/l (fixed rep) | global inf W/l_g on admissible span k <= top")
    for t in sorted(set(list(range(6, len(hi)+1, STEP)) + [len(hi)])):
        I = hi[:t]; Z = nullZ(I); Ms, Ds, Gs = blk(I, Z); Dfix = Z.T*sub(mp.diag(d), I, I)*Z
        A_ = [i for i in range(nP) if cls(ks[i]) and ks[i] <= ks[I[-1]]]; ZA = nullZ(A_); MA, DA, GA = blk(A_, ZA)
        print(f"   {ks[I[-1]]:3d} | {t-5:2d} | {mp.nstr(gmin(Ms, Ds),4)} | {mp.nstr(gmin(Ms, Gs),4)} | {mp.nstr(gmin(Ms, Dfix),4)} | {mp.nstr(gmin(MA, DA),4)}", flush=True)
if WARG != 'L': sys.exit(0)
# ---- two-block Schur: LM_adm (k <= 4N) + HI_adm (4N < k <= top), all even k
ZL = nullZ(lo); ML, DL, GL = blk(lo, ZL); kLM = gmin(ML, DL); nl = ZL.cols
print(f"## two-block Schur, all even k: LM = k <= {ks[lo[-1]]} (admissible dim {nl}), kappa_LM = inf W/l_g = {mp.nstr(kLM,4)}, inf W/|F|^2 on LM = {mp.nstr(gmin(ML, GL),4)}")
print("  top k | alpha_HI | Gamma' (l_g metric) | Gamma'^2/(kLM aHI) | 2x2 bound | true inf W/l_g on LM+HI | mu = inf l_g/|F|^2 | bound*mu / lambda_A | inf W/|F|^2 / lambda_A | |Gram|")
for t in sorted(set(list(range(6, len(hiall)+1, 2*STEP)) + [len(hiall)])):
    I = hiall[:t]; ZH = nullZ(I); MH, DH, GH = blk(I, ZH); aHI = gmin(MH, DH)
    All = lo + I; Zb = mp.zeros(len(All), nl + ZH.cols)
    for a in range(len(lo)):
        for b in range(nl): Zb[a, b] = ZL[a, b]
    for a in range(len(I)):
        for b in range(ZH.cols): Zb[len(lo)+a, nl+b] = ZH[a, b]
    MB, DB, GB = blk(All, Zb)
    X = isq(sub(DB, range(nl, nl+ZH.cols), range(nl, nl+ZH.cols)))*sub(MB, range(nl, nl+ZH.cols), range(nl))*isq(sub(DB, range(nl), range(nl)))
    # D-normalised coupling uses the block-diagonal part of D_g; report also the D_g cross block size
    Gp = opn(X); tr = kLM + aHI; det = kLM*aHI - Gp**2; bd = (tr - mp.sqrt(tr**2 - 4*det))/2
    tg = gmin(MB, DB); mu = gmin(DB, GB); wg = gmin(MB, GB); Gn = max(mp.eigsy(GB, eigvals_only=True))
    print(f"   {ks[I[-1]]:3d} | {mp.nstr(aHI,4)} | {mp.nstr(Gp,4)} | {mp.nstr(Gp**2/(kLM*aHI),4)} | {mp.nstr(bd,4)} | {mp.nstr(tg,4)} | {mp.nstr(mu,4)} | {mp.nstr(bd*mu/lamA,4)} | {mp.nstr(wg/lamA,6)} | {mp.nstr(Gn,4)}", flush=True)
