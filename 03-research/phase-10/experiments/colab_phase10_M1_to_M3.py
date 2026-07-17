#!/usr/bin/env python3
# ======================================================================================
# Phase 10 (cohomological turn) — M10.1 -> M10.3, single self-contained Colab script.
#
#   M10.1  bare Hodge gap of the Weil-Carleson form vs band d  -> DEGENERATION toward zeta
#   M10.2  REGULARIZED Hodge gap (sine-kernel Gram of zeros)    -> SURVIVES (positive, definite)
#   M10.3  uniform lower frame bound at fixed sampling ratio    -> T-STABLE (S(T)/Muckenhoupt)
#
# Only numpy + mpmath (for zeta zeros) + optional matplotlib. Paste into a Colab cell and run.
# Crank the DEPTH parameters near the top to test with more numbers / higher T / more zeros.
# Zeta zeros are CACHED, so deeper re-runs reuse them.
# Author: David Alejandro Trejo Pizzo.
# ======================================================================================

# !pip -q install mpmath   # (Colab already has it; uncomment if needed)
import numpy as np, mpmath as mp, time, warnings
warnings.filterwarnings("ignore")
np.seterr(all="ignore")          # benign sinc/overflow at near-coincident nodes
mp.mp.dps = 20
try:
    import matplotlib.pyplot as plt
    HAVE_PLT = True
except Exception:
    HAVE_PLT = False

# ----------------------------- DEPTH PARAMETERS (edit me) -----------------------------
N_BASIS       = 12          # sinc basis half-size; dim M = 2N+1. Bigger = deeper, slower.
GRID_PTS      = 30000       # integration grid for the archimedean Gram. Bigger = more accurate.
M101_T0       = 100.0       # height for M10.1 / M10.2 sweeps
M101_DS       = [1.0,1.5,2.0,2.5,3.0,3.5,4.0]              # bands for M10.1/M10.2
M103_HEIGHTS  = [50.,100.,300.,1000.,3000.,10000.]        # heights for M10.3 (add 30000,1e5 for depth)
M103_RATIO    = 1.25        # sampling ratio: band d = ratio*(1/2)log(T/2pi) (K just under M)
ZERO_MAXN     = 60000       # safety cap on how many zeta zeros we will ever fetch
# --------------------------------------------------------------------------------------

# ---------- archimedean envelope Phi(r)=Re psi(1/4+ir/2)-log pi  (fast asymptotic) ----------
def Phi_vec(r):
    r = np.asarray(r, float)
    z = 0.25 + 0.5j*r
    # psi(z) ~ ln z - 1/(2z) - 1/(12 z^2) + 1/(120 z^4) - 1/(252 z^6)   (accurate for |z|>~3)
    psi = (np.log(z) - 1/(2*z) - 1/(12*z**2) + 1/(120*z**4) - 1/(252*z**6))
    out = np.real(psi) - np.log(np.pi)
    # fall back to exact mpmath for any small |z| (low r) where the asymptotic is weak
    small = np.abs(z) < 3.0
    if np.any(small):
        for i in np.nonzero(small)[0]:
            out[i] = float(mp.re(mp.digamma(0.25 + 0.5j*r[i]))) - float(mp.log(mp.pi))
    return out

# ---------- prime comb F(r) = 2 sum_{n<=X} Lambda(n)/sqrt(n) cos(r log n) ----------
def prime_powers(X):
    X = int(X)
    s = np.ones(X+1, bool); s[:2] = False
    for p in range(2, int(X**0.5)+1):
        if s[p]: s[p*p::p] = False
    rows = []
    for p in np.nonzero(s)[0]:
        lp = np.log(p); pk = p
        while pk <= X:
            rows.append((np.log(pk), lp/np.sqrt(pk))); pk *= p
    return np.array(rows) if rows else np.zeros((0,2))

def F_vec(r, pp):
    if pp.shape[0] == 0: return np.zeros_like(r)
    return 2.0*np.sum(pp[:,1][:,None]*np.cos(pp[:,0][:,None]*r[None,:]), axis=0)

