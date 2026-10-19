# Phase 51 — Construction of the phase→inertia functor

The phase constructs a candidate mathematical object left open by the preceding phase (GAP-158.A):
a genuine transport of the unconditional, RH-free uniform equidistribution structure of the
Kronecker flow on the Bohr torus to an invariant of the inertia/height coordinate where the zero
ordinates and the negative index of the Weil form live. It then asks whether the resulting transport
can be equipped with a canonical metric (via KK-theory / noncommutative Poincaré duality) that reads
off the Weil signature without smuggling in the Riemann Hypothesis.

## Results
- Construction of a phase→inertia transport object (𝔉_KMS) that is genuinely RH-free: CONSTRUCTION
  (Doc 160), with the five design constraints from earlier phases satisfied.
- Identification that the metric needed to read the transported object as the Weil inertia m is not
  determined by the dynamics alone — only the Weil form itself (which already enumerates the zeros)
  is known to have the right signature: GAP (Doc 160, GAP-160.A), i.e. the transport by itself does
  not yet give an RH-free inertia metric.
- Decision on whether the KK-theoretic / noncommutative-Poincaré-duality fundamental class supplies
  that canonical, RH-free metric: the candidate metric is found to carry ζ through the modular
  (Bost–Connes dual-weight) structure, reproducing a structural circularity: NO-GO (Doc 161, Theorem
  161.9 structural circularity) — ending in a genuine no-go rather than the hoped-for construction.

## Documents
- `160-construction-of-the-phase-inertia-functor-transport.md` — constructs the RH-free phase→inertia transport 𝔉_KMS.
- `161-canonical-inertia-metric-via-noncommutative-poincar.md` — decides whether a canonical KK/Poincaré-duality metric closes the gap; ends in a no-go (structural circularity).

## Relation to other phases
Follows `phase-50-diophantine-thread` (GAP-158.A) and feeds `phase-52-homotopy-inertia`, which takes
the Doc 161 circularity as its starting obstruction and asks whether m can instead be read as a
metric-free secondary homotopic invariant.
