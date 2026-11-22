# K3_GAMMA_001 — Candidate K3: Γ-limit / ultraproduct of leakage-renormalized windows

Phase 200, stage 3. Pure mathematics; the only arithmetic is on already published data
(MORI15_EXTREMAL_001).

**One-line verdict.** K3.1 = (P0c) is PROVED in asymptotic form (exact limit constant 1/(1+3/8) = 8/11) and
ARGUED with an explicit constant for all μ ≥ 5; but the Γ-limit 𝒩_∞ is **comb-generic** (it does not see Λ at leading order on the
Hermite scale) and **not quantitative** (μ₀ ineffective, exclusion 19(b)+26 remains intact), and it fails the Mori test by
a factor > 2. **K3 as a route to L′♯: NO-GO.** K3.1 survives as a Λ-free tool.

## 0. Corpus and index

- SPEC_SIGN_OBJECT_001 §C (K3), BRIDGE_001 §2 (P0c), §9 (gap (15, μ₀)), AUDIT_CONSTRAINTS_001 (rows 19, 26, pairwise
  exclusion), MORI15_EXTREMAL_001 §4 (coefficients, leakage, κ_emp), Paper 46 thm:ext-cell, cor:ext-cellpos, cor:ext-cfals,
  thm:ext-multi, thm:ext-layer and the following paragraph ("the layer does not distinguish c′v_n from v_n at leading order").
- ROUTES-TRIED index, l.278 (front I, phase 193–194): "Γ-convergence, concentration-compactness, rearrangements: dead."
  The spec gives leakage renormalization and the self-dual sector ψ_{4j} as the new reason. §2.4 of this memo shows this
  difference **does not dodge** the cause of failure: after renormalizing, the leading term is still universal.
  Grep of "ultraproduct," "nonstandard," "Hermite" in the index: no other entry. Nothing else from the index is retried.

## 1. Rigorous definition of the object

**1.1 Data.** μ ≥ 5, λ = μ, T = ½log μ, c = 2πμ. {ψ_k = ψ_k(c;·)} are the normalized prolate functions in L²(ℝ), with
concentration eigenvalues λ_k(c) ∈ (0,1) strictly decreasing in k (CITED, Slepian–Pollak). The leakage is
d_k := 1 − λ_k(c). The leakage form ℓ(f) := ‖f‖²_{L²(ℝ)} − ‖f‖²_{L²(−1,1)} is **diagonal** in {ψ_k} (double orthogonality,
CITED): ℓ(Σa_kψ_k) = Σ a_k² d_k.

**1.2 Space.** 𝒳_μ := {f = Σ_{j=0}^{J(μ)} a_{4j}ψ_{4j} : a ∈ ℝ^{J+1}, f(0) = 0}, J(μ) = ⌈μ + C₁ log μ⌉ (self-dual
even sector, BRIDGE §3.2). The remaining admissibility conditions (f̂(0) = 0 is automatic on the self-dual sector: f̂ = ±f by
the self-duality of ψ_{4j} under the rescaled Fourier transform, so that f̂(0) ∝ f(0); CITED Slepian) reduce to
a single linear restriction
  (R_μ)  Σ_j a_{4j} ψ_{4j}(0) = 0.
E: f ↦ g = Ef is BRIDGE's operator (window at T). W_T(Ef) is the Weil form of the declared carrier.

**1.3 Renormalization and coordinates.** 𝒩_μ(f) := W_T(Ef)/d₄. Leakage coordinates b_j := a_{4j}(d_{4j}/d₄)^{1/2}, j ≥ 0; so
ℓ(f)/d₄ = Σ_j b_j² =: ‖b‖². In b coordinates, (R_μ) is Σ_j b_j·ψ_{4j}(0)(d₄/d_{4j})^{1/2} = 0.

**1.4 Hermite limit.** For fixed k and c → ∞, c^{-1/4}ψ_k(x/√c) → h_k(x) (Hermite functions) locally uniformly
(CITED: Slepian 1965; Rokhlin–Xiao). In particular ψ_4(0)/ψ_0(0) → h_4(0)/h_0(0) = 3/(2√6) = 0.61237…, and for fixed k,
d_{k+4}/d_k ≍ c^{4}·(const)^{-1} → ∞ (Fuchs asymptotics d_k ~ √π 2^{3k+2} c^{k+½} e^{−2c}/k!, CITED). Consequence:
the coefficient of b₀ in (R_μ), ψ₀(0)(d₄/d₀)^{1/2}, **diverges** like c^{2}; the restriction in b coordinates forces
b₀ = O(c^{-2})·(…) → 0: in the limit b₀ disappears, and a₀ becomes **enslaved** to a₄ via a₀ = −a₄ψ₄(0)/ψ₀(0) + O(…), without
costing any leakage (d₀/d₄ → 0).

