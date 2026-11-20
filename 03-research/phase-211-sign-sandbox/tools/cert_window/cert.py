"""Stage 2: inertia certificate of Paper 47 prop:lowercert (c = 0, primitive form) from build_G output.
usage: cert.py G.pkl par k1 mu1,mu2,... [prec]
Certifies: a_T >= mu on the unit sphere of P_T^par  (n_-(R') <= 1 via Householder + Haynsworth,
then positive definiteness of the Schur complement S by recursive block Schur complements in balls).
"""
import sys, time, json, pickle
import numpy as np
from flint import arb, arb_mat, ctx

fn, par, k1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
mus = sys.argv[4].split(',')
PREC = int(sys.argv[5]) if len(sys.argv) > 5 else 320
ctx.prec = PREC
d = pickle.load(open(fn, 'rb'))
t0 = time.time()
def unser(t):
    m, r = t
    return arb(m, r * 1.0001 + 1e-110 * (1 + abs(float(m))))
Texpr = d['Texpr']
if Texpr == '1': T = arb(1)
elif Texpr == 'log5h': T = arb(5).log() / 2
elif Texpr == '1.2': T = arb(6) / 5
elif Texpr == '1.035': T = arb(207) / 200
elif Texpr == '1.098': T = arb(549) / 500
elif Texpr == 'log15h+0.01': T = arb(15).log() / 2 + arb(1) / 100
PI = arb.pi()
K2 = d['K2']; tauN = d['tauN']
s_inf = arb(d['s_inf'][0]) / d['s_inf'][1]
om_p = arb(d['om_p']); om_m = arb(d['om_m'])
qerr = arb(arb(d['qerr']).upper()); qerrD = arb(arb(d['qerrD']).upper())
rows = list(range(par, K2, 2)); nR = len(rows)
nE = len([l for l in rows if l < k1]); assert rows[nE - 1] < k1 <= rows[nE] if nE < nR else True
Graw = d['G'][par]
sc = [(2 * T / PI * (2 * l + 1)).sqrt() * (1 if ((l - par) // 2) % 2 == 0 else -1) for l in rows]
G = arb_mat(nR, nR)
for a in range(nR):
    for b in range(nR):
        G[a, b] = sc[a] * sc[b] * (unser(Graw[a][b]) + arb(0, float(qerr.str(5, radius=False)) * 1.001))
print(f'[load] nR={nR} nE={nE} {time.time()-t0:.0f}s', flush=True)
cst = T * tauN
def Lam_star(k):
    df = arb(1)
    for q in range(1, 2 * k + 2, 2): df *= q
    term = cst ** (2 * k + 1) / df ** 2; tot = arb(0); j = k
    while True:
        tot += term; ratio = cst ** 2 / arb((2 * j + 3) ** 2); term = term * ratio; j += 1
        if ratio < arb(1) / 2 and term < tot * arb(2) ** (-PREC): break
    tot += arb(0, (2 * term).upper())
    return 2 / PI * tot
LamK2 = Lam_star(K2)
# trace of P_Y S_c P_Y over the parity, Y = degrees >= k1:  sum_{k1<=l<K2, par} (2T/pi)(2l+1) D_l + Lam*_K2
Dl = [unser(t) for t in d['D']]
trY = sum(((2 * T / PI) * (2 * l + 1) * (Dl[l] + arb(0, float(qerrD.str(5, radius=False)) * 1.001)) for l in rows if l >= k1), arb(0)) + LamK2
print(f'[trace] tr(P_Y S_c P_Y) <= {trY.str(5)},  Lam*_K2 = {LamK2.str(3)}', flush=True)
xh = T / 2
chi = [((2 * l + 1) / (2 * T)).sqrt() * 2 * T * (PI / (2 * xh)).sqrt() * xh.bessel_i(arb(l) + arb(1) / 2) for l in rows]
chinorm2 = T.sinh() + (T if par == 0 else -T)

def sub(M, r0, r1, c0, c1):
    S = arb_mat(r1 - r0, c1 - c0)
    for i in range(r0, r1):
        for j in range(c0, c1): S[i - r0, j - c0] = M[i, j]
    return S

def pd(A, n, depth=0):
    """certify the symmetric ball matrix A (n x n) positive definite; returns min pivot info or None"""
    if n <= 48:
        # midpoint Cholesky L (approximate), X = L^{-1} (exact arb matrix of midpoints, lower triangular with
        # nonzero diagonal, hence invertible); A PD  <=>  X A X^T PD, certified by Gershgorin on X A X^T.
        Am = [[arb(A[i, j].mid()) for j in range(n)] for i in range(n)]
        L = [[arb(0)] * n for _ in range(n)]
        for j in range(n):
            v = Am[j][j] - sum((L[j][k] * L[j][k] for k in range(j)), arb(0))
            if not v.mid() > 0:
                print(f'    leaf midpoint not PD depth {depth} j={j}/{n} v={v.str(5)}', flush=True); return None
            L[j][j] = arb(v.sqrt().mid())
            for i in range(j + 1, n):
                L[i][j] = arb(((Am[i][j] - sum((L[i][k] * L[j][k] for k in range(j)), arb(0))) / L[j][j]).mid())
        X = [[arb(0)] * n for _ in range(n)]
        for i in range(n):
            X[i][i] = arb((1 / L[i][i]).mid())
            for j in range(i):
                X[i][j] = arb((-sum((L[i][k] * X[k][j] for k in range(j, i)), arb(0)) / L[i][i]).mid())
        Xm = arb_mat(n, n, [X[i][j] for i in range(n) for j in range(n)])
        M = Xm * A * Xm.transpose()
        worst = None
        for i in range(n):
            g = M[i, i] - sum((abs(M[i, j]) for j in range(n) if j != i), arb(0))
            if not g > 0:
                print(f'    leaf Gershgorin fails depth {depth} row {i}/{n}: {g.str(5)}', flush=True); return None
            worst = g if worst is None or float(g.mid()) < float(worst.mid()) else worst
        return worst
    h = n // 2
    A11 = sub(A, 0, h, 0, h)
    p1 = pd(A11, h, depth + 1)
    if p1 is None: return None
    B12 = sub(A, 0, h, h, n)
    X = A11.solve(B12, nonstop=True)
    if not X[0, 0].is_finite():
        print(f'    solve failed depth {depth} n={n}', flush=True); return None
    S = sub(A, h, n, h, n) - B12.transpose() * X
    S = (S + S.transpose()) / 2      # the exact Schur complement is symmetric; still enclosed
    p2 = pd(S, n - h, depth + 1)
    if p2 is None: return None
    return p1 if float(p1.mid()) < float(p2.mid()) else p2


def strip(M):
    return arb_mat(M.nrows(), M.ncols(), [arb(M[i, j].mid()) for i in range(M.nrows()) for j in range(M.ncols())])

def chol_inv(A):
    """approximate inverse of the Cholesky factor of the (midpoint) matrix A; returns an exact
    lower-triangular arb_mat X (midpoints only) or None if a midpoint pivot is not positive"""
    n = A.nrows()
    if n <= 48:
        Am = [[arb(A[i, j].mid()) for j in range(n)] for i in range(n)]
        L = [[arb(0)] * n for _ in range(n)]
        for j in range(n):
            v = Am[j][j] - sum((L[j][k] * L[j][k] for k in range(j)), arb(0))
            if not v.mid() > 0: return None
            L[j][j] = arb(v.sqrt().mid())
            for i in range(j + 1, n):
                L[i][j] = arb(((Am[i][j] - sum((L[i][k] * L[j][k] for k in range(j)), arb(0))) / L[j][j]).mid())
        X = [[arb(0)] * n for _ in range(n)]
        for i in range(n):
            X[i][i] = arb((1 / L[i][i]).mid())
            for j in range(i):
                X[i][j] = arb((-sum((L[i][k] * X[k][j] for k in range(j, i)), arb(0)) / L[i][i]).mid())
        return arb_mat(n, n, [X[i][j] for i in range(n) for j in range(n)])
    h = n // 2
    A11 = sub(A, 0, h, 0, h); B = sub(A, h, n, 0, h); C = sub(A, h, n, h, n)
    X11 = chol_inv(A11)
    if X11 is None: return None
    L21 = strip(B * X11.transpose())                  # B L11^{-T}
    X22 = chol_inv(strip(C - L21 * L21.transpose()))
    if X22 is None: return None
    X21 = strip(-(X22 * L21 * X11))
    X = arb_mat(n, n)
    for i in range(h):
        for j in range(i + 1): X[i, j] = X11[i, j]
    for i in range(n - h):
        for j in range(h): X[h + i, j] = X21[i, j]
        for j in range(i + 1): X[h + i, h + j] = X22[i, j]
    return X

def pd_global(S):
    n = S.nrows()
    X = chol_inv(strip(S))
    if X is None:
        print('    midpoint Cholesky fails', flush=True); return None
    M = X * S * X.transpose()
    worst = None
    for i in range(n):
        g = M[i, i] - sum((abs(M[i, j]) for j in range(n) if j != i), arb(0))
        if not g > 0:
            print(f'    Gershgorin fails row {i}/{n}: {g.str(5)}', flush=True); return None
        worst = g if worst is None or float(g.mid()) < float(worst.mid()) else worst
    return worst

results = []
for mu_s in mus:
    mu = arb(mu_s)
    qY = s_inf - mu - om_p * trY
    assert qY > 0, 'q_Y not positive'
    beta = (om_p + om_m) * LamK2.sqrt()
    PK2chi2 = chinorm2 - sum((c * c for c in chi), arb(0))
    PK2chi_up = arb(max(float(PK2chi2.upper().str(10, radius=False)), 0) * 1.0001 + 1e-200).sqrt()
    PYchi2 = chinorm2 - sum((chi[a] * chi[a] for a in range(nE)), arb(0))
    GEY = sub(G, 0, nE, nE, nR)
    chiY = arb_mat(nR - nE, 1, [chi[c] for c in range(nE, nR)])
    gram = GEY * GEY.transpose()
    cross = GEY * chiY
    bb = arb(0, (beta * beta).upper())
    Rxx = arb_mat(nE, nE)
    for a in range(nE):
        for b in range(nE):
            v = -G[a, b] - (gram[a, b] + bb) / qY
            if a == b: v += s_inf - mu
            Rxx[a, b] = v
    rx = arb_mat(nE, 1, [chi[a] + (cross[a, 0] + arb(0, (beta * PK2chi_up).upper())) / qY for a in range(nE)])
    dup = arb((PYchi2 / qY).upper()); Rxi = -dup
    dd = nE
    rmid = np.array([float(rx[a, 0].mid()) for a in range(dd)])
    v = rmid.copy(); v[0] += np.sign(rmid[0]) * np.linalg.norm(rmid)
    Hf = np.eye(dd) - 2.0 * np.outer(v, v) / np.dot(v, v)
    H = arb_mat(dd, dd, [arb(float(Hf[i, j])) for i in range(dd) for j in range(dd)])
    HtH = H.transpose() * H
    offmax = max(sum((abs(HtH[i, j] - (1 if i == j else 0)) for j in range(dd)), arb(0)).upper() for i in range(dd))
    assert arb(offmax) < 1, 'H not certified invertible'
    Rp = H.transpose() * Rxx * H
    rp = H.transpose() * rx
    Btt, Btx, Bxx = Rp[0, 0], rp[0, 0], Rxi
    detB = Btt * Bxx - Btx * Btx
    assert detB < 0, 'det B not certified negative'
    i_tt, i_tx, i_xx = Bxx / detB, -Btx / detB, Btt / detB
    n = dd - 1
    S = arb_mat(n, n)
    for a in range(n):
        ua, wa = Rp[a + 1, 0], rp[a + 1, 0]
        for b in range(a, n):
            ub, wb = Rp[b + 1, 0], rp[b + 1, 0]
            val = Rp[a + 1, b + 1] - (ua * ub * i_tt + (ua * wb + wa * ub) * i_tx + wa * wb * i_xx)
            S[a, b] = val; S[b, a] = val
    if mu_s == mus[0]:
        Sm = np.array([[float(S[a, b].mid()) for b in range(n)] for a in range(n)])
        ev = np.linalg.eigvalsh(Sm)[:3]
    else: ev = None
    piv = pd_global(S)
    res = dict(fn=fn, par=par, k1=k1, nE=nE, K2=K2, tauN=tauN, mu=mu_s, prec=PREC, certified=piv is not None,
               min_pivot=None if piv is None else piv.str(8), qY=qY.str(8), trY=trY.str(5),
               beta=beta.str(3), detB=detB.str(5), maxrad_S=max(float(S[a, a].rad().str(3, radius=False)) for a in range(n)),
               S_mid_eigs_double=None if ev is None else [float(x) for x in ev], seconds=time.time() - t0)
    print(json.dumps(res), flush=True)
    results.append(res)
json.dump(results, open(f'cert_{fn[:-4]}_par{par}_k{k1}.json', 'w'), indent=1)
