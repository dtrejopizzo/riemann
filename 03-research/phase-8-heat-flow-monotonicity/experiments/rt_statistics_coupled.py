#!/usr/bin/env python3
"""
Phase 8 / Rodgers-Tao statistics-coupled — locate the EXACT statistical object for Lambda<=0 (RH).

Logic (from N5 + Gate B):
 - The flow is arithmetic-blind; arithmetic enters via the INITIAL zero configuration.
 - A complex pair at t=0 (RH false) is born, going backward, from a near-COLLISION of two real zeros.
   By Gate B an isolated pair heals with d(y^2)/dt=-2; reversing, a tight real pair of (normalized) gap
   g collides under backward flow on a t-scale ~ g^2.  So Lambda is governed by the CLOSEST pairs.
 - Rodgers-Tao proved Lambda>=0 from the LOWER tail (zeros fluctuate, not a rigid lattice).
   RH = Lambda<=0 needs the UPPER tail: NO pair is anomalously tight, UNIFORMLY in T.

This script measures, on real zeta zeros, the gap distribution and the minimum normalized gap (the
Lehmer phenomenon), to exhibit precisely the object whose uniform control is RH-equivalent.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 30

def zeta_ordinates(n0, n1):
    return np.array([float(mp.im(mp.zetazero(n))) for n in range(n0, n1+1)])

def normalized_gaps(g):
    # local mean spacing ~ 2*pi/log(g/2pi); normalize gaps to mean 1
    mid = 0.5*(g[1:]+g[:-1])
    dens = np.log(mid/(2*np.pi))/(2*np.pi)        # zeros per unit
    return (g[1:]-g[:-1])*dens

if __name__=="__main__":
    print("="*80)
    print(" Rodgers-Tao statistics-coupled: the gap object whose uniform upper control = RH (Lambda<=0)")
    print("="*80)
    # sample several height ranges to probe UNIFORMITY (the wall is uniform-in-T)
    blocks = [(1,300),(1000,1300),(10000,10300)]
    allmin=[]
    for (a,b) in blocks:
        g = zeta_ordinates(a,b)
        ng = normalized_gaps(g)
        T = g.mean()
        print(f"\n height ~ {T:8.1f}  (zeros #{a}-{b}):")
        print(f"   normalized gaps: mean={ng.mean():.3f} (target 1)  min={ng.min():.4f}  "
              f"#(<0.3)={np.sum(ng<0.3)}  #(<0.15)={np.sum(ng<0.15)}")
        allmin.append(ng.min())
        # Gate-B 'collision time' proxy for the tightest pair: t_coll ~ (gap)^2 (flow units, schematic)
        print(f"   tightest pair: normalized gap g_min={ng.min():.4f}  ->  backward-collision scale ~ g_min^2 "
              f"= {ng.min()**2:.4f} (smaller => closer to a t=0 birth)")
    print("\n" + "-"*80)
    print(f" min normalized gap across blocks: {np.min(allmin):.4f}")
    print(" Lehmer phenomenon: gaps get arbitrarily small (no positive uniform lower bound on gaps);")
    print(" the zeros never actually collide ON the line (they stay simple real = RH), but come close.")
    print("-"*80)
    print(" THE PRECISE STATEMENT:")
    print("  * Rodgers-Tao Lambda>=0  <= zeros FLUCTUATE (lower tail; unconditional-ish).  DONE.")
    print("  * RH = Lambda<=0         <= NO pair collides for t>0, UNIFORMLY in T  =  a uniform UPPER")
    print("    bound on clustering = the upper tail of pair correlation / no-tight-Lehmer, uniformly.")
    print("  This is OPEN and RH-conditional (Montgomery proven only in a range; uniform upper unknown).")
    print("  => statistics-coupling reaches EXACTLY the B1 pair-correlation wall, upper tail. Same wall.")
    print("="*80)
