# E73.153 Results - Forced row collapse

Date: 2026-07-12.

Script:

```text
E73_153_forced_row_collapse.py
```

Purpose:

Verify coordinatewise that the complete signed forced Mellin rows are exactly
the two Cauchy divisor rows:

```text
M_L(w)^(-1)
[P_{z_1,w}^{signed};P_{z_2,w}^{signed}]
=
[1/(w+i d_n);1/(-w+i d_n)].
```

## Output summary

The verifier tested several non-optimized row pairs `z_1,z_2` for

```text
lambda=16,20,24,28,32,
gamma=14.13,21.02,25.01.
```

Representative rows:

```text
 lam     L gamma      z1      z2      cond       rowId       err0       err1
  16   5.545   14.13   14.13   21.02  1.74e+02   2.69e-15   7.23e-14   2.68e-15
  20   5.991   21.02   14.13   25.01  7.62e+00   2.87e-14   3.50e-14   2.88e-14
  24   6.356   25.01   14.13   30.42  7.19e+00   6.08e-15   3.30e-14   4.40e-15
  28   6.664   14.13   14.13   21.02  1.18e+02   2.15e-13   2.35e-13   2.15e-13
  32   6.931   25.01   14.13   25.01  1.58e+02   1.38e-15   2.47e-14   1.42e-15
```

Here:

```text
rowId = ||[P_z1;P_z2] - M[q_w;q_-w]|| / ||[P_z1;P_z2]||,
err0  = ||decoded row 0 - q_w||/||q_w||,
err1  = ||decoded row 1 - q_-w||/||q_-w||.
```

All errors are at floating-point scale, with the largest displayed errors
around `1e-13`.

## Consequence

The complete signed two-row forcing is an exact decoder, not an amplifier:

```text
forced row = Cauchy divisor row.
```

Therefore E73.149--E73.152 should be read as follows:

```text
correct: complete Mellin pair lies in the ideal (H_0(w),H_0(-w));
correct: rowspace distance is the null Cauchy coefficient;
false hope: choosing z_1,z_2 creates a stronger rowspace row.
```

The active frontier returns to the direct Cauchy divisor estimate:

```text
H0-DIV_17:
|H_0(w)|+|H_0(-w)| <= C L^-17
```

for the critical standard-box nodes.

## Updated map

```text
H0-DIV_17
=> LDIV_17
=> CSV_17
=> Asymptotic Standard-Box Theorem
=> Uniform GATE-73
=> scalar WRL
=> Omega_7.
```

The next proof must use the eigenline equation and the finite Feshbach
structure to estimate the Cauchy transform directly.
