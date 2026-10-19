"""lp.py NAME T U M BETA [TAUMAX] -- R155_016: the comb-vanishing LP.

Class: compactly supported C^2 flat-top spline weights (comblib.WinC),
       w = 1 on [-2T,2T], supp w subset [-U,U], lattice h = 2T/M.
Equalities: w(log n) = 0 for every prime power n with 2T < log n <= U (Cor D.2).
Objective: maximise min_tau f_w(tau) on [0, TAUMAX], TAUMAX >= tau_stop(w).
BETA=1: (beta_0-2, beta_1) free; BETA=0: beta = (2,0).

The equalities are eliminated exactly: x = x_p + N z with A x_p = b, N = null(A).
LP variables: z (dim = nullity), |x| bounds via t_i, and the level c.
Zero side is the oracle (1000 zeros); the prime side is evaluated at the argmin.
DIAGNOSTIC.
"""
import numpy as np, json, sys, time
from scipy.optimize import linprog
import comblib as C

NAME = sys.argv[1]; T = float(sys.argv[2]); U = float(sys.argv[3])
M = int(sys.argv[4]); BETA = int(sys.argv[5])
TAUMAX = float(sys.argv[6]) if len(sys.argv) > 6 else 220.0
DC = 0.02; NZ = 1000; BINF = 3.0; L1 = 60.0; BCAP = 50.0
NOCOMB = len(sys.argv) > 7 and sys.argv[7] == "nocomb"
t00 = time.time()

win = C.WinC(T, U, M=M, Umaxpad=0.5)
gam = C.R1.load_zeros()[:NZ]
ns, lam = C.P.prime_table(win.Umax)
ln, vn = win.comb_nodes(ns, lam)

# ---- eliminate the comb equalities
A = win.spl(ln).T                       # (m, nX)
b = -win.base(ln)
m, nX = A.shape
if NOCOMB:
    xp = np.zeros(nX); N = np.eye(nX); rk = 0
else:
    xp, *_ = np.linalg.lstsq(A, b, rcond=None)
    Uu, sv, Vt = np.linalg.svd(A)
    rk = int((sv > 1e-9 * sv[0]).sum()) if len(sv) else 0
    N = Vt[rk:].T                       # (nX, nullity)
nz = N.shape[1]
resid = float(np.abs(A @ xp - b).max()) if m else 0.0
print(f"# {NAME}: m={m} nX={nX} rank={rk} nullity={nz} resid={resid:.2e} "
      f"U_true={win.U:.4f} h={win.h:.5f}", flush=True)

# ---- zero-side rows for the effective basis [base + xp-part, N-directions]
Z = C.Zfun(win.u, gam)
Sp = win.spl(win.u)                                    # (nX, nq)
Phi = np.vstack([(win.base(win.u) + xp @ Sp)[None, :], (N.T @ Sp)])
tau = np.arange(0.0, TAUMAX + 1e-12, DC)
Arow = C.rows(win, Phi, Z, tau)
b0 = Arow[0]; Az = Arow[1:]
Ag = C.ghat(T, tau) if BETA else np.zeros((2, len(tau)))
print(f"# rows done {time.time()-t00:.1f}s", flush=True)


def solve(b0s, Azs, Ags):
    """vars: z (nz, free), t (nX >= |x-xp part|), bet(2 split), c."""
    nb = 2 if BETA else 0
    n = nz + nX + nb + 1
    ic, it0, ib0 = n - 1, nz, nz + nX
    nt = len(b0s)
    rows_ = []
    bub = []
    # f(tau) >= c  ->  c - Az^T z - Ag^T bet <= b0
    R = np.zeros((nt, n)); R[:, :nz] = -Azs.T
    if BETA: R[:, ib0:ib0 + 2] = -Ags.T
    R[:, ic] = 1.0
    rows_.append(R); bub.append(b0s)
    # |x_i| <= t_i , x = xp + N z
    for sgn in (1.0, -1.0):
        R = np.zeros((nX, n)); R[:, :nz] = sgn * N; R[:, it0:it0 + nX] = -np.eye(nX)
        rows_.append(R); bub.append(-sgn * xp)
    # t_i <= BINF ; sum t_i <= L1
    R = np.zeros((1, n)); R[0, it0:it0 + nX] = 1.0
    rows_.append(R); bub.append(np.array([L1]))
    A_ub = np.vstack(rows_); b_ub = np.concatenate(bub)
    cvec = np.zeros(n); cvec[ic] = -1.0
    bnds = [(None, None)] * nz + [(0, BINF)] * nX + [(-BCAP, BCAP)] * nb + [(None, None)]
    r = linprog(cvec, A_ub=A_ub, b_ub=b_ub, bounds=bnds, method="highs")
    if not r.success:
        return None, None, None
    z = r.x[:nz]; bet = r.x[ib0:ib0 + 2] if BETA else np.zeros(2)
    return r.x[ic], z, bet


