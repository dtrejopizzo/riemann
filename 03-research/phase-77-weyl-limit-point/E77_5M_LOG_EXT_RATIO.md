# E77.5m - LOG-EXT-RATIO Residual Scaling

## Objective

E77.5l reduced the invariant section-lag identity to the signed residual:

```text
R_N(sigma)=Delta external_N(sigma)-Delta logT_N(sigma).
```

E77.5m asks whether the measured residual is already compatible with a
summable envelope, or whether another leading term must be removed.

## Probe

Artifacts:

```text
E77_5m_log_ext_ratio_probe.py
E77_5m_log_ext_ratio_results.json
```

Command:

```bash
python3 E77_5m_log_ext_ratio_probe.py
```

The probe reads the certified E77.5l result and computes:

```text
R_N,
R_N / Delta external_N,
N R_N,
N^2 R_N,
local power slopes.
```

## Certification Table

Max-residual rows from E77.5l.

| build | N -> N+2 | R | R/external | N R | N^2 R | local slope |
|---|---:|---:|---:|---:|---:|---:|
| zeta | 8 -> 10 | 0.016718890 | 0.17025008 | 0.13375112 | 1.0700090 | - |
| zeta | 10 -> 12 | 0.010901876 | 0.16687484 | 0.10901876 | 1.0901876 | -1.916 |
| zeta | 12 -> 14 | 0.0087845201 | 0.18847691 | 0.10541424 | 1.2649709 | -1.184 |
| zeta | 14 -> 16 | 0.0067070345 | 0.19201494 | 0.093898483 | 1.3145788 | -1.750 |
| zeta | 16 -> 18 | 0.0060012026 | 0.22100593 | 0.096019241 | 1.5363079 | -0.833 |
| zeta | 18 -> 20 | 0.0050268859 | 0.23148677 | 0.090483946 | 1.6287110 | -1.504 |
| zeta | 20 -> 22 | 0.0039752000 | 0.22379295 | 0.079504000 | 1.5900800 | -2.228 |
| planted | 8 -> 10 | 0.77260549 | 7.8675167 | 6.1808439 | 49.446752 | - |
| planted | 10 -> 12 | 0.057585672 | 0.88146298 | 0.57585672 | 5.7585672 | -11.64 |
| planted | 12 -> 14 | 0.043902506 | 0.94195342 | 0.52683007 | 6.3219608 | -1.488 |
| planted | 14 -> 16 | 0.031495622 | 0.90168464 | 0.44093871 | 6.1731420 | -2.155 |
| planted | 16 -> 18 | 0.026192799 | 0.96460065 | 0.41908478 | 6.7053565 | -1.381 |
| planted | 18 -> 20 | 0.020343089 | 0.93679390 | 0.36617561 | 6.5911609 | -2.146 |
| planted | 20 -> 22 | 0.017361602 | 0.97741094 | 0.34723203 | 6.9446406 | -1.504 |

## Autopsy

The residual is not yet theorem-grade summable.

For zeta, `N R_N` is the flatter diagnostic:

```text
0.134, 0.109, 0.105, 0.0939, 0.0960, 0.0905, 0.0795.
```

This suggests a leading `1/N` term remains.  A `1/N` envelope is not
summable, so `LOG-EXT-RATIO` cannot close `DELTA-ENVELOPE` without removing
that leading coefficient.

For the planted falsifier, after the first overshoot, `N^2 R_N` is roughly
flat around `6--7`, and `R_N/external_N` remains close to `1`.  The planted
build therefore fails the zeta coupling in a different way: its log-transfer
update cancels little of the external tail.

## Reduced Target

`LOG-EXT-RATIO` is reduced to:

```text
LEAD-1/N-CANCEL:
  identify the leading 1/N coefficient in

    R_N = Delta external_N - Delta logT_N

  and prove its signed cancellation in the next cell-normalized residual.
```

The next object must subtract or symbolically cancel this leading term
before attempting a summable envelope.

## Status

```text
proved:    no summable delta envelope yet;
refuted:   raw LOG-EXT-RATIO residual as already summable;
observed:  zeta residual behaves like a remaining 1/N term in this window;
observed:  planted leaves most of the external tail uncancelled;
reduced:   LOG-EXT-RATIO -> LEAD-1/N-CANCEL;
next:      E77.5n should isolate the coefficient of N R_N by sigma and
           derive it from the moving-boundary cell expansion.
```
