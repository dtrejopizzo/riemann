# LINK_016 — Dense range of map 011 on the even polar-free carrier

2026-10-19. **PROVED, favourable review in AUDIT_016.md:** at the critical parameter α=1/4, for each T>0, the map U_T of LINK011 has dense range in 𝓗_(1/4) when restricted to even F with zero cosh moment. The same holds restricting the source to a smooth core.

This closes, for that map, the gap «signed continuous combination positive only on its image» of 015. It does not prove that U is injective or surjective, does not identify V with the whole Gaussian factor and obtains no sign for Q_T.

## 0. Corpus and written difference

Consulted: the project rules, the ROUTES-TRIED-INDEX index (Hamburger, Fourier anti, domain 015, LINK011–014), master grid and current base crossword `05-meta-and-planning/ABCD-CLOSURE-PLAN/CROSSWORD-TO-D.md`. The base file replaced the dated name; entry 015 was verified.

The Hamburger/co-Poisson identification routes are not reopened as a sign mechanism for D. **New reason:** the annihilator of the image of the map 011, whose domain and kernel are already fixed, is computed. The Fourier equation appears as a consequence of that annihilator, and is used only to prove density. The result answers a concrete question that did not follow from 015: positivity on the image versus positivity on the whole space. No other positive form nor an FE «with defect» is proposed as a proof of the node.

## 1. Exact object and statement

Fix α=1/4, s=1/2. In 𝓗=𝓗_(1/4), write

`f_d=X_d−1/d`, `||f_d||²=S(d,d)=O(d^(−1/2))`, d≥2.

Its span is dense by the definition of 𝓗 as the completion of the Haar-centred algebra. The retained map is

`U_TF=Σ_(d≥2)a_d(F)f_d`,

`a_d(F)=2∫_(−T)^T F(x)e^(x/2)[τ(d²exp(2x))−τ(exp(2x))/d]dx`.

LINK011 proved absolute convergence in norm and boundedness from L²([−T,T]). Define

`𝒫_T^ev={F∈L²([−T,T]):F(−x)=F(x), ∫F(x)cosh(x/2)dx=0}`.

**Theorem 1.** For all T>0,

`closure U_T(𝒫_T^ev)=𝓗`.                            (1)

Complexifying the spaces is allowed; the real statement follows from the same argument on their real parts.

## 2. Annihilator of the range and its analytic function

Use an inner product linear in the first argument. Let h∈𝓗 be orthogonal to U_T(𝒫_T^ev). Put

`η_d=⟨f_d,h⟩`, `c=Σ_(d≥2)η_d/d`.

Cauchy–Schwarz and the diagonal bound of 011 give

`|η_d|≤C||h||d^(−1/4)`;

hence the series defining c converges absolutely. The identity of the map and its convergence allow writing

`⟨U_TF,h⟩=∫_(−T)^T F(x)b_h(x)dx`,

`b_h(z)=2exp(z/2)[Σ_(d≥2)η_d τ(d²exp(2z))−cτ(exp(2z))]`. (2)

The function b_h is holomorphic in the strip `|Im z|<π/4`: there Re(exp(2z))>0, and on each compact subset of the strip the Gaussian series and the sum over d converge uniformly with all their derivatives.

The annihilator in the even subspace of the single-moment condition is the span of cosh(x/2). Hence there exists λ∈C with

`[b_h(x)+b_h(−x)]/2=λcosh(x/2)`

for almost every x∈(−T,T). Both sides are analytic; the equality is pointwise and the identity principle extends it to the whole strip, in particular to all real x.

## 3. Arithmetic distribution of explicit coefficients

Define an even, purely atomic distribution with no derivatives of deltas:

`μ=Σ_(n∈Z\{0}) a_|n| δ_n`,

`a_n=Σ_(d|n,d≥2)η_d−c`, `μ({0})=0`.

The coefficients have polynomial growth: the bound |η_d|≤C and the fact that the number of divisors is ≤n suffice. Hence μ is an even tempered distribution. Its Gaussian transform is, for y>0,

`Θ_μ(y):=⟨μ,exp(−πy·²)⟩`

`=Σ_(d≥2)η_dτ(d²y)−cτ(y)`.

The double sums are absolutely convergent; (2) gives

`b_h(x)=2y^(1/4)Θ_μ(y)`, `y=exp(2x)`.

The even identity of the previous section is exactly equivalent to

`Θ_μ(y)+y^(−1/2)Θ_μ(1/y)=(λ/2)(1+y^(−1/2))`, y>0. (3)

The factor λ/2 is important. Define

`μ′=μ−(λ/2)δ_0`.

Then (3) becomes

`Θ_(μ′)(y)+y^(−1/2)Θ_(μ′)(1/y)=0`.                 (4)

## 4. Gaussian injectivity on even tempered distributions

The argument is included so as not to assume a uniqueness of measures that would not cover distributions.

