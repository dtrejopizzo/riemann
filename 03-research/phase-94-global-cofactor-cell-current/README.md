# Phase 94 - Global cofactor cell current

## 1. Objective

Compute `DIRECT-BORDERED-ANCHOR` without an inner inverse by combining the
global bordered determinant with the rank-two displacement identity of the
Gamma--prime CCM matrix.

## 2. Main result

For the raw right boundary column, the entire bordered numerator and its safe
derivative are expressed through determinants and adjugate vectors only.  The
two-generator formula survives at singular sections as a polynomial identity.

## 3. Work order

```text
E94.001  exact global cofactor current;
E94.002  inverse-free boundary displacement identity;
E94.003  polynomial two-generator numerator;
E94.004  exact bilateral Gamma--Euler defect;
E94.005  deformation cofactor identity and remaining theorem.
E94.006  multiprecision certification of the finite identities.
```

## Outcome

Closed; see [`PHASE_94_CLOSURE.md`](PHASE_94_CLOSURE.md) (“Inverse-free cofactor anchor”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: `COFACTOR-CELL-ANCHOR`; determinant-level Gamma--Euler cancellation; DIRECT-BORDERED-ANCHOR and Omega7.

## Contents

- `E94_001_GLOBAL_COFACTOR_CURRENT.md` — E94.001 - Exact global cofactor current
- `E94_002_BOUNDARY_DISPLACEMENT_POLYNOMIAL.md` — E94.002 - Inverse-free boundary displacement polynomial
- `E94_003_POLYNOMIAL_TWO_GENERATOR_NUMERATOR.md` — E94.003 - Polynomial two-generator numerator
- `E94_004_EXACT_BORDERED_EULER_DEFECT.md` — E94.004 - Exact bordered Euler defect
- `E94_005_DEFORMATION_COFACTOR_IDENTITY.md` — E94.005 - Deformation cofactor identity
- `E94_006_FINITE_IDENTITY_CERTIFICATION.md` — E94.006 - Finite identity certification
- `PHASE_94_CLOSURE.md` — Phase 94 closure - Inverse-free cofactor anchor

## Relation to other phases

Continues [`phase-93-direct-bordered-anchor`](../phase-93-direct-bordered-anchor/); its open target passes to [`phase-95-characteristic-jacobian-current`](../phase-95-characteristic-jacobian-current/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
