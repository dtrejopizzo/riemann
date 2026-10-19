# R167_291 — Audit, phase 167 (Lemma K, R167_101, R167_102, R167_103)

Scope: analytic number theory (Dirichlet polynomials, simultaneous approximation, sieves). No numerics beyond
hand arithmetic. No file other than this one was edited. Labels: PROVED / PROVED-CITED / ARGUED / OPEN / WRONG.

## Summary table

| Item | Statement audited | Verdict |
|---|---|---|
| 1a | Lemma K: Kronecker alignment, complex w, prime powers | PROVED for fixed N with γ free (X-normalisation). Minor fixes K1–K3 |
| 1b | "trivial bound attained at resonant frequencies ≍ √γ_q; (WS*) asks O(log γ_q)" | **WRONG** (scale mismatch, K4) |
| 1c | "the only thing distinguishing γ_q from a resonant γ is being a zero ordinate" | **WRONG as stated**; correct replacement R1 below |
| 2 | Thm B (sieve blindness) of R167_102 | PROVED for \|𝒮\| (two-sided). **Gap** for the one-sided Re form that (WS*) actually needs; repaired (B′) PROVED-CITED. Formulation fix F2 |
| 3 | Thm C ceiling; Cor D(b) "X^δ ≈ 2δL, B/w(0) ≈ 4L" | Thm C PROVED. Cor D(b): X^δ ≈ 2δL PROVED in model; "B/w(0) ≈ 4L" is **only an upper bound for the first term**; with E_K it is B/w(0) ≤ 4c_Θe^{δΔ}L − π C_S(γ)(2T+Δ). Fix F3 |
| 4 | Prop W constant 2.078 | PROVED (= 2·1.03883). "Only zero-free bound is trivial" is overstated (Vinogradov–Korobov gives a subpolynomial saving); threshold changes by o(T). ARGUED→fix F4 |
| 5 | Closing verdict "(WS) zero-free theorem is false uniformly and circular pointwise" | **Half WRONG.** "False uniformly" holds only for the uniformity "Y fixed, γ → ∞". For the uniformity relevant to the witness (Y ≤ γ^{O(1)}) the uniform statement is not false: it is RH-type (true under RH, via Thm A). Replacement R5 |
| S | Theorem S / Cor S′ (R167_103) | PROVED given citations, with one fix: (S4) constant depends on the log-gaps, not only on (A, θ, C_N) |

## 1. Lemma K (R167_190)

**(a) Kronecker and alignment. PROVED.** The numbers {log p}_{p≤N} are ℚ-linearly independent (unique factorisation). By
Kronecker, {(γ log p/2π) mod 1}_{p≤N}, γ ∈ ℝ, is dense in 𝕋^{π(N)}, and the set of good γ is relatively dense, hence unbounded.

- K1 (w is complex). The weight is complex. C1 of R167_101 gives w(−u) = conj w(u), and w = (e^{−iγ_q·}g)*ǩ is not real
  in general. This does not matter: take φ_p := −arg w(log p) (any value where w(log p) = 0). Then every prime term equals
  (log p/√p)|w(log p)|(1+O(ε)) ≥ 0. Hence Re 𝒮(γ) ≥ (1−ε)Σ_{p≤N}(log p/√p)|w(log p)| − E_pp, which is one-sided as (WS*) needs.
- K2 (prime powers). The phases of p^k are kφ_p and cannot be chosen. Bound them trivially:
  E_pp ≤ w(0)·Σ_{k≥2}Σ_{p^k≤N} log p·p^{−k/2} = w(0)(½log N + O(1)), from k = 2 via Mertens; k ≥ 3 contributes O(1).
  The main term is a √N-size quantity, so this is negligible. PROVED.
- K3 (the size is not ‖w‖_∞ X^{1/2}). The main term is ≍ ∫ e^{u/2}|w(u)| du (by PNT), not X^{1/2}‖w‖_∞. By §6.3 of R167_101,
  w vanishes at the outer edge u = 2T+Δ, and nothing bounds |w| from below near u ≈ 2T. The correct statement is
  sup_γ Re 𝒮(γ) ≥ (1−ε)Σ_p (log p/√p)|w(log p)| − O(w(0) log N). This is still "the trivial bound is attained": the triangle
  inequality gives the same quantity as an upper bound. Also, R167_190 writes N = Xe^{2Δ}; after R167_101's correction it is Y = Xe^{Δ}.

