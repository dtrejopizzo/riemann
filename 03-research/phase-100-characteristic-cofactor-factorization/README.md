# Phase 100 - Characteristic cofactor factorization

## 1. Objective

Identify the normalized characteristic-adjugate commutator left open by
Phase 99 and determine whether it is a new boundary source.

## 2. Result

At a simple characteristic level, the normalized adjugate is the negative
orthogonal spectral projection.  Its Euler trace current is exactly the
velocity of the selected level.  It is therefore the determinant form of the
moving-level chain rule, not an additional arithmetic source.

## 3. Work order

```text
E100.001  normalized adjugate equals signed projection;
E100.002  off-diagonal commutator factorization;
E100.003  Euler trace equals level velocity;
E100.004  bilateral scalar factorization;
E100.005  recombination decision.
```

## Outcome

Closed; see [`PHASE_100_CLOSURE.md`](PHASE_100_CLOSURE.md) (“Characteristic term identified exactly”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: recombined adjugate boundary current; DIRECT-BORDERED-ANCHOR and Omega7.

## Contents

- `E100_001_SIGNED_PROJECTION.md` — E100.001 - Normalized characteristic adjugate
- `E100_002_OFF_DIAGONAL_COMMUTATOR.md` — E100.002 - Off-diagonal projection commutator
- `E100_003_LEVEL_VELOCITY_TRACE.md` — E100.003 - Euler trace and level velocity
- `E100_004_BILATERAL_CHAIN_FACTOR.md` — E100.004 - Bilateral moving-level factor
- `E100_005_RECOMBINATION_DECISION.md` — E100.005 - Recombination decision
- `PHASE_100_CLOSURE.md` — Phase 100 closure - Characteristic term identified exactly

## Relation to other phases

Continues [`phase-99-adjugate-boundary-sandwich`](../phase-99-adjugate-boundary-sandwich/); its open target passes to [`phase-101-covariant-bordered-current`](../phase-101-covariant-bordered-current/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
