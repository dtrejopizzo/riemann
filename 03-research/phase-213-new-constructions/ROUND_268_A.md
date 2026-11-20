# Necessary separation of the binomial endpoints in a fit of square-root cost

Let x be an integer, N=2x and g the weight of 267. Group real coefficients a_(n,k) by endpoint n≤N, with 1≤k≤n/2 by symmetry. Write V_n=Σ_k |a_(n,k)|. If the response R coincides with g(p/x) at all primes p≤N, then for every fixed ε in (0,1/3), with H=x^(1/6+ε), one has for x sufficiently large

    Σ_n (H+N−n)V_n ≫ x.

In particular, with a single endpoint N one needs ≫ x^(5/6−ε) units of variation, even allowing arbitrary coefficients. If all endpoints lie in [N−D,N], the cost is ≫ x/(H+D). This rules out a cost x^(1/2+o(1)) for D≤x^(1/2−η), with any fixed η>0.

**Three primes near three positions.** By 267 there is a closed interval I of positive length, interior to (2/3,1), and c>0 with |g(2r)−g(2−r)|≥2c on I. For all t∈xI except a set of measure o(x) choose primes p,q,s in the intervals of length H starting respectively at t, 2t and N+1−t. This uses the prime number theorem in almost all short intervals of length X^(1/6+δ); one may take δ=ε/2 and cover the three regions by a fixed number of dyadic pieces. Each affine change of variable preserves the o(x) estimate for the exceptional measure. By continuity, |R(q)−R(s)−R(p)|≥c: p lies below x, q and s above.

**Effect of each endpoint.** Let A_n(u)=Σ_(k≥u) a_(n,k) for positive integer arguments. By compactness of I choose a small fixed η₀>0. For n≥N−η₀x, the counting formulas of 267, applied with endpoint n, give exactly

    R_n(q)=A_n(n+1−q),     R_n(s)=A_n(n+1−s),
    R_n(p)=A_n(n+1−2p)−A_n(p).

Indeed q,s lie between n/2 and n, and p lies between n/3 and n/2 with a margin proportional to x. For the three primes and n in that range, all arguments of the tails shown are positive and ≤⌊n/2⌋+1. The two differences of tails are bounded by sums of |a_(n,k)| over two intervals. The first is centered at n+1−2t with radius 3H; the second at t with radius N−n+2H. Integrating in t, each k counts on a set of measure O(H+N−n), by the slopes −2 and 1 of the centers. These bounds depend only on t and H; the choice of the primes requires no independence. For endpoints n<N−η₀x one uses |R_n(q)−R_n(s)−R_n(p)|≤3V_n because the carries are zero or one; after integration this costs O(x V_n)=O((N−n)V_n). Summing the bounds and integrating over the good t yields the announced inequality.

**Scope.** The proof also tolerates a uniform error less than c/6 per prime, taking c for the exact separation. It uses no fit on composites, no scalar entropy condition, and no restrictions on the sign or the sum of the coefficients. For families with sufficiently separated endpoints the inequality leaves the construction of 262 open. The external input is limited to the existence of primes in almost all intervals; the deduction about the endpoints is a comparison of three carry responses. [Statement of the short-interval result in the notes of K. Matomäki](https://math.mit.edu/~drew/MITNT/KaisaMatomakiSlides.pdf).
