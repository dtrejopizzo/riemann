# SHAPE_THEOREM — What any proof of row D must be: one statement, the proved barriers as its lemmas (reviewed and corrected the same day, see §0 and SHAPE_THEOREM_REVIEW.md)

Pen and paper. Row D (λ_A(T) ≥ 0 on P_T for every T > 0, declared carrier, Paper 46 eq:target). Labels:
PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO. "P46" = 04-papers/46-row-d-dual-certificates/main.tex;
"188/" = phase-188-closing-D; "189/" = phase-189-new-theory; "186/" = phase-186-toolbox; index = 05-meta-and-planning/ROUTES-TRIED-INDEX.

Corpus check : index README, 04_ Part I-a/b/c, 06_ barrier key; P46 sec:barriers, sec:negative,
sec:Z, sec:combs, sec:wh; 188/ L2_BUILD_010/011/019/026/031, N_BUILD_003/013/018/021; 189/ NT_011, NT_014, NT_011_014_REVIEW;
186/ R186_036, R186_051; P47 §18 (T1, T2); crossword §3.2 (α)–(θ); phase-190 EXP_003/004/005. Nothing below is a new route; it
is the record's barriers organized as the lemmas of one theorem. **No sign is certified here and no negative value of 𝔞_T for ζ.**

---

## 0. ERRATUM (independent review; see SHAPE_THEOREM_REVIEW.md)
The following corrections supersede the text below where they conflict.
1. **Theorem S restated in three tiers.** Part (A) (transfer) holds only for the operations whose falsifier is PROVED: O1, O2, O3,
   O4 (c large; c → 0), O7, O8a, O8b, O12, O13, O15, and the derived classes 𝒞_PNT, 𝒞_zeros, 𝒞_prog, 𝒞_BT (A15, A17). Tier (A′):
   O4ε and O5 CONDITIONAL (κ_T ≠ 0; c_{F*}(log n₀) ≠ 0); O9 CITED (complete form) / ARGUED (primitive bottom); O6 and O8c ARGUED
   (no window witness in the record); O10 OPEN. O11 and O14 are **not** transfer instances (no member with negative bottom): the
   antisymmetry B3 and the margin lemmas of the former A13 belong to part (B). Part (C) reads: "a property destroyed by each operation
   of tier (A); and, with the stated labels, by those of tier (A′)".
2. **A1.** T₀(0) = 0.74921 (P46 prop:arch); "≈ 0.8047" was ½log5, the smallest ½log N for N ≥ 5.
3. **A5.** When s = −1 the admissible range is ε ≤ Λ(n₀) (a ≥ 0); a contact with Λ(n₀) = 0 admits only s = +1, 𝒞_BT only s = −1.
4. **A6 → ARGUED.** R167_103 row 7: the DMV/Zhang systems have no Γ_ℝ functional equation and no window form W_T in the record's sense;
   the transfer to a negative window bottom is ARGUED (a Beurling Weil form would be needed). Consequently the "not ℤ-integral" branch of
   Lemma I and the ℤ-integrality third of Corollary (b) are ARGUED.
5. **A11.** thm:famblind also requires the weight class to be closed under one-term amplification (thm:famFE: the FE class). Bilateral
   laws remain NOT excluded (unchanged).
6. **A13 (O14) → structural.** lem:wh-T / lem:wh-Tprime / thm:wh-detinherit(iii) modify the form to bottom 0, not < 0; they are precision
   constraints (margin ≤ Lkλ_A/c_P, ≤ Lλ_A; ε₀ ≥ 1 never decides), now Lemma B9.
7. **A9.** The comb of Ξ_Q has weights of both signs (no Euler product): Ξ_Q is a form object, not a member of 𝔚. P47 Thm 18.16 concerns the
   Hodge-index inequality (18.2), a different form; it is cited only for the falsifier and the axiom list.
8. **B2d.** thm:kappa gives κ_* ≥ ¼|C₀| = 1.3430 (lower bound; κ_* ≤ |C₀|(¼ + τ₀²)); "κ* = 1.343…" is corrected. The reading "deficit paid
   by the fluctuation" is ARGUED; the inequalities are PROVED.
9. **B2c.** "no fixed band can be discarded" depends on B2b (CONDITIONAL).
10. **Lemma I.** Rows 13 and 21 keep the functional equation (M_m = ξ·polynomial, f_t self-dual); what they break is the Euler product
    over ℕ (M_m: polynomial factor; f_t: frequencies m/√M ∉ ℕ). They belong to the second branch; conclusion (b) stands as a finite case
    analysis over the 23 listed properties, PROVED relative to the table modulo CITED (Epstein) and ARGUED (Beurling).
11. **Corollary (c).** −c_{F*}(log n) is a supergradient of the concave μ_T (lem:degen); the one-sided directional derivative is the
    minimum over minimizers. "First variation" is correct only when the minimizer is unique.
12. **Corollary (e)10.** The A3/A7–A9 requirement of Paper 47 (Thm 12.4, Thm 18.16, Ξ_a) concerns the Hodge-index inequality (18.2), not
    λ_A(T); no Ξ_a-type window-form falsifier exists in the record. For the window form the record supports only: (i) A1–A6 alone do not
    suffice (Ξ_Q, complete form, CITED); (ii) the transfer principle of A10. Item 10 is restated as: "uses a property beyond A1–A6, and is
    uniform over fields only if it names the property separating ζ from every ξ_K".
13. **A8b** is confirmed PROVED (prop:ftprim, independently re-derived in SECONDARY_ITEMS.md review item 4);
    L2_BUILD_011 row 13 is stale (erratum note added there).
14. **B8.** R186_018 and R186_028 are cited as index W1 entries, not re-verified; omitted from the Paper 46 version.

---

## 1. Definitions

### 1.1 Objects
- **Combs.** 𝔚 := {a : ℕ_{≥2} → ℝ_{≥0}} (finite on every window). Weights v_n(a) := 2a(n)/√n; v_n := v_n(Λ). Contacts
  𝒩_T := {n ≥ 2 : log n < 2T}; mass 𝖠_T(a) := Σ_{n∈𝒩_T} v_n(a).
- **Window form of a comb** (P46 eq:symbol, eq:form, subsec:finite). σ_T^{(a)}(τ) := m(τ) − Σ_{n∈𝒩_T} v_n(a) cos(τ log n),
  m(τ) = Re ψ(¼ + iτ/2) − log π; 𝔞_T^{(a)}(F) := (1/2π)∫ σ_T^{(a)} |F̂|² on 𝒟_T ⊂ L²(I_T);
  P_T := {A(F) = B(F) = 0} (Tate moments A(F) = ∫F e^{t/2}, B(F) = ∫F e^{−t/2});
  λ_A(T; a) := inf{𝔞_T^{(a)}(F) : F ∈ P_T ∩ 𝒟_T, ‖F‖ = 1}; WP_T(a) :⟺ λ_A(T; a) ≥ 0. λ_A(T) := λ_A(T; Λ).
  **Row D** :⟺ WP_T(Λ) for every T > 0. (Equivalently lim_{T→∞} λ_A(T) ≥ 0, lem:monoT; and equivalently λ_A(T) ≥ −ε(T) ∀T for
  some ε → 0, thm:wit-Tc(iv). These are internal restatements of D; they are not used as anything else.)
