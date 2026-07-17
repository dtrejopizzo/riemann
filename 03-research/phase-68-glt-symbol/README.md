# Phase 68 -- the GLT/pseudodifferential symbol of Omega_7

**Opened:** 2026-07-06. Successor to Phase 67.
**Target:** close (or precisely fail) the forcer, in the rigorous framework Phase 67 arrived at.

## Where Phase 67 left us

The terminal defect `A_N - P_lambda` is a **Generalized Locally Toeplitz (GLT) / pseudodifferential**
sequence with a rigorous 2-variable symbol `kappa(x, theta)`, `x in [0,1]` (position), `theta in
[-pi,pi]` (frequency). By GLT distribution theory (Serra-Capizzano, Garoni; Widom):

```
ind_-(A_N - P_lambda) / N  ->  (1/2pi) measure{ (x,theta) : kappa(x,theta) < 0 },
Omega_7  <=>  kappa(x,theta) >= 0 everywhere  <=>  RH.
```

The 1-D band-averaged symbol `sigma(theta) = int kappa(x,theta) dx` is the faithful leading-order
detector distilled to `02-foundations/engine/symbol_positivity_detector.py`.

## The single task

Prove `kappa(x,theta) >= 0` **by structure** -- from the Gamma_q archimedean carrier and the Euler/von
Mangoldt data -- without computing the zeros, without `-zeta'/zeta` as a partition function, without
fitting. This is the forcer. It is expected to be Weil-positivity-hard (the phase-cancellation wall,
MW-1/MW-2), but now lives in GLT/Widom symbol calculus, which has real tools.

## Status update (E68.1-E68.2)

The object is **not a clean GLT sequence**: the position-resolved symbol fails the GLT distribution law
(`measure{kappa<0} ~ 0.4` for zeta while `ind_- = 0`), so rigorous GLT eigenvalue-counting is not
available. What survives is a faithful **symbol-depth detector**: `min kappa -> 0` for zeta (marginal
touch), `-> -infinity` for off-line. So the corrected target is symbol-DEPTH nonnegativity
(`min kappa >= 0`), pursued analytically, not via GLT measure rigor.

## Plan

1. **Identify `kappa(x,theta)` explicitly.** Extract the GLT symbol of `A_N` and of `P_lambda`
   separately (position-resolved band values -> a smooth 2-D symbol). Verify GLT distribution against
   the exact eigenvalues (not just the 1-D average).
2. **Analytic form of `kappa`.** Relate `kappa_A` to the Gamma_q/polygamma archimedean data and
   `kappa_P` to the Euler symbol; identify `kappa = kappa_A - kappa_P` with an explicit special-function
   expression (the position variable x is expected to track the gauge/height flow).
3. **Nonnegativity attack.** Two honest sub-targets:
   - (a) show `kappa >= 0` reduces to a 1-parameter family of pointwise inequalities that Widom /
     Borodin-Okounkov / a positivity certificate can address;
   - (b) locate exactly where `kappa` would go negative for an off-line zero, and prove that the Euler
     structure forbids it -- or find the precise obstruction (new characterization of the wall).
4. **Falsifier throughout.** Davenport-Heilbronn and planted off-line zeros must make `kappa` go
   negative; any mechanism that also certifies them is wrong.

## Honesty contract (carried from Phase 67)

No fabricated closure. Every lemma passes a numerical gate before being written. The detector is not a
proof. If the forcer lands on the Weil wall again, characterize the wall precisely in GLT language --
that is itself a result.
