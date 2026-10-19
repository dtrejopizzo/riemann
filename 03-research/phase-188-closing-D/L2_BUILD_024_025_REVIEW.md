# L2_BUILD_024 + L2_BUILD_025 (Theorem S, Lemma I, Proposition H) — Review (pen and paper)

Checked against Paper 47 (F̂(τ) = ∫F e^{iτt}; A = ∫Fe^{t/2}, B = ∫Fe^{−t/2}; thm:nyq-cone P_T = (¼−∂²)H²_0(I_T), F̂ = (τ²+¼)Ĝ; eq:Aform;
lem:contA; cor:void). or mentioned.

## 1. The profile (024 §2, 025 §1) — CONFIRMED with one FIX
- ĝ(z) = ∫₀^a e^{bt}e^{izt}dt = (e^{(b+iz)a} − 1)/(b+iz). Zeros: (b+iz)a = 2πik, k ≠ 0 ⇒ z = 2πk/a + ib; z = ib is removable (ĝ(ib) = a ≠ 0). ✓
  g̃(t) = g(−t) has transform ĝ(−z), zeros at 2πk/a − ib. ✓  Ĝ₀ = ĝ(z)²ĝ(−z)², = |ĝ|⁴ > 0 on ℝ. ✓
- G₀ = 4-fold convolution of bounded functions with jumps at the ends: C², vanishing to order 3 at the endpoints of its support (length 4a), so
  G₀ ∈ H²₀(I_{2a}) and F₀ = (¼−∂²)G₀ ∈ P_{2a} (thm:nyq-cone). ✓  F̂₀ = (τ²+¼)|ĝ|⁴ > 0, F̂₀ = O(τ^{−2}), F̂₀² = O(τ^{−4}). ✓
- FIX: the hypothesis should read |b| > ½ (024's "b ≠ 0" is insufficient, see §3(b); 025's "b > ½" is sufficient; b < −½ works symmetrically).
  At ±i/2, Ĝ₀ ≠ 0 since all zeros of ĝ(±z) have |Im z| = |b| > ½. ✓

## 2. Definition of B and the (⇒) direction (024 §1, §2(iii)) — CONFIRMED
- B(d) = 𝔞(F₀, τ_dF₀) is the bilinear form of eq:Aform (archimedean multiplier m acting on c₀, comb at all log n with c₀ supported in
  [−2T₀, 2T₀], finitely many n per d). Even, real, continuous. ✓
- For translates a_k + I_{T₀} ⊂ I_T (primitive: A(τ_aF₀) = e^{a/2}A(F₀) = 0, L2_023 Lemma L), Σs_ks̄_lB(a_k − a_l) = 𝔞_T(Re F) + 𝔞_T(Im F) ≥ 0
  under the target (complex coefficients handled by B even and real). Positive definiteness follows. ✓

## 3. Lemma I / (⇐) direction (025 §1, Steps 1–4) — CONFIRMED with two FIXes
Step 1. ∫Bφ = (1/2π)∫mF̂₀²φ̂ − ½Σ v_n[(c₀*φ)(log n) + (c₀*φ)(−log n)] for φ ∈ C_c^∞. The memo's form "−Σ v_n(c₀*φ)(log n)" is correct
  only for EVEN φ. FIX: take χ even; then φ_j = ψ̌χ(·/j) is even (ψ is even and real: ĉ_G = |Ĝ|² even for real G, F̂₀ even). With that, ✓.
  Bochner: ∫Bφ = ∫φ̂ dμ, μ ≥ 0 finite. ✓
Step 2. Holomorphy strip: ĉ_G(z) = Ĝ(z)Ĝ(−z) (G real) has double zeros at ±i/2 (Ĝ(±i/2) = 0 ⟺ A = B = 0) — each of ±i/2 is a zero of
  both factors, order ≥ 2. ✓  F̂₀(z)² = (z²+¼)²Ĝ₀(z)² has zeros of order exactly 2 at ±i/2 and the others at |Im z| = |b|. ✓  So ψ = ĉ_G/F̂₀²
  is holomorphic in |Im z| < |b|. ✓
  Decay: on |Im z| ≤ β < |b|: |e^{(b+iz)a}| = e^{(b−Im z)a} ≥ e^{(b−β)a} > 1, so |ĝ(z)| ≥ (e^{(b−β)a} − 1)/|b + iz|, same for ĝ(−z): 1/Ĝ₀² grows
  polynomially; (z²+¼)^{−2} is cancelled near ±i/2 and bounded elsewhere on the substrip; Ĝ(x+iη) = O_N(e^{T|η|}(1+|x|)^{−N}) for smooth
  compactly supported G. Hence ψ is rapidly decreasing on horizontal lines, and contour shift gives |ψ̌(u)| ≤ C_β e^{−β|u|}. ✓
  c₀*ψ̌ = c_G: ĉ₀ψ = F̂₀²·ĉ_G/F̂₀² = ĉ_G, both factors integrable. ✓
