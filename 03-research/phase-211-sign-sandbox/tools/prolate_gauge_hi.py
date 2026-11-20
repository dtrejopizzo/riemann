"""(HR) test on the high prolate block with the gauge quotient (NUMERICAL tool).
Even sector of P_T; images h_k = P_+ Pi_T E psi_k (even k <= KMAX; psi_k prolates of [-lam, lam], c = 2 pi N).
M = a_T Gram of the h_k; D = diag(d_k) fixed-representative leakage; D_g = gauge-minimised leakage
    D_g = D - D J H^{-1} J^T D,  H = I - J^T diag(chi) J,
J = overlaps of the psi_k with an orthonormal even Legendre basis of L^2(-1/lam, 1/lam) (MIN functions): the gauge G_T
(functions supported in |x| < 1/lam, killed by E on I_T).  Class +1 analysis = k = 0 mod 4 (Schur chain of ROUND_009_B
with D replaced by D_g); 'all' = every even k (class -1 remnants included) for (HR)(a).
Reports, as the high block grows (4N < k <= K): alpha_HI (fixed D and gauge D_g), Gamma' (LM-HI coupling in the D_g
metric), 2x2 Schur bound, true gen-min; then the assembled lower bound for a_T / |F|^2 on the class +1 span,
kappa_C, |Gram|, and lambda_A.
Optional 6th argument w in {L, 0.99, 1.01, a3}: the weight of the comb (falsifier test; default L = Lambda).
Environment FULL=1: keep both parities of Pi_T E psi_k (full images; then 'all even k' is prob:ext-L on the block).
Usage: python3 prolate_gauge_hi.py T Nb dps KMAX MIN [w]"""
import sys, os, pickle, mpmath as mp, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as G
T = float(sys.argv[1]); Nb = int(sys.argv[2]); dps = int(sys.argv[3]); KMAX = int(sys.argv[4]); MIN = int(sys.argv[5])
D = G.build(T, Nb, dps=dps, verbose=False)
mp.mp.dps = dps + 30
P = pickle.load(open(os.path.join(G.CACHE, f'sector_T{T}_N{Nb}_K{KMAX}.pkl'), 'rb'))
ks = P['ks']; d = [mp.mpf(x) for x in P['d']]; nP = len(ks)
V = [mp.matrix([mp.mpf(x) for x in r]) for r in P['C']]
Tm = mp.mpf(T); lam = mp.exp(Tm); NN = lam**2; c = 2*mp.pi*NN; FN = 4*NN
# ---- prolate Legendre coefficients (same construction as prolate_sector.py) and gauge overlaps J
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
xs, ws = G.gl_nodes(max(80, 4*MIN)); h = 1/lam
def leg(x, kmax):
    v = [mp.mpf(1), x]
    for k in range(2, kmax+1): v.append(((2*k-1)*x*v[-1]-(k-1)*v[-2])/k)
    return v
J = mp.matrix(nP, MIN)
for x, w in zip(xs, ws):
    X = h*x/lam
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
# completeness check of the gauge expansion on the computed prolates: sum_k J_kj^2 should be 1
cmpl = min(mp.fsum(J[k, j]**2 for k in range(nP)) for j in range(MIN))
print(f"# T={T} N={mp.nstr(NN,5)} 4N={mp.nstr(FN,4)} KMAX={KMAX} MIN={MIN}  lambda_min(H)={mp.nstr(min(mp.eigsy(H, eigvals_only=True)),4)}  min_j sum_k J_kj^2={mp.nstr(cmpl,6)}", flush=True)
DJ = mp.matrix(nP, MIN)
for k in range(nP):
    for j in range(MIN): DJ[k, j] = d[k]*J[k, j]
Dg = mp.diag(d) - DJ*mp.inverse(H)*DJ.T
# ---- images in the even sector of P_T
Pr = G.projector(D); WARG = sys.argv[6] if len(sys.argv) > 6 else 'L'
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
print(f"  weight w = {WARG}")
def evn(v):
    w = Pr*v
    if os.environ.get('FULL') != '1':
        for j in range(1, Nb, 2): w[j] = 0
    return w
U = mp.matrix(Nb, nP)
for i in range(nP):
    w = evn(V[i])
    for r in range(Nb): U[r, i] = w[r]
Mf = U.T*Mw*U; Gf = U.T*U
lamA, par, res = G.lambda_A(D); lev = res['ev'][0]
print(f"  lambda_A = {mp.nstr(lamA,5)} ({par}), lambda_A^ev = {mp.nstr(lev,5)}, d_8 = {mp.nstr(d[4],5)}, lambda_A^ev/d_8 = {mp.nstr(lev/d[4],4)}", flush=True)
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

