# E73.118 Results - Low-Scale Exact LOCK Base Probe

Date: 2026-07-12.

Script:

```text
E73_118_low_lock_base_probe.py
```

Purpose:

Resolve the remaining `lambda=16` failure from E73.117.  The wide-box
certificate failed only in `LOCK`, with exponent about

```text
LOCK ~= L^-4.53,
```

because E73.117 still used the crude sufficient factor

```text
4(1+exp(alpha L))/alpha.
```

E73.118 replaces this low-scale factor by the exact local `HWIN`
expression on the interval-order compatible FAR triples.  The local
`tau` window is exact by nearest-zero cell enumeration.  The `alpha`
dependence is gridded, so this is still a base-case probe rather than a
full interval-alpha certificate.

Output:

```text
E73.118 low-scale exact LOCK base probe
Uses exact HWIN on compatible FAR triples; alpha is gridded, tau windows exact.
This is a base-case probe, not yet an interval alpha certificate.
 lam     L box                         lockExactB mainBox nTri status
  16   5.545 [0.15,0.25]x[13.63,14.63]     -9.921 2.049e-01    1 PASS
  16   5.545 [0.15,0.25]x[20.52,21.52]    -10.001 2.058e-01    1 PASS
```

Conclusion:

The `lambda=16` obstruction is not structural.  It is an artifact of the
global `LOCK` constant used in E73.117.  With the exact local `HWIN`
expression, the base case has large slack:

```text
LOCK exact <= L^-9.921
```

on the first wide box and

```text
LOCK exact <= L^-10.001
```

on the second.

The remaining work for a closed finite base certificate is now small and
explicit:

```text
replace the gridded alpha maximum by an interval alpha enclosure for
HWIN(alpha+i gamma, local_window).
```

After that replacement, the finite low-scale base `lambda=16` joins the
E73.117 box route:

```text
lambda=16: exact LOCK base certificate;
lambda=20: finite subdivided box cover;
lambda>=24: wide-box GATE-73 certificate in tested range.
```

