# Phase 6 — Osterwalder–Schrader reflection positivity: a moonshot attempt and its refutation

The phase asks whether Weil's positivity criterion can be recast as Euclidean-field-theory
Osterwalder–Schrader (OS) reflection positivity, with the functional-equation symmetry playing the role
of the reflection, in the hope that per-place (per-prime) reflection positivity plus OS reconstruction
would force the sign and even hand over a Hilbert–Pólya operator for free. The phase computes the
local prime form explicitly to test the mechanism.

## Results
- Recasting of Weil's criterion as an OS reflection-positive form, with the reflection identified as
  the Weil involution itself: PROVED as a faithful recasting (not a new mechanism); an initial
  variant using a separate linear reflection operator is retracted as incorrect.
- Claim that OS reconstruction yields a Hilbert–Pólya self-adjoint operator "for free": RETRACTED —
  the two-point function is oscillatory, not of the decaying type OS reconstruction requires.
- Per-place (local prime) reflection positivity: computed exactly, $G_p(r) = \frac{2\log p}{p|1-z_p|^2}(\sqrt p \cos(r\log p) - 1)$,
  and shown to be INDEFINITE (both signs attained) for every finite prime $p$: REFUTED. This is a
  rigorous no-go for the Euler-lattice mechanism (per-place positivity + tensor gluing ⟹ global
  positivity), establishing that Weil positivity does not localize per prime but is a genuine
  cross-place phenomenon.
- Follow-up attempt to reduce RH to a pointwise comparison "archimedean envelope ≥ prime comb": FLAWED
  and retracted — the prime comb is distributional (it encodes the zeros as negative deltas), so no
  pointwise comparison is valid; what survives is only the standard (RH-tied, already known) heuristic
  link between zero clustering and large values of $S(T)$, not a new sound reduction.

## Documents
- `M-OS-1-S1-setup.md` — the OS recasting of Weil's criterion (with later corrections noted inline).
- `M-OS-2-S2-local-REFUTATION.md` — the explicit computation of $G_p$ and the per-place no-go.
- `S2-followup-incoherence.md` — the attempted pointwise reduction and its retraction.
- `S2f-PROGRESS-CANDID.md` — candid summary of what survived and what was refuted across the phase.

## Relation to other phases
The no-go on per-place positivity is consistent with, and reproduces in a new language, the
cross-place (archimedean vs. prime) obstruction identified independently in the Kreĭn-space program of
`phase-4-krein-space-realization`/`phase-5-structural` (route B, P8's Theorem C).