# ---- (HR)(a): high block alone, both classes and class +1, raw images (no stiff elimination needed: k > 4N)
for lab, cls in (("class +1", lambda k: k % 4 == 0), ("all even k (class -1 remnants included)", lambda k: True)):
    hi = [i for i in range(nP) if ks[i] > FN and cls(ks[i])]
    print(f"## (HR)(a) high block alone, {lab}: top k | dim | alpha_HI fixed D | alpha_HI gauge D_g | min eig D_g/D on block | alpha_HI vs Gram (M/|F|^2)")
    for t in range(1, len(hi)+1):
        I = hi[:t]
        Ms = sub(Mf, I, I); Ds = sub(mp.diag(d), I, I); Dgs = sub(Dg, I, I); Gs = sub(Gf, I, I)
        rat = min(gen(Dgs, Ds)[0])
        print(f"   {ks[I[-1]]:3d} | {t:2d} | {mp.nstr(gmin(Ms, Ds),4)} | {mp.nstr(gmin(Ms, Dgs),4)} | {mp.nstr(rat,4)} | {mp.nstr(gmin(Ms, Gs),4)}", flush=True)

# ---- admissible version: f(lambda) = 0 (def:ext), i.e. sum_k a_k psi_k(lambda) = 0; raw prolates violate it
pl = [mp.fsum(Dd[i]*mp.sqrt(kl[i]+mp.mpf(1)/2) for i in range(m))/mp.sqrt(lam) for Dd in De]
def nullZ(I):
    cvec = mp.matrix([pl[i] for i in I]); n_ = len(I)
    Q_, R_ = mp.qr(cvec, mode='full'); return Q_[:, 1:]
print("  psi_k(lambda): " + ", ".join(f"{ks[i]}:{mp.nstr(pl[i],3)}" for i in range(0, nP, 4)))
for lab, cls in (("class +1", lambda k: k % 4 == 0), ("all even k", lambda k: True)):
    hi = [i for i in range(nP) if ks[i] > FN and cls(ks[i])]
    print(f"## (HR)(a) ADMISSIBLE high block (f(lambda)=0), {lab}: top k | dim | alpha_HI gauge D_g | M/|F|^2 | global true gen-min (M, D_g) on admissible span k <= top")
    for t in range(2, len(hi)+1):
        I = hi[:t]; Z = nullZ(I)
        Ms = Z.T*sub(Mf, I, I)*Z; Dgs = Z.T*sub(Dg, I, I)*Z; Gs = Z.T*sub(Gf, I, I)*Z
        A_ = [i for i in range(nP) if cls(ks[i]) and ks[i] <= ks[I[-1]]]; ZA = nullZ(A_)
        tg = gmin(ZA.T*sub(Mf, A_, A_)*ZA, ZA.T*sub(Dg, A_, A_)*ZA)
        print(f"   {ks[I[-1]]:3d} | {t-1:2d} | {mp.nstr(gmin(Ms, Dgs),4)} | {mp.nstr(gmin(Ms, Gs),4)} | {mp.nstr(tg,4)}", flush=True)
if WARG != 'L' or os.environ.get('FULL') == '1': sys.exit(0)

# ---- class +1 Schur chain with D_g
idx = [i for i in range(nP) if ks[i] % 4 == 0]; n = len(idx); kk = [ks[i] for i in idx]
Mm = sub(Mf, idx, idx); Dm = sub(Dg, idx, idx); Gm = sub(Gf, idx, idx)
E3, V3 = gen(Mm[:3, :3], Dm[:3, :3]); o = sorted(range(3), key=lambda i: E3[i])
B = mp.zeros(n, n)
for i in range(3): B[i, 0] = V3[i, o[0]]; B[i, 1] = V3[i, o[1]]; B[i, 2] = V3[i, o[2]]
for j in range(3, n): B[j, j] = 1
Mb = B.T*Mm*B; Db = B.T*Dm*B
Sx = [1, 2]; Rx = [0] + list(range(3, n)); r = len(Rx)
MSS = sub(Mb, Sx, Sx); MSSi = mp.inverse(MSS); MRS = sub(Mb, Rx, Sx)
Mt = sub(Mb, Rx, Rx) - MRS*MSSi*MRS.T
Lf = mp.zeros(n, r)
for c_, i in enumerate(Rx): Lf[i, c_] = 1
Ss = -MSSi*MRS.T
for a_, i in enumerate(Sx):
    for c_ in range(r): Lf[i, c_] = Ss[a_, c_]