**(b) Scale. WRONG as used in the closing paragraph (K4).** Simultaneous approximation of π(N) phases to accuracy ε needs, in
the worst case, γ up to about ε^{−π(N)} (Dirichlet's box principle; Kronecker gives no better uniform bound, and Bohr–Jessen /
Montgomery-type Ω-results for Dirichlet polynomials put the resonant heights at log γ ≳ π(N)·log(1/ε)). So resonant γ satisfy

  log γ_res ≳ N/log N, i.e. Y ≲ (log γ_res)·log log γ_res.

At a resonant height the attained size is ≍ Y^{1/2}w(0) ≲ (log γ_res)^{1/2+o(1)}·w(0). That is **smaller** than 4L·w(0) with
L = log(γ_res/2π). So Lemma K does **not** show that a bound of shape "Re 𝒮(γ) < C·log γ·w(0)", uniform in γ, fails. It shows only
that a bound of shape "≤ C·Y^η·w(0), η < ½, for all γ > H with Y fixed" fails. R167_190 item (b) says "the bound attained at
resonant frequencies is ≍ √γ_q". That conflates two scales. At the witness, Y ≤ (1.57γ_q/2π)e^{Δ} (Det+), so π(Y) ≫ log γ_q.
Kronecker resonance is not available at heights ≍ Y^{O(1)}: the number of free phases exceeds the height budget.

**(c) The direction of (WS*). CONFIRMED.** From Thm A, Lemma Q and Thm B of R167_101,
4Re 𝒮 = (L/π I − O_K) + 4c_Θ|G(t_q)|²|k(−iδ)| − R_K + small. So the witness makes Re 𝒮 **large and positive**, and the exclusion
needs the upper bound Re 𝒮 < B. A resonant γ (in the regime log γ ≫ Y) makes Re 𝒮 large and positive in the same way. To a
one-sided upper-bound test it "looks like" a zero. That reading is correct.

**R1 (replacement for "only a zero distinguishes γ_q from a resonant γ").** Two things distinguish them.
1. The scale relation log γ_q ≍ log Y (Det+). Resonance needs log γ ≳ Y/log Y.
2. In the polynomial range γ ≤ Y^{A}, large values of the smooth sum 𝒮(γ) are governed exactly by zeros. By Thm A,
   Re 𝒮(γ) − (arch − on-line) = −(off-line zero contribution near γ). Under RH this gives Re 𝒮(γ) ≤ E_K/4 + small for **every**
   γ in the range, with no resonance possible.

The circularity conclusion survives, but its source is the explicit formula (Thm C of R167_102, Thm 2 of R166_802), not Lemma K.
**Label of Lemma K:** PROVED in the form "for fixed N, sup over γ ∈ ℝ attains the triangle-inequality bound, one-sided". Its
corollary "(WS) false uniformly in γ" holds only in the Y-fixed uniformity, which is irrelevant to the witness.

## 2. Thm B of R167_102 (b_θ)

- **Expansion. PROVED.** In 𝒮[b_θ] = ½𝒮[Λ] + ¼e^{−iθ}A + ¼e^{iθ}B, the e^{−i(...)} half of the cosine cancels n^{iγ}e^{iφ_n},
  which gives A = ΣΛn^{−1/2}|W| ≥ 0. The mean of |e^{−iθ}A + e^{iθ}B|² over θ is A² + |B|² ≥ A², so some θ has
  |f(θ) − f(θ+π)| ≥ A/2. Hence max(|f(θ)|, |f(θ+π)|) ≥ A/4. The memo's A/8 is conservative. 0 ≤ b_θ ≤ Λ is correct.
- **Gap (one-sided).** (WS*) is the one-sided bound Re 𝒮 < B. Here Re f(θ) − Re f(θ+π) = ½Re((A + B̄)e^{−iθ}), whose amplitude is
  |A + B̄|. That vanishes if B = −A, which is the case where ψ_n := γ log n + φ_n concentrates near π/2 mod π. So Thm B as written
  does not show that the class cannot prove the one-sided (WS*). sup_{0≤b≤Λ} Re 𝒮[b] = P := ΣΛn^{−1/2}|W|(cos ψ_n)_+, and P is
  large only if ψ_n is not concentrated.
