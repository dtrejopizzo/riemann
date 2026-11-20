# Quadratic sampling of the numerator: up to 4096 real poles without additional restrictions

For n≤4096, arbitrary v_j>1/2 with multiplicity and F(s)=P(s)/∏(s+v_j), deg P<n, the complete form of the causal datum satisfies

    W(F) ≥ exp(−330000) ||f||₂².

Here f is the inverse Laplace transform of F. The uniform margin is deliberately conservative. The exact sum over zeros of 201, Z2 up to G=3·10¹² and the count Z3 are used. The conclusion covers complex numerators.

**Sampling equivalence in each band.** Put n₀=4096, H=1200000000, t=n₀²/H<0.014. On I=(A,A+H], A≥G, for any complex polynomial p of degree <n₀, let ||p|| be its L²(I,dx) norm. Then

    l log A ||p||² ≤ Σ_{γ∈I}|p(γ)|² ≤ h log A ||p||²,
    l=0.14−6t>0.056,  h=0.17+6t<0.254.

The sum counts multiplicities. In the orthonormal Legendre basis translated to the interval, the sum of squares of their values at each endpoint is t. The norm of differentiation is ≤2t: on [−1,1] its squared Hilbert–Schmidt norm is Σ_{k<n₀}(2k+1)k(k+1)/2<n₀⁴ by ∫(P'_k)²=k(k+1), which is obtained by expanding the derivative in Legendre polynomials of opposite parity by orthogonality and integration by parts. Rescale by 2/H. Integrating |p|² by parts against the remainder of Z3 costs ≤log A via the sum of the two endpoint values and the variation of |p|², in total ≤6t log A||p||². The remainder of Z3 has supremum ≤log A and the derivative of the main term lies between 0.14 log A and 0.17 log A as in 201. Right-sided values are taken for the stated convention. By symmetry the same estimate holds on the negative half-axis using t' = |γ| as variable.

**Difference in norm over the ordinates.** Take p(t')=P(±it'). Shifting the argument of P by a real number δ_γ with |δ_γ|≤1/2, Taylor and the ℓ² triangle inequality give a norm difference ≤√(h log A)(exp(t)−1)||p||. Indeed apply the upper sampling bound to each derivative and use ||p^(k)||≤(2t)^k||p||. δ_γ is not assumed constant. For D(s)=∏(s+v_j), the ratio D(±it')/D(±it'+δ_γ) differs from one by at most b=(1−1/(2G))^(−n₀)−1<10⁻⁸. The ratio between the maximum and minimum of |D| on I is ≤exp(n₀H/G). Comparing with the unshifted vector X_γ=F(iγ), both deviations X_γ^±−X_γ in ℓ² have norm ≤e||X||, with

    e ≤ exp(n₀H/G) √(h/l) [(1+b)(exp(t)−1)+b] < 0.16.

Thus the real sum of products of the two vectors is ≥(1−2e−e²)||X||²>0.65||X||². Using the lower sampling bound and the denominator ratio once more, this exceeds 0.01∫_I |F(±ix)|²dx because 0.65 l log(G) exp(−2n₀H/G)>0.01. Sum over the high bands and keep nonnegativity below G by Z2.

**Global floor in norm.** Compare the low interval [−G,G] with I=[G,G+H] in the ordinate variable. In the Legendre coordinate |x|≤1+4G/H≤10001. By recurrence |P_k(x)|≤(2·10001+1)^k for Legendre polynomials normalized at 1. Cauchy–Schwarz in the orthonormal expansion gives sup_[−G,G]|P(i·)|≤(n₀/√H)21000^n₀||P(i·)||_{L²(I)}. Moreover max_I|D|/min_[−G,G]|D|≤(7·10¹²)^n₀ since v_j≥1/2. Therefore the ratio of the low energy to the high energy is at most C=(2G n₀²/H)(21000·7·10¹²)^(2n₀) with log C<325000. The floor follows from 0.01/(1+C) and Plancherel with factor 1/(2π).

**Scale of the method.** At any order n, on bands starting from max(3·10¹²,100n³), take H=80n²; then t=1/80 and nH/A≤0.8. The same two sampling bounds and Taylor prove the sign of each high band (n/(2A) is tiny and H/A≤0.001 for A in this range: for small n use A≥3·10¹² and for n≥800 use A≥100n³). The sign of the whole form is deduced only if the low part up to that height is also controlled. No additional verification is presupposed. The advance over 201 is relative control in sampling norm for all numerators and their derivatives, not an optimization of the maximum on a subinterval. The interpolation obstruction of 201 remains in force when a band is fixed and the order is allowed to grow without limit.

**Independent audit.** The discrepancy term 6t, the application of Taylor with variable shifts, the denominator factor, the extrapolation and the Plancherel normalization were verified. The computed bound for e is <0.155.
