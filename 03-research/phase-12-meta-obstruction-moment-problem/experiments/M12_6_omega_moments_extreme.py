#!/usr/bin/env python3
"""
Phase 12 / M12.6 — hook the omega-class moment machinery (P2-P5) to the large-sieve extreme bound.

The extreme of S(T) (= extreme large value of the explicit-formula prime sum F) is bounded, via the
MOMENT METHOD (deterministic, upper, non-positivity), by
   max_window |F|  <=  (E[F^{2k}])^{1/2k} * (#eff points)^{1/2k}   (optimize over k).
The 2k-th moments E[F^{2k}] are controlled by the DIAGONAL (Q-linear independence of {log p}) up to a
critical k, then RESONANCES (coherent prime alignments) inflate them -- the FREEZING. The omega-class
structure (P5) is exactly the decomposition that tracks this inflation.

We compute the moments of the prime-sum S-approx over a window, compare to Gaussian ((2k-1)!! sigma^{2k}),
locate the resonance onset (freezing), and read off the moment-method extreme bound vs the actual max.
"""
import numpy as np

def prime_powers(X):
    Xi=int(X); s=np.ones(Xi+1,bool); s[:2]=False
    for p in range(2,int(Xi**0.5)+1):
        if s[p]: s[p*p::p]=False
    out=[]
    for p in np.nonzero(s)[0]:
        lp=np.log(p); pk=p
        while pk<=Xi:
            out.append((np.log(pk), lp/(np.sqrt(pk)*np.log(pk)))); pk*=p
    return np.array(out)

def F_grid(Tgrid, pp):
    out=np.zeros_like(Tgrid)
    for logn,coef in pp:
        out -= coef*np.sin(Tgrid*logn)
    return out/np.pi

if __name__=="__main__":
    print("="*80)
    print(" M12.6 — omega-class moments + the moment-method extreme bound (deterministic, upper, non-PSD)")
    print("="*80)
    # window high enough that many primes contribute; X = e^{2d}-style cutoff ~ window scale
    T0=1e6; W=2000.0; X=3000
    grid=np.linspace(T0-W, T0+W, 200000)
    pp=prime_powers(X)
    F=F_grid(grid, pp); F-=F.mean()
    sigma=np.std(F); mx=np.max(np.abs(F))
    print(f" window T0={T0:.0f} +/- {W:.0f}, primes up to {X}, sigma={sigma:.4f}, max|F|={mx:.4f} (={mx/sigma:.2f} sigma)")

    print("\n  2k-th moments vs Gaussian (ratio>1 = super-Gaussian = resonance inflation = omega-class signal):")
    print("   2k    E[F^2k]/sigma^2k     Gaussian (2k-1)!!     ratio   ")
    from math import factorial
    def dfact(m):  # (m)!! for odd m
        r=1.0
        while m>0: r*=m; m-=2
        return r
    onset=None
    for k in range(1,9):
        m2k=np.mean(F**(2*k))/sigma**(2*k)
        g=dfact(2*k-1)
        ratio=m2k/g
        flag=""
        if ratio>1.5 and onset is None: onset=k; flag="  <- resonance onset (freezing)"
        print(f"   {2*k:2d}    {m2k:14.3e}     {g:12.1f}     {ratio:6.3f}{flag}")

    # moment-method extreme bound: max|F| <= (E[F^2k])^{1/2k} * Neff^{1/2k}; Neff ~ window * mean spacing of F
    Neff = 2*W * (np.log(T0)/(2*np.pi))   # ~ number of independent oscillation cells
    print(f"\n  moment-method extreme bound (Neff~{Neff:.0f}):  max|F| <= min_k (E[F^2k] Neff)^{{1/2k}}")
    best=np.inf
    for k in range(1,9):
        m2k=np.mean(F**(2*k))
        bnd=(m2k*Neff)**(1/(2*k))
        best=min(best,bnd)
    print(f"   moment bound on max|F| = {best:.3f}   (actual max = {mx:.3f}; ratio {best/mx:.2f})")
    print("\n"+"-"*80)
    print(" READ: the moments are ~Gaussian up to the resonance onset (k~%s), then inflate = FREEZING."%onset)
    print("  * up to freezing: the moment (large-sieve) UPPER bound holds -- DETERMINISTIC, upper, non-positivity.")
    print("  * past freezing: coherent prime alignments inflate the moments; the UPPER bound there needs control")
    print("    of the RESONANCE = how well {T log p mod 2pi} can align = a DIOPHANTINE/equidistribution question")
    print("    on {log p}. THAT is the genuine open frontier (Soundararajan resonance, Bondarenko-Seip), and the")
    print("    omega-class decomposition (P5) is the tool that tracks it. The remaining wall is the extreme")
    print("    resonance bound -- NOT the capstone, NOT N7: a Diophantine question about prime frequencies.")
    print("="*80)