**1.5 The limit object.** Let 𝒰 be a non-principal ultrafilter on ℕ and H_𝒰 = ∏_𝒰 ℓ²(b) the Hilbert ultraproduct (sequences
bounded in ‖b‖ modulo those null in 𝒰). The forms 𝒩_μ (restricted to (R_μ)) are quadratic forms on ℓ²; if |𝒩_μ(b)| ≤
M_μ‖b‖² with M_μ bounded in 𝒰, st 𝒩_μ defines a bounded form 𝒩_𝒰 on H_𝒰. The object the spec calls 𝒩_∞ is the restriction
of 𝒩_𝒰 to the separable subspace ℓ²(b₁, b₂, …) ↪ H_𝒰 (constant sequences) — a **quadratic form** (not a measure; a
self-adjoint operator on ℓ² via Riesz). Equivalent Γ-limit: 𝔉 = Γ-lim 𝒩_μ in the weak ℓ² topology on balls.

**1.6 Necessary hypotheses (explicit).** (H1) uniform bound M_μ ≤ M (necessary for st to exist); (H2) equicoercivity:
𝒩_μ(b) ≥ −C + c₀‖b‖² uniformly; (H3) compactness: every sequence with ‖b^{(μ)}‖ = 1 and 𝒩_μ bounded has a
**strongly** convergent subsequence in ℓ² (not just weakly). (H1) is **false** as stated: §2.2 shows 𝒩_μ ~ (log μ)‖b‖². One
has to renormalize a second time by L(μ) := log 2μ, or subtract the leading term (§2.3). (H3) is **false** in ℓ²(b):
§3.2 (mass escaping toward the plunge j ≈ μ).

## 2. Lemma K3.1 (= P0c) and its dependence on Λ

**2.1 Lemma K3.1.** *For every μ ≥ μ₁ and every f ∈ 𝒳_μ,*
  ℓ(f) ≥ κ₁(μ)·d₄·‖f‖²,  κ₁(μ) = [1 + r(μ)²(1 + ε(μ))]^{-1},  r(μ) = ψ₄(0)/ψ₀(0),  ε(μ) = Σ_{j≥2} ψ_{4j}(0)² d₄ / (ψ₄(0)² d_{4j}),
*and κ₁(μ) → 1/(1 + 3/8) = 8/11 = 0.7273 as μ → ∞. The constant is optimal (attained on span{ψ₀, ψ₄} ∩ (R_μ)).*

*Proof (PROVED given what is CITED in 1.1, 1.4).* Let f = Σa_{4j}ψ_{4j}, ‖f‖² = Σa², ℓ = Σa²d_{4j}. Since d_{4j} ≥ d₄ for j ≥ 1
(monotonicity, CITED), ℓ ≥ d₄Σ_{j≥1}a². By (R_μ) and Cauchy–Schwarz with weights d_{4j}:
  a₀²ψ₀(0)² = (Σ_{j≥1} a_{4j}ψ_{4j}(0))² ≤ (Σ_{j≥1} a²d_{4j})·(Σ_{j≥1} ψ_{4j}(0)²/d_{4j}) ≤ ℓ·(ψ₄(0)²/d₄)(1 + ε).
Hence ‖f‖² = a₀² + Σ_{j≥1}a² ≤ ℓ/d₄·[r²(1+ε) + 1]. Equality: take a₈ = … = 0, a₀ = −a₄r; then ℓ = a₄²d₄ + a₀²d₀ and
‖f‖² = a₄²(1+r²); as d₀/d₄ → 0 the ratio tends to (1+r²)^{-1}. Limit: r → 3/(2√6), r² = 3/8; ε(μ) → 0 because
d₄/d₈ ≍ c^{-4} and Σ_{k ≤ 4J}ψ_k(0)² ≤ 2Σλ_kψ_k(0)² + Σ_{k > plunge}ψ_k(0)² ≤ 2c/π + O(√c·log μ) (sinc kernel
identity Σλ_kψ_k(x)² = c/π, CITED, plus the bound sup ‖ψ_k‖_∞² ≲ √c from Bonami–Karoui, CITED), so that
ε(μ) ≲ (c/ψ₄(0)²)·(d₄/d₈) ≲ c^{1/2}·c^{-4} → 0. □

