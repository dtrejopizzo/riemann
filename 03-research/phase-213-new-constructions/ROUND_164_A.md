# How far the negativity of the distant block reaches

Use D_X,N_X(H) of 162–163, and call F_X(H) the integrated block |p−q|>H. There are constants b,c>0 such that, unconditionally, if

    X exp(−b log X/log log X) ≤ H ≤ X/log X,

then F_X(H)≤−cXH for X sufficiently large. The lower end is smaller than X/(log X)^k for each fixed k, though larger than X^α for each fixed α<1. The advance over 162 is that the relative distance can decrease at this rate.

**Smoothed sum.** For U(x)=Σ_q Λ(q)K(x/q) the formula
    U(x)=−Σ_ρ mρ B(ρ)x^ρ+O(x^(−1/4))
holds. Here distinct zeros are summed. Move the inversion of B(s)(−ζ'/ζ)(s) to Re s=−1/4 as in 156 and 160. No real poles remain in the strip: B is entire and B(1)=0. Polynomial growth on good horizontals and the bound for the product of uniforms of 160 give absolute and uniform convergence of Σ mρ |B(ρ)|. More precisely the tail above height T costs O(exp(−c₁√T)) for large T by the zero count and the decay of the product, absorbing polynomial factors.

The classical zero-free region of De la Vallée Poussin gives β≤1−a/log(3+|γ|) for some a>0. Take T=(log x)². At the low zeros one gains exp(−c₂ log x/log log x) when bounding x^β; at the high ones the tail of coefficients gains exp(−c₁ log x). By 161 passing from U to S, the sum over simple primes, costs O(√x). Thus |S(x)|≤C x exp(−b log x/log log x), for some b>0 that can be decreased. On [X,2X] this bound is kept with X and eventually a larger constant. Since F_X(H)=∫₁² S(Xv)²dv−D_X−N_X(H), the lower bound N_X(H)≥c₀XH of 163 dominates the square uniformly in the indicated range. This proves the negative ceiling without assuming RH.

**What carrying it to fixed powers would mean.** Let Θ be the supremum of the real parts of the nontrivial zeros. For 0<α<1 and H=X^α:

- If α>2Θ−1, then F_X(H)≤−cXH eventually. Indeed, the preceding absolute formula directly gives U=O(x^Θ) and also S=O(x^Θ) since Θ≥1/2.
- If α<2Θ−1, then F_X(H)>0 for infinitely many dyadic scales. If it were eventually ≤0, 163 would give ∫₁² S(Xv)²dv=O(X^(1+α)log X). By dyadic Cauchy–Schwarz the Mellin transform of S would be holomorphic on Re s>(1+α)/2. There is a zero to the right by definition of Θ, and the rightmost one at that same ordinate keeps a pole in the integrand of 162. Contradiction.

The equality case is not decided. With the convention of adding the endpoint 1 to the set of exponents giving eventual negativity, the infimum is exactly 2Θ−1. In particular proving the distant sign for a single fixed exponent α<1 would already force a zero-free strip of width (1−α)/2 next to Re s=1. The unconditional result only uses the classical region whose width decreases with height. The transition to polynomial H should not be treated as a routine improvement of the truncation.
