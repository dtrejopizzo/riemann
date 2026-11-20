"""Class-blind tail Gram on the high prolate block (NUMERICAL tool; ROUND_014_A).
Same objects as prolate_gauge_3blk.py. In the variable b = S a (S = diag(i^k)) reports: D-normalised diagonal and band
profile of S M S on the high indices 4N < k <= TOP, Gershgorin and banded bounds, the unconstrained bottom, the
constraint-compatible generalised minima (w.r.t. D and the gauge leakage), principal angles between the constraint
span and its S-image, the bottom eigenvector. Usage: TOP=.. FASTMUL=1 python3 prolate_tailgram.py T Nb dps KMAX MIN [w]"""
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
# ---- tail Gram in the class-blind variable b = S a (ROUND_014_A) ----
def C5(I):
    C = mp.matrix(len(I), 5)
    for a, i in enumerate(I):
        C[a, 0] = psl[i]; C[a, 1] = ps0[i]; C[a, 2] = psI[i]; C[a, 3] = AV[0, i]; C[a, 4] = BV[0, i]
    return C
def tonp(A): return np.array([[float(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
Mn = tonp(Mf); Dgn = tonp(Dg); dn = np.array([float(x) for x in d])
import scipy.linalg as sl
TOP = int(os.environ.get('TOP', '0')) or max(ks)
H = [i for i in range(nP) if FN < ks[i] <= TOP]
kH = np.array([ks[i] for i in H]); s = np.array([(-1)**(ks[i]//2) for i in H], float)   # eps_k = i^k
GH = (s[:, None]*Mn[np.ix_(H, H)]*s[None, :])          # S M S on the high block (b-variable)
DH = dn[H]; Gh = GH/np.sqrt(DH[:, None]*DH[None, :])  # D-normalised
print(f"## tail Gram, T={T}, high indices {kH[0]}..{kH[-1]} (n={len(H)}), 4N={float(FN):.2f}, c={float(c):.2f}")
print("  diag (k, Ghat_kk, d_k):", [(int(k), round(Gh[a, a], 3), round(DH[a], 4)) for a, k in enumerate(kH)])
print("  band profile, offset 2m: mean|.|, max|.|, mean signed")
for mm in range(1, 9):
    v = np.array([Gh[a, a+mm] for a in range(len(H)-mm)])
    print(f"   m={mm}: {np.mean(abs(v)):.3f} {np.max(abs(v)):.3f} {np.mean(v):+.3f}   first rows {np.round(v[:6],3)}")
# Gershgorin / banded sweep bound with D normalisation
off = np.sum(abs(Gh), 1) - abs(np.diag(Gh))
print(f"  Gershgorin: min(diag - rowsum_off) = {np.min(np.diag(Gh)-off):.3f}; min diag {np.min(np.diag(Gh)):.3f}; max rowsum_off {np.max(off):.3f}")
for bw in (1, 2, 3):
    B = np.array([[Gh[a, b] if abs(a-b) <= bw else 0 for b in range(len(H))] for a in range(len(H))])
    R = Gh - B
    print(f"   band {bw}: lmin(banded) = {np.min(np.linalg.eigvalsh(B)):.3f}, |remainder|_op = {np.max(abs(np.linalg.eigvalsh(R))):.3f}")
lmD = np.min(np.linalg.eigvalsh(Gh))
print(f"  bottom of S M S on the FULL high span (D-normalised, unconstrained, b-variable): {lmD:.4f}")
# constraint-compatible subspace: b in S V where V = admissible (5 constraints in a); in b: (C^T S) b = 0
Cb = (tonp(C5(H)).T*s[None, :]).T  # rows: constraint coefficients in b
Q, _ = np.linalg.qr(Cb/np.linalg.norm(Cb, axis=0), mode='complete'); Zb = Q[:, 5:]
Dd = np.diag(DH); DgH = s[:, None]*Dgn[np.ix_(H, H)]*s[None, :]
gm = lambda A, B: np.min(sl.eigh(Zb.T@A@Zb, Zb.T@B@Zb, eigvals_only=True))
print(f"  constraint-compatible: gen-min(SMS, D) = {gm(GH, Dd):.4f}, gen-min(SMS, S l_g S) = {gm(GH, DgH):.4f}")
# is the constraint set S-invariant? principal angles between admissible a-space and S(admissible)
Ca = tonp(C5(H)); Qa, _ = np.linalg.qr(Ca/np.linalg.norm(Ca, axis=0))
Qs, _ = np.linalg.qr((Ca.T*s[None, :]).T/np.linalg.norm(Ca, axis=0))
print("  cosines of principal angles between constraint span and its S-image:", np.round(np.linalg.svd(Qa.T@Qs, compute_uv=False), 3))
# bottom eigenvector profile
E, W = np.linalg.eigh(Gh); w0 = W[:, 0]
print("  bottom eigvec (k, b_k):", [(int(k), round(x, 2)) for k, x in zip(kH, w0)])
print("  lowest 5 eigs:", np.round(E[:5], 3))
# wedge: the low-rank (non-admissible) correction: compare with gen-min on cut index windows
for lo_, hi_ in ((0, len(H)//2), (len(H)//2, len(H))):
    sub_ = list(range(lo_, hi_)); print(f"   window k {kH[lo_]}..{kH[hi_-1]}: lmin = {np.min(np.linalg.eigvalsh(Gh[np.ix_(sub_, sub_)])):.3f}")
# gauge directions in b: g = S D J (columns); overlap of the D-bottom (constraint-compatible) with them
Jn = tonp(DJ)[H, :]*s[:, None]
Qg_, _ = np.linalg.qr(Jn)
ev_, evec_ = sl.eigh(Zb.T@GH@Zb, Zb.T@Dd@Zb); bvec = Zb@evec_[:, 0]; bvec /= np.linalg.norm(bvec)
print(f"  constraint-compatible D-bottom: |proj onto gauge span|/|b| = {np.linalg.norm(Qg_.T@bvec):.3f} (gauge rank {Jn.shape[1]})")
Pc = np.eye(len(H)) - Qg_@Qg_.T
Q2, _ = np.linalg.qr(np.hstack([Cb/np.linalg.norm(Cb, axis=0), Qg_]), mode='complete'); Z2 = Q2[:, 5+Qg_.shape[1]:]
print(f"  D-bottom on constraint-compatible ∩ gauge-orthogonal: {np.min(sl.eigh(Z2.T@GH@Z2, Z2.T@Dd@Z2, eigvals_only=True)):.4f}")
G2 = Z2.T@Gh@Z2
# symbol comparison on the diagonal: m(pi k/2)
mm = lambda t: float(mp.re(mp.digamma(mp.mpf(1)/4 + 0.5j*t)) - mp.log(mp.pi))
print("  diag vs m(pi k/2):", [(int(k), round(Gh[a, a], 3), round(mm(np.pi*k/2), 3)) for a, k in enumerate(kH) if a % 3 == 0])
if os.environ.get('SAVE'): np.savez(os.environ['SAVE'], GH=GH, DH=DH, Cb=Cb, Jn=Jn, DgH=DgH, kH=kH, s=s)
# Toeplitz fit along the index axis: sigma_hat(m) = mean of the m-th diagonal; symbol min; fit error
n_ = len(H); sh_ = [np.mean([Gh[a, a+q] for a in range(n_-q)]) for q in range(n_)]
Tp = np.array([[sh_[abs(a-b)] for b in range(n_)] for a in range(n_)])
th = np.linspace(0, np.pi, 721); sym = sh_[0] + 2*sum(sh_[q]*np.cos(q*th) for q in range(1, n_))
print(f"  Toeplitz fit: symbol min {sym.min():.3f} at theta={th[sym.argmin()]:.3f}, max {sym.max():.3f}; lmin(Tp) {np.min(np.linalg.eigvalsh(Tp)):.3f}; |Gh-Tp|_op {np.max(abs(np.linalg.eigvalsh(Gh-Tp))):.3f}")
# sweep in TOP (sub-blocks of the same build)
for top2 in [int(x) for x in os.environ.get('TOPS', '').split(',') if x]:
    I2 = [a for a in range(n_) if kH[a] <= top2]
    if len(I2) < 18: continue
    Cs = Cb[I2]; Gs = Jn[I2]; Qg2, _ = np.linalg.qr(Gs)
    Qc, _ = np.linalg.qr(Cs/np.linalg.norm(Cs, axis=0), mode='complete'); Zc = Qc[:, 5:]
    Qx, _ = np.linalg.qr(np.hstack([Cs/np.linalg.norm(Cs, axis=0), Qg2]), mode='complete'); Zx = Qx[:, 5+Qg2.shape[1]:]
    if Zx.shape[1] == 0: continue
    A_ = GH[np.ix_(I2, I2)]; Dd2 = np.diag(DH[I2]); L2 = DgH[np.ix_(I2, I2)]
    f = lambda Z, B: np.min(sl.eigh(Z.T@A_@Z, Z.T@B@Z, eigvals_only=True))
    print(f"   TOP {top2}: dim {len(I2)} | D-bottom (constr) {f(Zc, Dd2):.4f} | l_g-bottom (constr) {f(Zc, L2):.4f} | D-bottom (constr, gauge-orth, dim {Zx.shape[1]}) {f(Zx, Dd2):.4f} | lmin unconstrained {np.min(np.linalg.eigvalsh(A_)):.4f}")
