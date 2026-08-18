# E79.102 - After the outlier lock, the load-bearing spectral burden sharpens to the second scale

**Scope:** `DISCRIMINANT`, continuation of E79.101.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** once the
zeta-side lock

```text
escape_scale ~= outlier_abs                                             (102-1)
```

is in place, the remaining spectral burden is no longer diffuse. It sharpens to
the second spectral scale

```text
second_abs / mesh_radius.                                               (102-2)
```

## 0. Why this is the next candid compression

E79.101 upgraded the live object to a genuinely spectral form:

```text
escape_ratio / sqrt(outlier_fraction)
~= sqrt(outlier_abs * second_abs) / mesh_radius                        (102-3)
```

across the audited zeta ladder, because `outlier_abs / escape_scale` is already
locked within about `3%`.

Once that lock is granted, the only remaining spectral inputs are:

```text
outlier_abs / mesh_radius,
second_abs / mesh_radius.                                               (102-4)
```

So the next unavoidable question is:

```text
which of those two scales is still carrying the discriminating content? (102-5)
```

## 1. Evidence used

No new build is needed.  This note reads directly from

```text
E79_101_outlier_escape_agreement_results.json.                         (102-6)
```

and records, for each build and audited row:

```text
second_abs / mesh_radius,
outlier_abs / mesh_radius,
sqrt(outlier_abs * second_abs) / mesh_radius.                          (102-7)
```

## 2. Result

### Zeta

On the audited zeta ladder:

```text
second_abs / mesh_radius
  = 9.81, 10.57, 11.21, 11.66, 12.31, 12.99,                          (102-8)
```

so the second scale already lives in a stable linear-in-mesh regime of size

```text
~ 10 .. 13.                                                             (102-9)
```

### Planted controls

The planted controls do not share that regime.

For `plant gamma1`:

```text
second_abs / mesh_radius
  = 0.94, 1.13, 1.34, 1.35, 1.32, 1.25.                               (102-10)
```

For `plant gamma2`:

```text
second_abs / mesh_radius
  = 1.15, 1.04, 0.94, 1.09, 1.12, 1.09.                               (102-11)
```

So after the outlier lock, the second spectral scale alone still separates
zeta from both planted controls by more than an order of magnitude.

## 3. Reading

This is the key compression.

Before E79.101, the live object was still a mixed escape/outlier quantity.
After E79.101, the outlier side is already almost identified with the rank-one
escape scale itself on zeta.

That leaves the second scale as the genuinely new partner.

So the spectral reading

```text
sqrt(outlier_abs * second_abs) / mesh_radius                           (102-12)
```

is no longer balancing two equally mysterious factors. On the audited zeta
ladder:

- the first factor is already locked to the escape mechanism;
- the second factor is what remains genuinely arithmetic/discriminating.        (102-13)

In other words:

```text
after factoring out the outlier lock, the live burden sharpens to the
linear growth regime of second_abs.                                    (102-14)
```

## 4. Consequence

After E79.102, the candid next target is no longer the full mixed quantity

```text
escape_ratio / sqrt(outlier_fraction).                                 (102-15)
```

It is the sharper spectral statement:

```text
on zeta, second_abs grows linearly with the mesh at a scale ~10..13,
while the planted builds stay at scale ~1.                              (102-16)
```

Together with E79.101, that would explain the mixed spectral law almost
entirely.

## 5. Status

```text
proved by audit:
  after the outlier lock, second_abs / mesh_radius still separates zeta from
  both planted controls by more than an order of magnitude;

reduced:
  the post-E79.101 burden from the mixed spectral quantity to the second
  spectral scale itself;

open:
  explain the zeta-side linear growth regime of second_abs / mesh_radius, or
  identify the first certified breakdown of that regime.
```
