# Annex — Primary-source reading of the semilocal Sonin chain

Reading note. Nothing is built. The only own verifications are short and carry the label ARGUED.
Paths relative to `03-research/`.

## 0. Four-point filter (reading annex)

1. **Closest antecedent.** The Sonin trace identity `E_S = Son + R_{S,T}` (R183_018 §3, Prop 3.1), its
   semilocal form `(84)_S` (R186_015) and the decomposition of `W_T` from PROOF_L_SHARP_D_001 Thm 2.1. All were read in primary sources.
2. **New object.** None. This annex only reports.
3. **Difficulty avoided.** Not applicable.
4. **Connection with the global sign.** §6 assesses whether any statement about the remainders is left that is not in a closed
   class. The answer is negative.

## 1. (Q1) Sonin/concentration-type identities in the corpus

**(I-1) Archimedean Sonin trace, level (1,1).** R183_018 §1 and §3, Prop 3.1, `PROVED` from CC Thm 4.7 `CITED`.
- **Transform:** `F = F_{e_R}`, even Fourier on `L²(R)^ev`.
- **Constraint:** `Π = projection onto S(1,1) = {ξ = 0 on |q| ≤ 1, Fξ = 0 on |p| ≤ 1}`, the eigenvalue-1 part of `P P̂ P`
  (CC (72), (81)).
- **Positive form:** `Son(h) = Tr(ϑ(g)Πϑ(g)*) = ‖Πϑ(g)*‖²_HS ≥ 0`. It is exactly of the form `‖Q U F‖²`.
- **Carrier and set S:** `h ∈ C_c^∞(I_T)`, without moment condition, for all `T` and all `S ⊇ {∞} ∪ {p < e^{2T}}`.
- **Identity:** `E_S(h) = Son(h) + R_{S,T}(h)`, with
  `R_{S,T}(h) = −∫_{−2T}^{2T} c_h(x) ε(e^{|x|}) dx − Σ_{p<e^{2T}} 2 log p Σ_{k log p<2T} p^{−k/2} Re c_h(k log p)`.

**(I-2) Form with the kink separated.** PROOF_L_SHARP_D_001 Thm 2.1, `PROVED` given CC Thm 4.7.
- **Carrier:** real core `C²_c(I)`, extended to `E(core)` by density.
- **Identity:** `W_T(g) = Son_{1,1}(g) + 2ε′(1⁺)𝔅(g) − ⟨g,K_s g⟩ − ⟨g,C_p g⟩ + 2Re(A(g)B̄(g))`.
- **Matrix form (Cor 2.2):** in the prolate basis, `𝔐 = 𝔖 + 2ε′𝔅 − 𝔎 − ℭ + 𝔓`.

**(I-3) Semilocal chain for any finite S.** R186_009 (S = {∞,2}) and R186_015 (general S), status table.
- **Transform:** `F_S = E_S F_∞ E_S^{−1} = I·m_∞(D)·U_S(D)`, with `U_S = e^{iφ_S(D)}` and
  `φ_S′ = −Σ_p Σ_k v_{p^k} cos(kt log p)`.
  - It is unitary, involutive and self-adjoint, and satisfies `F_S ϑ(ρ) F_S = ϑ(ρ^{−1})` (U_S, L0: `PROVED`).
- **Constraint:** `Π_S = Q₁ ∧ Q₂`, with `Q₁ = 1−P` and `Q₂ = 1 − F_S P F_S`. It is a Riesz projection with a gap
  (R186_009 G, D: `PROVED`).
- **Identity (84)_S:** `Tr ϑ(f)Π_S = W_∞(f) − Σ_{p∈S} comb_p(f) + ∫ f(ρ^{−1}) ε_S(ρ) d*ρ`. It is `PROVED` given CC Thm 4.7
  (R186_015, rows C′_S and (84)_S). The prime comb comes out exact and separated:
  `Tr ϑ(h)(P̂^S − P̂_∞) = Σ_p Σ_k (log p) p^{−k/2}(h(p^k) + h(p^{−k}))`.

**(I-4) Semilocal−archimedean difference.** R183_033 §1.1, `PROVED` (029 + 025):
`Son_S − Son_∞ = exact prime term + ∫ c_h ε′_p + (1/2π)∫ |φ|² r_p`.

**(I-5) Concentration identity on the Sonin annulus.** PROOF_L_SHARP_U_001.
- U.2.1, `PROVED` in L²: `ℓ(g) = λ‖Πρ‖²` and the datum lives in `𝒱_μ = 𝒮(1,1)⁺ ⊖ 𝒮(1,μ)⁺`.
- U.3.1, `CONDITIONAL` (closability C1 and radical lemma C2): `𝔔 = 𝒲_refl[σ_+] − 𝒲_refl[σ_−] + E`.
- U.1.3: the minus sector contributes a forced −SOS. Label REF-D.

