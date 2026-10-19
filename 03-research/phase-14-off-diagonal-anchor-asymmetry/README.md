# Phase 14 — Off-diagonal structure, the anchor framework, and why the known routes collapse to one wall

The phase pursues two linked questions: (1) where, if anywhere, does the prime-factor-counting
function ω(n) touch the zeros of ζ exactly rather than merely through statistics of values; and
(2) what precisely is the logical ingredient missing to turn an unconditional zero-density result
into an unconditional zero-absence result. It develops a ζ-free "anchor" (Landau singularity)
framework to organize every known absence mechanism, tests it against the one proven case of RH
(function fields), and audits the program's remaining structural/positivity line for anything not
already reducible to a known barrier.

## Results

- The explicit formula is ω-blind: ω(p^a)=1 for every prime power, so any ω-weight enters only as a trivial overall factor — **PROVED**.
- The first exact, non-trivial bridge between the ω-weight and the zeros is through the additive-divisor correlation and its Motohashi spectral expansion — **PROVED** (exact identity, verified numerically against the leading asymptotic).
- The z^ω-weighted spectral modification is non-trivial as an extra Euler factor G_z(s) — **PROVED**, with G_z ~ ζ(s)^{2(z-1)} near s=1.
- G_z is entirely expressible as a product of ζ(Ns)-powers (constant Satake parameters ⟹ ζ-isobaric): the ω-weight is spectrally **self-referential**, contributing no new irreducible object — **PROVED**; line closed.
- N8: the density→absence gap is characterized as exactly the square-root-cancellation barrier, unifying it with the "wrong-sign capstone," N7, and the meta-obstruction — **ARGUED/characterized**, not a new theorem.
- N8's claimed universality is **REFUTED**: de la Vallée Poussin's classical zero-free theorem at σ=1 proves absence with no cancellation estimate at all, using only an algebraic positivity identity and the pole's location.
- The "anchor" (Landau singularity of a positive measure's transform) is formalized ζ-free, with a theorem recovering de la Vallée Poussin as the σ=1 instance — **PROVED** (Theorem A), but its reach is shown to be structurally confined to a shrinking neighborhood of the abscissa, never the center.
- Tested against the one proven RH (function fields): the anchor there collapses to the trivial-cohomology edge pole; the actual RH-proving mechanism is the Hodge index theorem (a definiteness/signature statement), not a center-anchor — **verdict: the anchor construction collapses**; the missing ingredient is reframed as a Hodge-index theorem on a 2-dimensional arithmetic geometry over Spec ℤ.
- Audit of the structural/positivity line (P7→T2→D2→T3→T4, localized Weil form and its ground state): every object reduces to the known square-root/capstone wall via λ_min = (π²/6)β_min² — **collapse confirmed**; no fifth kind of object found. One genuinely new, RH-independent object survives (Conjecture B2, an Euler-product classification statement) but does not bear on zero location.

## Documents

- `STRATEGIC-where-omega-touches-the-zeros.md`, `M14.1-...motohashi.md`, `M14.2-...spectral-modification.md`, `M14.3-...self-referential-close-the-line.md` — the ω/Motohashi line, from strategic redirection to closure.
- `N8-the-density-to-absence-gap.md` — characterization of the square-root cancellation barrier.
- `BREAK-N8-the-anchor-asymmetry.md` — refutation of N8's claimed universality via de la Vallée Poussin; introduces the anchor-asymmetry reframing.
- `ANCHOR-framework-a-classification-of-zero-absence.md` — the ζ-free anchor/sum-rule/Landau-singularity framework and its open construction question Q(anchor).
- `STAGE1-2-anchor-vs-definiteness-the-verdict.md` — tests the anchor framework against the function-field proof of RH; verdict that it collapses to Hodge-index positivity.
- `AUDIT-P7-structural-line-collapse.md` — audit of the localized-Weil-form structural line, tracing its collapse to the square-root wall.
- `experiments/` — numerical scripts supporting the above (additive-divisor verification, spectral modification checks, autocorrelation and cancellation tests).

## Relation to other phases

The Hodge-index reframing at the end of this phase (a definiteness theorem on an arithmetic surface for Spec ℤ) anticipates the direction later pursued as the program's row-D/positivity work in subsequent phases.
