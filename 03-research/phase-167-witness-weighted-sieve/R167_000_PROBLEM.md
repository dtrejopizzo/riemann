# R167_000 — The missing object: witness-weighted sieve bound for twisted Λ sums on a short range

**Status:** statement. Phase 167. Goal: build the inequality that the map (R166_802) leaves as the single
missing piece. Treated as a multiplicative-number-theory problem; the connection with D is in §4 and is not
used in §§1–3.

## 1. Fixed data (all known or bounded from the record)

- A scale X = e^{2T} with T ∈ (0.8047, T_max], T_max ≤ min_ρ τ(ρ) ≤ T_L(γ*) + 0.226 (R165_101). A gap Δ > 0.
- A real weight w: [log X, log X + 2Δ] → ℝ, of the form w = (G²)^∨ * ǩ with G entire real-rooted of type T and K
  of type ≤ Δ with K ≥ 0 on ℝ (R164_601 Props 1.1–1.3; R166_501 B(3)). Available properties of w: smooth,
  bounded by a ‖G‖²‖K‖-type quantity, and its transform is G²K, non-negative on ℝ.
- A frequency γ > H = 3·10¹² and an exponent δ ∈ (0, ½).

## 2. The quantity

$$\mathcal S(X,\Delta;\gamma,w)\;:=\;\sum_{X\le n\le Xe^{2\Delta}}\Lambda(n)\,n^{-1/2}\,n^{i\gamma}\,w(\log n).$$

## 3. The problem (no zeros, no ζ as an analytic function)

> **(WS) Witness-weighted sieve bound.** Prove, using only Λ's structure (support on prime powers,
> Λ(p^k) = log p, Λ ≥ 0, combinatorial identities: Möbius, Selberg Λ·log + Λ*Λ = μ*log², Vaughan/Heath-Brown,
> Selberg and large sieves), that
> $$|\mathcal S(X,\Delta;\gamma,w)|\;\le\;C\,X^{\,\eta}\,\|w\|_\star\qquad\text{with }\eta<\delta,$$
> for the (X, Δ, γ, w, δ) of §1, with explicit C and norm ‖·‖_⋆.

Observations fixing the problem:
- **Without a weight and asymptotically, (WS) with η < δ for every range is RH** (R166_802 Thm 3: the twisted
  sum's exponent is Θ − ½). So (WS) can only be true **on the finite range** [X, Xe^{2Δ}] with the concrete
  weight w and the concrete frequency γ, and must fail if forced to hold at every scale.
- **Classical sieves give η = ½** (Brun–Titchmarsh, Selberg, large sieve: R166_802 Thm 4). Getting below ½
  without zeros is the content.
- **The weight has structure:** w = (G²)^∨ * ǩ, with (G²)^∨ supported on [−2T, 2T] and of autocorrelation form
  c_F; the transform G²K ≥ 0 on ℝ. It is a weight **of truncated positive type**, not an arbitrary weight. That
  is the information no sieve has used.
- **Mandatory M_m test:** the bound must fail if Λ is replaced by Λ + β_m with
  β_m(u) = Σ_j 4cos(γ_j u)cosh(δ_j u) continuous (R163_801 Thm 5). Every sieve acts on integers; a continuous
  density cannot be sieved. The exact step where atomicity enters must be identified.
- **Mandatory f_t test:** f_t has an atomic prime side over a semigroup with irrational generators (R163_901).
  The Möbius/Selberg identities hold only in ℕ's Dirichlet algebra: that is where support integrality enters.

## 4. Connection with D (not used above)

At the witness, P gives Quartet_K + OnLine_K = 𝔄_K − 2Re 𝒮-type. The balance requires |𝒮| ≳ X^{δ}·(weight) for
the quartet to win. (WS) with η < δ forbids it. R166_802 Thm 1–2 says the bound must be an **upper** one and of
exactly strength δ; R166_501 says it must use Λ beyond the window and see β_m; R166_201 says w depends on all of
X (global). (WS) satisfies all three by construction, if proved.

## 5. Round 1 plan

- A1: formulate the exact quantitative requirement: which (η, C, ‖w‖_⋆) are needed, as functions of (T, Δ, γ,
  δ), to beat the quartet, using R165_101/102's bounds for T and the cone's geometry (R163_401 §3).
- A2: build (WS): Selberg sieve / large sieve with the twist n^{iγ} and the positive-type weight w; Vaughan
  identities on the short range; exploit that the weight's transform is ≥ 0 (duality: Σ_n Λ(n)n^{−½+iγ}w(log n) =
  ∫ Ĝ²K · (translated prime comb)); seek η < ½ on the finite range and measure the shortfall to η < δ.
- A3: the M_m and f_t tests: localize the step where atomicity and support integrality enter any (WS)-type
  bound, and prove a continuous density violates it.
- Review at the end of the round.
