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
