# E73.134 Results - Rowwise Kernel Margin

Date: 2026-07-12.

Script:

```text
E73_134_rowwise_kernel_margin.py
```

Purpose:

Correct the aggregate kernel formulation of E73.132/E73.133 by measuring
the exact rowwise quantities:

```text
p_gamma = log ||k_gamma|| / log L,
q_gamma = - log |<xi,e_gamma>| / log L,
e_gamma = k_gamma / ||k_gamma||.
```

Since

```text
|C_x(-gamma)| = ||k_gamma|| |<xi,e_gamma>|,
```

the CSV exponent is exactly:

```text
q_gamma - p_gamma.
```

For `CSV_17` one needs:

```text
q_gamma - p_gamma >= 17.
```

Output:

```text
E73.134 rowwise kernel margin
p=log||k||/logL, q=-log|<xi,e>|/logL, csvExp=log|C|/logL.
Need q-p >= 17 for CSV_17.
 lam     L gamma      pRow      qNorm   q-p    csvExp status
  16   5.545   14.13     0.593     21.125 20.533   -20.533 PASS
  16   5.545   21.02     0.588     20.591 20.003   -20.003 PASS
  16   5.545   25.01    -0.225     14.056 14.281   -14.281 FAIL
  20   5.991   14.13     0.611     19.937 19.326   -19.326 PASS
  20   5.991   21.02     1.695     20.411 18.716   -18.716 PASS
  20   5.991   25.01     1.045     20.339 19.295   -19.295 PASS
  24   6.356   14.13     0.740     19.599 18.860   -18.860 PASS
  24   6.356   21.02     0.784     19.864 19.079   -19.079 PASS
  24   6.356   25.01     0.732     20.525 19.792   -19.792 PASS
  28   6.664   14.13     2.599     19.776 17.177   -17.177 PASS
  28   6.664   21.02     0.747     18.273 17.526   -17.526 PASS
  28   6.664   25.01     0.632     18.756 18.124   -18.124 PASS
  32   6.931   14.13     0.663     19.245 18.582   -18.582 PASS
  32   6.931   21.02     0.936     19.009 18.073   -18.073 PASS
  32   6.931   25.01     0.660     18.190 17.529   -17.529 PASS
```

## Reading

The rowwise margin formulation handles near-pole amplification correctly.
For example, at `lambda=28`, `gamma=14.13`,

```text
p_gamma = 2.599
```

but the normalized leak is stronger:

```text
q_gamma = 19.776,
```

so

```text
q_gamma-p_gamma = 17.177.
```

Thus the right kernel theorem is not aggregate `||K xi|| <= L^-18`.
It is the rowwise margin theorem:

```text
ROW-KER_17:
|<xi,e_gamma>| <= L^{-17-p_gamma}
```

where `||k_gamma|| <= L^{p_gamma}`.

The only failing row in this table is `lambda=16, gamma=25.01`, which is
outside the asymptotic standard-box regime and is handled as part of the
finite/base bookkeeping rather than the uniform theorem.

