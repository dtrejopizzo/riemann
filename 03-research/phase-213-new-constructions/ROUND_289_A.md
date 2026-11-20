# Widening the filter with local repair: logarithmic gain and semiprime barrier

Keep Q,δ,κ,N of 288. For r>1 define L(r) as the sum of 2^(−ω(r))Wδ(log(a/b)) over distinct ordered coprime pairs with ab=r; put L(1)=0. For every squarefree n one has exactly

    Q(n)−μ(n)=Σ_(mr=n) μ(m)L(r),     Σ_(d|n) Q(d)=1_(n=1)+L(n).

The second formula inverts the first only within the divisors of the squarefree integer. Every active L(r) has r>N/κ², since |a−b|≥1 and |a−b|√(N/r)<κ. Thus all signs μ(m) of the correction can be obtained with m<κ².

**Repaired majorant.** On squarefree integers add to Q(n) the quantities L(r) with mr=n and μ(m)=−1; on the others keep zero. The result Q⁺ majorizes μ and Q pointwise. For 1≤κ≤N^(1/4) one obtains

    Σ_(n≤N)|Q(n)−μ(n)|,  Σ_(n≤N)(Q⁺(n)−μ(n))
       ≪ κ √N log(2κ)/(log(2N))^(3/4).

In particular κ=(log N)^(3/4)/log log N allows a growing width and an absolute cost O(√N) on all subintervals. For the criterion of 287 it is no longer necessary to restrict the width to the first sign change.

**Proof of the ceiling.** Sum the moduli of the terms of the first identity, even before grouping by n. For each m≤κ² and integer difference 1≤h<κ/√m there remains a sum over a≤A=√(N/m), b=a+h. By coprimality and squarefreeness, the weight is the product of μ²(a)2^(−ω(a)) and the same function at a+h. Drop the remaining restrictions and apply Cauchy–Schwarz. Since h≤A and A≥N^(1/4), the sum costs O(A/(log N)^(3/4)), uniformly in h.

To verify the elementary estimate used, let g(j)=μ²(j)4^(−ω(j)). By decomposing log j into primes, Σ_(j≤t)g(j)log j ≤(1/4)Σ_(u≤t)g(u)θ(t/u)≪t Σ_(u≤t)g(u)/u. The finite Euler product and Mertens' estimate for prime reciprocals bound the last factor by O((log(2t))^(1/4)). Separating j≤√t and dividing by log(√t) in the rest gives Σg(j)≪t/(log(2t))^(3/4). Finally sum over h and use Σ_(m≤κ²)1/m≪log(2κ); a factor two accounts for both orientations.

**Unconditional barrier.** For C log N≤κ≤N^(1/4), with C sufficiently large, already on products n=pq of two distinct primes one has

    Σ_(n=pq≤N) (Q(n)−μ(n)) ≫ κ √N/(log N)².

For these integers the only nontrivial factorization that can be close to balance is (p,q) and its inverse: the partition (1,pq) is outside the support and the prime divisors of n have no nearby factorizations (δ<log 2). Hence there is no negative compensation at any semiprime with distinct primes. Divide [.6√N,.8√N] into O(√N/κ) boxes of length ≤κ/10 and comparable to κ. The PNT gives ≫√N/log N primes in total. Cauchy–Schwarz applied to their occupancies and the identity for the number of distinct pairs give ≫κ√N/log²N pairs within the same box for large C. For each, log(q/p)≤κ/(6√N) and Wδ≥1/2 for large N. The correction is therefore ≥1/4. Each integer produced is distinct up to the order of its two factors.

In particular κ=N^α with 0<α≤1/4 makes it impossible for a procedure that only ADDS terms to Q to majorize μ to have total excess N^(1/2+o(1)). This barrier does not rule out a correction that also decreases Q on identified products. Nor does it prove a one-sided ceiling for the sum of Q⁺. The new datum compared to 288 is the quantitative budget at a growing width and the arithmetic obstruction independent of the sign at the other integers.
