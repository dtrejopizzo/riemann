# Correcting one unit of mass at a cost tending to zero

Among the integer binomials with upper argument n≤N from 262, let R_N be the maximum of |Σa_i e_i| over combinations that are exactly zero on every prime power and have Σ|a_i|≤1. Then

    R_N → ∞,       R_N ≤ log(N+1).

Consequently, for N≥6 the minimum cost of correcting a scalar error Δ without altering a single prime power is exactly |Δ|/R_N. The price per unit tends to zero unconditionally. The qualitative proof does not provide a lower growth rate for R_N.

**A concrete example.** From the four rows binom(p,1) for p=5,7,11,13 subtract the row binom(15,6) and divide by five. The combination has variation one and vanishes on every prime power: binom(15,6)=5005=5·7·11·13, and each prime of the product enters through the carry at m=p (all have p²>15). Its mass is [Σ e(p,1)−e(15,6)]/5, between 0.43082 and 0.43083. With the rows of 262 one obtained |log(1728/3125)|/3<0.198. The example only certifies a floor for the optimum.

**Dual reformulation.** Let A be the carry matrix with binomial rows and prime-power columns. R_N is the sup-norm distance from the vector e to the image of A. This is finite duality for the quotient norm: the functionals vanishing on the image are the combinations sought. Enlarging N preserves every witness by adding zeros, since an earlier row does not load higher powers either; R_N is nondecreasing. The column vector z_m=Λ(m) produces log binom(n,k). The bound 0≤e−log binom≤log(n+1) of 262 gives the ceiling.

**Consequence of a price that did not drop.** If R_N were bounded by C, then for each N there would exist z_m such that H(n)=Σ z_m⌊n/m⌋ satisfies, with D(n)=n log n−H(n) and D(0)=0,

    |D(n)−D(k)−D(n−k)|≤C   (n≤N).

The cyclic averaging of 261 applies to any scalar function with that defect. It gives |D(j)−c_N j|≤2C for c_N=D(N)/N. Since D(1)=0, |c_N|≤2C. At each fixed argument H(n) is bounded uniformly in N. So are the coordinates z_(p^a): H(n)−H(n−1) sums z_m over the primary divisors of n, from which they are recovered successively at n=p^a. Extracting a diagonal subsequence in all coefficients and in c_N produces a global H with H(n)=n log n−cn+O(1).

**Contradiction at the origin.** Define b(n)=H(n)−H(n−1)−log n. It is additive for coprime factors and bounded, by the last estimate. In particular Σ_p sup_(a≥1)|b(p^a)|<∞: for any finite set of primes choose powers with nearly maximal positive values, omitting those that do not contribute. The value of b at their product bounds the sum uniformly; repeat with the negative values.

For Re s>1 one has

    Σ b(n)n^(−s)=ζ(s) Σ_p (1−p^(−s)) Σ_(a≥1) b(p^a)p^(−as).

The factor after ζ is holomorphic in Re s>0 by uniform convergence on compacta. For real 0<s<1 it is bounded in modulus by Σ_p sup_a|b(p^a)|, since the weights of each geometric series sum to p^(−s)≤1. Since ζ is regular at 0, this continuation stays bounded as s tends to 0 from the right.

On the other hand, Σ_(j≤n)b(j)=H(n)−log(n!)=(1−c)n−(1/2)log n+O(1), by Stirling. The same formula for the real endpoint t≥1 holds with error O(1). By Mellin transform of the partial sum, the above continuation is

    (1−c)s/(s−1)−1/(2s)+s∫₁^∞ O(1)t^(−s−1)dt.

The last integral multiplied by s is bounded for real positive s. There is therefore divergence as s approaches zero, contradicting the computation via additivity. This proves the unbounded growth of R_N.

**Scope for the sign.** Given a fit in the atoms, the optimal correction of its concrete mass error now has an exact price, and it is asymptotically cheaper than repeating a fixed relation. But R_N≤log(N+1): this improvement, by itself, does not reduce the exponent of an error larger than the square root by a fixed power. The joint estimate of the fit cost and the size of the mass error for the weight of 257 remains open.
