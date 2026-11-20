# How much inclusion-exclusion the value of the original sieve requires

Keep Y, N∼λx^(3/2) and the weight f from the translations section of 042. In this round h=0 in all moduli. For n with Y<n≤N write r(n)=#{p≤Y:p divides n}. Let V be the exact value, that is, x^(−1/2)Σf(n)1_{r(n)=0}. In V_k replace the indicator by Σ_{j=0}^k(−1)^j binom(r(n),j). For each constant 0<α<1 and any integer k with k∼α log x/log log x, one has

    |V_k−V| = x^(1/2−α+o(1)).

For odd k, V_k is a lower bound. One can choose odd k with any α>1/2 less than one and obtain a minorant at distance o(1) from the original value. For α<1/2 the loss diverges in absolute value. These statements do not fix the behaviour of a particular sequence at the threshold α=1/2.

**Uniform upper bound.** For r>0, the truncated sum is (−1)^k binom(r−1,k), with value zero when k≥r. For r=0 there is no error. On the whole support f(n)≥0 for large x, since the positivity proof of 042 only uses n>Y, and f(n)≤log(N)w(n/x). The error therefore has a single sign and its absolute value is bounded above by replacing binom(r−1,k) with binom(r,k+1). The latter counts the squarefree divisors of n with k+1 distinct primes ≤Y. For any d≥1,

    Σ_{m≥1} w(dm/x) ≤ C x/d.

If d≤x split at m=x/d and sum m or m^(−2) in the corresponding branch. If d>x the sum is ζ(2)(x/d)². Summing over divisors first one deduces

    |V_k−V| ≤ C √x log(N) (Σ_{p≤Y}1/p)^(k+1)/(k+1)!.

The sum of reciprocals is O(log log x); the logarithm of its power is o(log x) for this k. By Stirling, log((k+1)!)=(α+o(1))log x. This gives the exponent of the upper bound.

**Lower bound at phase zero.** Take D the product of the first k+1 primes. By the prime number theorem log D∼k log k and the largest of its primes is O(log x), smaller than Y. Thus D=x^(α+o(1)) and there are (1+o(1))x/D multiples of it in [x,2x]. All of them belong to the support of the weight f for large x. There f(n)=(1−c)(x/n)²log n≳log x and binom(r(n)−1,k)≥1. Without cancellations, these integers contribute to the absolute error at least a constant times √x log x/D. This completes the equality of exponents.

**What the result estimates.** V_k is expressed through ordinary sums of f over multiples of products of at most k sieve primes; no average over phases intervenes. The computed cost is the error of truncating that concrete formula, not the error of V with respect to (3/2)√x. It remains to prove V_k≥(3/2)√x−O(1) for some odd choice of sufficient depth. There is no barrier here for other sieve weights. R166_601 already uses Legendre inclusion-exclusion, and the index records the Selberg identity as a route already travelled; that identity has not been reopened. What is specific to this cross-check is the depth threshold at additive precision O(1) for 042.

## Does optimising the coefficients of the counting polynomial help?

With the notation above let L_x(P)=x^(−1/2)Σ_{Y<n≤N} f(n)|1_{r(n)=0}−P(r(n))|. For any k∼α log x/log log x with 0<α<1,

    inf_{deg P≤k} L_x(P) = x^(1/2−α+o(1)).

The same exponent holds when the infimum is restricted to pointwise minorants. Real coefficients depending freely on x are allowed. Approximation in absolute error matters: for polynomials without sign restriction no lower limit is claimed for the error after cancelling positive and negative deviations.

**Every necessary counting level has mass.** For each j=0,...,k+1 write D_j=∏_{i≤j}p_i, D₀=1. Uniformly in j, D_j≤x^(α+o(1)) and p_j=O(log x) for j≥1. One can find at least x^(1−α−o(1)) integers in the support with r(n)=j and with f(n)≥x^(−o(1)):

* If D_j≤x/(2Y), use n=D_j q for primes x/D_j<q≤2x/D_j. Then q>Y and r(n)=j. The number of choices is ≫x/(D_j log x).
* In the other branch j≥1. Put T=min(Y,x/D_{j−1}) and use n=D_{j−1}q with q prime in (T/2,T]. Now D_{j−1}T=min(D_{j−1}Y,x)>x/(2p_j) or equals x. Hence T≥x^(1−α−o(1)), q>p_j for large x and q≤Y. One obtains r(n)=j with ≫T/log x choices.

The estimates for primes in intervals of ratio two are uniform because the smallest endpoint used tends to infinity. In both branches n lies between x/(C log x) and 2x, so it belongs to (Y,N]. If n≤x the ratio of the corrector c(x/n)² to w(n/x) is c(x/n)³=o(1) uniformly, using 042. If n≥x that ratio is c=o(1). On the whole interval f(n)≫1 for large x. Consequently the normalised mass of each level j in the list is at least x^(1/2−α−o(1)).

**Algebraic obstruction.** The difference of order k+1 of P at the integers 0,...,k+1 is zero; for the indicator of level zero its absolute value is one. The sum of the absolute values of the coefficients of that difference is 2^(k+1). Therefore at some level j the deviation has absolute value at least 2^(−k−1)=x^(−o(1)). Multiplying by the mass of that level proves the lower bound, uniformly in the coefficients. For the upper bound one can choose the largest odd order ≤k in the Bonferroni minorant of the previous section. Its error does not change sign and attains the stated exponent.

