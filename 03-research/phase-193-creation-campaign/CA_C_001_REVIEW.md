# CA_C_001 — Review
Checked vs P46 prop:shape-inputs (E), lem:cpos, lem:shape-amp, prop:shape-eulerdel, lem:shape-quartet, prop:shape-family, rem:shape-ident.

## Verdict
**NO-GO for the declared product-formula classes CONFIRMED (Theorem 1, Corollary 1 PROVED; two cells CONDITIONAL as labelled). Exact PF on the window = singleton (REF-D as a class) CONFIRMED. (Fam_η): OPEN necessary sub-statement — NOT an admissible candidate (does not imply the target without (Span_η)).**

## 1. Claims
| claim | check | label |
|---|---|---|
| Lemma 1 D_Λ(n) = log n = product formula | ✓ | CONFIRMED |
| Lemma 2 singleton | divisors of n < X lie in [1,X); a∗1 invertible by μ on the initial segment ✓ | CONFIRMED PROVED |
| Lemma 3 contact of chosen sign | lem:cpos with ℓ below the gap to other log n; F^± ∈ P_T (lem:cpos construction); archimedean part fixed ⇒ −∞ ✓ | CONFIRMED PROVED (depends on lem:cpos producing F in P_T — it does) |
| Lemma 4 Bertrand contact | real Bertrand (x>1 ⇒ prime in (x,2x)) CITED ✓; 2p₀ > X ✓ | CONFIRMED |
| Table cells | checked each: n₀=6 moves only composites ✓ (6 divides no prime power); p₀ moves only its own local relation ✓; a_P: D = 0 ≤ log n ✓; (≥,≥) Λ+c1₂ raises prime powers 2^k and composites ✓ | CONFIRMED |
| a ≥ 0, (=,≤) singleton | local "=" at all prime powers ⇒ a(p^k) = log p by induction; then D_a(m) = log m + Σ_{d|m, d∈C_T}a(d) ✓ | CONFIRMED |
| conditional cells | match lem:shape-weight/scale, lem:shape-est(iii) | CONDITIONAL ✓ |
| §3 reading "(E)+(F) on the window = complete places, standard local terms, nothing else" | ✓ restatement | ACCEPTED (coordinate) |
| Obs 1 (η > 2/3 ⇒ only d = 2) | d < e^{2T₀}/η < 2/η < 3 ✓ | CONFIRMED |
| Obs 2 (span) | ✓ | CONFIRMED |

## 2. Modifications
Every product-formula class is a class of combs ⇒ also closed under O7 (quartets keep the comb, lem:shape-quartet) — an additional, uniform exclusion of every cell, including the singleton ones as *deduction classes* (the O7 model has the exact PF and a negative bottom). FIX: add this line; it makes the singleton cells EXCLUDED by O7, not merely REF-D.
(Fam_η): for quartets the inequality changes by a smooth term (memo ✓); O6/O2/O10 break the collapse ✓.

## 3. (R) for (Fam_η): (1),(2),(3) met; (4) met; (6) unknown; it is a sub-statement, so (R) is not the right test — the question is whether it is true and whether (Span_η) holds. Pre-flag: EI_002 review (polar term M^{½}|W| dominates at bounded height for family vectors) suggests the family quotient is driven by the polar term — (Fam_η) may be easy (and then empty) or false; decide before investing.
## 4. REF-D: exact PF class yes; (Fam_η) no (strictly weaker if (Span_η) fails). 5. Retry: P122_009-010 (geometric), divisor-class use new ✓.
Endorsed index entries: "product formula as divisor-class coupling: NO-GO (CA_C_001 Thm 1) — and O7"; "(Fam_η): OPEN sub-statement".
