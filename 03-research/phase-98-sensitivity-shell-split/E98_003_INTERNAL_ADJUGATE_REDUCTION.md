# E98.003 - Internal adjugate reduction

## 1. Augmented compressed unit

Let `widehat Z_N` be the compressed Euler unit augmented by the identity on
the bordered scalar coordinate.  Let `B_z` be the bordered matrix whose
determinant is the global numerator.

The internal sensitivity contains a bordered adjugate part and the normalized
adjugate of the full characteristic matrix.  E97.004 reduces the bordered
part to the commutator

```text
[widehat Z_N,B_z].                                   (1.1)
```

The characteristic part remains

```text
[Z_N,adj(H_t-mu_tI)/partial_mu chi].                  (1.2)
```

It is finite on a simple branch.  The singular characteristic matrix may not
be inverted to rewrite (1.2).

## 2. Scalar shifts

Since

```text
[Z_N,mu I]=0,                                        (2.1)
```

the selected level disappears from the internal commutator.  It remains only
in the cofactor sensitivity multiplying that commutator.

## 3. Exact matrix sources

The bordered commutator in (1.1) contains exactly

```text
[Z_N,H_A];
[Z_N,H_P];
the boundary-column commutator;
the safe bordered-row commutator.                    (3.1)
```

Before compression, the one-sided part of `H_P` commutes with `Z`; the
noncommuting adjoint part and `[Z,H_A]` are the boundary operators calculated
in E83.005--E83.006.  Compression adds only the shell terms already separated
in E98.002.

## 4. Status

```text
localized exactly:
  bordered determinant commutator to archimedean, adjoint-boundary and
  bordered-row sources;
  characteristic constraint to a normalized-adjugate commutator;

no longer present as a source:
  the scalar moving level.
```
