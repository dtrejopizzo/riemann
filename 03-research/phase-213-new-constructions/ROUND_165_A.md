# Measuring the threshold of the distant block at an individual scale

In the notation of 162–164, for fixed constants C₀ large and η small,

    cXH ≤ N_X(H) ≤ CXH,    C₀ log X ≤ H ≤ ηX.

The upper bound gains the logarithm of 163 down to separations of logarithmic order. The tool external to the pigeonhole argument is Selberg's classical upper sieve inequality. The uniformity needed in the gap is detailed below.

**Pair sieve.** For p,q≤AX with fixed A, fix h=q−p>0. For odd h only one pair with p=2 occurs. For even h sieve n(n+h) for n≤AX by primes ℓ≤z=X^(1/20). The roots modulo ℓ are ν(ℓ)=2 unless ℓ divides h, in which case ν(ℓ)=1. The counts for a squarefree modulus l have error O(ν(l)), by individual classes. Selberg's upper inequality gives CX/G(z) plus O(z⁶), where G(z)=Σ_{l≤z} μ²(l)∏_{ℓ|l}ν(ℓ)/(ℓ−ν(ℓ)). For the error the quadratic form in Selberg's weights λ_l suffices: |λ_l|≤∏_{ℓ|l}(1−ν(ℓ)/ℓ)^(−1)≪log²(2z), by the formula for the optimal weights and Mertens. The double sum of errors is dominated by z² log⁴(2z) max_{l≤z²}ν(l)≪z⁶. Pairs with some prime ≤z cost O(z).

To bound G from below, expand the Euler product of 1+ν(ℓ)/(ℓ−ν(ℓ)) up to ℓ≤z^δ. Normalizing its terms as probabilities over l, the expectation of log l is Σ ν(ℓ)log ℓ/ℓ≤Cδ log z by Chebyshev. With fixed small δ at least half of the product has l≤z by Markov. By Mertens the full product is ≫log² z / M(h), with M(h)=∏_{ℓ|h}(1+3/ℓ): the exceptional factor at each ℓ>2 changes the ratio by (ℓ−2)/(ℓ−1) and its inverse is ≤1+3/ℓ. The prime 2 costs a fixed constant. Moreover Σ_{h≤H}M(h)≤H∏_ℓ(1+3/ℓ²)=O(H) on expanding over divisors. Thus the total weight Σ log p log q over distinct pairs in |p−q|≤H is O_A(XH), even for small H. It suffices to multiply the count by O(log² X), absorbing z⁶+z per gap.

**Local sign and crossing.** The positive rectangle argument of 163 still gives ≫XH. The cost of all negative products is now O(XH(H/X)²) by Lipschitz and the sieve; choose η small. This proves both uniform bounds. Write E_X=∫₁² S(Xv)²dv and T_X=max(C₀log X,(E_X−D_X)_+/X). Let H_X be the infimum of the H in [C₀log X,ηX] with F_X(H)≤0. Then H_X≍T_X: the identity F_X=E_X−D_X−N_X gives the lower bound using N_X≤CXH and the upper using N_X≥cXH. For large X there is room in the interval because E_X=o(X²) by 164. The upper bound moreover guarantees the sign for ALL H≥C' T_X up to ηX. No monotonicity of the signed block is presupposed.

**The equality case of 164.** If 0<α=2Θ−1<1, the majorant E_X=O(X^(2Θ)) gives strict negativity at H=M X^α with fixed M sufficiently large. For H=X^α itself, if no zero attains Θ, the absolute formula of 164 gives U(x)=o(x^Θ) by dominated convergence of the coefficients, and the same result for S because Θ>1/2. Then F_X(X^α)<0 eventually. For an attained supremum and prefactor one this proof does not decide the sign. In particular the local measurement of the crossing does not prove that T_X is subpolynomial; that would require controlling the excess E_X−D_X.

**Cross-check.** The pigeonholes of 163 only gave a ceiling O(XH log X), which did not allow comparing the crossing with the energy excess through uniform constants. The use here of the pair sieve is classical; the quantitative comparison concerns the block of 162. It is not a new method for bounding the real part of the zeros.
