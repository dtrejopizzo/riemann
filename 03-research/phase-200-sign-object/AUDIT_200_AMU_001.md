# AUDIT_200_AMU_001 — Audit of A_MU_FACTORIZATION_001 (phase 200, round 4)

Phase 200, pen and paper. Row D / L′♯ as independent goal.
Read: A_MU_FACTORIZATION_001; AUDIT_200_SPEC_003 (R-Q6, §7.2); SPEC_002 (T.1); Q2_LADDER_001 (Lemma R); Paper 47 §22
(def. of Z_log l.9615, thm:ext-half l.9651/9721, rem:ext-killing l.9669); README index, in particular l.463
(PROOF_L_SHARP_R_001), l.505 (PROOF_L_SHARP_MM_001), l.390 (INV_C_001) and l.407 (INV_T_001).

**Short verdict.** The inventory (a)–(e) holds up. Theorem D is notation. The "factorization" of Corollary F is a
sum-and-subtract of ε⁻¹‖Ψ̌‖², and convexity (Lemma F) plays no role in it. A_ε is not well defined on the quotient 𝒬_μ. The
deformation n ↦ n^ε is a Mellin shift already recorded as "do not retry" (l.463). **(f): NO-GO as
factorization.** Theorem D is filed as a notational identity.

---

## 0. Procedural failure: the index check was not complete

The memo states (§0) that "no entry writes Z_log as a derivative of a norm along n ↦ n^ε." That is false.

- **l.463, PROOF_L_SHARP_R_001.** R.1 (PROVED, AUDIT_16) writes the form as a "derivative in the exponent of the
  partial sums, s fixed": Θ_∞|F|² − 2Re(F̄F_log) = |ζ|²∂_u|Φ(s,w)/ζ(w)|². Differentiating in the exponent of the Dirichlet
  coefficients is exactly changing the weight n^{−w} to n^{−w+ε}, i.e. n ↦ n^ε. R.2 classifies it as REF-D. And the
  record literally says: **"Do not retry: σ-derivatives in the Mellin variable."**
- **l.505, PROOF_L_SHARP_MM_001.** The exterior loop Z over the leak tail is LOSSLESS on the line, by
  ∂_σ|Γ_ℝζ|² = 0 (mechanism ES-19). The strict margin is the truncation energy = W_T, and that is circular. R-F2 is this
  same observation, renamed.
- **l.390 (INV_C_001):** "exact Λ only via ∂_σ log of the h⁰ density." **l.407 (INV_T_001):** ∂_σ log|q| at σ = ½.

Every search the goal requires ("σ-derivative", "∂_σ", "ES-19", "Mellin") returns hits that the memo does not cite. By rule
(f) it needed a new written reason against l.463 and l.505. The reason given, (i)–(iii), does not mention them. The
only element that could be different is the cutoff at (T,∞), and MM_001 has already identified it as "truncation energy = W_T,
circular" (§2).

---

## 1. Theorem D: verification and status

**Computation (correct).** With h_n(y) := e^{y/2}r(ne^y),
- Z^{(ε)}r = Σ_n n^ε h_n;
- ∂_εZ^{(ε)}r|₀ = Σ log n·h_n = Z_log r (Paper 47 l.9615; the term n = 1 contributes log 1 = 0, so it coincides with the
  sum from n ≥ 2 in the paper);
- F_r′(0) = 2Re⟨Zr, Z_log r⟩ = 2⟨Ψ̌, Z_log r⟩ for real r.

Substituted into thm:ext-half (l.9721) this gives (2.2). Identity (2.3) is correct: from log(ne^y) = log n + y one gets
Z_log r = Z(log ξ·r) − yZr, and hence −F′(0) = 2⟨Ψ̌, yΨ̌⟩ − 2⟨Ψ̌, Z(log ξ·r)⟩. The uniform convergence for |ε| < ½ with
r = O(ξ⁻²) is correct.

