# Phase 22 — arithmetic consequences of a finite Pontryagin defect

Starting from the hypothesis "D" that the negative index of the Weil form is
finite and nonzero (κ = 2m, 0 < m < ∞, i.e. finitely many off-line zero
orbits), the phase asks what such a finite defect would leave behind in the
Chebyshev prime-counting function ψ(x), and searches for an unconditional
invariant that would be incompatible with its existence (pursuing Exclusion
Conjecture EX from phase 21). No numerics, pair correlation, de Branges/
SURF/GUE inputs, or RH-equivalent hypotheses are used; only Perron's
formula, the factorization ξ = ξ₀·P_{4m}, the Euler product, the functional
equation, and classical complex analysis.

## Results
- Definition and anatomy of the arithmetic defect D_m(x) = Σ (over off-line
  orbits) x^ρ/ρ, a finite real exponentially growing function, and the
  associated "virtual" function ψ₀ for the on-line part. **Constructions**,
  no sign attached.
- Theorem 22-C.1: an unconditional Korobov-Vinogradov zero-free-region bound
  forces each off-line shift b_j to shrink as b_j ≲ (log γ_j)^{-2/3}
  (log log γ_j)^{-1/3}; large-height off-line zeros must lie exponentially
  close to the critical line. **PROVED**, but explicitly noted not to give a
  contradiction (energy still grows, just sub-linearly).
- Corollary 22-C.2: controlled sub-linear growth of the defect's "energy"
  under Hypothesis D. **PROVED**.
- The Paley-Wiener argument (§C.2) is shown to reach exactly the boundary
  Re(s) = 1 and no further into the critical strip, so it cannot by itself
  exclude a finite defect.
- Proposition 22-D.1 (spectral dichotomy): under Hypothesis D, the spectrum
  of (ψ(x)-x)/√x splits into a continuous part (on-line zeros) and a
  discrete, growing-amplitude part at frequencies ±γ_j (off-line zeros).
  **PROVED**.
- Lemma 22-D.3 and Conjecture 22-D.1: a proposed route to contradiction via
  incompatibility between a finite discrete spectral defect and the
  (conjectural) absolutely-continuous spectrum of the Gaussian multiplicative
  chaos (GMC) model of ψ fluctuations; the logical chain Euler product ⟹
  GMC ⟹ ¬Hypothesis D ⟹ m = 0 is set up but depends on unproved GMC
  structure-function estimates. **CONDITIONAL / OPEN**.
- This GMC-incompatibility route is explicitly distinguished from (and not
  blocked by) an earlier no-go result (capstone N1) that the ω/chaos
  program alone cannot certify RH directly.

## Documents
- `00-setup.md` — ground rules, Hypothesis D, and the central arithmetic
  defect object.
- `01-modified-explicit-formula.md` — the modified explicit formula, the
  defect D_m(x), and the virtual function ψ₀.
- `02-invariants.md` — zero-free-region bound on the off-line shifts
  (22-C.1/C.2) and the Paley-Wiener boundary analysis.
- `03-spectral-rigidity.md` — the spectral-dichotomy proposition and the
  proposed GMC-incompatibility route toward Exclusion Conjecture EX.

## Relation to other phases
Direct continuation of phase 21 (Lorentz decomposition, Exclusion
Conjecture EX); the unresolved GMC structure-function estimate is handed
off explicitly as "the precise task of Phase 23."
