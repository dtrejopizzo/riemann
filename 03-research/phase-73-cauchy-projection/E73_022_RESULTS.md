# E73.022 results - scalar dual formula

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_022_scalar_dual_formula_probe.py
```

Output:

```text
E73.022 scalar dual formula probe
Compares <xi,S_b> by direct mesh source and rational Cauchy scalar formula.
 lam     L       |direct|    |formula|      absErr     expWeighted
   8   4.159    1.179e-10    1.179e-10   6.38e-17     2.710e-10
   8   4.159    1.746e-12    1.746e-12   1.79e-20     4.011e-12
   8   4.159    4.002e-09    4.002e-09   8.15e-17     9.194e-09
  10   4.605    1.180e-10    1.180e-10   2.45e-17     2.964e-10
  10   4.605    1.866e-12    1.866e-12   3.62e-20     4.686e-12
  10   4.605    3.722e-09    3.722e-09   8.45e-17     9.349e-09
  12   4.970    3.393e-12    3.393e-12   3.23e-16     9.168e-12
  12   4.970    8.965e-14    8.965e-14   3.31e-20     2.422e-13
  12   4.970    4.723e-11    4.723e-11   1.16e-16     1.276e-10
  14   5.278    9.047e-11    9.048e-11   1.55e-15     2.600e-10
  14   5.278    1.530e-12    1.530e-12   4.97e-19     4.396e-12
  14   5.278    2.479e-09    2.479e-09   6.31e-16     7.123e-09
  16   5.545    2.174e-10    2.174e-10   1.16e-14     6.589e-10
  16   5.545    3.338e-12    3.338e-12   2.94e-18     1.012e-11
  16   5.545    7.070e-09    7.070e-09   8.51e-15     2.143e-08
  18   5.781    1.471e-10    1.471e-10   9.53e-15     4.674e-10
  18   5.781    2.078e-12    2.078e-12   2.42e-18     6.604e-12
  18   5.781    5.230e-09    5.230e-09   9.59e-15     1.662e-08
```

Conclusion:

```text
<xi,S_b>
= sum_{k in K_L} Pi(b,k)(exp(i gamma_k L)-1)
  sum_n conjugate(xi_n)/(gamma_k+d_n)
```

matches the direct mesh pairing to numerical precision.

The scalar gate is therefore an explicit rational Cauchy residue identity.
