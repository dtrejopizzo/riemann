# E77.5z - LogT External Coupling

## Statement

E77.5y proved the exact finite identity

```text
Q_N = Q_ext,N - Q_logT,N.
```

Since `Q_ext,N` is build-independent, this block tests the scalar coupling

```text
A_N(sigma) = Q_logT,N(sigma) / Q_ext,N(sigma)
```

and its signed defect

```text
1 - A_N = Q_N / Q_ext,N.
```

The hoped-for closure was:

```text
LOGT-EXT-COUPLING:
  A_N has stable zeta branch profiles and the planted build breaks them.
```

## Probe

File:

```text
E77_5z_logt_ext_coupling_probe.py
```

Run:

```text
python3 E77_5z_logt_ext_coupling_probe.py \
  --output E77_5z_logt_ext_coupling_results.json
```

Input:

```text
E77_5y_q_functional_identity_results.json
```

## Zeta Profiles

At `sigma=1.0`:

| mod4 | N | A=Q_logT/Q_ext | defect=Q/Q_ext | Q |
|---:|---:|---:|---:|---:|
| 0 | 8 | 0.89598166 | 0.10401834 | 0.29362369 |
| 0 | 12 | 0.87683420 | 0.12316580 | 0.41548471 |
| 0 | 16 | 0.89703585 | 0.10296415 | 0.38293070 |
| 2 | 10 | 1.01878430 | -0.01878430 | -0.05885830 |
| 2 | 14 | 1.07060336 | -0.07060336 | -0.25163492 |
| 2 | 18 | 0.71032569 | 0.28967431 | 1.11451443 |

At `sigma=3.0`:

| mod4 | N | A=Q_logT/Q_ext | defect=Q/Q_ext | Q |
|---:|---:|---:|---:|---:|
| 0 | 8 | 0.81308543 | 0.18691457 | 1.58287118 |
| 0 | 12 | 0.83614156 | 0.16385844 | 1.65826909 |
| 0 | 16 | 0.87299368 | 0.12700632 | 1.41703551 |
| 2 | 10 | 0.96165461 | 0.03834539 | 0.36045168 |
| 2 | 14 | 1.03887589 | -0.03887589 | -0.41566848 |
| 2 | 18 | 0.69178893 | 0.30821107 | 3.55750243 |

## Plant Falsifier

At `sigma=1.0`:

| mod4 | N | A=Q_logT/Q_ext | defect=Q/Q_ext | Q |
|---:|---:|---:|---:|---:|
| 0 | 8 | 37.03420011 | -36.03420011 | -101.71758758 |
| 0 | 12 | -0.78867804 | 1.78867804 | 6.03388603 |
| 0 | 16 | -0.34333024 | 1.34333024 | 4.99593691 |
| 2 | 10 | 2.82940220 | -1.82940220 | -5.73220614 |
| 2 | 14 | 2.14067952 | -1.14067952 | -4.06545500 |
| 2 | 18 | 1.21203694 | -0.21203694 | -0.81580668 |

At `sigma=3.0`:

| mod4 | N | A=Q_logT/Q_ext | defect=Q/Q_ext | Q |
|---:|---:|---:|---:|---:|
| 0 | 8 | 1.73435885 | -0.73435885 | -6.21885962 |
| 0 | 12 | -0.22215354 | 1.22215354 | 12.36835531 |
| 0 | 16 | -0.21399122 | 1.21399122 | 13.54474885 |
| 2 | 10 | 0.47844711 | 0.52155289 | 4.90266497 |
| 2 | 14 | 0.59939271 | 0.40060729 | 4.28337028 |
| 2 | 18 | 0.46824701 | 0.53175299 | 6.13771776 |

## Proof-Or-Falsifier

The scalar coupling is not enough to close.

The zeta `N=0 mod 4` branch is coherent: at `sigma=1`, `A` stays in

```text
0.87683420 .. 0.89703585,
```

and at `sigma=3`, it drifts smoothly from `0.81308543` to `0.87299368`.

But the live obstruction is the `N=2 mod 4` branch.  There the scalar ratio
does not stabilize in the tested window:

```text
sigma=3:
N=10  A=0.96165461
N=14  A=1.03887589
N=18  A=0.69178893.
```

This is exactly the spike-forming branch.  The plant falsifier breaks zeta
behavior, but that only proves the scalar coupling is discriminating; it does
not prove the needed zeta envelope.

## Status

```text
proved:
  the scalar ratio A_N exposes the zeta/plant distinction;
  zeta mod0 coupling is coherent in the tested window.

refuted:
  LOGT-EXT-COUPLING as a scalar branch-stability theorem at N<=20.

open:
  derive Q_logT,N from the finite Schur formula for logT itself.
```

Reduced target:

```text
SCHUR-LOGT-FUNCTIONAL:
  expand Q_logT,N using T=t0-corr, Tp=t0p-corrp, and the six-node Schur
  response; isolate the mod2 anchor-crossing term that produces the
  coupling defect.
```
