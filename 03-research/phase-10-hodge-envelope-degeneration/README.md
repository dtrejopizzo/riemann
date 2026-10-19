# Phase 10 — The cohomological turn: Hodge-envelope degeneration

The phase tests the one route that could in principle escape the "wrong-sign capstone" (the observation that
every unconditional handle on the zeros is a positivity giving lower bounds, while the target needs an upper
constraint): a higher-level Hodge-index positivity, in analogy with the Weil-conjectures-for-curves proof,
that would yield the needed upper bound by duality. It builds a finite-dimensional Weil–Carleson intersection
form, grows the cohomology dimension toward ζ, and measures what happens to its positivity.

## Results
- M10.1: the bare Hodge gap of the intersection form shrinks to zero and the signature degenerates (null directions appear) as the band grows toward ζ — the cohomological face of the previously found "N3 saturation". NUMERICAL.
- M10.2: the regularized Hodge gap (smallest eigenvalue of the sine-kernel Gram matrix of the zeros, after removing trivial null directions) stays positive and even grows as the band resolves more zeros — first positive numerical sign for the route. NUMERICAL.
- M10.3: at fixed sampling ratio, the regularized gap is stable (≈0.20–0.29) across three orders of magnitude in height, the first numerical evidence consistent with a uniform lower frame bound. NUMERICAL.
- M10.4: the regularized Hodge gap prices out to exactly λ_min(G) = (π²/6)β_min² (deep-run identity), which is the identical exchange rate as an earlier pair-correlation route (T9-cal) — the cohomological and pair-correlation languages describe the same target. PROVED (identity), the route does not beat the prior one.
- M10.4: even in this two-sided determinantal/frame language, the operative direction (lower frame bound) is shown to be itself an upper-clustering constraint, so the wrong-sign capstone survives even the most favorable reformulation attempted. ARGUED — capstone confirmed, route does not escape it.
- Durable by-products: the identity λ_min(G)=(π²/6)β_min²; a four-way unification (N3 saturation = vanishing Hodge gap = intersection-form degeneration, in the relevant finite models); a reformulation chain connecting uniform Riesz sequences, A₂ condition, and S(T) extremal regularity. PROVED/ARGUED as stated in the documents.

## Documents
- `PHASE-10-NEW-MATHEMATICS-the-cohomological-turn.md` — rationale and program (Weil-conjectures-for-curves template).
- `M10.1-verdict-degenerate-hodge.md`, `M10.2-verdict-regularized-gap-survives.md`, `M10.3-verdict-uniform-frame-S(T).md`, `M10.4-verdict-route-priced-capstone-holds.md` — the four milestone verdicts.
- `DEEPRUN-analysis-M10.1-M10.3.md`, `REPORT-M10.1-to-M10.3-cohomological-turn.md`, `deeprun_M10.1-M10.3.png` — consolidated deep-run analysis and figure.
- `experiments/` — scripts computing the Hodge envelope, regularized gap, uniform frame bound, and the deep-run figure.

## Relation to other phases
Framed explicitly as pricing identically to an earlier pair-correlation route (T9-cal) from a preceding phase; its conclusion (the capstone holds even in the most favorable two-sided reformulation) closes the cohomological line of attack for later phases.
