#!/usr/bin/env python3
"""
Phase 7 — second order.  Claim to VERIFY (not assert):

  The subdominant spectrum of the band-limited Carleson operator A_Phi^{-1} P_F equals
  1 - (eigenvalues of the SINE-KERNEL Gram of the zeros in the window).

  Mechanism: A_Phi - P_F = sum_{rho in window} v_rho v_rho^T  with v_rho[j] = S_j(gamma_rho)
  (the evaluation functionals).  So in the A-metric the nonzero eigenvalues of A^{-1}(A-P)=I-M
  equal the eigenvalues of the K x K Gram  V^T A^{-1} V = [K_A(gamma_i,gamma_j)], the reproducing
  kernel of the band-limited space = the (weighted) sine kernel.  RH (zeros real) => this Gram is a
  real PSD sine-kernel matrix => all eigenvalues in [0,1] => C_k = 1 - eig in [0,1] => C<=1.

We test: (a) A-P ?= V V^T (rank K).  (b) nonzero eig(A^{-1}VV^T) ?= eig(V^T A^{-1} V).
(c) that K x K Gram ?= the sine-kernel matrix sin(d(gi-gj))/(pi(gi-gj)) (up to the slow arch weight).
Real zeta zeros via mpmath.zetazero.
"""
import numpy as np, mpmath as mp
import carleson_band_engine as e
mp.mp.dps = 25

def zeta_zeros_in(lo, hi, maxn=400):
    g = []
    n = 1
    while n <= maxn:
        t = float(mp.im(mp.zetazero(n)))
        if t > hi: break
        if t >= lo: g.append(t)
        n += 1
    return np.array(g)

def build_AP_and_basis(d, T0, N, grid_pts=30000, span=None):
    spacing = np.pi/d
    centers = T0 + spacing*np.arange(-N, N+1)
    if span is None: span = (N+40)*spacing
    r = np.linspace(T0-span, T0+span, grid_pts); w = r[1]-r[0]
    X = d*(r[None,:]-centers[:,None]); S = np.sinc(X/np.pi)
    Phi = e.Phi_vec(r); pp = e.prime_powers(np.exp(2*d)); F = e.F_vec(r, pp)
    Sw = S*w
    A = Sw @ (Phi[:,None]*S.T); A=(A+A.T)/2
    P = Sw @ (F[:,None]*S.T);  P=(P+P.T)/2
    return A, P, centers, spacing

def sinc_at(centers, d, x):
    """basis vector v[j]=S_j(x)=sinc(d(x-c_j)) for a single point x."""
    return np.sinc(d*(x-centers)/np.pi)

if __name__ == "__main__":
    d, T0, N = 2.5, 50.0, 9
    print("="*82)
    print(f" Phase 7 second order — Carleson subdominant spectrum vs SINE-KERNEL Gram on zeros")
    print(f" d={d}  T0={T0}  basis dim M={2*N+1}")
    print("="*82)
    A, P, centers, spacing = build_AP_and_basis(d, T0, N)
    M = A.shape[0]
    # window half-width covered by the basis (where evaluation modes live)
    halfwin = N*spacing
    zeros = zeta_zeros_in(T0-halfwin, T0+halfwin)
    K = len(zeros)
    print(f" window [{T0-halfwin:.2f},{T0+halfwin:.2f}]  contains K={K} zeta zeros:")
    print("  ", np.round(zeros,3))

    # (a) does A-P equal V V^T (rank K)?  V[j,rho]=S_j(gamma_rho)
    V = np.stack([sinc_at(centers, d, g) for g in zeros], axis=1)   # (M,K)
    AP = A - P
    VVt = V @ V.T
    # best scalar align (the explicit-formula normalization of the zero term):
    s = np.sum(AP*VVt)/np.sum(VVt*VVt)
    relerr = np.linalg.norm(AP - s*VVt)/np.linalg.norm(AP)
    print(f"\n (a) A-P  vs  s*V V^T :  best s={s:.4f}   rel.Frobenius err={relerr:.3e}   (rank(A-P)~K={K}?)")
    evAP = np.linalg.eigvalsh(AP)
    print(f"     eig(A-P) sorted desc (expect ~K nonzero, M-K~={M-K} near 0):")
    print("     ", np.array2string(evAP[::-1], precision=3, suppress_small=True, max_line_width=110))

    # (b) generalized spectrum C_k = eig(A^{-1}P); subdominant 1-C_k vs eig of K x K Gram
    L = np.linalg.cholesky(A); Li = np.linalg.inv(L)
    Mmat = Li @ P @ Li.T; Mmat=(Mmat+Mmat.T)/2
    Ck = np.linalg.eigvalsh(Mmat)[::-1]
    Ainv = Li.T @ Li
    Ggram = V.T @ Ainv @ V                # K x K reproducing-kernel Gram in A-metric
    gg = np.linalg.eigvalsh(Ggram)[::-1]
    print(f"\n (b) Carleson eigenvalues C_k (top {min(K+3,M)}):")
    print("     ", np.array2string(Ck[:K+3], precision=4, suppress_small=True, max_line_width=110))
    print(f"     1 - C_k  (the K active modes):")
    print("     ", np.array2string((1-Ck)[:K], precision=4, suppress_small=True, max_line_width=110))
    print(f"     eig of K x K reproducing-kernel Gram V^T A^-1 V :")
    print("     ", np.array2string(gg, precision=4, suppress_small=True, max_line_width=110))
    print(f"     match (sorted): max|diff| = {np.max(np.abs(np.sort(1-Ck)[-K:][::-1]-gg)):.3e}")

    # (c) is the K x K Gram the sine kernel of the zero gaps?  K_sine[i,j]=sinc(d(gi-gj)/pi)*Phi-weight
    Ksine = np.array([[np.sinc(d*(zeros[i]-zeros[j])/np.pi) for j in range(K)] for i in range(K)])
    # normalize both to unit diagonal to compare shape (arch weight scales the diagonal)
    Dg = np.sqrt(np.diag(Ggram)); Gn = Ggram/np.outer(Dg,Dg)
    print(f"\n (c) reproducing-kernel Gram (diag-normalized) vs plain sine kernel sin(d dg)/(pi dg):")
    print(f"     max|Gnorm - Ksine| = {np.max(np.abs(Gn-Ksine)):.3e}  (small => it IS the sine kernel)")
    print("="*82)
    print(" INTERPRETATION: if (a,b,c) hold, the second-order structure of the Weil-Carleson form IS the")
    print(" sine-kernel determinantal process on the zeros (Montgomery pair correlation). C_max=1 <=> zeros")
    print(" real; the subdominant gap = sine-kernel eigenvalues = GUE statistics. The lever to test next:")
    print(" does pushing a zero off-line make a sine-Gram eigenvalue exceed 1 (=> C>1)?")
