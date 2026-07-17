# E72.117 -- Gram determinant form of bad-subspace orthogonality

**Date:** 2026-07-09.
**Role:** convert `BORTH` into a finite determinant identity.

## 0. Setup

Let:

```text
U_x=[u_1 ... u_d]
```

be any full-rank column matrix whose span is the bad subspace:

```text
B_{x,H,q}=span{mass direction, first q right singular directions}.
```

For a finite root `tau_j`, write:

```text
Y_j=Y_x(tau_j).
```

Define the Gram matrices:

```text
G_x:=U_x^*U_x,
g_j:=U_x^*Y_j,
n_j:=Y_j^*Y_j,
```

and the augmented Gram matrix:

```text
G_x[Y_j]
 := [ G_x   g_j ]
    [ g_j^* n_j ].
```

## 1. Determinant identity

### Lemma 72.117.1

The relative squared distance of `Y_j` from the bad subspace is:

```text
dist(Y_j,B_{x,H,q})^2/||Y_j||^2
 = det(G_x[Y_j])/(det(G_x)||Y_j||^2).                       (GDIST)
```

Consequently:

```text
||P_{B,x}Y_j||^2/||Y_j||^2
 = 1 - det(G_x[Y_j])/(det(G_x)||Y_j||^2).                   (GPROJ)
```

### Proof

The Schur complement of `G_x` in `G_x[Y_j]` is:

```text
n_j-g_j^*G_x^(-1)g_j.
```

Since:

```text
g_j^*G_x^(-1)g_j=||P_{B,x}Y_j||^2,
```

the Schur complement is `dist(Y_j,B)^2`.  Taking determinants gives `(GDIST)` and `(GPROJ)`. `QED`

## 2. Determinantal BORTH

The bad-subspace orthogonality condition:

```text
||P_{B,x}Y_j||/||Y_j|| -> 0
```

is equivalent to the finite determinant saturation:

```text
det(G_x[Y_j])/(det(G_x)||Y_j||^2) -> 1.                     (GBORTH)
```

uniformly for finite root-height windows.

Thus the current endpoint can be stated without projections:

```text
CCGD,
BNORM,
GBORTH.
```

## 3. Explicit arithmetic meaning

Every entry involving `Y_j` is an endpoint discrepancy integral:

```text
(g_j)_a=<u_a,Y_j>
 = int_0^L exp(-i tau_j r)T_{x,H,q,a}(r)dE_x^leftarrow(r),
```

and:

```text
n_j=||Y_j||^2
```

is a finite quadratic form in the same Chebyshev Fourier packet.  Therefore `(GBORTH)` is an explicit
finite determinant identity in endpoint discrepancy transforms.

No limiting zero and no hidden infinite operator occurs in `(GBORTH)`.

## 4. Diagnostic

The companion script:

```text
E72_117_bad_subspace_gram_probe.py
```

compares three equivalent computations:

```text
QR projection,
Gram inverse projection,
Gram determinant projection.
```

Representative output:

```text
E72.117 bad-subspace Gram determinant probe q=3
 lam   N roots  maxQRproj  maxGramproj  maxDetProj  minSat
   6  18     3  1.568e-01    1.568e-01   1.568e-01  0.97542
   8  24     4  1.273e-01    1.273e-01   1.273e-01  0.98379
  10  28     3  9.242e-02    9.242e-02   9.242e-02  0.99146
  12  32     4  6.286e-02    6.286e-02   6.286e-02  0.99605
  14  36     4  5.847e-02    5.847e-02   5.847e-02  0.99658
```

The three projection computations agree to displayed precision.  The determinant saturation `minSat`
increases toward `1` in the tested windows.

## 5. Status

```text
proved: BORTH is equivalent to Gram determinant saturation GBORTH;
proved: GBORTH is finite and explicitly computable from endpoint discrepancy transforms;
observed: determinant saturation improves in tested windows;
open:   prove GBORTH and BNORM uniformly, plus CCGD.
```