Step 3. (a) φ_j → ψ̌ in L¹; φ̂_j → ψ uniformly and boundedly; ∫φ̂_j dμ → ∫ψdμ (μ finite); ∫mF̂₀²φ̂_j → ∫mF̂₀²ψ by domination with
  |m|F̂₀² ∈ L¹ (O(log τ·τ^{−4})). ✓  (b) |(c₀*φ_j)(log n)| ≤ ‖c₀‖₁ sup_{|w − log n| ≤ 2T₀}|ψ̌(w)| ≤ C n^{−β}e^{2βT₀}; Σ2Λ(n)n^{−½−β} < ∞ iff
  β > ½ — this is exactly why |b| > ½ is needed (choose ½ < β < |b|). Dominated convergence to Σ_{n<e^{2T}} v_n c_G(log n). ✓
  Conclusion 𝔞_T(G) = (1/2π)∫mĉ_G − Σ v_n c_G(log n) = ∫ψ dμ ≥ 0 (eq:Aform on P_T). ✓
Step 4. Density. The memo's mechanism "mollification + slight dilation of G" is WRONG as stated: dilation does not preserve the Tate
  conditions (A(G(·/r)) = r∫G(s)e^{rs/2}ds ≠ 0 in general). FIX: approximate at the level of H ∈ H²₀(I_T) with G = (¼−∂²)H (thm:nyq-cone):
  shrink H by a dilation toward the centre (preserves H²₀ and supports), mollify (stays in C_c^∞(I_T)), then G_k := (¼−∂²)H_k ∈ P_T ∩ C_c^∞
  automatically (Tate is automatic for elements of (¼−∂²)H²₀). Convergence in the form norm ∫(1+log(2+|τ|))|Ĝ|² follows from continuity of
  dilation and mollification in the weighted space ∫(τ²+¼)²(1+log(2+|τ|))|Ĥ|² (standard; CITED, cf. lem:contA). With this FIX, ✓.
**Verdict on Theorem S: PROVED for profiles with |b| > ½, with the two FIXes (even cut-off; density via H). The equivalence
"λ_A(T) ≥ 0 ∀T ⟺ B_{F₀} positive definite on ℝ" stands.** Novelty: a reformulation (Bochner on one translation orbit with F̂₀ > 0), new to
the corpus in its single-explicit-profile, T-free form; no sign content (as both memos state).

## 4. Proposition H (025 §3) — CONFIRMED; novelty: CLASSICAL
- Pair term: x = σ − β, y = σ − 1 + β, t = τ − γ: Re[1/(x+it) + 1/(y+it)] = (x+y)(xy+t²)/((x²+t²)(y²+t²)). ✓ For σ > 1, 0 < β < 1:
  x, y > 0 ⇒ term > 0. ✓ The paired Hadamard expansion of Re ξ′/ξ (constant cancelling against Σ Re 1/ρ) is classical, CITED. ✓
- D_σ = 2Re ξ′/ξ(s) = m_σ + p_σ − Σ2Λ(n)n^{−σ}cos(τ log n); at σ = ½, m_{½} = m and p_{½} = 0. ✓ B^{(σ)} = h_σ⋆h̃_σ with ĥ_σ = √D_σ·F̂₀ ∈ L²
  (D_σ = O(log τ), F̂₀² = O(τ^{−4})). ✓
- Novelty: the positivity of Re ξ′/ξ(s) for Re s > 1 is CLASSICAL (Lagarias-type results on the positivity of Re ξ′/ξ to the right of all zeros;
  CITED). Proposition H is that fact read on the single-profile orbit; record it as classical in content, new only in framing.
- Discrimination claims: a_P (no FE pairing) and Epstein/DH (zeros with real part > 1 exist, Davenport–Heilbronn, CITED) — CONFIRMED as
  stated; the a_P clause is ARGUED (its completed function is not a ξ-type function of order 1 with FE).
- "Transport from σ > 1 to ½": RECORD. Any mechanism transporting the positivity of D_σ (σ > 1) to σ = ½ must be checked against cor:void's
  C_zeros clause: if its only input is the location of the zeros (the pair-term positivity depends on the β's alone), it is an argument from
  membership in C_zeros, and cor:void excludes it as a proof of window positivity at T > ½log2 (the members ζ_a = ζE share the zeros). A valid
  transport must use more than zero location (e.g. the exact Λ through the Euler product at σ = ½, not only through the absence of zeros in
  Re s > 1). 025 §3 already notes that B = B^{(½)} is the analytic continuation, not the boundary value of D_σ — CONFIRMED (at σ = ½ the
  pair terms vanish off the line, x + y = 0).

## 5. Other items
- 024 §0 (sharpness of Theorem T via the explicit formula and Kronecker independence of ordinates): identity/heuristic, CONDITIONAL on an
  unproved independence hypothesis — correctly labelled; it is not used anywhere as a criterion. ✓
- 024 §3 "escape analysis": correct (reformulation; not inside W-loc/W-fam/norm classes; no sign gained). ✓
- No sign certified; no negative value of 𝔞_T for ζ.

## Summary of verdicts
| item | verdict |
|---|---|
| profile, F̂₀ > 0 | CONFIRMED; FIX hypothesis to |b| > ½ |
| (⇒) target ⇒ B p.d. | CONFIRMED |
| Lemma I Steps 1–3 | CONFIRMED; FIX: even cut-off χ (Step 1 formula valid for even φ) |
| Step 4 density | FIX REQUIRED and supplied (approximate H ∈ H²₀, not G; dilation does not preserve Tate) |
| Theorem S | PROVED with the FIXes |
| Proposition H | CONFIRMED; content CLASSICAL (Lagarias-type positivity of Re ξ′/ξ on Re s > 1), new only in framing |
| σ > 1 → ½ transport | must clear cor:void C_zeros clause; zero-location-only transports excluded |
