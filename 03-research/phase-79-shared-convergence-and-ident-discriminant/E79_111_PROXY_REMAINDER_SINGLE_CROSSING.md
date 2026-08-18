# E79.111 - The zeta proxy remainder is small and single-crossing

**Scope:** `DISCRIMINANT`, continuation of E79.110.  
**Class:** REDUCCION GENUINA.  

## 1. Question

E79.110 showed that the subtraction proxy

```text
proxy_N := 1/sqrt(outlier_fraction) - mesh_radius/second_abs           (111-1)
```

already captures most of the zeta residual coefficient

```text
alpha_N := [outlier_abs - escape_scale - mean(d)] / second_abs.        (111-2)
```

The next candid question is whether the leftover gap

```text
gap_N := alpha_N - proxy_N                                             (111-3)
```

is merely small, or whether it also has some residual organization.

## 2. Audit

Using the certified E79.90 and E79.101 rows, inspect:

```text
- the sign pattern of gap_N across the audited ladder,
- the absolute size |gap_N|.                                           (111-4)
```

## 3. Result

### Zeta

On the audited zeta ladder:

```text
gap_N = -0.0108, -0.0108, -0.0205, +0.0085, +0.0142, +0.0116.         (111-5)
```

So the zeta remainder has two notable features at once:

```text
1. it stays small in absolute value:
     mean |gap_N| ~ 0.0127,
     max  |gap_N| ~ 0.0205;                                            (111-6)

2. it changes sign exactly once:
     (-,-,-,+,+,+).                                                    (111-7)
```

In other words, on zeta the proxy first slightly overshoots `alpha_N`, then
slightly undershoots it, with only one crossing on the whole audited ladder.

### Planted controls

The planted controls do not share the same clean smallness regime.

For `plant_gamma1_beta030`:

```text
gap sign pattern = (+,-,-,-,-,-),
mean |gap_N| ~ 0.171,
max  |gap_N| ~ 0.257.                                                  (111-8)
```

For `plant_gamma2_beta030`:

```text
gap sign pattern = (+,+,-,-,-,-),
mean |gap_N| ~ 0.396,
max  |gap_N| ~ 1.049.                                                  (111-9)
```

They also show only one sign change, but at a scale one to two orders of
magnitude larger than zeta. So what matters is not the bare crossing count by
itself, but:

```text
single crossing + uniformly tiny remainder.                            (111-10)
```

## 4. Reading

This sharpens E79.110 in a useful way.

The subtraction proxy is not merely a dominant approximation on zeta. Its
remainder is already highly organized:

```text
small amplitude + one clean sign crossing across the audited ladder.   (111-11)
```

That is a much more structured object than an arbitrary unresolved error term.

## 5. Consequence

After E79.111, the candid live burden on this branch becomes:

```text
explain why the zeta-side residual coefficient is exhausted by the
subtraction proxy up to a tiny single-crossing remainder,
while the planted controls miss that small-amplitude regime.           (111-12)
```

This is the sharpest finite reading of the residual-coherence package so far.
