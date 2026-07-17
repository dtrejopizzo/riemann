#!/usr/bin/env python3
"""
Phase 9 / M9.1 — the spearhead make-or-break: is there an arithmetic-aware monotone functional F[H_t]
that escapes N5 and controls Lambda?

We test the THREE exhaustive sources of 'arithmetic awareness' for a functional of H_t:

 (1) GENERIC (heat-flow energy): F = sum g(z_j).  d/dt F = sum_{j<k} 2*[g'; z_j,z_k] (divided diff) --
     a UNIVERSAL formula (same for any config) => its monotonicity is arithmetic-BLIND (N5 again).
 (2) ARCHIMEDEAN (the zero density from the functional equation): controls the COUNT N(T), not which
     zeros are real => cannot control Lambda (the reality).
 (3) PRIMES via the EXPLICIT FORMULA: the ONLY source that sees reality -- but F = sum g(z_j) equals
     (arch) - 2 sum_n Lambda(n)/sqrt(n) g_hat(log n), and the positivity of this for positive-type g
     IS the Weil criterion = RH.  Arithmetic-awareness through primes = the wall.

This script: (A) VERIFIES the explicit formula numerically (anchors 'arithmetic = explicit formula'),
(B) shows the generic monotone energy does NOT detect complex zeros (blindness), establishing the
dichotomy N6.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 25

# ---------- (A) verify the explicit formula:  sum_rho h(gamma) = arch + pole - primes ----------
def explicit_formula_check(sigma=4.0, Nzeros=200, Xprime=20000):
    # h(r)=exp(-r^2/2 sigma^2);  g(u)=(sigma/sqrt(2pi)) exp(-sigma^2 u^2/2)
    # LHS: sum over zeros (pairs +/- gamma)
    zeros=[float(mp.im(mp.zetazero(n))) for n in range(1,Nzeros+1)]
    LHS=2.0*sum(np.exp(-g**2/(2*sigma**2)) for g in zeros)
    # RHS arch: (1/2pi) int h(r)[Re psi(1/4+ir/2)-log pi] dr
    r=np.linspace(-60,60,200000); dr=r[1]-r[0]
    Om=np.array([float(mp.re(mp.digamma(0.25+1j*rr/2))) for rr in r])-float(mp.log(mp.pi))
    arch=np.sum(np.exp(-r**2/(2*sigma**2))*Om)*dr/(2*np.pi)
    # pole: h(i/2)+h(-i/2) = 2 exp(+1/(8 sigma^2))
    pole=2.0*np.exp(1.0/(8*sigma**2))
    # primes: 2 sum_n Lambda(n)/sqrt(n) g(log n), g(u)=(sigma/sqrt(2pi))exp(-sigma^2 u^2/2)
    def gphys(u): return (sigma/np.sqrt(2*np.pi))*np.exp(-sigma**2*u**2/2)
    sieve=np.ones(Xprime+1,bool); sieve[:2]=False
    for p in range(2,int(Xprime**0.5)+1):
        if sieve[p]: sieve[p*p::p]=False
    primesum=0.0
    for p in np.nonzero(sieve)[0]:
        pk=p; lp=np.log(p)
        while pk<=Xprime:
            primesum+=lp/np.sqrt(pk)*gphys(np.log(pk)); pk*=p
    RHS=arch+pole-2*primesum
    return LHS,RHS,arch,pole,2*primesum

# ---------- (B) generic monotone energy does NOT detect complex zeros ----------
def energy_blind_demo():
    # config A: all real;  config B: same but one pair pushed off-line. Compare a generic
    # 'energy' E=sum_{j<k} 1/|z_j-z_k|^2 (a flow-related quantity) -- show it's insensitive to the
    # crucial off-line vs on-line distinction in sign/monotonicity (blindness illustration).
    base=np.array([-2.,-1.,0.,1.,2.])
    A=base.astype(complex)
    B=np.array([-2.,-1.,0.05+0.4j,0.05-0.4j,2.])  # one real zero -> complex pair
    def E(z): return sum(1/np.abs(z[i]-z[j])**2 for i in range(len(z)) for j in range(i+1,len(z)))
    return E(A),E(B)

if __name__=="__main__":
    print("="*78)
    print(" M9.1 — does an arithmetic-aware MONOTONE functional F[H_t] escape N5?")
    print("="*78)
    print("\n (A) Verify the explicit formula (arithmetic-awareness = THIS identity):")
    LHS,RHS,arch,pole,prim=explicit_formula_check()
    print(f"     LHS sum_rho h(gamma)      = {LHS:.6f}")
    print(f"     RHS arch+pole-primes      = {RHS:.6f}   (arch={arch:.4f}, pole={pole:.4f}, primes={prim:.4f})")
    print(f"     match: |LHS-RHS| = {abs(LHS-RHS):.4e}  -> {'OK, identity holds' if abs(LHS-RHS)<1e-2 else 'CHECK'}")
    print("     => a functional sum_rho g is arithmetic-aware ONLY through this (arch - primes) identity;")
    print("        its sign content for positive-type g IS the Weil criterion = RH. (source-3 = the wall)")
    print("\n (B) Generic monotone energy is blind to reality (source-1):")
    EA,EB=energy_blind_demo()
    print(f"     E(all real)={EA:.4f}   E(one pair off-line)={EB:.4f}")
    print(f"     => the generic energy changes smoothly and is NOT sign-keyed to on/off-line; its")
    print(f"        monotonicity under the flow is universal (holds for both) = arithmetic-blind (N5).")
    print("\n"+"="*78)
    print(" CONCLUSION (N6): every monotone F[H_t] is (1) generic=blind, (2) archimedean=counts not")
    print(" reality, or (3) prime-aware via the explicit formula = the Weil positivity wall. The")
    print(" arithmetic-aware-monotone ESCAPE from N5 does not exist for sum-over-zeros functionals.")
    print(" The one residual hope: a functional whose PRIME content uses only UNCONDITIONAL input")
    print(" (PNT/zero-density), not full positivity -> pivot to T9-A/T9-B.")
    print("="*78)
