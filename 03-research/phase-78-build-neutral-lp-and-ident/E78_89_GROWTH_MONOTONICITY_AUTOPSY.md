# E78.89 - The isolated growth quotient is not the right sigma-monotone target

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.88 showed that

```text
MODULUS-QUOTIENT_N(sigma)
 = GROWTH-QUOTIENT_N(sigma) * SECTOR-FACTOR_N(sigma),   (GMA-1)
```

with the exact `1/N` scale exposed. A natural next hope would be:

```text
prove sigma monotonicity on GROWTH-QUOTIENT_N itself,   (GMA-2)
```

and treat the sector factor as secondary bookkeeping.

This note audits that hope directly.

## 2. Exact comparison target

From E78.88,

```text
N * MODULUS-QUOTIENT_N(sigma)
 = GROWTH-QUOTIENT_N(sigma) / s_N+2,                    (GMA-3)
```

where

```text
s_N+2 = Im(u_N+2)/|u_N+2|.                              (GMA-4)
```

So if `GROWTH-QUOTIENT_N(sigma)` were sigma-decreasing, it would supply the
cleanest possible route to the modulus side.

The question is whether that statement is actually true on the certified
ladder.

## 3. Probe audit

Companion:

```text
E78_89_growth_monotonicity_autopsy_probe.py
E78_89_growth_monotonicity_autopsy_results.json
```

The probe compares the `sigma=1.0` and `sigma=3.0` rows from the exact
E78.88 split.

### Growth quotient

The hoped-for monotonicity fails on the current certified ladder:

```text
N=16:   G(3.0) - G(1.0) = +0.0033501
N=18:   G(3.0) - G(1.0) = +0.0462274.                   (GMA-5)
```

So the isolated growth quotient is **not** uniformly sigma-decreasing.

Representative full table:

```text
N= 8:  G(1.0)=2.556047, G(3.0)=2.452517
N=12:  G(1.0)=2.572961, G(3.0)=2.517969
N=16:  G(1.0)=2.552030, G(3.0)=2.555380
N=18:  G(1.0)=2.209486, G(3.0)=2.255713
N=20:  G(1.0)=2.179983, G(3.0)=1.928708.               (GMA-6)
```

The sign changes in `(GMA-5)` are enough to kill the monotonicity target as a
theorem candidate.

### Weighted modulus quotient

By contrast, the weighted modulus quotient from E78.88,

```text
W_N(sigma) := N * MODULUS-QUOTIENT_N(sigma),            (GMA-7)
```

remains sigma-decreasing on the same ladder, because E78.87 already proved the
unweighted modulus quotient is sigma-decreasing on every audited pair.

So the growth split does **not** sharpen the monotonicity front; it only
explains the scale.

## 4. Consequence

This is an candid autopsy:

```text
SIGMA-MONOTONE-GROWTH-QUOTIENT  -- REFUTED on the certified ladder. (GMA-8)
```

The exact split from E78.88 is still useful, but only in the following sense:

```text
1. it explains the explicit 1/N scale of MODULUS-QUOTIENT;
2. it localizes the remaining O(1) burden to GROWTH-QUOTIENT;
3. it does not provide a better sigma-monotone target than the already-audited
   weighted modulus quotient W_N.                        (GMA-9)
```

So the live monotonicity object stays

```text
W_N(sigma) = N * MODULUS-QUOTIENT_N(sigma),             (GMA-10)
```

not the isolated growth quotient.

## 5. Reduced target

The exact implication now is:

```text
LEFT-ENDPOINT-WEIGHTED-MODULUS-QUOTIENT
+ SIGMA-MONOTONE-WEIGHTED-MODULUS-QUOTIENT
=> MODULUS-QUOTIENT.                                    (GMA-11)
```

Here

```text
WEIGHTED-MODULUS-QUOTIENT:
  W_N(sigma) := N * (-SAFEDELTA_N(i sigma)) / modulus_term_N. (GMA-12)
```

This is equivalent to the modulus quotient up to the exact explicit factor
`1/N`, and it preserves the observed monotone direction on the current ladder.

That is strictly better than chasing a false monotonicity on `GROWTH-QUOTIENT`.

## 6. Candid reading

This note does **not** prove the weighted modulus quotient theorem cofinally.

What it proves is that the most tempting post-E78.88 sharpening is wrong:
growth quotient monotonicity already fails on the certified zeta ladder.

That matters because it prevents a fresh detector spiral around the wrong
auxiliary object.

## 7. Status

```text
refuted:
  SIGMA-MONOTONE-GROWTH-QUOTIENT is false on the current certified ladder;

proved:
  the growth/sector split from E78.88 still explains the scale but not the
  monotone direction;

clarified:
  the live monotonicity object remains the weighted modulus quotient
  W_N(sigma)=N*MODULUS-QUOTIENT_N(sigma);

reduced:
  the modulus-side monotonicity branch to
  SIGMA-MONOTONE-WEIGHTED-MODULUS-QUOTIENT plus
  LEFT-ENDPOINT-WEIGHTED-MODULUS-QUOTIENT;

next:
  attack the weighted modulus quotient directly at the left endpoint, using
  the exact quotient law rather than the false growth-monotonicity target.
```
