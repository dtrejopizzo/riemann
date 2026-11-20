# The endpoint k=4 fails unconditionally, with oscillation larger than the main term

For almost every t∈[1,2] and each fixed k with 0<k≤4, putting L=log x one has, with no hypothesis on zeros off the line,

    R_t(x,x/L^k) = Ω_±(x L^(−1−k/2) log L).

The notation means that there exist arbitrarily large sequences with both signs and modulus exceeding a positive constant times the indicated scale. In particular k=4 cannot replace the exponents strictly greater than four of 306. At the endpoint the oscillations exceed by a factor log log x the magnitude x/log³x of the block with cutoff at √x.

**The boundary of the series.** Fix a known zero ρ=1/2+iγ of ζ with γ>10, of multiplicity r≥1. In the factorization of 292 extract the second degree of the Euler corrector. For p≠3 the coefficient of p^(−2w) in its logarithm is

    −(1−χ(p)cos θ)²−cos(2θ)+1 = −1/2+2χ(p)cos θ−(3/2)cos(2θ),    θ=t log p.

Therefore one extracts ζ(2w)^(−1/2), L(2w+it,χ)L(2w−it,χ) and the product [ζ(2w+2it)ζ(2w−2it)]^(−3/4). The remainder over large primes converges locally, without zeros, in Re w>1/3 by elimination of degrees one and two. The finitely many primes are adjusted separately; take the branches from the right in the neighborhoods used. Approaching the real point w=1/2 from the right, D_t(w) remains bounded: ζ(w) does not vanish there and the factor ζ(2w)^(−1/2) tends to zero. At ρ all the extracted second-degree factors are local units, by absence of zeros on the line 1 and γ>10. The two first-degree L-functions and the finite factors of the numerator do not vanish there either, except for a discrete set of t per factor, as in 292. In this way D_t has a pole of order 2r at ρ. The exceptional set for this zero can be excluded once for all k.

**Mellin comparison.** Use z=L^k, F=−LR_t/(2x) and the expansion of 306 with M/k>1/2. For real s=−1/2+h, h↓0, its continued Mellin transform is O(1/h): the term H₀ remains bounded by the above computation, the shifted terms of positive index can only have a pole at s=−j/k, simple by the formula of 306. The indices j=0,1 have their pole at the origin of their own variable removed; for k≤4 no real pole remains to the right of −1/2. The other real evaluations of D_t and its derivatives are regular. The error of the expansion has a holomorphic Mellin transform on a half-plane containing the boundary.

If some point ρ+j/k with j≥1 is a pole of D_t, the rightmost one produces an uncancelled pole inside the half-plane by 306. In that case, even after adding or subtracting c z^(−1/2)log z, any assumption of eventual sign contradicts Landau, for all c>0. Otherwise, at s₀=ρ−1 the term H₀ gives a pole of order 2r and the other terms are regular. Call A≠0 the leading coefficient. If F≤c z^(−1/2)log z eventually, the Mellin transform of the nonnegative difference, after removing a compact set, converges in Re s>−1/2 by Landau. Its modulus at s₀+h is dominated by its value at −1/2+h. At the complex point the added term is regular, so the modulus is asymptotic to |A|h^(−2r); at the real point the bound is c h^(−2)+O(1/h), since the Mellin transform of the weight from 1 is (s+1/2)^(−2). Choosing 0<c<|A| gives a contradiction. Applying the same argument to −F gives the other orientation. Returning to x, with log z=k log L, proves the statement.

**Comparison with antecedents.** The index already records Landau's oscillation method and the use of multiple poles in 058. The specific point here is that the correcting factor on the critical line preserves the complex pole and does not produce a competing real pole of the same order at the moving cutoff. It is an obstruction to the sign of this block at the extreme exponent; the full form may still be positive.
