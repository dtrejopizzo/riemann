# Cutting by the squarefree part, and a positive subsum after pairing

In 051 complete rows were estimated when p|m. The restriction sf(km)≤S depended on m and was left without signed control. Here that restriction is factored so as to keep the saving uniformly in S. One also checks what happens when pairing the even and odd indices in the open case p∤m.

**Uniform cutoff.** In the repeated rows of 051 with e≥2 put k=p^e v, m=pw, W=y/(pk) and d=sf(p^(e+1)v). It suffices to consider w squarefree and coprime to p. Put b=gcd(w,d). Then b|v since it is squarefree and p∤b. Write w=bz. For each b|d coprime to p, the summands corresponding to it are exactly the squarefree z with gcd(z,pd)=1. One has

    sf(km)=d z/b,   μ(m)=−μ(b)μ(z).

Thus sf(km)≤S only introduces the upper endpoint z≤Sb/d in a sum with weight V(z/(W/b)).

To justify uniformity, let D=pd. The sum of μ(n) for n≤u coprime to D is Σ_h M(u/h), where h≤u has all its primes in D. This follows by convolution, comparing the factor at each prime power. For h≤√u apply the quantitative PNT for M and for h>√u use M(u/h)=O(u/h). The sum of h^(−1/2) over these integers is ∏_{q|D}(1−1/√q)^(−1). This product costs at most C^(1+ω(v))≤C v^C, because only p and the primes of v intervene. Since v≤C(log x)², the factor is polylogarithmic. The remainder h>√u costs O(u^(3/4) v^C). On the support of the weight u is comparable to W/b, and W/b≫L^(1/2)/(log x)^C by 051. Therefore partial summation, also with an arbitrary endpoint, costs O_N((W/b)/(log x)^N) for any N, choosing a larger exponent in the PNT. The jump due to the endpoint costs the same bound. The number of possible b is at most v. The sum over p,e,v of 051 absorbs all these factors and gives O_A(L/(log x)^A) **uniformly in S**. The same estimate holds on any interval of sf by difference.

In particular, for some fixed c>0, the original sum of 050 restricted to sf(km)≤c L/(log x)^4 is O(L) in absolute value **after summing with the original signs**. Choose c smaller than the constant of the lower bound of 051 for the rows p∤m. The repeated rows with e=1 cost O(L) in absolute values. This allows cutting the set of products itself, even if k admits several labels, by linearity. At the extreme of 051 the sum of absolute values can be larger.

**A pairing that still needs compensation.** Separately, restrict the expansion of 051 to the row of primes 3L<p<4L and group by t=vm. The combined row weight in v is log(p)(1−2·1_{2|v})U(pv); the compensation of 050 lives below 2L. For t=q and t=2q, with q a prime different from p and pq/y or 2pq/y in the fixed support of V, q is comparable to L. The divisors v containing q lie above the cutoff. The v=1,2 give U(p)=U(2p)=1 for large x. The joint contribution is therefore

    Σ_{3L<p<4L} log p Σ_{q prime, q≠p} [2 V(2q/X)−V(q/X)],    X=y/p.

By the quantitative PNT and partial summation with fixed V, Σ_q V(q/X)=X∫ V(t)/log(Xt) dt+O_N(X/log^N X). In the difference above the continuous density is X V(t)[1/log(Xt/2)−1/log(Xt)]; integrated it equals X(log 2)∫V/(log X)²+O(X/(log X)³). Eliminating q=p costs O(L) in the whole sum by Chebyshev. Given that Σ_{3L<p<4L}(log p)/p→log(4/3), the signed subsum is asymptotic to

    y log(4/3) log(2) (∫V)/(log L)².

It is positive and exceeds the tolerance O(L). It is not a global counterexample: it shows that even the pairing of these two families requires compensation from the rest of the sum. The divisor identity and finite differences have antecedents in 042–043 and in phase 188; the evaluation here concerns the weight and the cutoff of 049–051. The sign of the total complement remains open.
