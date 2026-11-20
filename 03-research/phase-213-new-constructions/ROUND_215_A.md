# A frequency band of width one detects the extreme angle without knowing it

For A_N from 210 and B_N(t)=∫₃ᴺ A_N(u)u^(−5/2+it)du from 214, define

    J_N = (∫_[√N,√N+1] |B_N(t)|²dt)^(1/2).

Then lim log(1+J_N)/√N = Θ = max_ρ arctan(|Re ρ−1/2|/|Im ρ|). If Θ=0 one even has J_N→0 by 210 and Plancherel. If Θ>0, for sufficiently large N there are two-sided bounds

    c exp(Θ√N)/√N ≤ J_N ≤ C exp(Θ√N)/√N.

The constants may depend on the extreme zeros. In particular it suffices to find an unbounded subsequence with log(1+J_N)=o(√N). The width and the centre of the band are explicit and independent of the height of any counterexample. 214 only localised the exponential rate in N: its N-th root ceiling of one in this band is compatible with the present criterion.

**Why the spectral sum does not cancel over the whole band.** In the notation of 214 take t positive, σ=−3/2. If Θ>0, only a finite set of w has arg w=−Θ, because |arg w|→0 in height. The rest has arg w≥−Θ+η for some η>0. By absolute convergence in σ,

    exp(−Θt) Z(σ+it) = Σ_j d_j exp(it log r_j) + O(exp(−ηt)),

where the r_j are the distinct moduli of the extreme w and d_j=m_j r_j^σ exp(−iσΘ) incorporates their multiplicity. None vanishes. The Gram matrix on [0,1] of the exponentials with frequencies log r_j is positive definite: a combination vanishing on the interval has all its derivatives at zero vanishing and Vandermonde gives zero coefficients. After translating the interval to [T,T+1] the coefficients only acquire phases. Therefore the L² norm of the trigonometric polynomial there lies between two positive constants independent of T. The exponential difference above, of norm o(1), preserves the floor. Hence ||Z|| on that interval is comparable to exp(ΘT).

**Normalisation and transfer.** For t=√N+d with 0≤d≤1 the beta formula of 214 gives uniformly

    |K_N(σ+it)|=(1+o(1))√(π/N) exp(−1/4).

In the uniform Stirling expansion used there one has y=t/(2N), log(1+y²)−2y arctan y=−y²+O(y⁴), Ny²→1/4 and Ny⁴→0. The constant is obtained from K_N(0)=4^N Γ(N)^2/(2Γ(2N)). By the global L² comparison of 214, the norms of 2B_N and K_N Z on the band differ by at most O(1). For Θ>0 the spectral floor tends to infinity and dominates that error. For Θ=0 it suffices to use ∫|B_N|²dt=2πE_N→0. All claims follow.

**The exact arithmetic estimate that is missing.** With W_N(u)=A_N(u)u^(−5/2), integrating first in the frequency gives the real identity

    J_N²=∫₃ᴺ∫₃ᴺ W_N(u) W_N(v) cos((√N+1/2)log(u/v)) sinc(log(u/v)/2) du dv,

with sinc(x)=sin(x)/x and sinc(0)=1. Finiteness of the sums and of the interval authorises Fubini, and the imaginary part vanishes by symmetry. The sign would be equivalent to a ceiling exp(o(√N)) for this single quadratic along a subsequence. Bounding the expression by absolute values loses the oscillation of log(u/v); the spectral argument does not provide the prime estimate.

**A single sample per square order.** One can also dispense with the frequency integration if a limsup is kept. Let D_k=B_(k²)(k), k≥2 integer. Then

    limsup_k log(1+|D_k|)/k=Θ.

The comparison of 214 is also pointwise with additive error O(1), uniform in N,t: the bounds on b_N+2·1_[3,N]A_N of its last section are integrable against u^(−5/2)du (at zero Cu², at infinity Cu log(2u)). Under RH even D_k→0 by 209 and domination for A_N using 210. If Θ>0, in the spectral expansion above P(k)=Σ d_j exp(ik log r_j) has strictly positive integer mean square. Indeed group the frequencies equal modulo 2π: the d_j share a phase and therefore each grouped coefficient is nonzero. The average in k of |P(k)|² tends to the sum of the grouped squared moduli by the geometric-series formula. Since P is bounded, there is a set of integers of positive lower density where |P(k)|≥c>0. On it one has |D_k|≥c' exp(Θk)/k eventually, and the corresponding upper bound holds on the whole tail. No floor is concluded for each k. This gives an alternative obligation: it suffices to prove that the single arithmetic sample D_k has subexponential growth in k for ALL large k.
