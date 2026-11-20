# Round 16, memo A — Curvature (Γ₂, Bakry–Émery, Lichnerowicz) as source of the sign

Notation of the common brief: a_T(F) = Arch(F) − Σ_n v_n c_F(log n) on P_T, v_n = 2Λ(n)/√n. Controls: cΛ with c = 2,
deletion of one prime power, Beurling-type weight. m(τ) = C_0 + ∫_0^∞(1 − cos τu)K(u)du is the symbol of Arch.

## 0. Cross-check (read in primary sources)

Search in 03-research, the index and the grid for «Bakry», «Γ₂», «Gamma_2», «carré du champ», «curvature», «Lichnerowicz»,
«Ollivier», «Erbar», «Beurling–Deny», «Dirichlet form», «log-Sobolev». Deciding matches:

- **Phase 64, `CURVATURE-computation.md`** §§2–5: exact Γ₂ of the prime jump generator, kernel B^{∘2} with
  B(ξ,η) = ½[ψ(ξ)+ψ(η)−ψ(ξ−η)]; Theorem 2: CD(0,∞) by Schur product if the weights are ≥ 0; §4: CD(0,∞) is
  marginal (ψ(0) = 0, no gap); §5: «the archimedean factor supplies the curvature» (sum of curvatures). Index
  04 (G2D-R160_S2 §3.1): DEAD [F3: any non-negative weight].
- **Phase 195, `INV_N_001_BAKRY_EMERY_GAMMA2_GAP_CEILING_NO_GO.md`** §§1–3: exactly the decomposition of the
  assignment, a_T = E_T + ∫W_T F² with E_T the Dirichlet form of the censored jump process (archimedean kernel ν
  plus atoms ½v_n at ±log n) and potential W_T; exact formula for Γ₂, **quadratic in J**, with mixed
  archimedean–prime and prime–prime terms (the compositions of jumps log p, log q that the assignment proposes as a channel
  for products and quotients already appear there). Theorem 3.3 (gap ceiling): every curvature/Poincaré
  transfer gives ≤ g_T + ess inf W_T < 0 at T = ½log 3, where positivity is proved. Index README:
  «do not retry Γ₂/CD/log-Sobolev/Poincaré of the jump part without an input coupling E_T and W_T».
- **Phase 160, `R160_M10_R1.md`**: Doob generator of the form, T3 (Γ₂ form of the statement:
  ‖L r‖² ≥ ½E(r), i.e. integrated Bakry–Émery), T4 (pointwise curvature ceiling ρ ≤ ¼), P1 (gauge); lines
  63 and 79: with a signed measure ν «E is not a Dirichlet form and the Markov argument does not apply».
- `RULES_AVOID.md` W4 (Lemma T, Lemma K), X2, Y3; `ROUND_012_A` Prop. B (Lyapunov format); `ROUND_013_C` O6
  (Mourre/virial = Lyapunov); `ROUND_015_C` (Lemma A: affinity in c; Prékopa Prop. B). Commutator [X, S_N] = −K_N
  of R161_001: family R161_057–065 (X3, J5).

**Conclusion of the cross-check.** Γ₂ of the jump part with positive rates, its quadratic character in the weight, the
mixed terms between primes and the Bakry–Émery ⇒ Poincaré transfer are **repetition** (phase 64, INV_N_001,
R160_M10_R1). The only thing not literally recorded is the variant **with negative prime rates** (signed
generator, not Markov), which R160_M10_R1 only flags as outside its argument. I examine that variant with the gate and
close it with a class lemma (§2). Ollivier and Erbar–Maas are treated in §3.

## 1. Four-point gate (signed variant)

1. Antecedent: INV_N_001 §§1–3; R160_M10_R1 T3–T4.
2. New statement: write a_T = E^{(L)}(F) := ⟨−LF, F⟩ with L = L_∞ − L_arith (negative prime rates) and use
   Bochner–Lichnerowicz (integrated or pointwise) for L.
