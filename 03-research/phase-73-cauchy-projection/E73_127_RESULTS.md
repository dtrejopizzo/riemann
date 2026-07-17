# E73.127 Results - Characteristic Reformulation of CSV

Date: 2026-07-12.

Script:

```text
E73_127_characteristic_csv_probe.py
```

Purpose:

After E73.126 showed that displacement-image projection is scalar-invisible,
CSV is reformulated using the finite characteristic function

```text
Phi_N(s) = (2/sqrt(L)) sin(sL/2) C_x(s).
```

CSV at `s=-gamma` becomes a characteristic small-value statement:

```text
Phi_N(-gamma) is small at the critical ordinates.
```

Output:

```text
E73.127 characteristic CSV probe
Phi_N(s)=(2/sqrt(L))sin(sL/2)C_x(s), evaluated at s=-gamma.
 lam     L gamma        CB      phiB    sineB
  16   5.545   14.13   -20.533   -20.630   -0.097
  16   5.545   21.02   -20.003   -20.107   -0.103
  16   5.545   25.01   -14.281   -15.240   -0.959
  20   5.991   14.13   -19.326   -19.440   -0.114
  20   5.991   21.02   -18.716   -19.911   -1.195
  20   5.991   25.01   -19.295   -19.848   -0.553
  24   6.356   14.13   -18.860   -19.101   -0.241
  24   6.356   21.02   -19.079   -19.366   -0.287
  24   6.356   25.01   -19.792   -20.031   -0.238
  28   6.664   14.13   -17.177   -19.276   -2.099
  28   6.664   21.02   -17.526   -17.775   -0.249
  28   6.664   25.01   -18.124   -18.261   -0.137
  32   6.931   14.13   -18.582   -18.747   -0.164
  32   6.931   21.02   -18.073   -18.510   -0.437
  32   6.931   25.01   -17.529   -17.693   -0.164
```

## Reading

The sine factor is usually only order `L^0` to `L^-1`; it does not create
the CSV cancellation.  The smallness is already in `C_x(-gamma)`, and it
persists in the finite characteristic function `Phi_N`.

Thus the viable theorem is not global convergence of raw `Phi_N` to `Xi`
as in E71.6.  The local theorem needed here is weaker:

```text
Characteristic CSV:
For every natural-height critical row gamma in the Phase 73 gate,

|Phi_N(-gamma)| <= C L^-17
```

up to the harmless sine normalization factor.

## Connection to earlier work

E71.6 showed that a naive global scalar normalization of `Phi_N` does not
give locally uniform convergence to `Xi`.  E73.127 does not revive that
failed global route.  It asks only for finite interpolation smallness at
the critical ordinates used in the GATE-73 rows.

This is a strictly narrower theorem and is the correct replacement for the
failed displacement-image attempt of E73.126.

