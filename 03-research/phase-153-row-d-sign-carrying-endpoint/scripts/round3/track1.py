"""TRACK 1 (P153.5): single off-line pair 1/2 +- a +- i g0 for zeta itself.

Form of record (Paper 42 eq:evalcoords, restricted to P_T):
    <A_T F,F> = sum_rho Fhat(rho) Fhat(1-rho),   Fhat(s) = int F(t) e^{(s-1/2)t} dt.
On-line rho = 1/2+i gamma gives |Fhat|^2.  An off-line quadruple 1/2 +- a +- i g0
gives  4 Re X,  X = Fhat(1/2+a+i g0) * conj Fhat(1/2-a+i g0).

Conditional criterion (Theorem T1.3): if zeta has that quadruple and every OTHER
zero on the line, then for every real F in P_T
        4 Re X(F)  <=  <A_T F,F>.
Q_T := A_T - C(a,g0)  must be >= 0 on P_T.   T*(a,g0) = inf{T : lmin(Q_T) < 0}.

Mesh-free spectral assembly (sine basis on (-T,T)), reusing scripts/audit/aud_spectral.py
conventions: basis_hat, moments (moments(T,K,[b]) = int phi_k e^{b t} dt exactly).
"""
import math, numpy as np, scipy.linalg as sla
from scipy.special import psi as digamma
from numpy.polynomial.legendre import leggauss

LAM = {2: math.log(2), 3: math.log(3), 4: math.log(2), 5: math.log(5),
       7: math.log(7), 8: math.log(2), 9: math.log(3), 11: math.log(11),
       13: math.log(13), 16: math.log(2), 25: math.log(5), 27: math.log(3)}

def basis_hat(T, K, tau):
    L = 2*T
    b = np.array([k*math.pi/L for k in range(1, K+1)])
    tau = np.asarray(tau, dtype=float)
    den = b[:, None]**2 - tau[None, :]**2
    sgn = np.array([(-1)**k for k in range(1, K+1)])[:, None]
    num = b[:, None]*(1 - sgn*np.exp(-1j*tau[None, :]*L))
    small = np.abs(den) < 1e-9
    out = np.where(small, 0.0+0.0j, num/np.where(small, 1.0, den))
    for i in range(K):
        m = small[i]
        if m.any():
            t0 = tau[m]
            out[i, m] = (-1j*L*(-1)**(i+1)*np.exp(-1j*t0*L)*b[i])/(2*b[i])
    return np.exp(1j*tau[None, :]*T)*out

def moments(T, K, betas):
    """rows r[j,k] = int_{-T}^{T} phi_k(t) e^{beta_j t} dt  (exact)."""
    L = 2*T
    rows = []
    for be in betas:
        r = []
        for k in range(1, K+1):
            b = k*math.pi/L
            r.append(np.exp(-be*T)*b*(1 - ((-1)**k)*np.exp(be*L))/(be**2 + b**2))
        rows.append(r)
    return np.array(rows)

def symbolA(tau, T):
    """Symbol of A_T:  Re psi(1/4 + i tau/2) - log pi - 2 sum Lambda(n) n^{-1/2} cos(tau log n)."""
    s = np.real(digamma(0.25 + 0.5j*tau)) - math.log(math.pi)
    for n, lam in LAM.items():
        if n < math.exp(2*T) - 1e-13:
            s -= 2*lam/math.sqrt(n)*np.cos(tau*math.log(n))
    return s

def matA(T, K, taumax, npan=600, ng=24):
    lo_edges = np.linspace(0, 60, npan//2 + 1)[:-1]
    hi_edges = np.exp(np.linspace(math.log(60), math.log(taumax), npan//2 + 1))
    edges = np.concatenate([lo_edges, hi_edges])
    x, w = leggauss(ng)
    M = np.zeros((K, K))
    for lo, hi in zip(edges[:-1], edges[1:]):
        t = 0.5*(hi-lo)*x + 0.5*(hi+lo)
        ww = 0.5*(hi-lo)*w
        H = basis_hat(T, K, t)
        W = ww*symbolA(t, T)
        M += np.real((H*W) @ H.conj().T)
    M = 2*M/(2*math.pi)
    G = np.eye(K)*T
    return 0.5*(M + M.T), G

def matC(T, K, a, g0):
    u = moments(T, K, [a + 1j*g0])[0]          # Fhat(1/2+a+i g0) = u . f
    vb = moments(T, K, [-a + 1j*g0])[0]
    v = np.conj(vb)                             # conj Fhat(1/2-a+i g0) = v . f  (F real)
    uR, uI = u.real, u.imag
    vR, vI = v.real, v.imag
    C = 2*(np.outer(uR, vR) + np.outer(vR, uR) - np.outer(uI, vI) - np.outer(vI, uI))
    return 0.5*(C + C.T)

def lmin_Q(T, K, a, g0, taumax=None, Acache=None):
    if taumax is None:
        taumax = max(4000.0, 60*max(1.0, g0))
    M, G = Acache if Acache is not None else matA(T, K, taumax)
    C = matC(T, K, a, g0)
    Z = sla.null_space(moments(T, K, [-0.5, 0.5]))
    Q = Z.T @ (M - C) @ Z
    Gr = Z.T @ G @ Z
    w = sla.eigh(0.5*(Q+Q.T), 0.5*(Gr+Gr.T), eigvals_only=True)
    return w[0]

def Kfor(T, g0, mult=3.0, kmin=60):
    return int(max(kmin, mult*g0*2*T/math.pi + 60))

def tstar(a, g0, K=None, lo=0.05, hi=3.0, tol=1e-3, taumax=None):
    if K is None:
        K = Kfor(hi, g0)
    if taumax is None:
        taumax = max(4000.0, 60*max(1.0, g0))
    def neg(T):
        return lmin_Q(T, K, a, g0, taumax) < 0
    if not neg(hi):
        return None, K
    if neg(lo):
        return lo, K
    while hi - lo > tol:
        mid = 0.5*(lo+hi)
        if neg(mid): hi = mid
        else: lo = mid
    return 0.5*(lo+hi), K

# ---- frequency-cutoff driven version (T-adaptive basis; Omega = frequency cap) ----
def lmin_Q_om(T, a, g0, om_mult=4.0, extra=40, quad_mult=8.0):
    Om = max(om_mult*max(g0, 1.0), 120.0)
    K = int(2*T*Om/math.pi) + extra
    taumax = quad_mult*Om
    M, G = matA(T, K, taumax)
    C = matC(T, K, a, g0)
    Z = sla.null_space(moments(T, K, [-0.5, 0.5]))
    Q = Z.T @ (M - C) @ Z; Gr = Z.T @ G @ Z
    w = sla.eigh(0.5*(Q+Q.T), 0.5*(Gr+Gr.T), eigvals_only=True)
    return w[0], K

def tstar_om(a, g0, lo=0.05, hi=3.0, tol=5e-4, **kw):
    if lmin_Q_om(hi, a, g0, **kw)[0] >= 0: return None
    if lmin_Q_om(lo, a, g0, **kw)[0] < 0: return lo
    while hi - lo > tol:
        mid = 0.5*(lo+hi)
        if lmin_Q_om(mid, a, g0, **kw)[0] < 0: hi = mid
        else: lo = mid
    return 0.5*(lo+hi)