**Remainder terms.** The sources are in (I-2) and in R183_018 §4–5.

| term | origin | sign | size as T grows |
|---|---|---|---|
| `2ε′(1⁺)𝔅(g)` | **boundary of the Sonin window**: the shell `λ/ρ < |x| < λ` gives the kink at ρ = 1 (D_001 Prop 2.3) | `≥ 0` on `∫g = 0` (𝔅 = ‖G‖²) | at level 1, `ε′(1⁺) ≈ 22.9965` is constant (CC Lemma 5.4 `CITED`); at level `λ = e^T`, `2ε′_λ(1⁺) ≍ μ^{O(1)} e^{4πμ}` (D_001 Prop 2.3 `PROVED`); the leakage weights enter inverted (`D^{−1}`) |
| `−⟨g,K_s g⟩` | smooth part of ε: prolate/leakage cross terms `λ_n(1−λ_n²)^{−1/2}⟨ξ_n|ϑζ_n⟩` | **no sign**; it is Hilbert–Schmidt and compact | in the record, ε only up to ρ ≤ 3 (R186_022); the number of eigenvalues above the Sonin floor grows with T (R186_013 NUMERICAL/ARGUED; R183_026 #{λ(K_{I_T}) > 1} ≈ 4T−2 NUMERICAL) |
| `−⟨g,C_p g⟩` | arithmetic: the primes with `k log p < 2T` | **indefinite**: measurable sum of trace-zero Toeplitz `T_n(σ_p)`, with ± spectrum of infinite multiplicity (R183_018 Prop 4.1 `PROVED`) | appears as soon as `T > ½log 2`, and with it `n₋(R_{S,T}) = ∞` (R183_018 Thm 5.1 `PROVED`) |
| `𝔓 = 2Re(AB̄)` | **gauge** (Tate moments, pole) | indefinite, of rank 2 | vanishes on `P_T` |
| `ε_S − ε_∞ = κ_S` | **finite S**: semilocal angle/compression correction | no sign | `∈ L^p_loc` and `R′_S` is HS for fixed S (`PROVED`); `log^r` singularities at all S-units. For S = S(T): comb at all integers, singularities of type `1/|ρ−n|`, **not uniform in T** (R186_015 row S(T), ARGUED) |
| archimedean cutoff | `ε` truncated to `|a| < 2T`; the symbol `ρ_T = m + ε̂_T` | **is not ≥ 0** (R186_022, NUMERICAL; `ρ_T(0) = −2.36` at ½log3) | — |

## 2. (Q2) What «PROVED for every finite S, without sign» means

**What is proved for finite S** (R186_015 table, rows U_S through M_S):
- `F_S` is unitary and involutive.
- `A_S = P F_S P` is compact, with `‖A_S‖ < 1`; it is not HS and lies in `S_p` for all `p > 2`.
- TC_S and C′_S hold (exact comb).
- (84)_S holds.
- `κ_S ∈ L^p_loc` and `R′_S` is HS on `L²(I_T)` for all T, with S fixed.

Index 04_PHASES l.123: «PARTIAL (PROVED ∀S; no sign) | remainder inertia in P_T OPEN».

**Why it does not give the sign.** The identity is `E_S = Son_S − C_{ε_S}`. That `Son_S ≥ 0` holds by construction, and it holds equally
for every involution F with `FϑF = ϑ^{−1}`. D_001 Thm 4.1 and Cor 4.2 (`PROVED`) show that `Son_c ≥ 0` exists for cΛ with
any real c, for per-prime exponents `c_p` and for deleted primes (`c_p = 0`). Sonin positivity therefore exists for
the whole family of falsifiers. The sign remains entirely in `Son_S ≥ C_{ε_S}` on `P_T`, which is the inertia
`N_T` of the remainder: OPEN (R183_028 §3.2; R183_033 §4).

**Is semilocal positivity proved, open or false for finite S?**
- **Fixed S not containing all `p < e^{2T}`:** it fails.
  - S = {∞}: one negative direction from T ≈ 0.596 and two from 0.80 (R183_026 §3, R183_033 §2; NUMERICAL not certified).
  - S = {∞,2}: breaks at T ≈ 0.567 (R183_033 §2, NUMERICAL).
- **S = S(T):** coincides with a_T.
  - For `T ≤ ½log5`, `PROVED` given Paper 46 (R183_030 Prop 3.1; `CITED`), with a gap ≥ 6.25e-13‖ξ‖².
  - Beyond, OPEN.
  - Up to 0.80, `n₋ = 0` is NUMERICAL, with a gap that falls superexponentially.

**The step S → all primes.** It is never needed within a window: by support only the `n < e^{2T}` act
(R183_018 Prop 3.1; R183_001 Thm 1). What fails is the **uniformity in T** of the family S(T). The constants contain
`∏_{p∈S}(1−p^{−1/2})^{−1}` and `Ψ_S`, which diverge. The predicted limit is a comb of integers with singularities `1/|ρ−n|`
(R186_015 Verdict, ARGUED).

## 3. (Q3) Coincidence in the finite window

**Yes, it is stated and used.**
- R183_030 §1.1: «With S = S(T) one has W_S = W_T, Paper 46's Weil form», with `S(T) = {∞} ∪ {p^k < e^{2T}}`. Label
  PROVED, bookkeeping.
- R183_018 Prop 3.1 requires `S ⊇ {∞} ∪ {p < e^{2T}}` precisely for that reason.
- R183_018 §6, caveat (ii), and R162_2602 Thm 4(b): every proof must use that S contains **all** `p < e^{2T}`.

**How the semilocal object differs from a_T in the window:**
- (a) **Complete Euler factors.** `F_S` and `Π_S` use `∏(1−p^{−s})^{−1}` untruncated (R186_015 §1). In the form only
  the `k log p < 2T` survive, by support. In the positive part and in the remainder, by contrast, the complete tail enters: `Son_S`
  and `ε_S` separately **do** see the powers `p^k > e^{2T}`. Only their difference does not see them.
- (b) **Carrier and gauge.**
  - CC work in the variable ξ (`h = (½−∂)ξ`), which imposes a single Tate moment.
  - `P_T` imposes two: R183_030 §1.1 and §1.2. On `P_T` the polar terms vanish.
  - D_001 §1: the admissibility conditions `f(0) = f̂(0) = 0` are those of CC (93) and not those of Sonin.
- (c) **Level.** The Sonin trace is at level `λ = 1`. The complete identity at level `λ = e^T > 1` depends on the
  dictionary D3 (R186_017), which is OPEN for `λ > 1` (R186_099; D_001 §5, CONDITIONAL).
- (d) **The positive part changes with T.** `Son_{S(T)}` grows in S with T, so the «finite-S» family is not a single fixed
  positive form.

## 4. (Q4) The three controls against each term

**What the memos say.**
- D_001 Thm 4.1 and Cor 4.2 (`PROVED`):
  - For cΛ and for the deletion of a prime, the identity does **not** fail.
  - `Son_c ≥ 0` stays the same; the comb becomes `c·comb`.
  - The failure (λ < 0 certified for c > 1 at T = 1 and at ½log5, CERT_FALSIFIERS_001) lives **inside**
    `C_{ε_c} = 2ε′_c(1⁺)𝔅 − K_s^{(c)}`.
- D_001 Prop 3.1: `𝔖, 𝔅, 𝔎, 𝔓` are blind to the comb and `ℭ` is linear in it. The barrier (B_001 Lemma 4.1) excludes every proof
  of the type «positive pieces + TV-robust bound of `𝔎 + ℭ`».
- U_001 §4:
  - With cΛ, the sector formula and C1 break with a defect linear in `(1−c)` (PROVED algebra).
  - With `a_P` the same happens (ARGUED).
  - With Beurling there is no Poisson nor `𝔉_μ`; U.2 survives.

**Own analysis (ARGUED), term by term:**

| term | cΛ, c = 2 | deletion of a prime power | Beurling-type weight |
|---|---|---|---|
| `Son_S` | exists and is ≥ 0 (Cor 4.2, PROVED); **blind** | exists and is ≥ 0 (`c_p = 0`, PROVED); **blind** | ARGUED: `F = I m_∞(D) e^{iφ(D)}` with φ odd is still a unitary involution with `FϑF = ϑ^{−1}`; the Halmos construction applies; **blind** |
| `2ε′(1⁺)𝔅` | the kink changes value, `ε′_c(1⁺) = Σ χ_n ψ_n(λ)²/D_n` with prolates of `F_c`; still ≥ 0 on ∫g = 0; does not change sign | same | same |
| `K_s`, `κ_S` | change nonlinearly in c, because `Π_c` is not linear in c; have no sign either before or after; the failure hides here | same; deletion removes the singularities of `ε_S` at the S-units involving p | the singularities move to the Beurling «S-units», in general dense and non-integer; no sign change of an individual term is seen |
| `C_p` | doubles; indefinite before and after | loses a Toeplitz block; indefinite | indefinite |

**ARGUED conclusion.** No individual term changes sign under the controls. The terms with a sign (`Son`, `𝔅`) are
blind. Those that see the control (`K_s`, `κ_S`, `C_p`) have no sign. The identity is valid for the three controls, so
it does not break. This contradicts the premise of the reverse argument («U unitary only for the true integers»): the U of the
corpus, `F_S`, is unitary for any odd symbol φ (R186_015 U_S; D_001 Thm 4.1(a)).

## 5. (Q5) Why these phases were stopped

- **Complete Sonin trace (η = 0).** NO-GO `PROVED` (R183_018 Thm 5.1; R183_019 Thm 4.1; R183_020).
  - Class: «complete Son + remainder with a finite number of negative directions».
  - Explicit falsifier: pairs `β(t−t_j) + β(t−t_j−log 2)` with `n₋ = ∞`.
- **η uniform in T, (L-Son).** False, CONDITIONAL on an external spectral hypothesis (R183_027; R183_028 §2).
- **W-Sonin.** Index 04 l.35; R183_031 Thm 1; R183_033.
  - Class: multiplier positive part with remainder of bounded inertia for all T.
  - Result: the limiting density ends up supported on the spectrum; it converges to the explicit formula. NO-GO.
- **W11′.** R184_015 Theorem 2 and Cor 3, `PROVED`.
  - Class: every decomposition `W_T = Pos_S + Δ_T` with `‖Δ_T‖ = e^{o(T)}`.
  - If Δ is defined from the source, it is blind to the falsifier `M_m`. If it is defined from the form, it is REF-D.
- **Single-mode alignment.** FALSIFIED, NUMERICAL (R186_023 Status, §2).
  - Class: fragile archimedean mode + prime phases.
  - Falsifier: `M(T) = W[h_a]` fails against `λ_min` by factors of up to 10^10 at ½log5, and the required rank grows
    with T.
- **ρ*(T).** R186_021, NUMERICAL: it rises by collapse of `Son_S`, not by C.
  - Class closed by Lemma H (iv) (R186_029 §1, `PROVED`): `1 − ρ* ≤ λ_A/λ_min(Son_S|P_T)`, inherits the margin.
  - R186_022: the truncated symbol is not ≥ 0. NO-GO for pointwise symbol arguments.
- **Walls.** Index 04 l.38–43:
  - **W-lin:** linear certificates in a fixed basis, congruence, Schur, inertia or norm bounds. Reason: they do not decide
    a new window (R186_029–031).
  - **W-det:** every determinant that decides the sign factors as `λ_A·R` (R186_034 Thm 3.1).
  - **W-fam:** functionals of `{λ_A(T′)}`. Bounded falsifier `f_t` (R186_036 Thm 3).
  - **W-pat:** window observables. Falsifier: the quartet model `M₁`, which coincides on all observables and is
    negative (phase 187).
  - **W-loc:** local or finite-rank criteria on `σ_T`. Falsifier `σ^{(η)} = min(σ_T, η)` (R186_043/044).
  - **W-mom:** finite moments. Margin `≤ k(1−β_max)` (R186_045 Lemma T/T′).
- **Theorem X** (R186_045 §2.2). `PROVED` as a reformulation.
  - As a datum from σ: OPEN.
  - It is blind to the class: `M₁` satisfies it under its contact and `f_t` coincides with ζ up to ½log λ₁.
- **Phase 199.**
  - D_001: NO-GO as a citation route.
    - Prop 3.1: the positive pieces are blind to the comb. Falsifier `ν′ = ν_Λ + mδ_{u_0}`.
    - Cor 4.2: the falsifier cΛ lives in `ε_c`.
  - U_001: REF-D. The minus sector is a forced −SOS.
- **Phase 158** (R158_005 §1, §3). Every positivity structure examined on the adèle class space is a
  reformulation, a compression, blind to zeros, false or empty. Label RESTATEMENT. MW-5 is left without an object.

## 6. (Q6) Own assessment (separate from the above)

I find no precise statement about the remainders that nobody has attempted and that does not fall into a recorded class.

- Every sign statement on `C_{ε_S}` against `Son_S` on `P_T` is `N_T`.
  - As a norm bound or bounded-inertia bound, it falls into W11′ or W-Sonin.
  - As an exact inequality, it is REF-D.
- The «blindness» of `Son` to the controls (D_001 Cor 4.2) prevents the Sonin positive part from carrying the sign, whatever
  S is.
- The only thing open and not closed is sign-free:
  - the boundedness (B) of `ε_S` (R186_009);
  - the non-uniformity of `κ_{S(T)}` (R186_015 row S(T), ARGUED);
  - the dictionary D3 for `λ > 1`.

  Proving them would give identities, not positivity. The reverse-engineering argument about «U unitary only for the true
  integers» does not hold for the U of the corpus. An object with that property would have to be different from `F_S`. For it there is
  no written antecedent in these phases, and I do not propose it here.
