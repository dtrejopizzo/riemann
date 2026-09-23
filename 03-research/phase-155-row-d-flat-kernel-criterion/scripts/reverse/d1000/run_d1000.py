"""run_d1000.py NAME T [M] [NZ] [L] [BINF] [BETA]
LP over C^2 flat-top weights against a FINITE zero universe (default: first 1000 zeros).
Stage 1: LP on a delta=0.005 grid.  Stage 2: cutting planes against a localised fine scan.
Stage 3: certified interval minimum via the Taylor/Bernstein bound with a computed ||f''||_inf.
The LP never sees the primes.  DIAGNOSTIC.
"""
import numpy as np, json, sys, time
from scipy.optimize import linprog
import dlib as D

NAME = sys.argv[1]; T = float(sys.argv[2])
M    = int(sys.argv[3]) if len(sys.argv) > 3 else 24
NZ   = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
L    = float(sys.argv[5]) if len(sys.argv) > 5 else 60.0
BINF = float(sys.argv[6]) if len(sys.argv) > 6 else 3.0
BETA = int(sys.argv[7]) if len(sys.argv) > 7 else 0
TAUX = float(sys.argv[8]) if len(sys.argv) > 8 else 0.0   # override tau_max   # 1 = allow the two primitivity multipliers
DF = 1e-4
NCAND = 250; NREF = 51; ITMAX = 4
t00 = time.time()

win = D.Win(T, M=M)
DC = 0.005 if (TAUX if TAUX>0 else win.taumax) < 20 else 0.02
gam_all = D.R1.load_zeros(); gam = gam_all[:NZ]
Z  = D.Zfun(win.u, gam)
Phi = win.basis_matrix()
taumax = TAUX if TAUX > 0 else win.taumax
tau = np.arange(0.0, taumax+1e-12, DC)
t0 = time.time(); Arow = D.rows(win, Phi, Z, tau); t_rows = time.time()-t0
b0 = Arow[0]; Ay = Arow[1:5]; Ax = Arow[5:]
nY, nX = 4, Ax.shape[0]

def ghat(tt):
    tt = np.asarray(tt, float)
    xs, ws = np.polynomial.legendre.leggauss(600)
    u = T*(xs+1.0); wq = T*ws                       # [0,2T]
    C = np.cos(np.outer(u, tt))
    return np.vstack([2*(wq*np.cosh(u/2)) @ C, 2*(wq*u*np.sinh(u/2)) @ C])
Ag = ghat(tau) if BETA else np.zeros((2, len(tau)))
BCAP = 50.0

def solve(b0s, Ays, Axs, Ags):
    nS = nY+nX+2; n = 2*nS+1; nt = len(b0s)
    A = np.vstack([Ays, Axs, Ags])
    A_ub = np.zeros((nt+1, n)); b_ub = np.zeros(nt+1)
    A_ub[:nt, :nS] = -A.T; A_ub[:nt, nS:2*nS] = A.T; A_ub[:nt, -1] = 1.0
    b_ub[:nt] = b0s
    A_ub[nt, :2*nS] = 1.0; A_ub[nt, nY+nX:nS] = 0.0; A_ub[nt, nS+nY+nX:2*nS] = 0.0; b_ub[nt] = L
    Aeq = np.zeros((1, n)); Aeq[0, :nY] = 1.0; Aeq[0, nS:nS+nY] = -1.0
    per = [(0, None)]*nY + [(0, BINF)]*nX + [(0, BCAP)]*2
    bnds = per + per + [(None, None)]
    r = linprog(np.r_[np.zeros(2*nS), -1.0], A_ub=A_ub, b_ub=b_ub,
                A_eq=Aeq, b_eq=np.array([1.0]), bounds=bnds, method="highs")
    if not r.success: return None, None, None
    z = r.x[:nS]-r.x[nS:2*nS]
    return r.x[-1], z[:nY], z[nY:nY+nX], z[nY+nX:]

