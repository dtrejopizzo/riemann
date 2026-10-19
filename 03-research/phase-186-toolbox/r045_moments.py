#!/usr/bin/env python3
"""R186_045 — Moments of the pencil (Neg_T, Pos_T) on P_T and the method of moments for beta_max.

Reuses r034_det.py (same Galerkin–Legendre construction: a_T, Neg, Pos, Tate).
  B = Pos^{-1/2} Neg Pos^{-1/2} | P_T  (Birman–Schwinger),  beta_j = spec B,  m_k = Tr(B^k) = sum beta_j^k.
Moment bounds (unit weights, support [0, beta_max]):
  (i)  beta_max <= m_k^{1/k}                         (trivial, exact: lim_k = beta_max)
  (ii) Samuelson (n atoms): beta_max <= m_1/n + sqrt((n-1)/n * (m_2 - m_1^2/n))
  (iii) k* = min{k : m_k < 1}  (exact criterion: beta_max < 1 <=> exists k with m_k < 1)
Lemma T: 1 - m_k^{1/k} <= 1 - beta_max = lambda_A / Pos(h*)  (inheritance).
Usage: python3 r045_moments.py [M=40] [nu=400]
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
import r034_det as R

def run(T, M, nu):
    name = {0.5*np.log(3): '1/2 log 3', 0.5*np.log(5): '1/2 log 5', np.log(2): 'log 2'}.get(T, '%.4f' % T)
    A, A0, ta, tb = R.build_x(T, M, nu)
    comps, zs = R.neg_set(T)
    N = R.build_neg(T, M, comps); Pos = A + N
    Z = R.null_basis([ta, tb])
    AP, NP, PP = Z.T @ A @ Z, Z.T @ N @ Z, Z.T @ Pos @ Z
    lamA = np.linalg.eigvalsh(AP)[0]
    Lc = np.linalg.cholesky(PP); Li = np.linalg.inv(Lc); B = Li @ NP @ Li.T
    beta = np.linalg.eigvalsh(B); beta = np.clip(beta, 0, None); bmax = beta[-1]
    n = len(beta)
    print(f"\n=== T = {name}  M = {M}  dim P_T = {n}  #comp = {len(comps)}  lambda_A = {lamA:+.4e}")
    print(f"beta_max = {bmax:.12f}   1 - beta_max = {1-bmax:.4e}   betas: {np.round(beta[-6:][::-1], 6).tolist()}")
    print(f"K_delta (1-beta<1e-2) = {(1-beta<1e-2).sum()}   tr Neg|P = {np.trace(NP):.4f}   tr B = m_1 = {beta.sum():.4f}")
    print(" k   m_k = Tr(B^k)     m_k^{1/k}    1 - m_k^{1/k}     k(1-beta_max)   Samuelson(k=2)")
    for k in range(1, 7):
        mk = (beta**k).sum()
        sam = beta.sum()/n + np.sqrt(max((n-1)/n*((beta**2).sum() - beta.sum()**2/n), 0)) if k == 2 else float('nan')
        print(f" {k}   {mk:12.6f}   {mk**(1/k):10.6f}   {1-mk**(1/k):+12.4e}   {k*(1-bmax):10.3e}   {sam:10.6f}")
    # exact k* and margin
    ks = None
    for k in (10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12):
        with np.errstate(under='ignore'):
            mk = np.sum(np.exp(k*np.log(beta[beta>0])))
        if mk < 1: ks = k; break
    # analytic estimate: k such that sum_{j>=2} beta_j^k < k(1-beta_max)
    b2 = beta[-2]
    print(f"k* = min{{k: m_k < 1}} ~ {ks}   (second beta: 1-beta_2 = {1-b2:.3e});  at k*: 1 - m_k^(1/k) ~ {(1-np.sum(np.exp(ks*np.log(beta[beta>0])))**(1/ks)) if ks else float('nan'):.3e}  vs 1-beta_max = {1-bmax:.3e}")
    # Lemma T with M_1-type: rank-one perturbation of size (1-beta_max) in the direction of beta_max
    v = np.linalg.eigh(B)[1][:, -1]; Bp = B + (1-bmax)*np.outer(v, v); bp = np.linalg.eigvalsh(Bp)
    print("Lemma T (check): B' = B + (1-beta_max) v v^T has beta_max' = %.12f; |m_k(B') - m_k(B)| for k=1..6: %s"
          % (bp[-1], ["%.2e" % abs((bp**k).sum() - (beta**k).sum()) for k in range(1, 7)]))
    return beta

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    nu = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    for T in (0.5*np.log(3), np.log(2), 0.5*np.log(5)):
        run(T, M, nu)
