#!/usr/bin/env python3
"""
Phase 7 — Open-core attack.  The RIGOROUS band-limited Carleson constant.

  RH  <=>  C(d,T0) := lambda_max(P_F, A_Phi) <= 1   for all band d, height T0,

where, for f = phi_hat band-limited to [-d,d] in the log-prime variable (so the
prime sum truncates to n <= e^{2d}: a FINITE, well-posed form, NOT the refuted
pointwise comb):

  A_Phi[i,j] = \int S_i(r) S_j(r) Phi(r) dr      Phi(r)=Re psi(1/4+ir/2)-log pi   (archimedean envelope, >0 for r>~7)
  P_F[i,j]   = \int S_i(r) S_j(r) F(r) dr         F(r)=2 sum_{n<=e^{2d}} Lambda(n)/sqrt(n) cos(r log n)   (prime comb, factor 2)

The threshold "1" is INTRINSIC (the factor-2 on F and Phi as written come from the
same Weil explicit formula); no free normalization.  Basis: sinc samples at spacing
pi/d centered at T0 (band-limited type d), windowed to |j|<=N.  The pole term
2|f(i/2)|^2 >= 0 is DROPPED -> conservative (makes C larger).

What we measure: C(d,T0) for zeta (RH true => expect <=1; the MARGIN 1-C and what
controls it is the open-core question), across heights at/near/between zeros, and as
d grows (more primes, finer resolution).  Honest: this is the large-values frontier;
we are measuring whether band-limited smoothing brings the comb under the envelope and
how the margin behaves.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 18

# ---------- archimedean envelope Phi(r) ----------
def Phi_vec(r):
    out = np.empty_like(r)
    lp = float(mp.log(mp.pi))
    for i, rr in enumerate(r):
        out[i] = float(mp.re(mp.digamma(mp.mpf('0.25') + 1j*rr/2))) - lp
    return out

# ---------- prime comb F(r) = 2 sum_{n<=N} Lambda(n)/sqrt(n) cos(r log n) ----------
def prime_powers(X):
    """yield (log n, Lambda(n)/sqrt(n)) for prime powers n=p^k <= X."""
    X = int(X)
    sieve = np.ones(X+1, bool); sieve[:2] = False
    for p in range(2, int(X**0.5)+1):
        if sieve[p]: sieve[p*p::p] = False
    out = []
    for p in np.nonzero(sieve)[0]:
        lp = np.log(p); pk = p
        while pk <= X:
            out.append((np.log(pk), lp/np.sqrt(pk)))
            pk *= p
    return np.array(out)  # columns: log n, Lambda(n)/sqrt(n)

def F_vec(r, pp):
    logs = pp[:,0][:,None]      # (Nterms,1)
    amps = pp[:,1][:,None]
    return 2.0 * np.sum(amps * np.cos(logs * r[None,:]), axis=0)

# ---------- band-limited sinc basis, spacing pi/d centered at T0 ----------
def carleson_C(d, T0, N, grid_pts=6000, span=None):
    """C(d,T0) = lambda_max(P_F, A_Phi); also returns margin and diagnostics."""
    spacing = np.pi/d
    centers = T0 + spacing*np.arange(-N, N+1)          # (2N+1,)
    # integration grid: cover window + sinc tails
    if span is None: span = (N+8)*spacing
    r = np.linspace(T0-span, T0+span, grid_pts)
    w = (r[1]-r[0])
    # sinc_j(r) = sin(d(r-c_j))/(d(r-c_j)) * (d/pi)^{1/2}  (L2-normalized: <sinc_i,sinc_j> = (pi/d) delta)
    # use unnormalized sinc then both A,P carry same factor -> ratio unaffected.
    X = d*(r[None,:] - centers[:,None])                # (2N+1, grid)
    S = np.sinc(X/np.pi)                                # numpy sinc = sin(pi x)/(pi x); arg X/pi -> sin(X)/X
    Phi = Phi_vec(r)
    pp = prime_powers(np.exp(2*d))
    F = F_vec(r, pp)
    Sw = S*w
    A = Sw @ (Phi[:,None]*S.T)                          # (2N+1,2N+1)
    P = Sw @ (F[:,None]*S.T)
    A = (A+A.T)/2; P = (P+P.T)/2
    # generalized eig: C = max eigenvalue of A^{-1} P (symmetrized).  A must be PD.
    evA = np.linalg.eigvalsh(A)
    if evA[0] <= 0:
        return dict(C=np.nan, note=f"A not PD (min eig {evA[0]:.2e}); height too low?", nA=A.shape[0])
    L = np.linalg.cholesky(A)
    Li = np.linalg.inv(L)
    M = Li @ P @ Li.T; M = (M+M.T)/2
    ev = np.linalg.eigvalsh(M)
    return dict(C=ev[-1], Cmin=ev[0], margin=1-ev[-1], nA=A.shape[0],
                nprimes=pp.shape[0], note="ok")

if __name__ == "__main__":
    print("="*84)
    print(" Phase 7 — band-limited Carleson constant  C(d,T0)=lambda_max(P_F,A_Phi);  RH => C<=1")
    print("="*84)
    # heights: 14.1347 (1st zero), 21.022 (2nd), 25.0 (between 2nd/3rd ~25.01), 30.0, 50.0, 100.0
    heights = [14.1347, 21.0220, 25.0109, 30.4249, 49.7738, 100.0]
    hlabel  = ["zero#1","zero#2","zero#4","between","zero","high"]
    for d in [2.0, 3.0, 4.0]:
        print(f"\n  d = {d}   (primes up to e^(2d) = {np.exp(2*d):.0f})")
        for T0, lab in zip(heights, hlabel):
            res = carleson_C(d, T0, N=10)
            if np.isnan(res["C"]):
                print(f"    T0={T0:8.3f} [{lab:7s}]  {res['note']}")
            else:
                flag = "  <= 1 OK" if res["C"]<=1+1e-9 else "  *** C>1 ***"
                print(f"    T0={T0:8.3f} [{lab:7s}]  C={res['C']:9.5f}  margin={res['margin']:+.4f}"
                      f"  (basis {res['nA']}, {res['nprimes']} prime terms){flag}")
    print("="*84)
