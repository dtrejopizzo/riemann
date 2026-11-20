# A single cosine as the interval varies, and a subsequence of false negatives

For x≥1 let F(x)=Σ_(x<p≤2x)(log p) cos(2πp/x), over primes only. Set t=log X, 0<h(t)≤1 with log(1/h)=o(log t) and

    J(X,h)=X⁻²∫_X^(X exp h) F(x)² dx.

Then log(1+J(X,h))/log X→2B. Unlike 235 the frequency and the real component are fixed. What is controlled along a subsequence is the energy when the start of the interval moves, not a single sample. In fact, if RH fails there are infinitely many integers n with |F(n)|≪log n, as well as excursions of both signs larger than n^(1/2+δ) for some δ>0. Thus a proof that only finds one small value per chosen scale would not distinguish a failure of the sign.

**The cosine preserves the relevant poles.** Its multiplier H(s)=∫₁² y^(s−1)cos(2πy)dy is entire and H(1)=0. For 1/2≤Re s≤1, two integrations by parts, using that the derivative of the cosine vanishes at both edges, give

    |s H(s)−(2^s−1)| ≤ 16π²/|s+1|.

Since |2^s−1|≥√2−1, H does not vanish in that strip for |Im s|≥400. All zeros to the right of the line lie above that threshold in absolute height by Z2 of 47. Thus there is no need to choose a harmonic depending on the zero.

**Ordinary average.** Fix ρ₀ with β₀>1/2 and σ between 1/2 and β₀. Use the f_t of 231 on [0,h], of mass one, which eliminates all other zeros with β≥σ and has norms up to two derivatives exp(o(t)). Applied to the analogous sum F_ψ over prime powers, the functional ∫ f_t(v)exp(−ρ₀(t+v))F_ψ(exp(t+v))dv gives

    −mult(ρ₀)H(ρ₀) + O(exp(−(β₀−σ)t+o(t))).

Indeed in the explicit formula for dψ the integral over the window [x,2x] against the cosine multiplies each term −x^ρ by H(ρ); the density dx gives xH(1)=0. It is legitimate to do the computation distributionally: integrating first in v smooths the two edges of the truncated cosine, and the transform of the test is the product of H with the shifted transform of f_t. The latter has uniform quadratic decay up to the factor exp(o(t)), while H is bounded in the critical strip by its integral. This allows absolute summation with Z3. The trivial terms of the explicit formula cost O(exp(−β₀t+o(t))) or less. Removing the higher powers costs O(exp((1/2−β₀)t+o(t))) after normalising. The nonzero limit and Cauchy–Schwarz imply J(X,h)≥X^(2β₀−1−o(1)). For the ceiling use θ(y)−y=O_ε(y^(1/2+B+ε)) from 235 and partial summation on a dyadic window; the continuum gives zero and the cost of the derivative of the cosine is O(1). Take the supremum over β₀, with the trivial floor if B=0.

**Obstruction to using pointwise data.** For Re s>1 the one-sided Mellin transform of F is exactly H(s)Σ_p(log p)p^(−s), by x∈[p/2,p] and p≥2. In Re s>1/2 the prime series continues as −ζ'/ζ(s) minus the absolutely convergent series of powers of order ≥2. The product is regular at every real point of that half-plane: the singularity at 1 cancels and there are no real zeros there. It has a pole at each right zero by the computation of H. Let 1/2<a<β₀. If F(x)≤x^a eventually, the Mellin transform of x^a−F(x), after removing a compact prefix, is that of a nonnegative function meromorphic in the half-plane considered. Landau forces a real singularity at the abscissa of convergence, which is ≥β₀ by the nonreal pole and finite by Chebyshev. There the expression 1/(s−a)−H(s)Σ_p(log p)p^(−s) is regular. Contradiction. The same argument for x^a+F(x) gives the other excursion. The conclusion holds arbitrarily far out with both signs.

For x∈[n,n+1] entries and exits cost O(log n) by counting integers at the edges; the change of the remaining phases costs O(1) by Chebyshev and the bound O(1/n) for the derivative of each phase. Hence there are also integer excursions of both signs (slightly reducing a) and |F(n+1)−F(n)|≪log n. Each crossing between signs gives an integer with |F(n)|≪log n. This does not guarantee a small sample in each interval of prescribed width nor that the integer is prime.

**Decision.** Averaging over starting points in 236 and searching over several harmonics in 235 are two different ways of avoiding cancellations. In the first, the remaining problem is a ceiling X^o(1) for J(X,h) along some sequence of WINDOWS. Do not use a small pointwise subsequence of F as a substitute.
