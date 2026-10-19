# L2_BUILD_028 — Integer-lattice test matrices for Theorem S; structure, (non-)diagonalization by multiplicativity, and the next-order
# balance at the ceiling r = 1

## Corpus check
phase-159 G2_B1_R5 Theorem D (test vectors b_m = m^{−½}, resolution ε = 1/(8M), G_M ≤ log 8M + C_χ ⇒ r ≤ 1) and Cor D1; 021 §4 (ceiling × threshold);
024/025 (Theorem S, B_{F₀}); R186_001 (Gram of translates in {log n}: NO-GO for Gram alone); R160_M12 (×p orbits); Bohr's correspondence (CITED).
grep "Redheffer / Dirichlet convolution operator / Bohr / ℚ_{>0} / multiplicative test vector / next-order Theorem D": none in the row-D record
beyond Theorem D itself. New: §1–§4.

## 1. The integer-lattice family is equivalent to Theorem S's condition (PROVED)
For the fixed profile F₀ of 025 and M ≥ 2, A_M := [B_{F₀}(log m − log k)]_{m,k≤M}. Then: D ⟺ A_M ⪰ 0 for all M.
(⟹) Theorem S. (⟸) B_{F₀} is continuous and depends only on differences. Given a finite configuration a_1,…,a_K and c > 0, let m_j := ⌊e^{c + a_j}⌋;
then |log m_j − c − a_j| ≤ e^{−c−a_j}·2 → 0 as c → ∞, so (log m_j − log m_l) → (a_j − a_l) and Σs_js_lB(a_j − a_l) = lim Σs_js_lB(log m_j − log m_l) ≥ 0.
(m_j distinct for c large.) Hence B_{F₀} is PD, and Theorem S gives D. ∎
So {A_M} is a natural, arithmetic, finite family of tests that is exactly as strong as D.

## 2. Structure of A_M (PROVED)
Quadratic form: s^TA_Ms = 𝔞(Σ_m s_mτ_{log m}F₀) = archimedean part + prime part, with
  prime part = −Σ_{n≥2} v_n Σ_{m,k≤M} s_ms_k c₀(log m − log k − log n)  (c₀ even).
(a) Exact coincidences m = kn give c₀(0) = 1: the "divisor part" −Σ_{k|m} s_ms_k v_{m/k} = −⟨s, (v·)*s⟩ — a Dirichlet-convolution (Redheffer-type) operator
    with kernel v_n = 2Λ(n)n^{−½}.
(b) Near-coincidences 0 < |log(m/(kn))| ≤ 2T₀ also contribute (c₀ ≢ 0 there); for m, k ≤ M and n < M² … they are unavoidable once 1/M < 2T₀, i.e. for
    every large M (gaps between log m shrink like 1/m). So A_M = Arch_M − Div_M − Near_M.
(c) Multiplicativity diagonalizes the divisor part only: on ℓ²(ℚ_{>0}) the shifts U_p (by log p) are commuting unitaries, Div = Σ_p f_p(U_p),
    f_p(z) = Σ_k log p·p^{−k/2}(z^k + z^{−k}), jointly diagonal under the characters of ℚ_{>0} (Bohr torus 𝕋^∞, one angle per prime): symbol
    Σ_p Σ_k 2 log p p^{−k/2}cos(kθ_p) = −2Re Σ_p (Euler-factor log-derivative at ½ with independent phases).
**NO-GO (PROVED): multiplicativity does not diagonalize A_M.** The archimedean part is the convolution by a(log r), a function of the REAL lag log r
(continuous, not a character combination), and on ℓ²(ℚ_{>0}) it is not even bounded (infinitely many rationals r with |log r| < 2T₀ and
a(log r) ≈ a(0) > 0); the near-coincidence part likewise couples ratios m/(kn) close to 1. Only the one-parameter subgroup θ_p = τ log p (Bohr diagonal)
sees both, and on it the form is the analytic pairing (1/2π)∫σ_∞F̂₀²|Σ_m s_m m^{iτ}|² — i.e. Theorem S again. Dirichlet characters χ do not help:
s ↦ χ·s preserves Div (χ(m)conj χ(k) = χ(n) when m = kn, |χ| = 1 on supports coprime to q… only up to the non-coprime part) but not Arch_M.

## 3. Next-order balance at the ceiling r = 1 (computation; Mertens CITED, archimedean asymptotic ARGUED)
Theorem D's test: translates of a profile χ_ε of width ε = θ/M (θ ≤ 1, so no overlaps), b_m = m^{−½}, m ≤ M. Then near-coincidences vanish and
  Q(M) = H(M)·a_ε − Σ_{n≤M}2Λ(n)n^{−1}H(M/n),   H(y) = Σ_{k≤y}1/k = log y + γ + O(1/y),   a_ε := 𝔞_∞(χ_ε) = log(1/ε) + C_χ + o(1)
(ARGUED: m(τ) = log(|τ|/2π) + O(1/|τ|) and scaling; C_χ = (1/2π)∫log(|σ|/2π)|χ̂(σ)|²dσ for the unit-width normalized profile).
Mertens (CITED): Σ_{n≤x}Λ(n)/n = log x − γ + o(1), hence Σ_{n≤x}Λ(n)log n/n = ½log²x + o(log x) (partial summation).
Comb: 2Σ_{n≤M}(Λ(n)/n)(log M − log n + γ) + O(1) = 2[(log M + γ)(log M − γ) − ½log²M] + o(log M) = log²M + o(log M).
Arch: (log M + γ)(log M − log θ + C_χ) = log²M + (γ + C_χ − log θ)log M + O(1).
  **Q(M) = (γ + C_χ + log(1/θ))·log M + o(log M).**
Leading orders cancel exactly (r = 1, the ceiling). The next-order coefficient γ + C_χ + log(1/θ) depends on the resolution θ = εM: it is positive for
θ < e^{γ + C_χ}, and can be made arbitrarily large by refining the profile (θ ↓ 0). So at the ceiling the integer test is satisfied by Λ at next order
for a cheap reason (resolution buys archimedean energy log(1/θ)); **it yields no certificate** — consistent with 018/019 (resolution vs density) and with
the exact criticality pattern (010, N_013, 026): the arithmetic content does not appear at order log M in this family.
(For comparison, a comb with r < 1 has Q ≈ (1 − r)log²M > 0 at leading order; r > 1 fails — Theorem D.)

## 4. Review
- §1: approximation of arbitrary configurations by log-integers is elementary (m_j = ⌊e^{c+a_j}⌋); continuity of B (024 §1) needed — yes. PROVED.
- §2(c): Bohr diagonalization of the divisor part is standard (CITED); the unboundedness of the archimedean convolution on ℓ²(ℚ_{>0}) is clear (a(0) > 0
  and infinitely many r near 1). The NO-GO concerns "multiplicativity diagonalizes A_M", correctly scoped.
- §3: the log²M cancellation uses only Mertens (CITED); the o(log M) remainder from Σ_{n≤x}Λ(n)/n − log x + γ = o(1) is fine for the log M coefficient. The
  archimedean asymptotic is ARGUED (not written to O(1)). The conclusion "no certificate" is about this test family only.
- No sign certified; no negative value of 𝔞_T for ζ.
