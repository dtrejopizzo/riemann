# E77.5n - Leading 1/N Coefficient Audit

## Objective

E77.5m reduced the live residual to:

```text
LEAD-1/N-CANCEL:
  identify the leading coefficient in
  R_N(sigma)=Delta external_N(sigma)-Delta logT_N(sigma).
```

E77.5n measures the coefficient profile

```text
C_N(sigma)=N R_N(sigma)
```

by sigma, rather than only at the maximum row.

## Probe

Artifacts:

```text
E77_5n_lead_1_over_n_cancel_probe.py
E77_5n_lead_1_over_n_cancel_results.json
```

Command:

```bash
python3 E77_5n_lead_1_over_n_cancel_probe.py
```

The probe reads the certified E77.5l artifact and records signed
coefficients, coefficient drift, and transverse sigma profile.

## Sigma Profiles

Rows show `C_N(sigma)` at the first and last tested section step
(`N=8` and `N=20`), plus the range over all tested N.

| build | sigma | C_8(sigma) | C_20(sigma) | range | last Delta C |
|---|---:|---:|---:|---:|---:|
| zeta | 0.55 | 0.0196040 | 0.0141856 | 0.0054184 | -0.0018812 |
| zeta | 0.60 | 0.0214230 | 0.0154780 | 0.0059450 | -0.0020532 |
| zeta | 0.75 | 0.0269406 | 0.0193600 | 0.0075806 | -0.0025708 |
| zeta | 1.00 | 0.0363857 | 0.0258492 | 0.0105364 | -0.0034399 |
| zeta | 1.50 | 0.0565563 | 0.0389275 | 0.0176288 | -0.0052119 |
| zeta | 2.00 | 0.0790525 | 0.0521894 | 0.0268630 | -0.0070460 |
| zeta | 3.00 | 0.1337511 | 0.0795040 | 0.0542471 | -0.0109799 |
| planted | 0.55 | -6.1808439 | 0.0528020 | 6.2380111 | 0.0077820 |
| planted | 0.60 | -5.4268589 | 0.0586125 | 5.4926633 | 0.0074142 |
| planted | 0.75 | -3.4936572 | 0.0765357 | 3.5885354 | 0.0058158 |
| planted | 1.00 | -1.5014218 | 0.1070803 | 1.6466594 | 0.0025179 |
| planted | 1.50 | -0.1198593 | 0.1679127 | 0.3799978 | -0.0036784 |
| planted | 2.00 | 0.2136574 | 0.2279640 | 0.1597952 | -0.0090353 |
| planted | 3.00 | 0.4786870 | 0.3472320 | 0.2286247 | -0.0189436 |

## Transverse Profile

For zeta, the coefficient is positive across the safe sigma window and
keeps a smooth transverse shape.  The max/min ratio by section is:

```text
6.82, 6.31, 5.96, 5.82, 5.69, 5.63, 5.60.
```

For planted, the profile changes sign at small sigma and has a large
transient:

```text
C_8(0.55)=-6.18, C_8(3.0)=0.479.
```

The later planted profile becomes positive, but it does not represent a
zeta-like cancellation: E77.5m showed `R_N/external_N -> 0.98`, so the
external tail is mostly uncancelled.

## Autopsy

The leading coefficient is not stable enough to close.

For zeta, `C_N(sigma)` is coherent and decreasing in the tested window, but
the drift is still visible at every sigma.  At `sigma=3`, for example:

```text
C_8=0.13375, C_20=0.07950.
```

Thus we cannot replace `R_N` by a fixed `C(sigma)/N` coefficient and call
the remainder summable.  That would be another finite-window extrapolation.

## Reduced Target

`LEAD-1/N-CANCEL` is reduced to:

```text
PROFILE-DRIFT-CANCEL:
  identify the finite cell source of the drift

    C_N(sigma)-C_{N+2}(sigma)

  and prove that after subtracting the moving profile, the residual has a
  summable envelope.
```

The next proof target is not a constant coefficient; it is the signed
evolution of the coefficient profile.

## Status

```text
proved:    no delta-envelope theorem yet;
refuted:   fixed leading coefficient closure at N<=22;
observed:  zeta C_N(sigma) is positive, smooth, and drifting downward;
observed:  planted has sign-changing/transient coefficient anatomy and
           fails the log/external coupling;
reduced:   LEAD-1/N-CANCEL -> PROFILE-DRIFT-CANCEL;
next:      E77.5o should derive Delta C_N(sigma) from the same
           moving-boundary cell update and test whether it is summable.
```
