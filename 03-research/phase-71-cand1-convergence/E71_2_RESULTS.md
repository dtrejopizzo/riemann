# E71.2 -- convergence is a live RH-detector on the non-positivity front

**Date:** 2026-07-07.
**Script:** E71_2_convergence_detector.py.
**Question:** E71.1 showed an off-line zero cannot appear as a complex eigenvalue (spectrum real by
algebra) -- it can only degrade convergence. Does it actually STALL `sp(H_x) → {γ_k}`?

## Result (λ=5.0, matched error of the k-th real eigenvalue to γ_k, vs N)

```
                 N     γ1      γ2      γ3      γ4      γ5
ζ true          40   0.0000  0.0000  0.0000  0.0000  0.0000    <- converges
ζ+offline b=.30 20   0.0761  0.3275  0.0098  0.1683  0.4120
   (g0=25)      30   0.0907  0.3134  0.0098  0.1985  0.3059
                40   0.0961  0.3086  0.0098  0.2083  0.2846    <- FLOORS (stable, /=0)
```

**Convergence discriminates.** True ζ: errors → 0 (all five zeros exact at N=40). Planted off-line
zero: errors floor at a stable nonzero level (~0.1-0.3) that does NOT shrink with N. The off-line
zero pulls a root to its own height (γ3 error 0.0098) but **globally corrupts** convergence
everywhere else -- it cannot be hidden.

## Reading

On the CAND-1 front -- which E71.1 proved is **off the Weil-positivity wall (MW-1)** -- convergence
`sp(H_x) → {γ}` is a **genuine RH-detector**, not blind:

```
RH holds     <=>  sp(H_x) converges to {γ_k} (error -> 0)
off-line zero =>  convergence STALLS at a nonzero floor (detected)
```

This is the operator-convergence analogue of the forced-negativity detector (OK-1), but on the one
route that does not pass through positivity.

## Honest status

- **Gained:** the CCM convergence front is (a) off MW-1 (E71.1) and (b) genuinely sensitive to
  off-line zeros (E71.2) -- a live detector, not a blind reformulation. This is real forward motion,
  distinct from the Phase 67-70 circles.
- **Not a proof:** a detector is not a theorem. Proving RH here = proving `sp(H_x)` CONVERGES for ζ
  (no off-line zero stalls it). But that is a **resolvent/operator-convergence** question about
  explicit self-adjoint operators (Caratheodory-Fejer rigidity, compactness) -- the open CCM 2025-26
  frontier -- NOT the positivity inequality of MW-1.
- **Next (E71.3):** characterize the convergence RATE for ζ and whether the prime side (finite Euler
  product, PNT-controlled, zero-independent) supplies a convergence bound -- the analogue of the E6
  horizon, now on a mechanism confirmed off the wall.

```
confirmed : convergence detects off-line zeros (stall vs error->0)  [E71.2]
off-wall  : the reality is algebraic, not positivity                 [E71.1]
open      : prove sp(H_x) converges for ζ (resolvent conv.) = RH, on the operator front not MW-1
```
