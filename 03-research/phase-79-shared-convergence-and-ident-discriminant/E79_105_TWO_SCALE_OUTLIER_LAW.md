# E79.105 - After the deterministic mean shift, the zeta outlier lock is largely a two-scale law

**Scope:** `DISCRIMINANT`, follow-up to E79.101 and E79.104.  
**Class:** REDUCCION GENUINA with an explicit empirical caveat.  

## 1. Why this is the next honest question

E79.101 reduced the live burden to the zeta-side lock

```text
outlier_abs ~= escape_scale.                                            (105-1)
```

E79.96 then reminded us that the old E78.155 finite predictor was not
`escape_scale` alone but

```text
kappa_hat = escape_scale + mean(d),                                     (105-2)
```

with `mean(d)` determined by the mesh.  For `lambda=6`,

```text
mean(d) = pi (N-1) / 6.                                                 (105-3)
```

So the next honest question is whether the remaining gap

```text
outlier_abs - (escape_scale + mean(d))                                  (105-4)
```

is still amorphous, or whether it already couples to another certified spectral
scale.

## 2. Probe

Companion files:

```text
E79_105_two_scale_outlier_law_probe.py
E79_105_two_scale_outlier_law_results.json
```

The probe reads only the certified spectral package from E79.101 and audits the
residual after removing `escape_scale + mean(d)`.  It then compares that
residual to `second_abs`.

As a descriptive compression, it fits a single zeta-side coefficient `alpha`
in the affine model

```text
outlier_abs ~= escape_scale + mean(d) + alpha second_abs.               (105-5)
```

This is a reading of the audited ladder, not a theorem claim.

## 3. Result

The least-squares coefficient on the audited zeta ladder is

```text
alpha_zeta ~= 0.23303.                                                  (105-6)
```

### Zeta

On the audited zeta ladder, the local coefficients

```text
alpha_N := [outlier_abs - escape_scale - mean(d)] / second_abs          (105-7)
```

lie in the narrow positive band

```text
0.1556, 0.1946, 0.1811, 0.2304, 0.2459, 0.2561,                        (105-8)
```

with mean about `0.2106` and standard deviation about `0.0362`.

Using the single fitted coefficient `alpha_zeta`, the two-scale affine model
predicts the actual zeta outlier with only

```text
mean abs relative error ~= 0.29%,
max  abs relative error ~= 0.56%.                                       (105-9)
```

So after peeling off the deterministic `mean(d)` shift, the remaining zeta-side
gap is already largely explained by `second_abs`.

### Planted controls

The same zeta-fitted affine law fails badly on the planted controls.

For `plant_gamma1_beta030`:

```text
mean local alpha ~= -0.0203,
std  local alpha ~=  0.0734,
mean abs prediction error ~= 20.0%,
max  abs prediction error ~= 24.6%.                                     (105-10)
```

For `plant_gamma2_beta030`:

```text
mean local alpha ~=  0.0732,
std  local alpha ~=  0.3809,
mean abs prediction error ~= 31.4%,
max  abs prediction error ~= 44.0%.                                     (105-11)
```

So the zeta-side two-scale law is not a generic artifact of the finite package.

## 4. Reading

This sharpens the live lock picture again.

The outlier lock is no longer best read as a bare near-identity

```text
outlier_abs ~= escape_scale.                                            (105-12)
```

Nor even as only the deterministic correction

```text
outlier_abs ~= escape_scale + mean(d).                                  (105-13)
```

Instead, on the audited zeta ladder it is already very close to a two-scale
affine law:

```text
outlier_abs ~= escape_scale + mean(d) + 0.23 second_abs.               (105-14)
```

The planted controls do not share this regime: after removing the same
deterministic `mean(d)` shift, their residuals against `second_abs` are not
rigid and may even change sign.

## 5. Consequence

After E79.105, the lock package can be read more structurally:

```text
zeta-side outlier lock
  = rank-one escape scale
  + deterministic mesh shift
  + coherent positive second-scale correction.                          (105-15)
```

This does not yet prove the lock, but it shrinks the honest burden.  The next
question is no longer just "why is `outlier_abs/escape_scale` near 1?", but:

```text
why does the residual after `escape_scale + mean(d)` line up with
`second_abs` on zeta, while the planted controls lose that coherence?   (105-16)
```

That is a more structured finite target than the raw lock ratio.
