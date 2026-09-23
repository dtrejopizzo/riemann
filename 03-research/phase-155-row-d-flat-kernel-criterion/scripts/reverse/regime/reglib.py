"""reglib.py -- phase 155, R155.008 "regime law over 100 windows".

Fixed C^2 flat-top class, comparable across every window T:

    w = 1 on [-2T,2T];  for u > 2T (even extension)
        w(u) = sum_i y_i psi_{s_i}(u-2T) + sum_{j=2..J+1} x_j beta((u-u_j)/h),
        psi_s(v) = (1+sv+s^2v^2/2)e^{-sv},  s in {2.5,4,8,16},  sum_i y_i = 1,
        beta = cardinal cubic B-spline (C^2, support 2h),  u_j = 2T + j*h.

h and J are FIXED (not M = 2T/h), so the admissible set is literally the same
shape family at every T; only the edge position 2T moves.  This answers the
hostile-audit point (R155_006 SS5) that a coefficient budget over an M-dependent
lattice is not comparable across windows: here the lattice is T-independent and
we additionally report the true norms ||w||_inf and int|w|.

Everything here is DIAGNOSTIC (double precision, finite tau-grid, truncated zero
table, LP trained on a table of zeros -> circular as a tool,
phase-4-handoff/proofs/00-PROOF-LOG.md:168, phase-136 MAP_1 ES-2).
"""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
PAR = os.path.dirname(HERE)
sys.path.insert(0, PAR)
import revlib as R1, revlib2 as R2, lp2                      # noqa: E402
from revlib import m_of_tau, Ktail_box, cosh_box, vonmangoldt_table  # noqa: E402

JOFF = 2                      # first spline node index (support starts at 2T)
SVALS = np.array([2.5, 4.0, 8.0, 16.0])

# ------------------------------------------------------------------ class
class Win:
    def __init__(self, T, h=0.25, J=30):
        self.T, self.h, self.J = T, h, J
        self.ujs = 2*T + h*np.arange(JOFF, JOFF+J)
        self.U = float(self.ujs[-1] + 2*h)        # sup supp w  (exponential type)
        self.sv = SVALS

# ------------------------------------------------------------------ zero side
def zero_side(tau, W, gam, chunk=256):
    """Bz,Ay,Ax : the zero-side sums sum_{|g|<=Gcut} what_col(tau -/+ g).
    Identical output to revlib2.zero_side (agreement 7e-10), ~1.4x faster:
    exp(2iTd) is reused from cos/sin(2Td) and sinc^4 from cos(hd) via
    sin^2(hd/2) = (1-cos hd)/2."""
    T, h, sv, ujs = W.T, W.h, W.sv, W.ujs
    tau = np.asarray(tau, float); nT = len(tau); J = len(ujs); nS = len(sv)
    Bz = np.zeros(nT); Ay = np.zeros((nS, nT)); Ax = np.zeros((J, nT))
    for a in range(0, len(gam), chunk):
        g = gam[a:a+chunk]
        for sgn in (-1.0, 1.0):
            d = tau[None, :] + sgn*g[:, None]
            c2 = np.cos(2*T*d); s2 = np.sin(2*T*d)
            ct = np.cos(h*d);   st = np.sin(h*d)
            with np.errstate(divide='ignore', invalid='ignore'):
                bb = 2.0*s2/d
                q = h*d/2
                P = 2*h*((1-ct)/2)**2/q**4
            bad = np.abs(d) < 1e-9
            bb[bad] = 4.0*T; P[bad] = 2*h
            Bz += bb.sum(0)
            for k in range(nS):                    # psi columns
                s = sv[k]; den = s*s + d*d
                A = s/den; B = d/den               # 1/(s-id) = A + iB
                rA = 1 + s*A + s*s*(A*A-B*B); rB = s*B + s*s*(2*A*B)
                Ay[k] += 2*(c2*(A*rA-B*rB) - s2*(A*rB+B*rA)).sum(0)
            Cm = c2*P                              # j=0
            Cc = (c2*ct - s2*st)*P                 # j=1
            ct2 = 2*ct
            for j in range(0, JOFF+J):
                if j == 0: cur = Cm
                elif j == 1: cur = Cc
                else:
                    cur = ct2*Cc; cur -= Cm; Cm = Cc; Cc = cur
                k = j - JOFF
                if 0 <= k < J: Ax[k] += cur.sum(0)
    return Bz, Ay, Ax

# ------------------------------------------------------------------ profile
def profile(W, y, x, v):
    """w(2T+v) for v >= 0."""
    v = np.asarray(v, float)
    out = np.zeros_like(v)
    for i, s in enumerate(W.sv): out += y[i]*R2.psi_edge(v, s)
    for k, uj in enumerate(W.ujs): out += x[k]*R2.beta_spline((v + 2*W.T - uj)/W.h)
    return out