- **Form objects.** The zero-side falsifiers are not combs but closed semibounded forms on the same spaces P_T:
  the quartet models 𝔞_T^{z,k} = 𝔞_T + kQ_z (P46 def:quartetmodel, lem:quartet; "M_m"), the self-dual deformations f_t = ζ + t g
  (P46 lem:selfdual, prop:ft, prop:ftprim), the FE-preserving twists ζ̃ = ζ·R (189/NT_011), Epstein Ξ_Q and Davenport–Heilbronn
  series (P47 §18.2, P46 rem:twohalves), Dedekind ξ_K (P47 §18.1), Beurling systems (R167_103, R184_005, R163_803).
  A **form object** is a family q = (q_T)_{T>0} of closed semibounded forms, q_T on P_T (or on a closed subspace of L²(I_T)), with
  bottoms λ(T; q). The comb objects are q_T = 𝔞_T^{(a)}|_{P_T}; q₀ := (𝔞_T|_{P_T})_T is the object of ζ.

### 1.2 Operations 𝒪 (each maps a form object to a form object)
| op | name | action | keeps |
|---|---|---|---|
| O1 | finite deletion | a ↦ a·1_{n≥N} | a ≥ 0, every PNT error term with inf ε > 0, every zero-free region/zero-density statement (ζ_a = ζ·E, E entire zero-free), a ≤ Λ |
| O2 | one-term amplification | a ↦ a + c·1_{n=n₀} | a ≥ 0, PNT error terms, all zeros and the pole, every progression statement up to O(1) |
| O3 | tail deletion | a ↦ a·1_{n<n₀} | exact values Λ(n), n < n₀; 0 ≤ a ≤ Λ; every upper-bound sieve inequality |
| O4 | uniform rescaling | a ↦ c·a, c > 0 (O4ε: c ∈ (1−ε, 1+ε)) | Euler product (ζ^c), support, multiplicativity of the generating function, relative size of all weights |
| O5 | ε-perturbation of weights | v ↦ v′, ‖v − v′‖₁ ≤ ε, or one weight by ε | every bounded continuous functional of v up to O(ε) |
| O6 | Beurling repositioning | ℕ ↦ generalized-integer semigroup with positive prime measure | a ≥ 0, Euler product, Λ*1 = log formally, sieve axioms |
| O7 | Euler-preserving prime deletion | a ↦ a_P := Λ·1_{p ≥ P} (all powers of p ≥ P) | Euler product over ℕ, ℤ-integrality, a ≥ 0, local values a(p^k) = log p on the support, all zeros in 0 < Re s < 1 and the pole |
| O8 | FE-preserving zero-side twist | ξ ↦ ξ_{z,k} (quartets, M_m); ζ ↦ ζ + t g (f_t); ξ ↦ ξ·R (ζ̃) | functional equation with Γ_ℝ, conductor 1, reality, pole, **exact comb** (M_m), or exact comb below λ₁ (f_t), or line identity + mean values (ζ̃) |
| O9 | Euler removal | ξ ↦ Ξ_Q (Epstein, h(−D) > 1), DH series | FE with Γ(s/2) (or Γ(s)), pole, reality, nonnegative coefficients, A1–A6 |
| O10 | field change | ξ ↦ ξ_K | every field-uniform property (equimodularity of the polar block, FE, Euler product over 𝒪_K) |
| O11 | FE reflection of the σ-family | D_σ ↦ D_{1−σ} | the σ-family of symbols as a set |
| O12 | window restriction | q ↦ (q_T)_{T∈J}, J bounded | the values λ(T), T ∈ J, monotonicity, continuity |
| O13 | symbol truncation | σ_T ↦ σ^{(η)} := min(σ_T, η) | the negative set U_T, the symbol on {σ_T < η} |
| O14 | bounded perturbation of the form | q_T ↦ q_T + 𝔟, ‖𝔟‖ ≤ λ_A(T) | every criterion valid for all bounded perturbations / all nonnegative trace-class B |
| O15 | Poisson randomization | positions {log n} ↦ Poisson process of the same intensity | density, mean counting, second moments |

### 1.3 Argument classes (what a deduction may use)
A **deduction class** 𝒜 is specified by a set 𝖯 of properties of form objects; a deduction in 𝒜 is a valid chain "q has 𝖯 ⇒ λ(T; q) ≥ 0 for every T" (or at a fixed T). 𝒜 is **closed under O ∈ 𝒪** if every q with 𝖯 has O(q) with 𝖯 (for the parameters of O listed in the clause). The record's named classes:
- **(LIN)** linear-in-autocorrelation identities + Bochner/Cauchy–Schwarz: everything expressible as Σ_i Re⟨A_iF, B_iF⟩ with convolution operators A_i, B_i (Euler, Möbius, log-derivative, Gram identities among U_μF, U_logF) — P46 prop:opcalc, 188/N_BUILD_018 Thm 2.
- **(FUN)** norm / determinant / moment / local-symbol / family / pattern / coherence functionals: W-lin, W-det, W-mom, W-loc, W-fam, W-pat, W-coh (P46 sec:barriers, sec:wh; 186/R186_029–053).
- **(ZERO)** zero-information inputs 𝒞_zeros: zero-free regions, zero density, finitely many verified zeros, all zeros and the pole (P46 cor:void, thm:finZ; 189/NT_011, NT_014).
- **(PNT/PROG/SIEVE)** 𝒞_PNT(ε), 𝒞_prog, 𝒞_BT: PNT with error term, progression statements (Siegel–Walfisz, BV, BDH, Brun–Titchmarsh), upper-bound sieves (P46 cor:void, prop:prog; 188/N_BUILD_021 Thm 2; R167_102/103).
- **(D)** dual / lattice / flat-top / SOS certificates: Definition def:PD, thm:Z, thm:sos, thm:posext, rem:farext (class (D) in P46).
- **(SYM)** σ-transport and FE-symmetrization of the spectral family D_σ (188/L2_BUILD_026, L2_027).
- **(GEO)** axioms A1–A6 / field-uniform properties (P47 §18).

---

## 2. Theorem (Shape)

**Theorem S (shape of any proof of row D).** Let 𝒜 be a deduction class with property set 𝖯, and let q₀ be the object of ζ.
*(A) Transfer part.* If 𝒜 is closed under any one of the operations O1–O15 in the parameter ranges of Lemmas A1–A15 below, then 𝒜
contains no valid deduction of WP_T(q₀) at the windows named in that lemma; in particular none proving row D.
*(B) Structural part.* Every valid deduction of row D, in whatever class, satisfies Lemmas B1–B8: its margin at T ≥ 1 is at most
4·10⁹ T e^{−15.449 T}; it is exact (no slack) at the centre, at every packet frequency, at the integer-resolution mean square, and at the
density ceiling; it cannot be the FE-symmetrization of the σ-family; if written in shift-multiplier calculus it is a linear identity on
(−2T, 2T) plus Bochner positivity, and no pure arithmetic sum of squares at T ≥ ½log3; every "weaker" substatement in the list B8 is the
target itself.
*(C) Positive form.* Hence every valid proof of row D uses, at a load-bearing line, a property of ζ that is destroyed by **each** of
O1–O15 — see Corollaries 3(a)–(e) for the explicit list.

