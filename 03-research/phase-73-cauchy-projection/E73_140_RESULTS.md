# E73.140 Results - CCC Row Margin

Date: 2026-07-12.

Script:

```text
E73_140_ccc_row_margin.py
```

Purpose:

Separate two quantities that were too easy to conflate:

```text
Eval margin = q_gamma - p_gamma
```

which is the actual `ROW-KER_17` / `CSV_17` margin, and

```text
Cell margin = -log_L |<e_gamma,H_L xi_L>| - p_gamma
```

which only checks the finite Euler-cell consistency equation.

Output:

```text
 lam     L gamma      pRow  evalExp evalMargin  cellExp cellMargin status
  16   5.545   14.13     0.593   21.210     20.617   20.615     20.022 PASS
  16   5.545   21.02     0.588   20.585     19.997   21.312     20.724 PASS
  16   5.545   25.01    -0.225   14.056     14.281   21.459     21.685 FAIL
  20   5.991   14.13     0.611   19.861     19.250   19.859     19.248 PASS
  20   5.991   21.02     1.695   20.413     18.718   20.584     18.889 PASS
  20   5.991   25.01     1.045   20.354     19.310   22.567     21.522 PASS
  24   6.356   14.13     0.740   19.601     18.862   20.685     19.945 PASS
  24   6.356   21.02     0.784   19.771     18.987   19.525     18.740 PASS
  24   6.356   25.01     0.732   20.686     19.953   20.031     19.299 PASS
  28   6.664   14.13     2.599   19.780     17.181   20.442     17.843 PASS
  28   6.664   21.02     0.747   18.282     17.535   20.403     19.655 PASS
  28   6.664   25.01     0.632   18.811     18.179   19.163     18.532 PASS
```

Eigen-residual audit:

```text
||H xi - mu xi||/||H|| ~= 1e-16
```

so the cell residual is already at double-precision floor.  It is a
consistency check, not a proof route.

## Reading

The true rowwise signal is the evaluation margin.  Apart from the known
finite/base row at `lambda=16, gamma=25.01`, all tested asymptotic rows pass
`q_gamma-p_gamma >= 17`.

The cell margin also passes, but this cannot be used as a theorem because

```text
<e_gamma,H_L xi_L> = mu_L <e_gamma,xi_L>
```

and the numerical value is dominated by eigensolver residual once `mu_L` is
near `1e-14`.

## Consequence

The next analytic target must be the direct critical evaluation identity:

```text
<e_gamma,xi_L> = L^{-17-p_gamma} times a bounded quantity,
```

derived from the explicit cell formula, not from dividing or multiplying by
the small eigenvalue.

Thus `CCC` remains useful only in its global Euler-orbit form:

```text
Prime orbit sum = W02 - WR + negligible,
```

but the load-bearing theorem is the non-spectral cancellation of the
critical Cauchy evaluation itself.
