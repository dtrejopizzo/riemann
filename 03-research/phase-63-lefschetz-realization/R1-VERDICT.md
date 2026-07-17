# R1 verdict — the scaling generator is complex-ANTILINEAR w.r.t. the polarization (operator-level MW-5)

**Date:** 2026-06-27 · Phase 63 · follows E97 (inconclusive crude test) + the clean engine-framework check.

## The clean finding

In the engine's framework (Weil matrix `A`, quaternionic complex structure `J` with `J²=−1`, where
Phase 62/E94 found `A ⪰ 0` on V₊), the scaling/Frobenius candidate is the generator
`D_log = diag(2πn/L)`. Two exact measurements (ζ, λ=11 and 17, mpmath dps=40):

- **`‖[D_log, J]‖ / ‖D_log‖ = 2.000` exactly** — `D_log` **anti-commutes** with `J`:
  `D_log J = −J D_log`. (Analytic: `J` flips `n→−n`; `D_log`'s symbol `2πn/L` is *odd* in `n`.)
- **A-self-adjointness defect of `D_log` ≈ 0.09** — `D_log` is *nearly* `A`-self-adjoint.

## Interpretation — why there is no Frobenius on the window

In a polarized Hodge structure with complex structure `J`:
- operators that **commute** with `J` are complex-**linear** = *morphisms of the Hodge structure*.
  **Frobenius must be of this type** (it is what forces RH over F_q: a polarized linear isometry
  whose eigenvalues positivity pins to the line).
- operators that **anti-commute** with `J` are complex-**antilinear** (like conjugation / a real
  structure) — they map V₊ → V₋ and are **not** morphisms.

The scaling generator is **antilinear** (exact anticommutation). Equivalently: J-linear operators
have symbol **even** in `n` (functions of `|n|`); the scaling generator's symbol is intrinsically
**odd** in `n`. The zeros are the spectrum of this odd, antilinear operator. So:

> **The zeros live in the complex-antilinear sector of the polarization; Frobenius must be linear.
> The natural dynamics on the window (scaling) is the wrong type to be confined by the polarization.**

This is a concrete, exact, operator-level statement of MW-5: not only is the polarization gapless
(Phase 62, form side) — the operator whose spectrum is the zeros is *antilinear* w.r.t. that
polarization's complex structure, so positivity (a property of the linear/Hermitian sector) cannot
constrain it. There is no Frobenius (J-linear, spectrum = zeros) on the finite window.

## Honest status

- This is a **sharp negative**: it identifies *why* the F_q→RH mechanism does not transfer at the
  operator level — a type mismatch (antilinear scaling vs linear Frobenius), exact and reproducible.
- It does **not** prove no Frobenius exists in a larger/true cohomological realization — only that
  the natural window operator is the wrong type. Whether a genuine J-linear operator with
  spectrum = zeros exists is exactly the open MW-5 question (the Connes–Consani / Deninger object).
- E97's crude attempt was inconclusive (instability); this engine-framework check is the real R1
  result. No false victory, no false no-go.

## What remains (R3, the decisive control)

Build the **F_q curve analog** and verify the contrast: there, Frobenius is **J-linear** (commutes
with the Hodge complex structure, even-type) and its eigenvalues are pinned by the (gapped)
polarization → RH is a theorem. Confirming that the *same* test gives commuting/linear Frobenius
over F_q but antilinear scaling over Spec ℤ would make MW-5 precise: **the missing object is a
J-linear (Hodge-morphism) Frobenius, which exists over F_q and not on the ℤ window.**

If R3 confirms the contrast → Phase 63 delivers a sharpened MW-5 statement (publishable as the
precise obstruction), not RH. If no J-linear zero-spectrum operator can exist even in principle,
that is the final wall and the program stops here (per David's plan).