*Proof.* (A) is Lemma lem:transfer (P46): if q₀ and O(q₀) both have 𝖯 and λ(T; O(q₀)) < 0, the deduction applied to O(q₀) is false.
Each Lemma A_i supplies O(q₀) explicitly and proves λ(T; O(q₀)) < 0 at the named T. (B) is the conjunction of Lemmas B1–B8, each proved
in the cited place. (C) is the contrapositive of (A): a proof whose property set were invariant under some O_i would lie in a class closed
under O_i. ∎ (The theorem is a bookkeeping statement; its whole content is in the lemmas and their labels.)

### 2.1 Transfer lemmas (operation → falsifier → window → label)

| # | op | Lemma | falsifier O(q₀) | fails WP_T at | label | proof |
|---|---|---|---|---|---|---|
| A1 | O1 | classes closed under finite deletion | Λ·1_{n≥N}, N ≥ max(5, e^{2T}) | every T ∈ [0.60, ½log N]; every T > T₀(0) = 0.74921 unconditionally | **PROVED** | P46 thm:finmod(i), cor:void; prop:arch(ii) for T > T₀(0); the 0.58/0.60 thresholds from thm:index(i)/cor:Tarch |
| A2 | O2 | classes closed under one-term amplification | Λ + c·1_{n=2}, c > c_*(T, 2) | every T > ½log2 (incl. (½log2, ½log5] where WP_T(Λ) holds) | **PROVED** | P46 thm:finmod(ii), cor:void; test F₊ of lem:cpos |
| A3 | O3 | classes closed under tail deletion (keep all Λ(n), n < n₀; 0 ≤ a ≤ Λ) | Λ·1_{n<n₀} | all T ≥ T₁(n₀) (not located) | **PROVED** | 188/N_BUILD_003 Thm 1; P46 prop:finsupp, cor:wtail(i) (limit value C₀ − Σ_{n<n₀} v_n < 0) |
| A4 | O4 | classes closed under uniform rescaling cΛ, all c > 0 | cΛ, c large: every T > ½log2; cΛ, c → 0: every T ≥ 0.60 | as stated | **PROVED** | c large: finmod(ii) argument with F₊ at log 2 (only n = 2 is charged, 188/L2_BUILD_011 row 6); c → 0: λ_A(T; cΛ) is concave in c and equals λ_{∞,P}(T) < 0 at c = 0 (cor:Tarch; unconditionally for T > T₀(0)) |
| A4ε | O4ε | classes closed under (1 ± ε)Λ for small ε (𝒞_ε of N_003) | (1 + sgn κ_T ε)Λ, ε > λ_A(T)/\|κ_T\|, κ_T := Σ v_n c_h(log n), h a minimizer | at T, **if κ_T ≠ 0** | **CONDITIONAL (κ_T ≠ 0)** | P46 prop:wit-sens (Rayleigh with h); 188/N_BUILD_003 Thm 2. κ_{log2} ≈ 0.09 NUMÉRICO (rem:wit-sens). If κ_T = 0 for every minimizer, Lemma lem:degen applies and the clause is empty at that T |
| A5 | O5 | classes closed under changing one weight by ε (inputs known to width ε) | Λ + s ε 1_{n=n₀}, s = sgn c_{F*}(log n₀), ε > ε_*(T, n₀) = √n₀ λ_A/(2\|c_{F*}(log n₀)\|) | at T, **if c_{F*}(log n₀) ≠ 0** | **CONDITIONAL**; the quantitative 10⁻⁵ at log 2 is **NUMÉRICO** | P46 rem:resweights (envelope inequality of lem:degen); 186/R186_051 Prop 4.5 (λ_A(log 2): +1.04·10⁻⁷ → −7.8·10⁻⁷ at ε = 10⁻⁵, Galerkin) |
| A6 | O6 | classes closed under Beurling repositioning (a ≥ 0, Euler, Λ*1 = log formally, sieve axioms) | DMV / Zhang generalized systems with an off-line zero; ℕ ∪ √2ℕ (R184_005); BF^disc (R163_803) | some T (not located) | **ARGUED** (erratum 4: no Beurling window form W_T exists in the record, R167_103 row 7; the step "off-line zero ⇒ negative window bottom" is not written) | R167_102 Thm B/B′, R167_103 Thm S; 188/L2_BUILD_011 row 4 |
| A7 | O7 | classes closed under Euler-preserving prime deletion | a_P = Λ·1_{p≥P}: Euler product ζ∏_{p<P}(1 − p^{−s}) over ℕ, integral, positive, same zeros and pole; comb empty on 𝒩_T for T ≤ ½log P | every T ∈ [0.60, ½log P] | **PROVED** | 188/L2_BUILD_011 row 8 (variant of finmod(i)); breaks only the FE |
| A8a | O8 | classes closed under quartet multiplication (exact comb kept; FE, reality, pole kept; a.c. part −kβ_z added) | ξ_{z,k}, k ≥ k₀(T, δ, γ) | every T (witness at T, hence at all T′ ≥ T) | **PROVED** | P46 thm:wit-model(iii); shared properties prop:quartetmodel (lem:contA, first contact, thm:margin-type bound) |
| A8b | O8 | classes using only window data below ½log λ₁ (exact Λ(n), n < λ₁) + FE + reality + pole | f_t = ζ + t g (self-dual measure with a hole) | some T > ½log λ₁ (primitive witness φ₀) | **PROVED** (unconditional per rem:bar-fam; (H_f) PROVED, index 04_ F-f_t) | P46 lem:selfdual, prop:ft, prop:ftprim, thm:famFE |
| A8c | O8 | class 𝓜 = FE (Γ_ℝ, q = 1) + line identity Re ζ′/ζ = −½m + finitely many mean-value/moment bounds with slack, **without** (holomorphy ∧ order 1) jointly | ζ̃ = ζ·R, R = ∏_±[(s−½−δ∓iγ₀)(s−½+δ∓iγ₀)]/[(s−½−2δ∓iγ₀)(s−½+2δ∓iγ₀)] | excludes pointwise upper bounds for ℓ″ (hence pointwise (𝒱)) on every interval; **as a window-form falsifier of WP_T: ARGUED only** (an m-fold version would need the analogue of thm:wit-model(iii), not written) | **PROVED for the (𝒱)-step** (NO-GO class 𝓜, restated by the review) / **ARGUED for WP_T** | 189/NT_011 Thm 11.2; NT_011_014_REVIEW (FIX: 𝓜 must not contain holomorphy and order-1 growth together) |
| A9 | O9 | classes using only FE + pole + reality + nonnegative coefficients (A1–A6, no Euler) | Epstein Ξ_Q with h(−D) > 1 (Davenport–Heilbronn zeros in Re s > 1); DH series | complete Weil form negative (CITED); some window T for the **complete** form W_T (a negative test has compact support) | **CITED (complete form) / ARGUED (primitive form λ_A: a primitive witness as in prop:ftprim is not written for Ξ_Q)** | P46 rem:twohalves; P47 Thm 18.10, 18.16 (T2) with (X21) CITED |
| A10 | O10 | classes using only field-uniform properties | ξ_K (any K), S₃-type non-abelian cases | **no explicit window-form falsifier in the record** | **CONDITIONAL / OPEN falsifier**: the record's T1 (P47 Thm 18.1) is a transfer principle ("a derivation from field-uniform 𝖯 is a derivation for every ξ_K"); its falsifier half passes through a statement about ζ_K that the stated rule excludes from use here, so it is restated as the bare transfer principle, PROVED as such, with the falsifier half OPEN | P47 §18.1; index 04_ W9 = T1, F-ζ_K/S₃ |
| A11 | O12 | classes using the family only on a bounded J ⊂ (0, T₁] + monotonicity + continuity, and the weights only through a class closed under O2 (or the FE class) | Λ + c 1_{n=n₀}, n₀ > e^{2T₁} (and f_t with λ₁ > e^{2T₁}, FE-preserving) | every T > ½log n₀, c > c_*(T, n₀) | **PROVED** | P46 thm:famblind, thm:famFE, rem:bar-fam; 186/R186_036 Thm 3(a). **Not excluded:** unbounded J, which enters only through L = lim λ_A ≥ 0 (R186_036 Thm 3(b)), and two-sided laws λ_A = L(T)(1 + o(1)), L > 0 (rem:bar-fam: "this class is open") |
| A12 | O13 | criteria depending on σ_T only through {σ_T < η} (components of U_T and neighbourhoods) | σ^{(η)} = min(σ_T, η), η < η₀(T) | every T (at T ≤ ½log5 the first form is positive, the second is not) | **PROVED** | P46 thm:nolocal, rem:bar-loc |
| A13 (→ B9, erratum 6: not a transfer instance) | O14 | criteria valid for all bounded perturbations of the form / all nonnegative trace-class B (moments, norms, leading-term determinants with O(1) relative error) | q_T − λ_A\|⟨·, h*⟩\|² (bottom 0), B_T + (1 − β₁)v₁⊗v₁ | every T: margin of the criterion ≤ Lk λ_A/c_P (moments), ≤ Lλ_A (continuous), D₀ with ε₀ ≥ 1 never decides | **PROVED** | P46 lem:wh-T, lem:wh-Tprime, thm:wh-det, thm:wh-detinherit(iii); 186/R186_034 Thm 3.1, R186_045 |
| A14 | O8 | deductions from window observables 𝖮 (bottom up to relative error, parity, peak frequency, eigenvalue counts, fitted laws) | ξ_{z,1} with δ ∈ {10⁻³, 10⁻⁶} (matches 𝖮 to 3 %, numerically) and δ = 0.1 (negative between 0.55 and 0.69) | T ∈ [0.55, 0.69] | **NUMÉRICO for the full list 𝖮; PROVED for the proved shared-property list of prop:quartetmodel with k large (thm:wit-model(iii))** | P46 cor:pattern, rem:quartetnum, rem:bar-pat; phase 187 |
| A15 | O1/O2 via 𝒞_prog, 𝒞_BT | classes defined by progression statements up to O(1) (Siegel–Walfisz, BV, BDH, Titchmarsh divisor, Brun–Titchmarsh) or by upper-bound sieves (0 ≤ a ≤ Λ) | reduce to A1/A2 (progressions) and A1/A3 (sieves); b_θ = Λ·½(1 + cos(γ log n + …)) for sieve blindness | every T > T₀(0) (deletion), T > ½log2 (amplification) | **PROVED** | P46 prop:prog; 188/N_BUILD_021 Thm 2; R167_102 Thm B/B′ (b_θ), R167_103 Thm S |
| A16 | O15 | density-type arguments (positions only through intensity/moments) | Poisson comb ν_Π of intensity κ | T ≥ T(c, κ): P(𝔞^{ν_Π}_T ≥ 0 on P_T) ≤ e^{−cT log T} | **PROVED** | P46 thm:poisson, thm:band; 188/L2_BUILD_021–023 |
| A17 | O1/O2 (𝒞_zeros) | zero-information classes: zero-free regions, zero density, all zeros + pole; finitely many verified zeros | Λ1_{n≥N}, Λ + c1_{n=2} (ζ_a = ζE, E entire zero-free, same zeros); for flat-top certificates: any finite symmetric Z | every T > ½log2 (cor:void); every T and every finite Z (thm:finZ) | **PROVED**; 189/NT_014 "(b) ∈ 𝒞_zeros" is **ARGUED** (forward PROVED, converse ARGUED) | P46 cor:void, thm:finZ, thm:finDet; 188/L2_BUILD_010 §3; 189/NT_014 Thm 14.1 / Prop 14.2 |

