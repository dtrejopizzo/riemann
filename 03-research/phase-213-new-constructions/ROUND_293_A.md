# Which cofactors can be removed from the self-convolution at square-root cost

For b_t of 292, fix A>1, 0≤δ<1 and y=(log x)^A. Let r_y(n) be the product, with multiplicities, of the prime powers of n whose primes exceed y (empty product 1). In the region n≤x, r_y(n)≤x^δ, the positive and negative masses in magnitude of b_t each satisfy

    Σ max(±b_t(n),0) = x^(1−(1−δ)/A+o(1)),

uniformly for 1≤t≤2. Thus, for 1<A≤2 and δ≤1−A/2 that whole region can be discarded from the sum BEFORE taking its positive part in the criterion of 292. For A=3/2 this eliminates all n whose cofactor above (log x)^(3/2) is at most x^(1/4). For A=2 it includes all n built exclusively from primes up to (log x)². Beyond the indicated boundary each sign separately exceeds the square-root budget.

**Grouping and ceiling.** With u_p=1−Re(χ(p)p^(it))∈[0,2], the local coefficients of b_t at levels 0,1,2 are 1,−2u_p,u_p², and they vanish at higher levels. A complete unweighted packet sums to (1−u_p)², but a cutoff at x can exclude its levels 1 or 2. To include all these boundary effects, factor n=d r with d composed of primes ≤y and r=r_y(n). Take σ=1−1/A>0. Then

    Σ |b_t(n)| ≤ x^σ ∏_(p≤y)(1+2p^(−σ))² · Σ_(r≤x^δ)|b_t(r)|r^(−σ).

By Chebyshev and partial summation, the logarithm of the product is O_A(y^(1−σ)/log y)=O_A(log x/log log x). For the last factor it suffices that |b_t(r)|≤4^ω(r)≤τ(r)²=r^o(1) on its support, uniformly in t. This gives the announced exponent σ+δ(1−σ), also for δ=0.

**Floor for each sign.** For large Z and each t∈[1,2] there are ≫Z/log Z primes p in [.9 Z,Z] with u_p≥3/4, uniformly. Indeed, choose the nonzero class modulo 3 with sign of χ opposite to that of cos(t log Z). Along the interval the cosine varies by at most 2log(10/9)<1/4. The prime number theorem in the two fixed classes gives the count. The exceptional prime 3 plays no role at large scale.

Take k distinct primes from that set with Z=y, with k equal to the integer part of (1−δ)log x/log y or an adjacent integer below to adjust the parity. If δ>0, multiply by a prime q from the same construction with Z=x^δ. For δ=0 do not use q. The products are ≤x and have the required cofactor; different choices give distinct integers. Each coefficient has the sign fixed by the parity and modulus ≥1. If M≫y/log y is the number of small candidates, M/k≫(log x)^(A−1); hence binom(M,k)≥(M/k)^k contributes x^((1−δ)(1−1/A)+o(1)) as a floor on the exponent. The large prime, when applicable, contributes an additional x^(δ+o(1)) choices. Carrying out the construction for both parities proves the two floors.

**Scope.** The positive part is a 1-Lipschitz function: on deleting this region in the admissible range, its integral in t changes by at most x^(1/2+o(1)). The character is still the fixed one modulo 3, with no hypothesis on auxiliary zeros. The floors beyond the boundary only rule out paying for the deletion by summing moduli; they do not rule out a saving by compensation between the two parities. The one-sided bound for the remaining integers is missing. The count of smooth numbers via Rankin is classical; here it is applied with an allowed cofactor and yields the lower exponent of each sign for the real coefficients of the criterion, uniformly in frequency.
