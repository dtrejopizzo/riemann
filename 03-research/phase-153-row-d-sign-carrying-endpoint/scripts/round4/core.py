"""R153 round 4: decay law of lambda(T) = lambda_min(A_T|P_T).
Reuses verbatim the mesh-free spectral sine assembly of scripts/audit/aud_spectral.py
(basis_hat, moments).  Parity-resolved; codim-2 (P_T) and codim-4 (a->0 limit of
P_T^{(a)}) constraint spaces; second-order operator D_T = -g''(D).  DIAGNOSTIC-NUMERIC."""
import math, sys, os, numpy as np, scipy.linalg as sla
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'audit'))
import aud_spectral as A
from numpy.polynomial.legendre import leggauss
from scipy.special import psi as digamma

LAM = {}
for n in range(2, 400):
    for p in (2,3,5,7,11,13,17,19):
        v = p
        while v <= n:
            if v == n: LAM[n] = math.log(p)
            v *= p

def contacts(T):
    return [(n,l) for n,l in sorted(LAM.items()) if n < math.exp(2*T) - 1e-13]

# ---- symbol of A_T (NOT doubled): g(tau) = Re psi(1/4+i tau/2) - log pi - 2 sum w_n cos(tau log n)
def gsym(tau, T, order=0):
    """order=0: g; order=2: g''(tau)."""
    tau = np.asarray(tau, dtype=float)
    if order == 0:
        s = np.real(digamma(0.25 + 0.5j*tau)) - math.log(math.pi)
        for n,l in contacts(T):
            s -= 2*l/math.sqrt(n)*np.cos(tau*math.log(n))
        return s
    # g'' by complex-step-free exact route: Re psi(1/4+i tau/2)'' = -(1/4) Re psi''(1/4+i tau/2)
    z = 0.25 + 0.5j*tau
    s = -0.25*np.real(psi2(z))
    for n,l in contacts(T):
        L = math.log(n)
        s += 2*l/math.sqrt(n)*L*L*np.cos(tau*L)
    return s

def psi2(z, M=60):
    """psi''(z) for complex z: recurrence + asymptotic (checked vs mpmath to 1e-14)."""
    z = np.asarray(z, dtype=complex); acc = np.zeros_like(z)
    for k in range(M): acc += -2.0/(z+k)**3
    w = z + M
    return acc + (-1/w**2 - 1/w**3 - 0.5/w**4 + 1/(6*w**6) - 1/(6*w**8))

def assemble(T, K, taumax=4000.0, npan=400, ng=24, order=0):
    edges = np.concatenate([np.linspace(0,50,npan//2+1)[:-1],
                            np.exp(np.linspace(math.log(50), math.log(taumax), npan//2+1))])
    x,w = leggauss(ng); M = np.zeros((K,K))
    for lo,hi in zip(edges[:-1], edges[1:]):
        t = 0.5*(hi-lo)*x + 0.5*(hi+lo); ww = 0.5*(hi-lo)*w
        H = A.basis_hat(T,K,t); m = gsym(t,T,order)
        M += np.real(H@np.diag(ww*m)@H.conj().T)
    M = 2*M/(2*math.pi)                 # +-tau halves, 1/2pi
    return 0.5*(M+M.T)

def mom(T, K, beta):
    L = 2*T
    b = np.array([k*math.pi/L for k in range(1,K+1)])
    sg = np.array([(-1)**k for k in range(1,K+1)])
    return np.exp(-beta*T)*b*(1-sg*np.exp(beta*L))/(beta**2+b**2)

def dmom(T, K, beta, h=1e-6):
    return (mom(T,K,beta+h)-mom(T,K,beta-h))/(2*h)

def blocks(K):
    ev = np.array([k for k in range(1,K+1) if k % 2 == 1]) - 1   # even-parity basis fns
    od = np.array([k for k in range(1,K+1) if k % 2 == 0]) - 1
    return ev, od

def lam_min(T, K, codim=2, M=None, want_vec=False, **kw):
    """returns (lambda, parity, coefficient vector in full K basis)"""
    if M is None: M = assemble(T,K,**kw)
    m1 = mom(T,K,0.5); m2 = dmom(T,K,0.5)
    out = []
    for name, idx in zip(('even','odd'), blocks(K)):
        Mb = M[np.ix_(idx,idx)]
        rows = [m1[idx]] + ([m2[idx]] if codim == 4 else [])
        Z = sla.null_space(np.array(rows))
        w,V = sla.eigh(Z.T@Mb@Z, T*np.eye(Z.shape[1]))
        vec = np.zeros(K); vec[idx] = Z@V[:,0]
        out.append((w[0], name, vec))
    out.sort(key=lambda r: r[0])
    return out[0] if want_vec else (out[0][0], out[0][1], out)