- **Repair (B′). PROVED-CITED.** P ≥ ½(ΣΛn^{−1/2}|W||cos ψ_n| + Re 𝒮[Λ]). Also
  Σ|W||cos ψ| ≥ Σ|W|²cos²ψ/w(0) = (2w(0))^{−1}[ΣΛn^{−1/2}|W|² + Re ΣΛn^{−1/2}W(log n − u₀)²n^{2iγ}].
  The last sum is a smooth-weight (W ∈ C^∞, §6.4 of R167_101) twisted sum at height 2γ ≤ Y^{O(1)}. By the Vinogradov–Korobov
  zero-free region (unconditional) it is o(X^{1/2}·mass), so P ≥ (¼ − o(1))·(ΣΛn^{−1/2}|W|²/w(0)) + ½Re 𝒮[Λ]. When Re 𝒮[Λ] ≥ 0
  (the only case in which (WS*) is in question), P ≫ X^{1/2}·(mass). So the one-sided blindness holds. The inputs are a
  **zero-free region**, not zeros; that is legitimate.
- **F2 (formulation).** "obeys every upper bound Λ obeys" is too broad. It is true for inequalities of the monotone form
  Σ b φ ≤ U_φ with φ ≥ 0. It is also true for the large-sieve inequality, which holds for every sequence. It is false for:
  - two-sided statements, such as Bombieri–Vinogradov or PNT in progressions; their lower halves fail for b_θ;
  - upper bounds whose proof goes through an identity, such as Vaughan-type |ΣΛ(n)e(αn)| bounds, or bounds on twisted sums
    ΣΛ(n)n^{it} derived from Λ = μ*log.

  R167_102 §4 (iii) lists "Bombieri–Vinogradov-type upper bounds". It should read "upper-bound halves of B–V with φ ≥ 0".
  Correct statement: **every conclusion derivable from {b ≥ 0, supp b ⊂ prime powers, Σbφ ≤ U_φ (φ ≥ 0)} holds for b_θ.**
  The memo's moral "identities are the only way below ½" is then accurate as a statement about this class. As a statement about
  all methods it remains ARGUED (Thm D).

## 3. Thm C and Cor D (R167_101)

- **Thm C. PROVED.** Φ ≥ 0 on ℝ, entire of type 2T+Δ, and integrable, so it is in the Cartwright class. We have
  log|Φ(iy)| ≤ (2T+Δ)|y| + P_{|y|}*log Φ, and Jensen (∫P = 1) gives ≤ (2T+Δ)|y| + log(P_{|y|}*Φ). Since P_δ ≤ 1/(πδ), this gives
  |Φ(−iδ)| ≤ Y^δ I/(πδ) = 2Y^δ w(0)/δ, with Y^δ = X^δe^{δΔ}. Arithmetic correct.
- **Cor D(b), lattice model.** The contact equation sinh(2δT)/(2δ) − T = L/2 gives e^{2δT} ≈ 2δL + 4δT, so T ≈ log(2δL)/(2δ)
  and 4δT = O(log y) ≪ 2δL for large y = δL. Hence X^δ ≈ 2δL(1+o(1)). PROVED in the model. Caveat: if one instead takes T ≈ L/2,
  one gets 4δL; that is not the large-y regime.
- **"B/w(0) ≈ 4L": WRONG as an evaluation, correct as an upper bound on the first term.** Thm C gives
  B ≤ (2c_Θ/δ)X^δe^{δΔ}w(0) − E_K/4 ≈ 4c_Θe^{δΔ}L·w(0) − E_K/4. With E_K/4 ≥ ½C_S(2T+Δ)‖G‖²_∞‖k‖₁ ≥ πC_S(γ)(2T+Δ)w(0) and
  C_S ≈ 0.112L:

  **B/w(0) ≤ L·[4c_Θe^{δΔ} − 0.35(2T+Δ)]**, so B > 0 forces 2T+Δ ≲ 11.4·c_Θe^{δΔ}.

  This is Prop E made concrete, and it makes B marginal. Also, in the large-y regime X = (2δL)^{1/δ} is **polylogarithmic** in
  γ_q, not ≍ γ_q. So the "trivial size" there is X^{1/2} = (2δL)^{1/(2δ)}, not √γ_q. The required saving is from
  L^{1/(2δ)} to L, a polylog-power saving. "RH quality" is still a fair description (it is a bound at one scale, at the level of
  the explicit-formula error), but the closing paragraph's "√γ_q vs O(log γ_q)" holds only in the small-y regime
  (T_c ≈ T_L), where Prop E fails and B < 0 anyway.
