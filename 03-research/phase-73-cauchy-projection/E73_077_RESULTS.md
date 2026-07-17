# E73.077 results - pair coefficient budget

## 1. Purpose

E73.075 proves

```text
Pair_z^infty(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).
```

E73.077 measures the separated budget

```text
|A_L(z,w)H_0(w)|+|B_L(z,w)H_0(-w)|
```

at critical heights and at a non-nodal control frequency.

## 2. Representative output

```text
E73.077 pair coefficient budget probe
Measures Pair=A H0(w)+B H0(-w) term sizes at critical heights.
 lam     L   zIm    wIm      pairB   AH+BHB    ABmaxB    HmaxB    pair
  16   5.545  14.13   14.13  -18.838  -18.847    1.756  -20.041  9.68e-15
  16   5.545  14.13   21.02  -20.307  -19.933   -0.270  -19.144  7.82e-16
  16   5.545  14.13   25.01  -14.966  -14.962   -1.060  -13.602  7.35e-12
  16   5.545  14.13   28.40  -10.621   -9.828   -1.289   -8.475  1.26e-08
  20   5.991  14.13   14.13  -17.446  -17.605    1.754  -19.360  2.72e-14
  20   5.991  14.13   21.02  -18.349  -19.571   -0.966  -18.668  5.41e-15
  20   5.991  14.13   28.40   -7.993   -7.988   -1.069   -6.949  6.09e-07
  24   6.356  14.13   14.13  -17.046  -17.184    1.638  -17.625  2.03e-14
  24   6.356  14.13   21.02  -18.591  -19.252   -0.315  -19.093  1.17e-15
  24   6.356  14.13   28.40   -5.203   -5.030   -0.405   -4.144  6.62e-05
```

Here `valueB=log(value)/log(L)`.

## 3. Diagnosis

At critical heights `w=i gamma`, the coefficient-weighted divisor terms are tiny:

```text
|A H_0(w)|+|B H_0(-w)| = L^-17 to L^-20
```

for the first critical heights in the tested range.

At the non-nodal control frequency `w=28.40i`, the same quantity degrades to about

```text
L^-5 to L^-10.
```

This is exactly what the divisor theorem predicts: the budget is a nodal budget, not a global
frequency bound.

## 4. Status

```text
observed: coefficient-weighted pair divisibility has large slack at critical nodes;
observed: non-nodal controls do not have the same slack;
next: formulate the remaining budget as a coefficient-weighted H_0 nodal estimate.
```
