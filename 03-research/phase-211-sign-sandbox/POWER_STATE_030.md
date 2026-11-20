# State030 — Compensation of an interior block at fixed rate

Status: partial results PROVED and audited. Replaces STATE029. Goal active, global sign OPEN, papers untouched.

## Real arithmetic block, uniform at large orders

POWER_INTERIOR_SCALE_030 transforms the joint representation exactly, via divisor inversion, into

    W[g_N]/norm² = int_1^infinito G_N(x) H(x)dx,
    G_N=x^-1/2[(3/2)rho_N(logx)−rho_N'(logx)]>0,
    H(x)=1+[log((x+1)/(x−1))−gamma−log(4pi)−1
                            −2sum_(q<=x)qLambda(q)]/x².

The logarithmic singularities at integers greater than1 cancel, keeping the real arithmetic jumps. The identity alone gives no sign.

At FIXED u=63/2 one proves, for ALL N>=2^20,

    int_1^(9/4) G_N(x)H(x)dx >1/100.

The block contains the adverse contact2. The local comparison with G_*=(3/2)x^-1/2 has error<=7M2/4, M2=u²/(2N−3). The main integral is computed exactly, includes Lambda(2), and exceeds1/50; the integrated error is<1/200. No campaign over orders is evaluated. The remainder from9/4 to infinity remains without sign control: positivity of total W is not claimed.

It is also proved that the ordinary primitive and the primitive weighted by x² of H up to5/2 are negative. The real monotonicity of G_N at large orders does not suffice for the positive-primitive criterion. The favourable block is proved using its real magnitude, not by assuming that false premise.

## Gamma–Gaussian comparison with explicit cost

POWER_GAMMA_BALANCE_030 proves for ALL N>=2 at fixed rate

    0<A_sharp(EV)−ARCH_sharp[g_N]/norm²
      <=.5[psi(N−.5)−log(N−1.5)]<1/[2(N−1.5)].

The remainder weight L_N is that of the real inverse gamma law. Its moment int L_N/a² is computed exactly, and K_sharp<=1/t controls the negative curvature. It is a constructive O(1/N) estimate, valid even at N2 without finite variance of V.

The comparison of the FULL forms without cost is false for the real law N2: Wgamma/norm²<.85 and G_W(EV)>.875, so the integrated gap is<−1/40. This does not mean W negative: that row already has proved positivity. The signed arithmetic fluctuation must still be compensated together with the sharp loss; the Gaussian comparison alone does not decide it.

## Evidence and remaining obligation

POWER_INTERIOR_AUDIT_030 approves both memos, including inversion/Fubini, exact primitive J, contact2, uniform limits and the Gaussian comparison. The proofs were read and the two exact verifiers reproduced: PASS. The proofs provide uniformity in N; the scripts certify constants.

There is no new coverage of total W nor window T. At u31.5 rows N1..5 for all k and cone k>=10000N² remain; N>=6 below the cone remains. The regions029 of increasing rates remain valid with their explicit bridge limit. A tail of another representation cannot be added without accounting for its boundaries.

The next obligation is to control the remainder of the pairing G_N H at fixed rate or the arithmetic difference in the gamma–Gaussian comparison. The favourable integrated block and the sharp cost are concrete tools; neither replaces that obligation.
