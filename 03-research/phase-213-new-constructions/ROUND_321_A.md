# The short operator is small in frequency mean, but admits no uniform contraction

In the construction of 320 distribute the density correction as in 049: take a(d)=μ(d) for d≤D, a(d)=c for D<d≤2D, with c=−(Σ_(d≤D)μ(d)/d)/(Σ_(D<d≤2D)1/d), and zero after. Thus |c|≪log(2D); the proof of 320 goes through literally because it only used the support, the zero harmonic mass and Σ|a|≪D log(2D). With g=1*a and the same cut, the action of the intermediate sum on the scale function x^s is multiplication by

    H_X(s)=Σ_(D<n<2N) g(n)(1−ψ(n/N))n^(−s).

The frequency Im s is dual to log x; it is different from the parameter t of the arithmetic coefficients. There are three verifiable behaviours.

**Mean frequency.** Fixing 1/2<σ<1, the average over [0,T] of |H_X(σ+iτ)|² converges as T→∞, with X fixed, to the sum of squares of the weighted coefficients. Integrating the cross terms proves it directly. Since |g(n)|≪τ(n)log(2D), that sum is O_(σ,ε)(D^(1−2σ+ε)) by the divisor ceiling and the sum from D to infinity (use a loss smaller than 2σ−1). It tends to zero as X→∞. It is important to distribute the correction: a single large coefficient at 2D does not give this proof.

**Uniform amplification.** For the same σ and any initial height T₀ one has sup_(τ>T₀)|H_X(σ+iτ)| ≫_σ N^(1−σ)/log N. Indeed, the frequencies log p of the primes up to 2N are rationally independent by unique factorization; Kronecker's theorem for the continuous flow allows simultaneous approximation of any choice of phases, also at arbitrarily large heights. Choose all phases equal to exp(iθ). The first Fourier coefficient in θ of the resulting polynomial only picks up the integers with a single prime factor counted with multiplicity, that is, the primes. On 2D<p≤N one has g(p)=1 and the cut equals one. On N<p<2N it is still nonnegative, and D<p≤2D costs in total O_σ(D^(1−σ)log D). By the PNT the primes of [N/2,N] contribute ≫N^(1−σ)/log N, which dominates that cost because N is comparable to D³. The maximum of the modulus dominates the modulus of the coefficient. Hence there is no contraction for all modes x^(σ+iτ), even though the mean square tends to zero.

**At a fixed frequency corresponding to a zero.** Let A_D(s)=Σ a(d)d^(−s). For each fixed s with 0<Re s<1 and each fixed K,

    1+H_X(s)=ζ(s)A_D(s)+O_(s,K)((log X)^(−K)).

For Re s>1 the difference is the signed sampling of f(v)=ψ(v/N)v^(−s), up to the global sign of the subtraction. In Poisson the integral cancels because A_D(1)=0. The Fourier integrals at nonzero frequency, expressed with j integrations by parts, continue to Re s>0 and are locally uniform: ||f^(j)||₁≪_(s,j) N^(1−Re s−j) for j≥2. This continues the identity by uniqueness; the pole at 1 of the product is removable. The total error costs O_(s,j)(N^(1−Re s−j)D^j log(2D)). Since N/D is comparable to (log X)², it suffices to choose j fixed and large enough. Thus, at any fixed critical zero ρ one has H_X(ρ)=−1+O_K((log X)^(−K)). In the recurrence the main sample carries coefficient +1, so this mode cancels to every logarithmic order.

Bohr phase approximation already appears in the index in other operator problems. Here the three estimates are applied to the same short symbol that had to be controlled in 320. The second prevents proving the sign through a uniform contraction of the bare operator; it does not say that the arithmetic input observed by the positive kernel has relevant weight at the extreme heights. The third explains why the recurrence tolerates critical modes even at fixed height. Controlling the action on the concrete arithmetic balances is missing.
