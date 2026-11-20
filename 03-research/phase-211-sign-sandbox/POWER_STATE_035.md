# State035 — Scalar rows 1–17 complete at fixed rate

Status: PROVED and audited. Replaces STATE034. Goal active; global sign OPEN. Papers untouched.

## Positivity of the full form

For F_(N,k,u)(s)=s^k/(s+u)^(N+k), at u=63/2, it is proved that:

    W[f_(N,k,u)] > ||f_(N,k,u)||²/40,  1 <= N <= 17, k >= 0.

POWER_BOUNDARY_BALANCE_035 certifies a single terminal N17,k0: ARCH/norm² > −.868, polar/norm² > .911 and modulus of the full arithmetic comb < .002. Hence the terminal has margin > .041. The exact normalised recurrence

    A_N0 = A_N1/(2N) + (2N−1) A_(N+1),0/(2N)

keeps all parts of W. The positive column k1 of034 and this terminal allow descending to N3; rows1,2 were already proved. All k>=1 up to N17 are covered by034. The difference relative to018 is having both real sign data; the recurrence alone does not suffice.

These are individual scalar atoms: not all their linear combinations are certified. The space certificates fixed V12 007 and eight arbitrary poles014 keep their own scope. No new window T is certified, nor is T=log(5)/2 exceeded.

## Specific signed average

POWER_SIGNED_TRANSFORM_035 proves that A_N0 is an average of t_m=T_m/[m(m+1)/2] with an explicit positive law P_(N−1). Its exact tail, uniform bounds and concentration at m of order sqrt(N) are obtained; the variable m(m−1)/(4(N−1)) converges in distribution to Gamma of shape2. The quadratic substitution of the generator reconstructs the weights exactly.

Any fixed adverse prefix has cost explicitly bounded by O(N^−2). This does not control the adverse terms in the moving window nor their magnitudes. The infinite oscillation034 remains valid; positivity of each T_m is not assumed again. The signed arithmetic average remains OPEN.

## Audit and remainder

POWER_BOUNDARY_AUDIT_035 approves both constructions. Rational terminal and symbolic transform verifiers: PASS, reproduced independently three times. The uniform proofs are analytic; no sweep over cases was done.

At fixed rate, from N18 below the cone k>=10000N² remains pending, except the already decided atom N211,k1 032. The variable-rate regions029/034 and other earlier results are kept. The global objective is not closed. The continuation036 addresses compensation in the moving window, with prior consultation of the corpus and an explicit difference from refuted criteria.