**Status: notation, not a new identity.** The term −2⟨Ψ̌, Z_log r⟩ of thm:ext-half is rewritten as −∂_ε‖Z^{(ε)}r‖²|₀
because ∂_εn^ε = n^ε log n. That is the chain rule applied to the definition of Z_log. There is no additional
arithmetic content.
- The phrase "Λ*1 = log ⟺ the prime term is ∂_ε of a norm" is misleading. Any term of the form
  −2⟨Zr, Z_w r⟩ with weights w_n = log n is an ε-derivative, and the convolution with Λ has already been spent in rem:ext-killing(ii) before
  writing (1.0).
- The "semiring" (log(nξ) = log n + log ξ) only contributes (2.3). It is the trivial change-of-variable identity ξ = ne^y, already
  present in Paper 47 l.10343 ("For Z_log use log n = log b + log k").
- **Label:** PROVED (given thm:ext-half) **as rewriting**. Precedent: AUDIT_19 on M1 ("I1 renamed, nothing is actually varied").

---

## 2. Lemma F and Corollary F

### 2.1 Convexity is not automatic

F_r(ε) = ∫_T^∞|Σ_n n^ε h_n|² = Σ_{m,n}(mn)^ε G_{mn}, with G_{mn} := ⟨h_m, h_n⟩_{L²(T,∞)}.

- It is a sum of exponentials e^{ε log(mn)} with real coefficients G_{mn}.
- **Sufficient condition (PROVED):** if G_{mn} ≥ 0 for every pair, F is log-convex in ε (sum of exponentials with
  positive weights), and in particular convex.
- **In general there is no convexity.** If G has negative entries, F″ = Σ(log mn)²(mn)^εG_{mn} can be negative. For Mori's
  r*, which changes sign, nothing guarantees it.
- The memo's claim "the first term is ≥ 0, the second has no sign" is correct. Lemma F is, therefore, a
  positive-correlation condition on the dilates, not a "three-lines type" convexity.

### 2.2 The ε deformation is the Mellin shift σ = ½ + ε

By (2.1) of the memo itself, Z^{(ε)}r = e^{−εy}Z(ξ^εr). Multiplying r by ξ^ε shifts its Mellin transform by one unit ε in σ. On the
full line, the memo itself obtains F(ε) = (1/2π)∫|ζ(½ − ε + it)|²|R(t)|²dt. **Yes: it is moving the line.** That is exactly
F4/ES-19 (∂_σ|Γ_ℝζ|² = 0 plus the collapse of the comb) and the l.463 class ("σ-derivatives in the Mellin variable").

The cutoff at T is likewise not a new object:
- in (2.1), the cutoff introduces the weight e^{−2εy}1_{(T,∞)};
- its derivative at ε = 0 is 2⟨Ψ̌, yΨ̌⟩, which is nothing other than the truncation defect of the reflection σ ↔ 1−σ;
- it is the "truncation energy = W_T" of MM_001 and the aliasing tail B.1.a.

R-F2 confirms that all the content is in that cutoff, and that cutoff is already recorded as circular.

### 2.3 Corollary F is a sum-and-subtract, not a factorization

Corollary F writes 𝒲 = ‖A_εr‖² − ℰ_ε + Δ_ε. If the terms are combined without sign, the exact decomposition with
ℰ_exact := ℰ_ε − Δ_ε is
 ℰ_exact = ε⁻¹F(0) + F′(0) = ε⁻¹‖Ψ̌‖² + 2⟨Ψ̌, Z_log r⟩,
 ‖A_εr‖² − ℰ_exact = 𝒜 + 2AB − 2⟨Ψ̌, Z_log r⟩ = 𝒲.