3. Why it would avoid the ceiling: INV_N_001 separates E_T ≥ K·Var and W_T; with sign in the rates, potential and jumps
   would be coupled inside a single generator.
4. Global inequality: Γ₂^L ≥ κΓ^L (+ N^{−1}(Lf)²) ⟹ «gap» ⟹ a_T ≥ 0 for all T.

Point 4 fails by Lemma L (below): Lichnerowicz produces no sign without Γ ≥ 0. **It does not pass the gate.**

## 2. Class lemma

**Lemma L (Lichnerowicz is blind to the sign; PROVED).** Let L be symmetric on L²(I) (or on P_T with the L² metric), with
domain D, and let Γ, Γ₂ be arbitrary pointwise forms with ∫Γ(f) = ⟨−Lf,f⟩ =: E(f) and ∫Γ₂(f) = ‖Lf‖² (integration
identities valid for every symmetric jump generator with L1 = 0, with or without sign in the rates). If
Γ₂ ≥ κΓ + N^{−1}(Lf)² pointwise (or only integrated), with κ > 0, N ∈ (1,∞], then for each eigenvector
−Lf = λf one obtains λ(λ(1 − 1/N) − κ) ≥ 0, i.e.
  spec(−L) ∩ (0, κN/(N−1)) = ∅,
and nothing more: the condition is compatible with arbitrary eigenvalues λ ≤ 0.
*Proof.* Integrate: λ²‖f‖² ≥ κλ‖f‖² + λ²‖f‖²/N. Conversely, if spec(−L) ∩ (0,κN/(N−1)) = ∅, the integrated
inequality ‖Lf‖²(1 − 1/N) ≥ κE(f) holds by spectral calculus (each component with λ ≤ 0 contributes ≥ 0 on the
left and ≤ 0 on the right). ∎

**Corollary L′ (PROVED).** In the Markov case the sign of λ comes from pointwise Γ ≥ 0 (rates ≥ 0), not from Γ₂; with
signed rates, «E(f) ≥ 0» is the statement itself (J3). All the sign information of a Bochner–Lichnerowicz chain
resides in Γ ≥ 0, and pointwise Γ ≥ 0 requires rates ≥ 0, which is blind by Lemma K (holds for every weight ≥ 0).
**Controls.** At c = 2 (form with negative directions), under deletion and under Beurling, the integrated version of
CD(κ,N) holds whenever the spectrum of −L_c avoids (0, κN/(N−1)): the «curvature inequality» does not break in the
controls by structure but only by spectral accident; by Lemma T of round 13 a certificate using
only CD plus signed Γ₂ proves the false statement. (An explicit reason for the remainder ceasing to be ≥ 0 does not exist: there is no
remainder that ceases to be so; the false statement E ≥ 0 is inferred only if Γ ≥ 0 is added, which also fails at c = 2.)

**Answer to (1), reverse reconstruction (PROVED).** (a) Arch is not the Γ₂ side of any generator: ∫Γ₂ = ‖L′F‖² ≥ 0
while m(0) = C_0 < 0 and Arch has negative directions on P_T above the archimedean threshold. (b) What is
a square is Arch − C_0‖F‖² on ℝ: m − C_0 = ψ_∞ is negative definite (Lévy–Khintchine with K > 0), and so is √ψ_∞
(Bochner subordination, CITED), so that Arch − C_0‖·‖² = ‖L′F‖² with L′ of positive rates and symbol √ψ_∞
(in the window, plus boundary terms). Then a_T ≥ 0 reads ‖L′F‖² ≥ |C_0|‖F‖² + Prime(F) + boundary: Γ₂ of **one**
generator against Γ of **another**. No Bakry–Émery theorem compares Γ₂^{L′} with Γ^{L_arith} of a different
generator; it is a comparison of two forms, each blind, i.e. the statement (J3). (c) The
Tate–Beckner identity X + 𝓕X𝓕 = m(D) does not give m = ℓ² by (a).

