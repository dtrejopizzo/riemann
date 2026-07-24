# E78.13 - Transfer growth versus t0 and 1-theta

**Run:** 2026-07-18.
**Scope:** IDENT transfer-scale geometry.

## 1. Purpose

E78.12 showed that zeta denominator amplification is dynamically driven by the
growth of `|T|`, while the planted build shrinks `|T|` and compensates through
`|1-theta|`.  This note asks whether the zeta growth of `|T|` itself reduces to
`|t0|`, or whether it remains a genuinely coupled `t0 * (1-theta)` product law.

## 2. Probe

Companion:

```text
E78_13_t0_vs_theta_probe.py
E78_13_t0_vs_theta_results.json
```

Using the exact identity

```text
T = t0 (1-theta),
```

the probe records across one step `N -> N+2`:

```text
|T_{N+2}| / |T_N|,
|t0_{N+2}| / |t0_N|,
|1-theta_{N+2}| / |1-theta_N|.
```

## 3. Status

## 3. Results

On the audited step `N=8 -> 10` at `lambda=6`, safe grid

```text
sigma in {0.55,0.6,0.75,1.0,1.5,2.0,3.0},
```

the factor ratios are:

### Zeta

```text
|T_{10}| / |T_8|              in [1.908, 2.027],
|t0_{10}| / |t0_8|            in [2.902, 2.924],
|1-theta_{10}| / |1-theta_8|  in [0.653, 0.698].
```

### Planted build

```text
|T_{10}| / |T_8|              in [0.261, 0.307],
|t0_{10}| / |t0_8|            in [0.0869, 0.0913],
|1-theta_{10}| / |1-theta_8|  in [2.996, 3.359].
```

The product law is exact to roundoff in the stored data.

## 4. Reading

This is the cleanest reduction so far.

In zeta:

```text
t0 is the growth driver:
  |t0| grows by almost a factor 3,
while |1-theta| shrinks by about a factor 0.67,
leaving net |T|-growth around a factor 2.
```

In the planted build:

```text
t0 collapses by roughly a factor 11,
while |1-theta| grows only by about a factor 3,
so |T| still shrinks strongly.
```

So the dynamic split is:

```text
t0 drives the geometry;
1-theta modulates it in the opposite direction.
```

That means the transfer-scale separation from E78.12 is not a genuinely
irreducible product law.  It is mostly a `t0` law with a controlled Schur-anchor
correction.

## 5. Consequence

The live shell-side geometry may now be sharpened to:

```text
T0-DRIVEN-TRANSFER:
the zeta build exhibits coherent growth of the core-anchor scale |t0|,
while the planted build exhibits collapse of |t0|; the factor 1-theta acts as
a secondary modulator rather than the main driver.
```

So the honest remaining interaction is:

```text
t0-growth
+ quotient defect Delta[T'/T]
+ controlled near-anchor correction from 1-theta.
```

This is a genuine reduction of the denominator geometry.

## 6. Status

```text
observed:
  the zeta transfer-scale growth is mainly driven by t0-growth, not by the
  Schur-anchor factor;

observed:
  the planted build shows the opposite t0 behavior (strong collapse), with
  |1-theta| unable to compensate;

reduced:
  TRANSFER-DRIVEN-DENOMINATOR to T0-DRIVEN-TRANSFER plus a controlled
  1-theta correction;

next:
  search for an exact shell law governing t0-growth and its interaction with
  Delta[T'/T].
```
