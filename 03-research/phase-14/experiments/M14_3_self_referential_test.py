#!/usr/bin/env python3
"""
Phase 14 / M14.3 — THE BINARY TEST: is G_z spectrally SELF-REFERENTIAL (only zeta-factors) or does it
introduce NEW irreducible spectral structure?

G_z(s) = prod_p (1 - alpha p^{-s})(1 - beta p^{-s}),  with alpha+beta=2(1-z), alpha*beta=1-z
CONSTANT (independent of p, because z^{omega(n)} depends only on the COUNT of primes, not on WHICH).

A degree-2 Euler product with CONSTANT Satake parameters is zeta-ISOBARIC:
   log G_z = -sum_p sum_k (alpha^k+beta^k)/k p^{-ks}
           = -sum_k (alpha^k+beta^k)/k P(ks),   P = prime zeta,   P(ks)=sum_m mu(m)/m log zeta(kms)
   => G_z(s) = prod_{N>=1} zeta(Ns)^{c_N},   c_N = -(1/N) sum_{k|N} (alpha^k+beta^k) mu(N/k).
So G_z is ENTIRELY a product of zeta(Ns)-powers. NO new irreducible L-function. SCENARIO A.

The structural reason: omega(n) counts primes UNIFORMLY (prime-blind); a prime-blind weight has constant
Satake parameters, hence a zeta-isobaric spectral signature -- it cannot produce a prime-DISTINGUISHING
(zero-distinguishing) L-function. This is the spectral twin of the explicit-formula omega-blindness.

We (i) compute the c_N, (ii) verify G_z = prod zeta(Ns)^{c_N} numerically against the direct Euler product.
"""
import numpy as np

def divisors(N):
    return [k for k in range(1,N+1) if N%k==0]

def mobius(m):
    if m==1: return 1
    res=1; mm=m; p=2
    while p*p<=mm:
        if mm%p==0:
            mm//=p
            if mm%p==0: return 0   # square factor
            res=-res
        p+=1
    if mm>1: res=-res
    return res

def satake(z):
    # roots of t^2 - 2(1-z) t + (1-z): alpha,beta with alpha+beta=2(1-z), alpha*beta=1-z
    disc=(1-z)**2-(1-z)
    s=np.sqrt(complex(disc))
    return (1-z)+s, (1-z)-s

def cN(z, N):
    a,b=satake(z)
    s=0
    for k in divisors(N):
        s += (a**k + b**k) * mobius(N//k)
    return -(1.0/N)*s

def zeta_num(s, terms=200000):
    n=np.arange(1,terms+1)
    return np.sum(n.astype(float)**(-s))   # crude Dirichlet sum (s>1)

def Gz_direct(z, s, P=200000):
    # direct Euler product over primes p<=P
    sieve=np.ones(P+1,bool); sieve[:2]=False
    for p in range(2,int(P**0.5)+1):
        if sieve[p]: sieve[p*p::p]=False
    primes=np.nonzero(sieve)[0].astype(float)
    x=primes**(-s)
    return np.prod(1 + 2*(z-1)*x + (1-z)*x**2)

if __name__=="__main__":
    print("="*82)
    print(" M14.3 — is G_z self-referential (zeta-factors only) or new spectral structure? BINARY TEST")
    print("="*82)
    print("\n the zeta-power exponents c_N of  G_z(s)=prod_N zeta(Ns)^{c_N}:")
    print("   z       c_1            c_2            c_3            c_4")
    for z in [0.5, 1.5, 2.0, 3.0]:
        cs=[complex(cN(z,N)) for N in (1,2,3,4)]
        def fmt(c): return f"{c.real:+.4f}" + (f"{c.imag:+.4f}i" if abs(c.imag)>1e-9 else "")
        print(f"   {z:4.1f}   {fmt(cs[0]):14s} {fmt(cs[1]):14s} {fmt(cs[2]):14s} {fmt(cs[3]):14s}")
    print("   (c_1=2(z-1), c_2=-2z(z-1), ... all real, finite, explicit -- pure zeta-power exponents.)")

    print("\n verify  G_z(s) = prod_N zeta(Ns)^{c_N}  vs the direct Euler product (s=2.0):")
    s=2.0
    print("   z      G_z (direct Euler)     prod zeta(Ns)^{c_N} (N<=8)     rel.err")
    for z in [0.5,1.5,2.0]:
        direct=Gz_direct(z,s)
        prodz=1.0
        for N in range(1,9):
            prodz *= zeta_num(N*s)**(cN(z,N).real)
        print(f"   {z:4.1f}   {direct:.8f}          {prodz:.8f}            {abs(direct-prodz)/abs(direct):.2e}")
    print("\n"+"-"*82)
    print(" THE BINARY ANSWER:  THE omega-WEIGHT IS SPECTRALLY SELF-REFERENTIAL.")
    print("  * G_z(s) = prod_N zeta(Ns)^{c_N} EXACTLY (constant Satake parameters => zeta-isobaric).")
    print("    The z != 1 vs z = 1 ratio is expressible COMPLETELY via zeta-factors. No new irreducible")
    print("    spectral weight appears. The zeta-zeros enter ONLY because G_z is built from zeta-powers.")
    print("  * STRUCTURAL REASON: omega(n) counts primes UNIFORMLY (prime-blind); a prime-blind weight has")
    print("    CONSTANT Satake parameters, hence a zeta-isobaric signature -- it cannot produce a prime-")
    print("    DISTINGUISHING (zero-distinguishing) L-function. This is the spectral twin of the explicit-")
    print("    formula omega-blindness (omega=1 on prime powers).")
    print("  => Per the audit criterion: CLOSE this RH line. The omega-structure, exact and spectral though")
    print("     it is, reduces to zeta itself (self-referential) and gives no new information on the zeros.")
    print("="*82)
