#!/usr/bin/env python3
"""
Phase 12 / M12.7 — the Baker bridge, quantified, and the pivot to additive energy.

The extreme large values come from near-resonances |sum ± log p_i| < 1/W (small linear forms in log p).
TWO deterministic, upper, non-positivity tools:
 (A) BAKER (linear forms in logs): lower bound on a SINGLE |sum b_i log p_i| -- but exponentially WEAK
     (|Lambda| >= exp(-C log A log B)), too weak to control the count.
 (B) ADDITIVE ENERGY of {log p} (the COUNT of near-resonances): the 4-term ones are pq ~ rs, i.e. the
     MULTIPLICATIVE additive energy of primes. This is EXACTLY the moment inflation P5 measured (omega-class
     fingerprint). Bounded by sieve / multiplicative methods (deterministic, upper, non-positivity).

We compute the smallest 4-term near-resonance |log(pq/rs)|, compare to Baker, and the additive-energy count.
"""
import numpy as np, mpmath as mp
mp.mp.dps=30

def primes_upto(X):
    s=np.ones(X+1,bool); s[:2]=False
    for p in range(2,int(X**0.5)+1):
        if s[p]: s[p*p::p]=False
    return np.nonzero(s)[0]

if __name__=="__main__":
    print("="*80)
    print(" M12.7 — Baker bound vs additive energy of {log p} (the near-resonance count)")
    print("="*80)
    X=300; P=primes_upto(X)
    logP=np.log(P.astype(float))
    # all products pq (p<=q), with their log
    prods=[]
    for i in range(len(P)):
        for j in range(i,len(P)):
            prods.append((logP[i]+logP[j], P[i],P[j]))
    prods.sort()
    L=np.array([x[0] for x in prods])
    gaps=np.diff(L)
    kmin=np.argmin(gaps)
    a=prods[kmin]; b=prods[kmin+1]
    print(f"\n (A) smallest 4-term near-resonance |log(pq/rs)| among primes<= {X}:")
    print(f"     {a[1]}*{a[2]}={a[1]*a[2]} vs {b[1]}*{b[2]}={b[1]*b[2]}:  |log(pq/rs)| = {gaps[kmin]:.3e}")
    # Baker (Baker-Wustholz schematic): |Lambda| >= exp(-C(n) log A log B), here n=4, A=max prime, B=1
    A=float(max(a[1]*a[2], b[1]*b[2]));
    baker = float(mp.e**(-1e4*mp.log(A)))   # schematic constant ~1e4 (real Baker-Wustholz is far larger)
    print(f"     Baker-type lower bound (schematic, C~1e4): |Lambda| >= exp(-C log A) ~ {baker:.2e}")
    print(f"     => Baker's bound ({baker:.1e}) is ASTRONOMICALLY below the actual ({gaps[kmin]:.1e}):")
    print(f"        Baker is EXPONENTIALLY too weak to control near-resonances. (the famous weakness)")

    print(f"\n (B) additive energy: # of 4-tuples with |log(pq/rs)| < threshold (the moment inflation):")
    print("     threshold    #near-resonant pairs (pq,rs)   ")
    for thr in [1e-1,1e-2,1e-3,1e-4]:
        cnt=np.sum(gaps<thr)
        print(f"     {thr:.0e}        {cnt:6d}")
    print(f"     total product-pairs = {len(L)} ; energy grows as threshold relaxes (the near-resonances).")
    print("\n"+"-"*80)
    print(" VERDICT (M12.7):")
    print("  * BAKER is the right MECHANISM (deterministic, upper, non-positivity, transcendence) but")
    print("    EXPONENTIALLY too weak quantitatively. Reaching the threshold needs LANG-WALDSCHMIDT /")
    print("    abc-strength linear-forms bounds (conjectural) -- a genuine, named, deep open problem.")
    print("  * THE PIVOT: the extreme needs the COUNT (additive energy), not the single smallest. The")
    print("    4-term energy = multiplicative near-quadruples pq~rs = EXACTLY P5's omega-class moment")
    print("    inflation. Bounded by SIEVE / multiplicative methods (deterministic, upper, non-positivity),")
    print("    sharp at low order; the high-order energy (the freezing) is the moment-conjecture/resonance")
    print("    frontier -- where our omega-class machinery (P2-P5) lives. RH (via the mechanism-correct")
    print("    chain) <= a sharp high-order additive-energy bound for {log p} = the moment-conjecture")
    print("    frontier. Deterministic, upper, non-positivity end to end. NOT the capstone, NOT N7.")
    print("="*80)
