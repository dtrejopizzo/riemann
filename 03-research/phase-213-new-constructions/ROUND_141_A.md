# Two positive weights and a Möbius contribution of determined sign

For z>0 set V(z)=Σ_{k≥1 odd}exp(−k²z). For X>0 there is an absolutely convergent identity

    F(X)=Σ_r μ(r)V(r/X)=Σ_{4∤n} λ(n) exp(−n/X).

Indeed the convolution of μ with the indicator of squares equals λ; removing the squares with even root subtracts 1_{4|n}λ(n/4), and λ(n/4)=λ(n). On both sides the weights of the arithmetic coefficients that are kept are positive. In 140 the weight on μ was positive and rapidly decreasing at both ends, but a coefficient −2 appeared in one Liouville class.

**The price of positivity and how to pay it.** By Poisson for the Gaussian (subtracting the even subseries) one has

    V(z)=√π/(4√z) + O(z^(−1/2) exp(−π²/(4z)))   (0<z≤1).

The constant term cancels exactly. The root singularity was to be expected: for a positive weight φ in place of the exponential, the Mellin transform of the profile Σ_{k odd}φ(k²z) in Re s>1/2 is (1−4^(−s))ζ(2s) φ̂(s), with φ̂(s)=∫φ(u)u^(s−1)du. If φ̂ is finite and continuous at 1/2, its value is positive for a weight that is nonzero almost everywhere in the sense of not being identically zero as an element of weighted L¹. The factor ζ(2s) forces divergence when approaching from the right. A profile that is positive in this class cannot be flat and decreasing to zero at both ends if it also decays rapidly at infinity.

Let c₀=1/ζ(1/2)<0. There exist infinitely many arbitrarily large integers D, characterized by crossing the level c₀, with

    |Σ_{r≤D} μ(r)/√r − c₀| ≤ D^(−1/2).

Indeed the one-sided Mellin transform of the step function on the left before taking modulus is 1/[sζ(s+1/2)]−c₀/s for Re s>1/2. It is regular on the real axis s≥0, including the origin by the choice of c₀. A nontrivial zero with Reρ≥1/2 gives a pole at ρ−1/2. If the centered step function had constant weak sign from some point on, the abscissa of convergence of the integral would lie between 0 and 1/2 (a pole on the boundary suffices for the lower bound); by Landau it would have a real singularity at that abscissa. This contradicts regularity. The jumps have modulus ≤1/√D, which gives the bound when changing sign or passing through zero.

**Unconditional sign result.** For each such D and simultaneously for all X≥2D log D,

    (1/√X) Σ_{r≤D} μ(r)V(r/X)
       = √π/(4ζ(1/2)) + O(D^(−1/2)).

Indeed the normalized error of the Poisson formula is ≪Σ_{r≤D}r^(−1/2)exp(−π²X/(4r))≪√D exp(−π²X/(4D)) and the crossing error costs O(D^(−1/2)). The term is therefore strictly negative uniformly for D large. No spacing law between the crossings is needed. For each large X one can choose the last of these D with 2D log D≤X: it exists and tends to infinity with X, without a rate proved here.

**Remaining obligation.** With that choice D(X), a one-sided ceiling Oε(X^(1/2+ε)) for Σ_{r>D(X)} μ(r)V(r/X), for all ε>0, is sufficient and necessary for the sign. The equivalence follows because the removed block is O(√X). For the total, the Mellin transform is Γ(s)(1−4^(−s))ζ(2s)/ζ(s). On Re s>1/2 the numerator does not vanish, the real axis is regular and Landau applies as in 140. Under RH the two-sided ceiling is obtained from that of the sums of λ, removing the scale of the multiples of 4 and summing by parts. The tail r>10X log X can moreover be removed in absolute value by the decay of V. The negative constant found for the block does not prove a sign of the total.

**Cross-check.** 073 already uses the recurrence μ*Λ=−μ log, so repeating it without a new estimate was not the route followed. 134 chooses crossings of the exponent-1 moment at level zero. Here the crossing at the critical exponent requires the nonzero level c₀ to cancel the real singularity of the transform; that level determines the sign of the uniform theta term. 140 and the theta transformations of the corpus give the antecedents of the weight; no novelty is attributed to the Poisson identity or to Landau.
