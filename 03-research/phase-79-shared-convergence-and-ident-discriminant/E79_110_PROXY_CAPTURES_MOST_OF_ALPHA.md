# E79.110 - The subtraction proxy captures most of the zeta residual coefficient

**Scope:** `DISCRIMINANT`, continuation of E79.108-E79.109.  
**Class:** REDUCCION GENUINA.  

## 1. Why this note is worth writing

E79.108 isolated the sharp proxy

```text
proxy_N := 1/sqrt(outlier_fraction) - mesh_radius/second_abs,          (110-1)
```

and E79.109 showed that its leftover gap does not collapse to any obvious
one-parameter correction.

But there is still a quantitative question that matters for the shape of the
frontier:

```text
even if the remaining gap has no simple scalar law, does proxy_N already
capture most of alpha_N on the candid zeta ladder?                     (110-2)
```

If yes, then the subtraction proxy is not only the sharpest candidate in a
qualitative sense; it is already the dominant quantitative component.

## 2. Audit

Using the certified E79.90 and E79.101 rows, compare

```text
alpha_N := [outlier_abs - escape_scale - mean(d)] / second_abs,        (110-3)
proxy_N := 1/sqrt(outlier_fraction) - mesh_radius/second_abs,          (110-4)
gap_N   := alpha_N - proxy_N.                                          (110-5)
```

The key normalized quantity is

```text
gap_N / alpha_N,                                                       (110-6)
```

equivalently `proxy_N / alpha_N = 1 - gap_N/alpha_N`.

## 3. Result

### Zeta

On the audited zeta ladder:

```text
N=8:   gap/alpha = -0.0694,   proxy/alpha = 1.0694,
N=10:  gap/alpha = -0.0555,   proxy/alpha = 1.0555,
N=12:  gap/alpha = -0.1130,   proxy/alpha = 1.1130,
N=14:  gap/alpha = +0.0371,   proxy/alpha = 0.9629,
N=16:  gap/alpha = +0.0579,   proxy/alpha = 0.9421,
N=18:  gap/alpha = +0.0455,   proxy/alpha = 0.9545.                   (110-7)
```

So:

```text
mean |gap/alpha| ~ 6.3%,
max  |gap/alpha| ~ 11.3%.                                              (110-8)
```

Equivalently, the proxy already captures about

```text
94% .. 111% of alpha_N on the audited zeta ladder.                     (110-9)
```

That is much stronger than merely saying that the proxy is the best candidate in
the family. It says the subtraction proxy already carries almost the whole
zeta-side residual signal.

### Planted controls

The same normalized check fails badly on the planted controls.

For `plant_gamma1_beta030`:

```text
mean |gap/alpha| ~ 31.4,   max ~ 137.5,                               (110-10)
```

with several rows where even the sign of `proxy_N` disagrees with `alpha_N`.

For `plant_gamma2_beta030`:

```text
mean |gap/alpha| ~ 1.10,   max ~ 1.79.                                 (110-11)
```

So the subtraction proxy is not merely imperfect off the candid ladder; it
ceases to be a dominant approximation at all.

## 4. Reading

This sharpens the live object once more.

The subtraction-shaped proxy from E79.108 is not just the cleanest candidate
left standing. On zeta it already explains almost all of the residual
coefficient:

```text
alpha_N
  = proxy_N + small relative remainder,                                (110-12)
```

with the remainder only at the `O(10^-1)` relative scale on the whole audited
ladder.

The planted controls do not share that regime. So the candid content is now
more focused:

```text
why does the zeta-side coefficient enter the regime
  alpha_N ~= 1/sqrt(outlier_fraction) - mesh_radius/second_abs,
with only a small relative remainder, while the planted controls do not? (110-13)
```

## 5. Consequence

After E79.110, the subtraction proxy should be regarded as the current
load-bearing finite approximation to the residual coefficient. The remaining gap
is still live, but it is now clearly secondary on the candid ladder rather than
comparable in size.
