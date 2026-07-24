# E79.112 - On the honest ladder, the proxy remainder crosses once near the middle and stays genuinely secondary

**Scope:** `DISCRIMINANT`, refinement of E79.111.  
**Class:** REDUCCION GENUINA.  

## 1. Why this note is worth adding

E79.111 established that on the audited zeta ladder the proxy remainder

```text
gap_N := alpha_N - \left( 1/\sqrt{outlier_fraction} - mesh_radius/second_abs \right)
                                                                      (112-1)
```

is:

```text
- tiny in absolute value,
- single-crossing in sign.                                             (112-2)
```

There are two natural follow-up questions:

```text
1. where does that crossing occur on the audited ladder?
2. how secondary is the gap compared to the proxy itself?              (112-3)
```

## 2. Audit

Use the same certified E79.90 and E79.101 rows.

For the crossing location, linearly interpolate between the last negative and
first positive zeta rows.

For the size comparison, inspect

```text
|gap_N| / |proxy_N|                                                    (112-4)
```

and equivalently compare the mean absolute scales of `gap_N`, `proxy_N`, and
`alpha_N`.

## 3. Result

### Zeta crossing window

From E79.111 the zeta sign pattern is

```text
(-,-,-,+,+,+),                                                         (112-5)
```

with the sign change occurring between `N=12` and `N=14`:

```text
gap_12 = -0.02046,
gap_14 = +0.00854.                                                     (112-6)
```

Linear interpolation places the crossing at

```text
N_cross ~ 13.41.                                                       (112-7)
```

So the crossing is not a boundary effect at the first or last audited row. It
occurs near the middle of the honest ladder.

### Zeta size hierarchy

On the same audited zeta ladder:

```text
mean |gap_N|   ~ 0.01275,
mean |proxy_N| ~ 0.21188,
mean |alpha_N| ~ 0.21060.                                              (112-8)
```

Hence the gap is smaller than the proxy by roughly a factor of

```text
0.01275 / 0.21188 ~ 0.060.                                             (112-9)
```

This is the same content seen rowwise in E79.110 (`~6%` mean relative gap), now
expressed as a direct hierarchy of absolute scales:

```text
|gap_N| << |proxy_N| ~ |alpha_N|.                                      (112-10)
```

### Planted controls

For comparison, the planted crossings occur much earlier:

```text
plant_gamma1_beta030: between N=8 and 10,  N_cross ~ 9.59,
plant_gamma2_beta030: between N=10 and 12, N_cross ~ 11.63,            (112-11)
```

and at far larger absolute gap scales (E79.111).

So the honest zeta-side picture is distinguished not merely by "one crossing"
but by:

```text
mid-ladder crossing + genuinely secondary amplitude.                   (112-12)
```

## 4. Reading

This sharpens E79.111 one step further.

The current best proxy does not leave behind an arbitrary small error. On zeta
it leaves behind a remainder that:

```text
- stays one order of magnitude smaller than the proxy itself,
- crosses zero only once,
- does so near the middle of the audited ladder.                       (112-13)
```

That is a fairly rigid finite geometry.

## 5. Consequence

After E79.112, the residual-coherence branch can be summarized as:

```text
alpha_N
  = \left(1/\sqrt{outlier_fraction} - mesh_radius/second_abs\right)
    + tiny single-crossing remainder,                                  (112-14)
```

with the crossing localized near `N ~ 13.4` on the audited zeta ladder.

This is the sharpest finite form reached on this branch so far.
