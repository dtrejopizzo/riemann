# REVIEW_BARRIER_EST_001 — review of BARRIER_EST_001_ESTIMATE_CLASS_NO_GO.md

Phase 197. Review checked against Paper 46 main.tex (def:comb l.7225, subsec:shape-est / lem:shape-est l.8648ff,
cor:margin1 l.3516, prop:env l.3013, prop:wit-sens l.7087) and AUDIT_PHASE193_CERTAINTY (CIRC table, rows 1a).
 No sign is produced by the memo or by this review.

## Verdict summary
| item | verdict |
|---|---|
| (a) class 𝓔 | CORRECT but NARROW: near-tautological, and it **does not contain Paper 46's own estimate notion** (memo §3 last note is wrong) |
| (b) Lemma 3 | PROVED (signs, admissibility, normalisation all correct) |
| (c) Thm 4 / Cor 5 | PROVED (absolute form); 16.449 relative constant ARGUED (memo's "A_T ≥ …" is an elided step) |
| (d) 𝓔^ℕ, Prop 6 | qualitative PROVED; the stated bound has a **normalisation error** (relative vs absolute ℓ¹ slack); quantitative κ̂ OPEN, hard |
| (e) CIRC upgrades | over-claimed: only #15, #16 upgrade cleanly; #2, #14, #23, #26 need 𝓔^ℕ and stay CIRC/CONDITIONAL; #25 conditional on formulation |

## (a) The class 𝓔(T,r)
1. **What it is.** Since |b_T(ν)−b_T(ν′)| ≤ ‖(ν−ν′)|_{(0,2T)}‖_TV (|c_F| ≤ ‖F‖²), Thm 4 says: a premise set that cannot tell ν_Λ
   from ν_Λ plus a positive mass > λ_A(T) cannot prove b_T ≥ 0. Correct, short, not vacuous — but it is the Lipschitz bound of
   prop:wit-sens read backwards plus one decreasing direction. Label it a PROVED *formalisation* of the black-box-estimate
   clause, not a new barrier.
2. **Does a real estimate argument hold uniformly over this ball?** Used *as a premise* (black box), an inequality such as
   |ψ(x)−x| ≤ R(x) is TV-robust with large slack — yes. But no number-theoretic argument that reaches a sign uses estimates
   alone: it always also uses an exact support/integrality axiom (supp ν ⊆ log ℕ, or merely ν((0,log 2)) = 0, Λ(n) ≥ 0 on
   integers, Euler product). Any single such axiom violates (E2) and **kills the u→0⁺ falsifier** (no mass below log 2).
   So 𝓔 misses exactly the hybrid class "estimate + exact support", which is where real proofs live. This is the precise gap.
3. **Paper 46's own notion is integer-supported.** In subsec:shape-est, 𝓕^{(a)}_T(F) = Σ_{n∈𝒩_T} v_n(a) Re c_F(log n) − 2∫…,
   and λ_A(T;a) is the bottom for a weight vector a on 𝒩_T (§subsec:finite). The comb a there is *not* a def:comb measure.
   Hence memo §3's note ("instance (a) falls under the PROVED Thm 4, not §3") is **false against the paper's definitions**:
   lem:shape-est(iv) in the paper's sense falls under 𝓔^ℕ. Memo §4's "(iv) PROVED for 𝓔" must be restated as "PROVED for the
   measure extension of the estimate notion"; the paper's (iv) stays ARGUED (quantitatively), now with a weaker hypothesis (d).
4. A cheap intermediate class worth naming: 𝓔^{≥log2} (premises TV-robust among combs with ν((0,log2)) = 0). Falsifier needs
   κ̃_T := sup_{u∈[log 2,2T)} Re c_F(u) over near-minimizers; qualitative positivity by the Prop 6 argument; quantitative OPEN.

## (b) Lemma 3
𝔞^{ν′}_T(F) = m_T(F) − ∫Re c_F dν_Λ − m Re c_F(u): sign correct (added mass lowers the form). An atom at u ∈ (0,2T) is a
positive Borel measure finite on bounded sets — admissible in def:comb. Order of choice is right: F unit near-minimizer
first (exists by def. of bottom), then u small by L²-continuity of translation (c_F(0) = 1). ‖ν′−ν_Λ‖_TV = m. PROVED.

## (c) Theorem 4, Corollary 5
For m ∈ (λ_A, r], choose η with m(1−η) > λ_A+η: b_T(ν′) < 0, while ν′ satisfies Prem by (E1); Lemma 2 (CITED, Shoenfield)
plus soundness gives b_T(ν′) ≥ 0 — contradiction. r ≤ λ_A(T) ≤ 4·10⁹Te^{−15.449T} (cor:margin1, T ≥ 1): PROVED.
Exponent statements (c < 15.449; C T^{−k}) PROVED. Relative form: absolute slack = ε A_T with A_T = (4+o(1))e^T
(prop:env(iii)); "A_T ≥ 3.9e^T for T ≥ 1" is elided ("A_T ≥ …") and not in the paper; with o(1) only it holds for T ≥ T₀
ineffective. c < 16.449 is PROVED for large T, the explicit constant ARGUED (repairable with explicit Chebyshev bounds,
Rosser–Schoenfeld, CITED-able).

## (d) 𝓔^ℕ and κ̂_T
- **Normalisation error.** κ̂_T(η) carries the factor v_n, so the perturbation is relative: v_n ↦ v_n(1+ε sgn Re c_F(log n)),
  ℓ¹ change ε A_T, decrease ε κ̂. Correct statement: relative slack r_rel ≤ (λ_A+η)/κ̂_T(η), or absolute ℓ¹ slack
  r ≤ A_T(λ_A+η)/κ̂_T(η) (and ε < 1 for positivity). The memo's "ℓ¹(v)-slack r ≤ (λ_A+η)/κ̂" is right only in the relative reading.
- Qualitative κ̂ > 0: correct (nonempty open set of near-minimizers; a quadratic form vanishing on an open cone vanishes on
  P_T∩𝒟_T; shift-by-log 2 form has infinite rank for 2T > log 2, P_T has codim 2). PROVED.
- **Gain over the paper:** κ̂ uses Σ v_n|Re c_F(log n)| (unsigned), so the condition κ_T ≠ 0 of lem:shape-est(iii) is replaced by
  "some c_h(log n) ≠ 0" — strictly weaker. Real progress, worth integrating.
- **Why quantitative κ̂ is hard.** Qualitative positivity is useless as a barrier: the bound (λ_A+η)/κ̂ is below the margin
  only if η ≲ λ_A and κ̂(η) is bounded below; as η → 0, κ̂ → sup over the minimiser eigenspace. One-line reduction (PROVED):
  for 𝔞_T(F) < λ_A+η, Σ_n v_n|Re c_F(log n)| ≥ m_T(F) − λ_A − η, so κ̂_T(η) ≥ sup_{near-min} m_T(F) − λ_A − η. A quantitative κ̂
  therefore follows from a lower bound on the archimedean form m_T at near-minimizers. At a fixed window (T = log 2,
  numerically κ ≈ 0.09) this is a certified Galerkin/interval computation — feasible with existing machinery (NUMÉRICO→
  certifiable). Uniform in T it requires structural control of the minimiser (that it is not m_T-null), which is OPEN and
  not easier than the current minimiser-structure questions of phases 155/186. Rating: fixed T medium, all T hard.

## (e) CIRC kills (AUDIT_2026-10-15 §1a)
Rule: Thm 4 applies only if the seed's sign step is stated on **measure** combs with TV-robust premises and *no* exact
support axiom. Integer-indexed seeds need 𝓔^ℕ (κ̂ OPEN).
| # | seed | memo claim | verdict |
|---|---|---|---|
| 2 | P191 "T* cannot be an estimate" | non-circular for 𝓔 | **stays CIRC**: T* is about Λ on 𝒩_T, i.e. paper's (integer) estimate notion → 𝓔^ℕ; downgrade cause changes from "(iv) ARGUED" to "κ̂ quantitative OPEN" |
| 14 | C_001 tolerance cells | iff tolerance on measures | **stays CONDITIONAL** (product-formula cells are integer-indexed); condition weakened κ_T ≠ 0 → κ̂ bound |
| 15 | E8 Golden–Thompson | (B′) half non-circular | **UPGRADED**: trace inequalities hold for every positive comb, hence TV-robust; (in fact already caught by comb-genericity A1) |
| 16 | E9 MSS / Lee–Yang | (B′) leg non-circular | **UPGRADED** on (B′) leg, same reason; retry strength unchanged |
| 23 | M5 singular series | (B′) leg PROVED | moot/overclaimed: singular series are integer data → 𝓔^ℕ; the kill already stands via CA_M_001 (PROVED) |
| 25 | F7 Selberg equidistribution | non-circular | **CONDITIONAL on formulation**: discrepancy ⊇ TV ball (good direction), upgrade valid only if the premise is on measures and no log ℕ support axiom is used |
| 26 | C_006 Helson H²(𝔻^∞) | (B′) half non-circular | **NOT upgraded**: Bohr lift needs frequencies log n; an atom at u ∉ log ℕ leaves the setting → 𝓔^ℕ. Kill still stands on its RD half |
Audit row (B′) should read: "(iv) PROVED for measure combs (𝓔, BARRIER_EST_001 Thm 4); for the paper's integer-weight
estimates qualitative only, unsigned κ̂ replaces κ_T ≠ 0, quantitative OPEN; reading for named estimates ARGUED".

## Required corrections to the memo before any Paper 46 integration
1. Delete/rewrite §3 last note and §4 first bullet (paper's estimate notion is integer-supported).
2. Fix Prop 6 normalisation (relative slack, or factor A_T).
3. Replace "A_T ≥ …" by a cited explicit bound or keep ARGUED.
4. Replace §5 list by the table above.
5. Add the hybrid-class remark ((a)2, (a)4): 𝓔 excludes every proof using an exact support axiom.
Labels after review: Lemma 3, Thm 4, Cor 5 (exponent) PROVED · Prop 6 qualitative PROVED (corrected normalisation) ·
κ̂ ≥ m_T − λ_A − η PROVED · quantitative κ̂ OPEN · 16.449 constant ARGUED · row D OPEN, no sign.
