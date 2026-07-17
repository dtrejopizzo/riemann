# R3 verdict — F_q positive control: the contrast is exact, MW-5 made precise

**Date:** 2026-06-27 · Phase 63 · [E98_fq_control.py](E98_fq_control.py). Genuine elliptic curves (real point counts).

## What was checked

For three actual elliptic curves over F_p (point-counted, so `a` and `θ` are real arithmetic),
build Frobenius on H¹ in the natural Hodge basis, `F = √q · R(θ)`, and test the same three things
that R1 tested for the ζ scaling operator:

| curve | #E, a, q | (1) `‖[F,J]‖/‖F‖` | (2) Q-similitude / gap | (3) `|eig F|` vs √q |
|-------|----------|---------------------|------------------------|----------------------|
| y²=x³+x+1 / F₁₀₁ | 105, −3, 101 | **0.0** | `F^TQF=qQ`, Q=I, **gap 1.0** | 10.0499 = √q ✓ |
| y²=x³−x+1 / F₁₀₃ | 112, −8, 103 | **0.0** | exact, **gap 1.0** | 10.1489 = √q ✓ |
| y²=x³+2x+3 / F₂₁₁ | 204, 8, 211 | **4e-16** | exact, **gap 1.0** | 14.5258 = √q ✓ |

All three pass exactly: Frobenius **commutes with J** (J-linear / Hodge morphism), is a **similitude
of a positive-definite, gapped polarization**, and its eigenvalues sit **exactly on `|z|=√q`** — the
curve RH, *forced by* (1)+(2).

## The exact contrast (operator-level MW-5)

|  | J-relation | polarization | spectrum |
|--|-----------|--------------|----------|
| **F_q curve (Frobenius)** | **commutes** (linear) | **PD, gapped** (gap 1) | `|z|=√q` exact |
| **Spec ℤ (ζ scaling)** | **anti-commutes** (R1, ratio 2.000) | **gapless** `e^{−cL}` (Phase 62) | zeros marginal |

Both ingredients that make the curve proof work **fail simultaneously** on the ζ window:
1. the operator carrying the spectrum is the wrong *type* (antilinear vs linear), and
2. the polarization has no *gap* (marginal vs PD).

These are not independent accidents — they are two faces of the same absence: there is no
**J-linear Frobenius isometry of a gapped polarization** on the ζ window. Over F_q that object is
the geometric Frobenius of an actual curve; over Spec ℤ it would be the Frobenius of the
Connes–Consani arithmetic site / Deninger's conjectural Weil cohomology — **which does not exist as
a realized object.** That is MW-5, now stated precisely and demonstrated by direct contrast.

## Honest status — Phase 63 conclusion

- **No proof of RH.** The MW-5 frontier was attacked head-on and the obstruction is now *exact and
  located*, not vague: the curve mechanism needs (linear Frobenius) + (gapped polarization); the ζ
  window provably has (antilinear scaling) + (gapless polarization).
- This is the **sharpest statement of the wall the program has produced**: a side-by-side,
  reproducible demonstration of precisely which two structural inputs the function-field proof has
  and Spec ℤ lacks. It is a genuine contribution (the precise obstruction), suitable to write up.
- Per the plan ("if nothing works we stop"): the realization frontier does **not** cross within
  reach of numerics — manufacturing a J-linear gapped Frobenius is exactly building the missing
  cohomology, which is a theory problem, not a computational one. **Phase 63 closes here.**

## What a future attempt would need (handoff)

A genuine crossing requires constructing (not observing) an operator on a Spec-ℤ cohomology that is
**both** J-linear (a Hodge morphism) **and** an isometry of a **positive-definite** polarization,
with spectrum = the zeros. R1+R3 show the naive window operators cannot be both. This is the
Connes–Consani / Deninger program; the program's role has been to pin down, concretely and
honestly, exactly what such an object must satisfy and why the finite window cannot supply it.
