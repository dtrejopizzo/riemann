# The positive bias of the sieved product and a sign criterion without barrier

For the same Q_a of 365, z=L², L=log x and fixed a>0, **eventual positivity Q_a(x)>0 is equivalent to the parabolic exclusion of 364**. Hence it suffices to prove eventual positivity for a in a positive sequence tending to zero. For each a in the verified range of 364 the sign is already strictly positive at every sufficiently large scale. This concerns the new observable, not an enlargement of the support window of P46.

**Formula in the regime without forbidden zeros.** Define K(s)=LΦ_a(s)+log E_z(s) using the real branch on the real axis and let s₀ be the real solution of K'(s₀)=0 near 1/2. Then

    Q_a(x) ∼ [−L/ζ(1/2)] exp(K(s₀))/√(2π K''(s₀)),
    K(s₀)=L/2+(1+log 2+o(1))L/log z,    K''(s₀)∼L log z.

The sign of the coefficient is positive, since ζ(1/2)<0 by the alternating eta series.

**Localization.** For σ=1/2+c/log z, with c in a fixed compact set, the prime number theorem and partial summation give Σ_{p≤z}log p/(p^σ−1)∼2e^(−c)L uniformly. The terms of powers ≥2 cost O(log²z) here for c≥0. The main sum is obtained by integrating t^(−σ)dt. Similarly log E_z(σ)∼2e^(−c)L/log z, and the second derivative of log E is ∼2e^(−c)L log z (add a factor log p to the first sum). Since K''>0, the sign change of K'=L(1+a(σ−1/2))−Σlog p/(p^σ−1) gives s₀=1/2+(log 2+o(1))/log z. Substituting into K and K'' gives the two formulas.

**Integral on the vertical through the critical point.** Write D_z=E_z B_z with B_z=F'−F(H+L_z), F=1/ζ, H the sum of higher powers of 361 and L_z(s)=Σ_{p≤z}log p/p^s. Near t=0 at the scale t=v/√K'', v fixed, L_z(s₀+it)∼L (the relative change is O(|t|log z)), H=O(log z) by its simple pole and F→1/ζ(1/2). Hence B_z/L→−1/ζ(1/2). The expansion of K at the same point is K(s₀+it)=K(s₀)−v²/2+o(1). Indeed the third complex derivative of log E is bounded by O(L(log z)²) on the vertical, by its absolutely convergent series and partial summation.

For |t|≤1/log z, the terms k=1 of log E give a real loss
Σ p^(−s₀)(1−cos(t log p)) ≫ K''t². The remaining terms of the logarithm only add loss. On this stretch B_z=O(L), using the regularity of F around 1/2 and H=O(log z). Dominated convergence after the change of variable v justifies the Gaussian equivalent with the constant 1/√(2π). For 1/log z≤|t|≤T fixed, the factor x^Φ contributes an additional loss of at least exp(−aL/(2log²z)) and |E_z(s₀+it)|≤E_z(s₀). On the compact set of heights the factor B_z is O_a(L^C): the critical zeros are at distance at least s₀−1/2 and the other zeros of the compact set have fixed abscissae. This second stretch is negligible relative to the main one.

**Closing the contour.** Use as in 364 a height T with strict margin in 1+a(1/4−T²)/2<1/2, avoiding zero ordinates. Horizontals and tails are negligible: the cost of the Euler factor in Re s≥s₀ is exp(o(L)), and the margin in the exponent is fixed. Under the exclusion, the crossed poles have Re Φ≤1/2 and Re ρ>1/2. On circles of radius 1/L around each one, the logarithm of the bound of the finite product is O_ρ(z^(1−Re ρ+o(1)))=o(L/log z), and the other factors cost at most a power of L. Their number is finite at fixed T. Thus all the residues together cost at most exp(L/2+o(L/log z)), strictly below the computed bias, even for Re Φ=1/2. This proves the equivalent and the eventual positivity. If a forbidden zero exists, 365 already gives negative values in each sufficiently distant multiplicative block, preventing that sign.

**Difference from the previous steps.** 144 obtains a bias for a Liouville average. In this case the positive term arises from the real critical point of the finite Euler product, whose cut changes with x. 365 required comparison with an explicit ceiling; now the single inequality Q_a(x)>0 suffices. It is not yet proved for a arbitrarily close to zero.
