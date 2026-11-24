# Cross-check annex — near-null directions of a_T on P_T and window in c

Cross-check prior to any construction. Nothing new is derived or computed; what the corpus already
contains is located and reported with its label. Notation of `ROUND_006_WINDOW_SPLIT_NUMERIC.md`: a_T = Arch − Π,
Π(F) = Σ v_n c_F(log n), a_T^{(c)} = Arch − cΠ, Φ_T(c) = ground value of a_T^{(c)} on the unit sphere of P_T.
Paths relative to the repository root; "211/" = `03-research/phase-211-sign-sandbox/`, "P46" =
`04-papers/46-row-d-sign-radial-intersection-form/main.tex`, "P48" = `04-papers/48-routes-to-weil-positivity/main.tex`, "IDX" =
`05-meta-and-planning/ROUTES-TRIED-INDEX/`.

**Pivot cross-checked.** Take as object the near-null directions of a_T on P_T (the cluster of tiny
eigenvalues) and look for the exact relation between Arch and the contact terms on that subspace that makes
the ground value touch (almost) zero at c = 1 from both sides.

**Result of the cross-check, in one line.** The pivot is a repetition of candidate C11 of phase 211 ("near-null
pair and tangency c* = 1", `211/ROUND_003_A.md`), with its continuations C8, C12, C16, C19, C21, C35, C43 and C51
of the same ledger; the data of `ROUND_006` §10.3 reproduce those of these memos. No
subquestion was found that both lacks an antecedent and has a sign mechanism.

Scope of the reading. Read as primary sources (the memo, not the summary): `211/ROUND_003_A.md` in full;
`211/ROUND_002_D.md` §§6–7; `211/ROUND_002_E.md` (Lemmas 1–3, Cor. 4, correction, §4, next step);
`211/ROUND_004_A.md` §§4–5; `211/ROUND_007_B.md` §§4.3–4.5; `211/ROUND_021_A.md` §§3.3–3.4 and result;
passages of `211/ROUND_005_C.md` §5, `ROUND_009_B.md` §3, `ROUND_015_B.md` §4, `ROUND_017_A.md`,
`ROUND_027_A.md`; `211/LEDGER.md` in full; P46 lem:contA, cor:Tarch, lem:degen, prop:wit-sens, rem:wit-sens,
lem:shape-scale, thm:X, rem:X, lem:flowdet, rem:bar-loc, rem:bar-fam; P48 req:spec (R10) and the
sensitivity paragraph; `phase-192-exact-identity/PHASE_192_REVIEW_SUMMARY.md`; `phase-162-…/R162_2902_P2_DEGEN.md`
§§2–3; headers and verdicts of `R162_2101`, `R162_504`, `R186_018`, `R186_023`, `R186_025`, `R186_048`,
`R155_044`, `phase-198-parity-split/BB_001_…md`. Only by index row (not as primary source): phases 154, 156,
164, 199, 200, 202, 203, 204, 205 as far as cited below; this is stated in each case. The search was by concept
(minimizer, h*, g*, ground value, near-null, near-kernel, cluster, ladder, tangency, pin, calibration, window in
c, J_T, Danskin, concavity, sensitivity), not exhaustive. A search without matches does not prove novelty.

---

## 1. Lowest eigenvalues of a_T on P_T and their eigenfunctions

### 1.1 Structure of the ground value

| What | Where | Statement | Label |
|---|---|---|---|
| Continuity of the ground value | P46 lem:contA (l.621) | T ↦ λ_A(T) is continuous on (0,∞); the proof uses only the total absolute mass of the weights | PROVED |
| Empty entry instant | `phase-186-toolbox/R186_048_COMPONENT_BIRTH.md` Lemma 2.2, 2.4 | 𝔞_{T_n⁺} ≡ 𝔞_{T_n⁻}; the new contact is visible only through collars of width 2ε, \|c_F(log n)\| ≤ boundary mass | PROVED |
| Parity | P46 (paragraph after prop:finite); `211/ROUND_003_A.md` Prop. 1 | a_T commutes with J on P_T; λ_A = min of the even and odd ground values; Φ_T = min of the per-sector Φ | PROVED |
| Simplicity of the ground value | `211/ROUND_003_A.md` end of §3; `211/ROUND_027_A.md` §1 | there is no Perron–Frobenius for a_T on P_T (every F ∈ P_T changes sign; Π breaks positivity preservation). Simplicity OPEN; ground state even and simple with sector ratio 10–250 (0.6 ≤ T ≤ 1) and gap 200–2000 (T = 0.8, 1.0, 1.2) | OPEN / NUMERICAL |
| Perron–Frobenius on L²(I_T) | `phase-162-…/R162_504_SECOND_EIGENVALUE.md` Thms. 1–3, §5 | simple and even ground state of the form without restriction to P_T; parity ladder; the sign mechanism with Λ∗1 = log: NO-GO | PROVED (structure) / NO-GO |
| Nodes | `phase-155-…/R155_044_ROUND6A_NODAL.md` Prop. N1–N2; P46 prop:nodes | every nonzero F ∈ P_T has ≥ 2 sign changes; the k-th even eigenvector of Arch\|P_T has k nodes (k ≤ 8, NUMERICAL); the PF₂ kernel route closed for K | PROVED / NUMERICAL |
| Superexponential ladder | `211/ROUND_003_A.md` §2.1, §2.3; `211/ROUND_007_B.md` §4.3 | the four lowest eigenvalues (two per sector) decrease monotonically and superexponentially; λ_ev,2 = 2.2·10⁻¹ (0.6), **1.7·10⁻³ (0.7)**, 6.4·10⁻⁷ (0.8), 1.9·10⁻¹¹ (0.9); at ½log5+ε the ladder is 3·10⁻¹², 6·10⁻¹⁰, 3·10⁻⁷, 3·10⁻⁵, 2·10⁻³ | NUMERICAL |
| Size of the cluster | `211/ROUND_005_E.md` Thm. 3.1; `ROUND_006_A.md`; `ROUND_006_C.md` Thms. A–B | two-sided Weyl count PROVED; m_δ(T) ≤ exp(2e^T(1+o(1))) PROVED (generic on the comb); observed cluster ≈ 0.15e^{4T} (2, 4, 4, 6, 9, 16) NUMERICAL | PROVED / NUMERICAL |
| Upper bound on the margin | P46 thm:margin, cor:margin1; RULES_AVOID B2 | λ_A(T) ≤ 4·10⁹Te^{−15.449T} for T ≥ 1; limsup λ_A ≤ 0. (The paper's proof uses data from the other side; here only the bound on the form is cited.) | PROVED |
| Two-sided law | `211/ROUND_007_D.md` Lemma 4.6; LEDGER 211 C20 | the lower half of a law λ_A = L(T)(1+o(1)) is the target plus a margin; simple exponential law NO-GO | PROVED / NO-GO |

The value "1.7·10⁻³" that `ROUND_006` §10.3 gives as the third eigenvalue at T = 0.70 is λ_ev,2(0.7), already tabulated
in `211/ROUND_003_A.md` §2.3.

### 1.2 Where the near-kernel comes from (radical, prolate, Sonin-type explanations)

- `phase-162-…/R162_2101_*.md` §2 (PROVED as structure; §4 NUMERICAL, uncertified). The form extended to
  the whole line has an even radical of infinite dimension; the truncations to I_T of its vectors are null
  up to a doubly exponential error, and the radical contains primitive vectors; hence an even near-kernel
  of dimension ≥ 2 with one direction in P_T. Lemma 3: at a primitive contact the minimizer satisfies Wx = κφ̂ and
  \|κ\| = ‖Wx‖. The hypothesis of a local identity between the atom at log 2 and the archimedean or polar term:
  **NO-GO**. (The memo uses an external framing in §2; here only its content about the form.)
- P46 thm:ext-half (l.9913; PROVED given four citations): half-line identity, a_T(Ef) = exterior form of the
  out-of-band datum. It is the exact relation between the archimedean part and the comb on the images E: it holds only
  with Λ∗1 = log and Poisson. `211/ROUND_001_B.md`: there is no common radical vector of 𝒲 and 𝒲^c for c ≠ 1 (PROVED);
  the "fusion" reading NO-GO.
- `211/ROUND_008_E.md`, `ROUND_009_A.md`, `ROUND_009_B.md` (LEDGER C21–C23). Minimizer in the prolate block
  of dimension 3 to 10⁻⁴; λ_A ≈ κ₈(1−χ₈) and λ_j^ev ≈ κ_j(1−χ_{4j+8}) (NUMERICAL); upper half PROVED
  (λ_A ≤ 4KC₅N⁹(1−χ₈), given thm:ext-half); Fourier class–parity rule **free of Λ, not a sign step**
  (PROVED, `ROUND_009_B` §3.1); the near-nullity of the self-dual class breaks under every falsifier; the lower
  half is prob:ext-L, OPEN.
- Phase 199 (IDX README l.466–483; by index only): extremal vector at ½log15, f* = E⁻¹g* Fourier self-dual,
  1.106ψ₀ − 1.822ψ₄ + …; "rough floor = first-order response of the comb on the prolate part": NO-GO
  (NUMERICAL, PROOF_L_SHARP_BB_001).
- Phases 183–186 (IDX `04_PHASES_100-189.md` l.123–130; `phase-186-toolbox/`): semilocal Sonin chain PROVED
  for every finite S, without sign; invariant ρ*(T) = sup C/Son_S, positivity ⟺ ρ* < 1, 0 at ½log2 and 0.9437 at
  ½log3 with maximizer = h* (`R186_018`, reformulation); one-mode alignment **FALSIFIED** (`R186_023`:
  M(T) does not follow λ_min, error of 1 to 12 orders; a vector with overlap 0.96 gives Rayleigh quotient ~3·10⁻³,
  already above λ_min); phase of the comb on components FALSIFIED (tautological, `R186_044`).
- IDX `05b_LITERATURE_EXTENSION.md` L106 (CITED, unrefereed): ≥ m eigenvalues in [−δ, δ] with
  δ ≲ λ^{4m+17/2}e^{−πλ²}; recorded as a NO-GO quantifier ("a carrier must resolve m eigenvalues
  clustered at that scale").

### 1.3 Walls that fall on functionals of the minimizer

- P46 thm:X (l.8281; PROVED) and rem:X: what positivity on a larger window imposes on the new contacts
  is an inequality averaged over U_{T₀} at resolution π/T, never pointwise; a necessary condition, and
  the quartet model satisfies it with negative ground value (NUMERICAL).
- P46 lem:flowdet and rem:bar-loc: the coefficient of any log det flow near a small ground value is
  dominated by ⟨A′h*, h*⟩/λ_A, a functional of the minimizer; the difference with the quartet model is an
  inequality between two functionals of h*.
- P48 req:spec (R10) (l.552): the object cannot be a functional of the minimizer alone; every first-order
  discriminant is linear in the weights through c_{F*}(log n) and is satisfied by explicit models (PROVED at
  first order). RULES_AVOID B8 (W-lin, W-det, W-fam, W-pat, W-loc, W-mom) and B9.
- IDX README l.141–146 (SPEC_A): exact induction in T by contacts, NOT ADMISSIBLE; the residual conjecture is
  a property of the exterior field of the minimizer, not of Λ.
- **Phase 192** (`phase-192-exact-identity/PHASE_192_REVIEW_SUMMARY.md`): three exact identities on the
  minimizer (exterior field of h*, Mellin/Poisson on s_w, phase function of the window). The three
  identities PROVED and the three **EXCLUDED** as carriers: invariant under all modifications of the
  comb. The summary records only two channels of nonlinearity (h*(Λ) through the resolvent; a test constructed
  with the coefficients), "it does not add a third and does not prove that none exists".
- `phase-198-parity-split/BB_001_…md`: Π = Arch(h*) − λ_A (PROVED, trivial); squared Euler–Lagrange identity
  (CONDITIONAL); **BB3 NO-GO PROVED**: every polynomial identity in the shifts obtained from
  Euler–Lagrange is generic on the comb. CC_001: Hessian ∂²λ/∂κ_p∂κ_q = −2⟨C_p h*, R_⊥C_q h*⟩ ≼ 0, no sign
  for the cross term, continuous in the positions (NO-GO).
- `211/ROUND_007_B.md` §4.3 (**class NO-GO**: statements about values of the pieces at "the minimizer").
  (a) PROVED: the split depends on the Λ-free density chosen in the bookkeeping; (b) NUMERICAL: on the
  span of the three lowest eigenvectors the Λ-free piece ranges over [−0.11, +0.49] (½log5+ε),
  [−0.13, +0.46] (0.9), [−0.15, +0.44] (1.0), with gaps 10⁻¹⁰–10⁻¹⁵; a change of 10⁻⁷ in one weight or
  c = 1 ± 10⁻⁷ rotates the minimizer within the ladder. The ladder also exists for cΛ, a_P and the
  Beurling shift, with negative ground value: generic geometry on the comb.

---

## 2. Dependence on c

### 2.1 Archimedean threshold

- P46 cor:Tarch (l.2562; PROVED, with interval verification): 0.58 ≤ T*_{∞,P} ≤ 0.60; the ground value of Arch
  on P_T is strictly decreasing, positive before and negative after, and < 0 for all T ≥ 0.60.
  P46 thm:index: n₋(Arch\|P_T) = 0, 1, 2 on (0, T*_ev), (T*_ev, T*_odd), (T*_odd, 0.90], with
  log 2 ≤ T*_odd ≤ 0.81 (PROVED, computer-assisted).
- `05-meta-and-planning/ABCD-CLOSURE-PLAN/PATH-TO-D.md` l.71, 136;
  `phase-155-…/R155_031_CORPUS_SYNTHESIS_PATH_TO_D.md` l.158, 352; `R155_029` l.27: T*_{∞,P} ≤ 0.5958; "below
  it the primes are a cost, above it they are necessary".
- Reading remark: `ROUND_006` §10.3 states "Arch ⪰ 0 on P_T at T = 0.5925". 0.5925 lies inside the
  interval [0.58, 0.60] that cor:Tarch does not decide; the statement is NUMERICAL (compatible with the bound 0.5958).

### 2.2 Concavity, derivative at c = 1, dual representation

- P46 lem:degen (l.3294; PROVED): μ_T(v) concave and finite on ℝ^{𝒩_T};
  μ_T(v) ≤ μ_T(v⁰) − Σ(v_n − v⁰_n)c_{F*}(log n). It is not known whether the degenerate case (c_{F*} = 0 at all
  contacts) occurs.
- P46 prop:wit-sens (l.7283; PROVED) and rem:wit-sens: λ_A(T; (1+ε)v) ≤ λ_A − εκ_T, κ_T = Σ v_n c_h(log n) = Π
  on the minimizer; if κ_T > 0, (1+ε)Λ violates positivity for ε > λ_A/κ_T. NUMERICAL: κ_{log 2} ≈ 0.09,
  a uniform relative change of ~10⁻⁶ destroys positivity at T = log 2. P46 lem:shape-scale (l.8641):
  cΛ fails for large c at every T > ½log2 and for small c at every T ≥ 0.60 (PROVED); the version with
  c ∈ (1−ε, 1+ε) is CONDITIONAL on κ_T ≠ 0, "it is not known".
- P48 l.404–407: "concavity only gives upper bounds; lower bounds only come from chords, that is from
  convex decompositions of the comb".
- `phase-162-…/R162_2902_P2_DEGEN.md` §3–4: D1 (V ½-Lipschitz, V → −∞), D2, D3; Danskin
  V′(v±) = −c_{F*_v}(log 2) ∈ [−½, ½] (PROVED); the log 2 case OPEN and blind to Λ.
- Phase 198 BB_001 §2: λ_A(T; cΛ) concave in c, Π monotone in c (PROVED; only upper bounds).
- Phase 203 (IDX README l.587–589; by index): Danskin ∂λ_A/∂a(n) = −2n^{−½}c_{g*}(log n) (PROVED in the truncated
  class; CONDITIONAL on P_T); Theorem 2.3 NO-GO: concavity on the comb only gives upper bounds.
  AUDIT_203_001: at ½log15 the slope at c = 1 is ≈ −0.063; "the function rises from negative, has a
  maximum and falls to ≈ 0 at c = 1"; (1+ε)Λ has negative ground value for ε > 8·10⁻⁶⁹.
- **`211/ROUND_002_D.md` Theorem 1 (PROVED).** Joint range of (Π, Arch) on the sphere of P_T convex
  (Toeplitz–Hausdorff); Π takes both signs; Φ_T concave, → −∞ at both ends;
  max_c Φ_T(c) = Θ_T := inf{Arch(F): Π(F) = 0}; J_T = {c: Φ_T(c) ≥ 0} closed bounded interval; the target
  at T ⟺ Θ_T ≥ 0 ∧ 1 ∈ J_T; Θ_T is invariant under c. Cor. 3: λ_A ≥ Θ_T − \|1 − c*_T\|π_T (estimate with
  slack ≍ e^T). `211/ROUND_002_E.md` Lemma 2 (𝒦_T compact convex), Lemma 3 and **Cor. 4 (PROVED)**: where
  Θ_T(Λ) > 0 the condition Θ_T ≥ 0 survives small modifications; it only separates in tangency windows,
  where it coincides with the target. Correction: c*_T = 1 ⟺ 0 ∈ range of Π on the eigenspace of the ground value.
  Status in LEDGER 211: C8, PIVOT. RULES_AVOID B10 records it with that label.
- `211/ROUND_027_A.md` (C51; NUMERICAL NO-GO): v_T(Λ) is not the global maximizer of μ_T; the ground value at v_T(Λ)
  is simple and the gradient (c_{F*}(log n))_n is nonzero at T = 0.8, 1.0, 1.2; max μ_T = 0.047 versus
  λ_A = 6.2·10⁻¹² (T = 0.8).

### 2.3 The narrow two-sided window in c: already recorded

- **`211/ROUND_003_A.md` (C11).** Lemma 3 (Weyl "pin", PROVED): for an orthonormal pair in P_T on which Π
  is indefinite (eigenvalues μ₋ < 0 < μ₊), λ_A ≤ Θ_T ≤ Λ₂ and \|1 − c*_T\| ≤ (Λ₂ − λ_A)/min(\|μ₋\|, μ₊).
  **Lemma 4 (rigidity, PROVED):** if a_T\|_S ≤ ε, then λ_A(T; cΛ) ≤ ε − \|c − 1\|·\|μ_∓(Π\|_S)\| (μ₋ for
  c > 1, μ₊ for c < 1); if Π\|_S is indefinite, every c with \|c − 1\| > ε/min(\|μ₋\|, μ₊) gives negative ground value.
  NUMERICAL: the pair that fixes the tangency is the EVEN pair {e_ev,1, e_ev,2} (not an even–odd degeneracy); Π is
  indefinite on it from T ≈ 0.61 (the smaller eigenvalue of M_ev changes sign between 0.600 and 0.625) and
  decreases to −0.205 at T = 1; on the odd pair Π is positive definite at every T tested. Pin bounds:
  2.4·10⁻², 2.0·10⁻⁶, 7·10⁻¹¹, 2·10⁻¹⁴ at log 2, ½log5, 0.9, 1.0 (observed: 1.7·10⁻³, 1.3·10⁻⁷, rounding).
  Inertia of Π on the span with eigenvalues < 10⁻³: (0,2), (1,3), (2,4), (2,7).
  Prop. 2 (PROVED given Kato–Danskin, CITED): Φ′_±(1) = −max/−min of Π on the eigenspace of the ground value; the
  exact tangency c* = 1 is a codimension-one coincidence. **Recorded reading:** the computed ground state
  is even and simple with Π(e_ev,1) > 0 (0.088, 0.062, 0.046), hence the exact maximizer satisfies c*_T < 1
  strictly; what is observed is approximate tangency.
- `211/ROUND_015_B.md` §4.2 and `ROUND_017_A.md` (C33b, C35; NUMERICAL with PROVED second-order formula):
  b(c) = λ_A + (1−c)P − (1−c)²X + O(\|1−c\|³), P = Π(F_b), X = Σ_g\|Π(F_b, g)\|²/(μ_g − λ_A). Two thresholds of
  different nature: c > 1 dies at first order at \|1−c\| ≈ λ_A/Π(F) (5·10⁻²² at T = 1, 10⁻¹⁰ at T = 0.8);
  c < 1 survives first order and dies at second order through the coupling with the next rung,
  threshold ≈ Π(F)μ_g/X² (10⁻¹⁸–10⁻¹⁶ at T = 1; 10⁻⁸–10⁻⁶ at T = 0.8).
- **`211/ROUND_021_A.md` (C43; NO-GO with PROVED pieces).** Window J_R of the R-cell form: closed
  interval; Galerkin windows are outer bounds; J_R → {1} from both sides and superexponentially
  (NUMERICAL). **Lemma 3.3 (PROVED):** λ₀/‖𝒦‖ ≤ c₊ − 1 ≤ λ₀/K₀ and analogues for c₋. §3.4: "the narrowing of
  the window does not provide a lower bound; it is equivalent to the absence of one"; the mechanism survives
  Beurling systems, hence it is not a sign step. Prop. 3.2: P_w𝔇_R = [M_x, 𝔇_R] if and only if w ≡ 1 on
  prime powers < R: after using the identity "no remainder is left", the question is the sign of the Λ-free form
  Q₀ − 𝒦_R.
- Phase 200, LEMMA_I3_001 (IDX README l.537; by index): exact pencil in the radical gauge,
  A(c) = Lᵀ[(1−c)C ⊕ (A_⊥⊥(1) + (1−c)Q/C)]L with L fixed, Schur complement affine in c; inertia jump at
  c = 1; "comb modulo gauge ≽ 0 on the near-kernel": FALSE; NO-GO as a sign object.
- RULES_AVOID D17 lists "windows in c" and "𝒜𝒫 − c𝒞 with c ≠ 1" among what is not relaunched
  (`211/ROUND_019_B`, `ROUND_020_A`: margins in c of a representative are ℝ or ∅; S-lemma multiplier
  forced to 1; C39: 2×2 positivity of rungs survives c ∈ [0, 3.5]).
- "Control c = 2": RULES_AVOID M5 (closure under product of factors, check at c = 2, not found) and
  N3; R3-i (`REVIEW_003.md`): it is not enough that the identity stops holding for cΛ; R3-e: exterior blocks
  homogeneous in c; L6/R4-f: inertia does not distinguish c = 1.

On the concrete values of `ROUND_006` §10.3 (T = 0.70 and 0.75, N = 30): there is no textual match for
those two rows, but the phenomenon, its mechanism (Lemma 4 of 003_A, Lemma 3.3 of 021_A) and its sizes are
recorded at T = log 2, ½log5, 0.8, 0.9, 1.0, 1.2 and ½log15. The new values are compatible with them
(at T = 0.70 the ground value at c = 0.999 is larger than at c = 1, as c* < 1 requires; the width ~10⁻³ matches the
1.7·10⁻³ observed at log 2). The sentence "every exact certificate at T ≥ 0.70 distinguishes c = 1 with that
precision" is P46 rem:wit-sens and `211/ROUND_004_A` Prop. B.

---

## 3. "Exact identity on the near-null subspace": attempts under other names

| Attempt | Where | What was constructed | Where it stopped and why (recorded) |
|---|---|---|---|
| Matrix inequality on the near-null pair | `211/ROUND_003_A.md` §4 | Σ v_n R_n(S) ⪯ Arch_S in 2×2, S = lowest even pair | circular: S depends on Λ; saturated to 18 digits; (P1)–(P2) "as strong as the positivity they would serve" |
| Λ-free planes (eigenvectors of Arch) | `211/ROUND_004_A.md` Prop. B, §5 | explicit k×k conditions on v_n | **NO-GO PROVED**: every condition with slack ε_E > 0 survives \|c−1\|‖Π\|_E‖ < ε_E; the Schur complement requires margin precision; doubly exponential arena |
| Family of comb responses E_T | `211/ROUND_005_C.md` §§2, 5; `ROUND_007_E.md` | exact reduction PROVED; sign lemma (SL_T), cubic in v, without slack | mechanisms via identities (Selberg, local factors, Lévy kernel): NO-GO, they hold for Beurling and a_P; λ_min(a\|E_T) exceeds λ_A by 6/13/31 orders: the sign lives in the Schur coupling |
| Budget σ_T + κ − ℛ on the minimizer | `211/ROUND_007_B.md` §§3.3–4.3 | identification with the pole-free form and ℛ = Π + 𝔢; response cubic | NO-GO: parts of size ±1.4·10⁻³ cancel to 3·10⁻¹²; values on the minimizer undefined below the ladder |
| Neumann series of the Schur coupling | `211/ROUND_008_D.md` | finite polynomial inequality 𝒫_K(v) ⪰ 0 | NO-GO: degree ∝ log(1/λ_A); low even degrees give the wrong sign |
| Krylov and words from Λ-free seeds | `211/ROUND_005_A/B/E`, `ROUND_006_B` | word algebra, Widom-type square | NO-GO: homogeneous families invariant under cΛ; they do not capture the Π-indefinite near-kernel below the dimension of the cluster; Lanczos blind to the cluster |
| Coupling vector of the survivor; rungs | `211/ROUND_017_A`, `ROUND_018_B` | Schur form split into arch/comb/Tate; second-level radical identity | PIVOT / NO-GO: arch and comb parts cancel with shares ±10²…10³⁸; 2×2 positivity of rungs generic in c |
| Even Schur reduction at log 2 | `phase-155-…/R155_032`, `R155_039`; PATH-TO-D (iii); `R162_2902` Thm. P2 | Prop 3c.1, Thm. 3c.3; W_{log 2} ≻ 0 on seven even modes (certificate) | structural identity PROVED only for the prime part (chains of ≤ 4 vertices, closed spectrum, 0.9009276…), **blind to Λ**; "there is no identity for the full S_even beyond the archimedean spectrum" |
| Nodal explanation of the cancellation | `R155_044`; `R162_2902` §2 | cancellation between n = 2 and n = 3 = interference in the chain P₄ | tool; the arena requires ≥ 12 modes (P46 thm:arena); no fixed truncation decides |
| Finite reduction (L1)/(L2) | `phase-186-toolbox/R186_025` Thms. A, B, Cor.; P46 thm:coer-schur | λ_A > 0 ⟺ S_{T,k} ≻ 0, dimension 2k−2 | (L1) PROVED; (L2) OPEN: "it is positivity rewritten in an explicit basis", inherits the decay of the margin; interlacing/first crossing NO-GO (phase 204, by index) |
| Theorem P, negative indices | P46 thm:index, thm:parityschur, prop:polarcap, subsec:inertia-excl | n₋ ≤ 5/7/8; polar capacity | PROVED tool without sign; the inertia count does not distinguish c = 1 (RULES_AVOID L6) |
| Flat-top dual certificates | phase 154; P46 thm:Z, thm:C; RULES_AVOID C3 | certificates up to ½log5 (own) and ½log15 (CITED) | the dual class is the target itself; per-window format (W-fam) |
| Per-window converse | phase 156; P46 prop:onewindow, cor:convfail | 2×2 polar-capacity condition | FALSIFIED in comb models (IDX 04 l.204) |
| Tail theorem | phase 164 (IDX 04 l.904–909; by index) | reduction to a tail condition | PARTIAL; the condition remains a reformulation (IDX 04 l.1029). The memos use an external framing; not developed |
| Exterior table | phase 202 (IDX README l.579–583; by index) | form by classes q = b/a and layers; Lemma M | phase closed: X1 = partition of the inequality; "𝔅_n is never multiplicative" |
| Component object | phase 205 (IDX README l.626–632; by index) | comb matrix in Dirichlet sines; Green function of the pole | skeleton without a sign node; the finite reformulation "n₋(𝔄_N) = 1" NO-GO as a route |
| Exact identities on the minimizer | phase 192; phase 198 BB_001 | see §1.3 | EXCLUDED / generic on the comb |
| Variation formula of λ_A in T | `211/ROUND_008_C`, `ROUND_024_A` | virial bracket; jump −2v_nF*(T_n)² | NO-GO as a route (reformulation; class 𝒦_H); CONDITIONAL on boundary regularity |

---

## 4. Closed patterns of `RULES_AVOID.md` under which the pivot falls

- **B9** "The sign remains in a functional of the minimizer (IDX SPEC_A, BARRIER_W; P48 req:spec R10)." The proposed
  object is the low eigenspace, a function of Λ through the resolvent.
- **B10** "Concavity on the comb (Danskin) gives only upper bounds. Its dual representation
  Θ_T = max_c λ_A(T; cΛ) is PROVED and only separates in tangency windows, where Θ_T = λ_A: status PIVOT, not
  open terrain." It is the literal statement of the phenomenon of `ROUND_006` §10.3.
- **B3** "Exact reformulation presented as progress." The exact relation on S is
  Arch\|_S = Π\|_S + a_T\|_S; "the ground value touches zero at c = 1" is the target restricted to S.
- **B8** (W-fam, W-loc): law on a bounded range of windows; criterion recomputed per window.
- **B1** in the identities variant: phase 192 and BB3 (generic on the comb).
- **D17** "windows in c", "Λ-free planes E_k and every fixed finite Λ-free subspace", "Neumann
  truncation of the Schur coupling", "capture of the sign in E_T", "Lanczos blindness", "global maximization
  of μ_T(v)", "sign only from the high block or only from the low one".
- **D11** "Nodal localization of a negative witness".
- **J3** canonical factorizations exist with remainder ≥ 0 if and only if the target holds; **J6** / R3-e;
  **R3-i**: "it is not enough to point out that the identity stops holding for cΛ; one must point out why the remainder stops
  being ≥ 0".
- **L6** inertia or signature count: does not distinguish c = 1.
- **G6** named walls: W-Sonin, W-fam, W-loc, thm:X as a necessary condition.
- `OBJECT_SPEC.md` O5 (uniformity in T; not a family whose dimension is recomputed per window), O8 ("it is not
  a functional of the minimizer"), O4.
- C1: "Sonin, prolates, semilocal as a source of sign"; "coercivity, Schur, inertia … as a source of
  sign"; "defect/continuation, Morse index".

---

## 5. Assessment (separate from the findings)

**(a) Repetition?** Yes. Main entry: LEDGER 211 **C11** (`211/ROUND_003_A.md`), whose title is that of the
pivot. Pieces already written that exhaust its statement:

1. The exact relation between Arch and the contacts on the near-null subspace is Arch\|_S = Π\|_S + a_T\|_S
   (003_A §2.1), and its origin is the half-line identity with the radical (P46 thm:ext-half; `R162_2101` §2;
   021_A Prop. 3.2). That identity characterizes c = 1 and, once used, leaves no signed remainder.
2. Why the ground value becomes negative on both sides of c = 1: Lemma 4 of 003_A (near-kernel with Π
   indefinite) and Lemma 3.3 of 021_A; two-threshold law of 015_B/017_A.
3. That this gives no lower bound: 021_A §3.4(i), B10, P48 l.404–407.
4. That the non-circular version (Λ-free planes) is NO-GO: 004_A Prop. B.
5. That the Λ-dependent version is the target at margin precision: 005_C, 007_B, 007_E, 008_D.

Precision about the premise. "Touches (almost) zero exactly at c = 1 from both sides" is not what the record
says. What is recorded is: exact tangency = codimension-one coincidence (003_A Prop. 2); numerically
Π(F*) > 0, hence the maximum of Φ_T is at c* < 1 strictly and Θ_T > λ_A; J_T is an interval containing 1
in its interior if λ_A > 0, with c₊ − 1 ≈ λ_A/Π(F*) and 1 − c₋ of the size of the next rung. There is no
"exact two-sided contact" to explain; there is an interval whose width is the margin read in the variable c.

Consistency note (ARGUED; not written in the corpus, not verified by a second reader and not used
as a finding). With a_T\|_S between 0 and ε, Π\|_S lies between Arch\|_S − ε and Arch\|_S, so that the negative
directions of Π on the near-kernel are bounded by the negative index of Arch on P_T (P46 thm:index:
0, 1, 2). This fits the inertia table of 003_A §2.6 and the fact that the pin is even from T ≈ 0.61, just
after T*_ev ∈ [0.58, 0.60]. If correct, two-sidedness is a consequence of the archimedean index, which is
free of Λ, plus near-nullity: generic, without mechanism.

**(b) Subquestion without antecedent.** None that has both absence of antecedent and a sign mechanism.
What remains unexecuted, with its status:

- (C1)–(C3) of 003_A §4 as theorems (Π indefinite on the even pair with uniform μ₋ ≤ −c₀; λ_ev,2 → 0
  superexponentially; ground state even and simple). OPEN, only NUMERICAL. They are structural statements that their own
  memo describes as as strong as the positivity; proving them would give c* → 1, not λ_A ≥ 0.
- The relation of the pin threshold (T ≈ 0.61) to T*_ev: not found in writing (see the preceding note). Free
  of Λ in its archimedean half.
- Convergence in c for T ∈ [0.60, 0.75]: `ROUND_006` §10.3 declares it uncontrolled; it is numerical.
- From round 6 of this phase, without textual antecedent and outside the pivot: the direction ℓ of §10.2
  (overlap 0.60–0.62 with the lowest eigenvector) and the obstructing pair of equal density. `REVIEW_006.md` already
  records them as "without object".

A search without matches does not prove conceptual novelty; here, moreover, the matches are abundant.

**(c) What the four-point filter would have to say** for the only variant that is not literally a
closed entry (an identity on the near-null subspace depending on Λ, with its own formula):

1. *Closest antecedent.* `211/ROUND_003_A.md` §4 and Lemma 4; `211/ROUND_005_C.md` §5 ((SL_T)); `211/ROUND_021_A.md`
   Prop. 3.2 and Lemma 3.3; P46 thm:ext-half; phase 192.
2. *New object or statement.* It would have to write S_T without solving the problem (not "the lowest
   eigenvectors"): an explicit family with growing dim S_T (cluster ≈ 0.15e^{4T}), which is neither E(prolates of the
   self-dual class) nor the family of responses E_T nor a Λ-free plane, together with V_T on it. Today there
   is no such object; "the near-kernel" defined by the spectrum is circular (J3).
3. *Why it avoids the difficulty of the antecedent.* It would have to answer three recorded reasons: (i) on
   S the available identity is already exact and leaves no remainder (021_A §3.4); (ii) the sign is not in a_T\|_S but
   in the Schur coupling with S^⊥, which must be known to relative precision e^{−15.449T} (004_A §5(c);
   007_E); (iii) every identity on the minimizer obtained from the Euler–Lagrange equation or from the
   identities of the comb holds for Beurling and a_P (BB3; 005_C §5.3(iv); phase 192).
4. *Link with global positivity.* It would have to be (G) of `OBJECT_SPEC.md` on all of P_T and every T:
   a_T = ‖V_TF‖² + ρ_T. The two-sided information in c does not give it: by 021_A Lemma 3.3 the width of the window is
   λ₀ up to constants, and by B10 concavity only bounds from above. One would need an inequality of the type
   "Schur complement of a_T with respect to S_T ⪰ 0 with S_T^⊥ coercive", uniform in T, and item (5) of
   `OBJECT_SPEC.md` §4: the line where the remainder stops being ≥ 0 for cΛ with \|c − 1\| arbitrarily small
   and for a_P. With dim S_T finite per window it also clashes with O5.

**Conclusion of the cross-check.** The pivot, as stated, does not pass the gate: it is C11 of phase 211 with
its later closures, and falls under B9, B10 and D17. No derivation or computation on it is authorized. The data of
`ROUND_006` §10.3 may be recorded as a NUMERICAL reproduction, at T = 0.70 and 0.75, of `211/ROUND_003_A` Lemma 4
and `211/ROUND_021_A` Lemma 3.3. Global sign: OPEN.

## Caveats

- No script was run and no value was recomputed.
- Phases 154, 156, 164, 199, 200, 202, 203, 204 and 205: cited by index row except where reading as primary
  source is indicated. The memos `211/ROUND_005_C`, `008_D`, `008_E`, `009_A/B`, `015_B`, `017_A`, `018_B`
  were read by passages, not in full.
- `211/ROUND_008_A.md` is truncated (RULES_AVOID §H); it was not used.
- Several memos prior to phase 211 (R162_2101, R163–R165, phase 199) use an external framing of the
  target; their content about the form was recorded and nothing else.
- The index summarizes by phase; the folders prior to phase 100 were not opened for this cross-check.
