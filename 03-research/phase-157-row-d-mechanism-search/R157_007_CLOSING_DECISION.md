# R157_007 — Closing decision, phase 157

Inputs: R157_001 + R157_003 (DMV import), R157_002 + R157_004 (filtered mechanism search), R157_005 + R157_006
(Berkovich test). Blueprint R157_000 (F4 amended per R157_004).

## 1. Labels of record
| statement | label |
|---|---|
| (H-DMV) via (H-DMV′): a discrete Beurling system with `N = ρx + O(x^θ)`, `θ < 1`, zeros `β_n → 1` | CITED (secondary source): Broucke–Debruyne–Vindas, Broucke, Broucke–Debruyne; independently Zhang 2007 (zbMATH) + Révész Thm 5. Primary texts unread |
| T3 (P46 Rem 27.16) | METHOD-CONSTRAINT modulo that import; stays a Remark |
| Phase 150 misquoted DMV (integer law is `O(x^θ)`, not `O(x e^{−c√log x})`) | CORRECTION |
| O3 margin resolution: a change of one `Λ(n₀)` of size `≤ 2·10⁹ T e^{−14.449T}/\|c_{F*}(log n₀)\|` flips the primitive sign; vacuous for `T ≤ 1.51`; degenerate case → Lemma D (OPEN) | PROVED (upper bound) |
| Continuity of `T ↦ λ^W_T` (Lemma C; = Bombieri Thm 5); `λ^W_T > 0` for `T ≤ 0.005` by an elementary bound (Lemma E) | PROVED |
| O4: RH ⟺ `λ^W_T ≠ 0 ∀T` | RESTATEMENT; the "determinate at a crossing" clause FAILS |
| Mechanism search: 61 candidates → 39 EXCLUDED, 20 EQUIVALENT, 1 closed as restatement (P152.2), 1 NOT EXCLUDED without an object (MW-5 cluster incl. Deninger) | survey, audited |
| (P152.2), Berkovich difference kernel on `A^{1,an}_Z`: every energy in 𝔄⁺ is `W = Σ_v Q_v` or reduces to D.195 (3.5) = RD_T | RESTATEMENT (not an impossibility) |
| NG-E1 proved: `Q_p(F_φ) = −v_p‖φ‖²`; each local form is negative definite on an infinite-dimensional subspace of `P_T` for `T > ½log p` | PROVED |
| T1 reading corrected (P46 Rem 18.1a): a field-uniform proof is admissible and proves GRH for all K | CORRECTION (blueprint F4; PATH-TO-D item 9) |

## 2. Effect on the map
The filter now has a proved backbone: F1 (O3 + `cor:void`), F2 (`thm:margin`), F3, F5, and the amended F4 (T2 + T3).
Every candidate in the corpus and the standard literature is either excluded, equivalent to RH, or a restatement.
The one remaining entry, the MW-5 cluster (Deninger's foliated dynamics and the residuals of the `h⁰` and import
readings), is not excluded by any proved statement, but no one has built an object for it and it has no one-round
test. By O1 (R157_002), a "uniformity mechanism" is exactly a proof of Weil's criterion; the per-window language
supplies filters, not an object.

## 3. Decisions
(a) Direction: (A) close row D in the map, final; or (B′) open a phase on MW-5, which first requires building a
concrete object (a foliated space or dynamical system with the required cohomology) that the filter can test.
(b) Lemma 3.1(iii) for Paper 44 depends on first deciding whether Dictionary B.1 (R152_001:266) enters Paper 44.
(c) Commit phase 157 and the P46/P47 edits.
Row-D label unchanged; endpoint of record unchanged; no sign beyond the table in the reduced statement, §3.
