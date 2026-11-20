# What exactly the variance measures after removing the critical pairs

**Status: PROVED, with independent review of paired Hadamard, multiplicities and orders of the remainders.**

Let V₀=ξ''(1/2)/ξ(1/2), the variance of the normalized kernel of 406. Write the zeros of the upper half-plane with multiplicity as ρ=1/2+δ+iγ. Then

    V₀ = Σ_{γ>0} 2(γ²−δ²)/(γ²+δ²)².

Indeed, for the even function w↦ξ(1/2+w) the Hadamard product grouped by pairs wρ,−wρ has factors 1−w²/wρ². It converges locally by Σ|wρ|^(−2)<∞; the linear exponential factor is constant by parity. Two logarithmic derivatives at zero and conjugation give the formula. All summands are strictly positive since γ>|δ| (the strip 0<Re ρ<1 and the verification at height 1 suffice). Simplicity plays no role.

**Consequence for 407–409.** After dividing by all pairs of zeros on the line up to height H, the remaining normalized second derivative is exactly the previous sum over the non-removed zeros. This holds even if the positivity of the quotient kernel is not yet known. As H grows the residue tends to the sum over the exterior zeros, by absolute convergence; hence it tends to zero if and only if RH. Positivity at each step, even if proved for all critical pairs in order, does not by itself suffice to identify that limit with zero. If the line is verified up to H, the residue after removing those pairs is O(log H/H), by partial summation of the zero count. The certificate of 409 does provide positivity for its finite stage; the variance identity alone does not provide that kernel sign.

**Separating the effect of moving zeros horizontally.** Let us compare V₀ with the moment that would result from projecting all zeros onto the line, keeping ordinates and multiplicities. The deficit is

    Σ_{γ>0} 2/γ² − V₀
      = Σ_{γ>0} 2 δ²(3γ²+δ²)/[γ²(γ²+δ²)²] ≥0.

It vanishes exactly under RH. Each term measures a squared horizontal displacement. In particular, after a rigorous verification up to H, the total deficit is O(log H/H³): it suffices that δ²≤1/4, to sum O(γ^(−4)) for γ>H and to use N(T)=O(T log T). Here Σ2/γ² includes the ordinates of ALL zeros with multiplicity; replacing them by those of the only zeros known on the line would change the statement. The gain of two powers of H relative to the residual variance comes from subtracting the common vertical contribution, not from excluding higher zeros.

**Review record.** Choosing a representative withγ>0 of each pair±wρ produces the product∏(1−w²/wρ²), including each multiplicity. When grouping, the canonical exponentials of genus1 cancel within each pair; the only remaining global factor is exp(a+bw), and parity forces b=0. No additional quadratic factor appears. The second derivative of log ξ at0 is−2Σwρ^(−2); the two upper representativesδ+iγ and−δ+iγ of a quartet cancel their imaginary parts and leave exactly the written summands, without dividing again by2. At multiple critical zeros2/γ² is subtracted for each removed order.

Each residual term is between0 and2/γ². The exact deficit is2δ²(3γ²+δ²)/(γ²(γ²+δ²)²) and, for largeγ with|δ|≤1/2, it is O(γ^(−4)). Partial summation withN(T)=O(Tlog T), counting all zeros and their multiplicities, gives respectively the remainders O(log H/H) and O(log H/H³). The hypothesis of verification up toH means that all zeros of that strip are on the line, not only that a list of critical zeros is known. Without positivity of the quotient kernel, the value is a formal normalized second derivative, not a claim of positivity of a measure; the spectral identity and its limit remain valid.

This computation gives a proof of obstruction to the passage from finite to global: the additional datum required for concentration already encodes the whole possible exterior spectrum in a positive sum. To deduce RH by this route one would need an independent bound forcing that residue or the deficit to zero; counting positivity stages or substituting a finite H does not provide such a bound. No historical novelty of the Hadamard product or of its moments is claimed.
