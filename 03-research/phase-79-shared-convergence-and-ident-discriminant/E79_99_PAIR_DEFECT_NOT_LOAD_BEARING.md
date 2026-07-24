# E79.99 - The E79.97 law is not being carried by mean pair defect; the live burden sharpens to escape-outlier coupling

**Scope:** `DISCRIMINANT`, post-E79.97/E79.98 decomposition of the square-root law.  
**Class:** AUTOPSIA HONESTA + sharper replacement target.  
**What we know after this document that we did not know before:** the zeta-side
square-root law from E79.97 is **not** primarily being carried by the internal
pair-defect factor. The planted main control can have pair defect as small as,
or smaller than, zeta while remaining far outside the zeta-side escape regime.

## 0. Why this check is necessary

E79.97 found the coupled law

```text
escape_ratio * sqrt(D_N) ~ const_zeta,                                 (99-1)
```

and E79.88 / E79.86 already give the exact identity

```text
D_N = mean_pair_defect / outlier_fraction.                             (99-2)
```

So the law rewrites exactly as

```text
escape_ratio * sqrt(mean_pair_defect / outlier_fraction) ~ const_zeta, (99-3)
```

or equivalently

```text
escape_ratio / sqrt(outlier_fraction)
  ~ const_zeta / sqrt(mean_pair_defect).                               (99-4)
```

Before treating this as a new primitive invariant, we have to decide which side
is actually carrying the discriminating burden:

```text
is it the smallness of mean_pair_defect,
or the coupling between escape and outlier separation?                 (99-5)
```

## 1. Evidence used

No new build is needed.  This note reads the already certified long-ladder data
from

```text
E79_90_escape_balance_split_results.json.                              (99-6)
```

The two derived quantities of interest are:

```text
A_N := mean_pair_defect,                                               (99-7)
B_N := escape_ratio / sqrt(outlier_fraction).                          (99-8)
```

## 2. The key counterpattern

The planted main control already refutes the idea that pair defect is the
load-bearing piece.

On the zeta ladder,

```text
mean_pair_defect ~ 0.0178, 0.0178, 0.0141, 0.0159, 0.0151, 0.0138.     (99-9)
```

But on the planted main control, the tail rows are **even smaller**:

```text
N=14:  mean_pair_defect ~ 0.00925,
N=16:  mean_pair_defect ~ 0.00889,
N=18:  mean_pair_defect ~ 0.00678.                                    (99-10)
```

So by the internal-cloud-defect metric alone, those planted rows look at least
as good as zeta.

Yet they remain far outside the zeta-side escape regime:

```text
zeta:   escape_ratio ~ 115 .. 134,
plant:  escape_ratio ~ 1.09 .. 1.43 on the same tail range.           (99-11)
```

Therefore:

```text
small mean_pair_defect is not the load-bearing reason for E79.97.      (99-12)
```

## 3. What survives after removing the pair-defect burden

Once the pair-defect side is demoted, the surviving object is the outlier side
coupled to escape:

```text
B_N = escape_ratio / sqrt(outlier_fraction).                           (99-13)
```

On the audited zeta ladder this is already fairly rigid:

```text
36.08, 34.52, 37.88, 36.98, 38.33, 39.26,                             (99-14)
```

with relative spread about

```text
12.8%.                                                                 (99-15)
```

By contrast, the planted controls stay tiny or erratic:

```text
plant gamma1:  0.70, 1.32, 1.19, 1.08, 1.19, 1.23,
plant gamma2:  2.47, 0.18, 0.98, 1.02, 1.11, 1.13.                    (99-16)
```

So after dividing out the outlier scale only partially, the zeta-side regime is
still separated from both planted controls by more than an order of magnitude.

## 4. Reading

This tells us something structurally important about E79.97.

The square-root law is **not** saying:

```text
large escape + tiny internal pair defect.                              (99-17)
```

because the planted main control can match or beat zeta on pair defect and yet
does not come close to the zeta coupling.

What the law is really localizing is:

```text
large escape matched to strong outlier separation.                      (99-18)
```

with the pair-defect factor acting more like a mild renormalization than the
primary source of separation.

So the live burden sharpens again:

```text
the discriminating content of E79.97 sits chiefly in the escape-outlier
coupling, not in the pair-defect term by itself.                       (99-19)
```

## 5. Consequence

After E79.99, the honest next target is no longer

```text
derive the square-root law from generic small pair defect.             (99-20)
```

It is:

```text
explain the zeta-side regime of
  escape_ratio / sqrt(outlier_fraction),                               (99-21)
```

or find the first audited obstruction to treating that quantity as the next
primitive finite invariant.

That is a smaller and more load-bearing object than the full E79.97 law.

## 6. Status

```text
proved by audit:
  the planted main control attains pair defects as small as or smaller than
  zeta on the tail rows while remaining far outside the zeta escape regime;

refuted:
  mean_pair_defect as the primary load-bearing source of the E79.97 law;

reduced:
  the live burden from the full square-root coupling to the sharper
  escape-outlier object escape_ratio / sqrt(outlier_fraction);

open:
  determine whether that escape-outlier coupling follows from CLOSE plus the
  rank-one mechanism, or whether it should be promoted to the next primitive
  finite invariant.
```
