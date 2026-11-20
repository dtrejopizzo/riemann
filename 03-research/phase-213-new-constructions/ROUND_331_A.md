# Truncation by common divisor in the energy of nearby pairs

In the energy of 325–326, the absolute cost of the distinct pairs with greatest common divisor greater than G≥1 is

    O(h binom(2m,m)/G),     0<h≤1, m≥1,

with an absolute constant for the normalized kernel of 325. The result holds even if μ is replaced by coefficients of modulus ≤1.

**Proof.** Since |K|≤1 and K vanishes for |log(n/d)|>h, use 2l_m(n)l_m(d)≤l_m(n)²+l_m(d)² and symmetry. For X≤n<2X, X a power of two, majorize by the sum over all common divisors g>G. There are at most 2X/g multiples of g in the block. For each one the other multiples are at distance at most 2(e−1)hX, hence there are at most 4(e−1)hX/g distinct neighbours, even when that last quantity is less than one. Summing g^(−2) for g>G, the block costs at most a constant times h(log(2X))^(2m)/(GX(m!)²). Since ∫_[2X,4X] dv/v²=1/(4X), the sum of (log(2X))^(2m)/X is bounded by four times the integral of (log v)^(2m)/v² from 1 to infinity, equal to 4(2m)! including the factor four.

**Application to the sign.** For h=exp(−am), 0<a<log 4, it suffices to keep the diagonal and the pairs with gcd ≤ exp((log 4−a)m). Everything removed, even taking moduli, costs O(1/√m). In the remaining ones write n=gr, d=gs with (r,s)=1. Then μ(n)μ(d)=μ(r)μ(s)μ²(g) if (g,rs)=1 and it vanishes otherwise. At a fixed reduced quotient r/s all terms have the same sign, since K≥0. Divisor inversion within a single family of common multiples produces no cancellation among its members: the pending gain must combine distinct reduced quotients. The bound does not estimate that signed sum.

**Antecedent.** 326 estimates the total proximity cost without distinguishing the gcd. The truncation above keeps its counting argument and quantifies which part can already be removed at diagonal cost. No novelty is attributed to the elementary factorization of μ.
