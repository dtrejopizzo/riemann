# Optimal loss of a positive divisorial minorant at variable scale

In 040 the fixed profile was discarded. Here the coefficients b_n≥0 may be chosen anew for each x>1. At n=1 one may fix b₁=0. Let w(t)=min(t,t^(−2)), as in 040. For an integer cap N on the support, maximize

    x^(−1/2) Σ_{n≤N} b_n log n

under the constraints Σ_{n≤N:p^e|n}b_n ≤ w(p^e/x) for each prime p and e≥1. Constraints are only needed where Λ does not vanish. By the divisor identity, each admissible family is a minorant of Q(x) of 039. Call M_N(x) the maximum.

**Exact solution.** Put d_{p,e}=min_{1≤i≤e} w(p^i/x). Then

    M_N(x)=x^(−1/2) Σ_{p^e≤N} (log p)d_{p,e}.

Indeed the masses accumulated by the multiples of p^e are decreasing in e, so d_{p,e} dominates them term by term. The decomposition of log n gives the upper bound. To attain it, on each chain truncate d to zero from the first power greater than N and put b_{p^e}=d_{p,e}−d_{p,e+1} with those truncated values. At the other integers put zero. Telescoping saturates all bounds simultaneously. With infinite support the same construction attains the limit M∞, by monotonicity and convergence of the sum dominated by Q(x). Among finitely supported sequences without a prescribed cap that limit is a supremum.

**How much the constraints cost.** The first level e=1 keeps the full weight of each admitted prime. For the squares d_{p,2}=min(p/x,x²/p⁴). Splitting at p=x^(3/5), the Chebyshev bound θ(t)=O(t) and partial summation give

    x^(−1/2) Σ_p log(p) d_{p,2} = O(x^(−3/10)).

Indeed the two pieces are bounded by constants times x^(−3/2)(x^(3/5))² and x^(3/2)(x^(3/5))^(−3). For e≥3 the retained contribution, being at most the full one, is O(x^(−1/6)) by 039. These bounds hold for all N. From 039, the full weight of the squares tends to 2/3; hence

    Q(x)−M∞(x) = 2/3 + o(1).

**Finite cap.** If N≥x and N→∞, the primes greater than N lie entirely on the decreasing branch of the weight. By the previous computations,

    Q(x)−M_N(x) = 2/3 + o(1) + x^(3/2) Σ_{p>N} (log p)/p²,

with the first o(1) uniform in N≥x. By the prime number theorem and partial summation, the tail is asymptotic to 1/N. Thus, for any fixed λ>0, N∼λx^(3/2) gives loss 2/3+1/λ+o(1). In general, to keep the loss bounded it is necessary and sufficient that N≥c x^(3/2) eventually for some c>0. If N<x along a subsequence, the tail of primes >x already costs order √x; for N≥x the previous formula applies.

The additive precision O(1) required in 039 is indeed attainable by a positive minorant if it may be chosen at each scale. The exact construction depends on the primes and keeps their first-level sum. What is pending is a lower bound of M_N(x) by (3/2)√x−O(1) with N of the indicated size; computing the loss does not provide that bound. The divisorial operation already appeared in 040 and N_BUILD022. The cross-check did not locate this chain optimization problem with this weight function.

## Can the coefficients at primes be replaced by products of two primes?

Now impose b_p=0 for each prime p. Denote the new finite maximum by M_N^comp. To keep Q(x)−M_N^comp(x)=O(1) it is necessary and sufficient that N≥c x^(9/4) eventually, for some c>0. For sufficiency it suffices to use products of two distinct primes. The claim concerns the support of the coefficients; their choice still uses the capacities of the individual primes.

**Necessity.** If no such c exists, there is a subsequence with N=o(x^(9/4)). Fix δ>0, P=δ x^(3/2) and consider the primes in (P,2P]. A composite integer ≤N containing one of those primes p contains exactly one, with exponent one, since P²>N for large x. Its cofactor has some prime divisor q≤N/P. Hence the sum of masses assigned to the primes of that band is at most

    Σ_{q prime≤N/P} w(q/x) = o(√x/log x).

Indeed y=N/P=o(x^(3/4)); if y≤x^(2/3) the sum over all integers divided by x suffices. For y>x^(2/3) one uses Σ_{q≤y}q≪y²/log y. Multiplying by log(2P)/√x gives o(1) contribution to the band. Its full weighted capacity, by contrast, is x^(3/2)Σ_{P<p≤2P}log(p)/p²∼1/(2δ) by the prime number theorem. The deficit in each row is nonnegative, so the liminf of the loss along that subsequence is at least 1/(2δ) for each fixed δ. A bounded loss is impossible.

**Sufficiency.** It suffices to build for N=⌊c x^(9/4)⌋, since increasing N preserves feasibility. Choose X=λ x^(3/2), with λ>0 sufficiently small depending on c. The first-level capacities d_p=w(p/x) will be saturated for *all* primes p≤X. The primes p with √N<p≤X are traversed from largest to smallest. Assign their mass d_p to products pq, distributing it among primes q≤y=min(x,N/p) with available capacity. Those partners are less than √N and the allowed sets grow during the traversal. It suffices to verify at each step that the demand accumulated up to the current p does not exceed the total capacity of its partners.

The demand is at most C x²/(p log p) by the Chebyshev bound and partial summation. The capacity available *before starting the whole traversal* at q≤y is at least c₁ y²/(x log y), by the number of primes in (y/2,y]. Here y grows uniformly. If y=x, the demand is o(x/log x) because p>√N. If y=N/p<x, the demand/capacity ratio is at most C′ x³ p/N² ≤ C′ x³ X/N², which is less than one when λ is chosen sufficiently small. Thus the distribution is completed without exceeding capacities.

There remain the residual demands of the primes ≤√N. Their sum L is ≫x/log x: on [x/2,x] alone there was mass of that order and the previous traversal consumed O(x²/(√N log N))=o(x/log x). Each residual demand is ≤1. For large x none exceeds L/2. Divide a circle of length L into consecutive arcs with those lengths; pair each point with the opposite point. Almost no pair has both ends in the same arc. The paired length between two arcs gives a nonnegative coefficient b_pq (count each pair once), with sum at each prime exactly its residual demand. The products are ≤N. This second distribution uses distinct partners and does not activate constraints for p². The value attained is thus exactly the contribution of the primes ≤X. Its loss relative to Q tends to 2/3+1/λ by 039 and the previous tail computation. This is an upper bound on the optimal deficit for this restricted support; it does not identify its optimal constant.

In particular, at the support scale x^(3/2) of the first part, composites alone cannot certify the desired lower bound. Allowing the scale x^(9/4) the sum over primes can be reproduced, but its uniform estimate remains necessary.
