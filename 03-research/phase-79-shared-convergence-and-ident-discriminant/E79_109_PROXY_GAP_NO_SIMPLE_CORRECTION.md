# E79.109 - The final proxy gap does not appear to admit a simple one-parameter correction

**Scope:** `DISCRIMINANT`, follow-up to E79.108.  
**Class:** AUTOPSIA FRANCA.  

## 1. Question

After E79.108, the sharpest finite proxy for the residual coefficient is

```text
proxy_N := 1/sqrt(outlier_fraction) - mesh_radius/second_abs,          (109-1)
```

equivalently

```text
proxy_N := spectral_reading/escape_ratio - mesh_radius/second_abs      (109-2)
```

up to the already-known outlier-lock defect.

The next obvious hope is that the remaining gap

```text
gap_N := alpha_N - proxy_N,                                            (109-3)
```

might itself be governed by one more simple scalar such as:

```text
(a) outlier_over_escape - 1,
(b) mesh_radius/second_abs,
(c) mean(d)/second_abs.                                                (109-4)
```

## 2. Audit

Using the certified E79.90 and E79.101 rows, compare `gap_N` against those three
candidate correction scales.

For zeta this means auditing:

```text
gap_N / (outlier_over_escape - 1),
gap_N / (mesh_radius/second_abs),
gap_N / (mean(d)/second_abs).                                          (109-5)
```

and checking whether any of these ratios stabilizes tightly enough to count as
an candid next reduction.

## 3. Result

### Zeta

On the audited zeta ladder:

```text
gap/lock-defect      mean ~ -0.20, std ~ 0.65,
gap/(mesh/second)    mean ~ -0.004, std ~ 0.153,
gap/(mean(d)/second) mean ~ -0.013, std ~ 0.512.                      (109-6)
```

The last two means are close to zero, but the spreads are far too large for a
credible scalar correction law. The sign also flips across the ladder.

So there is no evidence that the proxy gap is simply:

```text
constant * lock-defect,
constant * mesh_radius/second_abs,
or constant * mean(d)/second_abs.                                      (109-7)
```

### Planted controls

The planted controls are even less organized:

```text
plant_gamma1_beta030:
  gap/lock-defect      std ~ 0.50,
  gap/(mesh/second)    std ~ 0.19,
  gap/(mean(d)/second) std ~ 0.62;

plant_gamma2_beta030:
  gap/lock-defect      std ~ 3.40,
  gap/(mesh/second)    std ~ 0.55,
  gap/(mean(d)/second) std ~ 1.85.                                    (109-8)
```

So no simple correction law survives the cross-build audit either.

## 4. Reading

This is the candid stopping point for the current proxy-refinement thread.

E79.108 successfully collapsed the residual-coherence object to a single sharp
subtraction-shaped proxy. But E79.109 says the leftover error around that proxy
does **not** immediately collapse one step further to any obvious one-parameter
correction.

So the right lesson is:

```text
the proxy itself is real and sharp,
but its remaining gap is not yet governed by a simple scalar law.      (109-9)
```

## 5. Consequence

After E79.109, the candid live burden remains:

```text
explain why alpha_N nearly matches
  1/sqrt(outlier_fraction) - mesh_radius/second_abs
on zeta, while the planted controls do not,                            (109-10)
```

without pretending that the residual error has already been reduced to one more
elementary correction factor.
