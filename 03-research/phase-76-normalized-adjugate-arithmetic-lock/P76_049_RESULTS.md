# P76.049 - Mixed shell cocycle results

The block identity `(MSC-3)` and its derivative close with relative errors
between `1e-76` and `1e-64` for `N=5,...,9`.

However the signed terms are large:

```text
N       |t0|          |tau Sigma^-1 kappa|       |Tnew|
5       2.28e3         3.51e3                     1.23e3
7       3.55e6         4.76e6                     1.21e6
9       8.92e6         1.14e7                     2.44e6
```

The shell inverse and Cauchy residuals are also individually unstable.  Thus
the observed `N^-2` gain is not present in the raw block update and cannot be
proved by bounding `(MSC-3)` termwise.

The amplitude must first be cancelled by a safe-point cross ratio.  This is
consistent with P76.034: only ratios normalized wholly inside `Re(s)>1` are
canonical and stable.
