"""Three-block class-split assembly on admissible prolate data (NUMERICAL tool; ROUND_012_B).
Same objects as prolate_gauge_adm.py (admissible data, full image numerator M = W_T(Ef), gauge-minimised leakage D_g).
Blocks, each admissible on its own (five linear conditions imposed inside each block):
  LM = even k <= 4N;  H+ = 4N < k <= top, k = 0 mod 4;  H- = 4N < k <= top, k = 2 mod 4.
Reports for each top in KLIST: gen-mins kappa_LM, alpha_+, alpha_-, alpha_HI (H+ + H- jointly admissible as in 11B),
D-normalised coupling norms G_{L+}, G_{L-}, G_{+-} (block-diagonal normalisation, as in 11B), relative size of the
D_g cross blocks, the three-block Schur bound theta3 = lambda_min of [[k,-g,-g],[-g,a+,-g],[-g,-g,a-]], the true gen-min
on LM + H+ + H-, and theta3*mu/lambda_A.  Usage: KLIST=a,b,c LAMA=.. FASTMUL=1 python3 prolate_gauge_3blk.py T Nb dps KMAX MIN"""
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
def bdiag(blocks):
    n = sum(Z.cols for _, Z in blocks); r = sum(len(I) for I, _ in blocks)
    Zb = mp.zeros(r, n); I_all = []; ro = 0; co = 0; cuts = []
    for I, Z in blocks:
        for a in range(len(I)):
            for b in range(Z.cols): Zb[ro+a, co+b] = Z[a, b]
        I_all += I; cuts.append((co, co+Z.cols)); ro += len(I); co += Z.cols
    return I_all, Zb, cuts
def rng(c): return range(c[0], c[1])
KLIST = [int(x) for x in os.environ['KLIST'].split(',')]
lo = [i for i in range(nP) if ks[i] <= FN]; ZL = nullZ(lo); ML, DL, GL = blk(lo, ZL); kLM = gmin(ML, DL)
print(f"## three-block: kappa_LM = {mp.nstr(kLM,5)} (LM admissible dim {ZL.cols}), lambda_A = {mp.nstr(lamA,5)}")
print("  top | dim+ dim- | alpha_+ | alpha_- | alpha_HI(joint) | G_L+ | G_L- | G_+- | Gamma'(L,HI) | Dcross L+ L- +- | theta3 | theta2(LM,HI) | true inf W/l_g | theta3*mu/lamA | Ritz W/|F|^2/lamA")
for top in KLIST:
    if os.environ.get('SPLIT') == 'range':   # control: split the high block by index range instead of class
        hh = [i for i in range(nP) if FN < ks[i] <= top]; Hp = hh[:len(hh)//2]; Hm = hh[len(hh)//2:]
    else:
        Hp = [i for i in range(nP) if FN < ks[i] <= top and ks[i] % 4 == 0]
        Hm = [i for i in range(nP) if FN < ks[i] <= top and ks[i] % 4 == 2]
    Hall = [i for i in range(nP) if FN < ks[i] <= top]
    Zp = nullZ(Hp); Zm = nullZ(Hm); Zh = nullZ(Hall)
    I3, Z3, cuts = bdiag([(lo, ZL), (Hp, Zp), (Hm, Zm)])
    M3, D3, G3 = blk(I3, Z3)
    S = lambda A, a, b: sub(A, rng(cuts[a]), rng(cuts[b]))
    al = [gmin(S(M3, j, j), S(D3, j, j)) for j in range(3)]
    Ri = [isq(S(D3, j, j)) for j in range(3)]
    g = {}; dc = {}
    for (a, b) in ((0, 1), (0, 2), (1, 2)):
        g[(a, b)] = opn(Ri[a]*S(M3, a, b)*Ri[b]); dc[(a, b)] = opn(Ri[a]*S(D3, a, b)*Ri[b])
    if os.environ.get('PROFILE'):   # index profile of the top singular pair of the normalised H+/H- coupling
        X = Ri[1]*S(M3, 1, 2)*Ri[2]; U, Sv, Vt = mp.svd_r(X)
        up = Z3[len(lo):len(lo)+len(Hp), cuts[1][0]:cuts[1][1]]*Ri[1]*U[:, 0]; vm = Z3[len(lo)+len(Hp):, cuts[2][0]:cuts[2][1]]*Ri[2]*Vt.T[:, 0]
        print("     H+ profile:", [(ks[i], round(float(abs(up[a])/mp.norm(up)), 2)) for a, i in enumerate(Hp)])
        print("     H- profile:", [(ks[i], round(float(abs(vm[a])/mp.norm(vm)), 2)) for a, i in enumerate(Hm)])
        print("     singular values:", [mp.nstr(x, 3) for x in Sv[:4]])
    C = mp.matrix([[al[0], -g[(0,1)], -g[(0,2)]], [-g[(0,1)], al[1], -g[(1,2)]], [-g[(0,2)], -g[(1,2)], al[2]]])
    th3 = min(mp.eigsy(C, eigvals_only=True))
    # two-block with the jointly admissible HI (as in 11B) for comparison
    I2, Z2, c2 = bdiag([(lo, ZL), (Hall, Zh)]); M2, D2, G2 = blk(I2, Z2)
    aHI = gmin(sub(M2, rng(c2[1]), rng(c2[1])), sub(D2, rng(c2[1]), rng(c2[1])))
    Gp = opn(isq(sub(D2, rng(c2[0]), rng(c2[0])))*sub(M2, rng(c2[0]), rng(c2[1]))*isq(sub(D2, rng(c2[1]), rng(c2[1]))))
    tr = kLM + aHI; th2 = (tr - mp.sqrt(tr**2 - 4*(kLM*aHI - Gp**2)))/2
    tg = gmin(M3, D3); mu = gmin(D3, G3); wg = gmin(M3, G3)
    print(f"   {top:3d} | {Zp.cols} {Zm.cols} | {mp.nstr(al[1],4)} | {mp.nstr(al[2],4)} | {mp.nstr(aHI,4)} | {mp.nstr(g[(0,1)],4)} | {mp.nstr(g[(0,2)],4)} | {mp.nstr(g[(1,2)],4)} | {mp.nstr(Gp,4)} | {mp.nstr(dc[(0,1)],3)} {mp.nstr(dc[(0,2)],3)} {mp.nstr(dc[(1,2)],3)} | {mp.nstr(th3,4)} | {mp.nstr(th2,4)} | {mp.nstr(tg,4)} | {mp.nstr(th3*mu/lamA,4)} | {mp.nstr(wg/lamA,5)}", flush=True)
