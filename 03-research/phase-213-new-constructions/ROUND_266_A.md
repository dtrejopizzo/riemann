# Differences of rows with a common endpoint

For a binomial row with upper endpoint n, write Y_k(n) for its mass on proper powers (265), and include Y_0=0. Here the endpoint n is allowed to shift. The distribution is taken first in natural density for each finite family of lengths. One obtains a bound for signed combinations whose cost depends on the separation between lengths.

**Limit law.** For each prime p take a uniform p-adic integer U_p, independently of the others. For q=p^a define C_k(q)=1 if U_p mod q < k mod q, and zero otherwise. This formula is the carry in subtracting k. Define Y_k=Σ_{p,a≥2} log(p) C_k(p^a). For fixed k the sum is almost surely finite because Σ min(1,k/p^a) converges. The joint law is that of the rows in natural density: truncating at q≤M one applies the Chinese remainder theorem. For M larger than all lengths, the cost of omitting a power in n≤X is, proportionally, at most k_max Σ_{M<q≤X}(1/q+1/X), except for the first k_max integers. The number of proper powers up to X is O(√X log X), so the tail disappears in the iterated limit. This approximation holds even for probabilities of arbitrary sets of values of the vector, since the truncated vector agrees outside the exceptional event.

**Exact cancellation.** Put μ_k=Σ log(p){k/p^a} and Z_k=Y_k−μ_k. For each q, the carry counts multiples in (n−k,n] minus ⌊k/q⌋. Subtracting two intervals with a common endpoint and centering gives exactly Z_{k+h}(U)−Z_k(U)=Z_h(U−k), where each coordinate is shifted by −k. By invariance of the law, if V(h)=Var Z_h, the covariance of two rows is (V(k)+V(l)−V(|k−l|))/2.

**Size of the difference.** As h→∞,
   
    V(h) ~ κ √h log h,     κ=ζ(3/2)/(2π).

On the squares alone, independence between primes gives the sum of (log p)² φ(h/p²), with φ(u)={u}(1−{u}). In the range δ√h≤p≤A√h the prime number theorem, by partial summation, gives after normalizing by √h log h the limit (1/2)∫_δ^A φ(1/y²)dy. The normalized tails have limsup O(δ+1/A) by θ(t)≪t and φ(u)≤min(1,u). To evaluate the integral use φ(u)=Σ_{m≥1}(1−cos(2πmu))/(πm)² and u=1/y². Tonelli and integration by parts give ∫₀^∞(1−cos(2πmu))u^(−3/2)du=2π√m (Fresnel integral). This yields κ.

Within each prime the high levels may depend on one another. The quadratic norm of the centered block a≥3 is ≤log(p)Σ_{a≥3}min(1,√h/p^(a/2)). For p≤h^(1/3) this is O(log(2h)) by the geometric tail. Above, it is O(log(p)√h/p^(3/2)). Summing squares over independent primes, even bounding over all integers, the variance of those blocks together is O(h^(1/3)log²(2h)). The triangle inequality in L² allows reincorporating them without affecting the asymptotic equivalent.

**Signed combinations.** For lengths k_i in an integer interval of diameter d≥1 and real coefficients b_i summing to zero, subtract from each row the row of minimal length. This gives

    ||Σ b_i Z_{k_i}||₂ ≪ (Σ |b_i|) d^(1/4) √log(2d).

The constant is independent of the position of the interval and of the number of rows. By Chebyshev, if the right-hand side is o(√x), the limiting proportion of shifts with centered error exceeding ε√x tends to zero for every ε>0 as x grows. The exact centering is used and the density is taken first for each x. For the fit of 262 one requires an endpoint within a finite range and the simultaneous reproduction of prescribed atoms. The density obtained here does not guarantee a shift with those properties. The global sign remains open.

**What survives if atoms are fixed.** In a progression n≡r (mod M), the coordinates of the primes not dividing M remain independent and uniform by the same truncation argument (for fixed M, the tail bound in relative density only loses a factor M). If the whole contribution of p|M is set aside separately, the variance of the remaining increment is at most V(h), exactly by additivity of variances across primes. Hence the bound for signed combinations holds for the residue even after fixing any finite number of compatible congruences, with the same constant. This pins down the pending cost: in the rows of the fit, to impose a prescribed value at q=p^a via congruences one must include that prime in the reserved block. When all atoms are imposed, the random estimate no longer controls the block where the fit is decided.
