"""R155.026 round 3c: RIGOROUS lower enclosure of w11 = W_T(F*) at T = log 2,
for the explicit N=18 Galerkin archimedean ground state F* (an explicit polynomial).
Levy form (Paper 47 thm:A):  W_T(F) = 2A(F)B(F) + C0*c(0) + int_0^{2T}(c(0)-c(u))K(u)du
                                       + c(0)*Ktail(2T) - sum_{n in N_T} v_n c(log n).
Every step is a two-sided bound; only floating-point rounding is allowed for, by an
explicit slack EPS added to the upper/subtracted from the lower bound."""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3a'))
import numpy as np, arch_core as ac
from numpy.polynomial import chebyshev as C

t0 = time.time()
T = float(np.log(2)); N = 18; TWO_T = 2*T
ac.Cmat.__defaults__ = (100,)
G = ac.gamma_matrix(T, N, nu=120); Pl, a, b = ac.pole_matrix(T, N)
Q = np.column_stack([a, b]); U, s, _ = np.linalg.svd(Q, full_matrices=True); Z = U[:, 2:]
ev, V = np.linalg.eigh(Z.T @ G @ Z)
coef = Z @ V[:, 0]                      # EXPLICIT coefficient vector of F* (orthonormal Legendre)
c0 = float(coef @ coef)

def Fval(t):
    return ac.basis(np.asarray(t, float), T, N) @ coef

def cfun(u, ng=80):
    """c(u) = int_{-T+u}^{T} F(t)F(t-u) dt, exact for polynomials (Gauss, ng nodes)."""
    u = float(u)
    if u >= TWO_T: return 0.0
    lo, hi = -T+u, T
    xg, wg = np.polynomial.legendre.leggauss(ng)
    t = 0.5*(hi-lo)*xg + 0.5*(hi+lo); w = 0.5*(hi-lo)*wg
    return float(np.sum(w*Fval(t)*Fval(t-u)))

# --- Chebyshev representation of c on [0,2T] (c is a polynomial of degree <= 2N-1 = 35)
deg = 2*N + 2
k = np.arange(deg+1)
nodes = 0.5*TWO_T*(np.cos(np.pi*(k+0.5)/(deg+1)) + 1.0)
vals = np.array([cfun(x) for x in nodes])
cc = C.chebfit(2*nodes/TWO_T - 1.0, vals, deg)
test = np.linspace(0.001, TWO_T-0.001, 25)
resid = max(abs(C.chebval(2*x/TWO_T-1.0, cc) - cfun(x)) for x in test)
EPS = 1e-9                                        # rounding slack, >> observed residual
assert resid < 1e-11, resid
gc = -cc.copy(); gc[0] += c0                       # g(u) = c(0) - c(u)  (>= 0 by Cauchy-Schwarz)
gpr = C.chebder(gc)*(2.0/TWO_T)
G1 = float(np.sum(np.abs(gpr)))                    # rigorous sup|g'| on [0,2T]

def gval(x):  return C.chebval(2*np.asarray(x)/TWO_T - 1.0, gc)
def Kd(u):    return 0.5/np.sinh(u/2.0) + 0.5/np.cosh(u/2.0)   # decreasing on (0,inf)

# --- panel enclosure of int_0^{2T} g K
delta = 1e-7
M = 3_000_000
lo_edges = delta*np.exp(np.linspace(0.0, np.log(TWO_T/delta), M+1))
al, be = lo_edges[:-1], lo_edges[1:]
h = be - al; mid = 0.5*(al+be)
gm = gval(mid); half = 0.5*G1*h
glo = np.maximum(gm - half, 0.0); ghi = gm + half
I_lo = float(np.sum(h*glo*Kd(be))); I_hi = float(np.sum(h*ghi*Kd(al)))
I_hi += G1*(delta + delta**2/4.0)                   # [0,delta]: 0 <= int <= G1(d + d^2/4)

# --- the remaining (finite, exact) terms
Ktail = float(ac.Ktail(TWO_T))
prim = 0.0; contacts = []
for n in (2, 3, 4, 5, 6, 7):
    if np.log(n) < TWO_T:
        from math import log
        lam = {2: np.log(2), 3: np.log(3), 4: np.log(2), 5: np.log(5), 7: np.log(7)}.get(n)
        if lam is None: continue
        v = 2*lam/np.sqrt(n); contacts.append(n); prim -= v*cfun(np.log(n))
xg, wg = np.polynomial.legendre.leggauss(400); t = T*xg; w = T*wg
Aq = float(np.sum(w*Fval(t)*np.exp(t/2))); Bq = float(np.sum(w*Fval(t)*np.exp(-t/2)))
pole_bound = 2*abs(Aq)*abs(Bq) + 1e-12

base = ac.C0*c0 + c0*Ktail + prim
w11_lo = base + I_lo - pole_bound - EPS
w11_hi = base + I_hi + pole_bound + EPS
print('c(0) = %.12f   G1 = %.4f   cheb resid = %.2e   contacts %s' % (c0, G1, resid, contacts))
print('A(F*) = %.3e  B(F*) = %.3e  |pole| <= %.2e' % (Aq, Bq, pole_bound))
print('Levy integral  in [%.10f, %.10f]  (width %.2e)' % (I_lo, I_hi, I_hi-I_lo))
print('w11           in [%.10f, %.10f]  (width %.2e)' % (w11_lo, w11_hi, w11_hi-w11_lo))
print('unit-norm w11 in [%.10f, %.10f]' % (w11_lo/c0, w11_hi/c0))
print('VERDICT: w11 > 0 rigorously:', w11_lo > 0)
json.dump(dict(T=T, N=N, c0=c0, G1=G1, resid=resid, I_lo=I_lo, I_hi=I_hi,
               w11_lo=w11_lo, w11_hi=w11_hi, panels=M, delta=delta, EPS=EPS,
               contacts=contacts, A=Aq, B=Bq, coef=list(coef)),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r3c_02.json'), 'w'), indent=1)
print('runtime %.1fs' % (time.time()-t0))
