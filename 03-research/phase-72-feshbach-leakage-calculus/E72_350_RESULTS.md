# E72.350 RESULTS -- TailBasis row stress

**Command**

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_349_cfir_row_candidate_probe.py
```

## Selected results

```text
 lam   N roots node       mode      maxNullAmp    maxRelNull    rmsRelNull
  6.0  10     2  root     tail   8.02252e-16   8.82174e-15   6.50873e-15
  6.0  10     2  root window_tail   1.48548e-15   1.28185e-16   1.04771e-16
  6.0  10     2  root window_minus_tail   6.16719e-16   4.85492e-17   4.51986e-17
  6.0  10     2 shift     tail   4.92013e-03   2.08751e-03   1.59756e-03
 6.0  10     2 shift window_tail   3.33864e+00   1.20840e-01   8.75266e-02
 6.0  10     2 shift window_minus_tail   3.34362e+00   1.10411e-01   8.05814e-02
  6.0  10     2 shift   fitLam   4.61154e-01   3.19936e-02   2.46128e-02

  8.0  12     3  root     tail   3.19701e-15   2.17557e-14   1.41998e-14
  8.0  12     3  root window_tail   1.35874e-11   7.27820e-13   4.25233e-13
  8.0  12     3  root window_minus_tail   1.35809e-11   7.25083e-13   4.23554e-13
  8.0  12     3 shift     tail   2.22147e-02   6.34339e-03   4.19890e-03
 8.0  12     3 shift window_tail   1.61618e+01   2.18073e-01   1.77929e-01
 8.0  12     3 shift window_minus_tail   1.61788e+01   2.19231e-01   1.78135e-01
  8.0  12     3 shift   fitLam   4.34578e+00   6.81866e-02   5.66583e-02

 10.0  14     3 shift     tail   4.40100e-02   3.95621e-03   2.68725e-03
 10.0  14     3 shift window_tail   1.74115e+01   1.89467e-01   1.31048e-01
 10.0  14     3 shift window_minus_tail   1.74946e+01   1.72555e-01   1.20113e-01
 10.0  14     3 shift   fitLam   4.07081e+00   5.34710e-02   4.76734e-02

 12.0  16     3 shift     tail   4.03168e-02   4.43739e-03   2.89294e-03
 12.0  16     3 shift window_tail   1.85437e+01   1.26997e-01   7.86881e-02
 12.0  16     3 shift window_minus_tail   1.85102e+01   1.30222e-01   8.06980e-02
 12.0  16     3 shift   fitLam   7.89793e+00   8.22170e-02   6.78982e-02
```

## Interpretation

`TailBasis` alone has shifted relative defects around

```text
2e-3 to 6e-3,
```

much smaller than the partial `window` row, whose shifted relative defect is about

```text
0.13 to 0.22.
```

But `window + tail` and `window - tail` remain at the same order as `window`.  Therefore the collapsed
tail is correctly small/coherent, but it is not the missing cancellation that closes the shifted row.

Allowing one fitted scalar `Lambda` per finite window improves the shifted relative defect to

```text
3e-2 to 8e-2,
```

but still does not close it.  Thus a scalar left-coefficient correction is helpful but insufficient.
E72.351 proves the exact consistency criterion and records that the nodewise `Lambda_a` values have
large relative spread in shifted controls.

E72.352 corrects the next-step diagnosis.  The full coupled transformed operator row

```text
T_W02 - T_WR - T_Prime - 2kappa_*G.
```

is load-bearing only before the residual row is formed.  Once the finite singular
operator `E=C_E-mu I` and null vector `xi` are fixed, every additive rowspace correction
`A E` satisfies

```text
(R + A E)xi = R xi.
```

Therefore it cannot repair the observed CFIR row defect.  The missing object must be
an exact construction of the residual row `R_T` itself: normalization, Hermite window,
TailBasis sign, balanced kernel, or a non-rowspace compatibility identity.

## Status

```text
validated: TailBasis implementation is finite and stable;
observed: TailBasis is not enough to repair incomplete window rows;
corrected: additive operator rows cannot repair row-ideal defects;
next: derive the exact residual row R_T and prove its row-ideal membership.
```
