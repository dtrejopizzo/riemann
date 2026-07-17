# E73.137 Results - Cell Balance Probe

Date: 2026-07-12.

Script:

```text
E73_137_cell_balance_probe.py
```

Purpose:

Inspect the explicit zeta-coupled cell equation in the critical evaluation
channel.  The CCM matrix is decomposed as

```text
H = W02 - WR - Prime.
```

For each normalized critical row `e_gamma`, the script measures:

```text
<e,W02 xi>,
<e,WR xi>,
<e,Prime xi>,
<e,xi>,
```

and the cancellation ratio

```text
|<e,(W02-WR-Prime)xi>| /
(|<e,W02 xi>|+|<e,WR xi>|+|<e,Prime xi>|).
```

Output:

```text
E73.137 cell balance probe
Measures <e,W02 xi>, <e,WR xi>, <e,Prime xi> for normalized critical rows.
 lam     L gamma      evalB    W02B     WRB  PrimeB balanceB cancelB
  16   5.545   14.13  -20.602   -1.468  -3.014  -1.511  -20.290 -19.227
  16   5.545   21.02  -19.922   -1.694  -3.234  -1.738  -21.186 -19.897
  16   5.545   25.01  -13.639   -0.981  -2.524  -1.024  -21.120 -20.543
  20   5.991   14.13  -19.580   -1.549  -3.108  -1.584  -19.038 -17.876
  20   5.991   21.02  -21.349   -2.777  -4.710  -2.795  -20.232 -17.842
  20   5.991   25.01  -18.916   -2.316  -3.815  -2.355  -20.462 -18.533
  24   6.356   14.13  -18.578   -2.242  -3.551  -2.293  -19.927 -18.059
  24   6.356   21.02  -21.363   -2.502  -3.785  -2.555  -21.061 -18.933
  24   6.356   25.01  -20.614   -2.546  -3.807  -2.601  -19.864 -17.693
```

## Reading

This is the first clear cell-level mechanism for ROW-KER.

The critical row sees:

```text
<e,W02 xi>    ~= L^-1 ... L^-2.5,
<e,Prime xi> ~= L^-1 ... L^-2.6,
```

with nearly identical exponents, while

```text
<e,WR xi>
```

is smaller by roughly one to two powers.

The full cell balance cancels to:

```text
cancelB ~= -18 to -20.
```

This matches the ROW-KER/CSV scale.  Therefore the cancellation is not
abstract spectral proximity; it is the explicit critical-row cancellation

```text
<e,W02 xi> - <e,Prime xi>
```

with `WR` and `mu<e,xi>` as lower-order corrections.

## Consequence

The next theorem should target:

```text
Critical Cell Cancellation:
<e_gamma,W02 xi> - <e_gamma,Prime xi>
 =
 <e_gamma,WR xi> + mu<e_gamma,xi> + O(L^{-17-p_gamma}).
```

Equivalently, prove the exact finite cell identity behind the observed
near equality of the archimedean `W02` channel and the prime channel in
critical rows.

This is the first candidate that is:

```text
explicit,
finite,
arithmetically coupled,
not a range-projection tautology,
not an arch/free artifact,
not a root-proximity assumption.
```

