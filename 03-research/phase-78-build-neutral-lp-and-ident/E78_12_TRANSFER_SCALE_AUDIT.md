# E78.12 - Transfer-scale amplification audit

**Run:** 2026-07-18.
**Scope:** IDENT geometry on the fixed-L finite front.

## 1. Purpose

E78.11 showed that the huge zeta denominator `1+W` is carried mainly by the
transfer scale `|T|`, not by a large `|1-theta|`.  This note audits how those
two factors move across one consecutive section step.

## 2. Probe

Companion:

```text
E78_12_transfer_scale_probe.py
E78_12_transfer_scale_results.json
```

The probe uses the exact common-core transfer packet and records, for each safe
sample point and each step `N -> N+2`,

```text
|T_{N+2}| / |T_N|,
|1-theta_{N+2}| / |1-theta_N|.
```

## 3. Status

## 3. Results

On the short audited step `N=8 -> 10` at `lambda=6`, safe grid

```text
sigma in {0.55,0.6,0.75,1.0,1.5,2.0,3.0},
```

the factor ratios are:

### Zeta

```text
|T_{10}| / |T_8|              in [1.908, 2.027],
|1-theta_{10}| / |1-theta_8|  in [0.653, 0.698].
```

### Planted build

```text
|T_{10}| / |T_8|              in [0.261, 0.307],
|1-theta_{10}| / |1-theta_8|  in [2.996, 3.359].
```

## 4. Reading

This is a clean geometric split.

In the zeta build:

```text
the transfer scale T grows by about a factor 2,
while |1-theta| shrinks by about a factor 0.67.
```

So the denominator amplification is dynamically driven by `T`; the Schur-anchor
factor `1-theta` moderates the growth rather than causing it.

In the planted build the opposite happens:

```text
T shrinks strongly,
while |1-theta| grows by about a factor 3.
```

Thus the product law is still exact, but the **driver** is different in the two
builds.

## 5. Consequence

This allows a sharper reduction of the live geometry:

```text
TRANSFER-DRIVEN-DENOMINATOR:
on the zeta safe ladder, the amplification of 1+W is carried primarily by the
transfer scale T, with 1-theta staying in a controlled near-anchor regime.
```

So the honest open interaction is now:

```text
large transfer scale T
+ quotient defect Delta[T'/T]
+ controlled near-anchor factor 1-theta.
```

This is smaller and more directional than the raw product geometry from E78.11.

## 6. Status

```text
observed:
  zeta denominator amplification is dynamically driven by growth of |T|, not by
  growth of |1-theta|;

observed:
  planted build shows the opposite geometry: shrinking |T| and expanding
  |1-theta|;

reduced:
  the live denominator geometry to TRANSFER-DRIVEN-DENOMINATOR plus the
  quotient defect;

next:
  search for an exact shell law governing the zeta transfer-scale growth and its
  interaction with Delta[T'/T].
```