Cb0, CAz, CAg = b0.copy(), Az.copy(), Ag.copy()
Zenv = C.Zenvelope(win, gam)
hist = []
y = None
for it in range(3):
    c, z, bet = solve(Cb0, CAz, CAg)
    if c is None:
        print(json.dumps(dict(name=NAME, status="infeasible"))); sys.exit(1)
    x = xp + N @ z
    f = b0 + z @ Az + bet @ Ag
    sel = np.argsort(f)[:400]
    fine = np.unique(np.clip((tau[sel][:, None] + np.linspace(-DC / 2, DC / 2, 21)[None, :]).ravel(),
                             0, TAUMAX))
    Af = C.rows(win, Phi, Z, fine)
    Agf = C.ghat(T, fine) if BETA else np.zeros((2, len(fine)))
    ff = Af[0] + z @ Af[1:] + bet @ Agf
    hist.append(dict(it=it, c_lp=float(c), coarse=float(f.min()), fine=float(ff.min())))
    print(f"  it{it} c_lp={c:+.6e} coarse={f.min():+.6e} fine={ff.min():+.6e} "
          f"({time.time()-t00:.0f}s)", flush=True)
    if c - ff.min() < 1e-7 and it > 0:
        break
    s2 = np.argsort(ff)[:500]
    Cb0 = np.r_[Cb0, Af[0][s2]]; CAz = np.hstack([CAz, Af[1:][:, s2]])
    CAg = np.hstack([CAg, Agf[:, s2]])

# ---- Theorem D constants for the resulting w
D_K, D_c, Dtot, tau_stop, Lfun = C.Dw_and_taustop(win, x, bet)
tail_at_stop = float(Lfun(TAUMAX))

# ---- certified grid value (zero side dense) + Bernstein pad
_xs, _ws = np.polynomial.legendre.leggauss(400); _u = T * (_xs + 1.0); _w = T * _ws
G2 = np.array([2 * np.sum(_w * _u**2 * np.cosh(_u / 2)), 2 * np.sum(_w * _u**3 * np.sinh(_u / 2))])
B2 = C.d2_bound(win, x, Zenv) + float(np.abs(bet) @ G2)
d5 = np.arange(0.0, TAUMAX + 1e-12, 0.005)
f5 = C.fvals(win, Z, x, d5) + (bet @ C.ghat(T, d5) if BETA else 0.0)
amin = float(d5[np.argmin(f5)])
pad = B2 * 0.005**2 / 8.0

# ---- prime side at the argmin and on a coarse sweep
tsw = np.unique(np.r_[np.array([amin]), d5[np.argsort(f5)[:200]]])
fprs = C.f_prime(win, x, tsw, ns, lam) + (bet @ C.ghat(T, tsw) if BETA else 0.0)
fpr = float(fprs[0]); fpr_min = float(fprs.min())
fz_at = float(f5[np.argmin(f5)])
ugp = np.linspace(0, win.Umax, 8000); wgp = win.w_of_u(ugp, x)
out = dict(name=NAME, T=T, U=float(win.U), M=M, h=float(win.h), BETA=BETA, nocomb=NOCOMB,
           taumax=TAUMAX, m_eq=m, nX=nX, rank=rk, nullity=nz, resid=resid,
           c_lp=hist[-1]["c_lp"], min_zero_fine=hist[-1]["fine"],
           min_zero_dense=float(f5.min()), argmin=amin, B2=B2, pad=pad,
           certified=float(f5.min() - pad), prime_at_argmin=fpr, prime_min_sweep=fpr_min,
           zero_prime_gap=abs(fpr - fz_at), beta=bet.tolist(),
           D_K=D_K, D_cosh=D_c, D=Dtot, tau_stop=tau_stop, L_at_taumax=tail_at_stop,
           E_at_max=float(vn.sum()),
           winf=float(np.abs(wgp).max()), int_abs_w=float(2 * np.trapz(np.abs(wgp), ugp)),
           x=x.tolist(), t=time.time() - t00)
print(json.dumps({k: v for k, v in out.items() if k != "x"}))
json.dump(out, open(f"lp_{NAME}.json", "w"))
