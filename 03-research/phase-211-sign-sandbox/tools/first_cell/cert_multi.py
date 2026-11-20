# Certified lower bound for the Levy form on a window of length log 2 under one constraint <F, e^{-x/2}> = 0.
# Form: A[F] = (1/2pi) int m(tau)|F^(tau)|^2, m(tau) = Re psi(1/4 + i tau/2) - log pi.
# Lower bound: m >= min(m, M), M = m(tau*);  A[F] >= M|F|^2 - <G F, F>,  G = Op((M - m) 1_{|tau|<tau*}) >= 0.
# multi-constraint version: constraints <F, w_i> = 0, i in KEYS (subset of f0,flam,A,B), window xw = x - T - L/2
# usage: python3 cert_multi.py TAUSTAR n T KEYS   e.g. 50 72 0.8 f0,flam,A,B
import sys, numpy as np
from flint import arb, acb, arb_mat, ctx
ctx.prec = 120
ts = int(sys.argv[1]); n = int(sys.argv[2]); Tn = sys.argv[3]; KEYS = sys.argv[4].split(','); NQ = 40
L = arb(2).log(); pi = arb.pi(); half = arb(1) / 2
def mre(t):  # Re psi(1/4 + i t/2) - log pi, as analytic function of t (acb)
    return ((acb(arb(1)/4) + t * acb(0, 1) / 2).digamma() + (acb(arb(1)/4) - t * acb(0, 1) / 2).digamma()) / 2 - pi.log()
M = mre(acb(ts)).real
dfact = [arb(1)]
for l in range(1, n + 1): dfact.append(dfact[-1] * (2 * l + 1))
def jl(l, z): return z ** l / dfact[l] * (-z * z / 4).hypgeom_0f1(acb(l) + arb(3) / 2)
# --- quadrature: panels [p, p+1], Gauss-Legendre NQ nodes
gl = [arb.legendre_p_root(NQ, k, weight=True) for k in range(NQ)]
cols = []; wts = []
for p in range(ts):
    for x, w in gl:
        t = arb(p) + (x + 1) / 2
        hv = M - mre(acb(t)).real
        z = acb(t * L / 2)
        cols.append([(arb(2 * l + 1) * L).sqrt() * jl(l, z).real for l in range(n)])
        wts.append(w / 2 * hv / pi)
Aq = arb_mat(n, len(cols)); Aw = arb_mat(len(cols), n)
for j, c in enumerate(cols):
    for l in range(n): Aq[l, j] = c[l]; Aw[j, l] = c[l] * wts[j]
