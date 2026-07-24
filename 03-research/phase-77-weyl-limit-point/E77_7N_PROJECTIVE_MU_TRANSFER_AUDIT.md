# E77.7n - Projective mu-transfer audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7m reduced the Phase 76 / Phase 77 pencil mismatch to the directional
transfer problem

```text
PENCIL-TRANSFER-COMPATIBILITY.
```

The key question is whether one must compare the raw finite transfers

```text
T_N(z;mu_L) and T_N(z;0),
```

or the projectively normalized family

```text
T_N(z;mu) / T_N(z_0;mu),
```

which is the actual coordinate entering `theta_N`.

This note audits that distinction numerically and records the correct target.

## 2. Exact projective identity

For any `mu,nu` with invertible inner blocks,

```text
T_N(z;mu)-T_N(z;nu)
 = (mu-nu) r_z A_N(mu)^(-1) A_N(nu)^(-1) b_N.   (N-1)
```

The projective family is

```text
Pi_N(z;mu) = T_N(z;mu) / T_N(z_0;mu).          (N-2)
```

Since the Phase 76 scalar `theta_N` is built from canonical normalized
solutions, `(N-2)` is the relevant bridge quantity.  Raw transfer difference
is stronger than needed and may contain pure normalization drift.

## 3. Probe

Companion:

```text
E77_7m_pencil_transfer_probe.py
E77_7m_pencil_transfer_results.json
```

Command:

```bash
python3 E77_7m_pencil_transfer_probe.py \
  --lambda 6 --max-modes 18 --dps 60
```

The probe freezes `mu` at the largest finite section and compares, for each
smaller section:

```text
raw moving/frozen response x_N(mu_N), x_N(mu_ref);
projective profiles Pi_N(i sigma;mu_N), Pi_N(i sigma;mu_ref),
```

on `sigma in {0.6,1,2,3}` with anchor `sigma_0=1`.

The frozen point is only a finite surrogate, not the abstract `mu_L`.

## 4. Result

### Zeta

In E77.7b the raw safe-transfer defect was at the percent level:

```text
max relative difference ~ 0.0021 -- 0.0153.
```

After projective normalization it drops by roughly two orders of magnitude:

```text
max projective relative defect
= 6.38e-5 -- 1.81e-4     for N=7..17,
```

with `N=6` at `2.65e-4`.

So for zeta the moving/frozen discrepancy is mostly normalization drift, not
shape drift of the safe profile.

### Planted build

The raw safe-transfer defect in E77.7b ranged from

```text
0.054 up to 0.97,
```

with strong resonance sensitivity.

After projective normalization the defect becomes much smaller:

```text
max projective relative defect
= 0.073, 0.050, 0.042, 0.016, 0.021, ...
```

and decreases to

```text
0.0076, 0.0105, 0.0067, 0.0029
```

for `N=14..17`.

Thus projective normalization removes most of the plant's moving/frozen
instability as well.

## 5. Reading

The audit supports three conclusions.

```text
1. Raw transfer comparison is the wrong target.
   It overreacts to anchor scaling.

2. The correct bridge object is projective.
   The safe shape of the response is much more stable than its raw size.

3. This front is falsifier-neutral.
   Projective stabilization happens for both zeta and the planted build,
   so it cannot by itself be the arithmetic discriminant.
```

This is exactly the behavior required by the location rule: the LP interface
bridge should not kill the plant by a hidden sign or zero filter.

## 6. What is still not proved

The probe does **not** prove `PENCIL-TRANSFER-COMPATIBILITY`.

Open items remain:

```text
1. replace the finite frozen surrogate by the true mu_L;
2. prove local-uniform control on safe compacta, not one finite grid;
3. control the anchor T_N(z_0;mu) away from zero;
4. regularize the sections where A_N(mu_L) is singular.
```

So projective normalization identifies the right shape of the theorem, but
it does not close it.

## 7. Corrected bridge target

The admissible bridge is now:

```text
PROJECTIVE-MU-TRANSFER:
for each safe compact K,
sup_{z in K}
| T_N(z;mu_L)/T_N(z_0;mu_L) - T_N(z;0)/T_N(z_0;0) | -> 0,
```

with explicit anchor nonvanishing and singular-section treatment.

Then:

```text
PROJECTIVE-MU-TRANSFER
+ finite projective reduction
=> compatibility of the Phase 76 theta_N family with the intrinsic mu_L
   family.
```

This strictly improves E77.7m, because it identifies the correct projective
quantity rather than the stronger raw transfer.

## 8. Status

```text
proved:    exact mu-transfer identity (N-1);
observed:  projective normalization reduces zeta moving/frozen defects to
           1e-4 scale;
observed:  projective normalization removes most planted resonance as well;
refuted:   raw transfer difference as the right bridge target;
open:      PROJECTIVE-MU-TRANSFER at the true mu_L with anchor control and
           singular-section regularization.
```
