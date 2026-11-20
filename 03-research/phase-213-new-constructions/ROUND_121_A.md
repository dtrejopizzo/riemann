# Which arithmetic block keeps the rate of the full matrix

In the even orthonormal basis of 119 fix 0<a<1 and X=exp(2T). Define the real symmetric matrix K by its quadratic form for the tests F of that basis,

    K[F]=2Σ_{X^a<p≤X} (log p)c_F(log p)/√p
         −2∫_{X^a}^X c_F(log v)dv/√v,

where c_F is the autocorrelation of the extension by zero. The same definition holds on the primitive hyperplane. In both spaces, if Δ>0, the positive part of the largest eigenvalue of K has exact exponent Δ, with normalization 1/(2T) in each large window. If Δ=0 that part has exponent zero using log(1+positive part). Consequently its subexponential ceiling along any unbounded sequence suffices for the sign.

**Compensation of the density.** In the full form the polar term for real F is 2∫∫cosh((s−t)/2)F(s)F(t)dsdt. Subtracting 2∫₁ˣ c_F(log v)dv/√v leaves 2∫₀^{2T}exp(−u/2)c_F(u)du, of modulus ≤4 for ∥F∥₂=1. The difference between the comb of Λ and the prime comb has norm O(1+T): the squares cost O(Σ_{p≤√X}(log p)/p)=O(log X) by Chebyshev and the exponents ≥3 have an absolutely convergent sum. The archimedean symbol costs O(log(2+T)) in this basis by the L² derivative and Jensen as in 119.

**Error of the lower block.** For Θ=sup Reρ and each ε>0 one has θ(v)−v=O_ε(v^(Θ+ε)) for v≥2: this is the classical bound from the truncated explicit formula for ψ (height comparable to v, sum of 1/|ρ| up to that height O(log²v)); for integers or near jumps it suffices to evaluate at half-integers and use monotonicity. Removing the proper powers costs O(√v log²v); if Θ=1 Chebyshev suffices. For our basis |c_F|≤1 and |c_F'|≤∥F'∥₂≤πN/T. Integration by parts of the discrepancy against c_F(log v)/√v between 1 and X^a bounds edges and variation by O_ε((1+N/T)(X^a)^(Δ+ε)). Everything is uniform over the unit vectors and, therefore, in matrix norm.

It follows that ∥W+K∥≤O_ε((1+T)^3 exp(2a(Δ+ε)T)). If Δ>0 choose ε with a(Δ+ε)<Δ. By 119 and the variational inequality between the extremes, the error has a rate strictly smaller than the depth of the minimum of W and the claim follows. For Δ=0 use 119 and then arbitrary ε. No known numerical bound for Θ is used, nor is it concluded that K is positive. The comparison does not claim a subexponential error when Δ>0: it identifies an error of strictly smaller exponential order.

**Cross-check.** The combsine lemma of P47 already decomposes the comb in that family. 104 centers a cut X^a for a single fixed weight. Here all the vectors of a growing space share the control of the cut, and the conclusion concerns the worst matrix quotient of a moving band. The one-sided bound for the upper block remains open.
