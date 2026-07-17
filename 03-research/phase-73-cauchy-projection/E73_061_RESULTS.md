# E73.061 results - CMAIN divisor factors

## 1. Purpose

E73.061 splits the Cauchy value

```text
C_x(t)=P_x(t)/D_x(t)
```

on FAR3 nodes into numerator and denominator exponent contributions.

## 2. Representative output

```text
E73.061 CMAIN divisor-factor probe
 lam     L tau   gamma      numB      denB        cB        |P|        |D|       |C|
  16   5.545   14.13   37.59    74.473    85.068   -10.595  2.519e+55  1.920e+63 1.312e-08
  18   5.781   14.13   30.42    74.939    84.024    -9.085  1.265e+57  1.059e+64 1.194e-07
  20   5.991   14.13   32.94    80.126    92.126   -12.000  2.000e+62  4.278e+71 4.675e-10
  24   6.356   14.13   30.42    85.056    98.664   -13.608  2.072e+68  1.763e+79 1.176e-11
  24   6.356   14.13   37.59    99.303   108.205    -8.902  5.742e+79  8.117e+86 7.074e-08
```

## 3. Diagnosis

`CMAIN` is not caused by a small numerator in absolute size.  Both numerator and denominator are
huge:

```text
|P_x| about L^65 to L^99;
|D_x| about L^78 to L^108.
```

The small Cauchy value comes from a denominator-numerator exponent gap:

```text
denB - numB about 9 to 14.
```

Thus the correct arithmetic target is not:

```text
P_x is small.
```

It is:

```text
D_x dominates P_x by at least L^10 on FAR3 nodes.
```

## 4. Status

```text
observed: CMAIN comes from a divisor gap |D_x|/|P_x|;
next target: DEN-GAP.
```
