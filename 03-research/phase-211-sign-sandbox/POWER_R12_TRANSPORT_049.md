# POWER_R12_TRANSPORT_049 — Arithmetic transport R12 for the first movement from V12

Status: PROVED; independent review APPROVED in POWER_R12_AUDIT_049.md. The exhaustive finite certificate was reproduced independently, PASS. R12 is solved in its declared class, not the full sign of W. Papers untouched.

## 1. Corpus, difference and target

Consulted the project rules, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID, CROSSWORD-TO-D and PRIME_TRANSFER014, GEOMETRIC_TRANSFER015, ARITHMETIC_BLOCK007, R12_ENDPOINT048 and CENTERED_CUTOFF049. The universal falsifier014 does not belong to V12. The eventuality015 did not give an effective cut. The current difference is to combine the analytic cut J=14, uniform in ALL numerators of V12, with an exhaustive certificate of the only remaining segment j=1,...,13. The indices are fixed by the proof of the cut, not by a search for favourable cases.

Let u=63/2, Q(s)=s/(s+u), and E2=ARCH+POLAR−sqrt(2)log2·c(log2). The target is exactly R12 of PRIME_TRANSFER014§5, with c=1/2500.

## 2. Finite segment: matrices and error relative to the Gram

The verifier tools/power_r12_finite_segment_049_verify.py reproduces the audited interval formulas007 and048 for the first25 bands of the Toeplitz matrix E2 in the orthonormal Laguerre basis. It keeps ARCH, contact2 and polar exact in their original normalisations. The ARCH uses power sums from16 with Euler and explicit remainders, the polar is rational and log2 has a positive atanh remainder. The rational centres have denominator10^18. The sum of errors per row is less than10^−8.

On the circle z=(s−u)/(s+u), Q=(1+z)/2. For each j=1,...,13 the image Q^jV12 has coefficient matrix

    C_j[a,i]=binom(j,a−i), 0≤i≤11, 0≤a≤11+j,

understood as zero outside0≤a−i≤j. The common factor2^−j is omitted: it cancels from the sign of the inequality. The exact Gram is C_jᵀC_j. If T is the matrix E2 and Tc its interval centre, then

    |xᵀ C_jᵀ(T−Tc) C_j x| ≤ 10^−8 xᵀ C_jᵀC_j x.

The error is not paid against an identity of ill-conditioned coordinates. The rational LDL of dimension12 verifies, for ALL thirteen indices,

    C_jᵀ Tc C_j − (1/2500+10^−8)C_jᵀC_j > 0.

The single run ended exit0, with thirteen PASS messages and the conclusion

    E2[Q^jF] > ||Q^jF||²/2500,
    F∈V12 nonzero, j=1,...,13.                          (FINITE)

The check uses no floating eigenvalues nor discretisation of rates, and leaves no unverified indices in that segment.

## 3. Analytic tail and the whole orbit

CENTERED_CUTOFF049 proves for EVERY j≥14 and EVERY F∈V12,

    E_(Q^jF) τ^−2 < 1/405,
    ARCH[Q^jF]/||Q^jF||² > 859/800.

Contact2 has modulus less than the norm². R12_ENDPOINT048 gives

    |POLAR[Q^jF]|/||Q^jF||² ≤ (9/62)^j PB12,

with PB12<3: the polar bands have modulus<1/5 and the row sum is<12/5. Thus, for j≥14,

    E2[Q^jF]/||Q^jF||²
       > 859/800 − 1 − 3(9/62)^14 > 1/2500.             (TAIL)

Combining FINITE and TAIL, E2−c norm² is strictly positive on ALL of Q^jV12, for all integers j≥1.

## 4. Exact assembly and resolution of R12

For v≥u put r=1−u²/v²∈[0,1). Let G_v(s)=sF(s)/(s+v). The geometric identity015, applied to QF, gives

    E2[G_v]=(1−r)Σ_(j≥0) r^j E2[Q^(j+1)F],
    ||G_v||²=(1−r)Σ_(j≥0)r^j ||Q^(j+1)F||².           (MIX)

It is an identity of quadratic forms, not of functions. The polar is preserved because Q(−1/2)Q(1/2)=−1/3968 and

    (1−r)Σ r^j (−1/3968)^(j+1)=−1/(4v²−1).

The series converge absolutely by a direct argument. On the real axis |Q(iτ)|<=1 and the integral of |m(τ)||F(iτ)|² is finite for every F in V12, by its rational decay. This uniformly dominates the archimedean integrals of Q^jF. Contact2 is bounded by sqrt(2)log2·||F||², and the polar is the explicit geometric sequence above. Thus each E2[Q^jF] is uniformly bounded in j; the geometric sum and dominated convergence justify MIX for each finite v. The same domination with multiplier1 proves the norm identity and allows subtracting c. The case v=u is r=0 and is included.

By FINITE+TAIL and MIX,

    E2[G_v] > (1/2500)||G_v||²,
    F∈V12\{0}, ALL v≥u.                              (R12-PROVED)

This is exactly the obligation R12: |G_v(iτ)|²=τ²|F(iτ)|²/(v²+τ²) and POLAR[G_v]=−POLAR[F]/[4(v²−1/4)].

If f_v=(s+u)F/(s+v), T2 of014 implies

    (E2−c norm²)[f_v] ≥ (u²/v²)(E2−c norm²)[F].

007 certifies E2[F]>(1/1250−10^−8)||F||²; since that margin is greater than c, the base is also coercive at the same constant.

## 5. Scope

The restricted obligation R12 and the first movement from V12 are solved. The remaining contacts on the shifted space have not been bounded here: the small tail of007 was certified only on the confluent base V12. Hence no inequality for full W on those new spaces is inferred. Nor is R12 applied recursively to an intermediate base different from V12 without an additional proof. No global sign nor new time window is claimed.
