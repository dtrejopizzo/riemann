# A row of finite differences, with sign certified up to order 2^G

With F from 253, G=3·10¹² and S=G² define for integer n≥0

    b_n=Σ_(j=0)^n (−1)^j binom(n,j) F(2+j)
       =∫₁^∞ C(x)x^(−3)(1−1/x)^n dx.

One has b_n>0 for EVERY 0≤n≤2^G. Moreover the global sign is equivalent to b_n≥0 eventually, in this single row that always starts at 2. Here the integer n is a difference order, not a verified height nor a radius T. The 2^G orders are not evaluated separately.

**Stretch covered by differentiation.** For n≤S−2 the difference with step one is the integral of (−1)^n F^(n)(2+u₁+...+u_n) over the unit cube. 253 suffices; for n=0 use F(2)>0. For larger orders the cube leaves the interval of 253 and another estimate is needed.

**Damping in the beta product.** Divide b_n by B(3/2,n+1)>0. Applying the complete formula of 248, including the errors smaller than 50 down to y≥1 as in 253, each term x^z goes to

    L_n(z)=B(2−z,n+1)/B(3/2,n+1)=∏_(j=0)^n (j+3/2)/(j+2−z).

Integrating in the series of zeros is justified by absolute convergence with weight x^(−3). The main term of squares equals 4/15. For the verified zeros |L_n(ρ)|≤1 and they cost in total less than 0.094. For a zero above G, each factor with j+1≤G has in the denominator at least √2(j+1); the others have at least j+1. The product of (j+3/2)/(j+1) is ≤exp((1+log(n+1))/2)≤2√(n+1). Thus, for S−2<n≤2^G in the tail one has |L_n(ρ)|≤2√(n+1)2^(−G/2)<3. This tail is paid with less than 3·2.01·6.4·10^(−12). It is the simultaneous suppression by G different factors that allows this extension of orders.

For 0≤z<1/2 one has 0<L_n(z)≤(2/(n+2))^(1/2−z), since log(1−v)≤−v and Σ_(j=0)^n 1/(j+2−z)≥log((n+2)/2). The cost of x^z log x is L_n(z)Σ1/(j+2−z), at most L_n(z)(1+log(n+1)). Let v=2/(n+2). The low zeros of J₂ cost ≤0.235 v^(1/4) and the high ones ≤5·6.4·10^(−12) since Re(ρ/2)≤1/2. The bounded errors cost ≤100√v. By the one-sided bound of 248, the odd exponents cost at most

    (2/3)[v^(1/6)+v^(3/10)+(1+log(n+1))v^(5/14)/(2 log 2)].

For n≥10^24 these additional costs together are less than 0.001 (the term with logarithm decreases in this range). Thus b_n/B(3/2,n+1)>0.17 on the new stretch.

**Why a single row decides the sign.** By θ(x)≤2x one has |b_n|≤2/(n+1). For real 1<s<2 one can integrate the binomial identity in (1−1/x) and obtain F(s)=Σ_(n≥0)b_n(2−s)_n/n!, with rising factorial. Absolute convergence under the integral follows from the same majorant for |C| at s>1. The identity extends to the interior of the strip of convergence by analyticity. Uniformly on compacts of 0<Re s<2, Γ(n+2−s)/Γ(n+1)=n^(1−s)+O(n^(−Re s)). Therefore

    Γ(2−s)F(s)−Σ_(n≥1)(n b_n)n^(−s)

has holomorphic continuation to that strip by the series of errors and the term of index n=0 treated separately (its contribution is Γ(2−s)b₀). If the coefficients are eventually nonnegative, Landau prevents a nonreal pole of this series with Re s>1/2: the abscissa lies to the left of, or at, 1, and such a pole would require a real singularity to its right or at its same abscissa. But F is regular on the whole real half-line 1/2<s≤1 and has a pole at each zero to the right by 247. Every such zero is excluded. Under RH the pointwise positivity of 248 and 253 directly gives b_n>0 for all n. The same Landau argument applied with the opposite sign shows that under failure there are infinitely many n of each sign.

**Antecedents and limit.** Binomial transformations and the Hausdorff or Báez-Duarte criteria already appear in the index. The new estimate is the margin for the barycentre row of 247, at orders exceeding the derivative domain of 253, through the exact beta product. The reduction to one row is feasible because of its specific arithmetic poles; eventual positivity of that row remains unproved.
