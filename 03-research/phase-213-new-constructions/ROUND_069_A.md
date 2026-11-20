# Rows of reduced numerator up to powers below the square root

In the representative of 060 each slope a/b counts once, with a,b coprime and r=ab squarefree. We construct an equivalent criterion in which, for every fixed η between 0 and 1/2, all rows with a≤x^(1/2−η) can be removed, summing the absolute value of the balance of each complete row, at cost o(√x). The denominator runs over its whole range. The threshold applies to the reduced numerator, not to an index prior to reducing the quotient.

**Representative.** For D H(x)=H(x/4), take
     
    U(x)=(1−4^(1/3)D)(1−4^(1/4)D) Σ_{k≥1} S(x/k⁶).

The sum is locally finite by the lower support of S. The global sign is equivalent to U(j⁴)≤Cj² eventually. Under the sign, S satisfies the two-sided root bound of 060 and Σk⁻³ converges. For the converse, the two logarithmic derivatives of U and U itself are O(x) by 060 and Σk⁻⁶<∞, so that the upper interpolation between fourth powers of 060 preserves the root scale. In Mellin the multiplier with respect to S is ζ(6s) (1−4^(1/3−s))(1−4^(1/4−s)). It is holomorphic and zero-free on Re s>1/2. The transform of U is regular on the whole real axis s>1/2 by 060; Landau on C√x−U(x) on a tail extends holomorphy to that half-plane, exactly as in 060. Dividing by the multiplier preserves this holomorphy, and the pole-detection criterion of 060 gives the sign. This argument verifies the one-sided converse without assuming that Möbius inversion respects inequalities.

**Complete row.** Fix a squarefree numerator m. For each squarefree product r divisible by m there is exactly one admissible denominator, b=r/m. Denote by U_m the contribution so obtained, with the same scale filter applied before summing rows. It is a partition of the ordered slopes: the different orientations of the same product are counted with their original multiplicities. If F is the Mellin transform of one copy per product of 068, the Mellin transform of U_m on Re s>1 is
     
    K(s) μ(m)m^(−s) ∏_{p|m} (1−p^(−s)+p^(−2s))^(−1),
    K(s)=F(s) ζ(6s) (1−4^(1/3−s))(1−4^(1/4−s)).

At each forced prime the local option 1−u/(1+u²) is replaced by −u/(1+u²), with u=p^(−s). Their quotient gives the written factor. The permutations of sums in this half-plane converge absolutely as in 067. In K the average over sixth powers cancels the denominator ζ(6s) of 068. The differences eliminate the poles at 1/3 and 1/4. The pole at 1/2 was already cancelled by the centring. The formula of 068 then shows that K is entire and decreases faster than any power in height in each fixed vertical strip.

**Uniformity.** Fix 0<σ<1. On Re s≥σ the two zeros of 1−u+u² have absolute value one; by factorisation each inverse local factor is bounded by w_p=(1−p^(−σ))^(−2). For all m the inversion on Re s=σ gives
    
    |U_m(x)| ≤ C_σ (x/m)^σ ∏_{p|m} w_p.

Moreover Σ_{m≤Y}∏_{p|m}w_p ≤ Y∏_p(1+(w_p−1)/p) ≪_σ Y: expand the product into divisors and use w_p−1=O_σ(p^(−σ)). Partial summation gives for M≥1
     
    Σ_{m≤M} |U_m(x)| ≪_σ x^σ M^(1−σ).

For M=x^θ, fixed 0≤θ<1/2, choose 0<σ<(1/2−θ)/(1−θ); the exponent θ+(1−θ)σ is strictly less than 1/2. The equivalent criterion is therefore reduced to the upper bound for Σ_{m>x^θ} U_m(j⁴), with x=j⁴. In particular large products enter, and even rows with any admissible number of primes in the denominator.

**Cross-check and limit.** 054–056 treat indices before reduction and 059–060 small reduced products. The row here runs through all products that are multiples of m. The new step with respect to 068 is to combine the exact divisibility condition with an average that eliminates its denominator ζ(6s) and two differences that eliminate the residues. The constant depends on σ; this bound does not reach θ=1/2. By symmetry the statement holds for complete columns. Removing rows and columns simultaneously would require controlling their intersection. The complementary balance and the window remain open.
