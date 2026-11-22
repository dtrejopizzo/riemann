# L2_BUILD_027 — The conjugation test for the deformed problem at σ = ½ + η

## Corpus check
016 (dilations U_k: Tate points move, line moves), 017 §1 (e^{βu} on lags is not an autocorrelation), 026 (σ-family, limit lemma, density margin
O(σ−½)), N_BUILD_001 (A) (polar elimination on P_T), Paper 46 lem:polar (2cosh((s−t)/2) has signature (1,1): the reason a codim-2 Tate class exists).
Krein's factorization theorem for nonnegative entire functions of exponential type (CITED: Akhiezer, Lectures on Approximation Theory; Krein 1944).
New: §1–§3.

## 0. The deformed window problem at σ (definition)
Comb weights 2Λ(n)n^{−σ} at lags log n; mean density 2e^{(1−σ)u}du; archimedean symbol m_σ(τ) = Re ψ((σ+iτ)/2) − log π.
Primitive class matched to σ: P^σ_T := {F ∈ L²(I_T) : ∫F e^{±(1−σ)t}dt = 0} (the comb-mean pairing is 2∫₀^{2T}c_F e^{(1−σ)u}du and, c_F being even,
∫_ℝ c_F(u)e^{(1−σ)u}du = A_{1−σ}(F)·B_{1−σ}(F) with A_a = ∫Fe^{at}, B_a = ∫Fe^{−at}: rank two, signature (1,1) — so a codim-2 class kills it,
exactly as at σ = ½). Form: 𝔞^σ_T(F) := (1/2π)∫m_σ|F̂|² − Σ_{n<e^{2T}}2Λ(n)n^{−σ}c_F(log n), F ∈ P^σ_T ∩ D_T. P(σ): 𝔞^σ_T ⪰ 0 for all T.
At σ = ½ this is D exactly.

## 1. Exponential conjugation fails (PROVED)
Any conjugation F ↦ e^{ct}F maps P^σ_T onto {∫F e^{(±(1−σ)+c)t} = 0}; equal to P_T (exponents ±½) iff c + (1−σ) = ½ and c − (1−σ) = −½, i.e.
1 − σ = ½: only at σ = ½. Also (017 §1) c_{e^{ct}F}(u) ≠ e^{±cu}c_F(u), so comb weights are not converted either. ∎

## 2. Dilation matches the Tate points but moves the comb off log ℕ (PROVED)
U_r F(t) := r^{−½}F(t/r) maps P^σ_T onto P^{σ′} with exponents ±(1−σ)/r; choosing r = 2(1−σ) = 1 − 2η gives exponents ±½: U_r(P^σ_T) = P_{rT}.
Under U_r: c_{U_rF}(u) = c_F(u/r), so the comb at lags log n becomes a comb at lags r·log n = log(n^{r}), i.e. at the positions of the Beurling
system ℕ^{r} = {n^{1−2η}} (not log ℕ for η ≠ 0), with weights 2Λ(n)n^{−σ}; the archimedean symbol becomes m_σ(τ·r^{−1})… (Fourier scaling).
Hence: **the deformed problem P(½+η) is conjugate to a ½-type window problem for the dilated, non-integer comb ℕ^{1−2η} with damped weights and a
dilated Γ-symbol — NOT to the original problem for ζ.** It is therefore not a reformulation of D; the route is not closed by conjugacy. The
conjugation exists only for σ < 1 (r > 0) and degenerates at σ → 1 (r → 0: positions collapse, Tate exponents → 0). ∎

## 3. What the interpolating problem has and lacks
(a) Damped weights 2Λ(n)n^{−σ}, absolutely summable tail for σ > 1; mean density 2e^{(1−σ)u} (sub-exponential growth ↓ as σ ↑).
(b) Archimedean value at 0: m_σ(0) = ψ(σ/2) − log π, increasing in σ (ψ increasing) but still negative at σ = 1 (ψ(½) − log π = −γ − 2log 2 − log π < 0).
(c) No known endpoint for the window version: at σ > 1 the window form on P^σ_T equals (1/2π)∫(D_σ − p_σ)|F̂|² (because Σ2Λ(n)n^{−σ}cos(τ log n) =
    −2Re ζ′/ζ(σ+iτ) and D_σ = m_σ + p_σ + 2Re ζ′/ζ), with p_σ = 2Re[1/(σ+iτ) + 1/(σ−1+iτ)] > 0 for σ > 1; D_σ ≥ 0 (Prop H, CITED-known) does NOT
    give P(σ) because of the −p_σ term, which P^σ_T does not annihilate (its lag kernel e^{−σ|u|} + e^{−(σ−1)|u|} is positive definite, so it vanishes
    on no nonzero F). So P(1+ε) is OPEN for the window family. (PROVED as an identity; the endpoint status is OPEN.)
(d) Therefore the cleanest interpolating statement with a KNOWN endpoint is the fixed-profile family of 026:
      P_prof(σ): B^{comb}_σ is positive definite on ℝ.
    Known: P_prof(σ) for σ > 1 (Prop H; CITED-known). P_prof(½) ⟺ D (Theorem S). Continuity: limit lemma (026 §2(iii)): P_prof(σ_j) for a sequence
    σ_j ↓ ½ ⇒ D. Degeneration: the positive density is O(σ − ½) near ½ (026 §3, ARGUED).
    Missing (OPEN): (M) a monotonicity/propagation statement "P_prof(σ) ⇒ P_prof(σ′) for σ′ < σ" proved at the comb level. Warning recorded: any proof of
    (M) through residues of ξ′/ξ (zeros right of σ′) is a zero-location argument, excluded as a mechanism by cor:void (C_zeros); (M) must come from the
    damped comb itself. No such mechanism is known; P_prof is a reformulation-with-a-free-end, not a route.

## 4. Review
- §1 trivial and correct. §2: dilation computation correct (∫r^{−½}F(t/r)e^{±at}dt = r^{½}∫F(s)e^{±ars}ds; set ar = ½ with a = 1 − σ… careful: U_r maps
  P^σ to the class with exponents ±(1−σ)/r when written in the new variable; r = 2(1−σ) gives ±½ — consistent with the text). The conclusion "conjugate to a
  non-integer comb" is exact.
- §3(c): the identity 𝔞^σ = (1/2π)∫(D_σ − p_σ)|F̂|² on P^σ_T for σ > 1 assumes the polar pairing vanishes on P^σ_T — which holds for the comb-mean term
  (by §0) — and that p_σ is the remaining Γ/pole part; the sign claim p_σ > 0 for σ > 1 is correct pointwise. So P(1+ε) does not follow from Prop H. PROVED
  as stated; endpoint OPEN.
- Verdict: not conjugate ⇒ not a reformulation; but the window deformation has no known endpoint and the fixed-profile deformation has no propagation
  mechanism. No sign certified; no negative value of 𝔞_T for ζ.
