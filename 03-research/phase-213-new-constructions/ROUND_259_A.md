# Binomial subtractions for the octave: construction and necessary cost

Let g be the weight with support [1,2] of 257. For B≥1, let E(B) be the infimum of the error in L¹(dy) when approximating g by finite sums of carries from 258, of any positive split and scale, now with real coefficients whose sum of absolute values is ≤B. One obtains:

* Unconditionally c/B≤E(B)≪exp(−c'√log B) for large B.
* RH is equivalent to being able to obtain E(B)≤B^(−1+o(1)). If there is a zero ρ with real part β>1/2, necessarily E(B)≥c_ρ B^(−(1−β)/β).
* There is an explicit formula of approximation by signed carries that, before discretising the mixture, reproduces the weight EXACTLY for all y≥v, with a cut-off parameter 0<v<1. The leakage lies entirely in (0,v).

**Obstruction for signed coefficients.** The Mellin transform of a carry of scale u and split λ is u^s ζ(s)[1−λ^s−(1−λ)^s]/s for Re s>0 by 099 and continuation (the carry is bounded with finite upper support). Therefore every finite sum has Mellin transform zero at ρ. Its error e has sup norm ≤B+||g||∞. For 0<β<1 integrating |e| against y^(β−1), a decreasing weight, costs at most ||e||∞^(1−β)||e||₁^β/β (concentrate the mass on the initial interval at maximal height). Thus |H(ρ)| is bounded by that quantity. H from 257 never vanishes off the line and H(1/2+iγ₁)≠0 by 14.13<γ₁<14.14 and its explicit formula. This gives both lower bounds.

**Inverse that introduces no split zeros.** Average λ uniformly over [0,1] at scale one and call U(y) the resulting carry. One obtains Mellin transform ζ(s)(s−1)/[s(s+1)], since ∫λ^s dλ=1/(s+1). The mass of U is 1/2. Define

    f(u)=−u g'(u)+2g(u)+(2/u)∫_u^∞g(v)dv,
    a(u)=Σ_(n≤2/u) μ(n) f(nu).

In Re s>1 the Mellin transform of f is H(s)[s+2+2/(s−1)] and that of a is the previous one divided by ζ(s). The product with the Mellin transform of U is H(s), so

    g(y)=∫₀² a(u) U(y/u) du/u.

Fubini here is justified with weight y^(σ−1), σ>1, from the absolutely majorised series of μ. The equality by uniqueness of Mellin also holds pointwise: at y>0 only u≥y intervene; the discontinuities of the floor lie on a null set of u for each fixed y and the integral is continuous by local domination.

**Control of the construction.** For u<1, write X=1/u. The part with n<X is 2hX Σ_(n<X) μ(n)/n, with h=∫g. The part X≤n≤2X is bounded by partial summation, since f has bounded variation on [1,2]. Use the classical unconditional bound M(X)≪X exp(−c√log X) for M(X)=Σ_(n≤X)μ(n), and Σμ(n)/n=0. Integrating by parts in the tail of this last sum (reducing c) gives |a(u)|≪u^(−1)exp(−c'√log(1/u)). Under RH the classical bound M(X)≪_ε X^(1/2+ε) gives |a(u)|≪_ε u^(−1/2−ε).

Cutting the integral at u≥v has coefficient cost B_v=∫_v²|a(u)|du/u and L¹ error at most (1/2)∫₀^v|a(u)|du, by the mass of U at scale u. The tail is exactly zero for y≥v up to possible integration endpoints of measure zero. The truncated mixture is approximated, with arbitrarily small L¹ error and without increasing B_v, by finite sums: the carry depends continuously in L¹ on both parameters on the compact [v,2]×[0,1], by dominated convergence off the jumps; separate the positive and negative parts of the measure. With v=B^(−1/2) the unconditional bound above leaves B_v≤B for large B and gives the announced ceiling. Under RH the cost is O_ε(v^(−1/2−ε)) and the error O_ε(v^(1/2−ε)); eliminating v and leaving ε arbitrary gives the exponent −1+o(1). The obstruction at the zeros gives the converse.

**Additional arithmetic identity.** At physical scale x, with v=2/x and x>2, the truncated continuous mixture reproduces all terms at prime powers m≥2. With L(t)=log(⌊t⌋!)−(2/t)∫₀ᵗlog(⌊r⌋!)dr one obtains exactly Σ_m Λ(m)g(m/x)=∫_(2/x)^2 a(u)L(xu)du/u by the factorisation of factorials. The L¹ bounds for approximation by finite sums are continuous bounds and by themselves do not authorise discretising that identity at the atoms. The route still needs a control of cancellation: the Mertens estimate at square-root scale used to reach the optimal exponent already depends on RH.

**Cross-check.** 099 already identifies the Mellin multiplier for averaged splits; 129–134 already use Möbius inversion in factorial identities. What is additional is the approximation rate for the concrete positive dyadic weight, with cost in total variation of coefficients, a quantitative obstruction at each zero and a construction reaching the critical exponent under RH. 258 excluded positive majorisation of near-exact cost, even with variable splits.