def shape_stats(W, y, x, nv=4001):
    v = np.linspace(0.0, W.U - 2*W.T, nv)
    w = profile(W, y, x, v)
    mass = float(np.trapz(w, v)); absm = float(np.trapz(np.abs(w), v))
    winf = float(np.max(np.abs(w)))
    # shoulder decay rate: least-squares slope of log|w| over the first unit
    # where |w| >= 0.05 (a robust single number for the "edge function")
    m = (v <= 2.0) & (np.abs(w) >= 0.05)
    rate = float(-np.polyfit(v[m], np.log(np.abs(w[m])), 1)[0]) if m.sum() > 5 else float('nan')
    half = float(v[np.argmax(np.abs(w) < 0.5)]) if np.any(np.abs(w) < 0.5) else float('nan')
    cen = float(np.trapz(np.abs(w)*v, v)/max(absm, 1e-30))
    last = float(W.ujs[np.max(np.nonzero(np.abs(x) > 1e-3)[0])] - 2*W.T) if np.any(np.abs(x) > 1e-3) else 0.0
    sg = np.sign(x); nsw = int(np.sum(sg[:-1]*sg[1:] < 0))
    return dict(mass=mass, absmass=absm, winf=winf, rate=rate, half=half,
                centroid=cen, last_node=last, sign_changes=nsw)

# ------------------------------------------------------------------ certification
def bernstein_slack(U, finf, delta):
    """min_R f >= min_grid f - (1/2) U^2 ||f||_inf delta^2  for f of exp type U
    (Bernstein: ||f''||_inf <= U^2||f||_inf; Taylor at a grid-adjacent minimum)."""
    return 0.5*U*U*finf*delta*delta

def refine_min(W, gam, tau, f, dfine=0.005, dcoarse=0.02, kmax=250):
    """Fine-grid certification of min f.  Refines, at step dfine, every coarse
    interval whose endpoints lie within the coarse Bernstein slack of the coarse
    minimum; outside those intervals the coarse bound already exceeds the
    reported value, so the returned number is the honest grid minimum."""
    finf = float(np.max(np.abs(f)))*1.05
    slack_c = bernstein_slack(W.U, finf, dcoarse)
    lo = f.min()
    idx = np.nonzero(f <= lo + slack_c)[0]
    nband = len(idx)
    if nband == 0: idx = np.array([int(np.argmin(f))])
    elif nband > kmax: idx = idx[np.argsort(f[idx])[:kmax]]
    pts = []
    for i in idx:
        a = tau[max(i-1, 0)]; b = tau[min(i+1, len(tau)-1)]
        pts.append(np.arange(a, b + 1e-12, dfine))
    tp = np.unique(np.concatenate(pts))
    return tp, finf, slack_c, int(nband)

# ------------------------------------------------------------------ prime side
def f_prime_side(tau, W, y, x, ns, lam, gl_n=800):
    """Theorem Z (7.2), prime/Gamma side.  Gauss-Legendre order 800 on the
    B-spline integrals (hostile-audit repair R155_006 SS3: order 200 gave a
    7e-5 artefact)."""
    T, h, sv, ujs = W.T, W.h, W.sv, W.ujs
    tau = np.asarray(tau, float); logn = np.log(ns)
    Kt = Ktail_box(tau, T) \
        - sum(y[i]*R2.Ktail_psi(tau, T, sv[i]) for i in range(len(sv))) \
        - sum(x[k]*R2.Ktail_bspline(tau, T, ujs[k], h, n=gl_n) for k in range(len(ujs)))
    ch = cosh_box(tau, T) \
        + sum(y[i]*R2.cosh_psi(tau, T, sv[i]) for i in range(len(sv))) \
        + sum(x[k]*R2.cosh_bspline(tau, T, ujs[k], h, n=gl_n) for k in range(len(ujs)))
    wn = R2.w_of_logn(logn, T, sv, y, ujs, h, x)
    coef = 2*lam/np.sqrt(ns)*wn
    nz = np.abs(coef) > 0
    pr = -(coef[nz] @ np.cos(np.outer(logn[nz], tau)))
    return m_of_tau(tau) + Kt + pr + ch

# ------------------------------------------------------------------ bookkeeping
_PP = None
def prime_powers(N=4000):
    global _PP
    if _PP is None or _PP[0] < N: _PP = (N,) + vonmangoldt_table(N)
    return _PP[1], _PP[2]

def A_of_T(T):
    ns, lam = prime_powers(4000)
    m = np.log(ns) < 2*T - 1e-12
    return float(np.sum(2*lam[m]/np.sqrt(ns[m])))

def N_of_T(T):
    ns, lam = prime_powers(4000)
    return [int(n) for n in ns[np.log(ns) < 2*T - 1e-12]]

ENTRIES = {3: 0.5*np.log(3), 4: np.log(2), 5: 0.5*np.log(5), 7: 0.5*np.log(7),
           8: 1.5*np.log(2), 9: np.log(3), 11: 0.5*np.log(11)}

_ZER = None
def zeros(Gcut):
    global _ZER
    if _ZER is None: _ZER = R1.load_zeros()
    return _ZER[_ZER <= Gcut]
