# Compensation of the sectors of 354 at each center

Take h=X^(−δ), fixed 0<δ≤1/16, H=hX, and the threshold y and sectors U_h,V_h of 354. Put D(x)=x(1−e^(−h))∏_{p≤y}(1−1/p). For every fixed A and **each** center X≤x≤2X,

    U_h(x)= D(x)+O_(A,δ)(H/log^A X),
    V_h(x)=−D(x)+O_(A,δ)(H/log^A X).

The exact product in D is kept so as not to lose precision in the error. In particular ∫U_h V_h dx/x=−∫D² dx/x+O_A(H²/log^A X), adjusting the constants. The compensation occurs at the scale of the main profile in the window itself; root precision remains pending.

**Primes with small smooth cofactor.** For m≤√X the length of the prime window is comparable to hX/m, with endpoint of size z≈X/m≥c√X. For large X that length exceeds z^(0.86). The uniform estimate on primes in short intervals gives the weight θ equal to x(1−e^(−h))/m with relative error O_B(log^(−B) X); passing from Λ to θ the cost O(√z log²z) is absorbed. If the length exceeds z^0.99, divide it into stretches of length comparable to z^0.98, distributing the endpoint among the stretches; summing their relative errors preserves the precision. Summing in modulus the errors over the cofactors costs at most a factor O(log y) by 354. [Guth and Maynard, corollary 1.3 and proof in §13](https://arxiv.org/html/2405.20552v1)

**Large smooth cofactors, uniformly.** For each n of the pulse coming from a squarefree y-smooth m>√X, multiply distinct prime divisors of m until crossing X^(1/4). One obtains a divisor d in [X^(1/4),X^(1/4)y], squarefree and smooth. For large X that whole range lies below H. Hence each d contributes O(H/d) multiples in the window, with no additional boundary cost. The absolute weight of all representations of an n as pm is ≤Σ_{p|n} log p≤log(2X). For every fixed B, apply Rankin with α=B/log y:

    Σ_{d≥X^(1/4), smooth} μ²(d)/d ≪_B (log X)^(−5B) log y.

Indeed Σ_{p≤y}(p^α−1)/p≪_B (1/log y)Σ log p/p=O_B(1). Choosing B large enough, the whole tail costs O_A(H/log^A X) at each center. The same harmonic ceiling completes the product in the main term. This proves the first formula.

**Full sum.** By the identity of 353, first bound Σ μ(n)log n on the pulse. The estimate of 350 for μ in all intervals, followed by partial summation, gives O_A(H/log^A X): for prefixes of length <X^(2/3) use the trivial bound, and for the rest the theorem with fixed margin over 5/8 (the required upper endpoint has a fixed margin depending on δ). For p^k≤√X, k≥2, the same theorem gives |S_h(x/p^k)|≪_A (H/p^k)/log^A X, since the length exceeds z^0.86 with z≈X/p^k and is ≤z^(1−ε_δ). Sum with Σ_{p,k≥2}(log p)/p^k<∞. For p^k>√X the counting ceiling costs O(H X^(−1/8)+√X log²X), summing (H/p^k+1)log p as in 354. This proves P_h=O_A(H/log^A X) at each center and by subtraction gives the second formula. [Matomäki, Shao, Tao and Teräväinen, uniform estimate for μ](https://arxiv.org/abs/2204.03754)

**Scope.** 354 obtained the linear means for all widths. For the family of small powers the profile that cancels and its sign at each center are now known, even after forming quadratic products at the main level. The error H/log^A X is still larger than √H for fixed A; there is no root bound for the residue.
