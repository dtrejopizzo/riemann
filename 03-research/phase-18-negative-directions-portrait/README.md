# Phase 18 — a portrait of the negative directions of the Weil form

Instead of building a new realization, the phase dissects the explicit
object (from earlier phases) whose existence is equivalent to a negative
eigenvalue of the localized Weil quadratic form: the off-axis evaluation of
an off-line quartet ρ = ½ + b + iγ. It asks what any such negative direction
must inevitably look like, and whether neighbouring on-line zeros can
protect against it.

## Results
- Four inevitable structural properties of a negative direction, all
  numerically verified: shallowness O(b²) per direction (P1), concentration
  on the sinh-sine ("imaginary", off-line) mode rather than the cosh-cosine
  mode (P2), frequency localization at the ordinate γ (P3), and a fourth
  property stated in the source (P4). **NUMERICAL** verification of an
  analytic claim.
- Case B (local protection by neighbouring on-line zeros): the embedded
  bottom eigenvalue matches the isolated one to 4-5 significant figures
  across tested zero spacings down to 0.7; protection does not occur.
  **REFUTED**
- The negative-direction packet sits at frequency γ, narrower than the zero
  spacing, so neighbours barely overlap it — a genuine physical mechanism,
  not a numerical artifact.
- Conclusion: any mechanism against the negative direction must be global
  and lies in the pair-correlation regime already identified elsewhere as
  the governing obstacle; no new non-local handle was found. **NO-GO** for
  a local protection mechanism.

## Documents
- `01-negative-directions-portrait.md` — the rank-2 Weil form on a quartet,
  its negative eigenvector, and properties P1-P4.
- `02-explicit-formula-coupling.md` — embeds the quartet among on-line zeros
  and tests whether the neighbourhood protects against the dent (Case A vs
  Case B).
- `experiments/` — two Python scripts computing the eigenvalues/eigenvectors
  used in the two documents.

## Relation to other phases
Follows the symmetry-vs-positivity dichotomy and the explicit isolation of
the negative-direction object from earlier phases; recommends consolidating
the portrait and exploring a separate line built from multiplicative
statistics rather than continuing this direction further.
