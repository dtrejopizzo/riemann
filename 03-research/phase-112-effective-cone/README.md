# Phase 112 — Requirement d5: the effective cone

Row (d)'s Hodge-index argument needs an effective cone Eff — a set of divisors with D·H>0 against a
polarization H — that is genuinely the classical cone of sections (D effective iff h⁰(D)>0), not merely
a posited positivity. Using the polarization already identified in phase 107 (H = F_v+F_h, H²=2>0) and the
divisor assignment f ↦ D_f, the phase builds a candidate cone and tests whether it carries real sections
content or only formal positivity.

## Results
- D_f·H = f̂(0)+f̂(1) > 0 for f≥0: holds, but is shown to be a restatement of positivity of an integral, with no geometric content. PROVED (formal only).
- f≥0 ⟺ u_f convex, via u_f''(r)=f(r)/r: a genuine real characterization ("no subtraction needed in the DC decomposition") but not a statement about sections. PROVED, but not sufficient.
- Disjoint-support falsifiability test: 142 pairs checked, 0 negative, 0 sign flips, with truncation convergence verified under refinement. NUMERICAL (supporting evidence, not proof).
- D_f² < 0 for narrow bumps: expected and not a refutation, since effective divisors can have negative self-intersection when there is no common component (classical blow-up example). ARGUED.
- Headline verdict: d5 is satisfied only formally (outcome b) — no h⁰ exists in this category, so the classical step "h⁰(nD)→∞ hence nD effective" has nothing to land in; building h⁰ is requirements d3/d4, themselves blocked upstream by d1. NO-GO (for a genuine sections-based effective cone, at this stage) / OPEN (pending d1/d3/d4).

## Documents
- `112_00_PHASE_112_PLAN.md` — statement of requirement d5 and what a genuine effective cone must be.
- `112_01_THE_CANDIDATE_CONE.md` (+ `.py`) — construction of the candidate cone and the D_f·H>0 computation.
- `112_02_IS_IT_THE_RIGHT_CONE.md` (+ `.py`) — the convexity characterization and the disjoint-support falsifiability test.
- `112_03_VERDICT.md` (+ `.py`) — the D_f²<0 discussion and final verdict.
- `112_99_PHASE_112_SUMMARY.md` — consolidated verdict.

## Relation to other phases
Uses the polarization and divisor assignment built in phase 107; explicitly traces its gap (no h⁰) back to requirements d1/d3/d4, which phases 110–111 and later phases address.
