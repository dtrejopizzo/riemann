# E77.5y - Q Functional Identity

## Statement

E77.5x showed that the `Q_N` spike is not carried by the geometry of the
phase-aligned active vector alone.  E77.5y derives the exact finite scalar
functional instead.

For the signed E77.5l residual

```text
R_N(sigma) = Delta external_N(sigma) - Delta logT_N(sigma),
```

define

```text
C_N(sigma) = N R_N(sigma),
Q_N(sigma) = N^2(C_N(sigma)-C_{N+2}(sigma)).
```

Then the exact component identity is

```text
Q_N = Q_ext,N - Q_logT,N
```

where

```text
Q_ext,N  = N^2(N Delta external_N - (N+2) Delta external_{N+2}),
Q_logT,N = N^2(N Delta logT_N    - (N+2) Delta logT_{N+2}).
```

This is a finite identity between the `E77.5q` drift definition of `Q_N` and
the `E77.5l` log-transfer residual formula.  It uses signed deltas; no
pseudoinverse, no positivity reduction, and no absolute pre-cancellation
estimate enters.

## Probe

File:

```text
E77_5y_q_functional_identity_probe.py
```

Run:

```text
python3 E77_5y_q_functional_identity_probe.py \
  --output E77_5y_q_functional_identity_results.json
```

Inputs:

```text
E77_5l_logt_cell_update_results.json
E77_5q_mod4_drift_split_results.json
```

## Certification

The identity reconstructs `Q_N` to floating roundoff.

| build | sigma | max relative identity error |
|---|---:|---:|
| zeta | 1.0 | 3.553e-15 |
| zeta | 3.0 | 5.014e-15 |
| plant | 1.0 | 2.442e-15 |
| plant | 3.0 | 2.894e-15 |

## Component Anatomy

At `sigma=3.0`:

| build | N | mod4 | Q | Q_ext | Q_logT | cancellation index |
|---|---:|---:|---:|---:|---:|---:|
| zeta | 8 | 0 | 1.582871 | 8.46842 | 6.88555 | 9.700 |
| zeta | 10 | 2 | 0.360452 | 9.40013 | 9.03968 | 51.16 |
| zeta | 14 | 2 | -0.415668 | 10.6922 | 11.1079 | 52.45 |
| zeta | 16 | 0 | 1.417036 | 11.1572 | 9.74017 | 14.75 |
| zeta | 18 | 2 | 3.557502 | 11.5424 | 7.98492 | 5.489 |
| plant | 8 | 0 | -6.218860 | 8.46842 | 14.6873 | 3.723 |
| plant | 10 | 2 | 4.902665 | 9.40013 | 4.49747 | 2.835 |
| plant | 14 | 2 | 4.283370 | 10.6922 | 6.40882 | 3.992 |
| plant | 16 | 0 | 13.544749 | 11.1572 | -2.38754 | 1.000 |
| plant | 18 | 2 | 6.13772 | 11.5424 | 5.40470 | 2.761 |

At `sigma=1.0`:

| build | N | mod4 | Q | Q_ext | Q_logT | cancellation index |
|---|---:|---:|---:|---:|---:|---:|
| zeta | 8 | 0 | 0.293624 | 2.82281 | 2.52918 | 18.23 |
| zeta | 10 | 2 | -0.058858 | 3.13338 | 3.19223 | 107.47 |
| zeta | 14 | 2 | -0.251635 | 3.56406 | 3.81570 | 29.33 |
| zeta | 16 | 0 | 0.382931 | 3.71907 | 3.33614 | 18.42 |
| zeta | 18 | 2 | 1.114514 | 3.84747 | 2.73296 | 5.904 |
| plant | 8 | 0 | -101.717588 | 2.82281 | 104.54039 | 1.056 |
| plant | 10 | 2 | -5.732206 | 3.13338 | 8.86558 | 2.093 |
| plant | 14 | 2 | -4.065455 | 3.56406 | 7.62952 | 2.753 |
| plant | 16 | 0 | 4.995937 | 3.71907 | -1.27687 | 1.000 |
| plant | 18 | 2 | -0.815807 | 3.84747 | 4.66328 | 10.43 |

## Proof-Or-Falsifier

The identity is proved numerically to roundoff because it reconstructs the
independently recorded `E77.5q` values from the signed `E77.5l` deltas.

The important autopsy is structural:

```text
Q_ext is build-independent.
```

It is exactly the same for zeta and the planted falsifier.  Therefore no
closure can come from the external component alone.  The discriminant must be
the signed coupling

```text
Q_logT,N ~= Q_ext,N
```

with the correct residual profile.  In zeta this coupling is extremely
delicate: at `sigma=1`, `N=10`, the cancellation index is `107.47`; at
`sigma=3`, `N=14`, it is `52.45`.  The planted build does not preserve this
coupling: its `Q_logT` component can overshoot, undershoot, or change sign.

Thus E77.5y closes the bookkeeping identity but does not close Omega7.  It
strictly reduces the live object from an unexplained `Q_N` spike to a finite
signed coupling theorem for the log-transfer functional.

## Status

```text
proved:
  Q_N = Q_ext,N - Q_logT,N as an exact finite identity;
  the E77.5q drift definition and E77.5l residual definition agree to
  roundoff;
  Q_ext is build-independent and cannot be the discriminator.

refuted:
  any route that tries to close the spike from external-tail arithmetic alone.

open:
  prove the zeta-only signed coupling of Q_logT to Q_ext using the finite
  Schur/cell functional.
```

Reduced target:

```text
LOGT-EXT-COUPLING:
  prove that the finite Schur log-transfer functional tracks the
  build-independent external second profile with a signed summable residual;
  planted/off-line builds must break this coupling.
```
