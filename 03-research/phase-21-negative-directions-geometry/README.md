# Phase 21 — geometry of the negative directions of the Weil form

Rather than attacking the positivity question directly, the phase builds a
pure-mathematics theory of the maximal negative subspace 𝒩 of the localized
Weil (Kreĭn) form, asking what geometric properties any nonzero 𝒩 would
necessarily have — its dimension parity, its decomposition into orbit
pieces, and whether a finite nonzero dimension can be excluded. No
numerics, no pair correlation, no de Branges/SURF/GUE hypotheses, and no
RH-equivalent statement are used as inputs.

## Results
- Theorem 21-A.1 (parity): the negative index κ of the Weil form for ζ (or
  any primitive real Dirichlet L-function) is always even; the minimal
  nontrivial value is 2, since the Klein four-group action pairs each
  off-line zero orbit into independent contributions at heights +γ and -γ.
  **PROVED**.
- Theorem 21-A.3 / Corollary: κ = 2m exactly when there are m independent
  off-line orbits. **PROVED**.
- Theorem 21-B.1 (angular separation): the sub-orbit contributions at
  different heights are orthogonal up to an exponentially small error.
  **PROVED**.
- Theorem 21-B.2 (direct decomposition): 𝒩 splits as an orthogonal direct
  sum of 2-dimensional Lorentz planes ℝ^{1,1}, one per off-line orbit, up to
  the same exponentially small correction. **PROVED**.
- Exclusion Conjecture EX (that 0 < κ < ∞ is impossible, forcing κ ∈
  {0, ∞}): formulated and analyzed via Kreĭn-Langer factorization; shown
  to be consistent with pure functional analysis (no contradiction exists
  at that level alone) and shown to require an arithmetic input beyond
  functional analysis (the Euler product / Selberg-class uniqueness /
  spectral rigidity / linear-independence hypothesis), none of which
  currently yields a proof. **OPEN** (Theorem 21-D.1 only records the
  formal structure of the Pontryagin regime if 0 < κ < ∞ were to hold).

## Documents
- `00-setup.md` — ground rules, central object (the Kreĭn form Q, its
  negative subspace 𝒩 and index κ), and the phase's goals.
- `01-parity-and-geometry.md` — the parity theorem, angular separation, and
  the direct Lorentz-plane decomposition of 𝒩 (21-A, 21-B).
- `02-exclusion-principle.md` — statement and audit of Exclusion Conjecture
  EX, the Kreĭn-Langer factorization analysis, and the open obstacles to
  proving it.

## Relation to other phases
Builds on the symmetry-vs-positivity analysis (P29) and on the
Klein-group orbit structure of off-line zeros used in phase 18's portrait
of negative directions; identifies the Lorentz-plane decomposition as the
basis for a further defect theory and exclusion-principle search left open
for later phases.
