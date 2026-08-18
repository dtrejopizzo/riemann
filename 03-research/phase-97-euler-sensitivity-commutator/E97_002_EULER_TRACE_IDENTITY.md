# E97.002 - Euler trace-commutator identity

## 1. One-sided connection

Let `Z` be an invertible finite Euler unit and let `X` be the position
derivation.  Define

```text
A=Z^(-1)[X,Z].                                       (1.1)
```

### Theorem 1.1

For every compatible matrix `K`,

```text
Tr(KA)=Tr([Z,K]Z^(-1)X).                             (1.2)
```

### Proof

Expand the connection:

```text
Tr(KA)
 =Tr(KZ^(-1)XZ)-Tr(KX).                              (1.3)
```

Cyclicity of the trace gives

```text
Tr(KZ^(-1)XZ)=Tr(ZKZ^(-1)X).                         (1.4)
```

Since

```text
ZKZ^(-1)-K=[Z,K]Z^(-1),                              (1.5)
```

subtraction proves (1.2). `QED`

## 2. Adjoint connection

Taking adjoints in (1.1) gives

```text
A^*=[Z^*,X](Z^*)^(-1).                               (2.1)
```

The same cyclic calculation yields

```text
Tr(KA^*)
 =Tr((Z^*)^(-1)[K,Z^*]X).                            (2.2)
```

Consequently,

```text
Tr[K(A+A^*)]
 =Tr([Z,K]Z^(-1)X)
  +Tr((Z^*)^(-1)[K,Z^*]X).                           (2.3)
```

## 3. Interpretation

The prime connection pairs only with the failure of `K` to commute with the
Euler shift.  Any scalar or shift-commuting part of `K` disappears exactly.

## 4. Status

```text
proved:
  exact one-sided and Hermitian Euler trace identities.
```

