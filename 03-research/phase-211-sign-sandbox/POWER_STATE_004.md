# Revised state — three-power case resolved

Status: PROVED three case; OPEN sign at all orders. Goal active. Papers untouched.

## New theorem

For any a_1,a_2,a_3>=32 and real coefficients c_i, let rho=Σc_i X^{-a_i}, f(y)=Σc_i zeta(a_i)exp(-(a_i-1/2)y), y>0. Then

    Q[rho] >= (1/20)||f||².

If the function is nonzero, the sign is strictly positive. No separation or upper bound on exponents is required. Hence P3 for A>=32,h>0 is resolved, also for unequal triples. The confluent limits of total multiplicity three are covered.

Sources: POWER_POLE_MOVEMENT_004 (proof), POWER_CONFLUENT_004 (rational certificate), POWER_AUDIT_004 (independent review). It cancels the earlier high-range condition for triples; it does not change the scope of the general order-n theorem with increasing threshold.

## Insight and proof

The transforms are P(iτ)/∏(u_j+iτ). Raising the poles u_j individually multiplies the density by an increasing factor of |τ|. The archimedean multiplier is also increasing in |τ|. The covariance identity proves that each Rayleigh quotient increases, and by minmax so do all compressed eigenvalues. This reduces the archimedean minimum to confluent poles at u=31.5.

In the three-dimensional Laguerre basis, the archimedean matrix is an explicit Toeplitz3 and is certified >1/10 with rational sums. The weighted norm ||exp(uy/2)f||²<=1302||f||² controls the comb (<.003) and only the negative part of the polar (<.042). The sum keeps more than1/20 of margin.

## What has not been resolved

The fixed family32+k, of all orders, still has no proved sign. The bridge from that family to the sign of windows is proved. Do not extrapolate triples nor the six already certified sizes to all sizes.

In dimension four, a concrete diagnosis of the confluent case at31.5 gives a negative archimedean floor (~−.17005), while archimedean+polar is positive (~.32259). These numbers are diagnostics, not certificates. They motivate the next step: keep the positive contribution of the polar and check whether pole movement still has the right sign for that sum. Such monotonicity is NOT presupposed.
