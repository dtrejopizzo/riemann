# E72.264 -- Pole-even stable rational LM8 probe

**Purpose.** Rationalize the corrected pole-even homogeneous LM8 envelope from E72.263 in the stable
windows.

The corrected geometry is:

```text
C_model = B_even^T(H_model-e_pole I)B_even,
```

with the global odd pole energy subtracted and no accidental even line removed.

## Stable window

This probe targets the stable threshold:

```text
lambda >= 20
```

and tests the currently computed windows:

```text
lambda=20,24.
```

The transition window `lambda=16` is not included: E72.263 shows exact BSE passes there, but the
homogeneous envelope is too loose. It should be handled by a separate sharp finite certificate.

## Rational coefficients

Using the E72.263 `R`-degree-8 fit, add a homogeneous buffer `0.002 u^2`, i.e. add `0.002` to the
constant coefficient of each `R_j`, and round to six decimals:

```text
R0 =
  1.001029
 -1.951429 u
-18.253404 u^2
 -8.529708 u^3
+263.566056 u^4
+210.580938 u^5
-1548.826040 u^6
-746.639401 u^7
+3247.543544 u^8

R1 =
  1.000747
 -2.513120 u
-13.197720 u^2
+21.797818 u^3
+127.757425 u^4
-135.585710 u^5
-348.702213 u^6
+197.008969 u^7
+325.771912 u^8
```

These are rationals with denominator `10^6`.

## Stress output

```text
buffer=0.002, decimals=6
min R0-1       on [-1,0] = +1.029000e-03
min R0-0.09    on [0,1]  = +1.995770e-03
min R1-1       on [-1,0] = +7.470000e-04
min R1-0.16    on [0,1]  = +1.997180e-03

lambda=20  exact=8.277297e-01  env=9.154717e-01  slack=+2.542831e-02
lambda=24  exact=7.748451e-01  env=8.898777e-01  slack=+5.102225e-02
```

## Status

This is a floating stress check. E72.265 gives the exact rational Bernstein certificate for the four
univariate inequalities.
