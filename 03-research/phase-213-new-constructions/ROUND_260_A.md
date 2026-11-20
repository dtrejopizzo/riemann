# Which part of a binomial reaches the prime atoms of the octave

Fix K≥2. For integers n≤Kx and 1≤k≤n/2, let c(m)=⌊n/m⌋−⌊k/m⌋−⌊(n−k)/m⌋. Define the real fraction of the factorisation that falls inside the octave by

    r(x,n,k) = [Σ_(x<m≤2x) Λ(m)c(m)] / log binom(n,k).

For every sequence with x→∞ and k→∞, limsup r≤1/(2 log 2). The constant is attained as a limit by taking n=2k=2x an even integer. If k/n→0 and k→∞, the fraction tends to zero. This time the real atoms of the prime powers are weighted, not the lengths of the continuous bands. The restriction to the upper scale Kx is part of the theorem.

**Macroscopic splits.** If n≤x the local contribution is zero. For n>x, if k/n stays bounded away from zero, the kernel on [x,2x] has O_K(1) jumps, since n/m≤K. The estimate ψ(y)=y+o(x) uniform there shows that the numerator differs from the ordinary integral by o_K(x), even if the bands move. Endpoint conventions only cost O_K(log x). Stirling gives for the denominator n E(k/n)+O(log n), with the entropy of 258, which is of order x in this case. Apply 258 and, for the limiting equality, its symmetric example and PNT.

**Narrowing splits.** Suppose x<n≤Kx and k=o(n). By factorisation of the factorial numerator n(n−1)…(n−k+1), the numerator of r is bounded by the sum, over j≤K, of Λ(m) for m in (x,2x]∩((n−k)/j,n/j]. Moreover binom(n,k)≥(n/k)^k by the product of the ratios (n−i)/(k−i).

If k≥n^(7/10), each untrimmed interval has length k/j and endpoint comparable to n, with K fixed. By the interval PNT of 238 its prime mass is O_K(k); the contribution of proper powers is O_K(√n log² n)=o(k). Thus r≪_K 1/log(n/k)→0.

If k≤n^(7/10), fix a primorial Q. In each interval of length ≤k/j, the number of integers coprime to Q is ≤(k/j)φ(Q)/Q+O(Q) by periodicity. Among the non-coprime ones only powers of the prime divisors of Q contribute; in (x,2x] there is at most one power of each. Bounding the weight by log(2x) and dividing by k log(n/k)≥0.3k log n, one is left with limsup r≪_K φ(Q)/Q for k→∞. The Euler product allows this last ratio to be made arbitrarily small. The two cases and the extraction of subsequences prove the stated sequential uniformity.

**Minimal cost to evade the barrier on the primes.** Allow at each x a positive mixture of binomials with integer arguments up to Kx, with sum of coefficients B(x) and total cost L(x)=Σ a_i log binom(n_i,k_i). For each ε>0 there exist k₀ and x₀ such that r≤1/(2 log 2)+ε if k_i≥k₀ and x≥x₀, by the sequential result. The remaining binomials cost in total at most k₀ B(x) log(Kx), by symmetry of the split. Hence:

    local atomic mass ≤ (1/(2 log 2)+ε)L(x) + k₀ B(x)log(Kx).

If the mixture majorises g(p/x) of 257 merely at the primes x<p≤2x, its local mass is at least xh+o(x) by PNT and partial summation, with h=∫g. Even that purely arithmetic condition forces liminf L(x)/(xh)≥2 log 2 when B(x)=o(x/log x). More quantitatively, saving a fixed fraction η>0, i.e. L(x)≤(2 log 2−η)xh, forces B(x)≥c_(K,η)x/log x for large x; choose ε sufficiently small in the inequality above.

The order of coefficients is optimal: for each prime x<p≤2x use binom(p,1)=p with coefficient g(p/x). Its carry at m≥2 equals one exactly if m divides p. Thus it reproduces the weight at each prime and loads no proper power, with B(x)∼xh/log x and L(x)=Σg(p/x)log p∼xh. This construction again pays exactly the sum one seeks to bound; it does not by itself give a square-root margin.

**Distinction.** 258 explicitly left open the transfer of its geometric bound to the atoms. Here it is proved for budgets sublinear in x/log x and a mechanism that breaks the bound on reaching that scale is located. 259 allows subtractions; the atomic barrier proved here refers to positive coefficients. Arguments larger than a fixed multiple of x are not treated.
