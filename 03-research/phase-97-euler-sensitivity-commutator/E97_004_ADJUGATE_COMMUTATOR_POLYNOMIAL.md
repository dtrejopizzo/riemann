# E97.004 - Adjugate commutator polynomial

## 1. Identity

Let `B` and `W` be square matrices of the same size.  Then

```text
B[W,adj(B)]B=-det(B)[W,B].                            (1.1)
```

### Proof

For invertible `B`,

```text
adj(B)=det(B)B^(-1),                                 (1.2)

[W,B^(-1)]=-B^(-1)[W,B]B^(-1).                      (1.3)
```

Multiplying (1.3) by `det(B)` and by `B` on both sides proves (1.1).
Both sides of (1.1) are polynomial in the entries of `B` and `W`; since
invertible matrices are dense, the identity holds for every `B`. `QED`

## 2. Consequence for bordered sensitivities

For a nonzero bordered determinant, equation (1.1) converts its normalized
adjugate commutator into a sandwich against the commutator of the augmented
Euler unit with the bordered matrix.

The scalar shift `-mu I` commutes with the Euler unit.  What remains in the
matrix commutator is

```text
the archimedean shift commutator;
the adjoint Euler boundary commutator;
the bordered Cauchy row and boundary column;
the finite Fourier compression defect.               (2.1)
```

## 3. Characteristic-curve correction

On the physical curve,

```text
K=H_t-mu_t I,
det K=0.                                              (3.1)
```

At a simple level, the correct characteristic sensitivity is

```text
G_t=adj(K)/partial_mu chi(t,mu_t).                    (3.2)
```

It is finite, but (1.1) degenerates to

```text
adj(K)[W,K]adj(K)=0.                                  (3.3)
```

and does not determine `[W,G_t]`.  The normalized characteristic-adjugate
commutator must therefore remain a separate exact term.  Introducing
`K^(-1)` on the characteristic curve is invalid.

## 4. Status

```text
proved:
  singular-safe adjugate commutator identity;

corrected:
  the bordered adjugate commutator reduces to a source sandwich;
  the characteristic normalized-adjugate commutator remains explicit.
```
