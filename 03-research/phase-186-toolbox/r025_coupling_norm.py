#!/usr/bin/env python3
"""R186_025 (P2) — norm of the residual coupling K_1 between two adjacent blocks on
Tate-orthogonal functions.  Two experiments:
 (a) Weyl sequence f_M(x) = x^{-1/2} 1_{[e^{-M},1]} (corner variable) projected onto
     the orthogonal complement of {e^{+-x/2}} in each block: Q(F)/||F||^2 -> pi.
 (b) Legendre Galerkin on two blocks (-tau,0),(0,tau)... with increasing degree N: the norm
     rises slowly with N (does not converge to 0.74).
Kernel: K_1(u) = 2 e^{-5u/2}/(1-e^{-2u}) = K(u) - 2e^{-u/2}  (Paper 47 lem:K).
Usage: python3 r025_coupling_norm.py
"""
import numpy as np
from numpy.polynomial import legendre as L

def K1(u): return 2*np.exp(-2.5*u)/(-np.expm1(-2*u))

# ---------- (a) Weyl sequence, blocks B=(-tau,0), B'=(0,tau); f on B: f(x)=|x|^{-1/2} on e^{-M} tau<=|x|<=tau
def weyl(tau, M, n=6000):
    # logarithmic variable t = log(|x|/tau) in [-M,0]; x = tau e^t ; dx = x dt
    t = np.linspace(-M, 0, n); dt = t[1]-t[0]
    x = tau*np.exp(t); w = x*dt               # weights for dx
    def proj_tate(f):
        # project f onto the orthogonal complement of {e^{x/2}, e^{-x/2}} on the block (0,tau) (same geometry by symmetry)
        e1 = np.cosh(x/2); e2 = np.sinh(x/2)/tau     # same envelope, well-conditioned Gram
        G = np.array([[np.sum(e1*e1*w), np.sum(e1*e2*w)],[np.sum(e1*e2*w), np.sum(e2*e2*w)]])
        c = np.linalg.solve(G, [np.sum(f*e1*w), np.sum(f*e2*w)])
        return f - c[0]*e1 - c[1]*e2
    f = x**-0.5
    fp = proj_tate(f)
    # Q = int int f(-x) g(y) K_1(x+y) dx dy  with f=g=fp (symmetric blocks)
    S = x[:,None]+x[None,:]
    Q = (fp*w) @ K1(S) @ (fp*w)                # sum_i sum_j fp_i w_i K1_ij fp_j w_j
    nrm = np.sum(fp*fp*w)
    # quadratic form on F=(f_B,f_B'): Q_tot = 2 <f_B, H f_B'>; ||F||^2 = 2 nrm; ratio = Q/nrm
    return Q/nrm
print("# (a) Weyl: tau, M -> Q(F)/||F||^2  (expected limit pi = %.4f)" % np.pi)
for tau in (0.0619, 0.03):
    for M in (2, 4, 8, 16, 32, 64, 128):
        print(f"tau={tau} M={M:3d}  {weyl(tau,M):.4f}")

# ---------- (b) Legendre Galerkin on two adjacent blocks
def galerkin(tau, N, nq=None):
    nq = nq or 3*N+20
    xg, wg = L.leggauss(nq)
    # right block (0,tau): y = tau(1+xg)/2 ; reflected left block: x = tau(1+xg)/2 (distance to the corner)
    y = tau*(1+xg)/2; w = tau/2*wg
    # orthonormal Legendre basis on (0,tau)
    P = np.array([L.legval(xg, [0]*k+[1])*np.sqrt((2*k+1)/tau) for k in range(N)])
    # Tate: constraints in the basis
    C = np.array([(P*w) @ np.exp(y/2), (P*w) @ np.exp(-y/2)])
    ev, V = np.linalg.eigh(C.T@C); Z = V[:, :N-2]       # kernel of the 2 constraints
    H = (P*w) @ K1(y[:,None]+y[None,:]) @ (P*w).T      # <phi_i, K1 phi_j> between blocks (corner at 0)
    Hz = Z.T @ H @ Z
    s = np.linalg.svd(Hz, compute_uv=False)
    return s[0]
print("# (b) Galerkin: tau=0.0619, N -> norm of the pair on V (= sup Q/||F||^2)")
for N in (6, 10, 14, 20, 30, 40, 60, 80):
    print(f"N={N:3d}  {galerkin(0.0619, N):.4f}")
