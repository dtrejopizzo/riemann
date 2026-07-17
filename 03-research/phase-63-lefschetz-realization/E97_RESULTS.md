# E97 — polarized-isometry test (R1, first attempt): INCONCLUSIVE — wrong form + numerical instability

**Date:** 2026-06-27 · float64 · ζ vs DH falsador. Uses the phase-60 `E3_ccm_real` Connes operator
`H_x` (validated there: eigenvalue 14.105 vs γ₁=14.135 at λ=11).

## What was tested

The F_q→RH mechanism is: Frobenius is a *self-adjoint endomorphism of a positive polarization*, so
positivity forces real spectrum (eigenvalues on the line). Spec-ℤ analog: the Connes scaling
operator `H_x` (spectrum ≈ zeros). Test: `RH ⟸ (QW ⪰ 0 AND H_x is QW-self-adjoint) ⟹ real spectrum`.

## Result — the test as built cannot decide; three failures

| observable | ζ | DH | reading |
|---|---|----|---------|
| QW signature | (67,14) indefinite | (71,10) indefinite | **QW is NOT the PSD polarization** for either |
| H_x QW-self-adj defect | 0.13 | 0.16 | H_x is **not** QW-self-adjoint |
| #complex eigenvalues of H_x | 22, 36 | 12, 4 | **falsador inverts** → artifacts |

1. **Wrong polarization.** The Cauchy–Toeplitz `QW` (Connes constrained-minimizer form) is indefinite
   for *both* ζ and DH. The PSD polarization the program actually found (Phase 62 / E94) lives on
   **V₊** (the +i-eigenspace of the quaternionic `J`) inside the *engine's* Weil matrix `A`, a
   different object. E97 paired `H_x` with the wrong form.
2. **No self-adjointness.** `H_x` is not QW-self-adjoint (defect ~0.13), so the mechanism is absent
   for this pairing — unsurprising given (1).
3. **Numerical artifacts, not off-line zeros.** DH (which has off-line zeros) shows *fewer* complex
   eigenvalues than ζ — backwards. The complex spectrum comes from the ill-conditioned `ξ = QW⁻¹δ`
   solve in float64 with an indefinite, near-singular QW; it is noise, not arithmetic.

## Honest status — no conclusion either way

E97 does **not** establish or refute the polarized-isometry mechanism. It establishes only that this
*particular* realization (E3's `H_x` + its Cauchy–Toeplitz `QW`, float64) is unsuitable: wrong form,
unstable inverse. No false victory and no false no-go.

## The clean test (R1, redo)

1. **Match the operator to the PSD polarization.** Work in the engine's `A`/`J`/`V₊` framework
   (where positivity is real, Phase 62), and build the scaling/Frobenius operator *there* — or solve
   for the form `G` w.r.t. which the scaling operator is self-adjoint and test **its** positivity.
2. **mpmath dps≥40.** The `QW⁻¹` instability is fatal in float64; the residue is `e^{−cL}`.
3. **Note the obstruction already visible:** the scaling generator `D_log = diag(2πn/L)` does **not
   commute with `J`** (J flips `n→−n`), so it does not preserve V₊. The scaling action and the
   quaternionic structure are *incompatible on the window* — which may itself be the operator-level
   face of MW-5 (no Frobenius compatible with the polarization). This is the first concrete lead to
   chase in the redo.
4. **F_q positive control (R3):** build the analog for a curve over F_q and confirm the test PASSES
   there (Frobenius IS a polarized isometry of a PSD form), isolating exactly what Spec ℤ lacks.

## Reproduce

```
venv/bin/python E97_polarized_isometry.py "[(11.0,40,500),(20.0,60,800)]"
```
