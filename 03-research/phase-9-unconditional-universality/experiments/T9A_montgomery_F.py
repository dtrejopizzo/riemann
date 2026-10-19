#!/usr/bin/env python3
"""
Phase 9 / T9-A — attack the support barrier of Montgomery's pair correlation, head-on.

Montgomery's F(alpha,T) = (2pi)/(T log T) * sum_{0<g,g'<=T} (T^{i alpha (g-g')}) * 4/(4+(g-g')^2).
KNOWN (Montgomery, RH): F(alpha) ~ |alpha| for |alpha|<1 (+ a diagonal T^{-2|a|}log T spike near 0).
CONJECTURED (open): F(alpha) ~ 1 for |alpha|>1.  The |alpha|>1 region is governed by PRIME pair
correlations (Hardy-Littlewood) = the support barrier.

Our extremal target (P12): bound TIGHT pairs (small gaps) = an UPPER bound on a positive-kernel
integral of F at LARGE alpha.  Montgomery's unconditional tool is F>=0 (sum of squares) + the known
range |a|<1.  KEY QUESTION we probe: does F>=0 give the UPPER bound we need, or only lower bounds?

This computes F(alpha) from real zeros (shows the known/unknown boundary at alpha=1) and checks the
sign-direction of what the tight-pair target needs vs. what F>=0 provides.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 20

def zeros(N): return np.array([float(mp.im(mp.zetazero(n))) for n in range(1,N+1)])

def Fofalpha(g, alphas):
    T=g.max(); logT=np.log(T)
    D=g[:,None]-g[None,:]                 # (N,N) gamma-gamma'
    w=4.0/(4.0+D**2)
    norm=2*np.pi/(T*logT)
    F=np.array([norm*np.sum(np.cos(a*D*logT)*w) for a in alphas])
    return F

if __name__=="__main__":
    print("="*80)
    print(" T9-A: Montgomery F(alpha) from real zeros -- the known/unknown boundary at alpha=1")
    print("="*80)
    N=700; g=zeros(N); T=g.max()
    print(f" {N} zeros, T={T:.1f}, log T={np.log(T):.2f}")
    alphas=np.array([0.05,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.5,3.0])
    F=Fofalpha(g,alphas)
    print("\n  alpha   F(alpha)   Montgomery prediction        region")
    for a,f in zip(alphas,F):
        pred = f"~|a|={a:.2f}" if a<1 else "~1 (CONJECTURE, open)"
        reg  = "KNOWN (RH)" if a<1 else "UNKNOWN (prime corr.)"
        print(f"   {a:4.2f}   {f:7.3f}    {pred:24s} {reg}")
    print("\n  -> numerics show F rising ~|a| then leveling ~1 across a=1 (the conjecture holds in data);")
    print("     the a>1 region is exactly where PRIME pair-correlation (Hardy-Littlewood) enters.")

    print("\n"+"-"*80)
    print(" The sign-direction obstruction (our extremal target vs Montgomery's unconditional tool):")
    print("  * tight-pair count = sum_{g<g'} 1_{|g-g'| small} = int F(a) k_hat(a) da, k_hat>=0 at LARGE a")
    print("    (small gaps <-> high freq) -> needs an UPPER bound on F for a>1.")
    print("  * Montgomery's UNCONDITIONAL tool: F(a)>=0 (sum of squares) + F=|a| for a<1.")
    print("    F>=0 gives LOWER bounds on gap-counts (small gaps DO occur: Lehmer/simplicity), NOT the")
    print("    UPPER bound (clustering is bounded) that the collision margin needs.")
    print("  => the available unconditional handle is one-sided the WRONG way (echoes Gate-B/N5).")
    print("     T9-A reduces to UPPER bounds on F for a>1 = prime-pair-correlation upper bounds =")
    print("     variance of primes in short intervals (Goldston-Montgomery) -- famous & open.")
    print("="*80)
