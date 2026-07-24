# E77.5ae - Sector Certificate

## Statement

E77.5ad found the sector law for

```text
u = -theta'/(1-theta).
```

To avoid absolute-value algebra, this block replaces

```text
Im(u) > |Re(u)|
```

by the cone-equivalent signed pair

```text
Im(u) > 0,
Im(u)^2 - Re(u)^2 > 0.
```

The second expression is a rational finite Schur/cell quantity once `u` is
written from `theta` and `theta'`.

## Probe

File:

```text
E77_5ae_sector_certificate_probe.py
```

Run:

```text
python3 E77_5ae_sector_certificate_probe.py \
  --output E77_5ae_sector_certificate_results.json
```

Inputs:

```text
E77_5ac_theta_logderiv_coupling_zeta.json
E77_5ac_theta_logderiv_coupling_plant.json
```

## Zeta Certificate

| sigma | mod4 | Im(u)>0 | cone>0 | min cone | min normalized cone | N^2 cone first -> last |
|---:|---:|---|---|---:|---:|---:|
| 1.0 | 0 | true | true | 1.38076262e-05 | 0.881683384 | 0.0498009 -> 0.00552305 |
| 1.0 | 2 | true | true | 1.94383691e-05 | 0.750616233 | 0.0283363 -> 0.00629803 |
| 3.0 | 0 | true | true | 0.000129632786 | 0.986013700 | 0.409492 -> 0.0518531 |
| 3.0 | 2 | true | true | 0.000196902755 | 0.968454131 | 0.250276 -> 0.0637965 |

The weakest normalized zeta margin in this window is

```text
sigma=1.0, mod2: 0.750616233.
```

## Plant Falsifier

| sigma | mod4 | Im(u)>0 | cone>0 | min cone | min normalized cone | N^2 cone first -> last |
|---:|---:|---|---|---:|---:|---:|
| 1.0 | 0 | false | false | -0.0247599938 | -0.999998341 | -1.58464 -> -0.0222290 |
| 1.0 | 2 | false | false | -0.0118647613 | -0.999914154 | -1.18648 -> -0.0227079 |
| 3.0 | 0 | false | false | -0.00253432482 | -0.999668803 | -0.162197 -> -0.0237118 |
| 3.0 | 2 | true | false | -0.00309417181 | -0.999223321 | -0.309417 -> -0.0267318 |

The planted build can have `Im(u)>0` in one profile, but it still fails the
cone inequality.  This shows why the cone pair is the correct certificate,
not just the sign of the imaginary part.

## Scaling Autopsy

The raw cone numerator is positive for zeta but decays quickly.  At
`sigma=3.0, mod2`:

```text
N=10 cone=0.002502759
N=14 cone=0.000601375
N=18 cone=0.000196903
```

with local slopes about `-4.24` and `-4.44`.  So a raw lower bound on
`Im(u)^2-Re(u)^2` is not the right theorem.

The normalized cone

```text
(Im(u)^2-Re(u)^2)/|u|^2
```

is the stable object: zeta remains strongly positive, while planted is close
to `-1`.

## Status

```text
proved numerically:
  zeta satisfies Im(u)>0 and Im(u)^2-Re(u)^2>0 on the tested rows;
  planted fails the cone condition on the tested rows;
  the normalized cone is the robust sector object.

refuted:
  raw cone numerator as a uniform lower-bound certificate.

open:
  theorem-grade proof of a positive normalized cone margin.
```

Reduced target:

```text
NORMALIZED-SECTOR-MARGIN:
  prove a positive lower bound for
  (Im(u)^2-Re(u)^2)/|u|^2
  from finite Schur/cell algebra on the zeta cofinal path; planted/off-line
  builds must remain negative or fail the bound.
```
