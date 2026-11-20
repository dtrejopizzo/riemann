# Certified lower bound  Q[F] >= kappa * l_g^fam[F]  on the transported constraint space V, R = 3 cells (window log 3).
# Q[F] = Lev[D F] - c*Pi[D F] + 2 A(DF) B(DF)  (complete form of ROUND_016_B Lemma 2.3 on the idealised 3-cell data),
# D F = F + 2^{-1/2} F(.-log 2) on [0, log 3]; Pi[H] = (2 log2/sqrt2) <H(.-log2), H>;
# l_g^fam[F] = |F|^2 - c_F^T G^{-1} c_F, gauge family g_l(y) = P_{2l}(lam y) 1_{|y|<1/lam}, l < J (upper bound for the closure l_g).
# Basis: piecewise Legendre, pieces [0,log1.5],[log1.5,log2],[log2,log3], degree < n each.  Proof: ROUND_018_A section 3.
# usage: python3 cert3.py TAUSTAR n T J KAPPA [c]
import sys, time, numpy as np
from flint import arb, acb, arb_mat, ctx
ctx.prec = 128
t0 = time.time()
ts = int(sys.argv[1]); n = int(sys.argv[2]); Tn = sys.argv[3]; J = int(sys.argv[4]); KAP = arb(sys.argv[5])
cc = arb(sys.argv[6]) if len(sys.argv) > 6 else arb(1)
pi = arb.pi(); T = arb(Tn); lam = T.exp(); ell = arb(3).log()
cuts = [arb(0), (arb(3) / 2).log(), arb(2).log(), ell]; P = 3; N = P * n
cen = [(cuts[p] + cuts[p + 1]) / 2 for p in range(P)]; hl = [(cuts[p + 1] - cuts[p]) / 2 for p in range(P)]
def mre(t): return ((acb(arb(1) / 4) + t * acb(0, 1) / 2).digamma() + (acb(arb(1) / 4) - t * acb(0, 1) / 2).digamma()).real / 2 - pi.log()
M = mre(acb(ts)); C0 = mre(acb(0))
dfact = [arb(1)]
for l in range(1, 2 * max(n, 2 * J) + 3): dfact.append(dfact[-1] * (2 * l + 1))
def jl(l, z):  # real z
    return z ** l / dfact[l] * (-z * z / 4).hypgeom_0f1(arb(l) + arb(3) / 2)
def glnodes(Q):
    return [arb.legendre_p_root(Q, k, weight=True) for k in range(Q)]
# ---------- (1) truncated-symbol matrix G on the piecewise basis
NQ = 40; gl = glnodes(NQ)
Ure = arb_mat(N, ts * NQ); Uim = arb_mat(N, ts * NQ); col = 0; wts = []
for pnl in range(ts):
    for x, w in gl:
        t = arb(pnl) + (x + 1) / 2
        hv = M - mre(acb(t)); wts.append(w / 2 * hv / pi)
        for p in range(P):
            ph = -t * cen[p]; cph = ph.cos(); sph = ph.sin(); z = t * hl[p]
            for l in range(n):
                a = (arb(2 * l + 1) * 2 * hl[p]).sqrt() * jl(l, z)
                # (-i)^l * e^{i ph}
                k4 = l % 4
                re, im = [(cph, sph), (sph, -cph), (-cph, -sph), (-sph, cph)][k4]
                Ure[p * n + l, col] = a * re; Uim[p * n + l, col] = a * im
        col += 1
print('symbol nodes', round(time.time() - t0), flush=True)
UreW = arb_mat(ts * NQ, N); UimW = arb_mat(ts * NQ, N)
for j in range(ts * NQ):
    for a_ in range(N): UreW[j, a_] = Ure[a_, j] * wts[j]; UimW[j, a_] = Uim[a_, j] * wts[j]
G = Ure * UreW + Uim * UimW
# quadrature remainder (Bernstein ellipse rho=2, half-length 1/2 => |Im t| <= 3/8): |u_a| <= sqrt(2(2l+1)hl) e^{(3/8)(|c_p|+hl_p)}
rho = arb(2); Hb = (M - C0) + (arb(256) / 7 + arb(832) / 3000) * (arb(ts) + 1) ** 2
cmax = max(abs(c) + h for c, h in zip(cen, hl)).upper()
Bu = (arb(2 * (2 * n - 1)) * 2 * max(hl, key=lambda h: h.upper())) * (arb(3) / 4 * arb(cmax)).exp()
qerr = arb(ts) / 2 * arb(64) / 15 * Hb * Bu / pi * rho ** (-2 * NQ) / (rho ** 2 - 1)
for i in range(N):
    for j in range(N): G[i, j] = G[i, j] + arb(0, qerr.upper())