### 2.2 Structural lemmas (no falsifier; constraints on every proof)

| # | Lemma | statement | label | proof |
|---|---|---|---|---|
| B1 | margin | λ_W ≤ λ_P ≤ λ_A(T) ≤ 4·10⁹ T e^{−15.449 T} for T ≥ 1; limsup_{T→∞} λ_A ≤ 0. Hence every lower bound that proves row D at T must have absolute precision ≤ this; relative to the comb mass 2e^T, precision ≍ e^{−16.4 T} | **PROVED** (inputs CITED: (Z1), (Z2) verified zeros to H_PT, Platt–Trudgian) | P46 thm:margin, cor:margin1, lem:testfam; W2 |
| B2a | centre criticality | −2ζ′/ζ(½) = m(0) = C₀ exactly: at τ = 0 the zero sum Σ_ρ Re 1/(½ − ρ) vanishes for **every** zero configuration; (E₀) holds with equality at every order of the curvature expansion; the sign of 𝒯₀ is the sign of Z_T(φ₀) = Σ_ρ ĥ_T(γ_ρ) with no constant slack | **PROVED** (Hadamard product, FE CITED) | 188/L2_BUILD_010 §1–2 |
| B2b | packet criticality | at every γ, lim_T 𝓕_T(F_T) = m^♯(γ) = lim_T 𝔞^♯(F_T) whenever the Riesz means converge; hence (E_γ, C) ⟺ (E_γ) for every C ≥ 0: no slack at any frequency | **PROVED modulo CITED (Hardy–Riesz) + ARGUED (divergent alternative)**; i.e. **CONDITIONAL** | 188/N_BUILD_013 §1–3; P46 prop:Egamma-exact, prop:wit-Egamma |
| B2c | mean-square criticality | RMS of the comb over \|τ\| ≲ e^{2T} is ≥ 2T(1 − o(1)) (Σ 4Λ(n)²/n ≈ 8T²), equal to g₁(e^{2T}) ≈ 2T: comb oscillation and symbol are of the same size at the integer resolution; any proof must use correlation inside P_T on the low band \|τ\| < τ₁ (fixed) **and** at all frequencies up to e^{2T} at the critical level | **PROVED (Mertens CITED)** | 188/L2_BUILD_019 §4 |
| B2d | density ceiling | any comb a with λ_A(T; a) ≥ 0 ∀T has liminf S(x)/log x ≤ 1; Λ sits exactly at the ceiling (Mertens); the main-term comb ρ_κ is positive ∀T iff κ ≥ κ_* ≥ ¼|C₀| = 1.343 > 1 = κ(Λ), so the deficit (κ* − 1)/(¼ + τ²) must be paid by the fluctuation, never by the main term | **PROVED** | P46 thm:ceiling, thm:kappa, lem:reson; 188/N_BUILD_011 |
| B2e | no asymptotic slack | row D ⟺ λ_A(T) ≥ −ε(T) ∀T for some ε → 0 ⟺ λ_A(T_k) ≥ 0 along one sequence T_k → ∞ (internal restatements): there is no weaker "approximate" sub-statement in T | **PROVED** | P46 thm:wit-Tc(iv); lem:monoT |
| B3 | FE antisymmetry | D_{1−σ}(τ) = −D_σ(τ) exactly; every σ ↔ 1−σ symmetric combination of the spectral family vanishes; D_{½} ≡ 0 off ordinates: the on-line density carries no sign, all sign lives in singular parts / off-line residues | **PROVED** | 188/L2_BUILD_026 §1; P46 rem:fe; (SYM) class void |
| B4 | operator calculus is linear | Σ_i Re⟨A_i*F, B_i*F⟩ = ∫_{(−2T,2T)} Re c_F dν with ν = Re Σ_i Ā_i * B̌_i: every shift-multiplier identity is a measure identity on the window (carries the whole margin), and the only extra tool is Bochner (‖A*F‖² ≥ 0) / Cauchy–Schwarz. **Scope: shift-multiplier calculus only** (finite measures acting by convolution); SOS without C–S is not excluded by this lemma | **PROVED** (Plancherel) | P46 prop:opcalc; 188/N_BUILD_018 Thm 2 (the claim "C–S always loses" is **ARGUED**, shown only in the instances N_017 (size 4T) and L2_017 (class empty for T ≥ 0.60)) |
| B5 | arithmetic squares | no decomposition Σ_i\|D_i(τ)\|² = μ₀ − Σ_{𝒩_T} v_n cos(τ log n) with 𝔪_T − μ₀ ≥ 0 on P_T exists for T ≥ ½log3 (μ₀ ≥ 𝖠_T ≥ 0.980 > 0.311 ≥ λ_{∞,P}(½log3)); with a free positive-definite part the decompositions are exactly the certificates of def:PD, whose content is λ_P (thm:D1) | **PROVED** ((½log2, ½log3) OPEN) | P46 thm:sos; 188/N_BUILD_019 |
| B6 | orders, relative bounds, positive exterior, termwise comb | (i) ±δ_a, ±ρ ∉ 𝒦_T* (Möbius resolvent not monotone); (ii) no KLMN relative bound (θ, κ, C) decides for large T (even θ = 0 fails); (iii) no certificate of the complete form with ν ≥ 0 and value ≥ 0 at ½log3, ½log5 (κ_T(Φ) < 0 there: numerical evaluation of an elementary integral); (iv) term-by-term comb bounds cost the full mass 𝖠_T | **PROVED** ((iii) modulo 25-digit floating evaluation: **NUMÉRICO constant**) | P46 prop:cone, prop:relative, thm:posext, rem:posext, prop:primeblind; 188/N_BUILD_007/008 |
| B7 | flows and new contacts | (i) any C¹ flow of log det on Galerkin sections has coefficient dominated by ⟨A′h*, h*⟩/λ_A near a small bottom (a functional of the minimizer); (ii) positivity at T > T₀ forces the new primes to cancel σ_{T₀} on U_{T₀} **on average** (never pointwise); converse false | (i) **PROVED** (Jacobi/Hellmann–Feynman) with the barrier reading **ARGUED** (rem:bar-loc); (ii) **PROVED mod LW** / converse **NUMÉRICO** (M₁) | P46 lem:flowdet, rem:bar-loc, thm:X; 186/R186_044–048 |
| B8 | no weaker substatement (REF-D cluster) | each of: flat-top certificate f_w ≥ c (thm:Z: f_w = Σ_ρ ŵ(τ − γ_ρ), content = explicit formula on h_τ = w cos τ·), the Kreĭn indeterminacy (thm:KEPdich), Theorem S "B_{F₀} positive definite" (thm:oneprofile), residue-balanced constraints (R_Q), (B_Q) (L2_031 Thm E), λ_A ≥ −ε(T) (B2e), (N)/(N_loc) ⟺ (L2) (L2_006), ρ*(T) < 1 (R186_018), scalar index criterion (R186_028) — is an exact restatement of row D and not a weaker statement; a proof of any of them is a proof of D with the same shape | **PROVED** (each equivalence is internal to D; Theorem E PROVED; thm:Z PROVED; KEP mod λ_W = 0) | P46 thm:Z, thm:Zexh, thm:KEP1/2/dich, thm:oneprofile; 188/L2_BUILD_031 §2, §4; 188/L2_BUILD_006; index 04_ W1 |

