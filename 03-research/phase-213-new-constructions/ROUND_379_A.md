# Sign of the whole sector with a single prime above a second scale

**Status: PROVED, with independent review of the Laplace product and of the errors for each fixed a in (0,1).**

With L=log x, z=L², b=L^a, y=exp b and fixed 0<a<1, restrict S of 368 to the integers with exactly one prime factor >y. The other prime factors may form any subset of (z,y]. Then the balance of the sector satisfies

    S_uno ∼ −J (x/L) ∏_{z<p≤y}(1−1/p) ∼ −J (x/L) log z/b,
    J=∫ exp(−u)g(u)du.

In particular the compensation takes place here among all small multiplicities simultaneously, for each large x. 378 used only an interval of cofactor primes and an absolute count in a prescribed layer.

**Separation of the large prime.** Write n=mp, p>y, with m a divisor of the product of the primes of (z,y]. The sign is −μ(m). For Y=x/m one has Σ_p g(log(Y/p))≪Y for all Y>0 by dyadic summation over all integers. On m>exp(L/2) one therefore loses O(x exp(−L/(2b)+O(log L))) even in absolute value: insert (m/exp(L/2))^(1/b) into the reciprocal sum and use ∏(1+p^(−1+1/b))≤exp(O(log L)) by Mertens. This error is smaller than the main term.

If m≤exp(L/2), restricting to |u|=|log(Y/p)|≤√L costs O(Y exp(−cL)) in absolute value, by the same dyadic count. There p>y automatically for large x. The classical PNT with relative remainder O(exp(−c√L)) replaces the sum by

    Y ∫_{|u|≤√L} exp(−u)g(u)/(L−log m−u) du

with error O(Y exp(−c'√L)). Indeed, integrate by parts against π(t)−li(t) on [Y exp(−√L),Y exp(√L)]; the boundary terms and the integral are bounded using ∫exp(−u)|g'(u)|du<∞. Summing the errors over m costs a factor exp(O(log L)).

**Keeping the sign when summing the cofactors.** Represent the inverse of the denominator D=L−log m−u via ∫₀^∞ exp(−Dt)dt. It can be cut at 1/b with error O(exp(−L/(3b))) per term since D≥L/3. On 0≤t≤1/b extending the sum over m to all divisors costs, after removing the factor x, at most exp(−L/(2b)+O(log L)): apply Rankin again to Σ_{m>exp(L/2)} m^(−1+t) with margin 1/b, using p^(t+1/b)≤exp(2). The factor exp(ut) is integrated against exp(−u)g(u), with uniformly bounded exponential moments. What remains is the integral in t with weight exp(−Lt), integrated Gaussian factor and product

    P(t)=∏_{z<p≤y}(1−p^(−1+t)).

It is positive and decreasing on this interval. Moreover |(log P)'|≪Σ_{p≤y} (log p)/p≪b, since p^t≤e and p>z. For t=v/L with v fixed, P(t)/P(0)→1. The factor integrated in u converges to J and is uniformly bounded. Changing to v=Lt, domination by C exp(−v) and L/b→∞ give the announced equivalent, with the minus sign of the distinguished prime. Mertens gives the last equivalent. The previous absolute errors are negligible even after dividing by P(0)/L.

The part with zero primes >y also costs O(x exp(−L/(2b)+O(log L))) plus O(x exp(−cL)) by splitting m around exp(L/2) and using the Gaussian weight for small m (the first cost uses g(log(x/m))≪x/m). By 377 the part with at least two primes >y must compensate the negative balance to first order: the complete pulse is O(x exp(−cL/h))=o(xP(0)/L), and the sector with zero large primes is also o(xP(0)/L). The sign of the residue of that compensation is not obtained.

**Review record.** The factorization n=mp is unique, since exactly one prime >y is required and all factors are distinct. For m≤exp(L/2) and |u|≤sqrt L, one has p≥exp(L/2−sqrt L)>y and D≥L/3, uniformly in m for each fixed a<1. The error from cutting the Laplace integral is O(x exp(−L/(3b)+O(log L))); when extending the cofactors on 0≤t≤1/b, Rankin with margin 1/b uses p^(t+1/b)≤e² and gives the stated error. After dividing by the main term, all these errors tend to zero because L/b=L^(1−a)≫log L. For dominated convergence, P(t)/P(0)≤1 and |log(P(v/L)/P(0))|≪bv/L→0 for each fixed v. The complete Gaussian moment is exp((t−1/2)²/2), uniformly bounded on 0≤t≤1/b, and its value at t=0 is J=exp(1/8). This justifies domination by C exp(−v), also after the truncation in u. The estimates are uniform in the cofactors and in t; no uniformity is claimed when a=a(x) tends to 1.