print('G built', round(time.time() - t0), 'qerr', qerr.str(3), flush=True)
# ---------- (2) exact D, Pi
v2 = 2 * arb(2).log() / arb(2).sqrt()
Dm = arb_mat(N, N); Pim = arb_mat(N, N)
for i in range(N): Dm[i, i] = arb(1)
for l in range(n):
    Dm[2 * n + l, l] = 1 / arb(2).sqrt()
    Pim[2 * n + l, l] = v2 / 2; Pim[l, 2 * n + l] = v2 / 2
# ---------- (3) analytic weights: projections, norms, leakage, via Gauss-Legendre on each piece + Bernstein bound (rho=3)
import os; QW = int(os.environ.get("QW", "160")); glw = glnodes(QW); rW = arb(3)
xw = lambda y: y - T - ell
ns = [k for k in range(1, 60) if arb(k) * (-T).exp() < lam]
def weights(y):
    xi = (-xw(y)).exp(); wt = xi.sqrt(); out = {}
    out['pA'] = (xw(y) / 2).exp(); out['pB'] = (-xw(y) / 2).exp()
    out['f0'] = 2 * wt; out['flam'] = 2 * (2 * pi * lam * xi).cos() * wt
    sA = arb(0); sB = arb(0)
    for k in ns:
        a = arb(k) * (-T).exp(); b = arb(k) * T.exp()
        if b > lam: b = lam
        sA += 2 * ((2 * pi * xi * b).sin() - (2 * pi * xi * a).sin()) / (2 * pi * xi) / k
        sB += 2 * ((2 * pi * xi * b).ci() - (2 * pi * xi * a).ci())
    out['A'] = sA * wt; out['B'] = sB * wt
    for l in range(J): out[('g', l)] = wt * (2 / lam) * (-1) ** l * jl(2 * l, 2 * pi * xi / lam)
    return out
keys = ['pA', 'pB', 'f0', 'flam', 'A', 'B'] + [('g', l) for l in range(J)]
proj = {k: arb_mat(N, 1) for k in keys}; nrm = {k: arb(0) for k in keys}
for p in range(P):
    for x, w in glw:
        y = cen[p] + hl[p] * x; wv = weights(y); ww = w * hl[p]
        for l in range(n):
            ph = (arb(2 * l + 1) / (2 * hl[p])).sqrt() * x.legendre_p(l) * ww
            for k in keys: proj[k][p * n + l, 0] += ph * wv[k]
        for k in keys: nrm[k] += ww * wv[k] ** 2
# Bernstein bound for the y-quadratures: on the ellipse, |y - c_p| <= hl*(rho+1/rho)/2, |Im y| <= hl*(rho-1/rho)/2 ;
# |xi| <= XIB := e^{T + ell + 0.5};  |Im(2 pi xi s)| <= 2 pi XIB s.  |P_l| <= rho^l on E_rho (Chebyshev expansion with
# nonnegative coefficients summing to 1).  Crude sup bounds of every weight by WB below.
XIB = (T + ell + arb(1) / 2).exp()
EB = (2 * pi * lam * XIB).exp()
WB = EB * XIB * (arb(len(ns)) * (1 + 4 * T) + 4)
hmax = max(hl, key=lambda h: h.upper())
PB = (arb(2 * n + 1) / (2 * min(hl, key=lambda h: h.lower()))).sqrt() * rW ** n
werr = P * hmax * arb(64) / 15 * WB * PB * rW ** (-2 * QW) / (rW ** 2 - 1)
nerr = P * hmax * arb(64) / 15 * WB ** 2 * rW ** (-2 * QW) / (rW ** 2 - 1)
for k in keys:
    for i in range(N): proj[k][i, 0] = proj[k][i, 0] + arb(0, werr.upper())
    nrm[k] = nrm[k] + arb(0, nerr.upper())
def leak(k):
    s2 = sum((proj[k][i, 0] ** 2 for i in range(N)), arb(0)); d = nrm[k] - s2
    return arb(d.upper()).sqrt() if d.upper() > 0 else arb(0)
dl = {k: leak(k) for k in keys}
print('weights', round(time.time() - t0), 'werr', werr.str(3), 'max leak', max(float(dl[k].upper()) for k in keys), flush=True)
# ---------- (4) gauge Gram over (lam, inf): G_lk = delta_lk/(lam(4l+1)) - int_0^lam ghat_l ghat_k
GG = arb_mat(J, J)
for l in range(J): GG[l, l] = 1 / (lam * (4 * l + 1))
for x, w in glw:
    xi = lam * (x + 1) / 2; ww = w * lam / 2
    g = [(2 / lam) * (-1) ** l * jl(2 * l, 2 * pi * xi / lam) for l in range(J)]
    for l in range(J):
        for k in range(J): GG[l, k] -= ww * g[l] * g[k]
gerr = lam / 2 * arb(64) / 15 * (4 / lam ** 2) * (4 * pi * arb(2) / 3).exp() * rW ** (-2 * QW) / (rW ** 2 - 1)
for l in range(J):
    for k in range(J): GG[l, k] = GG[l, k] + arb(0, gerr.upper())
