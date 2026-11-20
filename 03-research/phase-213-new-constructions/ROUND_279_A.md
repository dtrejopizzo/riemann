# The exact exponent of the absolute mass in the band

Let Θ=sup_ρ Re ρ over the nontrivial zeros of ζ. For the weight of 275 and the specific construction of 274, with A(x) from 277, one has

    lim_(x→∞) log A(x)/log x = (1+Θ)/2.

It also holds with primes only. Hence RH is equivalent to A(x)=x^(3/4+o(1)). The result determines the absolute precision lost by forgetting the signs. It avoids returning to the bilinear reduction of 049, whose cancellation obstacle on two factors close to √x is already recorded.

**Floor at every scale.** For any fixed zero ρ with real part β>1/2, repeat the exact Mellin identity of 276. On [0,Y] the regularized tail is O(N^(−2)) also with y^(β−1), enlarging the constant C from the outset to cover 1/2≤β≤1 uniformly (for y≤Y one loses at most a factor 1+√Y relative to the estimate for β=1/2, absorbable into the decay exponent). H(ρ)≠0 by 275. It follows that ∫_Y^U |T| ≫_ρ x^β Y^(1−β). The relative transfer of 277 gives the same floor for A and its prime version. At Θ=1/2 use the first zero as in 276. Take first the lower limit in x and then the supremum over β. No uniformity in the ordinate of the zero is needed.

**Ceiling if Θ<1.** Fix Θ<θ<1. By the classical Mertens criterion in a zero-free half-plane, M(v)=O_θ(v^θ) (a strict margin is left between Θ and θ). For S_*(t)=Σ μ(d)w(dt/x), partial summation and the compact smoothness of w give

    |S_*(t)| + t|S_*'(t)| ≪_θ (x/t)^θ   (0<t≤2x).

For the derivative use the same bound with the weight u w'(u). Hence the full coefficients b_j of 261 have variation Σ|b_j|≪_θ x^θ on integrating the derivative over t≥1. The integer fit of 261 has the same order of cost and is exact at all atoms. By the explicit formula for the smooth weight, |J−xh|≪_w x^Θ for large x (the absolute sum of |H(ρ)| converges uniformly over the strip by vertical decay). By Stirling, its full entropy differs from xh by O_θ(x^θ log N). The full first discrete moment ΣS_*(j) is zero by exactness at m=1.

Now pass from the full profile to the cut profile χ(t/U)S_*(t) of 273. The variation of the two discrete moments is, respectively, O_θ(x^θ U^(1−θ)) and O_θ(x^θ U^(1−θ)log N), summing over j≤U. Applying the inverse of the normalized matrix of 273, including the centering of its second row, gives corrector amplitudes O_θ((x/U)^θ log²N). For y in the band, the full inversion satisfies Σ_l S_*(ly)=w(y/x)=0 at the real argument. Hence

    T(y)=Σ_(l≤U/y)(S(ly)−S_*(ly)).

Here there are O(log²N) summands and each argument is ≥Y. The previous estimates give sup_band |T|≪_θ (x/U)^θ log⁶(2N). By Chebyshev the Λ-mass of the band is O(U), so that limsup log A/log x≤(1+θ)/2. Let θ↓Θ. If Θ=1 it suffices that |T|≪U log²(2N) at the atoms by the total variation of the rows and |c|≤1. The upper limit is then ≤1, coinciding with the lower one.

**Consequence for the sign.** Even under RH the absolute mass has exponent exactly 3/4. The relative balance of 277 and the one-sided square-root bound of 275 are of different precisions. The present theorem further offers an alternative criterion entirely in terms of magnitudes: an upper bound with exponent 3/4 for A would suffice. That unconditional ceiling remains open.

**Sufficient subsequence.** Since the floor forced by each zero holds for all sufficiently large x, it suffices to exhibit any sequence x_j→∞ with A(x_j)≤x_j^(3/4+o(1)), even using only the prime version of A. A zero with β>1/2 would force exceeding that ceiling at all sufficiently large terms of the sequence. Neither positive density nor an estimate between selected scales is required.
