# Phase 15 — The Anatomy–Kreĭn–Hodge program: transcribing Weil's function-field proof to Spec ℤ

The phase attempts to transcribe Weil's function-field proof technique (an intersection pairing on
a surface, made positive-definite by the Hodge index theorem) to Spec ℤ, using three tools built
earlier in the program: the "anatomy" (a spectral arithmetic Frobenius with Satake recovery), the
localized Weil form viewed as a Kreĭn/Pontryagin pairing, and a Hodge–Riemann stability theorem.
It builds as much of the scaffold as is unconditionally available, isolates the precise missing
ingredient, audits several external claims to have closed the gap, and ends by mapping concrete
non-circular paths forward.

## Results

- M1, the arithmetic intersection pairing (Lefschetz trace identity = the explicit formula as a sum of local intersection numbers; effectivity Γ·Γ ≥ 0 via a Rankin–Selberg square) — **PROVED**, verified numerically to 10⁻¹².
- M2, the ample cone / trivial-cohomology part is positive — **PROVED** unconditionally (the de la Vallée Poussin / Landau edge positivity).
- Proposition C: RH ⟺ the pairing is positive semi-definite on the primitive part — **PROVED** (an equivalence, not new content).
- M3, the arithmetic Hodge index on the primitive part: shown equivalent to RH via three faces (geometric signature, Montgomery-type uniform form factor, Hodge–Riemann-stability strict definiteness) — this equivalence is **PROVED**; M3 itself remains **OPEN** (it is RH).
- Eight attempts (M3, Attempts 1–8) at supplying the missing positivity/Lefschetz structure directly — all **NO-GO** or reduce to the same gap; Attempt 5 notes a *proven* general arithmetic Hodge index (Faltings–Hriljac, Yuan–Zhang) exists but, per Attempt 6, controls heights (Néron–Tate), not the zero-carrying cohomology.
- Precise identified gap: an independent, positive, infinite-dimensional hard-Lefschetz 𝔰𝔩₂-structure (Kähler class ω) on the primitive Kreĭn space, commuting with the Frobenius operator 𝒯, that cannot be built from 𝒯 alone — **stated as the sole missing object**, not proved to exist or not exist.
- M7: an external "Structural Incompleteness Theorem" is audited and found correct, independently re-deriving this phase's own conclusion (one sub-lemma's proof repaired) — **confirmed convergence**.
- M8: an external claimed "proof of RH" via the Connes scaling action is audited and found **REFUTED** — its key integer-grading theorem rests on a false hypothesis (the scaling action has continuous, not compact, spectrum).
- M9: a guarded discovery run on constructing 𝒦_geom returns three candid negatives (confirming M5/M6/M8) plus one new RH-independent constraint (a Δ₃ statistic plateau); no fabricated proof.
- M10: an external "Arakelov–RH equivalence" theorem is audited — the forward direction (constructing the witness variety ⟹ RH) is correct but near-tautological; the claimed reverse direction is **NOT rigorous** and may be false — verdict: one-directional, not a biconditional.

## Documents

- `00-PHASE-15-overview.md` — the program's three tools and the M1–M3 milestone plan.
- `M1-arithmetic-intersection-pairing.md`, `M2-ample-cone-edge-positivity.md`, `M3-arithmetic-hodge-index.md` — the core constructions.
- `M3-attempt5` through `M3-attempt8`, `M3-genuine-attempts-on-the-core.md` — the eight attempts at the Hodge-index step.
- `M4-the-chosen-direction-archimedean-modular-omega.md`, `M5-the-lefschetz-dichotomy-closure.md`, `M6-the-prismatic-route-assessment.md` — further direction-finding and closures.
- `SYNTHESIS-M1-to-M3-and-the-precise-gap.md` — the full self-contained synthesis, the precise gap statement, and five concrete forward paths.
- `M7-advisor-incompleteness-theorem-audit.md`, `M8-front1-proof-audit-REFUTED.md`, `M9-discovery-run-1-assessment.md`, `M10-arakelov-equivalence-audit.md` — audits of external claims.
- `experiments/` — supporting numerical verification scripts (including a falsifier for the M8 claim).

## Relation to other phases

Builds on earlier anatomy (P19), Kreĭn-form (P16), and Hodge–Riemann-stability (P20) results from preceding phases; its "construct 𝒦_geom / the witness variety" target is the direct antecedent of the SURF-geometry search continued in phases 173–175.
