# E73.296 - Principal compression is not a forcer

Date: 2026-07-16.

## 1. Purpose

After E73.295, the final finite identity can be read in adjugate form or as
the directional cell scalar

```text
qH_LR_wxi_L.
```

The tempting shortcut is the rank-two principal compression:

```text
A=QH_LQ^*(QQ^*)^(-1),
h=Qxi_L.
```

E73.266 already rejected the identity

```text
QH_LR_wxi_L=(mu_LI-A)h
```

as a proof route if one uses `h=Qxi_L` as small input.  E73.296 tests the only
stronger possibility left: maybe `mu_LI-A` is itself small, or nearly singular
for structural reasons.  If so, the principal compression could force the
defect without prior control of `h`.

It does not.

## 2. Test

For each window, compute:

```text
M=mu_LI-A.
```

Report:

```text
||M||,
s_min(M),
det(M),
dist(mu_L,spec(A)),
||h||,
||Mh||,
||Mh||/(||M||||h||).
```

If principal compression were a non-circular forcer, one would expect `||M||`,
`s_min(M)`, or the eigenvalue gap to be small independently of `h`.

## 3. Result

Representative output from `E73_296_principal_compression_forcer_probe.py`:

```text
 lam     L gamma opB sminB detB eigGapB hB vectB relVect center0B center1B
   8   4.159   14.13 -0.73  -2.29 -3.02    -2.29 -19.03 -21.31 1.1e-01   -21.68   -21.46
  12   4.970   21.02 -0.41  -1.22 -1.65    -1.22 -15.28 -16.49 2.8e-01   -16.61   -16.84
  16   5.545   14.13  1.19   0.98  1.98     0.98 -20.04 -19.05 7.1e-01   -19.32   -19.96
  20   5.991   21.02  1.20   1.00  2.01     1.00 -18.50 -17.50 7.0e-01   -17.68   -17.79
```

For `lambda=16,20`, the compressed defect matrix has positive power size:

```text
||mu I-A|| ~ L^1.2,
s_min(mu I-A) ~ L^1.
```

So the matrix is not small and not structurally singular.  The small scalar
center comes only after applying it to the specific vector `h=Qxi_L`.

## 4. Consequence

The rank-two compression remains a detector:

```text
QH_LR_wxi_L=(mu_LI-A)Qxi_L.
```

But it cannot be a forcer.  Any proof that proceeds by bounding

```text
(mu_LI-A)Qxi_L
```

must supply independent control of `Qxi_L`, which is exactly the circular
branch rejected in E73.240 and E73.266.

The surviving endpoint is unchanged:

```text
FINAL-ETA-ADJ:
||qH_L(I-P_w)Adj_red(H_L-mu_LI)||
<= A_M L^(-M)||Adj_red(H_L-mu_LI)||,
```

or equivalently:

```text
F_L[y -> qQ_yR_wxi_L]=O_M(L^(-M)).
```

## 5. Program audit

This is not a new route; it is a refined closure of the old rank-two warning.

```text
E73.266 rejected rank-two transport through h=Qxi_L;
E73.296 rejects the stronger possibility that muI-A itself is a forcer.
```

Thus further work should stay on the signed cell/adju gate identity, not the
Cauchy principal compression.

## 6. Status

```text
tested: principal compression matrix muI-A;
rejected: matrix-level compression forcer;
kept: rank-two identity as detector only;
unchanged endpoint: FINAL-ETA-ADJ / Directional Cell Eigenline Cancellation.
```
