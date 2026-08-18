# E79.106 - The second-scale coefficient does not inherit from any obvious one-scalar formula

**Scope:** `DISCRIMINANT`, follow-up to E79.105.  
**Class:** AUTOPSIA FRANCA.  

## 1. Question

E79.105 showed that on the audited zeta ladder

```text
outlier_abs ~= escape_scale + mean(d) + alpha second_abs,              (106-1)
```

with a remarkably rigid empirical coefficient `alpha`.

The immediate next question is whether this `alpha` is already inherited from
some simpler scalar we had previously certified, or whether it is genuinely a
new two-scale object.

Write

```text
alpha_N := [outlier_abs - escape_scale - mean(d)] / second_abs.        (106-2)
```

On the zeta ladder E79.105 found

```text
alpha_N = 0.1556, 0.1946, 0.1811, 0.2304, 0.2459, 0.2561.              (106-3)
```

## 2. Audit set

Using only the already certified E79.90 and E79.101 rows, audit the most
obvious inherited candidates:

```text
(a) 1/outlier_fraction,
(b) mean(d)/second_abs,
(c) mesh_radius/second_abs,
(d) spectral_reading/escape_ratio,
(e) spectral_reading/escape_ratio - mesh_radius/second_abs,
(f) 1/sqrt(outlier_fraction).                                          (106-4)
```

The point is not to fit.  The point is to test whether any previously natural
one-scalar expression already *is* `alpha_N`, or at least tracks it tightly
enough to count as an inherited object.

## 3. Result

### Zeta

Mean absolute errors against `alpha_N` on the audited zeta ladder are:

```text
1/outlier_fraction                                 ~ 0.120,
mean(d)/second_abs                                 ~ 0.184,
mesh_radius/second_abs                             ~ 0.122,
spectral_reading/escape_ratio                      ~ 0.096,
1/sqrt(outlier_fraction)                           ~ 0.090,
spectral_reading/escape_ratio - mesh_radius/second_abs
                                                   ~ 0.011.            (106-5)
```

So:

1. none of the obvious one-scalar candidates is close;
2. the only candidate that gets near `alpha_N` is already a genuinely composite
   two-scale expression.

### Planted controls

That same best composite candidate

```text
spectral_reading/escape_ratio - mesh_radius/second_abs                 (106-6)
```

still fails badly on the planted controls:

```text
plant_gamma1_beta030: mean abs error ~ 0.309, max ~ 0.518,
plant_gamma2_beta030: mean abs error ~ 1.043, max ~ 4.274.            (106-7)
```

So even the near-match on zeta should not be read as a trivial identity of the
finite package.

## 4. Reading

This is the candid outcome we needed before pushing E79.105 further.

The E79.105 coefficient is **not** inherited from any simple pre-existing scalar
such as:

```text
1/outlier_fraction,
mesh_radius/second_abs,
spectral_reading/escape_ratio,
1/sqrt(outlier_fraction).                                              (106-8)
```

The only reasonably close candidate on zeta already mixes two scales:

```text
spectral_reading/escape_ratio - mesh_radius/second_abs,                (106-9)
```

and even that is not uniform across builds.

So the correct lesson is not "we found the canonical closed formula for
alpha_N", but the opposite:

```text
alpha_N remains a genuinely two-scale zeta-side coherence object.      (106-10)
```

## 5. Consequence

After E79.106, the next candid target is **not** to promote an accidental
one-scalar proxy into a theorem target.

The live burden stays where E79.105 put it:

```text
explain why the residual after escape_scale + mean(d)
lines up coherently with second_abs on zeta,
while the planted controls lose that coherence.                        (106-11)
```

The new autopsy just tells us that this alignment does not collapse to any of
the most obvious inherited scalars.  So the object is smaller than the raw
outlier lock, but not yet reducible to a simpler one-scale invariant.
