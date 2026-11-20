# State019 — Signed contact pattern, without global closure

Status: PROVED partial results; global sign OPEN. Goal active. Papers untouched. Replaces STATE018 as the current summary.

## Target and coverage of the full form

The scalar bridge017 still holds: W>=0 for ALL H_(N,k)=s^k/(s+u)^(N+k) at u31.5 suffices. The full rows N1,2,3 and the cone N>=2,k>=10000N² are proved. The eight arbitrary poles and the fixed block12 also remain valid. This round does NOT extend that coverage of W nor certify a new window T>log(5)/2.

The audit018 is complete: POWER_TABLE_AUDIT_018. It approves rows23, the exact LOW_TABLE budget and the arcsine model that keeps the structural positive regions but has a negative interior entry. That model is not W; it shows that the descent must use more arithmetic information.

## New signed result on the real comb

POWER_ARITHMETIC_DIFFERENCES_019 proves that the autocorrelation of H_(N,1) has exactly one simple positive root in x=u t. It is positive before and negative after. For N>=3, sqrt(2N−3)<chi_N<(1+sqrt(8N−11))/2; the extremes N1,2 are computed explicitly.

Since u log2>21 for u>=31.5, ALL arithmetic contacts lie after the root for 1<=N<=211. Hence the FULL comb is strictly positive in those cases. For k0 the full comb is strictly negative for ALL N. Thus a proved sign transition appears between k0 and k1, not a numerical observation nor a truncated sum.

The proof uses explicit coefficients, Descartes and two elementary recurrences of reverse Bessel polynomials. The unique frontier holds for ALL N; the threshold211 refers only to the corollary placing all contacts on the positive side. W>=0 is not deduced: ARCH and polar remain in the pending balance. The proof was read and the Fraction verifier reproduced PASS; an independent review approved it.

## Signed mean of dilations and limit of its inversion

POWER_SIGNED_MEAN_019 applies the known divisor identity to the positive kernel of LOW018. B(x)=sum_(m<=x)E0(x/m)=log(floor(x)!)−xH_floor(x)+floor(x) satisfies B(x)<=−(1−log2)(x−1). Integrating it gives an arithmetic mean of dilations strictly negative for all N>=2. It is not the original mean ERR.

Exact recovery requires h_N(x)=sum mu(m)mH_N(mx), with the Jacobian m. The first three terms at x1 are <-19/256 for N>=2^17. This refutes positivity of each prefix, NOT the sign of the full inverse, whose remainder is uncontrolled. The Euler/Möbius grouping already existed in the corpus; the specific scope is the signed mean and the prefix falsifier for this kernel.

Both memos were audited in POWER_SIGNED_AUDIT_019. Normalisations, endpoints, Fubini, constants and the scope of the prefix were also reviewed. No numerical campaign was done.

## Next obligation

A quantitative estimate combining the signed comb with ARCH and polar at variable orders is missing. The favourable sign of the comb alone does not compensate a deficit without measuring its size. Do not extrapolate positivity of dilations to ERR nor prefixes to the full inverse. The lower region of the table remains open and the objective is neither completed nor blocked.
