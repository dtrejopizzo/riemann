# E73.144 Results - Optimized Two-Row Pair Forcing

Date: 2026-07-12.

Script:

```text
E73_144_two_row_pair_optimizer.py
```

Purpose:

For each critical node `w=-i gamma`, choose the best two rows among the
first six FAR heights and measure

```text
margin = -log_L ||M_L(w;z_1,z_2)^(-1) Pair^M(w)||_1.
```

The target for direct active-packet forcing is:

```text
margin >= 17.
```

Output:

```text
 lam     L gamma    margin    ampB  pairNormB      z1      z2 status
  16   5.545   14.13    19.713   1.256    -18.592   14.13   21.02 PASS
  16   5.545   21.02    20.037   1.472    -19.951   25.01   32.94 PASS
  16   5.545   25.01    14.991   2.649    -17.065   30.42   32.94 FAIL
  20   5.991   14.13    18.835   0.917    -17.909   14.13   30.42 PASS
  20   5.991   21.02    18.483   2.361    -19.609   25.01   32.94 PASS
  20   5.991   25.01    19.559   1.818    -20.009   30.42   37.59 PASS
  24   6.356   14.13    17.625   1.105    -17.216   14.13   37.59 PASS
  24   6.356   21.02    18.697   0.961    -19.429   14.13   37.59 PASS
  24   6.356   25.01    18.892   1.161    -19.227   14.13   21.02 PASS
  28   6.664   14.13    16.733   2.725    -17.026   14.13   21.02 FAIL
  28   6.664   21.02    17.244   1.482    -17.724   30.42   32.94 PASS
  28   6.664   25.01    17.346   0.805    -17.314   21.02   32.94 PASS
  32   6.931   14.13    17.660   0.810    -16.873   14.13   21.02 PASS
  32   6.931   21.02    17.263   0.957    -18.166   14.13   25.01 PASS
  32   6.931   25.01    17.258   1.003    -17.118   14.13   21.02 PASS
```

Additional stress on the only asymptotic-looking failure

```text
lambda=28, gamma=14.13
```

with more rows and `sigma` variation did not cross `17`; best observed was
about `16.76`.

## Reading

The two-row mechanism is real: it forces the local divisor at the right
scale for almost every tested row from the active finite packet alone.

But active-packet forcing alone is not uniformly enough.  The missing
fraction of a power is exactly where the signed finite tail must be kept.

Thus the next theorem is not:

```text
Pair^M small and TailPair small separately.
```

It is:

```text
M_L(w;z_1,z_2)^(-1)
[
 Pair_{z_1}^M(w)+TailPair_{z_1}^M(w)
 Pair_{z_2}^M(w)+TailPair_{z_2}^M(w)
]
```

has `L^-17` size, with the sum treated as signed.