### 2.3 The input map as a lemma
**Lemma I (minimal surviving inputs; PROVED relative to the 23-row table in 188/L2_BUILD_011 §2, modulo CITED (Epstein) and ARGUED (Beurling); see erratum 10 for the row-13/21 bookkeeping).** Every property of Λ in the 23-row input map that is KILLED keeps one of: "no FE" (rows 1–9, 13–14, 21: O1, O2, O3, O7 falsifiers), "no Euler product over ℕ" (rows 10, 11: O9 falsifiers, f_χ), or "not ℤ-integral" (row 4: O6 falsifiers). Hence any surviving property set contains jointly (Euler product over ℕ, i.e. Λ*1 = log on ℕ) ∧ (FE with Γ(s/2), conductor 1, pole) — which identifies ζ (rows 9′, 12, 17; Hamburger / Thm O of R163_1001) — or the exact window vector (Λ(n))_{n<e^{2T}} per window (row 23). UNKNOWN as falsifier sources: Euler + FE at conductor q > 1 (row 18; 188/N_BUILD_021 Prop 3 shows it does not enter A_M exactly), étale structure for Spec ℤ (row 22, no object).

---

## 3. Corollaries

**(a) Non-linearity in the exact vector; destroyed by every operation.** A valid proof of row D uses the vector (Λ(n))_{n<e^{2T}} (i) exactly — A1, A2, A5, A7 forbid classes closed under changing any one value; A3 forbids using only the small values; A4 forbids using only the shape cΛ — and (ii) non-linearly: a linear functional of the weights is a measure identity on (−2T, 2T) (B4) and so carries the whole margin, i.e. is a certificate of class (D), whose content is λ_P itself (B5, B8). At the same time it uses (iii) a property not shared by the zero-side modifications: M_m (A8a) keeps the comb exactly, so the property is not a property of the comb alone; f_t (A8b) keeps the comb below λ₁ and the FE; Ξ_Q (A9) keeps the FE and nonnegativity. Each operation O1–O15 therefore breaks a load-bearing hypothesis of every valid proof. Labels: PROVED for O1–O4 (large/small c), O7, O8a, O8b, O12–O15; CONDITIONAL for O4ε, O5 (κ_T ≠ 0, c_{F*} ≠ 0); CITED for O6, O9 (complete form); OPEN falsifier for O10.

**(b) Joint use of Euler product × FE (conductor 1) × ℤ-integrality.** By Lemma I, dropping the FE leaves a_P (A7), dropping the Euler product leaves Epstein/DH (A9), dropping ℤ-integrality leaves Beurling (A6); each is a falsifier. So the three inputs enter jointly and non-linearly (crossword exigencias (α), (β), (δ), (θ)); and since the triple identifies ζ, the proof cannot be a class argument over a set of objects — it is a computation with ζ's own data at every window, uniform in T (W-identification, R164_190; T1 restated as transfer, A10).

