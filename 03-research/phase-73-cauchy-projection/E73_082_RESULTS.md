# E73.082 results - H0 zero-window budget

## 1. Purpose

E73.080 reduced the complete-mesh factor budget to a nodal `H_0` estimate:

```text
sum_{w in Z_T/+-} ( |H_0(w)|+|H_0(-w)| ).
```

E73.082 measures this quantity on critical-height windows of different sizes.

## 2. Output

```text
E73.082 H0 zero-window budget probe
Measures sum_{w in Z_T/+-} (|H0(w)|+|H0(-w)|).
 lam     L nwin      sumB      maxB        sum        max
  16   5.545    3   -13.443   -13.443  9.984e-11  9.983e-11
  16   5.545    5   -10.142   -10.209  2.850e-08  2.544e-08
  16   5.545    8    -9.907   -10.209  4.264e-08  2.544e-08
  18   5.781    3   -12.990   -12.990  1.265e-10  1.263e-10
  18   5.781    5    -7.879    -7.882  9.924e-07  9.866e-07
  20   5.991    3   -17.762   -18.092  1.547e-14  8.569e-15
  20   5.991    8    -8.843    -8.954  1.332e-07  1.092e-07
  24   6.356    3   -17.500   -17.575  8.788e-15  7.650e-15
  24   6.356    8    -8.646    -8.647  1.136e-07  1.134e-07
```

## 3. Diagnosis

The first three critical nodes have very strong cancellation:

```text
sumB = L^-13 to L^-17.
```

Larger windows are controlled by a single dominant node and degrade to:

```text
sumB = L^-8 to L^-10.
```

Thus a completely uniform large-window `H_0` bound is too crude for the final budget unless the
coefficient weights or FAR selection are kept.

## 4. Consequence

The correct target should not be a blind window sum.  It should be a weighted nodal estimate:

```text
HWIN:
sum_{w in Z_T/+-} C_L(z,w)( |H_0(w)|+|H_0(-w)| )
```

with the actual coefficient weights and the actual finite window used by the Cauchy projection.

The data support strong cancellation on selected critical nodes, but not an arbitrary enlargement of
the window.

## 5. Status

```text
observed: very strong H_0 cancellation on small selected windows;
observed: larger windows develop a dominant node near L^-8;
correction: use weighted HWIN, not a blind H_0 window sum.
```
