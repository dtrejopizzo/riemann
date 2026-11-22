# Phase 96 - Determinantal prime response

## 1. Objective

Expand the characteristic Jacobian of Phase 95 as an exact finite von
Mangoldt sum while retaining the complete determinant response.

## 2. Main result

The deformation derivative is linear in the prime direction even though the
bordered quotient is nonlinear.  This produces a global response kernel for
each shift length `y`, with no eigenvector or inner inverse.

## 3. Work order

```text
E96.001  polarized determinant derivatives;
E96.002  cellwise Jacobian expansion;
E96.003  bilateral response kernel;
E96.004  exact Euler-kernel defect;
E96.005  coupled-sum decision.
```

## Outcome

Closed; see [`PHASE_96_CLOSURE.md`](PHASE_96_CLOSURE.md) (“Global von Mangoldt response”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: `DETERMINANTAL-PRIME-RESPONSE`; DIRECT-BORDERED-ANCHOR and Omega7.

## Contents

- `E96_001_POLARIZED_DETERMINANT.md` — E96.001 - Polarized determinant derivative
- `E96_002_CELLWISE_JACOBIAN_EXPANSION.md` — E96.002 - Cellwise Jacobian expansion
- `E96_003_BILATERAL_RESPONSE_KERNEL.md` — E96.003 - Bilateral determinant response kernel
- `E96_004_EXACT_EULER_KERNEL_DEFECT.md` — E96.004 - Exact Euler-kernel defect
- `E96_005_COUPLED_SUM_DECISION.md` — E96.005 - Coupled-sum decision
- `PHASE_96_CLOSURE.md` — Phase 96 closure - Global von Mangoldt response

## Relation to other phases

Continues [`phase-95-characteristic-jacobian-current`](../phase-95-characteristic-jacobian-current/); its open target passes to [`phase-97-euler-sensitivity-commutator`](../phase-97-euler-sensitivity-commutator/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
