# N_BUILD_010 — Linearizing Φ at Λ: amplification falsifier, locality, and whether 𝒦_T can be quantitative

## Corpus check
Paper 46 thm:finmod(ii) (c_*(T,2)), prop:wit-sens (Lipschitz |Δλ_A| ≤ Σ|Δv_n|), cor:margin1; R164_102 Prop I (Hamburger);
R162_903 (nonlinear uses of Λ*1 = log collapse); N_BUILD_009. grep "linearization|DΦ|fixed point|Lipschitz in the weights|
residual": no prior linearization of a Poisson–Euler map. Review points (1)–(3) of the coordinator answered in §4.

## 1. The amplification falsifier and c_*(T,2) (PROVED)
λ_c := Λ + c·δ_{log 2}·(log 2 weight), i.e. a(2) = log 2 + c. The window weight v_2 changes by 2c/√2 = √2c, so by
prop:wit-sens **λ_A(T; λ_c) ≥ λ_A(T) − √2 c**, hence c_*(T,2) ≥ λ_A(T)/√2 (and for T ≥ 1, ≤ … by cor:margin1 λ_A is at most
4·10⁹Te^{−15.449T}, CITED): the falsifier becomes negative at an amplitude c that is doubly-exponentially small in T.

## 2. First-order residual (PROVED, formal in 𝔄_∞ with C_c^∞ tests)
Z[λ_c] = Z * exp_*(c′δ_{log 2}), c′ := c·2^{−½}/log 2, so Z[λ_c] − Z = c′ Z*δ_{log 2} + O(c²) = c′ Σ_{m≥1}(2m)^{−½}δ_{log 2m}
(the comb of the even integers). Poisson for 2ℤ: Σ_m f(2m) = ½∫₀^∞ f + ½Σ_{k≥1} 𝒞f(k/2) (+ the x = 0 term, irrelevant for tests
vanishing near 0). Hence 𝒞^*(Z*δ_{log 2}) = ½M̃ + ½·(comb on ½ℤ₊) ≠ Z*δ_{log 2}, and
 r(λ_c) = λ_c − Φ(λ_c) = c′·(−∂_s)[Z^{−1} * (Z*δ_{log2} − 𝒞^*(Z*δ_{log2}))] + O(c²) =: c·ρ₂ + O(c²),
with ρ₂ ≠ 0 (Prop 2 of 009: no nonzero fixed perturbation; here directly: the half-integer atoms of 𝒞^*(·) at x = 3/2 are not
cancelled by any even-integer atom). So ‖r(λ_c)‖ ≍ c in every norm in which ρ₂ ≠ 0.

## 3. Consistency at first order (PROVED) — and why it is empty
For the falsifier, min δ_T ≥ λ_A − √2c and ‖r‖ = c‖ρ₂‖ + O(c²); so (Ω_Φ) with 𝒦_T = K‖r‖ holds on this family as soon as
K‖ρ₂‖ ≥ √2. Consistent, no contradiction. But in general, prop:wit-sens plus a bound ‖η‖ ≤ K_T‖(I − DΦ(Λ))η‖ on window
perturbations η gives, to first order,
 min δ_T(Λ + η) ≥ λ_A(T) − K_T‖r(Λ + η)‖ + O(‖η‖²).
Evaluated at η = 0 this is λ_A(T) ≥ λ_A(T): **any Lipschitz 𝒦_T built by linearization at Λ makes (Ω_Φ) at λ = Λ identical
to WP_T; it carries no information on the sign.** (NO-GO, PROVED, for "perturbative 𝒦_T around Λ".)

## 4. The three review points
(1) Novelty. The characterization "Λ is the unique (PE) comb" is Hamburger's theorem re-expressed (CONDITIONAL on its growth
hypothesis); NOT new. What would be new is a non-perturbative inequality min δ_T(λ) ≥ −𝒦_T(λ − Φ(λ)) for all λ ∈ 𝔐⁺; §3 shows
that only a global (non-linearized) proof could carry content.
(2) Locality (PROVED). δ_T(λ) depends only on λ|_{[0,2T)} (L2_011 row 5). The residual at window scale does NOT: Poisson
maps the lattice nℤ (scale x ~ n) to (1/n)ℤ and a continuous part of density 1/n, so r|_{[0,2T)} depends on λ at all scales
(the Möbius factor Z^{−1} and the dual lattices mix them). Conversely, for a modification η inside the window, the residual
contains c·(nℤ-comb − Poisson dual) with an O(‖η‖) coefficient: there is no mechanism making r small while η is not —
except along near-self-dual directions. Such directions exist approximately: periodic perturbations a(n) = Λ(n)(1 + ε Re χ(n)),
χ primitive mod q, are Poisson-self-dual at conductor q (Gauss sums), so their conductor-1 residual is O(ε) — the same order as
their effect on the window form. No direction with residual o(‖η‖) and form change ≍ ‖η‖ has been found; existence is OPEN.
(3) Quantitative 𝒦_T. K_T := sup_η ‖η‖_{w}/‖(I − DΦ(Λ))η‖ on window perturbations (weighted ℓ¹ norm ‖η‖_w = Σ_{n<N}|η_n|/√n,
the norm of prop:wit-sens) is the only candidate constant. It is finite iff I − DΦ(Λ) is injective with closed range on window
perturbations — plausible (Prop 2) but not proved; its T-dependence is unknown. Even when finite, §3 shows it decides nothing
at Λ. So 𝒦_T can be made quantitative only perturbatively, and then it is empty. **(Ω_Φ) survives only as a global statement.**

## 5. Next construction (global, not perturbative)
A homotopy/continuation argument in 𝔐⁺: a path λ_t (t ∈ [0,1]) from a comb λ_0 with WP_T(λ_0) true and computable by hand
(e.g. λ_0 = 0 for T ≤ 0.58 where λ_{∞,P} > 0 — CITED) to λ_1 = Λ, with a monotone quantity controlling the window bottom along
the path by the residual r(λ_t) → 0. By W-fam/Lemma flowdet (Paper 46 §barriers) any flow coefficient near a crossing is a
functional of the minimizer; the path must be chosen so that the crossing is excluded by the residual, not by the flow. First
pen-and-paper test: λ_t = tΛ (Z^{t}, fails (P) for t ≠ 1): compute r(tΛ) and compare with the known failure of WP_T(tΛ) for
t > 1 + λ_A/κ_T (prop:wit-sens) — does ‖r(tΛ)‖ grow like |t − 1| uniformly in T?

## Self-review
- §1 correct (prop:wit-sens with v₂ = 2Λ(2)/√2). §2 formal: Z*δ_{log 2} and its Poisson dual are tempered; the identity is in the
weak sense on C_c^∞ tests in x > 0. ρ₂ ≠ 0 argued by an atom not cancelled — needs that Z^{−1}* does not cancel it: Z^{−1}*
is invertible, so it maps nonzero to nonzero. Correct.
- §3 is the key honest finding: a perturbative (Ω_Φ) is a tautology at Λ. NO-GO for that class.
- §4(2) the character direction: Poisson self-duality of χ-twisted combs holds with conductor q and Gauss-sum factor; its
conductor-1 residual is O(ε) not o(ε); recorded; existence of o-directions OPEN.
No sign contact; no negative value of 𝔞_T.
