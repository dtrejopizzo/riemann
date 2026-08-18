# E77.5q - Mod-4 Drift Split

## Objective

E77.5p refuted a single second coefficient:

```text
Q_N(sigma)=N^2(C_N(sigma)-C_{N+2}(sigma)).
```

The visible obstruction was adjacent-even oscillation.  E77.5q splits the
coefficient hierarchy by:

```text
N = 0 mod 4,
N = 2 mod 4.
```

## Probe

Artifacts:

```text
E77_5q_mod4_drift_split_probe.py
E77_5q_mod4_drift_split_results.json
```

Command:

```bash
python3 E77_5q_mod4_drift_split_probe.py
```

The probe reads the certified E77.5n and E77.5p artifacts.

## Results

Selected zeta profiles:

```text
sigma=1.0
mod 0 C: (8,0.036386), (12,0.032386), (16,0.030785), (20,0.025849)
mod 0 Q: (8,0.293624), (12,0.415485), (16,0.382931), Q-range=0.121861
mod 2 C: (10,0.031798), (14,0.029501), (18,0.029289)
mod 2 Q: (10,-0.058858), (14,-0.251635), (18,1.114514), Q-range=1.366149

sigma=3.0
mod 0 C: (8,0.133751), (12,0.105414), (16,0.096019), (20,0.079504)
mod 0 Q: (8,1.582871), (12,1.658269), (16,1.417036), Q-range=0.241234
mod 2 C: (10,0.109019), (14,0.093898), (18,0.090484)
mod 2 Q: (10,0.360452), (14,-0.415668), (18,3.557502), Q-range=3.973171
```

Selected planted profiles:

```text
sigma=1.0
mod 0 Q-range=107.751474
mod 2 Q-range=4.916399

sigma=3.0
mod 0 Q-range=19.763608
mod 2 Q-range=1.854347
```

## Reading

The mod-4 split is a real reduction.  For zeta, the `N=0 mod 4` subsequence
has a much more stable second coefficient:

```text
Q-range at sigma=1.0: 0.1219
Q-range at sigma=3.0: 0.2412.
```

The `N=2 mod 4` subsequence remains unstable, with a late spike:

```text
sigma=3.0: Q = 0.3605, -0.4157, 3.5575.
```

The planted falsifier does not reproduce a uniformly stable zeta-like
profile.  Its ranges remain large or anatomy-dependent across sigma and
mod classes.

## Reduced Target

`MOD4-DRIFT-SPLIT` is reduced to:

```text
MOD2-SPIKE-CELL:
  explain the N=2 mod 4 spike in Q_N(sigma) from the moving-boundary mesh
  cell, or find the corrected physical scaling that removes it.
```

The `N=0 mod 4` branch is now a candidate stable coefficient branch.  The
next proof must not average the two branches together.

## Status

```text
proved:    no delta-envelope theorem yet;
observed:  mod-4 splitting sharply improves zeta's N=0 mod 4 branch;
observed:  zeta N=2 mod 4 still has an unresolved late spike;
observed:  planted fails to match a uniform stable branch anatomy;
reduced:   MOD4-DRIFT-SPLIT -> MOD2-SPIKE-CELL;
next:      E77.5r should isolate the N=2 mod 4 spike and test physical
           boundary scaling d_N=2*pi*N/L.
```
