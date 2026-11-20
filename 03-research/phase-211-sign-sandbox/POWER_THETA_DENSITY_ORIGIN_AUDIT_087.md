# POWER_THETA_DENSITY_ORIGIN_AUDIT_087 — Independent audit

Status: **APPROVED / PROVED for the point and an unquantified neighbourhood.** Source `POWER_THETA_DENSITY_ORIGIN_087.md` and final code read in full. Independent reproduction gave exit0/NEGATIVE, as did the two earlier runs. Hash:

    f8f28e5f33659ec7245e23906ab11addc5a04243f1d502a8a070dbf12d13d7b7

Papers untouched; no campaigns.

## Formulas and normalization

The densities tPhi, (tPhi)'', −Phi', −Phi''' divided by tPhi give exactly 1, A, B, C. In lambda=t², multiplying the four ratios by phi=Phi/Phi0 multiplies the Wronskian by phi4; at 0 phi0=1. ORIGIN-MATRIX correctly contains the derivative factors k! and the indices a_(k+2), so it only needs Phi10. No factor t is lost when taking the analytic limit.

RAISE is correct: W(1,A,B,C)=W(A',B',C'); factoring k=B' and substituting U=A'/k, V=C'/k gives −k³J²(E/J)'. The coefficient of V6 in Wt is Wt(1,A,B)/t=−N077/(pt4), with correct sign. This signals a new obligation; it does not allow the jets of Phi to be treated as free.

W_R3,lambda=[(3v2²+v4)v6−20v2v4²]/180 was reproduced symbolically. v10 appears only in a5 with coefficient −1/10!, and in H33 with factor −4320; the cofactor is exactly W_R3, so the final coefficient is W_R3/840. JET-RAISE keeps factorials/signs, but does not pay for the rest nor the hierarchy.

## Intervals, tail and reproduction

The class I uses Fraction and outward integers at 70 digits for each operation; division only by a strictly positive interval. Machin128 and exp Taylor128 with division 2048/11 squarings have safe explicit remainders. Q0..10 are generated with the exact recurrence; the bound B 1745986560 covers their coefficient sums. All y>=3m² for m>=9 lie beyond the maximum of y11e−y, so the complete tail with ratio <1/2 is correctly paid. The factor m² was not omitted.

The prefactor Phi=pi exp(5t/2)S is applied via the COMPLETE binomial convolution up to order 10, after adding the tail to each Sder. The parity checks are only self-tests, not an inference of parity from intervals. Phi0>0 enables normalizing; the determinant is enclosed over the 24 permutations with outward rounding. The assert requires separating 0 without prescribing the sign.

The independent reproduction finished exit0 and obtained EXACTLY the same two rational endpoints, TAIL, B and hash as the source. The whole interval is negative. The approximate decimal was not used as proof. The change of provisional name 086 to 087 and docstring did not alter the object or the bounds.

## Scope

W_lambda(1,A,B,C)(0)<0 and analyticity give the same sign in some positive neighbourhood, WITHOUT quantified radius. Thus the local necessary condition of the R4 transport passes; neither the global sign nor the Chebyshev property of four densities on the whole half-line has been proved. The global Darboux criterion and the S4 branch remain OPEN.

No W coverage is added: four generators are already proved in 085 by another route. Neither five/all orders nor a window T are inferred. Consulting 073–086 and the three indices distinguishes this decision at a real point of the new transport from a mere repetition of 077 or an abstract falsifier.
