# A parameter-free quadratic prime average measures the maximal relative displacement

For the explicit weight and cut of 208–209, let A_N(u)=Σ_{p≤M₁(u)^(2N)}(log p)c_N(log p;u)/√p. For integers N≥4 form the unique nonnegative number

    E_N=∫₃ᴺ |A_N(u)|² du/u⁴.

Each E_N uses only primes up to M₁(3)^(2N), since M₁(u) decreases. The ordinary limit is proved

    lim E_N^(1/(2N)) = R_* = 1 + sup_ρ (Re ρ−1/2)²/(Im ρ)².

If RH holds, moreover E_N→0. If it fails, E_N grows exponentially for ALL N large enough, although the exponent can be arbitrarily small depending on the location of the zero. Thus it would suffice to prove that E_N is bounded along an unbounded sequence of integers. That arithmetic bound is not established.

**Global control of the error of 209.** For u≥3 and N≥2 one has |b_N(u)+2A_N(u)|≪u log(2u), with absolute constant, although only the o(1) of 209 at fixed rates or on compact sets is used. By scaling H_u(τ)=H₁(τ/u), 0≤H_u≤1 on the line, the archimedean term costs O(u log(2u)), and the polar O(1). On the shifted line, ∫|H_u(τ+i)|dτ≪u because in the variable τ/u the height is ≤1/3 and the integrand has an integrable majorant independent of that height. The cost of truncating the complete sum of 208 is then O(u) by Chebyshev, uniformly in the rate and in the cut X_N≥1. Powers ≥3 cost O(u) by ||c_N||∞≪u. For squares, 209 proves for the unit-scale profile ||c_N(·;1)||₁+||c'_N(·;1)||₁≪1 by estimates on the real line that do not use the contour at i. On rescaling, those norms are O(1) and O(u), respectively. Integrating by parts in the infinite sum over squares using θ(x)≪x and the O(u) endpoint, as in 209, gives O(1+u). Its truncation tail is already controlled by the absolute bound. This proves the uniform inequality.

**Maximum per zero and global ceiling.** With z=δ+iγ, h_u(z)=−4u²z²/(u²−z²)². Maximizing the modulus over a=u², the derivative has the sign of |z|⁴−a²; the maximum occurs at u=|z|>3. There h is real POSITIVE and equal to |z|²/γ². Moreover Σ_ρ |h_u(z)|≪u log(2u). Indeed, |u²−z²|≥u²+γ²−1/4 and |γ|>14; on |γ|≤u each term is O(1) and on |γ|>u it is O(u²/γ²). The count Z3 and the dyadic sum conclude. Hence |b_N|≤C u log(2u) R_*^(N−1). The preceding error bound and the integrability of log²(2u)/u² control the limsup of the root by R_*. Under RH, 209 and the same spectral argument at any height give A_N(u)→0 except on the countable set of ordinates; dominated convergence with the indicator of [3,N] proves E_N→0.

**Floor under RH.** Around the first ordinate γ₁, for fixed x in [−1,1] take u=γ₁ exp(x/√N). The profile proved in 209 gives A_N(u)→−m(γ₁)exp(−x²). Changing variables on that interval and applying Fatou to the nonnegative functions shows liminf √N E_N>0. This local lower bound also holds without RH by Z2. In particular the lower limit of the root is at least one.

**Floor if there is a zero off the line.** In that case R_*>1 is attained, because |δ|≤1/2 and |γ|→∞ in the tail. Fix a maximizer and u₀=|z|. The only terms attaining R_* at u₀ are those of the same quartet, with their multiplicities: both |z|=u₀ and the same |δ|/|γ| are required, which together fix |δ| and |γ|. All have positive value at u₀. The others have modulus ≤R_*−η with some η>0 in a fixed neighbourhood, by uniform decay in height and finiteness of the rest. On |u−u₀|≤c/N, with c>0 small enough and independent of N, each dominant term has, after raising to the power N, argument of modulus ≤π/4 and modulus ≥R_*^N exp(−C c), by bounded derivatives of the local logarithm. The remaining ones contribute in absolute sum O((R_*−η)^(N−1)) by the first-moment ceiling. Thus b_N≥c'R_*^N on that whole interval for large N. The local additive error is O(1), so that E_N≥c''R_*^(2N)/N, and the claimed limit is obtained.

**Difference in scope.** 207–208 related a limsup at fixed rate to detection intervals and then took a supremum in u. Here one uses the fact that the individual maximum in the rate is real positive, avoiding cancellations for all N on an interval of length comparable to 1/N. This gives a single finite arithmetic sequence and an ordinary limit for the RELATIVE displacement. The arguments do not bound E_N subexponentially over the true primes at unbounded scales.

With the verified height G one immediately obtains 1≤R_*≤1+1/(4G²)=1+1/(3.6·10²⁵). That bound comes directly from Z2 and the critical strip and does not establish R_*=1. The independent review checked the per-zero optimization, the isolation of the quartet and the global error with integrable weight.
