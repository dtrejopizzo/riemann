# Discrete test with binomial weights and no continuous term

Use W and H from 240. For real u define S(u)=Σ_p(log p)W(log p−u). Set r=1+floor(t/(log t log log t)), d=h/(2r), 0<h≤1 and log(1/h)/(log t log log t)→λ≥0 finite. To avoid any spectral alias in reading the data, the test uses G=t(log t)^3 and **the effective step is fixed** as δ=min(d,1/(4G)). Let E be the shift by δ. With 2r+1 equally spaced values of S form

    K(t,h)=exp(−t/2) max_{0≤k≤r} |(E−exp(δ))^r S(t+kδ)|.

Then log(1+K)/t→max(B−λ,0). The datum is only a finite sum over primes for each k; the operator uses explicit binomial weights. The nodes lie in [t,t+h]. For λ=0 the trimming of the step may concentrate them in a smaller window. Always r log(1/δ)=λt+o(t).

**Ceiling.** The continuous mean exp(u)H(1) vanishes exactly. In the expansion of 240 the error of prime powers and lower terms costs after the difference at most (1+exp(δ))^r exp(t/2)poly(t)=exp(t/2+o(t)). For the modes of zeros the multiplier is (exp(ρδ)−exp(δ))^r, of modulus ≤(δ exp(δ)|ρ−1|)^r by integration over the segment from 1 to ρ. The absolute moment of H of order r costs exp(O(r log(r+2))) according to 240. This gives the ceiling exp((1/2+B−λ)t+o(t)) for the part of zeros.

**Floor when λ<B.** Choose ρ₀, σ as in 240 with 1/2<σ<β₀−λ. Apply to the differenced sequence the additional polynomial

    L(E)=∏_{ρ distinct from ρ₀, Re ρ≥σ, |Im ρ|≤G} (E−exp(ρδ))/(exp(ρ₀δ)−exp(ρδ)),

with one factor per distinct zero. Its degree M≤t^(q+o(1)) with q<1 is less than r for large t. Its coefficients have ℓ¹ norm ≤exp(o(t)): each denominator is ≥cδ|ρ−ρ₀|≥c(ρ₀)δ, since |(ρ−ρ₀)δ|<1/2 and ρ₀ is fixed and isolated. The numerator has norm ≤1+exp(δ). Thus M log(1/δ)=o(t). L equals one on the chosen mode and eliminates the other enumerated modes. The chosen contribution has modulus exp((β₀−λ)t+o(t)), since H(ρ₀)≠0 and |exp(ρ₀δ)−exp(δ)|/δ→|ρ₀−1|>0. The low zeros with real part less than σ cost ≤exp(σt+o(t)) using the coefficient norms of both operators; the power error costs ≤exp(t/2+o(t)). The tail of zeros above G carries the factor exp(−cG/log²G). All these bounds are exponentially smaller than the chosen term. Since L only reads the first M+1 terms and has norm exp(o(t)), some of the observed residues reaches exp((β₀−λ)t−o(t)). Take the supremum over β₀. For λ≥B, K≥0 suffices.

**Arithmetic use.** Fix λ=0 and, for example, h=1. It would suffice to find arbitrarily large starting points at which the r+1 binomial sums over primes are all ≤exp(t/2+o(t)) in modulus. The filter L depends on the spectrum only in the proof; the test K is computed without knowing a single zero. The simultaneous maximum is essential in this proof. A zero crossing of a single one of the sums does not provide the block bound. Relative to 240, the continuous interval of observations, the optimal fit and the numerical subtraction of the main term have been eliminated.

**Simplification for the global objective.** In the case λ=0 and h=1 the FIRST difference suffices, even with the same exact exponent B. Indeed, in the ceiling above replace the order r by 1, keeping r as the number of observed steps. In the floor L still has degree ≤r, while the multiplier of the chosen zero has modulus comparable to δ=1/(4G)=exp(−o(t)); for every β₀>1/2 it suffices to choose 1/2<σ<β₀. The argument gives log(1+exp(−t/2)max_(k≤r)|S(t+(k+1)δ)−exp(δ)S(t+kδ)|)/t→B. Thus the pending estimate for the sign can be formulated using only consecutive differences of two counts with positive weights. By telescoping it is equivalent in exponent to controlling the oscillation on the mesh of exp(−kδ)S(t+kδ), since r=exp(o(t)) and rδ≤1.