# ------------------------------------------------ cutting planes
Cb0, CAy, CAx, CAg = b0.copy(), Ay.copy(), Ax.copy(), Ag.copy()
Zenv = D.Zenvelope(win, gam)
hist = []
for it in range(ITMAX):
    c, y, x, bet = solve(Cb0, CAy, CAx, CAg)
    if c is None: print("infeasible"); sys.exit(1)
    _xs, _ws = np.polynomial.legendre.leggauss(400); _u = T*(_xs+1.0); _w = T*_ws
    G2 = np.array([2*np.sum(_w*_u**2*np.cosh(_u/2)), 2*np.sum(_w*_u**3*np.sinh(_u/2))])
    B2 = D.d2_bound(win, y, x, Zenv) + float(np.abs(bet) @ G2)
    f = b0 + y@Ay + x@Ax + bet@Ag
    # localise: any tau with f < thr has a coarse node with f <= thr + B2*DC^2/8
    pad = B2*DC*DC/8.0
    lo = np.r_[True, f[1:] <= f[:-1]] & np.r_[f[:-1] <= f[1:], True]
    thr = np.quantile(f, 0.02)
    ci = np.nonzero(lo & (f <= max(thr, c) + pad))[0]
    if len(ci) == 0: ci = np.argsort(f)[:50]
    ci = ci[np.argsort(f[ci])[:NCAND]]            # cap the localisation set
    cand = tau[ci]
    off = np.linspace(-DC/2, DC/2, NREF)
    fine = np.unique(np.clip((cand[:, None] + off[None, :]).ravel(), 0.0, taumax))
    Af = D.rows(win, Phi, Z, fine)
    Agf = ghat(fine) if BETA else np.zeros((2, len(fine)))
    ff = Af[0] + y@Af[1:5] + x@Af[5:] + bet@Agf
    padf = B2*(DC/(NREF-1))**2/8.0
    cert = float(ff.min() - padf)
    hist.append({"it": it, "c_lp": float(c), "f_coarse_min": float(f.min()),
                 "f_fine_min": float(ff.min()), "certified": cert,
                 "B2": B2, "n_fine": int(len(fine)), "ncut": int(len(cand))})
    print(f"  it{it}: c_lp={c:+.5e} coarse={f.min():+.5e} fine={ff.min():+.5e} "
          f"cert={cert:+.5e} B2={B2:.3e} nfine={len(fine)}", flush=True)
    if c - ff.min() < 1e-7 and it > 0: break
    sel = np.argsort(ff)[:min(400, len(fine))]
    Cb0 = np.r_[Cb0, Af[0][sel]]
    CAy = np.hstack([CAy, Af[1:5][:, sel]]); CAx = np.hstack([CAx, Af[5:][:, sel]])
    CAg = np.hstack([CAg, Agf[:, sel]])

# ------------------------------------------------ diagnostics of the optimum
ug = np.linspace(0, win.Umax, 4000); wg = win.w_of_u(ug, y, x)
mass = float(np.trapz(wg, ug)*2); amass = float(np.trapz(np.abs(wg), ug)*2)
out = {"name": NAME, "T": T, "M": M, "h": win.h, "J": win.J, "nzeros": NZ,
       "Gamma": float(gam[-1]), "A_T": win.A_T, "taumax": taumax, "taumax_env": win.taumax, "L": L,
       "BINF": BINF, "dc": DC, "df": DF, "ngrid": len(tau), "npan": win.npan,
       "nq": len(win.u), "Uspl": win.Uspl, "Umax": win.Umax,
       "svals": win.sv.tolist(), "y": y.tolist(), "x": x.tolist(), "beta": bet.tolist(), "BETA": BETA,
       "iters": hist, "c_lp": hist[-1]["c_lp"], "f_fine_min": hist[-1]["f_fine_min"],
       "certified": hist[-1]["certified"], "B2": hist[-1]["B2"],
       "int_w": mass, "int_abs_w": amass, "winf": float(np.abs(wg).max()),
       "l1_x": float(np.abs(x).sum()), "l1_y": float(np.abs(y).sum()),
       "t_rows": t_rows, "t_total": time.time()-t00}
json.dump(out, open(f"d_{NAME}.json", "w"))
print(f"{NAME}: c_lp={out['c_lp']:+.6e}  fine={out['f_fine_min']:+.6e}  "
      f"cert={out['certified']:+.6e}  int|w|={amass:.3f} |w|inf={out['winf']:.3f} "
      f"t={out['t_total']:.1f}s -> d_{NAME}.json")
