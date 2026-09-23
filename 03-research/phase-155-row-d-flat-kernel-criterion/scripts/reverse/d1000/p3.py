"""p3.py NAME T BETA -- R155_011 (P3): the BOUNDED-PROFILE class 0 <= w <= 1.
Same C^2 flat-top class (psi edge + cubic B-spline lattice h = 2T/24), same 1000-zero oracle,
but with the pointwise constraints 0 <= w(u) <= 1 for u > 2T on a fine u-grid.
Domain [0,60].  BETA=1: (beta_0-2, beta_1) free; BETA=0: beta = (2,0).
Stage 2 certifies on the dense delta = 0.005 tau-grid with the Bernstein pad B2*delta^2/8.
DIAGNOSTIC (the LP sees only zeros; the prime side is evaluated at the argmin).
"""
import numpy as np, json, sys, time
from scipy.optimize import linprog
import dlib as D, primeside as P

NAME = sys.argv[1]; T = float(sys.argv[2]); BETA = int(sys.argv[3])
TAUMAX = 60.0; DC = 0.02; NZ = 1000; L = 60.0; BINF = 3.0; BCAP = 50.0
t00 = time.time()
win = D.Win(T, M=24)
gam = D.R1.load_zeros()[:NZ]
Z = D.Zfun(win.u, gam); Phi = win.basis_matrix()
tau = np.arange(0.0, TAUMAX+1e-12, DC)
Arow = D.rows(win, Phi, Z, tau)
b0 = Arow[0]; Ay = Arow[1:5]; Ax = Arow[5:]
nY, nX = 4, Ax.shape[0]

def ghat(tt):
    tt = np.asarray(tt, float)
    xs, ws = np.polynomial.legendre.leggauss(600)
    u = T*(xs+1.0); wq = T*ws; C = np.cos(np.outer(u, tt))
    return np.vstack([2*(wq*np.cosh(u/2)) @ C, 2*(wq*u*np.sinh(u/2)) @ C])
Ag = ghat(tau) if BETA else np.zeros((2, len(tau)))

# ---- pointwise profile rows: w(u) = sum y_i psi_i(u) + sum x_j beta_j(u), u > 2T
ug = np.arange(2*T, win.Uspl+2*win.h, win.h/8.0)
Wrow = np.vstack([np.array([D.R2.psi_edge(np.maximum(ug-2*T, 0.0), s) for s in win.sv]),
                  np.array([D.R2.beta_spline((ug-uj)/win.h) for uj in win.ujs])])   # (nY+nX, nu)
nu_ = Wrow.shape[1]

def solve(b0s, Ays, Axs, Ags):
    nS = nY+nX+2; n = 2*nS+1; nt = len(b0s)
    A = np.vstack([Ays, Axs, Ags])
    nrow = nt + 1 + 2*nu_
    A_ub = np.zeros((nrow, n)); b_ub = np.zeros(nrow)
    A_ub[:nt, :nS] = -A.T; A_ub[:nt, nS:2*nS] = A.T; A_ub[:nt, -1] = 1.0
    b_ub[:nt] = b0s
    A_ub[nt, :2*nS] = 1.0; A_ub[nt, nY+nX:nS] = 0.0; A_ub[nt, nS+nY+nX:2*nS] = 0.0
    b_ub[nt] = L
    r0 = nt+1
    A_ub[r0:r0+nu_, :nY+nX] = Wrow.T; A_ub[r0:r0+nu_, nS:nS+nY+nX] = -Wrow.T; b_ub[r0:r0+nu_] = 1.0
    r1 = r0+nu_
    A_ub[r1:r1+nu_, :nY+nX] = -Wrow.T; A_ub[r1:r1+nu_, nS:nS+nY+nX] = Wrow.T; b_ub[r1:r1+nu_] = 0.0
    Aeq = np.zeros((1, n)); Aeq[0, :nY] = 1.0; Aeq[0, nS:nS+nY] = -1.0
    per = [(0, None)]*nY + [(0, BINF)]*nX + [(0, BCAP)]*2
    r = linprog(np.r_[np.zeros(2*nS), -1.0], A_ub=A_ub, b_ub=b_ub, A_eq=Aeq,
                b_eq=np.array([1.0]), bounds=per+per+[(None, None)], method="highs")
    if not r.success: return None, None, None, None
    z = r.x[:nS]-r.x[nS:2*nS]
    return r.x[-1], z[:nY], z[nY:nY+nX], z[nY+nX:]