Thus, within the class that uses only the number of distinct sieve factors, modifying the coefficients does not lower the first-order depth threshold. The proof does not apply to weights that distinguish which primes divide n, nor does it control the signed value of the minorant of sufficient depth.

**Weights that do distinguish the primes: a partial barrier.** There is moreover a different lower bound for polynomials of degree ≤k in *all* the indicators 1_{p|n}, p≤Y, with no symmetry in their coefficients. They can be taken multiaffine since the variables are Boolean. For 0<α<3/4 the weighted L¹ error of any of these polynomials is at least

    x^( min(1/2−α, 3/4−2α) − o(1) ).

Indeed restrict to the cube of the first k+1 primes, setting the other variables to zero. At its vertices the target indicator is one only at the empty vertex. The mixed difference in the k+1 variables annihilates any monomial of degree at most k, and equals ±1 on the target. Some vertex therefore has error ≥2^(−k−1).

For *each* vertex S, let d be the product of its primes and T=max(Y,x/d). Take n=dq with q prime in (T,2T]. Thus the exact set of small prime divisors is S, even in the variables outside the cube. One has x≤n≤2 max(x,Yd)≤N for large x since d≤x^(α+o(1)) and α<3/4. There are ≫T/log T choices and each contributes x^(−1/2)(1−c)(x/n)² log n to the mass of the vertex. Since log n≥log T, the mass is ≫x^(3/2)/(d² T). In the two branches this is respectively x^(3/2)/(d²Y) or √x/d. The worse of these orders gives the stated bound. Multiplying by the pointwise error of the localised vertex completes the proof.

Therefore even weighting each intersection according to the primes that make it up does not allow bounded loss when α<3/8. For α≤1/4 the lower exponent of this class coincides with the Bonferroni upper one. For 3/8≤α<1/2 this proof does not decide whether such weights can attain loss O(1). These conclusions require absolute error or pointwise minoration.

## A shorter minorant that uses the unsieved part of the logarithm

For n in the support, compute

    A(n)=1−[Σ_{p≤Y} ν_p(n) log p]/log n,

where ν_p counts multiplicity. It only requires divisions by the sieve primes. It is the fraction of the logarithm of n that remains after removing those factors. It satisfies 0≤A≤1, equals one on the free integers and zero if all the primes of n are ≤Y. Multiply by A(n) the truncated Bonferroni polynomial B_k(r)=Σ_{j≤k}(−1)^j binom(r,j), with initial index j=0. For odd k one obtains a pointwise minorant of the coprimality indicator. Denote by W_k the value when summing it with the same normalised weight of 042.

For 0<α<3/4 and k∼α log x/log log x one has exactly at the scale of exponents

    |W_k−V|=x^(min(1/2−α,3/4−2α)+o(1)).

In particular any fixed α in (3/8,1/2) already gives error o(1), taking k odd. The modification uses both the valuations and the value of n, so it is neither a polynomial only in the count nor only in the indicators of small prime divisors.

**Upper bound.** The first bound of 043 is kept because A≤1 and the indicator is reproduced exactly when r=0. For the second, there can be an error only if n is a multiple of a squarefree divisor d with k+1 primes ≤Y. Moreover, A(n)log n=Σ_{q>Y, e≥1, q^e|n} log q. Bound the absolute value of the Bonferroni remainder by binom(r,k+1), expand both sums and use f(n)/log n≤(x/n)². By coprimality of d and q, the sum of n⁻² over their common multiples is ζ(2)/(dq^e)² if extended to all multiples. This yields

    |W_k−V| ≤ ζ(2) x^(3/2) [Σ_{q>Y prime} log(q)/(q²−1)]
                             [Σ_{d|P, ω(d)=k+1} d^(−2)].

The first bracket is O(1/Y) by Chebyshev and partial summation. Each d in the second is at least the product D of the first k+1 primes, which is x^(α+o(1)). Moreover, the sum of the inverses of those d is at most (Σ_{p≤Y}1/p)^(k+1)/(k+1)!=x^(−α+o(1)) as an upper bound. The result is ≤x^(3/4−2α+o(1)).

**Lower bound.** With T=max(Y,x/D) take n=Dq for primes T<q≤2T. Then r(n)=k+1, the error of B_k has absolute value one and A(n)log n=log q. All these integers belong to [x,N] for large x since α<3/4. Since the errors have a single sign, their normalised contribution is ≫x^(3/2)/(D²T), using that there are ≫T/log T primes in that interval. This gives the stated exponent in both branches of T. The critical case α=3/8 is not decided for sequences k given only to first order.

**What remains to be proved.** The modification avoids large losses on integers composed exclusively of small primes. This gain is certified before estimating the signed value of W_k. To conclude the sign one still needs W_k≥(3/2)√x−O(1). Optimality against all minorants that use valuations has not been proved. Cross-check: the logarithmic decomposition is classical and was used in 041; R166_601 treats sieving by small factors. What is additional is the error of its combination with the truncation of 043. Construction and both exponents independently audited.
