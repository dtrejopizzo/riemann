# CA_C_007 — Review

## Verdict
**Norm correction (Gram norm ‖F_s‖² = sᵀGs instead of ℓ²) ACCEPTED; CA_C_005's criticality premise correctly retracted (my CA_C_005 review flagged a different flaw — the span/family direction — which is now moot; note: positivity on the span ⇒ on the family is the right direction, as §6 says). Lemma 1, Lemma 2, Proposition 3 CONFIRMED PROVED. NUMÉRICO tables ACCEPTED as data. Conclusion "η-family positivity is FE-class generic (survives O10, O12) ⇒ EXCLUDED as a sign step" ENDORSED. §1 zero-side explanation: identity PROVED, mechanism ARGUED — classification only.**

## 1. Checks
| claim | check | label |
|---|---|---|
| Lemma 1 (tail = small window) | translates V_{log j}F₀, j ∈ (ηM,M], span a log-range of length log(1/η); centred they lie in P_{T_eff}, T_eff = T₀ + ½log(1/η) (lem:transl(i): translation keeps F̂(±i/2) = 0) ✓; e^{2T₀}/η < 3 ⇒ only contact 2 ✓; T_eff ≤ ½log3 (0.478 at η=0.7, 0.353 at η=0.9) ⇒ λ_A(T_eff) > 0 by Thm C range ✓ | CONFIRMED |
| Lemma 2 | regrouping as prop:shape-family(i); excluded divisors n < e^{2T₀}/η < 3 ✓ | CONFIRMED |
| Prop 3 | Schur complement with A_t ≻ 0 ✓ | CONFIRMED |
| §3, §5 tables | floating point, one profile; Beurling tail ill-conditioned (memo ✓) | NUMÉRICO |
| §5: x²+5y² full form negative, family positive; ζ_{ℚ(i)} family positive | ⇒ family positivity survives O10 and O12 | NUMÉRICO; exclusion by thm:shape(C) follows (with the NUMÉRICO label on the falsifier's family value) |

## 2. Process note
Several runs here go beyond "strictly necessary" for row D (the η-family was already off-route by CA_C_003). The §5 run is the one that settles the classification (FE-generic) and is accepted; further numerics on the η-family should stop.
## 3. Index: "η > 2/3 family: margin regime; one-scalar reduction s_M (PROVED); positivity FE-class generic (NUMÉRICO), Beurling-separating — not a sign step". Critical regime (full span, η ≲ 0.4) zero-driven: ARGUED.
