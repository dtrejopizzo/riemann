# E71.1 -- CAND-1 reality mechanism: self-adjointness is algebraic, not positivity

**Date:** 2026-07-07.
**Script:** E71_1_reality_mechanism.py.
**Question:** is the CCM "self-adjoint by construction" genuinely off the Weil-positivity wall
(MW-1), or is it positivity in disguise?

## The fork tested

Eigenvalues of `H` = real roots of `f(s) = Σ_k ξ_k/(s - d_k)`, `d_k = 2πk/L` real.
- (A) reality from `ξ` sign-definite -> off the wall;
- (B) reality requires `ξ` sign-definite and an off-line zero breaks it -> MW-1 disguise.

## Result

```
ζ (true):            ξ = 19 pos / 22 neg  -> NOT sign-definite;  complex roots of f: 0
ζ + off-line b=0.25: ξ = 16 pos / 25 neg  -> NOT sign-definite;  complex roots of f: 0
ζ + off-line b=0.40: ξ = 19 pos / 22 neg  -> NOT sign-definite;  complex roots of f: 0
```

**Both fork options were wrong.** The correct mechanism is the CCM finite self-adjoint construction
itself. In the rational model, the eigenvalues are roots of a real rational function with real poles,
but generic residues would not be enough to force all roots real. The tested CCM ground vectors have
mixed signs and still give an all-real spectrum. Thus the all-real spectrum is not coming from
sign-definite Weil positivity; it is coming from the self-adjoint finite operator structure.

## Consequence (two honest faces)

1. **CAND-1 is genuinely off MW-1.** Reality of `sp(H)` is not a Weil-positivity condition; it is
   automatic from the real-rational/interlacing structure. There is no positivity inequality to prove
   for reality. This is NOT the wall.

2. **The exact price:** because reality is automatic, the construction is STRUCTURALLY BLIND to an
   off-line zero *as a complex eigenvalue*. Planting an off-line zero produces NO complex root -- it
   only displaces the real roots. All RH content therefore lives in **convergence**:
   `sp(H_x) → {zeros of ζ}`. An off-line zero manifests as a CONVERGENCE FAILURE (real eigenvalues
   that fail to track the true zero), never as a complex eigenvalue.

## Status

```
confirmed : self-adjointness "by construction" is real and algebraic (not positivity) -> off MW-1
localized : 100% of the RH content is in operator convergence sp(H_x) -> {zeros}, per CAND-1 / NO-GO-LIST
open      : is convergence a genuine RH-DETECTOR? (off-line zero => convergence degrades?) -> E71.2
```

Matches the NO-GO-LIST CAND-1 entry exactly ("the obstacle is operator convergence, not
positivity"), verified from inside with numerics rather than taken on faith. Not on the failure list.
