# E90 — Cesàro Closure Gate for 2.3.F (Phase 62, step C0)

**Date:** 2026-06-26 · dps=40 · λ ∈ {7,9,11,13,15,17,19,21}, both parities · falsador DH mandatory.

## Question

Does the Cesàro-in-λ average of the intrinsic Jacobi of G_λ (a) converge for ζ, and
(b) reproduce the band-edge ladder k(k+2) — while the Davenport–Heilbronn (DH) falsador does not?

## Result — the discriminator is BOUNDEDNESS, not the ladder (honest refinement)

**1. The k(k+2) ladder is NON-discriminating.** Building the period-2 limit ladder from the
Cesàro-averaged bulk symbol (a_even, a_odd, b) gives:

| kind | shifted ladder | max err vs [0,1,2.667,5,8,11.667] |
|------|----------------|-----------------------------------|
| ζ    | [0, 1, 2.626, 4.818, 7.486, 10.513] | 1.15 |
| DH   | [0, 1, 2.649, 4.921, 7.781, 11.182] | **0.49** |

DH reproduces k(k+2) *better* than ζ. The shifted band-edge ladder is a **generic** property
of any near-uniform period-2 Jacobi chain with Dirichlet ends — it is geometry, not arithmetic.
**"Averaged Jacobi → k(k+2)" cannot by itself be the content of 2.3.F.** (Refutes the GATE-2
hypothesis as originally stated; corrects the optimistic reading of E85-T3.)

**2. The real discriminator is L1 boundedness / Cesàro convergence of the coefficients.**

Bulk band-width b_bulk(λ):

| λ | 7 | 9 | 11 | 13 | 15 | 17 | 19 | 21 | trend |
|---|---|---|----|----|----|----|----|----|-------|
| **ζ**  | 0.140 | 0.142 | 0.147 | 0.123 | 0.080 | 0.097 | 0.116 | 0.139 | **bounded, oscillates ~0.12, no growth** |
| **DH** | 1.384 | 1.545 | 1.708 | 1.851 | 1.949 | 2.039 | 2.096 | 2.176 | **monotone growth** |

`max b` over the chain: ζ stays 1.1–2.2 (flat); DH grows **linearly** 3.5 → 10.0 with λ.
Cesàro tail-variance of the leading coefficient: ζ 1.8e-3 vs DH 2.0e-2 (~10×);
var(b_bulk): ζ 5.0e-4 vs DH 6.8e-2 (~130×).

## Verdict — C0 PASSES for ζ, falsador works, but the target is relocated

- **ζ:** intrinsic Jacobi coefficients are **bounded** and **Cesàro-converge** (b_bulk ≈ 0.12,
  no λ-growth). This is exactly the L1 boundedness `sup_λ max|A_ij| < ∞` (R10's open link),
  now seen to hold *in the Cesàro/average sense* numerically.
- **DH (falsador):** coefficients are **unbounded** (b grows with λ) → L1 fails. Correctly rejected.
- **The ladder is a red herring.** It follows for free from period-2 Dirichlet geometry and
  carries no arithmetic; DH satisfies it too.

**Consequence for the plan (C1):** the analytic target is NOT "averaged ladder = k(k+2)".
It is: **prove the ζ intrinsic Jacobi band-width b_bulk(λ) is bounded (Cesàro) in λ** — i.e.
the boundedness L1, which is where DH demonstrably fails. The band-edge ladder is then a
geometric consequence requiring no further arithmetic. This is the honest content of 2.3.F-Loc.

**Honesty note:** no proof reached. C0 is a numerical gate; it tells us the Cesàro route is
*alive but its load-bearing claim moved* from the ladder to coefficient-boundedness. A false
victory (claiming "Jacobi → k(k+2) proves 2.3.F") would be worse than failure — and DH explicitly
refutes that claim here.

## Reproduce

```
venv/bin/python E90_cesaro_jacobi.py "[(7.0,14),(9.0,16),(11.0,18),(13.0,18),(15.0,20),(17.0,20),(19.0,22),(21.0,22)]"
```
(Builds cached in `.cache_23F/` at dps=50; DH builds generated this run.)
