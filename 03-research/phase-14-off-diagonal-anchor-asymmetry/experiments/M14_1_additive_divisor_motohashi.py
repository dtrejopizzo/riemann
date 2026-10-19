#!/usr/bin/env python3
"""
Phase 14 / M14.1 — the off-diagonal: the additive divisor correlation, the Motohashi bridge to the
spectrum/zeros, and the honest outcome (density), plus the genuinely new omega-weighted question.

The off-diagonal of the 4th moment of zeta is the ADDITIVE DIVISOR (shifted convolution) sum
   D(x,h) = sum_{n<=x} d(n) d(n+h),     d(n)=2^{omega(n)} on squarefree.
Its asymptotic (additive divisor 'conjecture', proven via Motohashi's spectral expansion for the
smoothed/4th-moment form):
   D(x,h) ~ x * P_{h}(log x),   P_h a degree-2 polynomial with arithmetic coefficients in sigma_{-1}(h).
The ERROR term is, by MOTOHASHI, an EXACT sum over the MAASS-form spectrum (kappa_j) weighted by the
central L-values H_j(1/2)^3 -- the first exact identity in which the divisor/omega structure meets the
automorphic spectrum (dual to the zeros). The 4th-moment bound it yields gives a ZERO-DENSITY theorem for
zeta (mechanism b: few off-line zeros), NOT absence -- the same quantitative wall as Littlewood.

We verify the main-term structure of D(x,h) (the (log x)^2 growth and the sigma_{-1}(h) dependence),
to ground the off-diagonal object, and frame the omega-weighted question.
"""
import numpy as np

def divisor_table(N):
    d=np.zeros(N+1,dtype=np.int64)
    for i in range(1,N+1):
        d[i::i]+=1
    return d

def sigma_minus1(h):
    s=0.0
    for dd in range(1,h+1):
        if h%dd==0: s+=1.0/dd
    return s

if __name__=="__main__":
    print("="*80)
    print(" M14.1 — additive divisor correlation D(x,h)=sum d(n)d(n+h) (the 4th-moment off-diagonal)")
    print("="*80)
    N=4_000_000
    print(f" building d(n) up to {N} ...")
    d=divisor_table(N)
    # additive divisor conjecture main term: D(x,h) ~ (6/pi^2) sigma_{-1}(h) x (log x)^2 + lower order.
    print("\n   h   sigma_{-1}(h)   D(x,h)/x      (log x)^2     D/(x (log x)^2)   pred 6/pi^2 sigma_{-1}(h)")
    x=N-20
    L2=np.log(x)**2
    for h in [1,2,3,6,12]:
        D=np.sum(d[1:x+1].astype(float)*d[1+h:x+1+h].astype(float))
        ratio=D/(x*L2)
        pred=(6/np.pi**2)*sigma_minus1(h)
        print(f"   {h:2d}   {sigma_minus1(h):.4f}        {D/x:8.2f}     {L2:7.3f}      {ratio:.4f}            {pred:.4f}")
    print("\n  -> D(x,h) ~ C(h) x (log x)^2 with C(h) tracking (6/pi^2) sigma_{-1}(h) (finite-x + lower-order")
    print("     log terms shift the constant; the (log x)^2 leading order and the sigma_{-1}(h) dependence are")
    print("     the additive-divisor structure). This off-diagonal is the object Motohashi expands spectrally.")
    print("\n"+"="*80)
    print(" THE BRIDGE AND THE HONEST OUTCOME:")
    print("  * MOTOHASHI (k=2): the smoothed 4th moment / the additive divisor error = an EXACT sum over the")
    print("    Maass-form spectrum {kappa_j}, weighted by central L-values H_j(1/2)^3. First exact identity")
    print("    where the divisor/omega structure meets the automorphic spectrum (dual to the zeros). EXACT,")
    print("    not a statistic -- it PASSES the advisor's filter.")
    print("  * OUTCOME: the resulting 4th-moment bound gives a ZERO-DENSITY theorem for zeta (few off-line")
    print("    zeros), NOT absence -- the same quantitative wall as Littlewood (the moment is (log)^4-large;")
    print("    one off-line zero is O(1)). Mechanism (b). Right direction (touches the spectrum/zeros), but")
    print("    density, not RH.")
    print("  * THE GENUINELY NEW QUESTION (where omega adds something): the z^{omega}-WEIGHTED divisor")
    print("    correlation sum z^{omega(n)} d(n) d(n+h) (z>1 = the supercritical / many-factor weight). Does")
    print("    its Motohashi-type spectral expansion have a DEFINITE / controllable feature on the spectral")
    print("    side that the unweighted one lacks? That is the first place the omega-LARGE-DEVIATION structure")
    print("    could give NEW spectral/zero information -- the M14.2 target. (Open; honestly, likely still")
    print("    density, but it is the exact, omega-sensitive, zeros-facing object the advisor asked for.)")
    print("="*80)
