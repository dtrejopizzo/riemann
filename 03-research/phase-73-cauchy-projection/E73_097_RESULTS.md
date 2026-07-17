# E73.097 results - FAR3 main budget

## 1. Purpose

After E73.091, E73.094, and E73.096, the remaining piece of `GATE-73` is the three main FAR3
nodewise rational terms:

```text
T_k(A,L)=W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

E73.097 reports these three terms separately.

## 2. Output

```text
E73.097 FAR3 main budget probe
Reports the three main rational WCS terms selected by FAR score.
 lam     L tau    mainB   maxB   gapToL5  gamma:termB list
  16   5.545   14.13   -6.111  -6.378   -1.111 30.4:-9.631,32.9:-6.699,37.6:-6.378
  16   5.545   21.02   -6.108  -6.328   -1.108 30.4:-9.835,32.9:-6.788,37.6:-6.328
  18   5.781   14.13   -6.621  -6.805   -1.621 30.4:-6.805,32.9:-8.101,37.6:-7.535
  18   5.781   21.02   -6.752  -7.003   -1.752 30.4:-7.003,32.9:-8.188,37.6:-7.486
  20   5.991   14.13   -6.282  -6.572   -1.282 30.4:-6.921,32.9:-7.650,37.6:-6.572
  20   5.991   21.02   -6.312  -6.524   -1.312 30.4:-7.116,32.9:-7.736,37.6:-6.524
  24   6.356   14.13   -5.974  -5.983   -0.974 30.4:-9.636,32.9:-8.258,37.6:-5.983
  24   6.356   21.02   -5.930  -5.937   -0.930 30.4:-9.824,32.9:-8.341,37.6:-5.937
  28   6.664   14.13   -6.070  -6.087   -1.070 30.4:-11.771,32.9:-7.888,37.6:-6.087
  28   6.664   21.02   -6.029  -6.042   -1.029 30.4:-11.955,32.9:-7.969,37.6:-6.042
```

`gapToL5 = mainB+5`.  Negative values mean the main sum is below `L^-5`.

## 3. Diagnosis

The three-node main sum is consistently below the target:

```text
worst tested mainB = -5.930.
```

The dominant node is usually:

```text
gamma ~= 37.6.
```

The margin relative to `L^-5` is roughly one power of `L` in the tested range.

## 4. Consequence

The final main certificate should be nodewise:

```text
FAR3-MAIN-RAT(A,L):
for gamma_k in D_3(A,L),
T_k(A,L) <= b_k(A,L)L^-5,
sum_{gamma_k in D_3(A,L)} b_k(A,L) <= C_main.
```

The rational term is:

```text
T_k(A,L)
=
e^(alpha L)G_theta,m(a,i gamma_k)|1-e^(i gamma_k L)|
|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

This is the last finite gate in `GATE-73`.

## 5. Status

```text
verified: FAR3 main rational terms satisfy the L^-5 budget in the harness;
identified: the dominant node is explicit and stable;
open: prove FAR3-MAIN-RAT uniformly for the natural-height cluster boxes.
```
