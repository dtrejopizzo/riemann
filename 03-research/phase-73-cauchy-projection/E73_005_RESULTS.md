# E73.005 results - coborder primitive audit

## Command

```text
python3 03-research/phase-73-cauchy-projection/E73_005_coborder_probe.py
```

## Output

```text
E73.005 coborder primitive probe
 lam     L   dim      |S|      eigRes    expEig    |Ymin|    |DY|     |D2Y|
   8   4.159    25 8.197e+00 1.179e-10 2.710e-10 1.224e+02 1.587e+03 2.442e+04
  10   4.605    29 9.108e+00 1.180e-10 2.964e-10 4.077e+02 5.308e+03 8.347e+04
  12   4.970    33 9.912e+00 3.393e-12 9.169e-12 5.222e+02 7.194e+03 1.202e+05
  14   5.278    37 1.054e+01 9.047e-11 2.600e-10 4.229e+02 6.513e+03 1.166e+05
```

## Interpretation

The source norm `|S|` is order `10`, but the eigenline residual

```text
eigRes=|<xi,S>|
```

is around `10^-10` in the tested windows.  The exponentially weighted residual is also tiny for the
synthetic off-line node used here.

The minimal unrestricted primitive

```text
Ymin=(C_E-mu I)^dagger(S-<xi,S>xi)
```

has polynomial-looking but sizable Sobolev norms.  This supports the coborder route while showing
that the proof cannot use a crude operator inverse; it must exploit the rational/divided-difference
structure of `Ymin`.

## Status

```text
verified: unrestricted coborder residual equals the NAT-SRC quantity;
observed: primitive norms are large but not visibly exponential in this range;
next: construct an explicit rational divided-difference primitive rather than using the pseudoinverse.
```