X = GG.inv()
Cg = arb_mat(N, J)
for l in range(J):
    for i in range(N): Cg[i, l] = proj[('g', l)][i, 0]
# ---------- (5) P-block of Phi = Q - kappa*l_g
al = Dm.transpose() * proj['pA']; be = Dm.transpose() * proj['pB']
Arch = arb_mat(N, N)
for i in range(N):
    for j in range(N): Arch[i, j] = (M if i == j else 0) - G[i, j]
QP = Dm.transpose() * (Arch - Pim * cc) * Dm + al * be.transpose() + be * al.transpose()
Phi = QP + Cg * X * Cg.transpose() * KAP
for i in range(N): Phi[i, i] = Phi[i, i] - KAP
Wm = arb_mat(N, 4)
for j, k in enumerate(['f0', 'flam', 'A', 'B']):
    for i in range(N): Wm[i, j] = proj[k][i, 0]
Gw = Wm.transpose() * Wm; Gwi = Gw.inv(); PW = Wm * Gwi * Wm.transpose()
Pi_ = arb_mat(N, N)
for i in range(N):
    for j in range(N): Pi_[i, j] = (1 if i == j else 0) - PW[i, j]
# float guess for gamma
Pf = np.array([[float(Phi[i, j].mid()) for j in range(N)] for i in range(N)])
Wf = np.array([[float(Wm[i, j].mid()) for j in range(4)] for i in range(N)])
import scipy.linalg as sl
Vn = sl.null_space(Wf.T); gfl = np.linalg.eigvalsh(Vn.T @ Pf @ Vn)[0]
gam = arb(gfl * 0.9)
print('float gamma', gfl, flush=True)
S = arb_mat(N, N)
for i in range(N):
    for j in range(N): S[i, j] = Phi[i, j] - (gam if i == j else 0)
S = Pi_ * S * Pi_ + Wm * Wm.transpose()
def ldl_pd(S):
    n_ = S.nrows(); A = [[S[i, j] for j in range(n_)] for i in range(n_)]; d = []
    for j in range(n_):
        dj = A[j][j]
        if not dj > 0: return False, j
        d.append(dj)
        for i in range(j + 1, n_):
            lij = A[i][j] / dj
            Ai = A[i]; Aj = A[j]
            for kk in range(j + 1, i + 1): Ai[kk] = Ai[kk] - lij * A[kk][j]
    return True, min(float(x.lower()) for x in d)
ok, info = ldl_pd(S)
print('PD', ok, info, round(time.time() - t0), flush=True)
# ---------- (6) assemble
fact = arb(1)
for j in range(1, n + 1): fact *= j
Ltot = ell; lmax = 2 * hmax
eps = Ltot * arb(ts) / pi * (M - C0) * (arb(ts) * lmax / 2) ** n / fact
gin = sum((Gwi[i, j] ** 2 for i in range(4) for j in range(4)), arb(0)).sqrt()
eta = (sum((dl[k] ** 2 for k in ['f0', 'flam', 'A', 'B']), arb(0)) * gin).sqrt()
nPhi = sum((Phi[i, j] ** 2 for i in range(N) for j in range(N)), arb(0)).sqrt()
nX = sum((X[i, j] ** 2 for i in range(J) for j in range(J)), arb(0)).sqrt()
nCg = sum((Cg[i, j] ** 2 for i in range(N) for j in range(J)), arb(0)).sqrt()
dg = sum((dl[('g', l)] ** 2 for l in range(J)), arb(0)).sqrt()
nal = sum((al[i, 0] ** 2 for i in range(N)), arb(0)).sqrt(); nbe = sum((be[i, 0] ** 2 for i in range(N)), arb(0)).sqrt()
da = arb(2).sqrt() * dl['pA']; db = arb(2).sqrt() * dl['pB']
Xc = nPhi * eta + 2 * eps + (nal * db + nbe * da) + KAP * nX * nCg * dg
Yc = (M - eps - v2 * abs(cc)) / 2 - KAP - gam * eta ** 2 - nPhi * eta ** 2 - 2 * da * db
okall = ok and (gam > 0) and (Yc > 0) and (Xc ** 2 < gam * Yc)
print(f"tau*={ts} n={n} T={Tn} J={J} kappa={KAP} c={cc}: M={M.str(8)} eps={eps.str(3)} eta={eta.str(3)} gauge-leak={dg.str(3)} gamma={gam.str(6)} X={Xc.str(3)} Y={Yc.str(5)} |Phi_P|={nPhi.str(4)}")
print(f"CERTIFIED={okall}: Q[F] >= {KAP} * l_g^fam[F] on V (3 cells, T={Tn}, J={J}); time {round(time.time()-t0)}s", flush=True)