**F(ε) disappears entirely.** The "factorization" is 𝒲 = (𝒜 + 2AB + ε⁻¹‖Ψ̌‖²) − (ε⁻¹‖Ψ̌‖² + 2⟨Ψ̌, Z_log r⟩), i.e.
adding and subtracting a multiple of the norm.
- The positivity of ℰ_exact is the Cauchy–Schwarz bound ⟨Ψ̌, Z_log r⟩ ≥ −‖Ψ̌‖²/(2ε) and needs no convexity.
- Lemma F only serves to replace ℰ_exact with the bound ε⁻¹F(ε), which is larger and leaves 𝒲 ≥ (something). **It is a bound, not an
  exact identity**, and it violates the operational definition of AUDIT_200_SPEC_003 §7.2 ("exact identity 𝒲 = ‖A_μr‖² − ℰ_μ with
  ℰ_μ ≥ 0").
- With the exact version, the condition ‖A_εr‖² ≥ ℰ_exact is literally 𝒲 ≥ 0. There is a free parameter ε and no
  new information. It is class C8, the "cancelling basis", with a scalar spectral translation in place of a basis.

**Minor correction.** "𝒜 + ε⁻¹‖·‖² PSD for ε < 1/5.372" is correct with m ≥ m(0) = −5.372 (m even and increasing for t > 0), but
it is trivial. Any form bounded below becomes PSD by adding a large constant.

### 2.4 A_ε is not defined on 𝒬_μ (domain failure)

The goal requires A_μ: 𝒬_μ → ℋ, i.e. A_μ must vanish on the radical/gauge 𝒢̄_T. For radical φ, 𝒲(φ) = 0 (Guo L4.4,
prop:ext-gauge), but ‖A_εφ‖² ≥ ε⁻¹‖Zφ‖² + O(‖Zφ‖²) > 0 as soon as Zφ ≠ 0. Hence ℰ_exact(φ) = ‖A_εφ‖² > 0, and the
decomposition does not descend to the quotient.

**Label:** ARGUED. It remains to verify that the gauge of prop:ext-gauge has Ψ̌_φ ≠ 0 on (T,∞). AUDIT_200_SPEC_003 l.33–36
indicates that Φ_φ has Mellin transform ζ𝓜φ, not zero in general. If confirmed, (f) also dies by domain failure.

---

## 3. Class 𝒦_H / constraint 11

- Lemma F, as stated ("for every r in the image of the admissible f's"), is evaluated at a generic r. It is not a flow
  evaluated at the minimizer: **it passes constraint 11**.
- But the proposed test F₀ (§7) evaluates F″ only at r*. If it were stated as "F″_{r*} ≥ cℓ*" as a working hypothesis, that
  would indeed be a derivative in a parameter evaluated at the minimizer: **REF-D** (H_001, constraint 11).
- Moreover, by §2.3, no version of Lemma F, generic or at r*, changes the content of 𝒲 ≥ 0. The point is already settled
  against (f) by another route.

---

## 4. R-F1 and R-F2

**R-F2: PROVED, but not new.** It is F4 + ES-19 + MM.1 (l.505: "lossless loop on the line via ∂_σ|Γ_ℝζ|² = 0") and R.2
(l.463). Recorded as a duplicate.

**R-F1: PROVED in its weak form, but nearly tautological.** (1.0) contains only the weights log n, so any functional
built on (1.0) sees only log n.

Two corrections:
- **The cΛ example is incorrect.** "2Λ*1 = 2 log" is true but irrelevant. In the cΛ system, the counting comb is d_c (the
  coefficients of ζ^c), not 1, and the identity feeding rem:ext-killing(ii) would be cΛ*d_c = log·d_c. For c = 2, (1.0)
  changes shape: the comb Z gets weights d_2(n) = τ(n). The formal analogue is not "(1.0) at double speed".
- **The Beurling case** is correct: Λ_B*1_B = log_B is the definition of the system, and the form (1.0) is the same over ℕ_B.

**Tension with R-Q6: apparent, resolved as follows.**
- R-Q6 says that *descent* (identifying the radical 𝒢̄_T) uses the exact Λ, via Guo L4.4: Φ_φ is radical because its Mellin
  transform ζ𝓜φ vanishes where the exact-Λ explicit formula demands.
- R-F1 says the *quadratic form on representatives* only sees Λ*1 = log.
- They do not contradict each other. The exact Λ lives in **which the null subspace is**, not in **the coefficients of the form**.
- Operational corollary: **an A_μ that sees the exact Λ must vanish on 𝒢̄_T by construction.** That is precisely the
  property A_ε fails to satisfy (§2.4).

---

## 5. Inventory (a)–(e)

- **(a)** Correct: σ ≡ 0 off the ordinates by F4. Fejér–Riesz on a null function is empty. NO-GO PROVED (given F4).
  Duplicates l.463/R.2 and MM.1, which should have been cited.
- **(b)** Correct as reclassification: C8 + thm:shape + G0 (l.255). NO-GO.
- **(c)** Lemma C.1: correct, but trivial. rad_μ = id on integers with no factors < μ is the definition. "𝔇 preserves the
  radical" is Lemma R step 3. NO-GO PROVED (given Guo L4.4). The phrase "𝒲(KΨ̌) depends on KΨ̌ only modulo the image of 𝔇 over
  Z_g" is poorly stated: it should say "modulo 𝒢̄_T". This does not change the verdict.
- **(d)** Correct: ℰ ≥ 0 ⟺ w ≥ mass at zeros, which is REF-D. D_μ(ρ) = −1 (SPEC_002 §A.2) ✓. NO-GO.
- **(e)** Duplicate of SQ ✓. The scale O(1) against 10⁻⁷⁰ violates P2 ✓.

---

## 6. Verdict and what remains for A_μ

| item | auditor's label |
|---|---|
| (a)–(e) | NO-GO confirmed ((a) duplicates l.463/l.505) |
| Theorem D | PROVED as **notation** (chain rule on the definition of Z_log); not a new identity |
| Lemma F | OPEN, but **irrelevant**: convexity ⟸ G_{mn} ≥ 0, false in general for r that changes sign |
| Corollary F | **NO-GO as factorization**: sum-and-subtract of ε⁻¹‖Ψ̌‖²; the exact version does not use F(ε); the version with F(ε) is a bound |
| A_ε on 𝒬_μ | does not descend (ARGUED, verify prop:ext-gauge) |
| n^ε deformation | = Mellin shift σ = ½ + ε; falls under "do not retry" of l.463 |
| R-F1 | PROVED (nearly tautological); c = 2 example corrected |
| R-F2 | PROVED, duplicate of MM.1/R.2/F4 |
| **(f)** | **NO-GO** (as factorization); Theorem D is filed as rewriting |

**On the F₀ test.** No result of F₀ rescues (f), because F(ε) does not enter the exact identity (§2.3).
- F″_{r*}(0) < 0: confirms Lemma F is false. This is the expected result, because G_{12} = ⟨h_1, h_2⟩ inherits the sign
  change of r* ((1,2) resonance, AUDIT_16 §6).
- F″_{r*}(0) ≥ cℓ*: would give an inequality at the minimizer, which is REF-D (§3).
- **Recommendation: do not run F₀ as a test of (f).** As an isolated datum, the sign of G_{12}(r*) can be noted in the grid,
  given its low cost, but not as a survival test.

**What remains for A_μ, given R-F1 and §4.** Concretely, any future candidate must satisfy, **before** any
computation:
1. **Exact vanishing on 𝒢̄_T** (descent). This is the only place where the exact Λ enters. There are two descriptions of the radical:
   - that of Guo L4.4 via zeros of ζ is REF-D;
   - the only non-REF-D one is that of Poisson over ℕ (SQ.0 / Lemma R: additive characters e(jN/k), Ramanujan sums c_k(N)).
   Hence A_μ must be built as a composition A_μ = B ∘ Π, where Π is a projector or quotient **given by the Ramanujan/Poisson
   relations of the radical** (not by zeros) and B is a fixed-norm operator. The object to build is Π, explicit
   in the Selberg y_k basis or in c_k(N). This distinguishes it from (e), which uses y_k as coordinates and not as quotient
   relations.
2. **Exact identity** with explicit ℰ and no free parameter that could absorb 𝒲. If ℰ = ℰ(ε) admits arbitrary ε, it is a
   sum-and-subtract and does not count.
3. **Leak scale** (P2): the pieces must be O(ℓ), not O(1).
4. **Alternative outside the exterior form: the window core**, where Λ appears as individual v_n and not via Λ*1. There
   the P10-formula is attainable for c = 2 and Beurling, but one must pass the walls W-lin…W-mom (l.50) and constraint 7 (S.4).
   Lower priority than point 1.

**Recommendation to the coordinator.** Next round: "Ramanujan quotient operator Π_μ". Define explicit Π_μ from
SQ.0, prove Π_μ(𝒢̄_T) = 0 (given Guo L4.4), and only then look for B. Before building, search the index for "Ramanujan",
"c_k(N)", "Poisson over ℕ" and "quotient".

---

## 7. Entry for the index (corrects line 521 of the README)

- **AUDIT_200_AMU_001 (auditor of A_MU_FACTORIZATION_001):**
  - (a)–(e): NO-GO confirmed. (a) duplicates l.463/l.505.
  - Theorem D: PROVED as notation (∂_εn^ε = n^ε log n applied to the definition of Z_log); not a new identity.
  - Corollary F: **NO-GO**. The exact identity is 𝒲 = (𝒜 + 2AB + ε⁻¹‖Ψ̌‖²) − (ε⁻¹‖Ψ̌‖² + 2⟨Ψ̌, Z_log r⟩): add and subtract,
    F(ε) plays no role. The version with F(ε) is a bound, not a factorization.
  - Lemma F: convex ⟸ ⟨h_m, h_n⟩ ≥ 0, not automatic; irrelevant.
  - n^ε = Mellin shift σ = ½ + ε: falls under "do not retry σ-derivatives in the Mellin variable" (l.463). The cutoff at
    T is the truncation energy of MM_001 (circular).
  - A_ε does not vanish on 𝒢̄_T (ARGUED), hence it is not defined on 𝒬_μ.
  - R-F2 duplicates MM.1/R.2. R-F1 PROVED (nearly tautological); the c = 2 example is wrong (comb d_c, not 1).
  - R-F1/R-Q6 tension resolved: the exact Λ lives in the null subspace, not in the coefficients. Every A_μ must vanish on
    𝒢̄_T via the Poisson/Ramanujan relations (not via zeros).
  - F₀ does not rescue (f): do not run as a test.
  - Do not retry: n^ε deformations / Mellin shift of the exterior comb, nor factorizations by sum-and-subtract of ε⁻¹‖·‖².
  - L′♯ OPEN. Row D OPEN.

---

## Summary (≤200 words)

The inventory (a)–(e) holds up, although (a) duplicates PROOF_L_SHARP_R_001 (l.463) and MM_001 (l.505), which the memo's index
check omitted.

Theorem D is correct, but it is notation: the chain rule applied to the definition of Z_log. The semiring only contributes
the change of variable already present in Paper 47.

The n^ε deformation is, by (2.1), the Mellin shift σ = ½ + ε. It falls under "do not retry σ-derivatives in the
Mellin variable", and the cutoff at T is the circular truncation energy of MM_001.

Central failure: the exact identity of Corollary F is 𝒲 = (𝒜 + 2AB + ε⁻¹‖Ψ̌‖²) − (ε⁻¹‖Ψ̌‖² + 2⟨Ψ̌, Z_log r⟩). It is a
sum-and-subtract in which F(ε) and Lemma F play no role. The version with F(ε) is a bound, not a factorization. Moreover, A_ε does not
vanish on the gauge 𝒢̄_T (ARGUED), so it is not defined on 𝒬_μ. Finally, the convexity only holds if the dilates
have positive correlation, which does not happen in general.

R-F1 PROVED (nearly tautological; the c = 2 example is wrong). R-F2 is a duplicate. The tension with R-Q6 is resolved as follows: the exact Λ
lives in the radical, not in the coefficients.

**(f): NO-GO.** F₀ does not rescue it. Next object: a quotient projector Π_μ defined by the
Poisson/Ramanujan relations of SQ.0, with Π_μ(𝒢̄_T) = 0, and only afterward B.

L′♯ OPEN. Row D OPEN.
