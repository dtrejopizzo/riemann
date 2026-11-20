# Two sectors of simple primes compensate in their signed mean

Let P_h be the simple-prime observable of 353. For large X fix log y=log X/(20 log log X). Split P_h=U_h+V_h according to whether the cofactor m of pm has all its primes ≤y (including m=1) or at least one greater than y. Then, uniformly for 0<h≤1,

    ∫_[X,2X] U_h dx/x ∼ e^(−γ) X(1−e^(−h))/log y,
    ∫_[X,2X] V_h dx/x ∼ −e^(−γ) X(1−e^(−h))/log y.

The second equivalence asserts a real compensation between whole sectors of the sum of 353. What is measured is the linear mean over centers; the full second moment remains open.

**Mean of the smooth sector.** By exact integration of each indicator, the first integral is the integral in v from 0 to h of

    Σ_{m smooth} μ(m)[θ(2Xe^(−v)/m)−θ(Xe^(−v)/m)].

For m≤√X the prime number theorem with relative error O_A((log X)^(−A)) gives the main term Xe^(−v)/m, with that relative precision, uniformly in v. The sum of the absolute weights 1/m over the smooth squarefree m costs O(log y) by Mertens' product. For m>√X use θ(t)≪t and Rankin's bound with α=1/log y:

    Σ_{m>√X, smooth} μ²(m)/m ≤ X^(−α/2)∏_{p≤y}(1+p^(−1+α)) ≪ (log X)^(−10) log y.

Indeed p^α−1≪α log p for p≤y and Σ_{p≤y} log p/p≪log y. The same tail allows completing the main term. The exact product ∏_{p≤y}(1−1/p)∼e^(−γ)/log y remains. The errors are integrated over length h and 1−e^(−h) is comparable to h throughout the range.

**Mean of the complementary sector.** For the full summatory function B(t)=Σ_{pm≤t}μ(m)log p one has B(t)≪_A t/(log t)^A for each fixed A. Indeed by the identity of 353 it is the sum of −Σ_{n≤t}μ(n)log n and −Σ_{k≥2,p^k≤t}(log p)M(t/p^k). The first term has that saving by the classical Mertens estimate M(t)≪_A t/(log t)^A and partial summation. In the second, for p^k≤√t the same saving is applied to M(t/p^k) and the convergent series Σ_{k≥2,p}(log p)/p^k is summed. For p^k>√t the absolute cost is O(t^(7/8)), since Σ_{k≥2,p}(log p)/(p^k)^(3/4)<∞. Hence the full mean is ∫_0^h [B(2Xe^(−v))−B(Xe^(−v))]dv ≪_A hX/(log X)^A. Subtracting the first equivalence gives the second.

**Decision for the route.** At h=X^(−δ) with δ≤1/16, these two mean values separately already exceed the norm budget √(hX)X^ε log X for ε small enough. One cannot add the norms of the two sectors to close 353. A step preserving the compensation could, for example, center both sectors in each dyadic block, but here only the full mean with logarithmic saving is controlled, not its fluctuations nor the mean at root scale. Mertens and Rankin are classical inputs; the separation is recorded as a specific diagnostic for the obligation on simple primes of 353.
