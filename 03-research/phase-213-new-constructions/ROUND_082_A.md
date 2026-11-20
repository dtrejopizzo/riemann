# Energy needed for the exponential cost of the comb to survive

Write W=Arch+D_T, where D_T=polar−C_T and C_T is the positive comb of 081. For T large enough, with absolute constants c,C>0, every test in the form domain satisfies
     
    |D_T[F]| ≤ C e^T [ exp(−c√T)||F||² + (Arch[F]−m(0)||F||²)/√T ].

In particular for ||F||=1 and |D_T[F]|≥δ e^T, δ>0 fixed, the archimedean excess is at least c_δ√T for T large. Moreover ||D_T||∼e^T as a bounded operator in the window, but on the plane of the two polar moments its norm as a map into all of L² is O(exp(T−c√T)).

**Estimate on the same test.** In the quadratic form the polar convolution kernel 2cosh(u/2) can be truncated to |u|≤2T, by the support of the autocorrelation. Its symbol minus that of the comb is
     
    b_T(ξ)=4∫₀^{2T} cosh(u/2)cos(ξu)du − 2Σ_{n≤e^(2T)} Λ(n)n^(−1/2)cos(ξ log n).

The contact at the endpoint has zero autocorrelation, so it is legitimate to include it. Replacing dψ(t) by dt in the sum leaves in the symbol the integral of 2 exp(−u/2)cos(ξu), uniformly bounded. For the error, integrate by parts against ψ(t)−t=O(t exp(−c√log t)) for t≥2. The derivative of the weight t^(−1/2)cos(ξ log t) costs O((1+|ξ|)t^(−3/2)); splitting the integral into t≤exp(T) and t>exp(T), and including the endpoint, gives O((1+|ξ|)exp(T−c₁√T)). The trivial absolute bound of the symbol is O(exp T) on the whole line by 081 and the total mass of the coefficients (for the symbol the mass is used, not the compressed norm).

Choose R=exp(c₁√T/2). In |ξ|≤R the symbol has size O(exp(T−c₁√T/2)). In |ξ|>R, Plancherel and monotonicity give spectral mass ≤(Arch[F]−m(0)||F||²)/(m(R)−m(0)); the denominator is comparable to √T. Integrating the symbol gives the inequality. This estimate keeps the polar term in the density cancellation.

**In which subspace the main cost lives.** Let P be the projection onto the plane of c(t)=cosh(t/2) and s(t)=sinh(t/2) restricted to the interval. By the row formula of 081 and the quantitative PNT,
     
    C_T c=e^T c+O(exp(T−c₁√T)c),
    C_T s=−e^T s+O(exp(T−c₁√T)c)

pointwise almost everywhere (in these two equalities c without argument inside the error denotes the profile). For the second identity subtract the rows corresponding to exp(t/2) and exp(−t/2). In both, Chebyshev is used at the endpoints X_±<exp(T/2), which contribute a relative error O(exp(−T/2)) with respect to e^T cosh(t/2), as in 081. The norms of c and s are comparable as T grows. The eigenvalues of the polar operator on those vectors are 2T+2sinh T and 2T−2sinh T, respectively. Hence ||D_T P||≪exp(T−c₂√T). By self-adjointness the cross block to that plane is also controlled. On the complement the compression is exactly that of −C_T and has norm ||C_T|| by 081. It follows that ||D_T||=||C_T||+O(exp(T−c₂√T))∼exp T. This refers to the bounded operator D_T, without the archimedean multiplier.

**Cross-check and pending scale.** P47 prop:wit-cheb already centers the comb via PNT on tests with derivative control. P211-006 and 081 already identify the modulations and the cosh test. Here the Fourier cutoff is used to obtain an energy condition for all tests of the domain, and the computation of the two rows to jointly control the polar plane and its crossing. The result excludes a non-archimedean excess of order e^T on normalized tests with archimedean excess o(√T). It does not prove W≥0: the upper bound for |D_T| is still far larger than the archimedean energy at the relevant scales. It produces no additional window.