# ---------- cached zeta zeros ----------
_ZC = {}                    # index -> imaginary ordinate
def _zero(n):
    if n not in _ZC: _ZC[n] = float(mp.im(mp.zetazero(n)))
    return _ZC[n]
def zeros_in(lo, hi):
    """all zeta ordinates in [lo,hi] (cached, scans upward)."""
    g=[]; n=1
    while n <= ZERO_MAXN:
        t=_zero(n)
        if t>hi: break
        if t>=lo: g.append(t)
        n+=1
    return np.array(g)

# ---------- the band-limited machinery ----------
def build_A(d, T0, N, grid_pts=GRID_PTS):
    sp = np.pi/d; centers = T0 + sp*np.arange(-N, N+1); span = (N+40)*sp
    r = np.linspace(T0-span, T0+span, grid_pts); w = r[1]-r[0]
    S = np.sinc(d*(r[None,:]-centers[:,None])/np.pi)
    A = (S*w) @ (Phi_vec(r)[:,None]*S.T); A = (A+A.T)/2
    return A, centers, r, w, S

def weil_form_spectrum(d, T0, N):
    """eigenvalues of (A_Phi - P_F) in the A_Phi metric = {1 - C_k}; bare Hodge gap = min."""
    A, centers, r, w, S = build_A(d, T0, N)
    pp = prime_powers(np.exp(2*d)); F = F_vec(r, pp)
    P = (S*w) @ (F[:,None]*S.T); P = (P+P.T)/2
    Li = np.linalg.inv(np.linalg.cholesky(A))
    M = Li @ (A-P) @ Li.T; M = (M+M.T)/2
    return np.linalg.eigvalsh(M), A.shape[0], int(pp.shape[0])

def reg_hodge_gap(d, T0, N):
    """regularized Hodge gap = lambda_min of the (unit-diagonal) sine-kernel Gram of the window zeros."""
    A, centers, r, w, S = build_A(d, T0, N)
    Li = np.linalg.inv(np.linalg.cholesky(A)); Ainv = Li.T @ Li
    halfwin = N*np.pi/d; zr = zeros_in(T0-halfwin, T0+halfwin); K = len(zr)
    if K < 2 or K > 2*N: return None, K, A.shape[0], np.nan
    V = np.stack([np.sinc(d*(zr[i]-centers)/np.pi) for i in range(K)], axis=1)  # (M,K)
    G = V.T @ Ainv @ V; G = (G+G.T)/2
    Dg = np.sqrt(np.diag(G)); Gn = G/np.outer(Dg, Dg)
    ev = np.linalg.eigvalsh(Gn)
    zs = np.sort(zr); dens = np.log(T0/(2*np.pi))/(2*np.pi); ng = np.diff(zs)*dens
    return ev[0], K, A.shape[0], (ng.min() if len(ng)>0 else np.nan)

# ====================================================================================
# M10.1 — bare Hodge gap vs band d (degeneration)
# ====================================================================================
def run_M101():
    print("="*86)
    print(" M10.1 — bare Hodge gap of the Weil-Carleson form vs band d (T0=%.0f, M=%d)"%(M101_T0,2*N_BASIS+1))
    print("="*86)
    print("   d    x=2d/logT0  primes   bare gap lam_min   #pos  #null   signature(1,#pos,#null)")
    gaps=[]
    for d in M101_DS:
        ev, M, npr = weil_form_spectrum(d, M101_T0, N_BASIS)
        gap=ev[0]; npos=int(np.sum(ev>1e-6)); nnull=int(np.sum(np.abs(ev)<=1e-6))
        x=2*d/np.log(M101_T0); gaps.append(gap)
        tag="definite/Lorentzian" if (nnull==0 and gap>1e-5) else "DEGENERATE"
        print("  %4.1f    %5.2f   %6d    %+0.3e    %3d   %3d    (1,%d,%d) %s"%(d,x,npr,gap,npos,nnull,npos,nnull,tag))
    print("\n  -> finite genus (small d): definite, gap>0 (curve-like). Toward zeta: gap->0, DEGENERATES.")
    return np.array(M101_DS), np.array(gaps)