H = Aq * Aw
# sign (-i)^l i^k = (-1)^((k-l)/2) for k-l even; zero otherwise
for l in range(n):
    for k in range(n):
        H[l, k] = H[l, k] * (((-1) ** ((k - l) // 2)) if (k - l) % 2 == 0 else 0)
# --- rigorous quadrature remainder (Bernstein ellipse rho=2 on each panel, half-length 1/2):
# |E| <= r*(64/15)*B*rho^(-2N)/(rho^2-1), B = sup_ellipse |h|*|a_l a_k|/pi ; |a_l| <= sqrt((2l+1)L) e^{L|Im t|/2}
rho = arb(2); a_ax = arb(5) / 8; b_ax = arb(3) / 8
# |h| on the ellipse: h = M - C0 - phi(tau^2), phi(x) = sum_k x/(a_k(x+4a_k^2)), a_k = k+1/4 (Paper 47 thm:S);
# for |Im tau| <= 3/8: |tau^2+4a_0^2| >= 7/64, |tau^2+4a_k^2| >= 3a_k^2 (k>=1), sum_{k>=1} a_k^-3 <= 0.832
Hb = (M - mre(acb(0)).real) + (arb(256) / 7 + arb(832) / 3000) * (arb(ts) + 1) ** 2
B = Hb * (2 * n - 1) * L * (L * b_ax).exp() / pi
qerr = ts * half * arb(64) / 15 * B * rho ** (-2 * NQ) / (rho ** 2 - 1)
for l in range(n):
    for k in range(n):
        if (k - l) % 2 == 0: H[l, k] = H[l, k] + arb(0, qerr.upper())
# --- constraint vectors (transported functionals of ROUND_016_B, cellRp.py), computed by rigorous integration
T = arb(Tn); lam = T.exp(); tp = 2 * pi
def xi_(x): return lam * (L / 2).exp() * (-x).exp()
def wfun(key, x):  # x acb on I
    xi = acb(lam * (L / 2).exp()) * (-x).exp(); wt = xi.sqrt()
    if key == 'f0': return 2 * wt
    if key == 'flam': return 2 * (tp * acb(lam) * xi).cos() * wt
    s_ = acb(0); lo = lambda nn: arb(nn) * (-T).exp()
    for nn in range(1, 50):
        if not (lo(nn) < lam): break
        aa = lo(nn); bb = lam
        if key == 'A': s_ += 2 * ((tp * xi * bb).sin() - (tp * xi * aa).sin()) / (tp * xi) / nn
        if key == 'B': s_ += 2 * ((tp * xi * bb).ci() - (tp * xi * aa).ci())
    return s_ * wt
k = len(KEYS); Wm = arb_mat(n, k); delt = []
for i, key in enumerate(KEYS):
    nrm = acb.integral(lambda x, an: wfun(key, x) ** 2, -L / 2, L / 2).real
    s2 = arb(0)
    for l in range(n):
        v = acb.integral(lambda x, an: wfun(key, x) * (2 * x / L).legendre_p(l), -L / 2, L / 2).real * (arb(2 * l + 1) / L).sqrt()
        Wm[l, i] = v; s2 += v * v
    dl2 = nrm - s2
    delt.append(arb(dl2.upper()).sqrt() if dl2.upper() > 0 else arb(0))
    print(key, '||w||^2', nrm.str(8), '||(1-P)w||^2 <=', dl2.upper(), flush=True)
Gm = Wm.transpose() * Wm; Gi = Gm.inv()
Pi_ = arb_mat(n, n); PW = Wm * Gi * Wm.transpose()
for i in range(n):
    for j in range(n): Pi_[i, j] = (1 if i == j else 0) - PW[i, j]
# sigma_min(W)^2 = 1/||Gi||; bound ||Gi|| by Frobenius
gin = arb(0)
for i in range(k):
    for j in range(k): gin += Gi[i, j] ** 2
eta = (sum(d * d for d in delt) * gin.sqrt()).sqrt()
Hm = np.array([[float(H[i, j].mid()) for j in range(n)] for i in range(n)])
Pm = np.array([[float(Pi_[i, j].mid()) for j in range(n)] for i in range(n)])
gam = np.linalg.eigvalsh(Pm @ Hm @ Pm).max() + 1e-12
g = arb(gam)
S = arb_mat(n, n)
for i in range(n):
    for j in range(n): S[i, j] = (g if i == j else 0) - H[i, j]
S = Pi_ * S * Pi_ + Wm * Wm.transpose()
def ldl_pd(S):
    n = S.nrows(); A = [[S[i, j] for j in range(n)] for i in range(n)]; d = []
    for j in range(n):
        dj = A[j][j]
        if not dj > 0: return False, j
        d.append(dj)
        for i in range(j + 1, n):
            lij = A[i][j] / dj
            for kk in range(j + 1, i + 1): A[i][kk] = A[i][kk] - lij * A[kk][j]
    return True, min(float(x.lower()) for x in d)
ok, info = ldl_pd(S)
fact = arb(1)
for j in range(1, n + 1): fact *= j
# --- tail bounds
gmax = M - mre(acb(0)).real                       # sup h = M - C0  (m increasing)
eps = L * arb(ts) / pi * gmax * (arb(ts) * L / 2) ** n / fact   # ||(1-P)G||_HS
c = eps + gmax * eta; d = eps + gmax * eta ** 2
# lambda_max of [[g, c],[c, d]]
lm = (g + d) / 2 + (((g - d) / 2) ** 2 + c * c).sqrt()
mu = M - lm
print(f"tau*={ts} n={n} NQ={NQ}: M={M.str(8)} quad-err={qerr.str(3)} PD={ok} ({info}) gamma={gam:.10f} eps={eps.str(3)} eta={eta.str(3)}")
print(f"CERTIFIED: A[F] >= mu |F|^2 on constraints {KEYS} at T={Tn}, mu >= {mu.lower()}  (mu ball {mu.str(10)})")
