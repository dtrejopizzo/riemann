# The logarithmic deficit of 153 is the exact mass of the perfect squares

Put f(t)=exp(−πt⁴), I=∫₀^∞ f(t)dt and J=∫₀^∞ log(t)f(t)dt. Complete S of 153 to
    V(x)=Σ_{p,k,n≥1} log p exp(−π(p^k n²/x)²).
Unconditionally, as x→∞,

    V(x)−S(x)=(I/2)√x log x + (J+I D)√x + o(√x),
    D=Σ_{p, k odd ≥3}(log p)p^(−k/2).

**Pointwise identity.** Even k correspond to p^(2l)n²=m². For fixed m the sum of their weights is Σ_{p|m} v_p(m)log p=log m. Hence that whole part is exactly Σ_m log m f(m/√x). With Y=√x, the sum of f(m/Y) differs from YI by O(1) by monotonicity. The sum of log(m/Y)f(m/Y), divided by Y, tends to J by improper Riemann sums: near zero it is controlled uniformly by the integral of |log t| on (0,δ), and in the tail by an integrable decreasing majorant. This gives YI log Y+YJ+o(Y). For each p and odd k≥3, the sum over n divided by Y tends to I/p^(k/2) and is bounded by that same value by comparison with the decreasing integral. D converges absolutely. Dominated convergence gives the remaining term.

**Consequence.** I=Γ(1/4)/(4π^(1/4)); by the definition of ξ, I/2=−ξ(1/2)/ζ(1/2). Thus the whole secondary term of 153 cancels on completing the count. The global sign is equivalent to the eventual ceiling V(x)≤ζ(2)x/2+O(√x). The additional contribution of size √x even has the explicit constant J+ID. The antecedent 073 already identified a harmonic drift of the prime squares and 152 transferred it to a kernel with constant limit. The observation here is that in the positive count of 153 the whole even part can be regrouped exactly, integer by integer, without any theorem on the distribution of primes.

**Limit.** The Dirichlet series of the complete count is ζ(2s)(−ζ'/ζ)(s). In particular the identity for the squares explains the secondary correction but leaves in V all the difficulty of the fluctuations of Λ. Since ζ(2s) does not vanish in Re s>1/2, completing the powers removes no possible off-line pole. Repeating the completion as a spectral argument would return to 150–153.
