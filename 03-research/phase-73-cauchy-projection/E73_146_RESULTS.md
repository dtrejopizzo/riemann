# E73.146 Results - Signed Tail Forcing Probe

Date: 2026-07-12.

Script:

```text
E73_146_signed_tail_forcing_probe.py
```

Purpose:

Compute the active packet, inactive tail, and signed sum after applying the
two-row divisor inverse:

```text
M_L(w)^(-1) active,
M_L(w)^(-1) tail,
M_L(w)^(-1) (active+tail).
```

The tail is computed directly as the inactive row

```text
p_infty - p_active,
```

not by substituting the divisor identity for `H_0`.

Output:

```text
 lam     L gamma   activeM    tailM  signedM      z1      z2 status
  16   5.545   14.13    19.713   19.522   19.744   14.13   21.02 PASS
  16   5.545   21.02    18.134   18.186   19.081   30.42   37.59 PASS
  16   5.545   25.01    13.839   13.691   13.443   21.02   25.01 FAIL
  20   5.991   14.13    18.679   18.547   18.412   14.13   37.59 PASS
  20   5.991   21.02    18.208   18.485   18.432   25.01   37.59 PASS
  20   5.991   25.01    18.986   18.045   18.065   32.94   37.59 PASS
  24   6.356   14.13    17.141   17.161   17.916   25.01   37.59 PASS
  24   6.356   21.02    17.919   17.976   18.070   25.01   32.94 PASS
  24   6.356   25.01    18.414   18.386   19.301   30.42   32.94 PASS
  28   6.664   14.13    16.715   16.515   16.308   14.13   30.42 FAIL
  28   6.664   21.02    16.693   16.619   17.121   14.13   32.94 PASS
  28   6.664   25.01    17.143   17.053   17.290   14.13   25.01 PASS
  32   6.931   14.13    17.480   17.256   17.267   21.02   30.42 PASS
  32   6.931   21.02    17.052   16.882   17.462   14.13   32.94 PASS
  32   6.931   25.01    16.071   16.084   17.510   32.94   37.59 PASS
```

## Reading

The signed tail mechanism is real but not monotone.  It improves several
rows, especially where active and inactive contributions have comparable
size.

It does not uniformly dominate the active packet in this small range:

```text
lambda=28, gamma=14.13
```

still falls below margin `17`.

The extended stress at `lambda=36,40` is not decisive because the raw
`ROW-KER_17` margin itself fails for some rows in that uncalibrated
`n_modes` schedule.  Those runs are diagnostic only; they are not part of
the current manifest.

## Consequence

`SIGNED-TAIL-LDIV_17` is still the right local theorem, but the proof needs
one more ingredient:

```text
ROW-SCALE:
choose the finite mode schedule / standard boxes so that the underlying
ROW-KER target is stable before applying two-row forcing.
```

Within the current calibrated range, two-row signed forcing explains most
of the observed local divisor smallness and isolates the remaining finite
transition rows.
