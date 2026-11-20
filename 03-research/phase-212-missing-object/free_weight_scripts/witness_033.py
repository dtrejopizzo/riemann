"""Dual optimum of V*+ = max_{w>=0} lambda_min(M0 - sum w_x C_x) on a lattice with generator 2 moved.
Dual: min Tr(rho M0) over rho>=0, Tr rho=1, c_rho(log x)=Tr(rho C_x) >= 0 at every lattice point;
complementarity: w_x>0 => c_rho(log x)=0.  Prints the state rho: rank, c_rho on the lattice, time and
frequency distribution.
usage: witness_033.py T N g2 [g3]"""
import sys, numpy as np
from math import log, exp
from numpy.polynomial.legendre import leggauss
from scipy.optimize import minimize
from forms import basis
from lattice_032A import setup

T = float(sys.argv[1]); N = int(sys.argv[2]); g2 = float(sys.argv[3])
g3 = float(sys.argv[4]) if len(sys.argv) > 4 else 3.0
X = exp(2 * T)
primes = [p for p in range(5, int(X) + 2) if all(p % q for q in range(2, int(p ** .5) + 1))]
els = {1.0}
for g in [g2, g3] + primes:
    new = set()
    for e in els:
        v = e * g
        while v < X: new.add(v); v *= g
    els |= new
el = np.array(sorted(e for e in els if e > 1.0001)); xs = np.log(el)
M0, C = setup(T, N, xs)
m = len(C); w = np.zeros(m)
for beta in [10, 30, 100, 300, 1000, 3000, 1e4, 3e4, 1e5]:
    def f(w):
        lam, V = np.linalg.eigh(M0 - np.tensordot(w, C, 1))
        a = -beta * (lam - lam[0]); p = np.exp(a); s = p.sum(); p /= s
        G = (V * p) @ V.T
        return -(lam[0] - np.log(s) / beta), np.einsum('mij,ij->m', C, G)
    w = minimize(f, w, jac=True, method='L-BFGS-B', bounds=[(0, None)] * m, options={'maxiter': 5000}).x
lam, V = np.linalg.eigh(M0 - np.tensordot(w, C, 1))
k = int(np.sum(lam - lam[0] < 2e-4)); Eb = V[:, :k]
Ck = np.einsum('ia,mij,jb->mab', Eb, C, Eb); act = w > 1e-3
def g(l):
    L = l.reshape(k, k); S = L @ L.T; S /= np.trace(S)
    c = np.einsum('mab,ab->m', Ck, S)
    return np.sum(c[act] ** 2) + np.sum(np.minimum(c[~act], 0) ** 2)
best = None
rng = np.random.default_rng(0)
for _ in range(20):
    r = minimize(g, rng.standard_normal(k * k), method='BFGS', options={'gtol': 1e-14, 'maxiter': 4000})
    if best is None or r.fun < best.fun: best = r
L = best.x.reshape(k, k); S = L @ L.T; S /= np.trace(S); rho = Eb @ S @ Eb.T
print(f"cluster dim k={k}  KKT residual={best.fun:.2e}")
print(f"T={T} N={N} g2={g2} g3={g3} npts={m}  V+={lam[0]:+.6f}  Tr(rho M0)={np.sum(rho*M0):+.6f}")
print("bottom eigenvalues:", " ".join(f"{x:+.5f}" for x in lam[:6]))
mu = np.linalg.eigvalsh(rho)[::-1]
print("rho spectrum:", " ".join(f"{x:.4f}" for x in mu[:6]))
c = np.einsum('mij,ij->m', C, rho)
print("  x        w_x       c_rho(log x)")
for e, wi, ci in zip(el, w, c):
    print(f"{e:8.4f} {wi:9.5f} {ci:+.5f}")
# reconstruct in time / frequency
xg, wg = leggauss(N + 40); t = T * xg; ww = wg * T
P = basis(T, N, t)
A = P.T @ (ww * np.exp(t / 2)); B = P.T @ (ww * np.exp(-t / 2))
Z = np.linalg.svd(np.vstack([A, B]))[2][2:].T
R = Z @ rho @ Z.T                       # rho in Legendre coefficients
dens = np.einsum('ti,ij,tj->t', P, R, P)
edges = np.linspace(-T, T, 11)
print("time mass by tenths of [-T,T]:", " ".join(f"{np.sum((ww*dens)[(t>=a)&(t<b)]):.3f}" for a, b in zip(edges[:-1], edges[1:])))
taus = np.linspace(0, 60, 241)
E = (P * ww[:, None]).T @ np.exp(-1j * np.outer(t, taus))      # N x ntau
S = np.real(np.einsum('it,ij,jt->t', E.conj(), R, E))
print("spectral density S(tau) (tau, S):")
for k in range(0, 241, 8):
    print(f"  {taus[k]:5.1f} {S[k]:.4f}")
cum = np.cumsum(S); cum /= cum[-1]
print("tau quantiles 10/50/90%:", " ".join(f"{taus[np.searchsorted(cum, q)]:.1f}" for q in (.1, .5, .9)))
# autocorrelation of rho on a fine grid of u
from forms import corr
us = np.linspace(0.02, 2 * T - 0.02, 80)
cu = [np.sum(rho * (Z.T @ corr(T, N, u) @ Z)) for u in us]
print("c_rho(u) on grid (u, e^u, c):")
for u, cc in zip(us, cu):
    print(f"  {u:.3f} {exp(u):7.3f} {cc:+.5f}")