- **F3:** restate Cor D(b) as "B/w(0) ≤ 4c_Θe^{δΔ}L − πC_S(γ)(2T+Δ); trivial size (2δL)^{1/(2δ)}·e^{Δ/2}·2.078".

## 4. Prop W

**2.078. PROVED.** By partial summation, Σ_{n<X}Λ(n)n^{−1/2} = ψ(X)X^{−1/2} + ½∫_1^Xψ(t)t^{−3/2}dt ≤ 1.03883(1 + 1)X^{1/2}
= 2.0777X^{1/2}. Here ψ(x) < 1.03883x holds for all x > 0 (Rosser–Schoenfeld). By PNT the true constant is 2 + o(1). The
threshold algebra (2/δ)Y^δ > 2.078X^{1/2} ⟺ Δ > [(1−2δ)T + log(1.039δ)]/δ checks.

**F4.** "Its only zero-free bound is trivial" contradicts R167_102 Thm D. Vinogradov–Korobov saves exp(−c(log X)^{3/5−ε}) on the
twisted window sum at height γ ≤ X^{O(1)}. The threshold changes only by o(T)/δ, so the conclusion stands. The sentence should read
"no zero-free bound saves a power".

## 5. Closing verdict of phase 167

"(WS) as a zero-free theorem is false in its uniform form and circular in its pointwise form."

- "false uniformly": **WRONG as stated** (§1b). It is true only for the uniformity "Y fixed, γ → ∞" (Lemma K). That
  uniformity has nothing to do with the witness. For the uniformity "γ ≤ Y^{A}, all γ" (the one the witness lives in), the uniform
  bound Re 𝒮(γ) < B(γ) is not refuted. By Thm A it follows from the absence of off-line zeros, so it is **RH-type: true under RH**,
  and its uniform-in-scale version is equivalent to a zero-free statement by Landau (R167_102 Thm C).
- "circular pointwise": CONFIRMED (Thm C, Thm E, R166_802 Thm 2). This is the operative obstruction.
- "class obstruction": CONFIRMED with fixes. Thm B (with B′ for the one-sided form) and Theorem S/Cor S′ (DMV/Zhang) show that
  monotone sieve inputs and θ ≥ ½ class tools cannot reach η < ½.

**R5 (replacement verdict).** (WS*) is not refuted. It is (i) out of reach of the monotone/sieve class (Thm B + B′, Cor S′,
PROVED / PROVED-CITED), (ii) equivalent in its scale-uniform form to a zero-free statement (Landau, PROVED), and (iii) at one scale,
an evaluation of pole − zero sum (Thm E). Lemma K should be demoted from evidence for (ii) to a remark: "large values attained
only at heights log γ ≳ Y/log Y".

## 6. Theorem S (R167_103)

The Selberg (S1) and B–T (S2) transfers are routine and correct (the remainder 2C_N((x+y)/d)^θ; D² x^θ ≤ y x^{−ε}).
- **Fix:** (S4) carries 3π/δ_ν with δ_ν the log-gap in 𝒩. Its constant is **not** a function of (A, θ, C_N) alone, contrary to
  the status-table row 4. Either drop (S4) from the "constants depend only on (A, θ, C_N)" clause, or add a gap axiom.
- Cor S′ (DMV/Zhang zeros near σ = 1 ⇒ twisted exponent ½ by Landau) is correct given the citations, which are flagged
  secondary. It applies only to proofs whose inputs hold with θ ≥ ½; it says nothing about proofs using N(x) = ⌊x⌋ (§5 of that
  memo correctly notes this).

## Ledger of fixes
K1–K3 (Lemma K precision), K4/R1 (scale: Lemma K irrelevant at the witness), B′ + F2 (one-sided blindness; formulation),
F3 (Cor D(b) with E_K; polylog X), F4 (Prop W wording), R5 (closing verdict), S4 constant.
No label of record moves. (WS*) remains OPEN.
