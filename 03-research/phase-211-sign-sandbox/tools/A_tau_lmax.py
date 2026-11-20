"""lambda_max(A_tau) on L^2[-T,T] by direct discretisation (phase 211, ROUND_013_B).  NUMERICAL tool.

A_tau f (x) = (1/2) sum_{n<N} v_n cos(tau log n) [f(x+log n) + f(x-log n)],  x in [-T,T], f extended by 0
outside [-T,T], N = e^{2T}, v_n = 2 Lambda(n)/sqrt(n).  m(tau) = Re psi(1/4+i tau/2) - log pi.

Discretisation (Galerkin, sine basis): e_k(x) = sin(k*pi*(x+T)/(2T))/sqrt(T), k=1..Nb, the standard
orthonormal half-range sine basis of L^2[-T,T] (0 continued outside [-T,T]; same basis as
tools/galerkin_mp.py).  For this basis the shift-and-restrict operator (Sh(s)f)(x) = f(x+s)*1_{[-T,T]}(x)
(f continued by 0 outside [-T,T]) has an EXACT closed-form matrix element
  <e_j, Sh(s) e_k> = (1/2T) [ I(a_j-a_k, (a_j-a_k)T - a_k s) - I(a_j+a_k, (a_j+a_k)T + a_k s) ],
  I(c,d) = (sin(cU+d)-sin(cL+d))/c  (or (U-L)cos(d) if c=0),  a_j = j*pi/(2T),
  L = max(-T,-T-s), U = min(T,T-s)  (from sin A sin B = 1/2[cos(A-B)-cos(A+B)] integrated over the
overlap [L,U] of the two translated supports).  Sh(s)* = Sh(-s) exactly, so A_tau = (1/2) sum_n v_n
cos(tau log n) (Sh(log n)+Sh(-log n)) is exactly self-adjoint and its Galerkin matrix in e_1..e_Nb is
exactly symmetric (no ad hoc symmetrisation, no grid/aliasing artifact).  By Rayleigh-Ritz the Galerkin
lambda_max(Nb) is a lower bound for the true lambda_max(A_tau) on L^2[-T,T], increasing monotonically
to it as Nb -> infinity; convergence is checked by comparing Nb and ~1.5*Nb.  This is a numerical
approximation only; it proves nothing about (1.2) or lambda_A(T).
"""
import math, sys
import numpy as np
from scipy.special import psi
from scipy.optimize import minimize_scalar

def m_sym(t):
    t = np.asarray(t, dtype=float)
    return psi(0.25 + 0.5j * t).real - math.log(math.pi)

def comb(T, scale=1.0):
    """[(n, p, v_n)] over prime powers n < e^{2T}; scale multiplies every v_n (falsifier (a))."""
    N = math.exp(2 * T); out = []
    for n in range(2, int(N) + 1):
        if math.log(n) >= 2 * T: break
        p = None
        for q in range(2, int(math.isqrt(n)) + 1):
            if n % q == 0: p = q; break
        if p is None: p = n
        k = n
        while k % p == 0: k //= p
        if k == 1: out.append((n, p, scale * 2 * math.log(p) / math.sqrt(n)))
    return out

def _I(c, d, L, U):
    """int_L^U cos(c*x+d) dx, vectorised over c,d (scalars L,U)."""
    c = np.asarray(c, dtype=float); d = np.asarray(d, dtype=float)
    out = np.where(c == 0, (U - L) * np.cos(d), 0.0)
    nz = c != 0
    cs = np.where(nz, c, 1.0)
    out = np.where(nz, (np.sin(cs * U + d) - np.sin(cs * L + d)) / cs, out)
    return out

def _shift_matrix(s, T, Nb):
    """Exact Nb x Nb Galerkin matrix <e_j, Sh(s) e_k> in the sine basis e_k, k=1..Nb."""
    j = np.arange(1, Nb + 1)[:, None]
    k = np.arange(1, Nb + 1)[None, :]
    a_j = j * math.pi / (2 * T)
    a_k = k * math.pi / (2 * T)
    L = max(-T, -T - s); U = min(T, T - s)
    if L >= U:
        return np.zeros((Nb, Nb))
    c1 = a_j - a_k; d1 = (a_j - a_k) * T - a_k * s
    c2 = a_j + a_k; d2 = (a_j + a_k) * T + a_k * s
    return (_I(c1, d1, L, U) - _I(c2, d2, L, U)) / (2 * T)

