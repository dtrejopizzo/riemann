# E78.10 - Numerator-defect reduction of W-QUOTIENT-DELTA

**Run:** 2026-07-18.
**Scope:** IDENT, fixed-L finite front.

## 1. Purpose

E78.9 showed that the invariant quotient-delta is not governed by one term
alone: in zeta it comes from a strong signed cancellation between a linear and a
mixed term. This note repackages that cancellation into a single exact
numerator-defect object.

## 2. Exact identity

With the notation of E78.9, let

```text
q_N = W_N'/(1+W_N),        q_M = W_M'/(1+W_M),              (ND-1)
```

for one step `N -> N+2` at one safe point `z=i sigma`.

Then

```text
q_N - q_M
= [Delta W' - q_M Delta W] / (1+W_N).                      (ND-2)
```

### Proof

Starting from

```text
q_N - q_M
= Delta W'/(1+W_N)
 -W_M' Delta W / ((1+W_N)(1+W_M))                          (ND-3)
```

from E78.9, factor `1/(1+W_N)` and use

```text
q_M = W_M'/(1+W_M).
```

Then

```text
q_N - q_M
= [Delta W' - q_M Delta W]/(1+W_N),
```

which is `(ND-2)`.  QED.

## 3. Consequence

Because E78.8 already audited `|1+W_N|` as safely nonzero on the tested ladder,
the live fixed-L object reduces from the full quotient-delta to the numerator

```text
NUMERATOR-DEFECT:
  Delta W' - q_M Delta W.                                  (ND-4)
```

This is strictly smaller than the two-term representation from E78.9: the
signed cancellation is now packaged into one exact finite quantity.

## 4. Probe

Companion:

```text
E78_10_w_numerator_defect_probe.py
E78_10_w_numerator_defect_results.json
```

The probe verifies `(ND-2)` directly.

## 5. Status

## 5. Audit

On the first cheap certified step `N=8 -> 10` at `lambda=6`, safe grid

```text
sigma in {0.55,0.6,0.75,1.0,1.5,2.0,3.0},
```

the probe gives:

### Zeta

```text
max |Q_delta|         = 4.58e-2
max |NUMERATOR-DEFECT|= 3.66e5
min |1+W_N|           = 7.10e5
reconstruction        = 5.30e-61.
```

### Planted build

```text
max |Q_delta|         = 5.32e-1
max |NUMERATOR-DEFECT|= 1.28e1
min |1+W_N|           = 2.05e1
reconstruction        = 5.50e-62.
```

So `(ND-2)` is numerically certified, but the two builds show opposite scales in
the numerator:

```text
zeta:   huge numerator defect, huge denominator, small quotient;
plant:  moderate numerator defect, moderate denominator, moderate quotient.
```

## 6. Reading

This is a useful correction.  `NUMERATOR-DEFECT` is an exact reparametrization
of the live front, but it is **not** yet a smaller forcing object by size.

In particular:

```text
1. the small zeta quotient-delta does not come from a small numerator defect;
2. it comes from a large numerator defect divided by an even larger safe
   denominator;
3. the plant does not share that same large-scale geometry.
```

So the right conclusion is:

```text
NUMERATOR-DEFECT is structurally useful,
but not a standalone smallness target.
```

It names the exact quantity that must be related to the shell algebra, but the
live forcing statement still has to be expressed at the quotient level, with the
healthy denominator kept in the picture.

## 7. Consequence

The honest frontier is now:

```text
QUOTIENT-DEFECT-GEOMETRY:
understand the exact relation between

  NUMERATOR-DEFECT = Delta W' - q_M Delta W

and the large denominator 1+W_N that turns it into the small zeta
W-QUOTIENT-DELTA.
```

So `NUMERATOR-DEFECT` should be kept as an exact internal coordinate, not yet as
the exposed live endpoint.

## 8. Status

```text
proved:
  exact numerator-defect representation
    q_N-q_M = [Delta W' - q_M Delta W]/(1+W_N);

observed:
  the zeta numerator defect is very large on the tested step, but the
  denominator is larger still, yielding a small quotient-delta;

observed:
  the planted build has a much smaller denominator and a moderate numerator
  defect, yielding an order-one quotient-delta;

clarified:
  NUMERATOR-DEFECT is a structurally useful reparametrization, but not yet a
  smaller smallness target than W-QUOTIENT-DELTA itself;

next:
  search the shell/two-generator algebra for the exact geometric relation
  between the large numerator and the even larger zeta denominator.
```
