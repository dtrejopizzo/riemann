# AUDIT_009 — Direct proof of the link by logarithmic flow

2026-10-19. Independent check. LINK_009_CONTINUOUS_FLOW read.
**Verdict: PROVED theorems1–2 in their precise classes. No NO-GO for O1 or D.**

## 1. Corpus and difference with respect to the previous attempt

Search in index/grid/crossword for interpolation, strong continuity, flow and Frobenius; reading of Paper44 rem:nointerp and 007–008. The change of object is explicit: this proof works with V_n in the canonical positive norm K, not with supports of Frobenius measures. The Gaussian component is included and it is proved that it does not cancel the arithmetic separation. This admits the test without retrying a closed construction.

**Precision on the Paper44 reference:** weak continuity of an arbitrary family of compact measures cannot be ruled out merely because the support changes type. The times log n have no finite accumulation, and it is possible to interpolate convexly between consecutive measures without a semigroup law or the requirement of remaining pure Frobenius objects. Hence the previous reference must not be expressed as a prohibition of ALL continuous interpolation. LINK009 does not depend on that claim: its new proofs use the semigroup law/a unitary group and an explicit norm limit.

## 2. Vector and exact separation

A=X₂−1/2 is Haar-centred and |A|²=1/4 pointwise. For odd coprime n,m, D_nA=X_n A and D_mA=X_m A: dividing by an odd number does not change v₂. Under P_s, the coordinates of the primes of nm are independent of v₂. Thus

    E_s(V_nA conjugate(V_mA))=(nm)^(−s/2)/4,
    E_s|V_nA|²=E_s|V_mA|²=1/4.

The squared distance of the arithmetic factor is κ/2·[1−(nm)^(−s/2)]. The norm of K is the SUM of this positive form and a Gaussian norm; there is no negative-sign term able to cancel it. Inequality(1) is correct.

n_k=2k+1 and m_k=2k+3 are odd coprime because their gcd divides 2. Their ratio tends to 1 and the lower limit of the distance is not zero. The bound ||G_nTA||≤sqrt(Π(A)/n) of 007 gives that the Gaussian distance tends to zero. The limit of the FULL squared distance is therefore κ/2>0. No numerical computation is needed.

## 3. Interpolation by C₀ semigroups

If W(log n)=V_n and W is a C₀ semigroup, writing m/n>1 allows factoring

    W(log m)−W(log n)=W(log n)[W(log(m/n))−I].

At the sampled times one knows exactly ||W(log n)||=||V_n||≤1, which eliminates the large time log n; no global bound on W is needed. Strong continuity is applied to the FIXED vector A at time log(m/n)→0. Contradiction with the separation of §2. The extension to every rescaling n^βV_n is verified in §6.

## 4. Unitary compression with fixed maps

For V_n=P U(log n)J, with fixed bounded P,J and C₀ unitary U,

    ||V_mA−V_nA||≤||P||·||(U(log(m/n))−I)JA||→0.

Unitarity allows taking out U(log n) without norm growth and continuity acts on the fixed JA. The contradiction does not require invariance of JH, reducibility, isometry of J nor P=J*. Theorem2 is proved exactly in a scope even more general than a usual orthogonal compression. It does not cover maps changing with n nor unbounded maps.

## 5. Final scope and next step

The result closes the SPECIFIC link that tries to declare V_n, D_n or their power rescalings as values of a C₀ semigroup; for V_n it also excludes fixed compressions of a unitary flow. It does not rule out continuous families without a flow law, unitary compressions of D_n, nor other observables or carriers. Nor does it by itself affect a proof of the node based on another map.

The positive auxiliary results 007 remain valid. What has been eliminated is a concrete way of importing them into Mellin analysis. To continue, operators, domain, convergence and gamma/comb/polar correspondence must be specified; do not use the spectral theorem of a generator of V_n whose existence has just been refuted.

**Full target D active and OPEN. Local link result approved, with no global barrier added.**

## 6. Final extension: every C₀ semigroup and power rescalings

**PROVED.** The exclusion does not need uniformity of norms outside the sampled times.

If S(t) is C₀ and S(log n)=V_n, then for the n,m of the argument

    ||V_mA−V_nA||
      ≤||S(log n)||·||(S(log(m/n))−I)A||
      ≤||(S(log(m/n))−I)A||→0,

because AT THOSE times ||S(log n)||=||V_n||≤1, regardless of the behaviour of S at other times. Thus no C₀ semigroup interpolates V_n, without extra hypotheses of contraction or global uniform bound.

More generally, if W(log n)=n^βV_n for a fixed real β, define S(t)=e^(−βt)W(t). It is a C₀ semigroup and S(log n)=V_n, impossible by the previous proof. In particular D_n=n^(−s/2)V_n does not admit such an exact C₀ interpolation either.

This extension concerns semigroups, whose law allowed factoring the difference. The compression of a group does not in general inherit that law. Theorem2 for UNITARY compressions of V_n remains proved, but this argument has not excluded a unitary compression of D_n or of another rescaling: its m,n distance may tend to zero. Do not automatically transfer the new semigroup exclusion to rescaled compressions.

The scope remains the direct logarithmic link of THIS family, not all possible representations of the node. **Final extension approved; D remains OPEN.**
