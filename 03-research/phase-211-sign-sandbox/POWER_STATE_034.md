# State034 — Full rows up to12 at fixed rate and oscillation of the Abel criterion

Status: two results PROVED and audited. Replaces STATE033. Goal active, global sign OPEN, papers untouched.

## New uniform region of positivity of full W

POWER_DIVISOR_COMPARISON_034 proves for ALL integers N>=3,k>=1 and rates u>=63/2 with u²>=225N/4:

    W[f_(N,k,u)] > ||f_(N,k,u)||²/40,
    F_(N,k,u)(s)=s^k/(s+u)^(N+k).

For k>=2 the margin is greater than3/20. At k1 the favourable comb019 is kept and ARCH−|polar|>.026 is proved; each odd lower comparator033 is positive. From k2 on, the beta increment of ARCH allows paying an absolute bound of the WHOLE comb through the two opposite weights029. The sign of the comb at k1 is not extrapolated to other columns.

The proof is analytic and uniform, not a sweep over N,k,u. The contraction033 is not responsible for compensating a negative ARCH in this region: here ARCH−|polar| is already positive. Case211 of032 keeps its separate proof with much finer cancellation.

## Exact coverage when combining earlier sources

At FIXED rate u0=63/2, the new condition reaches ALL N<=17 and k>=1. For k0,N<=12, the datum g_N=y^(N−1)e^-u0y/(N−1)! belongs to the block V12 proved in ARITHMETIC_BLOCK007. Hence ALL rows N1..12 for ALL k>=0 at u0 are complete. For N13..17 only k0 remains pending.

For ALL rates u>=u0, k0,N<=8 belongs to the space of eight repeated poles of SIGNED_TRANSFER014; together with the new region, rows N1..8 for ALL k>=0 and ALL u>=u0 are complete. The fixed certificate V12 is not extended to variable rates at N9..12.

These statements refer to the indicated scalar atoms. They do not certify arbitrary linear combinations of all the new atoms nor a window T. The already proved quadratic-form blocks007/014 keep their own scope.

## Abel criterion033 uniformly refuted

POWER_WEIGHTED_COEFFICIENT_034 proves that the real sequence T_m of033 has strictly positive and negative terms at arbitrarily large indices. Not only does the premise T_m>=0 for all m fail: excepting a finite number of indices does not suffice either.

The proof computes no new m. It uses the already audited positive cosh representation001 to continue the exponential functional E(v) real-analytically and obtain its parity. The generator F(z)=sum T_m z^(m−1) is symmetric around1 and decays as real z tends to infinity. An elementary lemma on positive series, proved in the text, shows that eventually one-signed coefficients would force the series to be entire. An odd derivative at1 above the exceptions would then force a zero tail, turning F into a polynomial; the decay contradicts F(0)=T1>1/8.

This is a refutation of the specific sufficient criterion, not a counterexample to W. The exact gamma mixture of033 remains valid: its weights may compensate the signs of T_m. It is not declared impossible to control those combinations by another mechanism.

## Evidence and remaining obligation

POWER_COMPARISON_AUDIT_034 approves both memos, the extension to k>=2 and the space inclusions007/014. Both proofs were reviewed and the rational verifier of the region reproduced: PASS. The oscillation is proved analytically, without a numerical certificate of indices nor unproved hypotheses on the series at1.

At u31.5, outside the cone k>=10000N² and the already decided atom211,k1, k0 forN>=13 remains and, fromN18, the columns below the cone not covered. There is no closure of the global sign nor a new certified window T. The continuation must keep the arithmetic compensation of the real weights; do not retry componentwise positivity of T_m, now refuted.