*Version for all μ ≥ 5: ARGUED.* Requires explicit values of r(μ) and d₄/d₈ for c ∈ [10π, ∞). At μ = 15, r = 0.6073
(MORI15 §4), κ₁ = 1/(1 + 0.3688) = 0.7306; the Fuchs formula with c = 31.4 gives d₄/d₈ ≪ 10⁻³, so ε is irrelevant, but
turning this into a bound with certified constants is explicit Bonami–Karoui, not done here.
*Transfer to ‖Ef‖* (literal form of P0c): uses the ‖g‖ ↔ ‖f‖ comparison from A Lemma 4.2 (MECH 3.1); it inherits that lemma's status.

**2.2 Does K3.1 depend on Λ?** No: K3.1 contains neither W_T nor the comb. It is a statement about prolates and a linear restriction.
It is **comb-generic by construction**, which is expected for (P0c) (BRIDGE lists it as "low leverage, needed for
closure"). It is not REF-D: it says nothing about the sign. Label: tool PROVED (asymptotic) / ARGUED (μ ≥ 5).

**2.3 Computing the Γ-limit: where c enters.** For b supported at a fixed j (Hermite region), the exterior data of Ef is
the continuation of the prolate tails ψ_{4j}|_{|t|>1}, frequency-c chirps with caustic envelope
|ρ_k(t)|² ≈ ½d_k·(2/π)·(t√(t²−1))^{-1} (thm:ext-layer(ii)–(iii), Lemma ext-envelope). The pieces of 𝔔 on that data:
- (D) Layer + cell diagonal: ∫𝔴_N|ρ_k|² with 𝔴_N(t) = H(t)log(tc/2π) − 2H₁(t) ≥ log 2N (Lemma B.0, PROVED). In layer
  (1,2): (1−χ_k)[⅔log 4N − 0.107689](1+η) (thm:ext-layer(iii)). In cells t ≥ 2 (fraction ⅓ of the dθ measure):
  weight log 2N + F(⌊t⌋) + O(1).
- (R) Resonances (1,n): O(N^{-1/2}log N) per unit mass (thm:ext-layer(iv), thm:ext-multi R_res = O(c^{-1/2})).
- (L) Lines m ≥ 2 of the Möbius lattice of the exterior data, and (E) the boundary channel g(T) = λ^{½}f(λ), jumps at
  x_n = log(λ/n), of size f(λ)² ≈ c·d₄a₄²/λ (BRIDGE §8): **same scale d₄** as the diagonal, with no log μ factor.

Hence, on the fixed-j sector,
  𝒩_μ(b) = L(μ)·Q₀(b) + Q₁^{(Λ)}(b) + o(1)‖b‖²,  Q₀(b) = Σ_j b_j² (diagonal),
with L(μ) = log 2μ and Q₁ an O(1) form containing: −0.0718 (= ⅔·0.1077) from the layer, the average of F in cells, (L), (E).

*With comb c′Λ* (cor:ext-cfals, and the paragraph after thm:ext-layer): the layer is **identical** (H₁ = 0 on (1,2)); the cells
change by −2(c′−1)∫_{t≥2}H₁(t)|ρ|² = −(c′−1)·O(1)·d_k (the envelope decays like t^{-2}, ∫_2^∞ log²t·t^{-2}dt < ∞); the
resonances change by (1−c′)log n·w_n, summable. **c′ enters only Q₁, never the L(μ)Q₀ term.**

**2.4 Decision.** The Γ-limit that exists is that of 𝒩_μ/L(μ), and it equals
  𝔉(b) = Γ-lim 𝒩_μ/L(μ) = Q₀(b) = ‖b‖²  (on the Hermite region; ARGUED, PROVED for each fixed j with μ ≥ 130 via
  thm:ext-layer(iii) plus cell control),
**the same for every c′ > 0** (also for c′ > 1: the negativity of cor:ext-cfals(ii) lives in chirps of frequency
ν_J = 2πJ^{(c′−1)/2} on cells J, not in prolate tails of frequency c = 2πμ; K3's sector is, by construction, in the
high-frequency regime of cor:ext-cellpos, whose threshold is logarithmic and comb-generic). Therefore:
- 𝔉 is the identity form: a trivial "square." It is positive, and remains so for cΛ with any c, Beurling with a_n ≡ 1 on
  average (Λ∗1 = log only enters F(⌊t⌋) = O(log)), and Λ with primes deleted (they alter F in cells: Q₁ order).
  **Comb-generic ⇒ NO-GO** (restriction 2).
- If instead the leading term is subtracted, 𝒩_μ − L(μ)Q₀ → Q₁^{(Λ)} does retain Λ (cells, lattice, boundary), but Q₁ has
  no sign and is not a known bounded form: it is exactly the content of the P2/P3 planks and of BRIDGE's boundary
  channel. The limit contributes no square; it rewrites the question as "L(μ) + inf Q₁ > 0," and the dependence on Λ is
  sub-leading (relative order L(μ)^{-1}). This is the L1 F-sign restriction: **the sign is second order and the Γ-limit loses it.**
- The spec's caveat ("K3 is only admissible if the limit retains the μ(n)-cocycle resonances at leading order")
  **does not hold**: the (1,n) resonances are O(N^{-1/2}log N), even below Q₁. K3 is asymptotic Theorem B′/thm:ext-multi
  under another name, as the spec warned.

## 3. Exclusion 19(b) + 26 and the value of μ₀

**3.1 μ₀ with existing tools.** Any quantitative version needs the layer diagonal with controlled
error: thm:ext-layer(iii) requires (H_ν) c ≥ 200 (μ ≥ 32), and its η is < 1 only for c ≳ 820, **N ≳ 130** (row 26). Moreover
the transfer from 2.4 to L′♯ requires L(μ) > sup|Q₁| over the admissible sphere; with the boundary E of size comparable to the
diagonal (row 19(b): 51–78 % at μ = 15) there is no bound on Q₁ whatsoever. Hence μ₀ ≥ 130 at best with
current constants, and μ₀ = ∞ (undetermined) as long as Q₁ is unbounded.

**3.2 Compactness does not close it.** The spec's "(a)+(b)+compactness ⇒ ∃μ₀" argument is by contradiction: if L′♯ failed
for μ_n → ∞, normalize b^{(n)} and pass to the limit. It fails in two places:
(i) (H3) is false: a sequence b^{(n)} can concentrate at j_n → ∞ (e.g. j_n ≈ μ_n/2, near the plunge
4j ≈ 4μ ≈ 2c/π), converge weakly to 0 in ℓ², and 𝔉(0) = 0 contradicts nothing. For j ~ μ the Hermite approximation fails
(Langer/Airy plunge regime); there d_{4j} ≈ 1 and the exterior data is no longer a caustic tail. Concentration–
compactness would require a limit profile at the plunge — this is, again, the boundary channel, 19(b). (This is the same reason
index entry l.278 declared Γ-convergence dead.)
(ii) Even with compactness, the argument gives an **ineffective** μ₀: it produces no number, and therefore cannot be spliced with
the certified base H.1 (μ ≤ 15).

**3.3 Does the Γ-limit say anything for 15 < μ < μ₀?** No. A Γ-limit is a statement about μ → ∞ in 𝒰; it contains no
information at finite μ without a rate, and the only available rate (η from thm:ext-layer) is vacuous for μ < 130. The pairwise
exclusion 19(b)+26 remains intact. **Best case for K3: CONDITIONAL** on (i) a uniform bound on Q₁ (boundary + lattice) and (ii) a
certified covering of 15 < μ ≲ 130 — and even then the result would be comb-generic (§2.4), so it does not count as
progress on row D.

## 4. Mori test μ = 15 (NUMERICAL, arithmetic on MORI15 §4)

Data: a₀ = 1.106365, a₄ = −1.821723 (a₈ ≈ 3·10⁻⁵, negligible), d₄ = 1.1667·10⁻⁷⁰ (from a₄²d₄ = 3.872·10⁻⁷⁰),
W_T(g*) = 4.763·10⁻⁷⁰, W/d₄ = 4.0824, κ_emp ∈ [0.56, 1.09].

**4.1 K3.1.** Prediction: ℓ_struct/(d₄‖f*‖²) = 1/(1+r²) with r = 0.6073: 0.7306. Data: a₄²/(a₀²+a₄²) = 3.3187/4.5427 =
0.7306. **Exact match** (f* is the extremal of K3.1: it lives in span{ψ₀,ψ₄} with a₀/a₄ = −r = −0.6073; MORI15 gives
a₀/a₄ = −0.6073, and a₄/a₀ = −1.6466 = −1/r). Hermite error: r²_∞ = 0.3750 vs 0.3688, κ₁ 0.7273 vs 0.7306 (0.45 %).
Reading: Mori's extremal **saturates (P0c)** — the leakage part is decided by f(0) = 0 alone, without arithmetic.

**4.2 κ_emp.** K3 in its Γ-limit form predicts W/ℓ → L(μ)·(fraction) ≈ log 30 = 3.40 (full diagonal) or
⅔log 60 − 0.0718 = 2.66 (layer only) per unit of ℓ. Data: κ_emp ∈ [0.56, 1.09]. Discrepancy: factor 2.4–6.

**4.3 W/(1−λ₄) = 4.08.** Prediction of the leading part: a₄²·[⅔log 4N − 0.1077] = 3.3187·2.622 = 8.70 (layer only, N = 15),
or a₄²·log 2N ≈ 11.3 (layer + cells). Data: 4.08. **Ratio 2.13–2.77 > 2**: by the spec's own death
criterion (§C.5: "if 𝒩_∞(b*) differs from 4.08 by more than a factor of 2, the limit does not retain the structure and K3 dies")
**K3 dies**. Moreover the difference 8.70 − 4.08 ≈ 4.6 (53 % of the diagonal) is Q₁'s negative share — consistent with row 19(b)
(boundary 51–78 %): the Γ-limit loses exactly what decides the size of W. Caveat: (H_ν) requires c ≥ 200 and at μ = 15, c = 94;
the layer formula is NUMERICAL there, not PROVED (row 26).

## 5. Labels, index entry, OPEN

**Labels.**
- Lemma K3.1 (P0c in f coordinates): **PROVED** asymptotically (mod CITED: Slepian–Pollak, Fuchs, Bonami–Karoui, Hermite),
  optimal limit constant 8/11; **ARGUED** for all μ ≥ 5 (explicit constants pending); the ‖f‖ → ‖Ef‖ step inherits A
  Lemma 4.2. Comb-generic by nature; a tool, not a sign.
- Γ-limit 𝔉 = Γ-lim 𝒩_μ/log 2μ = ‖b‖² on the Hermite region: **ARGUED** (PROVED for fixed j and μ ≥ 130 via
  thm:ext-layer(iii) + cells). **Comb-generic** (holds for c′Λ with every c′ > 0, deleted primes, Beurling): **NO-GO**.
- Without renormalization by log μ: 𝒩_μ diverges, (H1) false. With the leading term subtracted: Q₁^{(Λ)} with no sign = P2/P3
  planks + boundary; not a new object: **NO-GO** (reformulation).
- Compactness (H3): **false** (escape to the plunge); μ₀ ineffective; exclusion 19(b)+26 intact on (15, μ₀): K3 at best
  **CONDITIONAL**, and comb-generic regardless.
- Mori test: K3.1 **confirmed exactly** (0.7306); Γ-limit **fails** by a factor 2.1–2.8 in W/d₄ (NUMERICAL).
- **Overall K3: NO-GO** as a route to L′♯. Row D OPEN. L′♯ OPEN. No sign whatsoever is claimed.

**Index entry (phase 200, K3):**
> **K3_GAMMA_001 (phase 200, stage 3; Γ-limit/ultraproduct of leakage-renormalized windows on ψ_{4j}, Hermite
> scale):** NO-GO. 𝒩_μ = W_T/d₄ ~ log 2μ·‖b‖² + Q₁; Γ-lim 𝒩_μ/log 2μ = ‖b‖² is the same for c′Λ (all c′), Beurling, and
> deleted primes (the layer does not see c′; cells, lattice and boundary are O(1) = sub-leading): comb-generic; the sign lives in Q₁
> (boundary 19(b), lattice). Compactness false (escape to plunge j≈μ), μ₀ ineffective, exclusion 19(b)+26 intact. Mori test:
> leading term 8.7–11.3 vs 4.08 (factor >2, the spec's death criterion). Tool salvaged: Lemma K3.1 = (P0c) PROVED
> asymptotically, κ₁ → 8/11, saturated exactly by f* (0.7306). Do not retry: Γ-limits/ultraproducts of renormalized W_T
> on the Hermite scale. (`03-research/phase-200-sign-object/K3_GAMMA_001.md`) Row D OPEN.

**OPEN.**
1. K3.1 with explicit constants for all μ ≥ 5 (explicit Bonami–Karoui for d₄/d₈ and ψ_{4j}(0)), and the step to ‖Ef‖.
2. Q₁^{(Λ)}: uniform lower bound of the boundary channel + lattice m ≥ 2 on the self-dual sector — this is the real
   question, and no scaling limit contains it; it is BRIDGE's P2/P3/19(b).
3. The plunge profile (j ≈ μ) as its own object (Langer, not Hermite): the only place where a concentration–compactness
   argument could see something non-trivial; not proposed here because it coincides with the already-recorded boundary channel.
4. Row D, L′♯, (★★): OPEN.
