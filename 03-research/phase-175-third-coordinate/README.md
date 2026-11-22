# Phase 175 — Searching the literature for a geometric triple (H¹, Q, transfer map)

Phase 174 left open the construction of a genuine geometric/cohomological object carrying row D's
positivity. This phase reads the relevant literature in full — Álvarez López–Kordyukov–Leichtnam
(dynamical trace formulas), Deninger (rational Witt vector systems), Borger (Witt-vector jet
spaces), and Connes–Consani — to check whether any of them already supplies the required triple:
a cohomological H¹ with the right zero spectrum, a positive Hermitian form Q on it, and a transfer
map identifying Q with ζ's explicit formula.

## Results

- AKL's dynamical trace formula (their Theorem 1.3.10) — **PROVED** in their own paper, but it builds no specific arithmetic measure, no form Q, and does not identify its distribution with ζ's explicit formula; the authors themselves leave the arithmetic framework pending.
- Deninger's Witt-vector system X_E reproduces the von Mangoldt comb π = Σ Λ(n)δ_{log n} exactly — **PROVED** as an inference of this phase — but Deninger's own H¹ (his Theorem 10.2) is only H⁰ = R; no H¹ with the right zero spectrum, no Q, no Lefschetz formula matching ζ's is built — **NO-GO**.
- Borger's square W*(Spec Z) is not the same object as Spec Λ = W_*(A¹) (the jet space of the line, not of Spec Z); Borger's own framework states it says nothing about the archimedean place — **NO-GO** (missing cohomological object and missing archimedean place).
- Full gate audit (OT-1…OT-12 from phase 158) applied to AKL/Deninger as candidate arithmetic triples: all failed except OT-3 (definitional independence of the carriers, **PROVED**) — the rest **NO-GO**, meaning an unverified requirement, not a nonexistence proof.
- Round-by-round construction attempts (dynamics/renormalization, Witt/bivariate theory, recodings) all **NO-GO**; a pre-renormalization-positivity-implies-finite-part-positivity inference is explicitly shown **false** (PROVED) via a finite-part computation.
- H1–H5 gate summary: H1 (X defined without ζ) PROVED for the cited carriers; H2 (σ constructed) PROVED for the analytic output, NO-GO for a cohomological realization; H3 (sign of Q_X without using σ), H4 (exact transfer to W), H5 (falsifiers separating P₁₇₁, Davenport–Heilbronn, Ξ_a, Ξ_Q) all **NO-GO**.
- Overall verdict: **NO-GO** — row D remains open; nothing in the phase proves RH, and no impossibility theorem is claimed either.

## Documents

- `R175_FINAL.md` — literature audit against the OT-1…OT-12 gates, three rounds of construction attempts (A: dynamics/renormalization, B: Witt/bivariate, C: recodings), and the final H1–H5 gate table against Paper 47 §28.4's six clauses.

## Relation to other phases

Follows directly from phase 174's unresolved classification; cites phase 159 (G1_B5_R3) and phase 160 (R160_C4_R1) for related Witt/Coulomb-correction attempts, and Paper 47 §28.4 for the six clauses any successful construction must satisfy.
