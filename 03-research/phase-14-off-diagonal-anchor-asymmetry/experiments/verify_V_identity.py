#!/usr/bin/env python3
"""
Verify the backbone identity of the (LB) reduction, with REAL zeta zeros:

    V(d,T) := sum_{g,g'} 2 sin(2d(g-g'))/(g-g')   ==   integral_{-2d}^{2d} |sum_g e^{i g xi}|^2 dxi   >= 0,

and measure V(d,T)/(d N) (the form-factor-averaged second moment).  If V/(dN) stays O(1) and bounded as the
band d crosses alpha~1, that confirms (empirically) F(alpha) bounded for |alpha|>=1 (c=0 in reality, GUE),
i.e. the residue is exactly the *uniform* form factor and ZETA's zeros realize the clean bound.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 25

def get_zeros(n0, n1):
    g = []
    for n in range(n0, n1):
        g.append(float(mp.im(mp.zetazero(n))))
    return np.array(g)

def V_pairsum(g, d):
    diff = g[:,None]-g[None,:]
    with np.errstate(divide='ignore', invalid='ignore'):
        K = 2*np.sin(2*d*diff)/diff
    np.fill_diagonal(K, 4*d)        # limit of 2 sin(2d u)/u at u->0
    return np.sum(K)

def V_integral(g, d, pts=200000):
    xi = np.linspace(-2*d, 2*d, pts); w = xi[1]-xi[0]
    # |S(xi)|^2 = |sum e^{i g xi}|^2
    S = np.sum(np.exp(1j*np.outer(g, xi)), axis=0)
    return np.real(np.sum(np.abs(S)**2)*w)

if __name__ == "__main__":
    print("="*80)
    print(" Verify  V(d,T)=sum 2sin(2d(g-g'))/(g-g')  ==  int_{-2d}^{2d}|S|^2 dxi,  real zeta zeros")
    print("="*80)
    n0, n1 = 1000, 1080
    print(f" fetching zeros #{n0}..{n1-1} (mpmath)...")
    g = get_zeros(n0, n1)
    N = len(g); T = g.mean()
    rho = np.log(T/(2*np.pi))/(2*np.pi)    # mean zero density
    print(f"  N={N}  height T~{T:.1f}  mean density rho~{rho:.4f}  mean spacing ~{1/rho:.4f}")
    print(f"\n   {'d':>6} {'alpha=2d*rho':>12} {'V (pairsum)':>14} {'V (integral)':>14} {'rel.err':>9} {'V/(dN)':>9}")
    for d in [0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0]:
        Vp = V_pairsum(g, d); Vi = V_integral(g, d)
        alpha = 2*d*rho
        err = abs(Vp-Vi)/abs(Vi)
        print(f"   {d:>6.2f} {alpha:>12.4f} {Vp:>14.4f} {Vi:>14.4f} {err:>9.1e} {Vp/(d*N):>9.4f}")
    print("="*80)
    print(" identity holds if rel.err ~ 0 ;  V/(dN) bounded as alpha crosses 1 => F bounded for |alpha|>=1 (GUE).")
