# The growing prefix of layers has negative sign at the exact cut

**Status: PROVED, with independent review of multiplicities, tails and uniformity.**

Let L=log x, h=log L and M_k the positive Gaussian mass of 368 over products of exactly k distinct primes greater than L². There exist an absolute c>0 and x₀ such that, for x≥x₀ and 1≤k≤c√h,

    M_(k+1) ≥ 2 M_k.

Hence every prefix of odd final length j≤c√h+1 has balance Σ_{k=0}^j (−1)^k M_k<0. It is an inequality between masses at the same scale x.

**Grouping by cofactor.** In M_k, the range |log(n/x)|>2√L costs o(1) in total, uniformly in k: in each unit band of u=log(x/n) there are at most e x exp(−u) integers, using the lower end of the band to estimate that number. The sum of weights there costs O(x exp(−2L+O(√L))). In the rest extract the largest prime p and set m=n/p, Y=x/m. We have log p≥(L−2√L)/k and log Y≥log p−2√L≥L/(2k). Let D be the set of cofactors that arise this way. For each of them the mass of all the above p is ≤C Y/log Y: for p≤√Y the Gaussian decay is used, and for p>√Y one sums unit bands in log(Y/p) using π(t)≪t/log t and the same decay.

**Construction of the next layer.** For each m∈D choose a prime q with L²<q≤exp(L/(10k)), q∤m, and a prime r in [Y/q,2Y/q], r∤m. One has r>q, and discarding the at most k divisors of m leaves ≫Y/(q log Y) choices, uniformly by the dyadic PNT. The weight of mqr is ≥min_{[−log 2,0]}g>0. By Mertens the available sum of 1/q is h−O(log h+log(2k))≥h/2, since deleting the divisors of m costs at most k/L². Each product is counted at most k(k+1) times when designating q and r. Thus

    M_(k+1) ≥ c₁ h/[k(k+1)] Σ_{m∈D} Y/log Y
            ≥ c₂ h/[k(k+1)] (M_k−o(1)).

The absolute error is absorbed uniformly: form m from the first k−1 primes above L², all ≤2L² by the PNT. Then log m=O(kh)=o(L); taking p∈[x/m,2x/m] one gets M_k≥exp((1−o(1))L). Choosing c small enough concludes. For k=0, M_0=g(L)=o(1), while M_1→∞.

**Uniformity review.** The bound log Y≥L/(2k) and the choice q≤exp(L/(10k)) ensure r≥Y/q≥exp(2L/(5k))>q and r>L², for all k in the range simultaneously. The number of candidates r before discarding divisors of m is exponential in L/k, so removing at most k does not alter the uniform floor. Given the final product, designating the two distinct primes q,r determines m: there are at most (k+1)k designations, independently of how many original cofactors could produce it. The tail error is O(exp(−L+O(sqrt L))) after summing over all integers, so it is also so for each layer. On the other hand the constructed floor satisfies log M_k≥L−O(kh+h), uniformly; thus absorbing the o(1) does not require choosing a k-dependent subsequence. Finally c can be chosen with c₂/c²>4 and then a common x₀, obtaining the announced factor 2. The case k=0 is used only to pair M₀−M₁; the other pairs of an odd prefix use the inequalities with k even and k≤j−1≤c sqrt h.

**Scope.** Unlike the absolute count of 374, the prefix can be omitted from a one-sided majorant because its contribution is favorable. Omitting it may lose compensation with higher layers. The method only gives a factor h/k² and leaves open the intermediate zone up to the threshold of 374. No external priority is claimed for this counting inequality.
