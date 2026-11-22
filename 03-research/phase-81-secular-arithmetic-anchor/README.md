# Phase 81 - Secular arithmetic anchor

## 1. Objective

Prove or further reduce `RDI-ANCHOR` without assuming zero locations,
positivity, or a finite-`L` equality that the inherited chain does not require.

The entry point is the exact bordered determinant representation

```text
F_{L,N}(z)
 = det([zI-D_{L,N}, x_{L,N}; q_{L,N}^T,c_{L,N}])
   /det(zI-D_{L,N}).                                   (1.1)
```

When `c_{L,N}!=0` this is also a rank-one perturbation determinant, but the
proof-facing formula never divides by `c_{L,N}`.

All scalar normalizations disappear after safe normalization.

## 2. Work order

```text
E81.001  phase contract and admissibility rules.
E81.002  exact bordered secular reduction of the bilateral core determinant.
E81.003  Stieltjes-transform uniqueness and the arithmetic target measure.
E81.004  cell equation for the secular residues.
E81.005  outer arithmetic anchor or theorem-grade obstruction.
```

Later steps are admitted only when they imply the preceding target exactly.

## 3. Exit condition

```text
prove RDI-ANCHOR;
or reduce it to one explicit residue or measure identity whose failure can be
checked without zero-location input;
or refute the secular route with the exact false implication.
```

## Outcome

Closed at obstruction and exact-reduction grade; see [`PHASE_81_CLOSURE.md`](PHASE_81_CLOSURE.md) (“Secular loop theorem”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: the coupled generator outer identity (3.1).

## Contents

- `E81_001_PHASE_CONTRACT.md` — E81.001 - Secular-anchor contract
- `E81_002_RANK_ONE_SECULAR_REDUCTION.md` — E81.002 - Exact bordered secular reduction
- `E81_003_STIELTJES_UNIQUENESS.md` — E81.003 - Bilateral Stieltjes uniqueness
- `E81_004_TWO_GENERATOR_RESIDUES.md` — E81.004 - Exact two-generator formula for the secular residues
- `PHASE_81_CLOSURE.md` — Phase 81 closure - Secular loop theorem

## Relation to other phases

Continues [`phase-80-relative-determinant-identification`](../phase-80-relative-determinant-identification/); its open target passes to [`phase-82-coupled-generator-continuum`](../phase-82-coupled-generator-continuum/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
