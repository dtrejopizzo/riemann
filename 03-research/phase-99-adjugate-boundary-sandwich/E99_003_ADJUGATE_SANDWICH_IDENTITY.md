# E99.003 - Adjugate sandwich identity

## 1. Theorem

For square matrices `B,W` of the same size,

```text
det(B)[W,adj(B)]
 =-adj(B)[W,B]adj(B).                                (1.1)
```

### Proof

For invertible `B`, use

```text
adj(B)=det(B)B^(-1),
[W,B^(-1)]=-B^(-1)[W,B]B^(-1).                      (1.2)
```

This proves (1.1) on the dense set of invertible matrices.  Both sides are
polynomial in the entries of `B,W`, so (1.1) holds for all matrices. `QED`

## 2. Bordered application

With `B=B_z` and `W=widehat Z`, E99.002 gives

```text
det(B_z)[widehat Z,adj(B_z)]

 =-adj(B_z)
   [[ [Z,M], Zb-b],
    [h_z-h_zZ,0]]
   adj(B_z).                                         (2.1)
```

Thus every internal sensitivity commutator is a cofactor sandwich against
explicit sources.  No inverse occurs in (2.1).

## 3. Characteristic application and limit

The same identity with `B=K` gives, on the characteristic curve,

```text
adj(K)[Z,H_t]adj(K)=0.                               (3.1)
```

This is a compatibility identity, not a formula for `[Z,adj(K)]`.  The
characteristic-constraint term remains the normalized commutator

```text
[Z,adj(K)/partial_mu chi].                            (3.2)
```

It cannot be converted into a sandwich without a reduced characteristic
resolvent, which is not introduced here.

## 4. Status

```text
proved:
  singular-safe bordered sandwich identity;
  characteristic compatibility identity;

retained:
  normalized characteristic-adjugate commutator.
```
