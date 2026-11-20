# In which frequencies of the rate parameter a possible violation of the sign lives

Use b_N from 207, extended to 0<u≤1/2 through the same spectral sum (no claim about the original domain of the form is needed there). Write w_ρ=|γ|−i sgn(γ)δ, with z=ρ−1/2=δ+iγ, and Θ=max_ρ |arg w_ρ|. Thus tan Θ=max |δ/γ|. The signed average against any FIXED frequency of log u decays as O_t(N^(−1/2)), independently of RH. More precisely, if RH fails, the energy at exponential scale concentrates in the two bands |t|/(2N)≈tan Θ. This determines which oscillations of the parameter must be kept before attempting an estimate of the energy.

**Factorisation.** For s=−3/2+it and N≥1,

    ∫₀^∞ u^(s−1)b_N(u)du = K_N(s) Z(s),
    K_N(s)=4^N Γ(N+s/2)Γ(N−s/2)/(2Γ(2N)),
    Z(s)=Σ_ρ w_ρ^s.

The powers use the principal branch. For positive real w the integral of u^(s−1)[4u²w²/(u²+w²)²]^N is w^s K_N(s) by beta substitution. Both sides are holomorphic for Re w>0, by local domination on compacts, and therefore coincide there. For the interchange of the sum with the integral use |u²+w²|≥cos(Θ)(u²+|w|²). After scaling by |w| one obtains, for fixed N, a constant times |w|^(−3/2); Z3 makes the series summable. In particular |Z(s)|≤C exp(Θ|t|). The inequality |K_N(s)|≤K_N(−3/2)=O(N^(−1/2)) follows from the real beta integral and Stirling. Thus every band |t|≤o(N) has energy at most exp(o(N)), also if some zero leaves the line.

**Where the exponent is attained.** By Plancherel in log u the energy I_N=∫₀^∞ |b_N(u)|²du/u⁴ is (2π)⁻¹∫|K_N(s)Z(s)|²dt. Its root of order 2N tends to R=sec²Θ. In u≥3 the ceiling and the floor are those of 210 for b_N: in the off-line case the extreme quartet gives the floor on an interval of width comparable to 1/N. Under RH the first zero gives the floor on an interval of width comparable to 1/√N by the profile of 209 (or directly by positivity of all summands). In 0<u<3, |h_u|<1 by 207 and the first height; Σ|h_u|≤Cu² by Z3 and |γ|>14. This gives a bounded contribution even with u⁻⁴. At infinity the bound Cu log(2u) R^(N−1) of 210 ensures integrability.

For y=|t|/(2N), uniform Stirling in the half-plane Re z≥N−3/4 gives

    |K_N(s) Z(s)| ≤ C N^(−1/2) (1+y²)^(−1/2) exp(N f(y)),
    f(y)=log(1+y²)−2y arctan y+2Θy.

Indeed the factors Γ(N(1±iy)±3/4) admit the uniform Stirling expansion in the sector |arg z|≤π/2; the opposite real shifts cancel in the powers of the modulus. The unique maximum of f is at y=tan Θ, since f'=2(Θ−arctan y), and equals log R. For ε>0 the part |y−tan Θ|≥ε has strictly smaller supremum of f: f tends to −∞ at infinity. Integrating the quadratic bound using ∫(1+y²)⁻¹dy<∞ shows an exponential gap relative to I_N, even under RH. In particular, under failure of RH the energy restricted to | |t|/(2N)−tan Θ |<ε keeps the root limit R. No hypothesis on separation of the ordinates or absence of cancellation in Z(s) is required: the floor is given by 210 before transforming.

**Use and frontier.** 210 avoids cancellation by integrating the square in u. Here one computes why measuring only a few signed moments of u, even of growing frequency o(N), would lose all the exponential growth. The series Z(s) is built with the same zeros and its type Θ only gives the previous ceiling. This change of variable does not prove Θ=0. The result is about the spectral extension of b_N; the transform of the truncated prime sum is not identified with K_N Z.

**Transfer to the finite arithmetic observable.** Define B_N(t)=∫₃ᴺ A_N(u)u^(−5/2+it)du with A_N from 210. Although there is no pointwise equality with the factorisation, there is a uniform L² comparison:

    ||2B_N + K_N Z||_(L²(dt)) = O(1).

By Plancherel it suffices to estimate b_N+2·1_[3,N] A_N in L²(du/u⁴). On [3,N] use the absolute error Cu log(2u) of 210. For u<3 the bound Cu² was already given. For u>N≥4, 208 gives |h_u(z)|≤M_(1/2)(u)≤exp(C/u²) for every zero. The sum of first moduli of 210 gives |b_N(u)|≤Cu log(2u) exp(CN/u²), with square integrable against u⁻⁴ uniformly in N on that tail. This proves the comparison.

Therefore, if Θ>0, on the complement of each band | |t|/(2N)−tan Θ |<ε, the energy of B_N has limsup of 2N-th root at most max(1,exp(sup_complement f))<R. In the band it keeps exactly the rate R by 210. This is indeed a statement about finite primes. In particular the root of the arithmetic energy over |t|=o(N) has limsup ≤1 without hypotheses, also if RH fails. Under RH the O(1) comparison does not automatically transfer the exponential gap of the spectral complement.