**Lemma 2 (PROVED).** If ν is even tempered and `⟨ν,exp(−πy·²)⟩=0` for all y>0, then ν=0.

**Proof.** Differentiating in y at y=1 is legitimate in the Schwartz topology. One obtains

`⟨ν,x^(2k)exp(−πx²)⟩=0`, k≥0.

The corresponding odd moments are also zero by parity. The function

`G(z)=⟨ν,exp(−πx²+zx)⟩`

is entire: on each compact set of z, the Gaussian uniformly dominates all Schwartz seminorms and allows differentiation. All its Taylor coefficients at 0 are zero, so G≡0.

For purely imaginary z, G is the Fourier transform of the distribution `exp(−πx²)ν`, represented by a smooth function of at most polynomial growth on the real axis. The equality is also checked by duality against Schwartz tests; the interchange is justified by tempered continuity. Fourier injectivity gives `exp(−πx²)ν=0`.

For any compactly supported test φ, `exp(πx²)φ` is another compactly supported test, so ν(φ)=0. Hence ν=0 as a distribution, and by tempered continuity also on Schwartz space. ∎

Take the Fourier convention `exp(−2πixξ)`. Duality and the exact transform of a Gaussian give for every tempered distribution

`Θ_(𝓕ν)(y)=y^(−1/2)Θ_ν(1/y)`.

Since μ′ is even, so is `μ′+𝓕μ′`. From (4) and Lemma 2:

`𝓕μ′=−μ′`.                                        (5)

No explicit formula with zeros is involved.

## 5. Integer atomicity and the Fourier sign force vanishing

μ′ is a sum of **pure deltas at integers**, with coefficients of polynomial growth. Its Fourier transform is a 1-periodic distribution: each delta δ_n is transformed into exp(−2πinξ), and the series is interpreted in the tempered sense.

By (5), μ′ is also 1-periodic. Comparing its masses at n and n+1 forces all coefficients to be one and the same constant C, including that at 0. Hence

`μ′=CΣ_(n∈Z)δ_n`.

At y=1, (4) gives `Θ_(μ′)(1)=0`. But that quantity is `Cθ(1)` and θ(1)>0. Thus C=0, and μ′=0.

Since μ had zero coefficient at 0, the mass of μ′ at 0 is −λ/2; hence λ=0. One obtains μ=0. At n=1, its coefficient a_1 is −c, so c=0. Then

`Σ_(d|n,d≥2)η_d=0` for each n≥2.

Induction on n gives η_n=0: all proper divisors already have zero coefficient. Thus h is orthogonal to each f_d; by density of their span, h=0. This proves (1).

The restriction to pure deltas is part of the proof: no general classification of all distributions supported on Z with possible derivatives of deltas has been claimed.

## 6. Smooth core and consequences for signed forms

The even space C_c∞((−T,T)) with zero cosh moment is dense in 𝒫_T^ev in L². One approximates by smooth even tests and corrects the moment with a fixed test of nonzero moment. Since U_T is bounded, its image also has closure 𝓗. Hence density does not depend on allowing discontinuous tests nor on using all of L² without a core.

Let B be a Hermitian form **continuous in the norm of 𝓗**. From (1),

`B(U_TF)≥0 for all F∈𝒫_T^ev`

`⇔ B(h)≥0 for all h∈𝓗`.                           (6)

The non-trivial direction is continuity and approximation by the dense range. This already holds for a single window T>0.

In particular, for a fixed real combination of the three pieces of 015,

`B_(a,b,c)=aκG_s+bκvv*+cΠ`,

positivity only on the even polar-free image of 011 is equivalent to global PSD; by CONSTRUCTOR015 it occurs exactly if a,b,c≥0. The gap of signed continuous combinations in that span, positive only on that image, is closed.

With LINK014, no fixed nonzero combination of that span that is positive on the image can provide a positive uniform domination by Q_T using the same map 011. That conclusion is not deduced for T-dependent coefficients from 014 alone.

## 7. Precise limits

- The result is exclusive to the map 011, α=1/4 and its even polar-free tests; it does not extend to every map using −R.
- The proof uses all modes of the even polar-free space, or its dense core. It does not claim density for the image of a finite canonical block E_N(T), nor does it allow inferring global PSD from positivity only on that block.
- Dense range does not mean surjectivity, injectivity nor a bounded inverse. The compactness proved in 011 does not contradict density.
- Forms not continuous in the norm of 𝓗, changes of map, other kernels and T-dependent factors are not excluded.
- V is not identified with all of ℒ_α, nor is it proved that the Gaussian inversion preserves V.
- No equality, domination nor sign of the remainder of Q_T is obtained. Density does not turn the auxiliary kernel into the node.

**Status:** dense range and closure of the gap of continuous positivity on the image PROVED, favourable audit in AUDIT_016.md. D remains OPEN and active; no paper modified.
