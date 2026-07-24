# E78.79 - The normalized shell derivative is closer to an `N^{-1}` law than to a sigma law

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.78 reduced the radial coupling problem to the normalized integrand

```text
(-SAFEDELTA_N(i sigma)) / A_N.                          (WNS-1)
```

The next question is which normalization best organizes that quantity on the
audited zeta ladder.

This note audits the simplest candidates.

## 2. Probe comparison

Companion:

```text
E78_79_weighted_normalized_safedelta_probe.py
E78_79_weighted_normalized_safedelta_results.json
```

The probe compares:

```text
X_N(sigma)   := (-SAFEDELTA_N(i sigma)) / A_N,          (WNS-2)
N X_N(sigma),                                           (WNS-3)
sqrt(N) X_N(sigma),                                     (WNS-4)
X_N(sigma)/(sigma-sigma_0).                             (WNS-5)
```

on the common zeta ladder `sigma in {1.0,3.0}`, `N=8,10,12,14,16,18`.

## 3. Observed structure

The raw normalized integrand varies substantially:

```text
X_N(sigma)
  min    = 6.988e-3,
  median = 1.416e-2,
  max    = 4.004e-2.                                   (WNS-6)
```

and the sigma-normalized variants are worse.

By contrast, the weighted quantity `N X_N` is noticeably flatter:

```text
N X_N
  min    = 1.258e-1,
  median = 1.856e-1,
  max    = 3.203e-1,                                   (WNS-7)
```

with spread

```text
max/min ≈ 2.55,                                        (WNS-8)
```

compared with

```text
max/min ≈ 5.73                                          (WNS-9)
```

for the unweighted `X_N`.

Moreover the `N X_N` values are nearly sigma-stable row by row:

```text
sigma=1.0:
  0.3203, 0.2198, 0.2135, 0.1519, 0.1615, 0.1269

sigma=3.0:
  0.3067, 0.2126, 0.2097, 0.1494, 0.1599, 0.1258.      (WNS-10)
```

So the dominant variation is in `N`, not in `sigma`, and the first useful
flattening is exactly the `N` weight.

## 4. Consequence

This suggests the next honest reduced target:

```text
WEIGHTED-NORMALIZED-SAFEDELTA:
  prove N * (-SAFEDELTA_N(i sigma)) / A_N <= M(sigma)  (WNS-11)
```

on the safe axis.

Such a bound would imply

```text
(-SAFEDELTA_N(i sigma)) / A_N <= M(sigma) / N,         (WNS-12)
```

and therefore, by E78.78,

```text
TAIL_N(sigma_0,sigma) / A_N
 <= (1/2) ∫_{sigma_0}^{sigma} M(t)/N dt
 = O(1/N).                                             (WNS-13)
```

So the radial coupling front sharpens again:

```text
NORMALIZED-SAFEDELTA-AVERAGE
<=
WEIGHTED-NORMALIZED-SAFEDELTA.                         (WNS-14)
```

This is a genuine reduction because it replaces a two-variable average problem
with a pointwise weighted bound.

## 5. Honest reading

This note does not prove the `1/N` law. It only records that, among the obvious
normalizations, the `N`-weighted one is the first that behaves like a stable
candidate on the audited zeta ladder.

That matters because it rules out spending more time on the worse normalizations
`X_N/(sigma-sigma_0)` or `sqrt(N) X_N` as primary targets.

## 6. Status

```text
observed:
  the normalized derivative (-SAFEDELTA)/A is organized much better by the
  weight N than by sigma-based rescalings;

clarified:
  the next honest pointwise target is a weighted bound
  N*(-SAFEDELTA)/A <= M(sigma);

reduced:
  NORMALIZED-SAFEDELTA-AVERAGE to WEIGHTED-NORMALIZED-SAFEDELTA.
```
