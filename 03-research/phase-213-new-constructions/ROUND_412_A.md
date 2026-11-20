# Integrated comparison on the real axis that recovers the unweighted sum of displacements

**Status: PROVED, with independent review of the normalization at infinity, the factor2 and the extended limit.**

Let X(w)=ξ(1/2+w)/ξ(1/2) and P(w)=∏_{γ>0}(1+w²/γ²) using ALL ordinates with multiplicity. For real w both are positive. There exists c=lim_{w→+∞}log(X(w)/P(w)). If

    D(R)=∫_{−R}^R [log(X(w)/P(w))−c] dw,

then D(R)≥0 for R>0 and

    lim_{R→∞} R D(R) = 2 Σ_{γ>0} (Re ρ−1/2)²   in [0,∞].

This differs from the deficit of 410, which weights the displacements with order γ^(−4). In particular an unbounded sequence with D(R)=o(1/R) would suffice for RH. The claim does not give that estimate.

**Normalization.** By Hadamard as in 410, for the upper zero with δ=Re ρ−1/2 take the contribution of its conjugate pair log(((w−δ)²+γ²)/(δ²+γ²)). Sum symmetrically the abscissae δ and −δ (without duplicating the multiplicity). The difference with P is the sum of log(γ²/(δ²+γ²)) plus the sum of centered differences

    [f_γ(w−δ)+f_γ(w+δ)]/2−f_γ(w),    f_γ(w)=log(w²+γ²).

The constant converges by Σγ^(−2)<∞; the remaining terms cost O(δ²/γ²) by Taylor, uniformly in w, and tend individually to zero as w tends to infinity. Thus the constant is precisely c, also determinable as a limit along the real axis without introducing the abscissae into its definition. The sum is integrated term by term on each compact set.

**Positivity after integrating.** Let J(d)=∫_(−R)^R f_γ(w−d)dw. It is even and

    J''(d)=4R(R²+γ²−d²)/[((R−d)²+γ²)((R+d)²+γ²)].

Since |d|≤1/2 and γ>1, this expression is positive and comparable to R/(R²+γ²), with absolute constants. The integrated contribution is J(δ)−J(0)=∫₀^|δ| (|δ|−t) J''(t)dt. Hence

    D(R) ≍ Σ_{γ>0} δ² R/(R²+γ²).

At fixed γ, R J''(t)→4 uniformly for |t|≤1/2, so R[J(δ)−J(0)]→2δ². If Σδ² converges, Cδ² dominates and one passes to the limit. If it diverges, positivity allows taking arbitrary partial sums for the liminf. This proves the complete formula: no high zero can compensate the contribution of a low one in this integral.

**Review record.** When first grouping each zero with its conjugate the positive factors((w−δ)²+γ²)/(δ²+γ²) appear; the canonical linear exponentials cancel when summing the abscissaeδ and−δ with their multiplicities. The symmetric average used in the formula does not duplicate the upper set: each zero withγ>0 is still counted once. The constant is c=Σlog(γ²/(γ²+δ²)), finite and non-positive. The uniform bound |[f(w−δ)+f(w+δ)]/2−f(w)|≤Cδ²/γ² allows both the passage to infinity and integration on any compact set; without subtracting c there would be a term linear inR and the conclusion would not be valid.

The stated second derivative ofJ is positive for all R>0 becauseγ>|δ|, and is comparable toR/(R²+γ²) uniformly in|δ|≤1/2. Each integrated contribution is therefore non-negative, even when the centered difference has no pointwise sign. For a fixed upper zero, R[J(δ)−J(0)]→2δ²; an exterior quartet has two upper zeros and contributes4δ², which confirms the factor2 per zero. IfΣδ²<∞ it is dominated byCδ²; ifΣδ²=∞ the positive partial sums force liminf R D(R)=∞, which proves the extended limit without interchanging a divergent series. The valueD(R) remains finite for eachR, byΣδ²/γ²<∞. UnderRH it is identically0, and with some exterior zero it is strictly positive for eachR>0.

**Pending obligation.** Although X on the real axis is evaluated via ζ and its archimedean factor, P uses the ordinates of all zeros and c requires normalization at infinity. Replacing P by the product of only the verified critical zeros would invalidate the identity. The method distinguishes displacements that a Gram of ordinates alone does not detect, but it needs an independent estimate of the integrated quotient at scale o(1/R). No external priority is claimed.
