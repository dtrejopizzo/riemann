"""Core: matrices of the Weil form on L^2(-T,T) in an orthonormal Legendre basis.

W_T(F) = pole + gamma + prime, Paper 47 normalisation:
  gamma(F) = C0*||F||^2 + int_0^inf (||F||^2 - c_F(u)) K(u) du,  K = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2))
  pole(F)  = 2 A(F) B(F),   A = int F e^{t/2}, B = int F e^{-t/2}
  prime(F) = - sum_{n < e^{2T}} v_n c_F(log n),  v_n = 2 Lambda(n)/sqrt(n)
A_inf = pole + gamma (the archimedean form, no primes).
"""
import numpy as np
from numpy.polynomial import legendre as L
from scipy.special import psi as digamma

C0 = digamma(0.25) - np.log(np.pi)          # -5.3721834...

def Kdens(u):
    return 0.5/np.sinh(u/2.0) + 0.5/np.cosh(u/2.0)

def Ktail(x):
    """int_x^inf K = log coth(x/4)... (Thm S(iii) with x=2T): log coth(T/2)+pi-2 arctan e^T."""
    return np.log(1.0/np.tanh(x/4.0)) + np.pi - 2.0*np.arctan(np.exp(x/2.0))

def phi_bernstein(x, K=200000):
    a = np.arange(K) + 0.25
    return np.sum(x/(a*(x + 4*a*a)))

def basis(t, T, N):
    """orthonormal Legendre on (-T,T): rows = points, cols = basis index."""
    x = t/T
    V = np.zeros((len(x), N))
    for k in range(N):
        c = np.zeros(k+1); c[k] = 1.0
        V[:, k] = L.legval(x, c)*np.sqrt((2*k+1)/(2.0*T))
    return V

def Cmat(u, T, N, nq=220):
    """C_ij(u) = int phi_i(t) phi_j(t-u) dt, t in (-T+u, T); returns symmetrised."""
    u = abs(u)
    if u >= 2*T:
        return np.zeros((N, N))
    a, b = -T+u, T
    xg, wg = np.polynomial.legendre.leggauss(nq)
    t = 0.5*(b-a)*xg + 0.5*(a+b); w = 0.5*(b-a)*wg
    Vi = basis(t, T, N); Vj = basis(t-u, T, N)
    C = (Vi*w[:, None]).T @ Vj
    return 0.5*(C + C.T)

def gamma_matrix(T, N, nu=600):
    """C0*I + int_0^{2T}(I - C(u))K(u)du + Ktail(2T)*I."""
    I = np.eye(N)
    # split [0,2T] into [0,eps] and [eps,2T] for the 1/u kernel
    G = np.zeros((N, N))
    edges = [0.0, 0.02*2*T, 0.2*2*T, 2*T]
    for lo, hi in zip(edges[:-1], edges[1:]):
        xg, wg = np.polynomial.legendre.leggauss(nu)
        u = 0.5*(hi-lo)*xg + 0.5*(hi+lo); w = 0.5*(hi-lo)*wg
        for uu, ww in zip(u, w):
            G += ww*Kdens(uu)*(I - Cmat(uu, T, N))
    return C0*I + G + Ktail(2*T)*I

def pole_matrix(T, N, nq=400):
    xg, wg = np.polynomial.legendre.leggauss(nq)
    t = T*xg; w = T*wg
    V = basis(t, T, N)
    a = (V*(w*np.exp(t/2.0))[:, None]).sum(axis=0)
    b = (V*(w*np.exp(-t/2.0))[:, None]).sum(axis=0)
    return np.outer(a, b) + np.outer(b, a), a, b

def vonmangoldt(nmax):
    out = {}
    for p in range(2, nmax+1):
        if all(p % d for d in range(2, int(p**0.5)+1)):
            q = p
            while q <= nmax:
                out[q] = np.log(p); q *= p
    return out

def prime_matrix(T, N):
    nmax = int(np.exp(2*T)) + 1
    P = np.zeros((N, N)); A_T = 0.0; contacts = []
    for n, Lam in sorted(vonmangoldt(nmax).items()):
        if np.log(n) < 2*T:
            v = 2*Lam/np.sqrt(n); A_T += v; contacts.append(n)
            P -= v*Cmat(np.log(n), T, N)
    return P, A_T, contacts

def restrict(M, a, b):
    """restrict quadratic form M to {x: a.x = b.x = 0} (orthonormal basis => P_T)."""
    Q = np.column_stack([a, b])
    U, s, _ = np.linalg.svd(Q, full_matrices=True)
    r = int((s > 1e-12).sum())
    Z = U[:, r:]
    return Z.T @ M @ Z
