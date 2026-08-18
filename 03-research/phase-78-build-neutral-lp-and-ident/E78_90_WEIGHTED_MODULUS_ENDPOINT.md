# E78.90 - The candid endpoint target is a constant envelope for the weighted modulus quotient

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front, left endpoint slice `sigma=1.0`.

## 1. Purpose

E78.89 killed the false sharpening

```text
SIGMA-MONOTONE-GROWTH-QUOTIENT.                         (WME-1)
```

So the live modulus-side endpoint object is now

```text
W_N(1.0)
 := N * MODULUS-QUOTIENT_N(1.0).                        (WME-2)
```

This note asks two concrete questions:

```text
1. Does W_N(1.0) itself stay in a narrow audited band?
2. Is it already explained by the previously isolated radial scales
   A_N, BASE_N, TAIL_N/BASE_N?                          (WME-3)
```

The first would give the correct endpoint theorem candidate. The second would
offer a further reduction if true.

## 2. Probe audit

Companion:

```text
E78_90_weighted_modulus_endpoint_probe.py
E78_90_weighted_modulus_endpoint_results.json
```

The probe uses the exact weighted modulus rows from E78.88 on the left endpoint
slice `sigma=1.0`, and compares them against the common radial scales from
E78.77 wherever those are available (`N <= 18`).

### Endpoint band

Across the full currently certified left endpoint ladder `N=8,...,20`:

```text
W_N(1.0)
  min    = 2.152695,
  median = 2.361624,
  max    = 2.586236.                                   (WME-4)
```

The worst currently certified row is

```text
N=12:
  W_12(1.0) = 2.5862363964104347.                      (WME-5)
```

So the endpoint weighted modulus quotient is already compatible with the flat
audited envelope

```text
W_N(1.0) <= 2.59.                                      (WME-6)
```

That is the cleanest theorem candidate presently visible on this branch.

### Radial autopsy on the common ladder

On the common ladder `N=8,...,18`, the correlations with the radial comparison
objects from E78.77 are weak or misaligned:

```text
corr(W_N(1.0), A_N)         ≈  0.120,
corr(W_N(1.0), BASE_N)      ≈ -0.149,
corr(W_N(1.0), TAIL_N/A_N)  ≈  0.293,
corr(W_N(1.0), A_N/BASE_N)  ≈  0.582,
corr(W_N(1.0), TAIL_N/BASE) ≈  0.437.                 (WME-7)
```

So none of the currently isolated radial scales explains the endpoint weighted
modulus quotient in a way strong enough to justify a direct transfer theorem.

That is an candid negative result: the endpoint modulus object is not just a
relabeling of the reserve-budget scales.

## 3. Consequence

This yields the correct reduced endpoint target:

```text
LEFT-ENDPOINT-WEIGHTED-MODULUS-QUOTIENT:
  W_N(1.0) <= C_*.                                      (WME-8)
```

Combined with the live monotonicity object from E78.89,

```text
SIGMA-MONOTONE-WEIGHTED-MODULUS-QUOTIENT
+ LEFT-ENDPOINT-WEIGHTED-MODULUS-QUOTIENT
=> MODULUS-QUOTIENT
=> SECTOR-SIZE-QUOTIENT.                               (WME-9)
```

And on current evidence the most economical candidate is simply

```text
C_* = 2.59.                                             (WME-10)
```

The common-ladder radial comparison is therefore demoted to an autopsy, not a
mechanism.

## 4. Candid reading

This note does **not** prove the endpoint bound cofinally.

What it does prove is:

```text
1. the left-endpoint weighted modulus quotient already lives in a narrow
   audited constant band;
2. the obvious transfer to A_N / BASE_N / TAIL_N scales is not justified by
   the current evidence.                                (WME-11)
```

That is enough to prevent another false reduction and to state the next burden
in the cleanest possible way.

## 5. Status

```text
observed:
  the left-endpoint weighted modulus quotient stays in the audited band
  [2.152695, 2.586236] through N=20;

observed:
  the current worst row is W_12(1.0)=2.5862363964104347;

autopsied:
  the previously isolated radial scales from E78.77 do not explain the
  endpoint weighted modulus quotient strongly enough to support a direct
  transfer theorem;

reduced:
  the modulus-side endpoint burden to the explicit constant-envelope target
  W_N(1.0) <= C_*;

next:
  seek an exact finite expression for W_N(1.0) that is more intrinsic than the
  reserve-budget scales, or prove the constant envelope directly on the cofinal
  path.
```
