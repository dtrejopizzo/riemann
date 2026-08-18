# E98.002 - Exact Euler commutator shell split

## 1. One-sided identity

Let

```text
Z_N=P_NZP_N,
K_N=P_NK_NP_N.                                       (1.1)
```

### Theorem 1.1

On the physical module,

```text
[Z,K_N]
 =[Z_N,K_N]
  +Q_NZP_NK_N-K_NP_NZQ_N.                            (1.2)
```

### Proof

Insert `I=P_N+Q_N` on the outside of the two products:

```text
ZK_N
 =P_NZP_NK_N+Q_NZP_NK_N,                             (1.3)

K_NZ
 =K_NP_NZP_N+K_NP_NZQ_N.                             (1.4)
```

Subtract (1.4) from (1.3). `QED`

## 2. Adjoint identity

Likewise,

```text
[K_N,Z^*]
 =[K_N,Z_N^*]
  +K_NP_NZ^*Q_N-Q_NZ^*P_NK_N.                        (2.1)
```

## 3. Interpretation

The terms

```text
Q_NZP_NK_N,
K_NP_NZQ_N                                           (3.1)
```

are the exact shell crossings.  They must remain paired with `Z^{-1}X` in
the trace identity; their operator norms are not the target.

## 4. Status

```text
proved:
  exact internal/shell decomposition for both Euler directions.
```

