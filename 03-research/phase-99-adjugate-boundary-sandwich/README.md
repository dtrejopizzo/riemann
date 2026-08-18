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