Cb0, CAy, CAx, CAg = b0.copy(), Ay.copy(), Ax.copy(), Ag.copy()
Zenv = D.Zenvelope(win, gam); hist = []
for it in range(2):
    c, y, x, bet = solve(Cb0, CAy, CAx, CAg)
    if c is None: print("infeasible"); sys.exit(1)
    _xs, _ws = np.polynomial.legendre.leggauss(400); _u = T*(_xs+1.0); _w = T*_ws
    G2 = np.array([2*np.sum(_w*_u**2*np.cosh(_u/2)), 2*np.sum(_w*_u**3*np.sinh(_u/2))])
    B2 = D.d2_bound(win, y, x, Zenv) + float(np.abs(bet) @ G2)
    f = b0 + y@Ay + x@Ax + bet@Ag
    sel = np.argsort(f)[:300]
    fine = np.unique(np.clip((tau[sel][:, None]+np.linspace(-DC/2, DC/2, 21)[None, :]).ravel(), 0, TAUMAX))
    Af = D.rows(win, Phi, Z, fine); Agf = ghat(fine) if BETA else np.zeros((2, len(fine)))
    ff = Af[0] + y@Af[1:5] + x@Af[5:] + bet@Agf
    hist.append(dict(it=it, c_lp=float(c), f_coarse=float(f.min()), f_fine=float(ff.min()), B2=B2))
    print(f"  it{it} c_lp={c:+.5e} coarse={f.min():+.5e} fine={ff.min():+.5e} B2={B2:.3e}", flush=True)
    if c - ff.min() < 1e-7 and it > 0: break
    s2 = np.argsort(ff)[:400]
    Cb0 = np.r_[Cb0, Af[0][s2]]; CAy = np.hstack([CAy, Af[1:5][:, s2]])
    CAx = np.hstack([CAx, Af[5:][:, s2]]); CAg = np.hstack([CAg, Agf[:, s2]])

# certified: dense delta = 0.005 zero-side grid + Bernstein pad
d5 = np.arange(0.0, TAUMAX+1e-12, 0.005)
f5 = D.fvals(win, Z, y, x, d5) + (bet@ghat(d5) if BETA else 0.0)
pad = B2*0.005**2/8.0
amin = float(d5[np.argmin(f5)])
ns, lam = P.prime_table(win.Umax)
tp = np.array([amin])
fpr = float(P.f_prime(win, y, x, tp, ns, lam)[0] + (bet@ghat(tp))[0])
ugp = np.linspace(0, win.Umax, 8000); wgp = win.w_of_u(ugp, y, x)
out = dict(name=NAME, T=T, BETA=BETA, taumax=TAUMAX, c_lp=hist[-1]["c_lp"],
           min_zero_dense=float(f5.min()), argmin=amin, B2=B2, pad=pad,
           certified=float(f5.min()-pad), prime_at_argmin=fpr,
           beta=bet.tolist(), y=y.tolist(), x=x.tolist(),
           winf=float(np.abs(wgp).max()), wmin=float(wgp.min()),
           int_w=float(2*np.trapz(wgp, ugp)), int_abs_w=float(2*np.trapz(np.abs(wgp), ugp)),
           t=time.time()-t00)
print(json.dumps({k: v for k, v in out.items() if k not in ("y", "x")}))
json.dump(out, open(f"p3_{NAME}.json", "w"))
