# E77.5v - Missing Weighted Observable

## Objective

E77.5u showed that weighted `odd/inserted` models the stable zeta
`N=0 mod 4` branch but not the `N=2 mod 4` spike.  E77.5v tests the
remaining scalar weighted ratios from E77.5t:

```text
old-boundary-pair / inserted,
outer-pair / inserted,
old-shell-pair / inserted,
odd / inserted.
```

## Probe

Artifacts:

```text
E77_5v_missing_weight_probe.py
E77_5v_missing_weight_results.json
```

Command:

```bash
python3 E77_5v_missing_weight_probe.py
```

The probe computes finite correlations of each scalar ratio with `Q_N`,
split by build, sigma, and mod class.

## Results

Selected zeta correlations:

```text
sigma=1.0, mod0:
odd 0.751, old-boundary 0.763, outer 0.763, old-shell 0.732

sigma=1.0, mod2:
odd 0.753, old-boundary 0.746, outer 0.746, old-shell 0.762

sigma=3.0, mod0:
odd -0.626, old-boundary -0.611, outer -0.611, old-shell -0.642

sigma=3.0, mod2:
odd 0.717, old-boundary 0.709, outer 0.709, old-shell 0.725
```

Planted correlations are erratic and often artificially ±1 because the
reduced planted window has only two points in a mod class.

## Autopsy

No scalar weighted ratio isolates the mod2 spike.  The candidate ratios are
too correlated with each other on the zeta window, and the sign of the
correlation changes with sigma.  A scalar-ratio closure would be another
coordinate projection, not a theorem-grade cell law.

The next object must keep the complex active contribution vector:

```text
(tau_j(S^{-1}k)_j)_{j in active block}
```

with its phases and signed sums, instead of reducing it to absolute ratios.

## Reduced Target

`MOD2-MISSING-WEIGHT` is reduced to:

```text
COMPLEX-ACTIVE-VECTOR-LAW:
  prove the mod0/mod2 branch behavior from the complex weighted active
  vector in the common-core block.
```

The next probe should fit or compare the complex vector shape itself
against `Q_N`, including phase alignment between left and right inserted
nodes.

## Status

```text
proved:    no delta-envelope theorem yet;
refuted:   scalar weighted ratios as the missing mod2 observable;
observed:  zeta scalar correlations are not stable across sigma;
observed:  planted scalar ratios are not a valid shared law;
reduced:   MOD2-MISSING-WEIGHT -> COMPLEX-ACTIVE-VECTOR-LAW;
next:      E77.5w should retain the full complex active vector and compare
           phase-aligned branch shapes.
```
