# Phase 95 - Characteristic Jacobian current

## 1. Objective

Eliminate the moving finite level from the bordered deformation by treating it
as an algebraic branch of the full characteristic determinant.

## 2. Main construction

Let

```text
chi(t,mu)=det(H_t-mu I)                               (2.1)
```

and let `P(t,mu,z)` be the global cofactor numerator of Phase 94 before
substitution of the selected level.  Along a simple branch
`chi(t,mu_t)=0`, the total derivative of `log P` is a determinant Jacobian
divided by `P partial_mu chi`.

## 3. Work order

```text
E95.001  two-parameter algebraic lift;
E95.002  characteristic Jacobian theorem;
E95.003  bilateral projective current;
E95.004  branch and chart audit;
E95.005  exact remaining determinant identity.
```

## Outcome

Closed; see [`PHASE_95_CLOSURE.md`](PHASE_95_CLOSURE.md) (“Moving level absorbed into two determinants”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: signed Gamma--Euler evaluation of the determinant Jacobian; DIRECT-BORDERED-ANCHOR and Omega7.

## Contents

- `E95_001_TWO_PARAMETER_LIFT.md` — E95.001 - Two-parameter algebraic lift
- `E95_002_JACOBIAN_TANGENT_THEOREM.md` — E95.002 - Characteristic Jacobian tangent theorem
- `E95_003_BILATERAL_PROJECTIVE_JACOBIAN.md` — E95.003 - Bilateral projective Jacobian
- `E95_004_BRANCH_AND_CHART_AUDIT.md` — E95.004 - Branch and chart audit
- `E95_005_DETERMINANT_IDENTITY_TARGET.md` — E95.005 - Determinant identity target
- `PHASE_95_CLOSURE.md` — Phase 95 closure - Moving level absorbed into two determinants

## Relation to other phases

Continues [`phase-94-global-cofactor-cell-current`](../phase-94-global-cofactor-cell-current/); its open target passes to [`phase-96-determinantal-prime-response`](../phase-96-determinantal-prime-response/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
