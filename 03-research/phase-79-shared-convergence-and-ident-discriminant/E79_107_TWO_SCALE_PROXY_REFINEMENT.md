# E79.107 - Not every two-scale proxy is equal: the residual coefficient has a narrow admissible shape

**Scope:** `DISCRIMINANT`, refinement after the E79.106 autopsy.  
**Class:** REDUCCION GENUINA + proxy audit.  

## 1. Why this note exists

E79.106 showed that the residual coefficient

```text
alpha_N := [outlier_abs - escape_scale - mean(d)] / second_abs         (107-1)
```

does **not** inherit from any obvious one-scalar formula. That was important,
but it left open a more delicate possibility:

```text
maybe alpha_N is not one-scale, yet still has a nearly canonical
two-scale proxy built from the already certified package.              (107-2)
```

This note audits the first such candidates directly.

## 2. Candidates tested

Using only the certified E79.90 and E79.101 rows, compare `alpha_N` against:

```text
c1 := spectral_reading/escape_ratio - mesh_radius/second_abs,
c2 := c1 / (1 + mesh_radius/second_abs),
c3 := (spectral_reading/escape_ratio) * (1 - mesh_radius/second_abs),
c4 := 1/sqrt(outlier_fraction) - mesh_radius/second_abs,
c5 := spectral_reading/escape_ratio - mean(d)/second_abs.             (107-3)
```

The point is not to fit a new coefficient.  The point is to see whether the
E79.105 residual already prefers a narrow family of biescalar shapes.

## 3. Result

### Zeta

On the audited zeta ladder, the best candidates are clearly:

```text
c1: mean abs error ~ 0.0110, max ~ 0.0257,
c2: mean abs error ~ 0.0124, max ~ 0.0238,
c4: mean abs error ~ 0.0127, max ~ 0.0205.                            (107-4)
```

The weaker candidates are much worse:

```text
c3, c5: mean abs error ~ 0.069.                                        (107-5)
```

So after E79.106, the candid refinement is that `alpha_N` is not an arbitrary
two-scale object either: on zeta it already prefers a very narrow shape,
essentially

```text
spectral-reading piece  minus  mesh/second piece,                      (107-6)
```

with only mild further normalization freedom.

### Planted controls

That narrow shape is still not a build-uniform identity.

For `plant_gamma1_beta030`, the best of the same candidates is:

```text
c4: mean abs error ~ 0.171, max ~ 0.257,
c2: mean abs error ~ 0.181, max ~ 0.301.                              (107-7)
```

For `plant_gamma2_beta030`, the best is:

```text
c3: mean abs error ~ 0.319, max ~ 0.524,
c4: mean abs error ~ 0.396, max ~ 1.049.                              (107-8)
```

So the zeta-side proxy family does **not** transport canonically to the planted
controls.

## 4. Reading

This refines both E79.105 and E79.106.

- E79.105 said the residual is coherently tied to `second_abs`.
- E79.106 said it is not a disguised one-scalar invariant.
- E79.107 adds: among biescalar proxies, only a narrow subtraction-shaped family
  comes close on zeta.

The candid picture is now:

```text
alpha_N is genuinely biescalar,
but not wildly so;
on zeta it strongly prefers
  [spectral piece] - [mesh/second correction].                         (107-9)
```

That is a real structural sharpening of the live burden.

## 5. Consequence

After E79.107, the next candid target is no longer the raw question

```text
"why is alpha_N coherent?"                                             (107-10)
```

but the more structured one:

```text
why does the zeta-side residual coefficient nearly collapse onto the
subtraction-shaped proxy family
  spectral_reading/escape_ratio - mesh_radius/second_abs,
while the planted controls do not?                                     (107-11)
```

This is still not a theorem target, but it is a much tighter finite object than
the original outlier lock.
