# E79.100 - On the shared audited ladder, the escape-outlier coupling already has a direct spectral reading

**Scope:** `DISCRIMINANT`, refinement of the live object after E79.99.  
**Class:** REDUCCION GENUINA with explicit scope limit.  
**What we know after this document that we did not know before:** on the shared
audited ladder `N=8,10,12`, the zeta-side escape scale is already within about
`2%` of the actual farthest spectral outlier of `K_N`.  Consequently, the live
escape-outlier object from E79.99 can be read, on that shared ladder, as the
geometric mean of the top two spectral radii divided by the mesh radius.

## 0. Why this check is worth doing

E79.99 reduced the live burden to

```text
escape_ratio / sqrt(outlier_fraction),                                 (100-1)
```

where

```text
escape_ratio      = escape_scale / mesh_radius,
escape_scale      = |q^T x| / |c|,
outlier_fraction  = outlier_abs / second_abs.                          (100-2)
```

So algebraically,

```text
escape_ratio / sqrt(outlier_fraction)
  = (escape_scale / mesh_radius) * sqrt(second_abs / outlier_abs).     (100-3)
```

If `escape_scale` is close to `outlier_abs`, then the whole live object becomes

```text
sqrt(outlier_abs * second_abs) / mesh_radius,                          (100-4)
```

which is a direct and very natural spectral quantity.

The question is whether that approximation is actually true in the certified
data, or only wishful thinking.

## 1. Evidence used

No new build is needed.  This note combines the shared audited rows

```text
N = 8, 10, 12                                                          (100-5)
```

from:

```text
E79_85_cloud_symmetry_bridge_results.json   (outlier_abs, second_abs),
E79_90_escape_balance_split_results.json    (escape_scale, mesh_radius). (100-6)
```

The scope limit matters: E79.85 only audited the cloud spectrum through `N=12`,
so this note is intentionally limited to the shared subladder.

## 2. Result

### Zeta

On the shared zeta ladder:

```text
outlier_abs / escape_scale
  = 1.0136, 1.0205, 1.0179.                                            (100-7)
```

So the rank-one escape scale already matches the actual farthest outlier of
`K_N` to within about

```text
1.4% .. 2.1%.                                                          (100-8)
```

Consequently,

```text
escape_ratio / sqrt(outlier_fraction)
```

is already the same as

```text
sqrt(outlier_abs * second_abs) / mesh_radius                           (100-9)
```

up to that same tiny relative error.

### Planted controls

The planted controls do **not** share this rigidity.

For `plant gamma1`:

```text
outlier_abs / escape_scale
  = 1.50, 1.08, 1.22,                                                  (100-10)
```

and for `plant gamma2`:

```text
outlier_abs / escape_scale
  = 1.16, 6.14, 1.04.                                                  (100-11)
```

So the spectral reading is not generically true across builds.  It is a real
feature of the candid zeta-side regime, not a tautology.

## 3. Reading

This sharpens E79.99 in a useful way.

The live object is no longer just an algebraic escape/outlier quotient. On the
shared candid ladder it already has a direct spectral interpretation:

```text
zeta-side live object
  ~= geometric mean of the two largest spectral scales of K_N,
     normalized by the mesh radius.                                    (100-12)
```

That is much more concrete than a bare quotient.

Just as importantly, the planted controls show why this is not empty:

- they can share the definition of `escape_ratio / sqrt(outlier_fraction)`,
- but they do **not** share the near-identity `escape_scale ~= outlier_abs`.    (100-13)

So the candid content is that, on zeta, the rank-one escape mechanism is
already visible at the level of the actual farthest spectral atom.

## 4. Consequence

After E79.100, the live burden sharpens once more:

```text
either explain why, on the candid ladder,
  escape_scale ~= outlier_abs
and therefore
  escape_ratio / sqrt(outlier_fraction)
  ~= sqrt(outlier_abs * second_abs) / mesh_radius,                     (100-14)
```

or find the first audited breakdown of that spectral reading beyond the shared
subladder.

This does **not** yet replace E79.99 as the global live object, because the
shared-ladder scope is only `N=8,10,12`. But it does give the first direct
spectral interpretation of that object on certified data.

## 5. Status

```text
proved by shared-ladder audit:
  on zeta, escape_scale and outlier_abs already agree within about 2%;

proved by shared-ladder audit:
  the planted controls do not share that rigidity;

reduced:
  the E79.99 escape-outlier object to a direct spectral reading on the shared
  audited ladder:
    sqrt(outlier_abs * second_abs) / mesh_radius;

scope caveat:
  this reading is currently certified only on the shared rows N=8,10,12,
  because that is the overlap of the audited artifacts.
```