**(c) The sign is a correlation property, not a statistic.** Write h* for a real unit minimizer at T. Then λ_A(T) = 𝔞_T(h*) and, by the envelope inequality of lem:degen, λ_A(T; v′) ≤ λ_A(T) − Σ_n (v′_n − v_n) c_{h*}(log n): the first variation of the bottom in the weights is **−c_{h*}(log n)**, the autocorrelation of the minimizer at the contact (PROVED). Hence: (i) no bounded continuous functional of the weights or of the symbol decides the sign (A5, A13; R186_051 Prop 4.5: a 10⁻⁵ relative change of v flips λ_A(log 2) while every coherence statistic moves by < 10⁻⁵ — NUMÉRICO constant); (ii) no local criterion on σ_T (A12) and no term-by-term bound (B6(iv)) decides; (iii) phase 190 (NUMÉRICO): all statistics of the near-coincidence matrix Near_M (norm ≈ 0.17M, rank, sign pattern, mass ∝ Λ(n)n^{−3/2}, orthogonality to the negative archimedean cone, flatness in h = m − kn) are identical to 5 digits under 10⁻⁵ perturbations that make A_M indefinite from M ≈ 200–400, and the sign of A_M(Λ) is decided on the vector ≈ m^{−½} w(m/M) that annihilates the zero ordinates (EXP_003 Fact N2, zero-side observation). So the sign at T is the correlation of the exact weights with the minimizer's autocorrelation (equivalently, with the samples \|ĥ*(ω_k)\|² on the Nyquist mesh, R186_051 Thm 4.1), a quantity that is minimizer-dependent and not a function of symbol or matrix statistics. Label: PROVED (envelope, A12, A13) + NUMÉRICO (10⁻⁵ constants, Near statistics).

**(d) Criticality: no slack at any frequency, no slack in T.** B2a (centre), B2b (every packet frequency, CONDITIONAL), B2c (mean square at integer resolution), B2d (density ceiling: main term below κ*; deficit paid by fluctuation only), B2e (no asymptotic slack in T), B1 (margin ≤ 4·10⁹Te^{−15.449T}). A proof cannot discard any band of frequencies, cannot lose a constant at any γ, cannot win on the main term, and cannot stop at an approximate statement in T.

**(e) The admissible region, stated positively.** Nothing in §2 excludes an argument with all of the following properties, and every valid proof must have them:
1. uses the exact values Λ(n), n < e^{2T}, at every T (A1–A5, A7), **not** as membership in a class closed under any O_i;
2. uses the Euler product over ℕ (Λ*1 = log on ℕ, ℤ-integrality) and the functional equation with Γ(s/2) at conductor 1 together (Lemma I; A6, A7, A9);
3. is non-linear in Λ (B4) — equivalently, not of class (D)/(LIN): not a certificate, lattice certificate, flat-top certificate or operator identity + Cauchy–Schwarz (B5, B8); SOS with arithmetic squares and a free positive-definite part is allowed only as a certificate (REF-D);
4. is not zero-information (A17): it does not reduce to zero-free regions, densities, or finitely many zeros; the ζ̃ model (A8c) shows it must use holomorphy and order-1 growth jointly, or the Euler product on the line, if it passes through pointwise statements of the height flow;
5. is not a bounded functional of the weights or of the symbol (A5, A13, W-coh), not local on U_T (A12), not a determinant leading term with O(1) error (A13), not a pattern of window observables (A14), not a bounded-range family law (A11);
6. is sensitive to 10⁻⁵ perturbations of the weights at log 2 (NUMÉRICO) and in general to λ_A/κ_T (A4ε, A5): its precision at T ≥ 1 is ≤ 4·10⁹Te^{−15.449T} (B1);
7. is exact at the centre, at every packet frequency, at integer resolution (B2a–c), and wins only from the fluctuation of Λ, not from its density (B2d);
8. uses the positive part of σ_T on all of ℝ jointly with the negative set (rem:bar-loc), i.e. correlation inside P_T across all frequencies up to e^{2T} (B2c, (c));
9. is not a σ-transport through FE-symmetrization (B3), not a σ-transport through residues at zeros (A17; L2_027 (M)), and not an Euler-direction family that is exactly critical (NT_003/004);
10. uses a property beyond the axioms A1–A6 (A9: Ξ_Q, complete form, CITED), and is uniform over fields only if it names the property that separates ζ from every ξ_K (A10, transfer principle). [Erratum 12: the former reference to A3/A7–A9 of Paper 47 concerned the Hodge-index form, not λ_A.]
Specific objects the record does **not** exclude: two-sided asymptotic laws λ_A = L(T)(1 + o(1)) on unbounded ranges (rem:bar-fam, R6); signed exterior measures (rem:bar-lin); primitive certificates with ν ≥ 0 and free β (rem:bar-lin, only numerical indication of failure); arithmetic SOS on (½log2, ½log3); exact Schur reductions carrying the whole margin (thm:coer-schur, thm:wh-schur); conductor > 1 inputs by routes other than the two of N_021 Prop 3; the (N)/(N_loc) correlation inequality itself (R1) and its reductions (Ω₀), (E_γ), (Ω_Φ), (Ω_{t₀}), Problem (S) on the near-coincidence part (R9), the §28.4 object (R8), the NT door at σ = 1 (R10), O166.802.1 (R7).

---

## 4. What this theorem does not say

