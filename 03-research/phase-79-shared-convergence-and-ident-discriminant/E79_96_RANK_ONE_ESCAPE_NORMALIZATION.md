# E79.96 - The escape plateau is exactly a normalized rank-one escape scale

**Scope:** `DISCRIMINANT`, escape branch after E79.95.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the large
zeta-side plateau from E79.95 is not an abstract quotient with no internal
name. It is exactly the rank-one escape scale already present in the finite
package, normalized by the mesh radius.

## 0. Why this is the right next move

E79.95 left the live object in the form

```text
escape_ratio = (|q^T x|/mesh_radius)/|c|,                              (96-1)
```

with the question:

```text
why does this quotient lock onto a large zeta-side plateau?            (96-2)
```

But `phase-78` had already exposed a canonical rank-one escape scale:

```text
kappa_hat = q^T x / c + mean(d),                                       (96-3)
```

from E78.155.

So the immediate finite question is whether the plateau is really a new object,
or just the old rank-one escape scale seen in the correct normalization.

## 1. Derived probe

Companion files:

```text
E79_96_rank_one_escape_normalization_probe.py
E79_96_rank_one_escape_normalization_results.json
```

This is a **derived audit only**.  It reads the already certified ladders

```text
E79_90_escape_balance_split_results.json,
E79_91_escape_denominator_results.json,                                (96-4)
```

and checks three relations:

```text
(a) escape_ratio ?= escape_scale / mesh_radius,
(b) kappa_hat = |q^T x|/|c| + mean(d),
(c) how large is the normalized mean(d) shift?                         (96-5)
```

No new matrix build is used.

## 2. Exact identity behind the plateau

On the E79.90 ladder, `escape_scale` is exactly

```text
escape_scale = |q^T x| / |c|.                                          (96-6)
```

Therefore

```text
escape_ratio
  = (|q^T x|/mesh_radius)/|c|
  = (|q^T x|/|c|) / mesh_radius
  = escape_scale / mesh_radius.                                        (96-7)
```

The derived audit confirms this to roundoff on every audited row:

```text
max identity error:
  zeta                <= 1.4e-14,
  plant gamma1 beta=.30 <= 2.3e-16.                                   (96-8)
```

So the plateau from E79.95 is not a free-standing mystery. It is exactly the
mesh-normalized rank-one escape scale already present in the finite package.

## 3. Relation to the E78.155 predictor

E78.155 did not use `|q^T x|/|c|` alone. It used

```text
kappa_hat = |q^T x|/|c| + mean(d).                                     (96-9)
```

Hence

```text
kappa_hat / mesh_radius
  = escape_ratio + mean(d)/mesh_radius * 1/escape_scale * escape_scale
  = escape_ratio * (1 + mean(d)/escape_scale).                        (96-10)
```

So the only difference between `kappa_hat/mesh_radius` and `escape_ratio` is
the relative shift

```text
mean(d) / escape_scale.                                                (96-11)
```

And this is exactly where the two builds part ways.

## 4. Result

### Zeta

On the audited zeta ladder,

```text
mean(d) / escape_scale ~ 0.00222 .. 0.00260,                           (96-12)
```

so the shift is only about a quarter of one percent.  In particular:

```text
kappa_hat / mesh_radius
  = escape_ratio * (1 + O(2.5e-3)).                                   (96-13)
```

So on zeta the plateau is already the normalized E78.155 rank-one escape scale,
up to a tiny deterministic correction.

### Planted main control

On the planted main control,

```text
mean(d) / escape_scale ~ 0.18 .. 0.39,                                 (96-14)
```

so the same shift is order-one relative to the escape scale itself.

Therefore the planted build is **not** in the same asymptotic regime:

```text
kappa_hat / mesh_radius
  and
escape_ratio
remain visibly different.                                               (96-15)
```

This matches the qualitative picture from E78.155: the zeta build sits in a
genuine rank-one escape regime, while the planted build does not.

## 5. Reading

This sharpens E79.95 in an important way.

The live question is no longer

```text
why does an unnamed quotient stay large?                               (96-16)
```

It is now:

```text
why does the normalized rank-one escape scale
  (|q^T x|/|c|) / mesh_radius
stabilize around 10^2 on the zeta ladder, while the planted build stays
order-one?                                                              (96-17)
```

That is a smaller and more canonical target.

It also keeps the E78.155 correction honest:

- we are **not** reviving the false claim that one far outlier drives the
  transfer;
- we are using the rank-one escape scale only as a finite normalization of the
  escape branch, not as the transfer-dominating eigenvalue itself.              (96-18)

## 6. Consequence

After E79.96, the escape-side branch reduces again:

```text
CLOSE
=> large normalized rank-one escape scale
   (|q^T x|/|c|) / mesh_radius
=> STRONG_ESCAPE.                                                       (96-19)
```

So the next honest burden is no longer to explain an arbitrary plateau, but to
explain why the **rank-one escape scale itself** becomes linear in the mesh
with a large zeta-side constant.

## 7. Status

```text
proved by derived audit:
  escape_ratio is exactly escape_scale / mesh_radius on the audited ladder;

proved by derived audit:
  the E78.155 shift from escape_scale to kappa_hat is tiny on zeta
  (~0.22%-0.26%) and order-one relative on the planted main control
  (~18%-39%);

reduced:
  the E79.95 plateau question to the canonical finite object
  (|q^T x|/|c|) / mesh_radius, i.e. the normalized rank-one escape scale;

open:
  explain why that normalized rank-one escape scale stabilizes at a large
  zeta-side value instead of remaining order-one.
```
