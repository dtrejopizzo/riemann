# E77.5p - Second Coefficient Audit

## Objective

E77.5o reduced the live object to:

```text
SECOND-COEFF-CANCEL:
  identify the next coefficient in
  D_N(sigma)=C_N(sigma)-C_{N+2}(sigma).
```

E77.5p measures:

```text
Q_N(sigma)=N^2 D_N(sigma).
```

If `Q_N` stabilized, the next step would be to derive that coefficient from
the moving-boundary/four-node cell expansion.

## Probe

Artifacts:

```text
E77_5p_second_coeff_probe.py
E77_5p_second_coeff_results.json
```

Command:

```bash
python3 E77_5p_second_coeff_probe.py
```

The probe reads `E77_5o_profile_drift_results.json`.

## Results

Selected `Q_N` sequences:

```text
zeta sigma=1.0:
N=8  0.2936
N=10 -0.0589
N=12 0.4155
N=14 -0.2516
N=16 0.3829
N=18 1.1145

zeta sigma=3.0:
N=8  1.5829
N=10 0.3605
N=12 1.6583
N=14 -0.4157
N=16 1.4170
N=18 3.5575
```

For the planted falsifier:

```text
plant sigma=1.0:
N=8  -101.7176
N=10 -5.7322
N=12  6.0339
N=14 -4.0655
N=16  4.9959
N=18 -0.8158

plant sigma=3.0:
N=8  -6.2189
N=10  4.9027
N=12 12.3684
N=14  4.2834
N=16 13.5447
N=18  6.1377
```

The full sigma-profile table is in
`E77_5p_second_coeff_results.json`.

## Autopsy

The fixed second coefficient does not stabilize at `N<=22`.  The zeta
sequence alternates strongly across consecutive even steps, and the planted
sequence has larger transients plus sign changes.  Treating `Q_N` as a
single coefficient would repeat the finite-window extrapolation error
already blocked in E77.5n.

The visible pattern is not random noise: steps separated by 4 often look
more comparable than adjacent even steps.  The correct next reduction is to
separate the two even subsequences:

```text
N = 0 mod 4,
N = 2 mod 4.
```

## Reduced Target

`SECOND-COEFF-CANCEL` is reduced to:

```text
MOD4-DRIFT-SPLIT:
  split the coefficient/drift hierarchy by N mod 4 and test whether each
  subsequence has a stable signed profile.
```

If the split stabilizes, derive the two profiles from the mesh parity in
the moving-boundary cell expansion.  If it does not, the next object must
be a higher-period or physical-boundary scaling.

## Status

```text
proved:    no second-coefficient closure yet;
refuted:   single Q_N(sigma) coefficient at N<=22;
observed:  zeta Q_N has a strong adjacent-even oscillation;
observed:  planted has larger transient/sign-changing anatomy;
reduced:   SECOND-COEFF-CANCEL -> MOD4-DRIFT-SPLIT;
next:      E77.5q should split C_N, D_N, and Q_N by N mod 4.
```
