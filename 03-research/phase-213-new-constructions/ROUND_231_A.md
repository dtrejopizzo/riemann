# Local detection with plain primes after fitting a line

Let t=log X and 0<h=h(t)≤1 with log(1/h)=o(log t); constant h is included. Let I=[X,Xexp(h)]. Form, using only primes from the interval,

    D(X,h)=inf_(A,C real) X^(−2)∫_I [Σ_(X<p≤x) log p − A − C(x−X)]² dx.

Then log(1+D(X,h))/log X→2B for B from 229. The count before X and the expected mean slope may be unknown. For example it holds for h=exp(−√log log X), which tends to zero. This does not reach intervals of length X^(1−ε). A ceiling X^o(1) along a subsequence of these local fits would suffice for the sign.

**Quantitative control of the filter of 230.** Fix ρ₀=β₀+iγ₀ with β₀>1/2 and intermediate σ. By Ingham the tail of lengths of the positive filter for Re ρ≥σ, |γ|>G, costs O(G^(−κ)) with some fixed κ>0: by dyadics any κ less than 1−3(1−σ)/(2−σ) can be used. Choose G=max(G₀,(C/h)^(1/κ)) with constants such that the tail fits in h/3 and G>2|γ₀|+2. Then G=t^o(1). Reserve in the finite list of annihilations also the two exponents −ρ₀ and 1−ρ₀. If M is the length of the list of distinct nonzero exponents, M=O(G log(2G)+1)=t^o(1). For all of them use the same step

    l=h/[10(M+1)(G+|ρ₀|+3)].

Thus |w l|≤1/2 and |exp(wl)−1|≥c|w|l. The distance of all nonzero targets to the origin is bounded below by a constant depending on ρ₀, by discreteness and the two fixed additions. The finite factors of 230 have variation ≤C/l and the convolution has variation ≤(C/l)^M=exp(o(t)); the sum of their lengths is less than h/3. The positive tail product preserves variation one. The last factor is a smooth function of mass one rescaled to the interval (0,h/3). Its norms up to two derivatives cost O(h^(−3)), absorbed in exp(o(t)). The final filter f_t has mass one, support in [0,h], L² norm and L¹ norms of the first two derivatives ≤exp(o(t)). In particular its transform against exp(wv) for |Re w|≤1 is O(exp(o(t))/(1+|Im w|²)), uniformly in w, by parts.

**What can be removed from the count.** Repeat the explicit formula of 230 with that filter. The error of all zeros with β<σ is O(exp(−(β₀−σ)t+o(t))) by the unit count and the two derivatives. The trivial terms are controlled as in 230. The central residue is still −mult(ρ₀)/ρ₀. Using mass one and the additional annihilations, the integral of f_t(v)exp(−ρ₀(t+v)) against any line A+C exp(t+v) is exactly zero, whatever A,C are, even if they depend on X. By Cauchy–Schwarz one obtains for every line, with the same loss exp(o(t)),

    X^(−2)∫_I |ψ(x)−A−Cx|² dx ≥ exp((2β₀−1)t−o(t)).

Here only dx=x dv and x/X∈[1,e] have been used. Passing to θ changes the norm (root of the left-hand side) by at most X^o(1), since ψ−θ=O(√X log² X) on I. For each β₀>1/2 that loss is negligible. Subtracting θ(X) is absorbed into the intercept. For the ceiling take the line corresponding to subtracting x from θ(x), use again the bound on the powers and bound by a constant times the integral of 229 on a larger band. Approximating 1/2+B by right zeros gives the limit; if B=0 the ceiling and the nonnegativity of log(1+D) suffice.

**Evaluation on a finite interval.** Enumerate the interior primes and the two edges in increasing order. Between two successive edges a,b the local weighted count equals a constant S. The exact contribution to the objective before dividing by X² is

    (b−a)[S−A−C((a+b)/2−X)]² + C²(b−a)³/12.

These expressions are summed and a quadratic in two variables is minimised, with positive definite matrix because I has positive length. It requires no model for the level or the slope nor primes below X. The bound for this minimised sum has not been proved along any unbounded sequence.

**Scope.** 230 gave arbitrarily short support fixed in advance. Here the cost of the filters is quantified and allows it to shrink with X. The two additional annihilations turn the criterion into an estimate of interior irregularity around the best local line. No bibliographic priority is claimed nor has global positivity been obtained.
