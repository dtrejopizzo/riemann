# E73.095 results - OUT-FAR finite-window budget

## 1. Purpose

`GATE-73` separates outside control into:

```text
1. high zero tail beyond T_L=e^L L^A, already closed by E72.394;
2. finite FAR3 complement inside the natural-height window.
```

E73.095 measures the second piece:

```text
OUT-FAR_fin(A,L)
:=
sum_{gamma_k in K_L \ D_3(A,L)}
W_k(A,L)|C_x(i gamma_k)|.
```

The FAR3 set is selected by the non-tautological FAR score:

```text
F_k=W_k(A,L)dist(-gamma_k,Div(P_x)),
```

not by the final WCS term.

## 2. Output

```text
E73.095 OUT-FAR finite-window budget probe
Tail is the WCS contribution outside the FAR3 selected rows, inside finite K_L.
 lam     L tau nK      totalB    main3B    tailB  tailFracB  farGammas
  16   5.545   14.13 12     -6.110    -6.111  -10.504     -4.394 37.6,30.4,32.9
  16   5.545   21.02 12     -6.108    -6.108  -11.206     -5.098 37.6,30.4,32.9
  18   5.781   14.13 12     -6.621    -6.621  -10.867     -4.247 37.6,32.9,30.4
  18   5.781   21.02 12     -6.752    -6.752  -11.552     -4.800 37.6,32.9,30.4
  20   5.991   14.13 12     -6.282    -6.282  -14.213     -7.931 32.9,37.6,30.4
  20   5.991   21.02 12     -6.312    -6.312  -14.314     -8.002 37.6,32.9,30.4
  24   6.356   14.13 12     -5.974    -5.974  -15.634     -9.660 32.9,30.4,37.6
  24   6.356   21.02 12     -5.930    -5.930  -13.630     -7.700 32.9,30.4,37.6
```

The output is stable for `nK=6,8,10,12` in the tested range.

## 3. Diagnosis

The finite FAR3 complement satisfies:

```text
worst tested OUT-FAR_fin exponent = L^-10.504.
```

Thus the finite complement is below the `L^-9` tail scale in all but the smallest tested line if
one insists on `L^-9`, and below the `L^-5` main scale with very large slack in every line.

The `tailFracB` column improves from about `L^-4.2` to `L^-9.7` across the tested range.

## 4. Consequence

The correct finite outside certificate is:

```text
OUT-FAR_fin(A,L):
sum_{gamma_k in K_L \ D_3(A,L)}
W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|
<= C_out L^-9
```

or, for the main scalar-WRL gate with more slack:

```text
<= C_out L^-5.
```

The high zero tail is separately closed by E72.394:

```text
OUT-HIGH(A,L): |Im w|>T_L=e^L L^A.
```

Therefore:

```text
OUT-FAR = OUT-FAR_fin + OUT-HIGH.
```

## 5. Status

```text
proved: OUT-HIGH beyond natural height is polynomial/decaying (E72.394);
verified: finite FAR3 complement is tiny in the harness;
open: uniform proof of OUT-FAR_fin from divisor spacing and FAR selection.
```
