# Phase 99 - Adjugate boundary sandwich

## 1. Objective

Write the internal sensitivity commutator as an explicit cofactor sandwich
against the bordered Gamma--Euler boundary sources.

## 2. Main identity

For the bordered matrix `B_z` and the augmented Euler unit `widehat Z`,

```text
det(B_z)[widehat Z,adj(B_z)]
 =-adj(B_z)[widehat Z,B_z]adj(B_z).                   (2.1)
```

The commutator `[widehat Z,B_z]` has three explicit nonzero blocks: the inner
operator commutator, the boundary-column defect and the Cauchy-row defect.

## 3. Work order

```text
E99.001  constrained determinant sensitivity;
E99.002  exact augmented bordered commutator;
E99.003  adjugate sandwich identity;
E99.004  Gamma--Euler boundary source expansion;
E99.005  final sandwich target.
E99.006  certification on a singular simple characteristic curve.
```

## Outcome

Closed; see [`PHASE_99_CLOSURE.md`](PHASE_99_CLOSURE.md) (“Explicit boundary source sandwich”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: `ADJUGATE-BOUNDARY-SANDWICH`; DIRECT-BORDERED-ANCHOR and Omega7.

## Contents

- `E99_001_CONSTRAINED_DETERMINANT_SENSITIVITY.md` — E99.001 - Constrained determinant sensitivity
- `E99_002_AUGMENTED_BORDERED_COMMUTATOR.md` — E99.002 - Exact augmented bordered commutator
- `E99_003_ADJUGATE_SANDWICH_IDENTITY.md` — E99.003 - Adjugate sandwich identity
- `E99_004_GAMMA_EULER_SOURCE_EXPANSION.md` — E99.004 - Gamma--Euler source expansion
- `E99_005_FINAL_SANDWICH_TARGET.md` — E99.005 - Final adjugate boundary target
- `E99_006_SINGULAR_CURVE_CERTIFICATION.md` — E99.006 - Singular characteristic-curve certification
- `PHASE_99_CLOSURE.md` — Phase 99 closure - Explicit boundary source sandwich

## Relation to other phases

Continues [`phase-98-sensitivity-shell-split`](../phase-98-sensitivity-shell-split/); its open target passes to [`phase-100-characteristic-cofactor-factorization`](../phase-100-characteristic-cofactor-factorization/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
