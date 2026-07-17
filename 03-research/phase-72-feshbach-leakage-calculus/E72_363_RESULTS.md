# E72.363 results - residue eigenline probe

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_363_residue_eigenline_probe.py
```

The probe tests the eigenline form of the simple-window divisor block:

```text
P_k^perp(KWin k - tail)=0.
```

## Table

```text
lam   N roots node     ||k||      ||Kk||      ||tail||    perpNorm    relPerp   |lambda|
 6.0  10     2 root   1.503e-16  4.815e-16  1.097e-15  1.556e-15       nan        nan
 6.0  10     2 shift  1.257e+00  3.502e+00  5.526e-03  4.681e-01 1.337e-01  2.761e+00

 8.0  12     3 root   3.098e-12  1.372e-11  3.760e-15  1.850e-12 1.348e-01  4.391e+00
 8.0  12     3 shift  5.023e+00  2.313e+01  2.531e-02  4.779e+00 2.067e-01  4.504e+00

10.0  14     3 root   2.978e-12  1.342e-11  1.805e-14  1.578e-12 1.177e-01  4.469e+00
10.0  14     3 shift  4.927e+00  2.379e+01  5.109e-02  5.720e+00 2.406e-01  4.684e+00

12.0  16     3 root   1.832e-14  8.992e-14  2.335e-15  1.056e-14 1.201e-01  4.766e+00
12.0  16     3 shift  4.349e+00  2.095e+01  4.488e-02  9.064e+00 4.325e-01  4.345e+00
```

## Reading

For shifted controls, the tail is tiny compared with the interpolation image:

```text
||tail|| << ||KWin k||.
```

The perpendicular residual `relPerp` matches the Lambda-elimination failure from E72.354.  Therefore
the dominant obstruction is:

```text
KWin k is not collinear with k.
```

Finite Weyl-root rows have tiny `k`, so they are not load-bearing tests for the Xi-window theorem.

## Consequence

The next analytic theorem should target:

```text
P_k^perp KWin k = P_k^perp tail + O(L^B)
```

on Xi-zero residue windows.  Since the signed tail is small in generic controls, the main missing
mechanism is an Xi-divisor eigenline relation for the Cauchy kernel matrix `KWin`.
