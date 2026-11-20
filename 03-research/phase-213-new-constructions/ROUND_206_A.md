# To close the bridge, the eventual sign on each fixed dyadic ray would suffice

Fix u=63/2 and call W_(N,k) the form of the atom of 205. The following statements are equivalent:

* All nontrivial zeros lie on the critical line (equivalently, the global sign of paper 47).
* For each r=p/2^j>0, with p a positive integer and j≥0, W_(N,floor(rN))≥0 for all N large enough, with a threshold that may depend on r.

In particular, for the implication toward the global sign there is no need to prove uniformity as k/N grows. The obligation remains to prove a statement for ALL dyadic slopes, without a fixed ceiling. The condition can be weakened to proving eventual nonnegativity on the multiples of the pair (2^j,p) for each such pair.

**Formula and separation.** For z=ρ−1/2, put x=−z². The identity 201 for the real datum gives exactly

    W_(N,k)=Σ_ρ (u²+x)^(−N) [x/(u²+x)]^k.

Indeed F(−z)F(z) is the summand. Critical zeros give positive values; each non-real point has its conjugate with equal multiplicity. For a slope r>0 the magnitude of the summand at k=rN is exp(N H_r(x)), where

    H_r(x)=−log|u²+x| + r log|x/(u²+x)|.

From any zero off the line, its x_* is non-real (Z1 excludes height zero). Take r_*=|x_*|/u². On the positive half-line the maximum of t^r/(u²+t)^(1+r) is at t=r u² by differentiation. Since |u²+x_*|<u²+|x_*|, one has H_{r_*}(x_*)>sup_{t>0} H_{r_*}(t). By continuity the strict inequality persists on an open interval of slopes. This does not presuppose that this same x_* maximizes over the other zeros.

**Choosing a single dominant pair.** Uniformly for r in a compact subset of that interval, H_r(x)→−∞ as |γ|→∞, since |u²+x| grows like γ² and x/(u²+x)→1. Only finitely many candidates for the maximum remain. The lines H_r(x) and H_r(y) are identical only if |u²+x|=|u²+y| and |x|=|y|. These distances to two real points determine x up to conjugation. Avoid the finitely many intersections between distinct lines and take a nondegenerate compact subinterval J on which only one non-real pair x,conj(x) maximizes, uniformly separated from the rest by a gap η>0. The remainder after removing that pair, in absolute sum, is O(exp(N H_r(x)−(N−1)η)) for k/N=r∈J: extract N−1 powers and sum exp(H_r(y)) over zeros, uniformly finite by comparison with Σ(1+γ²)⁻¹ and Z3. The value exp(H_r(x)) is bounded above and below on J.

**A fixed ray detects the failure.** Write α=arg(1/(u²+x)) and β=arg(x/(u²+x)). The quotient defining β is non-real, since its imaginary part is u² Im(x)/|u²+x|². Choose q=2^j large enough that there are two consecutive integers p,p+1 with both ratios to q in J. qα+pβ=0 and qα+(p+1)β=0 modulo 2π cannot hold simultaneously. Fix one with θ=qα+pβ nonzero modulo 2π. At (N,k)=(q l,p l) the dominant pair contributes its multiplicity times 2 exp(NH_{p/q}(x)) cos(lθ). For infinitely many l one has cos(lθ)≤−1/2: if the rotation is periodic, some vertex of the regular polygon has that property and recurs; if it is irrational, use density on the circle. On that subsequence the exponential gap dominates the remainder and W_(N,k)<0. This contradicts the eventual sign on ONE fixed dyadic ray. Under RH all summands are nonnegative squares, proving the converse.

**Relation to the corpus.** 017 and 205 work on the exact scalar table. Rounds 142–143 already use exponent separation and a finite spectral maximum in a different Gaussian family. Here the maximum over the whole critical half-axis is computed exactly for the rational function, the initial datum off the line creates an open interval of slopes, and two neighbouring dyadic numerators avoid resonance on a single ray. The eventual sign for arbitrary slopes has not been proved. Round 205 does prove it simultaneously up to r=10¹⁹. The reformulation does not prove that a slope with negative sign exists for the true zeros.

**Pattern in each row under the hypothesis of a zero off the line.** On the same J, there is a fixed integer B such that each block of B consecutive integers k with k/N∈J contains a negative value for all N large enough. For the phases θ+jβ there is B such that, for every initial θ, some 0≤j<B gives cos(θ+jβ)<−1/4. If β/(2π) is rational, the period contains at least three uniform points since β is neither 0 nor π; if it is irrational, the translates of the open arc cover the circle and compactness gives a finite subcover. The dominant term at each k has phase Nα+kβ and the gap is uniform on J, which proves the claim. B and J may depend on the hypothetical spectrum. The strict comparison and the uniform dominance were independently checked.
