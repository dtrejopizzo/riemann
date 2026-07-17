# E99 — squaring lever: NO-GO, and the deepest statement of the wall (gaplessness = infinitude of zeros)

**Date:** 2026-06-27 · Phase 63, R6 · ζ vs DH · engine A/J/parity-sector framework (mpmath build, float64 eig).

## The idea (a genuine new lever)

R1's obstruction was that the scaling operator `D` (spectrum carries the zeros) is **antilinear**
(`DJ=−JD`), the wrong type for Frobenius. But `D` anti-commuting with `J` ⟹ `D²` **commutes** with
`J` — `D²` is J-**linear**, spectrum `γ²`, and `RH ⟺ γ²≥0 ⟺ D²⪰0`. Squaring moves the zeros from
the antilinear sector into the J-linear sector. **Hope:** maybe the gapless `e^{−cL}` cascade of the
polarization (Phase 62) lives only in the antilinear/odd directions, and the J-linear/even sector —
where `D²` and any Frobenius live — is **gapped**.

## Result — the J-linear sector is equally gapless

Decomposing the polarization `A` by parity (even = J-linear/cos sector, odd = antilinear/sin sector):

| | ζ even (J-linear) | ζ odd (antilinear) | DH even | DH odd |
|--|---|---|---|---|
| signature | PSD (8,0) | PSD (7,0) | **indef** (7,12) | **indef** (6,12) |
| relgap (min⁺/max) | **~1e-12** | ~5e-11 | 7e-2 | 0.16 |

- **ζ is PSD in BOTH sectors but GAPLESS in both** (relgap at the float64 floor ~1e-12). The cascade
  is **not** confined to the antilinear sector. Squaring lands `D²` in a J-linear sector that is just
  as gapless. **No crossing.**
- DH is indefinite in both sectors (the detector still works: ζ PSD, DH not).

## Why — the wall is the infinitude of the zeros (deepest statement)

The gap is `e^{−cL}=λ^{−2c}` and closes as `λ→∞` (the window resolves ever more zeros). The reason is
structural, and the F_q contrast (R3) makes it sharp:

> **A spectral gap requires finitely many eigenvalues.** A curve over F_q has genus `g` — `H¹` is
> `2g`-dimensional, Frobenius is a finite matrix with `2g` eigenvalues, and the polarization is
> positive-definite **with a gap** because the spectrum is *finite and discrete*. ζ has **infinitely
> many zeros**; the polarization on the window is positive but its margin → 0 as more zeros enter,
> because the zeros become dense (`N(T)~(T/2π)log T`). **The gaplessness is the analytic shadow of
> Spec ℤ having "infinite genus".**

This is why no finite-window / F_q-style argument can cross: the one ingredient the curve proof
relies on — a *gapped* positive polarization — is unavailable not by accident but because ζ's zeros
are infinite and accumulate. The gap we keep failing to find **does not exist at finite λ and
closes in the limit**, in every sector, after squaring, under every reformulation tried (Cesàro,
Hodge–Riemann, Euler/μ, antilinearity, squaring).

## Verdict

Squaring is a NO-GO. More importantly, E99 + R3 together give the program's sharpest, most
structural statement of the master wall:

> **The function-field proof needs a gapped positive polarization; ζ cannot have one on any finite
> window because it has infinitely many, accumulating zeros (infinite genus). The crossing requires
> an honestly infinite-dimensional realization with a *regularized* positivity (Deninger's
> regularized determinants / the arithmetic site), not a finite gap — which is a theory problem
> beyond what numerics can validate.**

No proof of RH; no false victory. This is, in the program's judgment, the natural floor of the
numerical/finite-window approach to the realization frontier.

## Reproduce
```
venv/bin/python E99_squaring_sectors.py "[(11.0,18),(15.0,20),(21.0,22)]"
```
