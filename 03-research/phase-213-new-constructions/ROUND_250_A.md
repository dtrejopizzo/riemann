# Blocks of length p^a that preserve the barycentre when primes are lost

Fix 3/4<a<1. For a prime p set h=p^a and N=#{r prime:p<r≤p+h}. Let M(p) be the largest integer 0≤m≤N such that removing ANY set of up to m of those primes leaves C(y)>0 on ALL of p≤y≤p+h. Set M=0 if it already fails without removing anything. With Θ from 249 one has

    limsup_(p prime→∞) log(1+M(p))/log p = min(a,1+Θ−a).

Under RH one moreover has, uniformly over all large primes,

    M(p) ∼ p C(p)/(2h log p).

In particular there are unconditionally, for each fixed a, arbitrarily distant primes with whole positive blocks tolerating p^(3/2−a−ε) arbitrary deletions for any ε>0. For example a=7/8 gives length p^(7/8) and allows p^(5/8−ε) deletions. The guarantee of 249 for deleting ALL new primes reached unconditionally, along a subsequence, length 0.41p^(3/4).

**Variation of the count.** For y close to x, the bound of 235 by partial summation gives C(y)=O_ε(x^(Θ+ε)) and |C'(y)|=O_ε(x^(Θ−1+ε)) between primes. For the derivative integrate −u k'(u) against dθ(xu) and divide by x. The main term disappears since k(1)=0 and ∫₀¹k=0. Continuity when a prime enters gives the same bound for integrated increments across the nodes. Each new prime r≤y contributes to C(y) an amount between zero and (2+o(1))h log p/p by the weight k(r/y), uniformly on the block.

**Ceiling for the number of deletions.** It is always ≤N≤h+1. When Θ<2a−1, in the first half of the block there are ≫h/log p primes by 238; each one contributes to C(p+h) at least c h log p/p with absolute c>0. Deleting more than O_ε(p^(1+Θ+ε−a)/log p)+1 of them suffices to make C(p+h)≤0 (if it already fails none is required). For sufficiently small ε there are enough candidates. This gives the announced ceiling including the boundary by the trivial limit.

**Subsequential floor.** If Θ>1/2, fix d<Θ close to Θ and small ε with d>Θ−1+a+ε and d>1/2. By 249 there are arbitrarily large x with C(x)≥x^d. Passing to the next prime p, at distance O(x^(5/8)) by 238, and running up to p+h costs altogether O(x^(a+Θ−1+ε))=o(x^d). Hence C(y)≥x^d/2 persists. The individual bound above allows deleting floor(p^(min(a,1+d−a)−ε)) arbitrary primes, and 238 guarantees there are that many. Let d↑Θ and ε↓0.

**Why the individual cost gives the constant under RH.** From 247 one obtains C(x)/√x=4/15−Σ K(ρ)exp(i Imρ log x)+o(1), an absolutely convergent series and therefore uniformly continuous as a function of the logarithm in its oscillatory part. This implies C(p+v)=C(p)+o(√p) uniformly for 0≤v≤h, with C(p)≥0.17√p for large p. Set m₀=p C(p)/(2h log p). For any 0<η<1, deleting up to (1−η)m₀ nodes preserves the whole block by the individual ceiling. For the converse fix 0<τ<1 with (1+η)(1−τ)>1. By 238 in (p,p+τh] there are ≫_τ h/log p primes, many more than m₀ since a>3/4. Each one contributes at p+h at least (2−o(1))(1−τ)h log p/p. Deleting ceil((1+η)m₀) of those primes makes that endpoint negative. Since η is arbitrary and m₀→∞, the equivalent and the floor when Θ=1/2 follow.

**Consequence for closure.** For a single fixed choice of a>3/4, it would suffice to establish M(p)≤p^(3/2−a+o(1)) at all large primes. Both a and 1+Θ−a would be strictly greater than 3/2−a if Θ>1/2. This upper bound remains open. The unconditional result on blocks does preserve the authentic primes outside the deleted ones and does not cover all starting points.

**Exact evaluation without searching among subsets.** For sufficiently large p, removing the first m primes after p minimises the count simultaneously at ALL points y of the block among all choices of up to m. Indeed, for p<r≤y the derivative with respect to r of the weight (log r)k(r/y), multiplied by y, is k(z)/z+(log r)k'(z), z=r/y. On this stretch z→1 uniformly, k'(1)=−2 and the term is negative. The r still above y contribute zero. The list of contributions in prime order is therefore nonincreasing and nonnegative. The minimal count is obtained with an artificial initial gap of length m in number of primes, followed by all remaining primes unchanged. To prove its sign on the whole block one only needs to evaluate the two endpoints and the kept primes: the concavity argument for y²C(y) of 247 holds for any fixed list. This turns the obligation of bounding M from above into the search for a single point that fails after removing a determined prefix.
