# Negative sign of the sieved average on decreasing relative intervals

Fix D≥2 and A>0. Let φ be smooth, nonnegative, of integral one and compact support in (0,1). For almost every fixed t in [1,2], L=log x and δ=L^(−A), the exact sieved balance of 310 satisfies

    ∫₀¹ φ(u) S_D(x(1+δu),t) du  ∼  −c_(D,t) √x/L^(3/2),    c_(D,t)>0.

In particular in each interval [x,x+x/(log x)^A], for sufficiently large x, there is a scale where S_D is negative with modulus ≫_(D,t)√x/L^(3/2). RH is not required and no uniformity for growing D is claimed. The sign of the average with its dilations is estimated, not the pointwise sign of B_t.

**Positivity of the sieve factor on the half-line.** The coefficient series whose partial sum is S_D is E(s)=D_t(s)ζ(s)² h_D(s), in the notation of 306 and 310. For real positive s the polynomial h_D(s) is strictly positive. Take independent Bernoulli variables X_p, p≤D, with probabilities q_p=p^(−s)(2−p^(−s)). By the lcm formula of 310,

    h_D(s)=E[(Σ_(d≤D) μ(d)∏_(p|d)X_p)²].

When all variables are zero, the square equals one and the event has positive probability. This avoids a possible vanishing or sign inversion due to the sieve.

**Three branch points.** Apply the second-degree extraction of 307. Multiplication by ζ(s)² has already removed the first-degree denominator, and the factors L(s±it,χ) are entire. The remaining non-entire factors are ζ(2s)^(−1/2) and [ζ(2s−2it)ζ(2s+2it)]^(−3/4). At s₀=1/2, E(s)=(s−s₀)^(1/2)(K+O(s−s₀)), with K>0 for the frequencies considered. Indeed, to the right on the real line the conjugate factors group into positive moduli; the t where L(1/2+it,χ) or some finite local numerator vanishes are excluded. Only p≤4 can intervene in this last exclusion. The other units are nonzero at s₀ and h_D(s₀)>0. At s±=1/2±it the expansion is (s−s±)^(3/4) times an analytic factor, possibly zero. The Euler remainder with the small primes adjusted is holomorphic and bounded on the closed strips of Re s>1/3 used.

**Inversion with the decreasing window.** In Mellin form the kernel multiplying E(s)x^s is

    Wδ(s)=s^(−1)∫ φ(u)(1+δu)^s du.

The inversion from Re s=2 follows by smoothed Perron. On a bounded strip and for |Im s|≥1, integrating by parts N times gives |Wδ(s)|≪_N (1+|Im s|)^(−1)(1+δ|Im s|)^(−N). In fixed neighborhoods of the three points the function and its first derivatives are uniformly bounded, and Wδ(1/2)→2. Shift initially to 1/2+1/L, without crossing singularities. There E(s) grows at most like L^C(2+|Im s|)^C, by the extracted factors, the absolute bounds for the reciprocals of ζ to the right of 1 and the polynomial growth of the L-functions. Take T=L^B, B>A+2 fixed, and N sufficiently large for the tail to be O(√x/L³).

In |Im s|≤T shift to 1/2−c/log(T+3), with horizontal cuts to the left of the three points. The classical zero-free region of ζ, with reduced c, accommodates the three branches. In the parts outside neighborhoods of the points, the factors and reciprocals are at most polynomial in T (for the real powers it suffices to bound their moduli); near the points the local expansions are used. The gain exp(−cL/log(T+3)) absorbs the powers of T on the left edge; on the horizontal edges it suffices to increase N. On each cut the discontinuity of (s−s_j)^ν integrated against x^s contributes x^(s_j)L^(−1−ν)/Γ(−ν) per unit of constant coefficient: parametrize s=s_j−v and use ∫₀^∞ exp(−Lv)v^ν dv=Γ(1+ν)L^(−1−ν) and the reflection formula for Γ. The error from the linear analytic factor costs an additional power of L, uniformly in δ. Hence the nonreal points cost O(√x/L^(7/4)), while the real one gives K Wδ(1/2)√x/[Γ(−1/2)L^(3/2)]. Since Γ(−1/2)=−2√π, one gets c_(D,t)=K/√π.

**Implication for the route.** This sign proves arithmetic cancellation in the positive average of dilations with a fixed sieve, even when the scale is localized in ever smaller relative intervals. Extracting only the sample n=1 requires controlling the rest of the dilations and the dependence on D; the computation of the real branch does not settle these two questions.
