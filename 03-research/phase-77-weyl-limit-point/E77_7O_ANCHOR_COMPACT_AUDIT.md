# E77.7o - Anchor compact audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7n reduced the LP pencil bridge to

```text
PROJECTIVE-MU-TRANSFER,
```

but left one explicit open condition:

```text
control the anchor T_N(z_0;mu) away from zero.
```

This note audits the finite safe-compact behavior of the anchor and locates
the next real gap.

## 2. Probe

Companion:

```text
E77_7o_anchor_compact_probe.py
E77_7o_anchor_compact_results.json
```

Command:

```bash
python3 E77_7o_anchor_compact_probe.py \
  --lambda 6 --max-modes 18 --dps 60
```

The probe samples the safe compact

```text
sigma in [0.6, 3.0]
```

on a 13-point grid.  For each section and for both the moving finite point
`mu_N` and the largest-section frozen reference `mu_ref`, it records

```text
min_{sigma in grid} |T_N(i sigma;mu)|.
```

The frozen point is only a finite surrogate, not the abstract `mu_L`.

## 3. Result

### Zeta

For every sampled section `N=6..18`, both moving and frozen anchors stay far
from zero on the whole tested compact.  In fact the minimum occurs at the
right edge `sigma=3.0` and grows very rapidly:

```text
N=6:  min |a_m| = 5.50e1,   min |a_f| = 5.46e1
N=12: min |a_m| = 5.11e8,   min |a_f| = 5.08e8
N=18: min |a_m| = 1.07e12,  min |a_f| = 1.07e12.
```

So there is no evidence of anchor collapse in the zeta build on the tested
safe compact.

### Planted build

The planted build also stays away from zero on the whole grid.  Its minima
are much smaller and irregular, but still strictly positive:

```text
N=6:  min |a_m| = 2.62e-1,  min |a_f| = 1.00e-1
N=12: min |a_m| = 2.58e0,   min |a_f| = 5.63e-1
N=17: min |a_m| = 1.99e1,   min |a_f| = 5.52e-1
N=18: min |a_m| = 2.63e0,   min |a_f| = 2.63e0.
```

Again, every sampled minimum occurs at `sigma=3.0`.

## 4. Reading

The finite audit supports:

```text
1. anchor nonvanishing is compatible with both builds;
2. anchor collapse is not what causes the raw moving/frozen instability of
   E77.7b;
3. the projective bridge remains falsifier-neutral at this level.
```

Combined with E77.7n, this means:

```text
raw transfer instability
  = mostly normalization drift,
not anchor zero-crossing.
```

So the genuine open problem in `PROJECTIVE-MU-TRANSFER` is the directional
paired `mu`-shift and the singular-section regularization, not loss of the
projective denominator on ordinary safe compacts.

## 5. What this does not prove

This is only a finite-grid audit.  It does **not** prove:

```text
1. a uniform positive lower bound for all large N and all sigma in compact K;
2. nonvanishing at the true infinite-volume point mu_L;
3. regularized nonvanishing across sections where A_N(mu_L) is singular.
```

So the theorem target remains open.

## 6. Reduced target

The anchor obligation can now be sharpened to:

```text
ANCHOR-COMPACT-NONVANISH:
for each safe compact K, the intrinsic mu_L anchor T_N(z_0;mu_L) does not
approach zero after the same projective regularization used for singular
sections.
```

This is smaller than "full projective transfer" and more accurate than a
raw moving/frozen comparison.

## 7. Status

```text
observed:  on the tested safe compact [0.6,3.0], both zeta and planted
           anchors stay away from zero for N=6..18;
observed:  every sampled minimum occurs at the right edge sigma=3.0;
refuted:   anchor zero-crossing as the source of the raw E77.7b resonance;
open:      ANCHOR-COMPACT-NONVANISH at the true mu_L with singular-section
           regularization;
next:      isolate the regularized projective transfer across singular
           sections.
```
