# Chain repair: only primes above √N require interpolation

For N=⌊2x⌋≥6 use the calibrated fit of 262. Require of a provisional combination a equality with g(m/x) only at the primes p>√N up to N. For each p≤√N define r_(p,j)=g(p^j/x)−R_a(p^j) for 1≤j≤J_p=⌊log N/log p⌋ and r_(p,J_p+1)=0. Write

    D=Σ_(p,j) |r_(p,j)−r_(p,j+1)|,
    B=xh−Σ a_(n,k)e(n,k)−Σ_(p,j) r_(p,j) log p.

The infimum of ||a||₁+D+|B| over such combinations is comparable to W_c(x) with absolute constants. In particular, a family of cost x^(1/2+o(1)) calibrated to that same order and with uniformly bounded errors at all powers of the small primes suffices to prove the global sign. The aggregate control D≤x^(1/2+o(1)) under the same initial calibration also suffices.

**Exact repair.** Add the row binom(p^j,1) with multiplier d_(p,j)=r_(p,j)−r_(p,j+1). On a modulus q its carry is 1_(q|p^j). By telescoping, the repair equals exactly r_(p,i) at p^i and zero on the chains of other primes. The added variation is D. The entropic mass of that row is log(p^j)+(p^j−1)log(1+1/(p^j−1)), whose difference from j log p lies between 0 and 1. Since Σ_j j d_(p,j)=Σ_j r_(p,j), the remaining calibration error has modulus ≤|B|+D. Correct it by the fixed null relation of 262 at a cost of at most an absolute constant per unit. Conversely, every exact calibrated fit already has D=B=0. This proves the comparison in both directions.

**Budget.** If |r_(p,j)|≤M uniformly, then D≪M√N/log N: there are O(√N/log N) primes and squares of primes in these chains, and O(N^(1/3) log N) higher levels. Moreover Σ_(p,j) log p ≪√N by the Chebyshev bound and the same count of higher powers. Hence the initial scalar correction changes by O(M√N). For errors without a pointwise bound, the above telescoping gives |Σ r_(p,j)log p|≤D log N, sufficient if D already has square-root size with subpolynomial loss. The comparison with B retains the cancellations of that term at finite scale.

**What remains to be built.** For large x the primes √N<p≤x must reproduce zero, besides being correct on x<p≤N. The construction of 267 controls the small response uniformly, but its error on a band of primes of size proportional to x violates precisely these remaining equations. The above procedure eliminates all exact interpolation conditions on squares, cubes and the other proper powers, under the explicit variation budget on the chains; it preserves the global mass condition. The universal obstruction of 270 does not control this specific construction.
