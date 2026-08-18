# E79.97 - The normalized rank-one escape scale and the cloud defect obey a zeta-side square-root law

**Scope:** `DISCRIMINANT`, bridge from the escape branch to the geometric branch.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the canonical
escape object from E79.96 does not float independently of the cloud geometry.
On the audited zeta ladder it couples to the geometric defect `D_N` by an
almost constant square-root law.

## 0. Why this is the right next move

E79.96 reduced the escape branch to the canonical finite quantity

```text
escape_ratio = (|q^T x|/|c|) / mesh_radius.                            (97-1)
```

The next candid question was whether that normalized rank-one escape scale can
be tied to any already-audited geometric object, instead of staying as an
isolated scalar.

The most direct candidate is the cloud defect `D_N`, because it is already part
of the operational geometry gate:

```text
GEOM := outlier_fraction > 5 and D_N < 5e-3.                           (97-2)
```

So the natural derived check is:

```text
does escape_ratio couple to D_N by a simple scale law?                 (97-3)
```

## 1. Derived probe

Companion files:

```text
E79_97_escape_geometry_sqrt_law_probe.py
E79_97_escape_geometry_sqrt_law_results.json
```

This is again a **derived audit only**.  It reads the certified long-ladder
data in

```text
E79_90_escape_balance_split_results.json,                              (97-4)
```

and records

```text
escape_ratio * sqrt(D_N)                                               (97-5)
```

for the audited rows of

```text
zeta,
plant gamma1 beta=.30,
plant gamma2 beta=.30.                                                 (97-6)
```

No new build is performed.

## 2. Result

### Zeta

On the audited zeta ladder,

```text
escape_ratio * sqrt(D_N)
  = 4.8185, 4.5992, 4.4905, 4.6561, 4.7142, 4.6106,                    (97-7)
```

so the quantity stays in a narrow band around

```text
~ 4.65                                                                  (97-8)
```

with relative spread about

```text
7.1%.                                                                  (97-9)
```

Equivalently,

```text
escape_ratio ~ 4.65 / sqrt(D_N)                                        (97-10)
```

all along the audited zeta ladder.

### Planted main control

On `plant gamma1 beta=.30`,

```text
escape_ratio * sqrt(D_N)
  = 0.252, 0.198, 0.129, 0.104, 0.112, 0.101,                          (97-11)
```

an order of magnitude smaller than zeta and drifting downward rather than
locking to the zeta scale.

### Second planted control

On `plant gamma2 beta=.30`, the same quantity is not rigid either:

```text
1.204, 0.082, 0.123, 0.151, 0.116, 0.088,                              (97-12)
```

including the already-understood resonant row at `N=8`, but with no stable
zeta-side scale.

## 3. Reading

This is the first clean bridge between the canonical escape object and the cloud
geometry.

E79.96 said:

```text
the live escape object is the normalized rank-one scale
  (|q^T x|/|c|)/mesh_radius.                                            (97-13)
```

E79.97 adds:

```text
on zeta, that scale is almost exactly the inverse square root of D_N.   (97-14)
```

So the geometry is no longer merely "downstream" from escape. On the audited
ladder, the two are quantitatively locked:

```text
large rank-one escape  <=>  very small D_N,                            (97-15)
```

with the zeta-side coupling law

```text
escape_ratio * sqrt(D_N) ~ const_zeta.                                 (97-16)
```

This does **not** prove a theorem-grade implication yet, but it changes the
shape of the burden in a useful way.  We no longer need to explain
`escape_ratio` and `D_N` as separate miracles.  The audited evidence says they
are two faces of one scale law on the candid ladder.

## 4. Consequence

After E79.97, the live burden can be sharpened from

```text
explain why escape_ratio is large                                          (97-17)
```

to

```text
explain the zeta-side square-root coupling
  escape_ratio ~ const / sqrt(D_N),                                   (97-18)
```

or name the first audited breakdown of that law.

Operationally, this is also the first direct bridge from the escape half back
to the geometry gate `GEOM`.

## 5. Status

```text
proved by derived audit:
  on the audited zeta ladder, escape_ratio * sqrt(D_N) stays in a narrow band
  around 4.65 with only about 7% relative spread;

proved by derived audit:
  both planted controls fail to enter that zeta-side square-root regime;

reduced:
  the escape/geometry front to a single coupled scale law rather than two
  unrelated predicates;

open:
  determine whether this square-root law can be derived from closure+balance,
  or whether it is the next primitive finite invariant of the discriminant.
```
