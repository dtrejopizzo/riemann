# E73.069 results - exact FAR3 rowspace budget

## 1. Purpose

E73.069 reruns the FAR3 rowspace test using the exact ground eigenvector instead of the symmetric
gauge vector.

The quantity tested is the exact main contribution

```text
T_k=Pref_k(A,L)|<xi_x,k_{-gamma_k}>|
```

on the three FAR-selected nodes.

## 2. Representative output

```text
E73.069 exact FAR3 row probe
Uses the exact ground eigenvector, not the symmetric gauge vector.
 lam     L tau   gamma  signedB relB weightB  ||Ex||B  signed    weighted
  16   5.545   14.13   37.59  -11.402 -10.509  -7.185  -19.307 3.293e-09  4.517e-06
  16   5.545   14.13   30.42  -11.853 -11.198  -7.866  -19.307 1.522e-09  1.408e-06
  16   5.545   14.13   32.94  -10.233  -9.477  -6.630  -19.307 2.443e-08  1.168e-05
  18   5.781   14.13   37.59  -10.625  -9.799  -6.118  -19.271 8.019e-09  2.177e-05
  18   5.781   14.13   32.94  -11.244 -10.565  -6.923  -19.271 2.707e-09  5.303e-06
  18   5.781   14.13   30.42   -8.346  -7.779  -6.066  -19.271 4.370e-07  2.388e-05
  20   5.991   14.13   32.94  -11.914 -11.311  -7.565  -18.334 5.447e-10  1.312e-06
  20   5.991   14.13   37.59  -10.293  -9.530  -6.247  -18.334 9.920e-09  1.389e-05
  20   5.991   14.13   30.42   -9.485  -9.012  -6.993  -18.334 4.214e-08  3.650e-06
  24   6.356   14.13   32.94  -12.838 -12.396  -8.659  -18.250 4.883e-11  1.111e-07
  24   6.356   14.13   30.42  -14.115 -13.884 -10.143  -18.250 4.603e-12  7.138e-09
  24   6.356   14.13   37.59   -9.015  -8.370  -6.095  -18.250 5.748e-08  1.271e-05
```

## 3. Diagnosis

The exact FAR3 weighted terms satisfy:

```text
T_k = L^-6 to L^-10
```

in the tested range.  This is comfortably within the `Main_3=O(L^-5)` budget.

The weakest visible row is the `gamma=37.59` node at `lambda=24`, but even there

```text
weightB=-6.095,
```

which leaves one full power of `L` of slack relative to `ROW-MAIN-5`.

## 4. Consequence

The exact-eigenline version strengthens the current endpoint:

```text
EXACT-ROW-MAIN-5:
sum_{gamma_k in FAR3(A,L)}
Pref_k(A,L)|<xi_x,k_{-gamma_k}>|
<= C L^-5.
```

This is the same theorem as `ROW-MAIN-5`, but with the proof object fixed correctly.

## 5. Status

```text
observed: exact eigenline gives the right FAR3 budget with slack;
corrected: symmetric gauge removed from load-bearing statements;
open: prove EXACT-ROW-MAIN-5 analytically from the finite CCM eigenline equation.
```
