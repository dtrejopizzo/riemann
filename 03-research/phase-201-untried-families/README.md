# Phase 201 — Families nobody used

## Phase objective
Phase 200 proved that all the already-used method families (LP/SDP certificates, Weil forms, mollifiers,
trace formula, Arakelov/Hodge, de Branges, moments, gauges, quotients, theta, von Neumann, Loeb, oscillation,
entire correspondences) do not suffice: Theorem Φ200 + 36 constraints (MAP_200_001). Nothing new is known about
the sign. **Phase 201 exclusively explores method families that nobody used for Weil positivity**, neither in the
corpus (routes index, now ROUTES-MASTER-INDEX.md; ~1,700 routes) nor in the literature (survey + new searches).

## Rules
- never D⟺RH.
- Every proposed family is verified as virgin: grep of the index (0 hits or entry cited with a reason for
  non-coverage) + bibliographic search ("Weil positivity", "explicit formula", "positive definite" + family name).
- Every family is filtered BEFORE construction by SPEC-𝔇 S1–S6 (HORN_B_BIGSHARP_001 §3) and by the 5 branches of
  Φ200 (MAP_200_001 §2): declared Λ channel and named falsifier (Epstein 11, DH 12, a_P, cΛ, Beurling).
- Nothing in the index is retried without a new written reason.

## Stages
1. Inventory of virgin families (two disjoint work lines) → FAMILIES_A/B_001.md.
2. Synthesis and ranking by S1–S6 → SPEC_201_001.md. Choice of ONE family.
3. Long constructive attempt with a fixed team (persistent line + audit + calibration).

## Status
- Stage 1 DONE: FAMILIES_A (30) + FAMILIES_B (32): 39 non-virgin, 21 virgin-but-dead (G1, Thm 3′, Φ200 branches),
  6 viable. Stage 2 DONE: SPEC_201 — chose B-V1 nonnegative rank (corrected by the diagonal-invariance lemma);
  finite and decidable Lemma V1.1′; second option B-V2 recurrence {x+y,xy}.
- Stage 3 IN PROGRESS: persistent line (V1_1_NONNEG_001) + audit (AUDIT_201_SPEC_001).
- Stage 3, family 1 (nonnegative rank): NO-GO PROVED at the first lemma (I_T ≡ 0 by blocks ≤ 3 columns; 1,080
  exact matrices confirm it). Audit: branch 2 + C-emb (a). Family 2 IN PROGRESS: recurrence {x+y, xy}.
- Family 2 (recurrence {x+y,xy}): NO-GO PROVED at the pre-test (Theorem V2-0: finite data). Family 3 (sign rank)
  is not launched (same theorem). New filters S7, S8. Next: inventory C with S7/S8 from the start.
- Inventory C (S7/S8, 14 families): 0 viable; lemmas L-loc, C-pos, S-0/S-1/S-2, P-fin. Pattern: intrinsic
  positivity with the Λ channel in the hypothesis = branch 2 (ARGUED).
- CPOS_CLASS_001: class Theorem C-pos ((i),(ii),(γ) PROVED; (α) PROVED if κ_T≠0; (β) ARGUED) → P46 thm:noimport.
  **Phase 201 closed by theorem**: no imported positivity with a uniform construction on the comb can give the sign.
  Main output (h1): non-uniform construction = exterior = table (★★) of phase 199. Decision pending.
</content>
</invoke>
