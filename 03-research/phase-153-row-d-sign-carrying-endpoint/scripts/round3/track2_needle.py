"""R153 Track 2: the b-needle.  Mesh-free spectral assembly (reuses scripts/audit).
Operator  A_T(b) = G_{Gamma,T} - m_0 - w2 (S_{log2}+S_{-log2}) - w3 (S_b + S_{-b})
on P_T = ker M_- cap ker M_+, w_n = Lambda(n) n^{-1/2}.
Rayleigh quotient in L^2.  All values DIAGNOSTIC-NUMERIC.
"""
import math, sys, os
import numpy as np, scipy.linalg as sla
from scipy.special import psi as digamma
from numpy.polynomial.legendre import leggauss
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'audit'))
from aud_spectral import basis_hat, moments

W2 = math.log(2)/math.sqrt(2)
W3 = math.log(3)/math.sqrt(3)
LOG3 = math.log(3)

_cache = {}

def blocks(T, K, taumax=4000., npan=400, ng=24):
    """Return (March, M2, Mcos(b) builder pieces): assemble panels once."""
    key = (T, K, taumax, npan, ng)
    if key in _cache: return _cache[key]
    edges = np.concatenate([np.linspace(0, 50, npan//2+1)[:-1],
                            np.exp(np.linspace(math.log(50), math.log(taumax), npan//2+1))])
    TAU = []; WW = []; HH = []
    x, w = leggauss(ng)
    for lo, hi in zip(edges[:-1], edges[1:]):
        t = 0.5*(hi-lo)*x + 0.5*(hi+lo); ww = 0.5*(hi-lo)*w
        TAU.append(t); WW.append(ww); HH.append(basis_hat(T, K, t))
    tau = np.concatenate(TAU); ww = np.concatenate(WW); H = np.concatenate(HH, axis=1)
    # |Hkl|^2 style: we need real part of H diag(w f(tau)) H^*
    arch = np.real(digamma(0.25+0.5j*tau)) - math.log(math.pi)
    March = np.real((H*(ww*arch))@H.conj().T)
    M2 = np.real((H*(ww*2*np.cos(tau*math.log(2))))@H.conj().T)
    out = (tau, ww, H, March, M2)
    _cache[key] = out
    return out

def lam_min(T, K, b, vec=False, w3=W3, w2=W2, **kw):
    tau, ww, H, March, M2 = blocks(T, K, **kw)
    M3 = np.real((H*(ww*2*np.cos(tau*b)))@H.conj().T)
    M = 2*(March - (w2/W2)*W2*M2 - w3*M3)/(2*math.pi)
    M = 0.5*(M+M.T)
    G = np.eye(K)*T
    C = moments(T, K, [-0.5, 0.5]); Z = sla.null_space(C)
    A = Z.T@M@Z; B = Z.T@G@Z
    if vec:
        w, V = sla.eigh(A, B); return w[0], Z@V[:, 0]
    return sla.eigh(A, B, eigvals_only=True)[0]

def autocorr(T, v, K, bs):
    """c_F(b) = int F(t)F(t+b) dt for F = sum v_k sin(k pi (t+T)/(2T)), normalised ||F||=1."""
    L = 2*T
    n = max(8192, 64*K)
    t = np.linspace(-T, T, n)
    F = np.zeros(n)
    for k in range(1, K+1):
        F += v[k-1]*np.sin(k*math.pi*(t+T)/L)
    nrm = math.sqrt(np.trapz(F*F, t))
    F /= nrm
    out = []
    for b in np.atleast_1d(bs):
        # int_{-T}^{T-b} F(t)F(t+b) dt
        m = t <= T-b
        tt = t[m]
        Fs = np.zeros_like(tt)
        for k in range(1, K+1):
            Fs += v[k-1]*np.sin(k*math.pi*(tt+b+T)/L)
        Fs /= nrm
        out.append(np.trapz(F[m]*Fs, tt))
    return np.array(out)
