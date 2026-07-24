# E78.94 - `U-RADIAL-GAP` polarizes exactly into numerator gain plus denominator deficit

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.93 identified the primary modulus-growth target:

```text
U-RADIAL-GAP_N
 := |q_a,N| - |q_b,N|,                                  (GPL-1)
```

with

```text
q_a,N = theta'_N+2 / theta'_N,
q_b,N = (1-theta_N+2)/(1-theta_N).                      (GPL-2)
```

This note removes the last remaining quotient opacity from that target.

## 2. Exact polarization

Add and subtract `1`:

```text
|q_a,N| - |q_b,N|
 = (|q_a,N| - 1) + (1 - |q_b,N|).                       (GPL-3)
```

Define

```text
NUMERATOR-RADIAL-GAIN_N
 := |q_a,N| - 1,                                        (GPL-4)

DENOMINATOR-RADIAL-DEFICIT_N
 := 1 - |q_b,N|.                                        (GPL-5)
```

Then the primary modulus-growth object becomes exactly

```text
GAP-POLARIZATION:
U-RADIAL-GAP_N
 = NUMERATOR-RADIAL-GAIN_N
   + DENOMINATOR-RADIAL-DEFICIT_N.                      (GPL-6)
```

So positivity of the gap is exactly the competition between:

```text
numerator radial expansion (or loss),
denominator radial contraction.                         (GPL-7)
```

This is the smallest current exact decomposition of the growth law.

## 3. Probe audit

Companion:

```text
E78_94_gap_polarization_probe.py
E78_94_gap_polarization_results.json
```

### Exactness

The polarization reconstructs to roundoff for both builds:

```text
max reconstruction error < 1e-15.                       (GPL-8)
```

### Zeta

Across the certified zeta ladder:

```text
NUMERATOR-RADIAL-GAIN_N
  min    = -0.720711,
  median = -0.184924,
  max    =  0.615691,                                   (GPL-9)

DENOMINATOR-RADIAL-DEFICIT_N
  min    = 0.305398,
  median = 0.727095,
  max    = 0.874483,                                    (GPL-10)

U-RADIAL-GAP_N
  min    = 0.152534,
  median = 0.371460,
  max    = 0.921090.                                    (GPL-11)
```

So the denominator side is the orderly one.

On both audited sigma slices, the denominator deficit is strictly increasing
with `N`, while the numerator gain loses sign after the first two steps:

```text
sigma=1.0:
  numerator gain =  0.6157,  0.0653, -0.2065, -0.3970, -0.4962, -0.5999, -0.7207
  denominator deficit
                 =  0.3054,  0.5721,  0.6789,  0.7665,  0.8083,  0.8440,  0.8732

sigma=3.0:
  numerator gain =  0.5301,  0.0275, -0.2163, -0.3978, -0.5059, -0.5853, -0.6619
  denominator deficit
                 =  0.3474,  0.5892,  0.6877,  0.7712,  0.8112,  0.8458,  0.8745. (GPL-12)
```

Thus on the healthy branch the gap stays positive because the denominator
contraction eventually dominates the numerator loss.

### Planted build

The planted build does not preserve either coherent denominator deficit or
coherent balance:

```text
NUMERATOR-RADIAL-GAIN_N
  min    = 0.536624,
  median = 4.120114,
  max    = 86.535472,

DENOMINATOR-RADIAL-DEFICIT_N
  min    = -9.711255,
  median = -0.599001,
  max    = 0.425844.                                    (GPL-13)
```

In particular, the plant can have a large positive numerator gain while the
denominator fails to contract at all:

```text
sigma=1.0, N=12:
  numerator gain      = +2.743380
  denominator deficit = -3.651807
  gap                 = -0.908427.                      (GPL-14)
```

So the falsifier breaks exactly by destroying the denominator-contraction side
of the polarized gap law.

## 4. Consequence

This yields the sharpest current refinement of the primary target:

```text
DENOMINATOR-RADIAL-DEFICIT-LOWER-BOUND
+ NUMERATOR-RADIAL-GAIN-LOWER-BOUND
=> U-RADIAL-GAP-LOWER-BOUND.                            (GPL-15)
```

But the audit also shows which side is the real driver:

```text
PRIMARY:
  DENOMINATOR-RADIAL-DEFICIT,

SECONDARY:
  NUMERATOR-RADIAL-GAIN.                                (GPL-16)
```

The denominator deficit is the coherent monotone branch; the numerator gain is
the fluctuating correction.

## 5. Honest reading

This note does **not** yet prove a cofinal lower bound for the denominator
deficit or the numerator gain.

What it proves is that the primary modulus-growth target has now been reduced
to the exact competition of two one-dimensional shell scalars, and that the
denominator side is the structurally stable one on the certified zeta ladder.

That is a real narrowing of the burden.

## 6. Status

```text
proved:
  U-RADIAL-GAP_N = (|q_a,N|-1) + (1-|q_b,N|) exactly;

proved:
  the polarization reconstructs to roundoff for both builds;

observed:
  on the certified zeta ladder the denominator radial deficit is the coherent
  monotone part, while the numerator gain changes sign after the first steps;

observed:
  the planted falsifier breaks the polarized law by losing denominator
  contraction, not merely by changing the numerator gain;

clarified:
  the primary live modulus-growth target has sharpened further to the
  denominator radial deficit, with numerator radial gain demoted to a
  correction term;

next:
  re-import the denominator radial contraction laws (E78.47-E78.50) as the
  primary source of U-RADIAL-GAP-LOWER-BOUND, and only then quantify the
  numerator correction.
```
