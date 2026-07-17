# E73.063 results - DEN-GAP L1 audit

## 1. Purpose

E73.063 tests whether `DEN-GAP` can be proved by the absolute estimate

```text
|C_x(t)| <= sum_n |xi_n|/|t-d_n|.
```

If this were sharp enough, the proof would be positive and elementary.  If not, `DEN-GAP` is a
signed cancellation statement.

## 2. Representative output

```text
E73.063 DEN-GAP L1 audit
 lam     L tau   gamma   signedB      l1B  cancelB    signed        l1      ratio
  16   5.545   14.13   37.59   -10.595    -1.199   -9.396  1.312e-08  1.283e-01  1.023e-07
  18   5.781   14.13   32.94   -12.421    -0.997  -11.424  3.429e-10  1.739e-01  1.972e-09
  20   5.991   14.13   30.42    -9.413    -0.988   -8.425  4.796e-08  1.705e-01  2.813e-07
  24   6.356   14.13   30.42   -13.608    -0.830  -12.778  1.176e-11  2.155e-01  5.456e-11
  24   6.356   14.13   37.59    -8.902    -1.054   -7.848  7.074e-08  1.424e-01  4.969e-07
```

## 3. Diagnosis

The absolute L1 ceiling is much too large:

```text
L1 ceiling:       about L^-1;
signed Cauchy:    about L^-9 to L^-13.
```

The cancellation factor is:

```text
signed / L1 about 1e-7 to 1e-11.
```

So `DEN-GAP` cannot be proved by a positive absolute bound on the rational kernel.

## 4. Consequence

Reject:

```text
DEN-GAP from sum |xi_n|/|t-d_n|.
```

The correct theorem is signed:

```text
SIGNED-CMAIN:
|sum_n xi_n/(t-d_n)|
<= C L^-8 sum_n |xi_n|/|t-d_n|
```

on FAR3 nodes, with enough slack to imply `CMAIN-10`.

## 5. Status

```text
observed: DEN-GAP is a signed cancellation of the finite CCM vector;
remaining: prove SIGNED-CMAIN from the pole-even eigenvector equation.
```
