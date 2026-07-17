# E73.152 Results - Spectral-cutoff forced row certificate

Date: 2026-07-12.

Script:

```text
E73_152_spectral_cutoff_forced_row.py
```

Purpose:

Verify the finite spectral-cutoff identity for the signed forced Mellin rows,
using the correct row-action convention

```text
c_a(row)=row v_a.
```

This makes the null coefficient exactly

```text
alpha=row xi_L.
```

## Representative output

```text
E73.152 spectral-cutoff forced row certificate
Uses row-action coeffs c_a=row@v_a; alpha equals row@xi.
eps=L^-8.  Need alphaB<=-17 for SFRL-CUT_17.
 lam     L gamma row  alphaB   rowB  betaB     yB  nearB   midB  bulkB  errB nNear status
  16   5.545   14.13   0 -17.832  0.593 -10.638 -0.370 -10.638 -3.670  0.593 -18.008    30 PASS
  16   5.545   25.01   0 -13.584 -0.225  -4.590  3.410  -4.590 -0.444 -0.412 -13.761    30 FAIL
  20   5.991   21.02   0 -18.703  1.695  -8.299  0.730  -8.299 -1.886  1.695 -17.197    37 PASS
  24   6.356   25.01   0 -18.799  0.732 -10.566 -0.197 -10.566 -3.394  0.732 -17.909    42 PASS
  28   6.664   14.13   0 -16.536  2.599  -9.262  1.618  -9.262 -1.525  2.599 -15.417    49 FAIL
  32   6.931   14.13   0 -16.811  0.663 -10.731 -0.320 -10.731 -2.891  0.663 -17.022    55 FAIL
  32   6.931   14.13   1 -17.390  0.663 -10.731 -0.320 -10.731 -2.891  0.663 -17.031    55 PASS
```

The full run keeps the previous calibrated picture:

```text
PASS rows: all tested rows except the known transition/base failures.
FAIL rows:
lambda=16, gamma=25.01,
lambda=28, gamma=14.13,
lambda=32, gamma=14.13, row 0 barely below exponent 17.
```

## Checks

The reconstruction error `errB` is at the expected small scale for the
finite spectral identity.  Thus the cutoff decomposition is not a numerical
artifact:

```text
r = y_eps E_L + alpha xi_L^* + beta_eps.
```

The near-null tail `beta` is present but not decisive for rowspace distance.
Typical near-null exponents are around

```text
betaB ~= -8 to -11
```

in the stable rows.  This is why the full pseudoinverse is unstable: it tries
to divide these harmless components by tiny spectral gaps.

## Consequence

The finite algebra is now clean:

```text
SFRL-CUT_17 is equivalent to proving alpha=row xi_L is O(L^-17)
for the signed forced Mellin rows.
```

The next analytic work must bound `alpha` from the explicit signed Mellin
formula.  Spectral inversion, adjugates, and rowspace additions cannot supply
that bound by themselves.

## Current frontier

proved:

```text
spectral-cutoff decomposition;
correct row-action convention;
finite verification of reconstruction;
identification of transition failures.
```

open:

```text
uniform analytic alpha bound for the forced Mellin rows;
finite/transition absorption for the low-scale failures.
```
