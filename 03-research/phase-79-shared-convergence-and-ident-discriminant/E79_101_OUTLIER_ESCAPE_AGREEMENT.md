# E79.101 - The outlier/escape agreement survives the long zeta ladder

**Scope:** `DISCRIMINANT`, continuation of the shared-ladder spectral reading.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the zeta-side
agreement

```text
escape_scale ~= outlier_abs                                              (101-1)
```

is not confined to the shared subladder `N=8,10,12`.  It survives the audited
long ladder through `N=18`.

## 0. Why this check matters

E79.100 gave the first direct spectral reading of the live escape-outlier object,
but only on the overlap of the certified artifacts:

```text
N = 8, 10, 12.                                                         (101-2)
```

That left an obvious uncertainty:

```text
is the near-identity escape_scale ~= outlier_abs a genuine zeta-side regime,
or just a short-ladder coincidence?                                     (101-3)
```

This note answers that directly by extending only the minimal cloud audit needed
for that comparison.

## 1. Probe

Companion files:

```text
E79_101_outlier_escape_agreement_probe.py
E79_101_outlier_escape_agreement_results.json
```

The probe recomputes, on the standard three builds and the long audited ladder

```text
N = 8, 10, 12, 14, 16, 18,   dps = 60,                                 (101-4)
```

the minimal spectral package:

```text
outlier_abs,
second_abs,
escape_scale = |q^T x|/|c|,
mesh_radius.                                                            (101-5)
```

The main audit quantity is

```text
outlier_abs / escape_scale.                                             (101-6)
```

## 2. Result

### Zeta

On the long zeta ladder:

```text
outlier_abs / escape_scale
= 1.0136, 1.0205, 1.0179, 1.0246, 1.0224, 1.0296.                     (101-7)
```

So the agreement not only survives but stays extremely rigid:

```text
about 1.4% .. 3.0% relative error across N=8..18.                      (101-8)
```

That is strong enough to upgrade E79.100's reading from "shared-ladder only" to
"audited long zeta ladder".

### Planted controls

The planted controls remain qualitatively different.

For `plant gamma1`:

```text
outlier_abs / escape_scale
= 1.50, 1.08, 1.22, 1.27, 1.23, 1.17.                                 (101-9)
```

For `plant gamma2`:

```text
outlier_abs / escape_scale
= 1.16, 6.14, 1.04, 1.30, 1.32, 1.33.                                 (101-10)
```

So the long-ladder rigidity is still a zeta-side feature, not a generic property
of the finite package.

## 3. Reading

This sharpens the live object one more time.

After E79.99 the active object was

```text
escape_ratio / sqrt(outlier_fraction).                                 (101-11)
```

After E79.100 we knew that, on `N=8,10,12`, this already had the spectral reading

```text
sqrt(outlier_abs * second_abs) / mesh_radius.                          (101-12)
```

E79.101 extends that reading to the whole audited zeta ladder:

```text
on zeta, the rank-one escape scale is already the farthest spectral outlier of
K_N, to within a few percent, through N=18.                            (101-13)
```

So the live object is no longer merely a partial reading.  On the audited zeta
ladder it is genuinely spectral.

## 4. Consequence

After E79.101, the honest live burden sharpens to:

```text
explain why the zeta-side rank-one escape scale locks onto the actual farthest
spectral outlier of K_N, while the planted builds do not,               (101-14)
```

and therefore why

```text
escape_ratio / sqrt(outlier_fraction)
~= sqrt(outlier_abs * second_abs) / mesh_radius                        (101-15)
```

holds across the audited zeta ladder.

That is a materially stronger and more spectral target than the algebraic form
we had before.

## 5. Status

```text
proved by long-ladder audit:
  on zeta, outlier_abs / escape_scale stays in the narrow band
  1.0136 .. 1.0296 across N=8..18;

proved by long-ladder audit:
  the planted controls do not share that rigidity;

upgraded:
  the E79.100 spectral reading from the shared subladder to the audited long
  zeta ladder;

reduced:
  the live burden to explaining the zeta-side lock
    escape_scale ~= outlier_abs.
```
