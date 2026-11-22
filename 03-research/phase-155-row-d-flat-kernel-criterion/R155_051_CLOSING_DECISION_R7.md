# R155_051 — Closing decision, round 7 (prolate floor; AL retraction; whole-paper review R2)

Inputs: R155_047/048 (Theorem P), TEX_HOSTILE_REVIEW_R2 (Paper 46 whole-paper), R155_049/050 (AL correction). Rules as before.

## 1. Labels of record
| statement | label |
|---|---|
| Theorem P: λ_k(S_c) ≤ Λ_k(c) = (2/π)∫₀^c(1 − Σ_{j<k}(2j+1)j_j²) (Legendre diagonal + Ky Fan); Cor P1 quadrature-free | PROVED (self-contained; likely folklore) |
| Cor P3: n₋(A_∞|P_T) ≤ min_{τ₁} min{k : Λ_k(Tτ₁) ≤ θ(τ₁)} ⇒ n₋ ≤ 5/7/8 at ½log3/log 2/0.80 | PROVED (theorem values); grid 5/6/7 DIAGNOSTIC |
| Two-sided: 2 ≤ n₋(Γ_T) ≤ 5, [2,6], [3,7] on L²; 0 ≤ n₋(A_∞|P_T) ≤ 5/7/8 | PROVED |
| The two-value relaxation cannot reach n₋ = 1 (exact count 5 at optimal τ₁ at log 2); multi-band relaxation untested | PROVED (two-value) / OPEN (multi-band) |
| Problem A via a uniform floor: does not follow (flat top is the near-λ₀ concentrator) | REMARK / HEURISTIC |
| **thm:AL / cor:ALdef (round 4b) RETRACTED**: wrong density and inconsistent hypothesis; passed audit R155_037 in error | RETRACTED |
| Theorem AL′: end-point-corrected lattice sampling of a comb-vanishing flat-top certificate loses exactly Θ(1/M): E_edge = (4/π)cosh T·d + O(d²), sharp; smooth part O_r(M^{−r}); signed ν allowed | PROVED |
| "The lattice is never the deficit" (round 4b) | WITHDRAWN |
| Coherence of Θ(1/M) with the archimedean Ceil_∞ deficit 0.28·M^{−1.17} | STRUCK (different setting: no polar block) |
| Flat-top vs lattice classes: the polar block's window cut is what separates them (why prop:TK does not bind flat-top certificates) | READING |
| Paper 46 whole-paper review R2: MAJOR REVISION (no headline theorem false; 1 FATAL = AL; constants; KEP08 range; abstract attribution; restructure to ~34 pp. + appendices) | applied in the R2 pass (in progress) |

Row-D label unchanged. Endpoint unchanged. No sign for ζ beyond log 2. No value of inf W at log 2 asserted.

## 2. Process finding of record
A theorem (AL) with a wrong hypothesis and a wrong density passed an audit (R155_037) and reached the paper. It was
caught only by the whole-paper referee. Rule added: every statement entering Paper 46 must be checked against the paper's
OWN definitions (def:W, def:PD, eq:nuw) by the integrating editor, not only against the memo's memo; and a whole-paper
review is mandatory after every three rounds of additions.

## 3. State of the path
Live analytic lever (prolate floor): built (Theorem P) and spent for the two-value relaxation; the multi-band relaxation is
the one remaining refinement toward n₋ = 1 (one short round). P6 (alignment-band arithmetic lower bound) and P7 (D-HS kill
tests) remain Decisions. The map is otherwise complete for what pure mathematics on the analytic side can decide with
the present tools; the remaining content of D is arithmetic (R155_031 §2.D).

## 4. Orders
(a) Finish the R2 major revision of Paper 46; then a confirmatory TeX review R3 (shorter: verify the 22 edits + AL′ +
 Theorem P + restructure only).
(b) Round 8 (optional, pending decision): multi-band relaxation for n₋; Decisions on P6/P7.