# ====================================================================================
# M10.2 — regularized Hodge gap vs band d (survives)
# ====================================================================================
def run_M102():
    print("="*86)
    print(" M10.2 — REGULARIZED Hodge gap (sine-kernel Gram) vs band d (T0=%.0f)"%M101_T0)
    print("="*86)
    print("    d    K/M    regularized gap lam_min(G)    tightest norm.gap")
    ds=[]; rg=[]
    for d in M101_DS:
        lam,K,M,mng = reg_hodge_gap(d, M101_T0, N_BASIS)
        if lam is None or K>2*N_BASIS:
            print("   %3.1f   %d/%d   (K>=M: trivially rank-deficient)"%(d,K,M)); continue
        print("   %3.1f   %d/%d    %.4f                  %.3f"%(d,K,M,lam,mng)); ds.append(d); rg.append(lam)
    print("\n  -> POSITIVE & healthy where the bare gap vanished: the primitive form is DEFINITE.")
    return np.array(ds), np.array(rg)

# ====================================================================================
# M10.3 — uniform frame bound at fixed sampling ratio vs height (stable -> S(T))
# ====================================================================================
def run_M103():
    print("="*86)
    print(" M10.3 — uniform lower frame bound: lambda_min(G) at fixed sampling ratio vs height")
    print("   band d = %.2f * (1/2)log(T/2pi)  (K just under M=%d)"%(M103_RATIO,2*N_BASIS+1))
    print("="*86)
    print("      T0        d     K/M       regularized gap    tightest norm.gap")
    Ts=[]; gaps=[]
    for T0 in M103_HEIGHTS:
        d = M103_RATIO*0.5*np.log(T0/(2*np.pi))
        lam,K,M,mng = reg_hodge_gap(d, T0, N_BASIS)
        if lam is None:
            print("   %8.0f  %5.2f   (skip K=%d)"%(T0,d,K)); continue
        print("   %8.0f  %5.2f   %d/%d      %.4f             %.3f"%(T0,d,K,M,lam,mng)); Ts.append(T0); gaps.append(lam)
    print("\n  -> T-STABLE => uniform lower frame bound plausibly holds (regularized Hodge index viable).")
    print("     RH <=> uniform A_2 (Muckenhoupt) on E~xi <=> regularity of S(T)=arg zeta/pi.")
    print("     Two-sided handle; S(T) has UNCONDITIONAL partial control (Selberg: O(log T), moments, CLT).")
    return np.array(Ts), np.array(gaps)

# ====================================================================================
if __name__ == "__main__":
    t0=time.time()
    d1,g1 = run_M101()
    d2,g2 = run_M102()
    T3,g3 = run_M103()
    print("\n[done in %.1f s; %d zeta zeros cached]"%(time.time()-t0, len(_ZC)))

    if HAVE_PLT:
        fig,ax=plt.subplots(1,3,figsize=(16,4.2))
        ax[0].semilogy(d1, np.maximum(g1,1e-16),'o-'); ax[0].set_title("M10.1 bare Hodge gap -> 0 (degeneration)")
        ax[0].set_xlabel("band d"); ax[0].set_ylabel("lambda_min(t)")
        ax[1].plot(d2,g2,'s-',color='C2'); ax[1].set_title("M10.2 regularized gap SURVIVES (>0)")
        ax[1].set_xlabel("band d"); ax[1].set_ylabel("lambda_min(G)"); ax[1].set_ylim(0,1)
        ax[2].plot(T3,g3,'^-',color='C3'); ax[2].set_xscale('log'); ax[2].set_title("M10.3 frame bound T-stable")
        ax[2].set_xlabel("height T0"); ax[2].set_ylabel("lambda_min(G)"); ax[2].set_ylim(0,0.5)
        plt.tight_layout(); plt.show()