Dh = Lf.T*Db*Lf
alS = gmin(MSS, sub(Db, Sx, Sx)); ab = Mt[0, 0]/Dh[0, 0]
cut = max(c_ for c_ in range(r) if kk[Rx[c_]] <= FN) + 1
LM = list(range(cut)); kLM = gmin(sub(Mt, LM, LM), sub(Dh, LM, LM))
print(f"## class +1 Schur chain with gauge D_g: alpha_b = {mp.nstr(ab,4)}, alpha_S = {mp.nstr(alS,4)}, kappa_LM (k <= {kk[Rx[cut-1]]}) = {mp.nstr(kLM,4)}")
print("  top k | alpha_HI (D_g) | Gamma' (D_g metric) | Gamma'^2/(kLM aHI) | 2x2 bound | true gen-min (Mt, Dh_g)")
best = None
for top in range(cut+1, r+1):
    HI = list(range(cut, top)); aHI = gmin(sub(Mt, HI, HI), sub(Dh, HI, HI))
    X = isq(sub(Dh, HI, HI))*sub(Mt, HI, LM)*isq(sub(Dh, LM, LM)); Gp = opn(X)
    tr = kLM + aHI; det = kLM*aHI - Gp**2; bd = (tr - mp.sqrt(tr**2 - 4*det))/2
    tg = gmin(sub(Mt, range(top), range(top)), sub(Dh, range(top), range(top)))
    print(f"   {kk[Rx[top-1]]:3d} | {mp.nstr(aHI,4)} | {mp.nstr(Gp,4)} | {mp.nstr(Gp**2/(kLM*aHI),4)} | {mp.nstr(bd,4)} | {mp.nstr(tg,4)}", flush=True)
    best = bd
# ---- assembled lower bound on the full class +1 span (k <= KMAX):
# M(x) = Mt(r) + M_SS[s - s*(r)] >= kt * Dh(r) + M_SS[s - s*(r)] =: Q(x)   (kt = 2x2 Schur bound at top = KMAX)
kt = best
# coordinates: x = Lf r + Sfull s', s' = s - s*(r); in b-basis
Sfull = mp.zeros(n, 2); Sfull[1, 0] = 1; Sfull[2, 1] = 1
Cmat = mp.zeros(n, n)
for c_ in range(r):
    for i in range(n): Cmat[i, c_] = Lf[i, c_]
for a_ in range(2):
    for i in range(n): Cmat[i, r+a_] = Sfull[i, a_]
Qy = mp.zeros(n, n)
for i in range(r):
    for j in range(r): Qy[i, j] = kt*Dh[i, j]
for i in range(2):
    for j in range(2): Qy[r+i, r+j] = MSS[i, j]
Gy = Cmat.T*(B.T*Gm*B)*Cmat; My = Cmat.T*Mb*Cmat
low = gmin(Qy, Gy); ritz = gmin(My, Gy)
# (2.1) quantities: kappa_C = sup |a_{0,4}| / |a_{>=8}| on the lift x = Lf r; delta_g = inf Dh(r) / |a_{>=8}|^2
Xa = B*Lf     # coefficients a (prolate coordinates) of the lift
A04 = sub(Xa, [0, 1], range(r)); A8 = sub(Xa, list(range(2, n)), range(r))
kC = mp.sqrt(max(gen(A04.T*A04, A8.T*A8)[0])); dg_ = gmin(Dh, A8.T*A8)
Gn = max(mp.eigsy(Gm, eigvals_only=True))
f21 = min(kt, alS)/(2*(1+kC**2)*Gn)*dg_
print(f"## assembled (class +1, k <= {KMAX}): Schur kt = {mp.nstr(kt,4)}; lower bound inf Q/|F|^2 = {mp.nstr(low,4)} "
      f"(= {mp.nstr(low/d[4],4)} d_8 = {mp.nstr(low/lev,4)} lambda_A^ev); Ritz min a_T/|F|^2 on span = {mp.nstr(ritz,4)} (= {mp.nstr(ritz/lev,6)} lambda_A^ev)")
print(f"   (2.1) constants: kappa_C = {mp.nstr(kC,4)}, |Gram| = {mp.nstr(Gn,4)}, delta_g = inf Dh_g/|a_>=8|^2 = {mp.nstr(dg_,4)} (= {mp.nstr(dg_/d[4],4)} d_8); (2.1) value = {mp.nstr(f21,4)} = {mp.nstr(f21/lev,4)} lambda_A^ev")
