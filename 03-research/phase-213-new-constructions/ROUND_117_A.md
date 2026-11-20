# Ceiling for the full minimum with possibly unbounded local mass

Let D₂(y) be the sum, with multiplicity, of (Reρ−1/2)² over the representatives of off-line quartets with positive ordinate at distance <1 from y, as in phase 159 G2_B2_R5. Assume D₂(y)≪[log(2+|y|)]^κ for some 0≤κ≤1. For the negative part M_W of the full floor and M_A of the primitive one,

    limsup log(1+M_A(T))/(2T) ≤ limsup log(1+M_W(T))/(2T)
                                  ≤ min(1/2, Δ+κ/2).

Hence, if the hypothesis holds for every κ>0, both quotients converge to Δ=sup Reρ−1/2, without requiring the supremum to be attained (115). The hypothesis allows local mass growing without bound. Paper 33 controls the mean of D₂, not this uniform growth.

**Frequency cost of a negative test.** For F real, unit and smooth on [−T,T], T≥1, with W_T(F)<0, write L(ξ)=log(2+|ξ|). The arithmetic formula W=m(D)−C_T+polar and m(ξ)≥cL(ξ)−C imply ∫L|F̂|²dξ/(2π)≪e^T. Indeed the comb has norm O(e^T) by 081 and the polar term is bounded by O(e^T) by Cauchy–Schwarz against exp(±t/2). Also M_W≪e^T. Jensen in the Plancherel measure gives ∫L^κ|F̂|²≪e^(κT) on those tests, without requiring a minimizer to exist.

**Spectral strip.** Reuse the segment, the subharmonicity and the rectangles of G2_B2_R5 §4 with radius 1/(2T). Instead of taking sup D₂ one gets
     
    −W_T(F) ≪ T² ∫_{|σ|≤Δ+1/(2T)} ∫ L(ξ)^κ |(t exp(σt)F)^∧(ξ)|² dξ dσ.

The locally weighted multiplicity in the integrand is valid because each rectangle covering (σ,ξ) has its ordinate at distance ≤1/(2T) from ξ. The new step is to keep the weight inside the integral until restricting to negative vectors.

**Multiplication and closure.** Extend the multiplier t exp(σt) from [−T,T] by a smooth cutoff equal to one there, zero outside [−T−1,T+1], with the first two derivatives of the cutoff uniformly bounded. The extended multiplier and its second derivative have L¹ norms ≪(1+T)² exp(|σ|T) for |σ|≤1. Its Fourier transform is bounded by that quantity times O((1+|ξ|)⁻²). Since L(ξ)^(κ/2)≪L(ξ−v)^(κ/2)L(v)^(κ/2), Young gives a bound for the weighted L² norm of the transform of the product by O((1+T)² exp(|σ|T)) times that of F̂. Inserting and using the previous moment gives −W_T(F)≪(1+T)^6 exp((2Δ+κ)T). Take the infimum by density of the tests and combine with 115.

**Cross-check and limit.** The use of sinh and of the quadratic masses is already exactly U₂ of G2_B2_R5 and is not counted as new. Theorem M there rules out a bound for the isolated negative channel on the whole unit ball if D₂ is unbounded. Here the weight is only paid on tests with negative full energy, which do have a logarithmic budget by the arithmetic formula. It is not proved that D₂ grows subpolynomially in log |y| for ζ; without that input the general upper bound at exponent Δ is not closed.
