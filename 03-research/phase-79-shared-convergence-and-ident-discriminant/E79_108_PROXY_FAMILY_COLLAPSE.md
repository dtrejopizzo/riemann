# E79.108 - The best proxy family collapses to one object once the outlier lock is granted

**Scope:** `DISCRIMINANT`, cleanup after E79.107.  
**Class:** REDUCCION GENUINA.  

## 1. Why this note is needed

E79.107 found three comparably good zeta-side proxies for the residual
coefficient

```text
alpha_N := [outlier_abs - escape_scale - mean(d)] / second_abs:        (108-1)

c1 := spectral_reading/escape_ratio - mesh_radius/second_abs,
c2 := c1 / (1 + mesh_radius/second_abs),
c4 := 1/sqrt(outlier_fraction) - mesh_radius/second_abs.              (108-2)
```

At first sight that looked like a small family of different good candidates.
But E79.104 had already proved that, once the outlier lock is granted,

```text
spectral_reading/escape_ratio ~= 1/sqrt(outlier_fraction),             (108-3)
```

with exactly the transported lock error.

So the next candid check is whether the E79.107 proxy family is genuinely
multiple, or whether it already collapses to a single object modulo the known
lock error.

## 2. Exact relation

From E79.104,

```text
outlier_fraction
  = (escape_ratio / spectral_reading)^2 * (outlier_abs/escape_scale)^2, (108-4)
```

hence

```text
spectral_reading/escape_ratio
  = (outlier_abs/escape_scale) / sqrt(outlier_fraction).               (108-5)
```

Therefore the two main E79.107 proxies satisfy the exact identity

```text
c1 - c4
  = spectral_reading/escape_ratio - 1/sqrt(outlier_fraction)
  = [(outlier_abs/escape_scale) - 1] / sqrt(outlier_fraction).         (108-6)
```

So `c1` and `c4` are not independent candidates at all. They differ exactly by
the same outlier-lock defect already isolated in E79.101/E79.104.

## 3. Audit

Using the certified E79.90 and E79.101 rows:

### Zeta

```text
|spectral_reading/escape_ratio - 1/sqrt(outlier_fraction)|
  = 0.00364, 0.00614, 0.00520, 0.00764, 0.00849, 0.00954,             (108-7)
```

with relative errors

```text
1.36%, 2.05%, 1.79%, 2.48%, 2.71%, 2.97%,                             (108-8)
```

which are exactly the E79.101 outlier-lock errors.

### Planted controls

The same difference is large precisely where the lock fails:

```text
plant_gamma1_beta030: mean relative gap ~ 24.4%, max ~ 50.3%,
plant_gamma2_beta030: mean relative gap ~ 93.8%, max ~ 514%.          (108-9)
```

So the proxy-family collapse is a genuine zeta-side consequence of the lock,
not a tautology of the finite package.

## 4. Reading

This cleans up E79.107 substantially.

The best proxy family is not really three unrelated near-hits. Once the
E79.104 lock is inserted, it collapses to:

```text
one subtraction-shaped object
  [1/sqrt(outlier_fraction)] - [mesh_radius/second_abs],               (108-10)
```

or equivalently

```text
[spectral_reading/escape_ratio] - [mesh_radius/second_abs],            (108-11)
```

with the difference between the two forms controlled exactly by the same lock
defect already tracked elsewhere.

So after E79.108 the live burden is cleaner than E79.107 suggested:

```text
the residual coefficient nearly collapses to one subtraction-shaped proxy,
not to a broad family of unrelated biescalar formulas.                 (108-12)
```

## 5. Consequence

After E79.108, the next candid target is:

```text
explain why alpha_N nearly matches
  1/sqrt(outlier_fraction) - mesh_radius/second_abs
on zeta, while the planted controls do not,                            (108-13)
```

with the equivalent `spectral_reading/escape_ratio` form available whenever the
outlier lock is the preferred language.

That is the sharpest finite form of the residual-coherence object so far.
