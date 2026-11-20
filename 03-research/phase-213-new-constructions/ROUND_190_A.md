# Strict positivity up to 131/50 with a Chebyshev filter

For every function in the domain of paper 47 and 0<T≤131/50, W_T(f)≥exp(−20000000001)||f||₂². The same verification height G=3·10¹² of 175–189 is used. The additional stretch is (2.58,2.62].

**Choice of the filter.** Let u(τ)=1−sinc(τ/H)^(2k), a=kR²/(3H²), d=m/2 and D_d the Chebyshev polynomial of the first kind. Take

    h(u)=D_d(2u/a−1)/D_d(2/a−1),   P(u)=h(u)²,   B=D_d(2/a−1)^(−2).

The filtered datum has transform h(u(τ)) f̂(τ). Since the degree is d, its additional support is at most 2kd/H. The argument of 178 for the spectral extension preserves exactly the identity with mask 1−P: on the line P is the square of a real even multiplier, and both autocorrelations have support inside the zone where the extension cutoff equals one. For 0≤u≤a, P≤B. For a≤u≤1 it increases up to one; hence the mask is nonnegative at all real atoms. For u≥7a/2 one has P≥B exp(m arcosh(6))/4. The gain uses D_d(cosh v)=cosh(dv). At fixed degree, the factor D_d(6) is the maximum possible at that point among real polynomials of degree ≤d bounded by one on the low interval, after rescaling to [−1,1]: a strict excess would give d sign changes of the difference at the alternating extrema plus a zero at 6 on rescaling the presumed extremizer to match D_d there.

**Parameters and margin.** Use T=131/50, s=29/2, U=log s, R=240000000, k=20, m=1020000000, H=400000000000, N=10¹⁰. The rational two-row computation of 189 gives ||C||≤17.31 on checking 1911 endpoints. One has T+km/H<U and 2U<5.5. The archimedean bracket minus comb is ≥1/10 for |τ|≥R and ≥−24 globally by 178. As in 179, u≤a on |τ|≤R and u≥7a/2 from |τ|≥2R on. Reserving half of the margin on |τ|>G/2 and using the leakage η of 179 at Ω=2R, the integrated floor, in units of B||f||², is

    η exp(m arcosh(6))/80 −24.

The filter has a larger polar value than the monomial filter. With |u(i/2)|≤k/H², the cost in these same units is at most 4 exp(T) exp(m arcosh(1+2k/(H²a))). The certificate verifies that the logarithm of the positive term of the floor exceeds the logarithm of this cost by more than ten, and is greater than ten. Thus more than 2B||f||² is kept after paying the pole.

**Spectral tail.** For a≤u≤1, P is convex: D_d has an expansion in powers of x−1 with nonnegative coefficients (use D_d(1+2v)=Σ_j binom(2d,2j)(1+v)^(d−j)v^j by the hyperbolic formula). Then 1−P(u)≤P'(1)(1−u); differentiating the hyperbolic formula gives P'(1)=m tanh(d arcosh(2/a−1))/√(1−a)≤2m. On |τ|>G/2 we have u≥7a/2, so the mask is ≤2m(2H/G)^(2k). As in 178 the power of |τ| in the mask also dominates the logarithmic growth of the correcting density. Its high cost is <1/1000 and is absorbed by the reserved density ≥1/(80π). The low cost is ≤2π exp(−20000000002)||f||² while B≥exp(−m arcosh(2/a−1))>exp(−20000000000). The low cost is less than B||f||². By inclusion of supports and density the conclusion follows for the whole indicated domain.

**Check.** Run python3 verify_190.py with python-flint. The computation uses Arb balls of 192 bits and does not form a polynomial of degree one billion: it verifies the hyperbolic identities through their logarithmic bounds. The Chebyshev minimax method is classical. Here it is applied to the mask of 179 and the support, real positivity, complex poles and the two corrections of the full formula are checked.

The substitution in the identity of the projected measure, the sign of the real mask, the high gain and the polar cost were checked independently.
