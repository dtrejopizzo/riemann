# E73.124 Results - Source of the Cauchy Small-Value

Date: 2026-07-12.

Script:

```text
E73_124_csv_source_probe.py
```

Purpose:

Determine whether the `CSV` phenomenon isolated in E73.122 is:

```text
geometric / archimedean / parity-driven,
```

or genuinely produced by the zeta-coupled arithmetic vector.

The script compares the same Cauchy value

```text
C_x(-gamma)=sum_n xi_n/(-gamma-d_n)
```

for two finite CCM ground vectors:

```text
zeta-coupled vector: include_arith=True,
arch/free vector:    include_arith=False.
```

It also reports cancellation ratio

```text
|sum terms| / sum |terms|.
```

Output excerpt:

```text
E73.124 CSV source probe
Compares C_x(-gamma) for zeta-coupled vector and arch/free vector.
 rel = |C_zeta|/|C_arch|; cancel = |sum terms|/sum |terms|.
 lam     L tau     gamma    zetaB    archB     relB zCancelB aCancelB
  20   5.991   14.13   14.13  -18.960   -1.838  -17.122  -19.057   -1.464
  20   5.991   14.13   21.02  -19.690   -0.195  -19.495  -19.143   -0.196
  20   5.991   14.13   25.01  -17.871   -0.094  -17.778  -17.083   -0.160
  24   6.356   14.13   14.13  -17.817   -1.116  -16.701  -17.809   -0.909
  24   6.356   14.13   21.02  -21.992   -0.475  -21.517  -21.886   -0.310
  28   6.664   14.13   14.13  -20.760    1.215  -21.975  -20.404   -0.042
  28   6.664   14.13   21.02  -17.254   -0.546  -16.709  -17.323   -0.411
  32   6.931   14.13   14.13  -19.617   -2.145  -17.473  -19.475   -1.622
  32   6.931   14.13   25.01  -17.656   -2.294  -15.362  -17.386   -1.635
```

## Diagnostic

The arch/free vector does not satisfy CSV:

```text
archB is usually between L^-2 and L^1.
```

The zeta-coupled vector does:

```text
zetaB is consistently around L^-17 or smaller.
```

The ratio

```text
|C_zeta|/|C_arch|
```

is itself about `L^-15` to `L^-22`.

Therefore CSV is not a parity artifact, not an archimedean near-null, and
not a generic property of the finite Cauchy mesh.  It is created by the
coupled arithmetic vector.

## Consequence

The proof of CSV must use the zeta-coupled cell equation

```text
(C_E-mu) xi = 0
```

or an equivalent finite displacement identity.  It cannot be derived from
the free CCM geometry alone.

This points back to E73.017:

```text
<xi,(C_E-mu)Y_b> = 0
```

for rational source vectors `Y_b`.  If the Cauchy row

```text
k_gamma(d)=1/(-gamma-d)
```

can be decomposed as

```text
k_gamma = (C_E-mu)Y_gamma + R_gamma,
```

with `|<xi,R_gamma>| <= C L^-17`, then CSV follows.

This is the next load-bearing theorem.

