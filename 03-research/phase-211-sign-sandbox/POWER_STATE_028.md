# State028 — Fourth and fifth full positive rows of W

Status: ROW4 and ROW5 PROVED and audited. Replaces STATE027 as the current summary. Global sign OPEN; goal active; papers untouched. Both constructions closed and reviewed.

## New coverage of the full form

POWER_ROW_FOUR_028 proves

    W[f_(4,k)] > ||f_(4,k)||²/50,
    F_(4,k)(s)=s^k/(s+u)^(4+k), ALL k>=0 and ALL u>=63/2.

The WHOLE arithmetic comb and the polar term are included. It is not positivity of an auxiliary kernel nor a sample of exponents. The proof combines ARCH/norm²>11/400, comb in magnitude<3/500 and polar loss<1/1000 for odd k; for even k the polar is positive. The resulting margin41/2000 exceeds1/50.

## What changed relative to the earlier rows

The exact formula ARCH40=d−ud'+(2u²/5)d''−(u³/15)d''' keeps the small positive margin that coarser bounds would lose. Monotonicity of ARCH in u and in k reduces all parameters to u=63/2,k0. The three polygamma series are bounded with a rational integral remainder.

The weight eta12 in WR4 reduces the cost of the full comb compared with eta15 used in018; positivity of the coefficients of its series proves uniformity in u. The real alternating sign of the polar avoids subtracting the favourable term at k0. No monotonicity of W under pole movement is assumed.

The full recurrence further implies strict positivity of the third difference of the initial row for ALL k. It does not imply differences of every order.

## Evidence and limit

POWER_ROWS_AUDIT_028 approves ROW4 and ROW5; both proofs were read and the two Fraction verifiers reproduced: PASS. Uniformity comes from analytic arguments, not from a sweep. The audit027 of the exterior balance and the gamma mixture is kept, without attributing to them the sign of the interior.

The coverage now includes rows N1,2,3,4,5 for all k and u>=31.5; the cone k>=10000N² at u31.5, eight arbitrary poles and fixed block12 also remain. In the sufficient table at u31.5, N>=6 below the cone remains. The bridge017 requires all N,k; a new row does not certify a window T nor resolve the global sign.

## Fifth row and separation pattern

POWER_ROW_SPLIT_028 proves W[f_(5,k,u)]>norm²/25 for ALL k>=0,u>=63/2. For k>=1 it gives the stronger margin4/5. ARCH50(u0)<−1/10, so requiring positive ARCH from k0 would have lost this real row.

At k0 and u between u0 and2u0 opposite extremes are combined: ARCH>−.13 and polar>.23. For u>=2u0, ARCH>.5 and the polar remains favourable. At k>=1, covariance and scaling give ARCH>.9; the odd polar loses less than.002. The FULL comb loses less than.06 at all parameters, by WR5 with eta12. These bounds prove the row without assuming monotonicity of AP or W.

The reusable criterion of the memo separates the obligation k0 from the orbit k>=1. The identity A_(N,1)=A_(N,0)+u∂_u A_(N,0) explains the improvement; the premises of the criterion are not proved for all N. The fourth difference of row1 is now strictly positive, without concluding full monotonicity.

The continuation029 looks for a uniform pattern through autocorrelation control with opposite weights and parameters N/u², after comparison with the no-go of weights at fixed u016. The objective of all N at fixed rate is not replaced by a result with increasing rate.
