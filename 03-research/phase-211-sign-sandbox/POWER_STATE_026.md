# State026 — Uniform cutoff and signed joint balance

Status: partial results PROVED and audited; global sign of W OPEN. Replaces STATE025 as the current summary. Goal active; papers untouched.

## Uniform cutoff, without extrapolating certificates

POWER_UNIFORM_CUTOFF_026 proves for d=N−1>=2 two cutoffs:

    t_J=d(d+220)/(330d+6300),
    M=u²/(2d−1), Q=sqrt(9/4+M), t_R=2dQ/(u²−Q²), u=63/2.

For t>=min(t_J,t_R), D_N'/D_N<=30. Hence the FULL Möbius sum satisfies K_N(x)>=x^-32 D_N(logx)/4>0 when logx exceeds that cutoff. Both cutoffs are d/330+O(1), improving the earlier d/30. The case N2 is treated through the affine polynomial. Jensen on the coefficients and elementary Riccati barriers provide uniform proofs, not a campaign over rows.

Moreover K_N(x)>0 for ALL 2<=N<=129 and x>=exp(2/3). Monotonicity of the formula and two rational endpoint checks prove the range. All integer cells contained in the tail have favourable balance and an explicit gamma bound. The interior remains pending and grows with N.

## The pending comparison is not resolved by ERR129

POWER_ARCH_CELL_026 proves ARCH_sharp129/norm²<−.81. The benefit guaranteed by ERR129<−.66 does not suffice to certify W129: adding only .66 leaves a comparator less than −.15. It is NOT an upper bound for W nor a counterexample; the real benefit may be larger.

The exact grouping W[g_N]/norm²=int K_N(t)Omega(t)dt keeps ARCH_sharp and all arithmetic terms. However Omega(3/2)<−.1, proved exactly. Only universal pointwise positivity of that weight is refuted. The restrictions on K_N coming from the gamma autocorrelation are not eliminated and may control the signed pairing.

## Evidence and scope

POWER_ARCH_CELL_AUDIT_026 approves both proofs, including grouped Fubini, Riccati barriers and full tails. Both texts were read and the two Fraction verifiers reproduced: PASS. Uniformity is not attributed to the scripts: the proofs provide it.

The coverage of W remains unchanged: rows N1,2,3 for all k, cone k>=10000N², eight arbitrary poles and fixed block12. The scalar bridge017 requires ALL N,k. There is no new certified window T nor closure of the global sign.

## Continuation027

Look for an inequality of the joint balance that uses the real gamma form and its curvature, keeping cancellations. Isolated integral or discrete masses and exterior positivity do not replace interior control. Two constructions continue, with independent review; universal pointwise positivity of K or Omega is not retried.
