# E79.103 - The second spectral scale is not independent on the audited ladder; it largely repackages outlier fraction

**Scope:** `DISCRIMINANT`, post-E79.102 audit of the second-scale reduction.  
**Class:** AUTOPSIA FRANCA + sharper replacement target.  
**What we know after this document that we did not know before:** the second
spectral scale isolated in E79.102 is not behaving like a genuinely new
primitive object on the audited ladder.  It is already largely encoded by the
older geometric quantity `outlier_fraction`.

## 0. Why this check is necessary

E79.102 reduced the post-E79.101 burden to

```text
second_abs / mesh_radius.                                               (103-1)
```

But before promoting that to the next primitive invariant, we have to rule out
the simpler possibility that it is just a repackaging of data already present in
the cloud geometry.

The most obvious candidate is `outlier_fraction`, since both quantities come
from the same two leading spectral scales:

```text
outlier_fraction = outlier_abs / second_abs.                           (103-2)
```

So the immediate audit is whether

```text
(second_abs / mesh_radius) / outlier_fraction                          (103-3)
```

is already roughly rigid.

## 1. Evidence used

No new build is needed.  This note combines

```text
E79_101_outlier_escape_agreement_results.json,
E79_90_escape_balance_split_results.json.                              (103-4)
```

and records the derived ratio

```text
R_N := (second_abs / mesh_radius) / outlier_fraction.                  (103-5)
```

## 2. Result

### Zeta

On the audited zeta ladder,

```text
R_N = 0.706, 0.951, 0.948, 1.103, 1.205, 1.342.                        (103-6)
```

So `second_abs / mesh_radius` and `outlier_fraction` already track each other
at order-one scale, with the ratio staying near `1` rather than opening a new
order-of-magnitude regime.

### Planted main control

On `plant gamma1`,

```text
R_N = 0.769, 0.717, 1.160, 1.322, 1.082, 0.930.                        (103-7)
```

This is strikingly similar in size and variability to zeta.

### Second planted control

On `plant gamma2`, aside from the already anomalous `N=8` row,

```text
R_N = 0.951, 0.816, 1.008, 0.934, 0.875                               (103-8)
```

on `N=10..18`, again order-one and close to the same regime.

So the separation discovered in E79.102 does **not** come from a genuinely new
shape of the ratio `second_abs / mesh_radius` relative to `outlier_fraction`.
It comes from the fact that zeta has much larger `outlier_fraction` to begin
with.

## 3. Reading

This is the candid correction to E79.102.

E79.102 was useful because it localized the remaining spectral burden to the
second scale. But the new audit shows that this second scale is not behaving as
an independent invariant. On the audited ladder it is already mostly determined,
up to an order-one factor, by the older outlier geometry:

```text
second_abs / mesh_radius
  ~= outlier_fraction.                                                  (103-9)
```

So the live content does **not** really sit in "linear growth of second_abs" as
a separate mystery. It sits one step earlier, in the fact that the outlier
fraction itself enters the zeta-side regime:

```text
outlier_fraction ~ 10..14   (zeta)
vs
outlier_fraction ~ 1        (planted).                                 (103-10)
```

That is the load-bearing difference.

## 4. Consequence

After E79.103, the candid post-E79.101 picture is:

```text
1. outlier lock:  escape_scale ~= outlier_abs,                         (103-11)
2. second scale:  second_abs / mesh_radius mostly repackages
                  outlier_fraction,
3. so the genuinely new burden is not second_abs by itself,
   but the large zeta-side outlier-fraction regime.                    (103-12)
```

So the next admissible target is not

```text
explain second_abs / mesh_radius as a new primitive invariant.         (103-13)
```

It is:

```text
explain why outlier_fraction itself enters the zeta-side regime
~ 10..14 while the planted builds stay near 1.                         (103-14)
```

That is simpler, older, and more faithful to the actual audited dependence.

## 5. Status

```text
proved by audit:
  the ratio (second_abs / mesh_radius) / outlier_fraction stays order-one
  across the audited ladder and does not create a new separation regime;

corrected:
  the E79.102 second-scale reduction is not a new primitive invariant;

reduced:
  the post-E79.101 live burden back to the large zeta-side regime of
  outlier_fraction itself, together with the already-audited outlier lock
  escape_scale ~= outlier_abs;

open:
  explain the zeta-side outlier-fraction regime, or identify the first
  certified breakdown of treating it as the next primitive discriminant object.
```