**Answer to (2) (PROVED).** With L_c = L_∞ − cL_pr, ∫Γ₂^{L_c} = ‖L_∞F‖² − 2c⟨L_∞F, L_prF⟩ + c²‖L_prF‖², quadratic in c
with prime–prime coupling at the delays log(pq), log(p/q) (as in INV_N_001 §2). But the statement is affine in c
(E^{(c)}), and the only named inequality, CD(κ,N), is equivalent by Lemma L to a spectral gap around 0,
which does not distinguish c = 1 from c = 2, nor deletion, nor Beurling. Pointwise, Γ₂ ≥ 0 on ℝ ⟸ B_c ⪰ 0 (Schur) ⟺ ψ_c
negative definite ⟺ rates ≥ 0 (Schoenberg, CITED); with c > 0 in negative rates B_c is not ⪰ 0 and there is no substitute.

**Answer to (3) (ARGUED).** Γ is bilinear in functions for a fixed L; [X, S_N] is a derivation on
operators. They coincide formally only if X is the derivation associated with a diffusion L (Γ(f,g) = (Xf)(Xg)); the
resulting format is that of the commutator of R161_057–065 (X3, J5) and the Lyapunov of ROUND_012_A Prop. B.
Λ∗1 = log enters no step of the Γ-calculus (it acts on products L·S_N, W3).

## 3. Other curvatures

- **Ollivier (W1-contraction) and Erbar–Maas/Mielke (entropic curvature):** defined for Markov semigroups
  (transition kernel ≥ 0, reversible measure). With signed rates e^{tL} is not Markov; a contraction in a
  norm, ‖e^{tL}‖ ≤ e^{−κt}, is equivalent to numerical range of L ≤ −κ, which is the statement (J3). With rates ≥ 0 they are
  blind (Lemma K). PROVED in that dichotomy; the «contraction between scales» of ROUND_009_G3 still has no object.
- **Discrete Bochner / curvature on graphs (Lin–Yau, Schmuckenschläger):** same dichotomy, Lemma L.

## 4. Verdict and labels

| # | Statement | Label |
|---|---|---|
| 1 | Γ₂/CD of jumps with rates ≥ 0, mixed terms between primes, transfer to Poincaré | repetition (phase 64; INV_N_001; R160_M10_R1) |
| 2 | Lemma L: integrated CD(κ,N) ⟺ spec(−L) ∩ (0,κN/(N−1)) = ∅; blind to the sign | PROVED |
| 3 | Cor. L′: the Bochner–Lichnerowicz sign comes only from Γ ≥ 0 (rates ≥ 0: blind; signed: J3) | PROVED |
| 4 | Arch is not a Γ₂ side (C_0 < 0); Arch − C_0‖·‖² = ‖L′F‖² on ℝ with symbol √ψ_∞ | PROVED mod. CITED (subordination) |
| 5 | Comparing Γ₂^{L′} with Γ^{arith} is the statement | PROVED (J3) |
| 6 | Ollivier/Erbar–Maas: Markov ⇒ blind; non-Markov ⇒ numerical range = statement | PROVED in the dichotomy |
| 7 | [X,S_N] as carré du champ: format R161_057–065 | ARGUED |
| 8 | Signed curvature as source of the sign | NO-GO in the Bochner–Lichnerowicz class (Lemma L) |

For independent checking: rederive Lemma L (including the spectral converse) and the claim that the identities
∫Γ = E, ∫Γ₂ = ‖Lf‖² hold for signed rates (they use only symmetry and L1 = 0); and the computation of (2).

**Next explicit operation (OPEN).** Lemma L shows that the only sign input in any Γ-type
computation is a first-order pointwise positivity. What lies outside the class is a pointwise form Γ̃(F)(x) ≥ 0
**not** associated with rates ≥ 0, with ∫Γ̃ = a_T + (blind term ≥ 0), whose pointwise positivity at each x is a
finite inequality between the v_n at delay x that uses an exact additive relation and fails in the three controls.
I have no such Γ̃; if one is proposed, it must first be cross-checked against ROUND_015_C Cor. B′ (pointwise signed split, class O/O3).
