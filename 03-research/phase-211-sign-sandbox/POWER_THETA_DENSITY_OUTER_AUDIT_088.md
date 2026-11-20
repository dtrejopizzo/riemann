# POWER_THETA_DENSITY_OUTER_AUDIT_088 — Independent audit

Status: **APPROVED / PROVED for ALL t>=1.** Source `POWER_THETA_DENSITY_OUTER_088.md` and verifier read in full; independent reproduction exit0 with four blocks PASS and the same hash as the earlier runs:

    d2b1e479295cbf9eda602a2786b657cab5c83db1c74dee9a7d00b751723fc8f4

Papers untouched; finite rational/polynomial proof, without mesh or sampled theta values.

## First mode and normalization

The four densities of the first mode are pi g0 F, while the factor removed for the ratios is tPhi1=t pi g0 b. The Wronskian identity when factoring a common function gives exactly W4,0=W(F)/(tb)^4. D=partial_t+2y partial_y acts on the polynomial F; the derivatives of g0 are eliminated by the general identity, not improperly omitted.

The verifier generates the recurrence B0..3, the 24-permutation determinant and P=−W(F)/(16y²) with Fraction. The substitution t=1+T, y=21+Y in P−4096t²y8 has exactly 27 positive coefficients including the constant. Therefore the sign holds on the WHOLE independent quadrant t>=1, y>=21. b<2y fixes G0<−4096t²y6 with the correct orientation. The real datum satisfies y>21 by pi>3, exp2>7.

## Complete theta tail up to V6

The cancellation of logy before differentiating logrm is valid. Each coefficient of the difference of log(1−h/m²) and log(1−h) contains 1−m^(−2n), of modulus <=1; this pays simultaneously for derivatives 1..6 via the Euler sum n5h^n<1 on h<=1/14. The complete Bell polynomials with arguments 2^(j+1)z give the indicated polynomial B6, less than 5000z6 from z>=63. The lower orders are dominated because B_(j+1)>=x1 Bj with x1=4z>=1.

Extending to ALL integers a>=3 loses no contribution. The successive ratio and the monotonicity of y6exp(−3y) pay for the WHOLE tail by E=62523502209/6553600000000000000000. The log6 coefficients are exactly (k−1)!S(6,k); their sum with powers of E <2E also pays for lower orders. No sign of that error is presupposed.

The jets of the first mode up to 6 stay in modulus <68y (and for p<2y); adding eta<1 keeps BOX 128y. The segments of the multivariable theorem are therefore contained in that box.

## Generic polynomial and propagation

The formal differentiation uses p'=q,...,v5'=v6 and forbids differentiating v6. The algorithm constructs G=t4W(1,A,B,C), cancels negative powers of t and checks 55 monomials, t degree <=2, jet degree <=6. The exact weighted sum K 30936927338496 controls the sum of the six partial derivatives on BOX by Kt²y5. Each term is paid by the jet degree and 128^(degree−1); t>=1, y>=21 allow enlarging to t²y5.

The rational inequality etaK=59029694970340794273/10^17<96·21<=96y is reproduced. Thus |G−G0|<96t²y6, and G<−4000t²y6; therefore W4<−4000y6/t² for ALL t>=1. A high tail was not replaced by a sample or by an asymptotic.

## Consequence and limits

With B'>0, J>0 global from 086, RAISE087 converts the sign into (Eraise/J)'>0 on the exterior region; Rolle gives the density determinant negative for all four nodes ALL >=1. This does not allow Andreief on the complete half-line: 0<t<1 remains pending. 087 only supplies an existing neighbourhood of the origin without radius, which does not cover that compact range.

No W coverage is added to 085, nor are five/all orders or a window T proved. Consulting 077/083–087 and the three records distinguishes the new exterior sign of a Wronskian up to V6 from the already proved N077 up to V4.
