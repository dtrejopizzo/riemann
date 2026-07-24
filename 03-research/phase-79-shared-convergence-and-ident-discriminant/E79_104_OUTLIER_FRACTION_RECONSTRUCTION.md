# E79.104 - Outlier fraction reconstructs once the zeta-side outlier lock is granted

**Scope:** IDENT discriminant geometry.
**Class:** REDUCCION GENUINA + correction to E79.103.

## 1. The exact identity

From the definitions already fixed in E79.90, E79.100, and E79.101,

```text
outlier_fraction = outlier_abs / second_abs,
spectral_reading = sqrt(outlier_abs * second_abs) / mesh_radius.
```

Therefore

```text
outlier_fraction
  = (outlier_abs / (mesh_radius * spectral_reading))^2.            (1)
```

This is exact. So once `outlier_abs` and `spectral_reading` are read from the
same certified cloud, `outlier_fraction` is already determined; it is not an
independent primitive beyond those two spectral quantities.

Now use the E79.90/E79.96 normalization

```text
escape_ratio = escape_scale / mesh_radius,
```

together with the zeta-side lock from E79.101:

```text
outlier_abs / escape_scale ~= 1.
```

Then (1) becomes

```text
outlier_fraction
  = (escape_ratio / spectral_reading)^2 * (outlier_abs / escape_scale)^2.   (2)
```

So after granting the outlier lock, `outlier_fraction` should be recoverable
from `escape_ratio` and `spectral_reading` up to the same lock error.

## 2. Probe

Probe `E79_104_outlier_fraction_reconstruction_probe.py` combines the certified
section data from E79.90 with the certified spectral audit from E79.101.

For each row it records:

```text
- exact reconstruction:      (outlier_abs / (mesh_radius * spectral_reading))^2
- lock-based approximation:  (escape_ratio / spectral_reading)^2
- lock ratio:                outlier_abs / escape_scale
```

## 3. Result

### Zeta

```text
N   outlier_fraction   approx/outlier_fraction   outlier_abs/escape_scale
8    13.8936                 0.9734                    1.0136
10   11.1090                 0.9603                    1.0205
12   11.8280                 0.9652                    1.0179
14   10.5662                 0.9521                    1.0248
16   10.2197                 0.9478                    1.0271
18    9.6796                 0.9432                    1.0297
```

And exactly as (2) predicts,

```text
approx/outlier_fraction = (escape_scale/outlier_abs)^2
                        = 1 / (outlier_abs/escape_scale)^2.
```

So on the audited zeta ladder the lock-based reconstruction error is only about
`4.3%` on average and at most about `5.7%`, which is precisely the E79.101
outlier-lock error transported through the square.

### Planted controls

```text
case                    mean abs approx rel error   max abs approx rel error
plant_gamma1_beta030              ~0.334                      ~0.557
plant_gamma2_beta030              ~0.301                      ~0.973
```

The exact identity (1) still holds row by row, but the `escape_ratio` version
fails badly because the outlier lock fails badly there too.

## 4. Consequence

This corrects the last sentence of E79.103.

It is still true that `second_abs / mesh_radius` by itself was not a new
primitive invariant. But after E79.101, the zeta-side burden does **not**
sharpen to `outlier_fraction` as a further independent mystery. Instead:

```text
outlier_fraction is already reconstructed once one grants
  (a) spectral_reading, and
  (b) the zeta-side outlier lock escape_scale ~= outlier_abs.
```

So the honest surviving burden is the lock package itself, not a new scalar
`outlier_fraction` layered on top of it.

Equivalently: on the audited zeta ladder,

```text
escape_ratio / spectral_reading ~= sqrt(outlier_fraction),
```

with exactly the error forced by the outlier lock.

## 5. Updated live reading

After E79.104 the sharpest honest picture is:

```text
- exact spectral geometry: outlier_fraction is derived from outlier_abs and
  spectral_reading;
- zeta-specific extra rigidity: outlier_abs ~= escape_scale;
- therefore zeta reconstructs outlier_fraction from escape_ratio and
  spectral_reading, while the planted controls do not.
```

So the live discriminant burden remains the zeta-only lock
`escape_scale ~= outlier_abs`, together with whatever mechanism forces the
shared spectral-reading package that this lock plugs into.
