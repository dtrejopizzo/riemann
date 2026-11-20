# The maximal oscillation has root scale in a typical shifted window

For integer D, N=D², take the off-diagonal term of 134,

    Q(x)=Σ_{k≤N}c_k {x/k},  c_k=Σ_{a,b≤D, a≠b, ab=k}μ(a)μ(b).

Let s be uniform real on a common period of the fractional parts, for example [0,lcm(1,…,N)]. Then

    E_s [sup_{0≤u≤v≤N} |Q(s+v)−Q(s+u)|²] ≤ N^(1+o(1)).

Hence for each ε>0 the proportion of shifts where the maximum exceeds N^(1/2+ε) is ≤N^(−2ε+o(1)). The maximum is taken over the whole window, not only over a prescribed pair of points. It applies to each harmonic cut of 134, but the identity representing Mertens requires the original window.

**Estimate of increments.** |c_k|≤τ(k)≤N^o(1). The L² series of {x/k}−1/2 has coefficient −1/(2πi m) at frequency m/k, m a nonzero integer. Regroup equal rational frequencies in lowest terms j/q. The coefficient has modulus ≤(2π|j|)⁻¹Σ_{r≤N/q}|c_{qr}|/r ≤N^o(1)/|j|. Exact orthogonality on the common period and |exp(2πijH/q)−1|≤min(2,2π|j|H/q) give

    E_s |Q(s+H)−Q(s)|² ≤ N^o(1) Σ_{q≤N}min(1,H/q) ≤ H N^o(1)

for 1≤H≤2N. Here the sum in j has been extended to all nonzero positive and negative integers: Σ_{j≥1}min(1,jt)²/j²≪min(1,t).

**From a pair of points to the maximum.** Cover by a dyadic tree of length 2^ceil(log₂ N). Each prefix of integer length is a sum of at most one cell from each level. By Cauchy–Schwarz its squared increment is bounded by O(log N) times the sum of the squares over all cells of the tree. At each level the expectation is O(N^(1+o(1))) by the above bound and translation invariance. For real endpoints, each interval [s+j,s+j+1] contains at most one integer in its interior, and all jumps of Q occur at integers. The slope between jumps satisfies |Σ c_k/k|≤N^o(1). Thus the additional oscillation within each unit cell is controlled by the difference of its endpoints plus twice that slope bound (integer s are null in the integral). This proves the statement.

**Why the shift is not free.** The above proof remains valid when replacing μ(a) by any real coefficients z_a of modulus ≤1. In that class the anchored window can have oscillation ≫D² even with |Σ z_a/a|≤1/D. To see it take z_a=1 on [.94D,.95D], add −1 at consecutive indices of [.80D,.82D] until crossing the harmonic balance and choose the closer of the two neighboring values. There are enough indices by comparing their harmonic sums (their limits are log(.82/.80)>log(.95/.94)). The residue is ≤1/(2·.80D)<1/D. The remaining coefficients are zero. In (.88D²,.91D²] the only multiple of products of the support that appears is the first multiple of each high-high pair: mixed and low-low products are smaller, and the second multiples exceed D². The distinct high pairs contribute ≍D² jumps counted with multiplicity and positive sign to the increment of the floor sum. The off-diagonal fractional slope equals (Σ z_a/a)²−Σ z_a²/a²=O(1/D). Hence the increment of the fractional sum has modulus ≫D². This is a falsifier of the shift inference for bounded coefficients and small harmonic balance; it does not reproduce the multiplicativity of μ.

**Cross-check and scope.** Fourier series of the sawtooth, orthogonality of rational frequencies and the dyadic maximal argument are classical. 134 requires the anchoring for its inversion identity. The computation separates the cost of the simultaneous maximum from the arithmetic problem of the anchoring. An estimate for s=0 with the true coefficients along a subsequence of the harmonic crossings is missing.

The same maximal claim holds for uniform integer shifts modulo the period. For s=k+t with k integer and 0≤t<1, all increments with integer endpoints coincide exactly with those shifted by k: Q(k+t+j)=Q(k+j)+tΣ c_l/l. The real endpoints of the window with integer origin only add to the grid values a slope of size N^o(1) on each piece. This avoids attributing the result to a randomization within the unit cell.
