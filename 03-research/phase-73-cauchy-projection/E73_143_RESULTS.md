# E73.143 Results - PAIR20 Forcing Probe

Date: 2026-07-12.

Script:

```text
E73_143_pair20_forcing_probe.py
```

Purpose:

Test the too-strong sufficient route from E73.142:

```text
Pair_z^M(w) small separately,
TailPair_z^M(w) small separately.
```

Output:

```text
 lam     L gamma      pairMB  pairInfB    tailB rowRelInf status
  16   5.545   14.13   -20.872   -20.539  -20.973  4.55e-02 PASS
  16   5.545   21.02   -19.989   -19.398  -19.430  1.98e-03 FAIL
  16   5.545   25.01   -15.808   -14.966  -15.124  2.18e-06 FAIL
  20   5.991   14.13   -19.169   -18.433  -18.569  2.56e-02 FAIL
  20   5.991   21.02   -19.650   -19.596  -20.649  7.82e-03 FAIL
  20   5.991   25.01   -20.092   -18.350  -18.362  1.18e-02 FAIL
  24   6.356   14.13   -18.242   -18.185  -19.211  1.08e-02 FAIL
  24   6.356   21.02   -18.694   -18.238  -18.459  6.60e-02 FAIL
  24   6.356   25.01   -19.660   -19.226  -19.466  1.10e-01 FAIL
  28   6.664   14.13   -18.655   -17.416  -17.464  3.43e-03 FAIL
  28   6.664   21.02   -17.180   -16.998  -17.353  3.13e-03 FAIL
  28   6.664   25.01   -17.621   -17.537  -18.153  3.01e-02 FAIL
```

## Reading

The separate `PAIR20` route is too strong.  The active finite packet and
the finite tail are each often only around `L^-17` to `L^-19`.

This does not kill the local-divisor mechanism.  It says the proof must
keep the signed identity

```text
Pair_z^infty(w)=Pair_z^M(w)+TailPair_z^M(w)
```

instead of bounding `Pair_z^M` and `TailPair` by absolute values separately.

This agrees with the warning from E72.341: the finite signed tail is part of
the interpolation residual and should not be split incoherently.
