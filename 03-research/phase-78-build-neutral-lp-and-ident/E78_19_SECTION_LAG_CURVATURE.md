# E78.19 - LOGT-CANCEL as discrete curvature of the section-lag error

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.18 localized the live residual target to

```text
LOGT-CANCEL_N
 := |Q_ext,N - Q_logT,N| / (|Q_ext,N| + |Q_logT,N|),      (SC-1)
```

with the Schur-compression factor demoted to a side condition.

This note rewrites `(SC-1)` in the most intrinsic Phase-77 coordinates: the
signed section-lag error from E77.5l/E77.5y.

## 2. Exact curvature identity

From E77.5y,

```text
R_N = Delta external_N - Delta logT_N,                    (SC-2)
C_N = N R_N,                                              (SC-3)
Q_N = N^2(C_N - C_{N+2}).                                 (SC-4)
```

Combining `(SC-4)` with E77.5y's exact coupling identity

```text
Q_N = Q_ext,N - Q_logT,N,                                 (SC-5)
```

gives the exact reformulation

```text
Q_ext,N - Q_logT,N = N^2(C_N - C_{N+2}).                  (SC-6)
```

Therefore

```text
LOGT-CANCEL_N
 = N^2 |C_N - C_{N+2}| / (|Q_ext,N| + |Q_logT,N|).        (SC-7)
```

So the live two-term mismatch is exactly the **weighted discrete curvature** of
the section-lag residual sequence `C_N = N R_N`.

Equivalently, using `(SC-2)`-`(SC-3)`,

```text
Q_ext,N - Q_logT,N
 = N^2( N R_N - (N+2)R_{N+2} ).                           (SC-8)
```

This is the smallest exact finite reformulation of `LOGT-CANCEL` now available.

## 3. Consequence

E78.18 said that the live target is the signed coupling between `Q_ext` and
`Q_logT`.  After `(SC-7)`, that coupling becomes:

```text
SECTION-LAG-CURVATURE:
prove that the weighted curvature

  N^2 |C_N - C_{N+2}|

is small compared with the external/logT denominator

  |Q_ext,N| + |Q_logT,N|

on a cofinal zeta envelope.                               (SC-9)
```

Because `(SC-7)` is exact,

```text
SECTION-LAG-CURVATURE
=> LOGT-CANCEL-COFINAL
=> RELATIVE-COUPLING-DEFECT,                              (SC-10)
```

provided the E78.18 Schur-compression side condition stays uniformly away from
zero.

## 4. Probe audit

Companion:

```text
E78_19_section_lag_curvature_probe.py
E78_19_section_lag_curvature_results.json
```

The probe reconstructs `(SC-6)` directly from the certified E77.5y JSON. The
reconstruction error is at floating roundoff.

Representative zeta rows:

```text
sigma=1.0, N=10:
  C_N              = 0.0317978
  C_{N+2}          = 0.0323864
  |Delta_C|        = 5.886e-4
  N^2 |Delta_C|    = 5.886e-2
  LOGT-CANCEL      = 9.305e-3

sigma=3.0, N=14:
  C_N              = 0.0938985
  C_{N+2}          = 0.0960192
  |Delta_C|        = 2.121e-3
  N^2 |Delta_C|    = 4.157e-1
  LOGT-CANCEL      = 1.907e-2
```

Representative planted rows:

```text
sigma=1.0, N=8:
  C_N              = -1.50142
  C_{N+2}          = 0.0879155
  |Delta_C|        = 1.58934
  N^2 |Delta_C|    = 1.01718e2
  LOGT-CANCEL      = 9.474e-1

sigma=3.0, N=18:
  C_N              = 0.366176
  C_{N+2}          = 0.347232
  |Delta_C|        = 1.894e-2
  N^2 |Delta_C|    = 6.138
  LOGT-CANCEL      = 3.622e-1
```

## 5. Candid reading

This is a useful reduction, but it does **not** close the front by itself.

What it proves:

```text
the numerator of LOGT-CANCEL is exactly a discrete curvature of the
section-lag residual sequence C_N.
```

What it does **not** prove:

```text
that small |Delta_C| alone controls LOGT-CANCEL uniformly.
```

The denominator still matters, and the raw size of `|Delta_C|` is only part of
the geometry.  So this note is a legitimate reduction, not a fake closure.

Still, it improves the front in one important way:

```text
the live arithmetic object is now a signed/weighted regularity statement about
the residual sequence C_N itself, not an opaque comparison between two
independent functionals.
```

## 6. Status

```text
proved:
  LOGT-CANCEL is exactly the normalized discrete curvature of C_N = N R_N;

proved:
  Q_ext,N - Q_logT,N = N^2(C_N - C_{N+2}) with roundoff-certified
  reconstruction;

reduced:
  LOGT-CANCEL-COFINAL to SECTION-LAG-CURVATURE plus the E78.18 compression
  side condition;

clarified:
  the remaining theorem-grade arithmetic work is a signed regularity/cofinal
  statement for the section-lag residual sequence, not an unexplained
  comparison of unrelated observables;

warning:
  raw curvature size alone is not yet the whole mechanism; the denominator
  normalization remains part of the target.
```