1. **It does not say that row D is unprovable.** Every clause is an instance of lem:transfer (a deduction applied to a falsifier is false) or a precision/criticality constraint; both exclude *deductions*, never the *conclusion*. The record contains proofs of WP_T for T ≤ ½log5 (P46 thm:C, thm:log5A/W) and, cited, to 0.8 (Zhu) and 17/16 (Liu, complete form, preprint) — all computations with the exact vector, in the admissible region (e).
2. **It uses no equivalence between row D and any other statement.** The internal restatements in B2e and B8 are equivalences among forms of D itself (bottoms, certificates, one-profile functions) and are used only to say "this is not weaker than D". The one place where the record's own proof passes through an external statement — T1 of Paper 47 — has been restated here (A10) as a bare transfer principle with its falsifier half left OPEN. The Epstein falsifier (A9) is a statement about Z_Q, obtained from Davenport–Heilbronn and Weil's criterion for Z_Q (CITED), i.e. about another object.
3. **Which clauses are not PROVED, and what would upgrade them.**
   - A4ε, A5 (small rescaling, single-weight ε): CONDITIONAL on κ_T ≠ 0, resp. c_{F*}(log n₀) ≠ 0 for some minimizer. Upgrade: prove κ_T ≠ 0 at one T (a sign statement about the minimizer's autocorrelation against the comb; rem:resweights says nothing is known), or prove the degenerate case of lem:degen cannot occur. NUMÉRICO: κ_{log2} ≈ 0.09.
   - A6 (Beurling): CITED; the negativity of the generalized window form comes from the explicit formula of the Beurling system. Upgrade: an explicit negative test for one DMV system at one T, written out.
   - A8c (ζ̃): PROVED only for the pointwise-(𝒱) step of the NT height-flow route; as a direct window-form falsifier ARGUED. Upgrade: an m-fold ζ̃^{(m)} with a witness at every T (analogue of thm:wit-model(iii); the quartet-minus-quartet form Q_{δ+iγ₀} − Q_{2δ+iγ₀} has the needed growth e^{4δT}, not computed).
   - A9 (Epstein): CITED for the complete form, ARGUED for the primitive bottom λ_A(T; Ξ_Q). Upgrade: a primitive witness as in prop:ftprim.
   - A10 (field change): OPEN falsifier. Upgrade: a window T and a number field K with λ_A(T; ξ_K) < 0 proved directly (a computation with ξ_K's own data, no transfer).
   - A14 (patterns): NUMÉRICO for the full observable list (δ = 10⁻³, 10⁻⁶ models); PROVED only for the proved shared-property list with k large.
   - A17/NT_014: "(b) ∈ 𝒞_zeros" ARGUED (converse of Thm 14.1).
   - B2b (packet criticality): CONDITIONAL on Hardy–Riesz (CITED) and the ARGUED divergent alternative.
   - B4's reading "Cauchy–Schwarz always loses": ARGUED (instances only); the lemma itself (linearity) is PROVED and its scope is shift-multiplier calculus only.
   - B6(iii) (positive exterior fails at ½log3, ½log5): the theorem is PROVED; the failure at those windows uses a 25-digit floating evaluation (NUMÉRICO constant).
   - B7: barrier readings ARGUED/NUMÉRICO (M₁ converse of thm:X).
4. **Known coverage gaps of the record (index README "Correcciones ").** Phases 6–31 are known only by summaries (no folder on disk); Part II of 04_ assigns families by keyword; RH2017–RH2020 by opening/closing lines. **Categories never tried**: condensed mathematics (MW-3 variant, index 06_ "MW-3"), K-theory / étale structure for Spec ℤ (input-map row 22: no object), the Lewis–Zagier / Mayer transfer-operator route (phase-152 R152_001, listed OPEN, never attempted), boundary triples for W_λ (phase-60 §4.B, never attempted). The theorem says nothing about these except that a proof from them must still satisfy §3(e).
5. **It does not rank the residues.** R1–R10 of index 06_ are all inside the admissible region; the theorem only states what each must escape ([void], [tail], [sens], [F], [T1/T2], [lin/det/fam/pat/loc/mom/coh], [margin], [opcalc], [zeros], [crit], [sym] — the barrier key of 06_), and §3(e) is that list written as properties of the proof instead of as walls.

---

## 5. Self-review (clause by clause: does the cited proof prove the clause as stated?)

- **A1.** thm:finmod(i) proves failure for 0.60 ≤ T ≤ ½log N via thm:index(i)/cor:Tarch and for T > T₀(0) via prop:arch(ii). The two thresholds 0.58/0.60 are from the paper's certified archimedean computation; the unconditional part is T > T₀(0) ≈ 0.8047. Clause stated with both ranges. ✓
- **A2.** thm:finmod(ii): F₊ of lem:cpos is smooth, in P_T, and only the contact n₀ is charged; c_* explicit. ✓ Works at every T > ½log n₀. ✓
- **A3.** N_003 Thm 1 is the dilated-test argument of prop:finsupp; limit value C₀ − Σ_{n<n₀} v_n < 0 since C₀ < 0 and v_n ≥ 0. The window T₁(n₀) is not located. ✓ (stated)
- **A4.** c large: the F₊ argument charges only n = 2 because supp c_{F₊} ⊂ [−log2 − \|J₀\|, log2 + \|J₀\|] and log3 − log2 > \|J₀\| for short J₀; so Σ v_n c_{F₊}(log n) = v₂‖φ‖² > 0 and 𝔞^{(cΛ)}(F₊) → −∞. ✓ c small: λ_A(T; cΛ) is an infimum of affine functions of c, hence concave and continuous; value at c = 0 is λ_{∞,P}(T) < 0 for T ≥ 0.60 (cor:Tarch) and for T > T₀(0) (prop:arch(ii)). ✓ **Concavity gives nothing for c near 1**: the small-ε clause is A4ε, CONDITIONAL. ✓
- **A4ε / W-tail Thm 2.** prop:wit-sens: λ_A(T; (1+ε)v) ≤ λ_A − εκ_T is Rayleigh with h; it flips the sign only if κ_T > 0 (or κ_T < 0 with (1−ε)); κ_T ≠ 0 is **not proved at any T**. The index entry "W-tail: uniform rescaling CONDITIONAL κ_T ≠ 0" is the honest label and is kept. ✓
- **A5.** rem:resweights: needs c_{F*}(log n₀) ≠ 0 for some minimizer and the chosen contact; otherwise lem:degen (degenerate case) and the clause is empty. The 10⁻⁵ figure is Galerkin, not certified. Labelled CONDITIONAL + NUMÉRICO. ✓
- **A6.** The record cites DMV/Zhang (generalized systems whose zeta has zeros off the line) and R167_103 Thm S (sieves hold for Beurling systems). The step "off-line zero of the Beurling zeta ⇒ negative window form of the Beurling comb" is the explicit formula of that system; it is an argument about the Beurling object and is CITED here, not re-proved. The window T is not located. ✓ (labelled)
- **A7.** L2_011 row 8: a_P(p^k) = log p for p ≥ P; generating function ∏_{p≥P}(1 − p^{−s})^{−1}; comb empty on 𝒩_T for e^{2T} ≤ P; form = 𝔞_∞ on P_T; negative for 0.60 ≤ T ≤ ½log P. ✓ It is finmod(i) with a different deleted set; novelty is only that the Euler product is kept exactly. ✓
- **A8a.** thm:wit-model(iii) is PROVED for configurations with multiplicity m ≥ m₀(T, δ, γ); the shared properties with ζ are those of prop:quartetmodel (continuity, monotonicity, first contact, margin-type bound), **not** the full observable list (that is A14, numerical). ✓
- **A8b.** rem:bar-fam states both family theorems unconditional and that prop:ftprim supplies a primitive witness; index 04_ F-f_t records "(H_f) PROVED " while L2_011 row 13 (written the same day, earlier) still says "primitive witness CONDITIONAL on (Z-strip)". I follow the paper and the later index entry: PROVED. If (H_f) were to be downgraded, A8b becomes CONDITIONAL and A11 keeps its unconditional half (thm:famblind). Flagged. ✓
- **A8c.** NT_011 Thm 11.2 is confirmed by the review **with a restated class**: 𝓜 must not contain holomorphy of ξ̃ in the strip together with order-1 growth (ζ̃ has four off-line poles). With that fix the NO-GO is for the pointwise-(𝒱) step only. **It is not a window-form falsifier of WP_T**: no witness of 𝔞_T^{ζ̃} on P_T is computed. Clause split accordingly (PROVED for the step / ARGUED for WP_T). The scope sentence of NT_011 ("arguments that use the Euler product non-trivially are not covered") is kept in §3(e)4. ✓
- **A9.** rem:twohalves: "by Weil's criterion applied to these functions, their Weil forms take negative values" — a negative test F for the complete Weil form of Z_Q has compact support, hence lies in some L²(I_T), so W_T(F; Ξ_Q) < 0 at that T (complete form). The **primitive** bottom λ_A(T; Ξ_Q) is not shown negative (same gap rem:bar-fam notes for f_t). Clause labelled CITED (complete) / ARGUED (primitive). ✓ T2 of Paper 47 (Thm 18.16) concerns the Hodge-index inequality (18.2), a different form; it is cited only as the source of the falsifier Ξ_Q and of the A1–A6 axiom list. ✓
- **A10.** Paper 47 Thm 18.1 (T1) is proved there by transferring (18.2) for ξ_K to a statement about ζ_K that the stated rule excludes from use. I do **not** use that step. What remains is the transfer principle (a derivation from field-uniform properties is a derivation for every ξ_K), which is a tautology, plus an OPEN falsifier half. The index lists "F-ζ_K/S₃: falsifies equimodularity, non-abelian unitary routes" — those are falsifications of specific Paper-46 routes (Hodge transfer), not computed negative window bottoms. Clause honestly labelled CONDITIONAL / OPEN falsifier. ✓
- **A11 / W-fam.** thm:famblind: bounded J ⊂ (0, T₁], amplification at n₀ > e^{2T₁}; proofs of lem:monoT/lem:contA use only nonnegativity and finiteness of weights, so the modified family has the same qualitative properties. ✓ **Does not exclude bilateral laws**: rem:bar-fam says explicitly "this class is open"; R186_036 Thm 3(b) says unbounded J enters only through L ≥ 0. Stated in the clause and in §3(e). ✓
- **A12.** thm:nolocal: for fixed F ∈ P_T, F̂ entire nonzero, ∫_{U_T} σ_T\|F̂\|² < 0; truncation at η < κ makes the form negative; criterion returns the same answer for σ_T and σ^{(η)}; at T ≤ ½log5 the first is positive. ✓ Every window. ✓
- **A13.** lem:wh-T: the modified operator B′ has norm 1 so Φ(m(B′)) ≥ 1; moment distance ≤ k(1 − β₁); sandwich (eq:wh-sandwich) relates 1 − β₁ to λ_A/c_P. ✓ lem:wh-Tprime: the rank-one correction has bottom 0. ✓ thm:wh-detinherit(iii): D_* (1;T) = (1 − β₁)Π_*, so a leading term with ε₀ ≥ 1 is compatible with D_* = 0. ✓ Admissible splittings only (coercive 𝔭_*, trace-class 𝔫_*). ✓
- **A14.** cor:pattern is Lemma lem:transfer plus the numerical Remark rem:quartetnum; the proved part is thm:wit-model(iii) for large k with prop:quartetmodel's list. Labelled NUMÉRICO/PROVED split. ✓
- **A15.** prop:prog and N_021 Thm 2: deletion changes each ψ_a(x; q, c) by ≤ ψ(N), amplification by ≤ c, both o(x) and even O(1); closure ⇒ cor:void. ✓ For sieves: C_BT closed under deletion only; amplification not needed (A1 suffices for T > T₀(0)). ✓ b_θ (R167_102) covers "positivity + support + upper bounds" without finite modification. ✓
- **A16.** thm:poisson: Esseen on independent blocks R_k, band theorem thm:band necessary condition; P ≤ e^{−cT log T} for T ≥ T(c, κ). ✓ Random falsifier, PROVED. ✓
- **A17.** cor:void 𝒞_zeros: ζ_a = ζE, E entire zero-free, so every zero-location statement is kept; failing members are A1/A2. ✓ thm:finZ: any finite symmetric Z and any flat-top w: f_{w,Z} takes negative values (lattice Cesàro argument); does not locate τ. ✓ NT_014: forward PROVED, converse ARGUED — the clause "(b) is zero-information" is ARGUED; stated. ✓ L2_010 §3's own exponent bookkeeping is ARGUED; its load-bearing NO-GO is cor:void. ✓
- **B1.** thm:margin uses (Z1) (no zero with 0 < \|γ\| ≤ 21 other than ρ₁) and (Z2) (zeros to H_PT on the line), both CITED (Platt–Trudgian). This is zero information used for an **upper** bound on λ_A — allowed (it excludes nothing; it bounds what a proof must achieve). ✓
- **B2a.** L2_010 §1: Re[1/(½−ρ) + 1/(½−ρ′)] = 0 for the pair ρ, 1 − ρ̄ at τ = 0; so −2ζ′/ζ(½) = C₀ for every configuration. ✓ (Hadamard product and FE CITED.) ✓
- **B2b.** N_013 §1(c) requires convergence of the Riesz means; §2 (divergent alternative, exponential oscillation) is ARGUED; §3's (⇒) depends on it. Labelled CONDITIONAL. ✓
- **B2c.** L2_019 §4(b): Σ 4Λ(n)²/n over n < e^{2T} ≈ 8T² is Mertens-type (CITED); the "RMS ≥ 2T" is §1's Fejér bound (PROVED). ✓ "No fixed band can be discarded" relies on B2b (CONDITIONAL) — stated as such in (d). ✓
- **B2d.** thm:ceiling (resonator with ε = 1/(8M), Schur test) and thm:kappa(iv) (g₁(0) = C₀ + 4 < 0) are PROVED. ✓
- **B2e.** thm:wit-Tc(iv): equivalences are internal to D (monotonicity + continuity). ✓ Used only as "no weaker asymptotic sub-statement". ✓
- **B3.** L2_026 §1: ξ′/ξ(1 − s) = −ξ′/ξ(s) and reality give D_{1−σ} = −D_σ; D_{½} ≡ 0 off ordinates. ✓ Elementary. ✓
- **B4.** prop:opcalc / N_018 Thm 2: Plancherel per term, c_F vanishes for \|u\| ≥ 2T. ✓ Scope = finite complex Borel measures acting by convolution (shift-multiplier calculus). It does **not** cover non-convolution operators, nor SOS used without Cauchy–Schwarz (N_018 §3 says so). Scope stated. ✓
- **B5.** thm:sos: μ₀ ≥ sup of the comb polynomial = 𝖠_T (lem:mbounds(iii)); λ_{∞,P}(½log3) ≤ 0.311 < 0.980 ≤ v₂ ≤ 𝖠_T. ✓ Uses the value in cor:mono (archimedean, certified in the paper). ✓ Interval (½log2, ½log3) OPEN. ✓
- **B6.** prop:cone (ii)–(iii): explicit two-bump tests. ✓ prop:relative: bottom (1−θ)λ^♯ − θκ − C < 0 for large T by prop:sharp(iii). ✓ thm:posext: Fubini with ν ≥ 0 on {Φ ≤ 0}; the Gaussian-difference family is admissible; the numerical values κ_T(Φ) = −0.1377, −0.1284 are floating, not enclosed. ✓ prop:primeblind: almost periodicity. ✓
- **B7.** lem:flowdet is Jacobi + Hellmann–Feynman (PROVED); the barrier reading (coefficient dominated by ⟨A′h*, h*⟩/λ_A) is rem:bar-loc, ARGUED. thm:X(i) is an identity; the converse failure (M₁ satisfies X and is negative) is numerical. ✓
- **B8.** thm:Z (i) is an algebraic identity with eq:m; (ii) is Weil's explicit formula on h_τ = w cos(τ·) with absolute convergence — PROVED. Theorem E (L2_031): block-approximation argument using only continuity of B and Theorem S; PROVED; its review flags (B_Q) "kills exactly" as ARGUED but Theorem E does not depend on it. ✓ KEP dichotomy coincides with D except at λ_W = 0 (index 04_). ✓ All are internal restatements of D; none is used as anything else. ✓
- **Lemma I.** L2_011 §2 is a case analysis over the table; rows 17 (ζ_θ not re-verified), 18, 22 are flagged UNKNOWN there and here. ✓
- **Corollary (c).** The envelope inequality is lem:degen (PROVED). The 10⁻⁵ constants and the Near statistics are NUMÉRICO (double precision, uncertified). Fact N2 of EXP_003 is a zero-side observation (𝒞_zeros class), used only descriptively. ✓
- **Overall.** No clause uses any equivalence between row D and an external statement; the three places where the record's own argument would (T1, Epstein via Weil's criterion for Z_Q, Beurling via its explicit formula) are either restated as transfer-only (T1) or labelled CITED as statements about other objects. No sign contact; nothing in this memo moves λ_A(T) for ζ.
