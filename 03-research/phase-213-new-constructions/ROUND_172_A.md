# A signed extension for all zeros with summable weighted cost

Let ρ=β+iγ be a nontrivial zero and δρ=|β−1/2|. Always sum with multiplicity. On the window (−2T,2T) the spectral datum of KEP(T) of paper 47 is, in distributions and with its spectral normalization, the sum of exp(iγu)cosh(δρ u). This uses the symmetry with respect to the critical line, without assuming RH. For any k>1 and L sufficiently large there is a real symmetric measure ν_L with transform supported in [−L,L], which coincides exactly with that local datum and satisfies

    ∫ (1+|τ|)^(−k) dν_L⁻(τ)
       ≤ C(T,k) Σρ [L^(−2)+δρ²](1+|γ|)^(−k).

The constant depends neither on the number of zeros nor on their separation. Here the extension freedom of KEP(T) is used; the measure does not require a common flat-top multiplier applied to the whole datum.

**Construction and convergence.** Take b and χ of 170, with χ=1 on the window. For each zero use as transform
    exp(iγu){ b(u/L)+χ(u)[cosh(δρ u)−b(u/L)] }.
The first term has nonnegative spectral density, translated to γ. On the fixed support of χ, the derivatives up to any order N of the correction are O_(T,N)(δρ²+L^(−2)), by δρ≤1/2, parity and Taylor. The translated correcting density is therefore bounded by C_(T,N)(δρ²+L^(−2))(1+|τ−γ|)^(−N). For N>k+1, multiplying by the weight of the statement and integrating costs at most C_k(1+|γ|)^(−k), by 1+|γ|≤(1+|τ|)(1+|τ−γ|). The count of zeros by bands O(log(2+|γ|)) gives absolute convergence in the weighted norm of the corrections. The sum of the positive terms is locally finite and tempered by the same count and the rapid decay of the density of b for fixed L. The local identity can be verified against each smooth test by integration by parts and passage to the limit. The negative part of the sum is dominated by the modulus of the corrections. The announced bound over the complete spectrum follows.

**Without cutoff in u.** One can also simply take b=1 and keep the same χ. This gives a tempered extension with positive atoms at the ordinates and the same bound without L^(−2); the requirement of compact support of the transform then disappears. If RH is known up to height G≥2, the weighted cost is ≤C(T,k)G^(1−k)log(2G), by δρ²≤1/4 and the unit count. In particular the height G of Z2 of the paper can be inserted. The constants have not been evaluated and G is fixed. Increasing k changes the norm and the constant.

**Direct consequence for the form.** For smooth f with compact support in (−T,T), in the KEP convention, the value W_T(f) is ∫|f̂(τ)|²dν(τ). The preceding extension implies
    W_T(f) ≥ −C(T,k) sup_τ [(1+|τ|)^k |f̂(τ)|²] · Σρ δρ² (1+|γ|)^(−k).
Thus a concrete negative direction would impose a quantitative minimum on that sum of displacements. The inequality does not give positivity: neither is the sum known to vanish nor has a uniform positive margin been obtained to absorb it. It is not legitimate to let k→∞ keeping the norm of the tests fixed.

**Cross-check.** Tail bounds by smoothing and quartet controls have antecedents in paper 47 and R7-01. The contribution with respect to 170–171 is passing to a signed extension of the complete real datum with summable corrections, each charged to its own δρ². The total unweighted negative mass of 171 has no proved finite majorant here. The remaining problem is to produce a positive extension or to absorb the correction in the original form.
