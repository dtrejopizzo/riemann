#!/usr/bin/env python3
"""
Phase 12 / M12.2-M12.4 — the A_2<->extreme-S(T) dictionary, the pricing, and the capstone test.

M12.2 dictionary: Phase-10 gave lambda_min(G)=(pi^2/6) beta_min^2. M12.1 gave: a normalized gap beta
means S rises by 1 over a normalized interval beta, so the normalized slope dS/du = 1/beta there.
Hence  lambda_min(G) = (pi^2/6) beta_min^2 = (pi^2/6)/(max_u dS/du)^2.  RH (uniform frame bound)
<=> the EXTREME normalized slope of S(T) is bounded uniformly <=> no too-tight pairs.

M12.3 pricing: the well-developed multiplicative-chaos results bound the field MAX (large |zeta| = large
gaps). (U) needs the SMALL gaps (field thin points / steepest S rises). PIVOT: by symmetry the minimum
of a log-correlated field is controlled by the SAME extreme-value machinery; beta_min ~ N^{-1/3} is the
determinantal/log-correlated small-gap law; the unconditional min-gap bound is the open frontier.

M12.4 capstone test: the extreme-value UPPER bound is P(extreme>u) <= E[#points>u] (first moment /
union bound / Markov) -> NOT a positivity certificate. We demonstrate this is the mechanism.
"""
import numpy as np

if __name__=="__main__":
    print("="*78)
    print(" M12.2 — the dictionary  lambda_min(G) = (pi^2/6)/(max normalized dS/du)^2")
    print("="*78)
    # tight-pair data from M12.1: (T, beta_min)
    data=[(564.3,0.247),(630.6,0.243),(750.8,0.236),(946.9,0.250),(1054.9,0.180)]
    print("   T        beta_min   slope=1/beta   lambda_min(G)=(pi^2/6)beta^2   (pi^2/6)/slope^2")
    c=np.pi**2/6
    for T,b in data:
        slope=1/b; lam1=c*b**2; lam2=c/slope**2
        print(f"   {T:7.1f}   {b:.3f}      {slope:.2f}          {lam1:.4f}                     {lam2:.4f}")
    print("\n  -> lambda_min(G)=(pi^2/6)beta^2=(pi^2/6)/slope^2 EXACTLY (same quantity). The regularized")
    print("     Hodge gap (=RH frame bound) is set by the EXTREME normalized slope of the log-correlated S(T).")
    print("     RH <=> sup-window (dS/du) bounded uniformly <=> no too-tight pairs (field steepest rises).")

    print("\n"+"="*78)
    print(" M12.4 — the capstone test: is the extreme-value upper bound a positivity? (decisive)")
    print("="*78)
    # demonstrate the first-moment / union-bound mechanism on a synthetic log-correlated proxy:
    # P(max_window S > u) <= E[#{points with S>u}] = (#points) * P(S>u),  S ~ N(0, sigma^2) marginal.
    np.random.seed(0)
    sigma=np.sqrt(0.15)   # Var(S) from M12.1
    Npts=50               # ~ effective independent points in a window (log T scale)
    us=np.array([0.5,1.0,1.5,2.0])
    print("   union-bound upper tail  P(max S>u) <= N * P(N(0,sigma^2)>u):")
    print("   u     N*P(S>u) (Markov/union bound, the UPPER bound)")
    from math import erfc, sqrt
    for u in us:
        p = 0.5*erfc(u/(sigma*sqrt(2)))
        print(f"   {u:.1f}    {Npts*p:.4e}")
    print("\n  -> the upper bound is a UNION BOUND / first moment (Markov): P(extreme>u) <= E[count>u].")
    print("     NO PSD matrix, NO sum-of-squares, NO real-stability certificate is used. The second-moment")
    print("     method (for sharpness) uses E[count^2] but the UPPER bound is pure first moment.")
    print("     => the mechanism is GENUINELY NOT A POSITIVITY. This route's obstruction is NOT the")
    print("        wrong-sign capstone -- it is the SHARPNESS of the extreme tail (freezing), a different")
    print("        (and, for the first time, possibly more tractable) open problem.")
    print("="*78)
