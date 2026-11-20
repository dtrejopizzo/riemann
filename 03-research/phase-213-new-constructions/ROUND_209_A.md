# Profile of each verified zero in an uncentred finite sum over primes

With H_u, c_N, M₁ and X_N from 208, now define

    A_N(u)=Σ_{p≤X_N(u)} (log p)/√p · c_N(log p;u),

only over PRIMES, without subtracting a background. For every fixed u≥3, b_N(u)=−2A_N(u)+o_u(1). The error also tends to zero along any sequence u_N→u≥3 with u_N≥3. Hence the growth criteria of 207–208 remain valid for A_N. Moreover, if 3<u<G−1, x is real and fixed and u_N=u exp(x/√N), one obtains

    lim A_N(u_N) = −m(u) exp(−x²),

where m(u) is the multiplicity of the zero with positive ordinate u, or zero if it does not exist. For u=3,G−1 at fixed rate the limit −m(u) holds likewise. In particular at the first positive ordinate the sum converges to −1 by Z1. The sum changes cut and weight with the rate; its normalization from 208 is used without an additional factor in N.

**Removing the truncation error.** On the line |H_u|<1 except at ±u. The archimedean term tends to zero by dominated convergence with |m(τ)|H_u(τ), and the polar one by |H_u(i/2)|<1. On the contour shifted to i, |H_u(τ+i)| attains M₁(u) only on a finite set by the formula of 208. Thus ∫ |H_u(τ+i)|^N dτ = o(M₁(u)^(N−1)): divide by that power and apply dominated convergence with |H_u(τ+i)|. For convergent rates the same holds since the quotients converge pointwise to one only at the maxima of the limit, and the majorants have a common tail O((1+τ²)⁻¹). Substitute this prefactor in the Chebyshev count of 208: even at the same cut X_N, the absolute sum of the tail for Λ or for primes alone is o(1).

**Fourier control on the line.** Uniformly for rates in a compact subset of [3,∞), ||c_N||∞+||c'_N||∞→0 and ||c_N||₁+||c'_N||₁=O(1). For the supremum use the integrals of H_u^N and |τ|H_u^N and domination from N≥2. For L¹ use, for g=H_u^N or g=τH_u^N,

    ||g||₂²≪N^(−1/2),    ||g'||₂²≪N^(1/2).

In the coordinate τ/u, the two maxima ±1 are nondegenerate quadratic: H_u(u s)=1−[(1−s²)/(1+s²)]². At small distance y from a maximum one has H^N≤exp(−cNy²) and |(H^N)'|≪N|y| exp(−c(N−1)y²), with constants uniform on the compact set. Integrating the squares gives the indicated powers. Outside those neighbourhoods H≤q<1 and the rational function and its derivatives allow leaving two powers of H in the integrals to control infinity. Plancherel and Cauchy–Schwarz with weight 1+t²/N give the L¹ bound, since ∫(1+t²/N)⁻¹dt=π√N.

**Squares and higher powers.** For exponents ≥3 one has Σ_pΣ_{j≥3}(log p)p^(−j/2)<∞; their contribution tends to zero. For squares, write θ(y)=Σ_{p≤y}log p. The continuous integral approximating Σ_p(log p)/p c_N(2log p) is ∫₁^∞ c_N(2log y)dy/y=∫₀^∞ c_N(2t)dt=H_u(0)^N/4=0. Integrating by parts against θ(y)−y, the difference is bounded by an endpoint term O(|c_N(0)|) plus

    ∫₀^∞ |θ(exp t)−exp t| exp(−t) [|c_N(2t)|+2|c'_N(2t)|]dt.

The endpoint at infinity vanishes for each N by contour decay. By PNT the first factor tends to zero for large t and is bounded on the whole half-line. Split into a fixed compact set and its complement: the compact set uses the suprema tending to zero and the rest the uniform L¹ norms. The result is o(1) without needing an error rate in the PNT. This separates the squares in the complete sum; the preceding estimate for the tail allows returning to the finite cut.

**The profile at known rates.** At every verified rate of the statement each non-critical zero has |h_u|<1 by the geometry of 207. The critical ones too, except at |γ|=u. For a sequence of rates tending to u, all those terms tend individually to zero when raised to the power N: a strict bound in a neighbourhood suffices for each zero, and in the tail a summable majorant O_u(1/(1+γ²)) for the power from N≥1. For the critical pair at ±u the value is exactly sech²(log(u_N/u)); its N-th power tends to exp(−x²). Add the two multiplicities and use the identity with −2A_N. This local recovery does not prove the sign for rates of arbitrary height.

**Antecedents.** In 208 the O(1) error allowed studying exponential growth, without distinguishing a finite limit from zero nor removing the squares. POWER_LOW_TABLE_018 already cancels continuous terms in another row. Here the simultaneous L¹ bound on the weight and its derivative, the PNT and the contour cut at the same X_N allow reading a multiplicity off the simple primes.
