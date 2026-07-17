# E73.104 results - FAR-SLOPE verifier

## 1. Purpose

E73.103 proposed:

```text
T_k=FAR_k Q_k.
```

It also listed the simple sufficient split:

```text
sum FAR_k <= L^6,
max Q_k <= L^-11.
```

E73.104 tests that split.

## 2. Output

```text
E73.104 FAR-SLOPE verifier
Checks sufficient split: sum FAR<=L^6 and max Q<=L^-11.
 lam     L tau    farSumB  maxQB  productB  directB status
  16   5.545   14.13     6.143 -11.747    -5.605   -6.111   FAIL
  18   5.781   14.13     6.349 -10.363    -4.014   -6.621   FAIL
  20   5.991   14.13     5.878 -10.357    -4.479   -6.282   FAIL
  24   6.356   21.02     5.463 -10.271    -4.809   -5.930   FAIL
  28   6.664   14.13     5.362 -11.155    -5.793   -6.070   PASS
```

`directB` is the true weighted sum:

```text
log_L(sum FAR_k Q_k).
```

## 3. Diagnosis

The direct weighted FAR-SLOPE sum passes the `L^-5` target in every tested case.  The crude split:

```text
sum FAR_k * max Q_k
```

fails in most cases.

Therefore the key structure is the anticorrelation:

```text
large FAR_k rows have smaller Q_k,
larger Q_k rows have smaller FAR_k.
```

This is exactly the kind of cancellation lost by replacing the weighted sum with a max bound.

## 4. Corrected target

The correct theorem is not:

```text
FAR-CEIL + max SLOPE.
```

It is the weighted inequality itself:

```text
WEIGHTED-FAR-SLOPE:
sum_{gamma_k in D_3(A,L)} FAR_k Q_k <= C_main L^-5.
```

Since `D_3` has only three rows, an interval proof can still be nodewise, but the budgets must be
assigned per node:

```text
FAR_k Q_k <= b_k(A,L)L^-5,
sum b_k(A,L) <= C_main.
```

## 5. Status

```text
confirmed: direct weighted FAR-SLOPE is the right main theorem;
refuted as proof route: max-Q split in low L windows;
next: formulate per-node weighted interval certificate for FAR-SLOPE.
```