class ATau:
    def __init__(self, T, Nb, scale=1.0):
        self.T = T; self.Nb = Nb
        C = comb(T, scale)
        self.ln = np.array([math.log(n) for n, _, _ in C])
        self.v = np.array([v for _, _, v in C])
        self.Spm = [_shift_matrix(ln, T, Nb) + _shift_matrix(-ln, T, Nb) for ln in self.ln]

    def matrix(self, tau):
        c = self.v * np.cos(tau * self.ln)
        A = np.zeros((self.Nb, self.Nb))
        for ci, S in zip(c, self.Spm):
            if ci != 0.0:
                A += ci * S
        return 0.5 * A

    def lambda_max(self, tau):
        A = self.matrix(tau)
        A = 0.5 * (A + A.T)  # removes floating-point asymmetry only (exact in theory)
        return float(np.linalg.eigvalsh(A)[-1])

    def lambda_max_vec(self, tau):
        A = self.matrix(tau)
        A = 0.5 * (A + A.T)
        w, V = np.linalg.eigh(A)
        coeffs = V[:, -1]
        # reconstruct eigenvector values on a plotting grid from the sine-basis coefficients
        xs = np.linspace(-T if False else -self.T, self.T, 801)
        k = np.arange(1, self.Nb + 1)
        basis = np.sin(np.outer(xs + self.T, k) * math.pi / (2 * self.T)) / math.sqrt(self.T)
        vec = basis @ coeffs
        return float(w[-1]), vec, xs

def scan(T, M=500, delta=0.1, rfac=3.0, fine_frac=0.15, fine_cap=1500, coarse_pts=400,
         refine_frac=0.02, scale=1.0, top=12):
    """Two-region scan: a fine region [lo, lo+fine_frac*(hi-lo)] at step <= 1/(10T) (capped at
    fine_cap points, so the achieved step may exceed 1/(10T) for large T; reported honestly as
    fine_step), where every prior round (011C/012A) locates the minimiser, plus a coarse pass
    (coarse_pts points) over the whole range [lo,hi] to check for a deeper minimum elsewhere."""
    N = math.exp(2 * T)
    lo = 2 * math.pi * N * (1 + delta)
    hi = 2 * math.pi * N * rfac
    op = ATau(T, M, scale)
    target_step = 1 / (10 * T)
    fine_hi = lo + fine_frac * (hi - lo)
    n_fine = min(fine_cap, max(50, int((fine_hi - lo) / target_step) + 1))
    ts_fine = np.linspace(lo, fine_hi, n_fine)
    ts_coarse = np.linspace(lo, hi, coarse_pts)
    ts = np.unique(np.concatenate([ts_fine, ts_coarse]))
    margins = np.array([m_sym(t) - op.lambda_max(t) for t in ts])
    order = np.argsort(margins)[:top]
    fine_step = ts_fine[1] - ts_fine[0] if n_fine > 1 else float('nan')
    best = []
    win = 3 * target_step  # local polish only: the function oscillates on scale ~ a few target_step,
    # so a window wider than that can let bounded Brent drift to a different, unrelated local min
    for idx in order:
        t0 = ts[idx]
        a, b = max(lo, t0 - win), min(hi, t0 + win)
        r = minimize_scalar(lambda t: m_sym(t) - op.lambda_max(t), bounds=(a, b), method='bounded',
                             options={'xatol': 1e-6})
        best.append((r.fun, r.x))
    best.sort()
    margin_min, tau_min = best[0]
    lam, vec, xs = op.lambda_max_vec(tau_min)
    return dict(T=T, Nb=M, N=N, lo=lo, hi=hi, fine_step=fine_step, target_step=target_step,
                coarse_step=(ts_coarse[1] - ts_coarse[0]) if coarse_pts > 1 else float('nan'),
                margin_min=margin_min, tau_min=tau_min, lambda_max=lam, m_at=float(m_sym(tau_min)),
                eigvec=vec, xs=xs)

if __name__ == '__main__':
    args = sys.argv[1:]
    T = float(args[0]) if args else 1.0
    M = int(args[1]) if len(args) > 1 else 500
    scale = float(args[2]) if len(args) > 2 else 1.0
    r = scan(T, M=M, scale=scale)
    print(f"T={T} M={M} scale={scale} lo={r['lo']:.4g} hi={r['hi']:.4g} fine_step={r['fine_step']:.4g} "
          f"coarse_step={r['coarse_step']:.4g} target_step={r['target_step']:.4g} "
          f"tau_min={r['tau_min']:.6g} lambda_max={r['lambda_max']:.6g} "
          f"m={r['m_at']:.6g} margin={r['margin_min']:.6g}")
