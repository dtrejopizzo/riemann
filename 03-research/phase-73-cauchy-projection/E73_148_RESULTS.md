# E73.148 Results - Signed Forced Rowspace Probe

Date: 2026-07-12.

Script:

```text
E73_148_signed_rowspace_probe.py
```

Purpose:

Build the two forced signed rows

```text
M_L(w)^(-1)
[
 p_infty(z_1,w)
 p_infty(z_2,w)
]
```

as actual rows over the finite mesh, and measure their null components
against the ground vector `xi_L`.

Output:

```text
 lam     L gamma row    ampB   normB    relB      z1      z2 status
  16   5.545   14.13   0 -19.907   0.593 -20.499   14.13   21.02 PASS
  16   5.545   14.13   1 -20.529   0.593 -21.121   14.13   21.02 PASS
  16   5.545   21.02   0 -19.257   0.588 -19.844   30.42   37.59 PASS
  16   5.545   21.02   1 -19.836   0.588 -20.424   30.42   37.59 PASS
  16   5.545   25.01   0 -13.602  -0.225 -13.377   21.02   25.01 FAIL
  16   5.545   25.01   1 -14.281  -0.225 -14.056   21.02   25.01 FAIL
  20   5.991   14.13   0 -18.583   0.611 -19.194   14.13   37.59 PASS
  20   5.991   14.13   1 -19.193   0.611 -19.804   14.13   37.59 PASS
  20   5.991   21.02   0 -18.868   1.695 -20.563   25.01   37.59 PASS
  20   5.991   21.02   1 -18.777   1.695 -20.472   25.01   37.59 PASS
  20   5.991   25.01   0 -18.132   1.045 -19.177   32.94   37.59 PASS
  20   5.991   25.01   1 -19.295   1.045 -20.339   32.94   37.59 PASS
  24   6.356   14.13   0 -18.070   0.740 -18.810   25.01   37.59 PASS
  24   6.356   14.13   1 -18.649   0.740 -19.389   25.01   37.59 PASS
  24   6.356   21.02   0 -18.905   0.784 -19.690   25.01   32.94 PASS
  24   6.356   21.02   1 -18.188   0.784 -18.972   25.01   32.94 PASS
  24   6.356   25.01   0 -19.830   0.732 -20.563   30.42   32.94 PASS
  24   6.356   25.01   1 -19.694   0.732 -20.427   30.42   32.94 PASS
  28   6.664   14.13   0 -16.886   2.599 -19.485   14.13   30.42 FAIL
  28   6.664   14.13   1 -16.522   2.599 -19.121   14.13   30.42 FAIL
  28   6.664   21.02   0 -17.313   0.747 -18.061   14.13   32.94 PASS
  28   6.664   21.02   1 -17.735   0.747 -18.482   14.13   32.94 PASS
  28   6.664   25.01   0 -18.003   0.632 -18.635   14.13   25.01 PASS
  28   6.664   25.01   1 -17.458   0.632 -18.090   14.13   25.01 PASS
  32   6.931   14.13   0 -17.770   0.663 -18.433   21.02   30.42 PASS
  32   6.931   14.13   1 -17.534   0.663 -18.197   21.02   30.42 PASS
  32   6.931   21.02   0 -17.859   0.936 -18.796   14.13   32.94 PASS
  32   6.931   21.02   1 -17.748   0.936 -18.684   14.13   32.94 PASS
  32   6.931   25.01   0 -18.839   0.660 -19.499   32.94   37.59 PASS
  32   6.931   25.01   1 -17.570   0.660 -18.231   32.94   37.59 PASS
```

Here

```text
ampB  = log_L |row xi|,
normB = log_L ||row||,
relB  = log_L(|row xi|/||row||).
```

## Reading

The forced signed rows are not small as vectors; their norms are typically
polynomial.  What is small is precisely their null component.

Thus the correct proof language is rowspace proximity:

```text
forced signed row = rowspace row + small null component.
```

The same two transition failures remain:

```text
lambda=16, gamma=25.01,
lambda=28, gamma=14.13.
```

The first is already part of the finite/base manifest.  The second is a
transition row that must either be absorbed into an enlarged manifest or
removed by a sharper row choice / scale schedule.

A free-row stress for `lambda=28, gamma=14.13`, allowing a small grid of
imaginary row heights and several `sigma` values, did not improve the
margin:

```text
best free-row margin ~= 16.60 < 17.
```

So this is not simply a poor choice among the first few zero-height rows.
It should be treated as a finite transition case unless a different scale
schedule changes the raw ROW-KER margin.

## Consequence

The next lemma is no longer a packet-size lemma.  It is:

```text
Signed Forced Rowspace Lemma:
dist(r_{w,j}, Row(H_L-mu_L I)) <= C L^-17
```

for the two forced rows `r_{w,j}`.

Because `Row(H_L-mu_L I)=xi_L^perp`, this is equivalent to the explicit
scalar residual

```text
|r_{w,j} xi_L| <= C L^-17.
```

This is a finite identity with a direct verifier.
