#!/usr/bin/env python3
"""
Phase 14 / M14.2 — IS THE z^omega WEIGHT A NON-TRIVIAL SPECTRAL MODIFICATION? (from the spectral side)

The input to the Motohashi/Kuznetsov machine for the z-weighted shifted convolution D_z(x,h)=
sum z^{omega(n)} d(n) d(n+h) is the multiplicative function a(n)=z^{omega(n)} d(n). Its Dirichlet series
controls the spectral weights. Compute the LOCAL (Euler) factor:

   sum_a z^{omega(p^a)} d(p^a) x^a = 1 + sum_{a>=1} z*(a+1) x^a = 1 + z * x(2-x)/(1-x)^2
                                   = [1 + 2(z-1)x + (1-z)x^2] / (1-x)^2 ,    x=p^{-s}.

So   sum_n a(n)/n^s = zeta(s)^2 * G_z(s),   G_z(s) = prod_p [1 + 2(z-1)p^{-s} + (1-z)p^{-2s}].
The leading 1/p^s coefficient of G_z is 2(z-1), so  G_z(s) ~ zeta(s)^{2(z-1)} * H_z(s)  near s=1,
hence  sum a(n)/n^s ~ zeta(s)^{2z} H_z(s)  (pole order 2z).

THE BINARY QUESTION: is G_z spectrally trivial (G_z=1 <=> z=1) or not?
 - G_z != 1 for z != 1: a NON-TRIVIAL extra Euler factor appears.
 - G_z ~ zeta^{2(z-1)} is a POWER OF zeta -> for NON-INTEGER z it has BRANCH POINTS at the zeta ZEROS;
   for integer z it is a zeta-power (the zeros enter as zeros/poles). EITHER WAY the spectral weight
   carries the zeta zeros. => the z^omega weight is NOT spectrally invisible.

We verify (i) the exponent of sum_{n<=N} a(n)/n is 2z (the zeta^{2z} structure), and (ii) G_z's local
factor roots (the Satake-like parameters the spectral side would see), confirming non-triviality.
"""
import numpy as np

def omega_d_table(N):
    """omega(n) and d(n) for n=1..N."""
    om=np.zeros(N+1,dtype=np.int32); d=np.zeros(N+1,dtype=np.int64)
    for i in range(1,N+1): d[i::i]+=1
    is_c=np.zeros(N+1,bool)
    for p in range(2,N+1):
        if not is_c[p]:
            om[p::p]+=1; is_c[p*p::p]=True if p*p<=N else False
    return om,d

if __name__=="__main__":
    print("="*82)
    print(" M14.2 — does z^omega induce a NON-TRIVIAL spectral modification? (the binary question)")
    print("="*82)
    N=3_000_000
    print(f" building omega(n),d(n) up to {N} ...")
    om,d=omega_d_table(N); n=np.arange(N+1)

    print("\n (i) exponent of sum_{n<=N} z^omega(n) d(n)/n  ~ (log N)^{2z}  (the zeta^{2z} pole order):")
    print("    z      fitted exponent     2z (predicted)    G_z = zeta^{2(z-1)} factor")
    Ns=np.array([3e4,1e5,3e5,1e6,3e6])
    for z in [0.5,1.0,1.5,2.0]:
        w=(z**om.astype(float))*d.astype(float)
        sums=np.array([np.sum(w[2:int(NN)+1]/n[2:int(NN)+1]) for NN in Ns])
        expo=np.polyfit(np.log(np.log(Ns)), np.log(sums),1)[0]
        extra = "TRIVIAL (G_1=1)" if z==1 else f"NON-TRIVIAL (~zeta^{2*(z-1):.1f})"
        print(f"   {z:4.1f}    {expo:6.2f}              {2*z:4.1f}            {extra}")

    print("\n (ii) the extra Euler factor G_z local: 1 + 2(z-1)x + (1-z)x^2 = (1-alpha x)(1-beta x):")
    print("    z      alpha          beta         alpha*beta=1-z   (Satake-like params the spectrum sees)")
    for z in [0.5,1.0,1.5,2.0,3.0]:
        # roots of t^2 - 2(1-z) t + (1-z) = 0  for (1-alpha x)(1-beta x): alpha+beta=2(1-z), alpha*beta=(1-z)
        disc=(1-z)**2-(1-z)
        if disc>=0:
            a=(1-z)+np.sqrt(disc); b=(1-z)-np.sqrt(disc)
            print(f"   {z:4.1f}    {a:+.4f}       {b:+.4f}      {1-z:+.4f}")
        else:
            a=complex(1-z, np.sqrt(-disc))
            print(f"   {z:4.1f}    {a.real:+.3f}{a.imag:+.3f}i (complex pair)   {1-z:+.4f}")
    print("\n"+"-"*82)
    print(" THE BINARY ANSWER:  z^omega is a NON-TRIVIAL spectral modification.")
    print("  * For z != 1 a genuine extra Euler factor G_z(s) = prod_p[1+2(z-1)p^-s+(1-z)p^-2s] appears;")
    print("    G_z = 1 iff z = 1. So the weight is NOT spectrally invisible.")
    print("  * G_z ~ zeta(s)^{2(z-1)} is a POWER OF zeta. For non-integer z it has BRANCH POINTS at the")
    print("    zeta ZEROS; the spectral weight in the Motohashi/Kuznetsov expansion therefore CARRIES THE")
    print("    ZETA ZEROS. This is the first omega-structure in the program that is NOT invisible to the")
    print("    spectral/zeros side -- it touches the zeros through the zeta^{2(z-1)} factor.")
    print("  * HONEST: G_z is a GL(1)/Eisenstein-type (zeta-power) factor, not new cuspidal structure; it")
    print("    REWEIGHTS the spectrum by a zeta-power carrying the zeros. Whether that yields NEW zero-info")
    print("    (vs re-expressing) is the deeper M14.3 question. But the binary criterion is met: NON-TRIVIAL.")
    print("="*82)
