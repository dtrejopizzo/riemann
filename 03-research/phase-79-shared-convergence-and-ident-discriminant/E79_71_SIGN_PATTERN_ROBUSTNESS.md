# E79.71 - The E79.70 sign pattern lives on a real local region, not a single coefficient point

**Scope:** `GAP-Z` only, robustness audit for the penalized selector of E79.70.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the linear
selector of E79.70 is not a single fragile coefficient accident. In a local box
around the discovered coefficients, there is a nontrivial region of exact `5/5`
solutions, and they preserve the same sign pattern:

```text
cardinality  negative,
span         positive,
gaps         negative,
start        positive.                                                  (71-1)
```

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the audited tiny family from E79.70.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Why this check matters

E79.70 found one exact selector:

```text
score = mismatch
        - 1.00 card
        + 0.78 span
        - 0.64 gaps
        + 0.36 start.                                                   (71-2)
```

That was enough to resolve the audited branch ambiguity, but not enough to know
whether the selector was meaningful or just one lucky coefficient tuple.

The candid next question is therefore:

```text
does the selector live in a stable local region,
or only at one numerically tuned point?                                 (71-3)
```

## 2. Probe

Companion files:

```text
E79_71_SIGN_PATTERN_ROBUSTNESS_probe.py
E79_71_sign_pattern_robustness_results.json
```

The probe reuses the E79.70 candidate family and scans a coefficient box around
the discovered values:

```text
cardinality in [-1.30, -0.70],
span        in [ 0.55,  1.00],
gaps        in [-0.90, -0.40],
start       in [ 0.15,  0.55],                                         (71-4)
```

with step `0.05`, keeping the mismatch coefficient fixed at `1`.

For each point, it records:

```text
1. exact audited recovery count,
2. the family chosen at each N,
3. whether the sign pattern agrees with E79.70.                         (71-5)
```

## 3. Result

The good news is immediate:

```text
exact 5/5 recovery occurs on a nontrivial local region, not just one point. (71-6)
```

And those exact solutions preserve the E79.70 sign pattern:

```text
card < 0,
span > 0,
gaps < 0,
start > 0.                                                              (71-7)
```

So the selector is not numerically arbitrary at the level that matters most.

## 4. Reading

This is the structural meaning of the robustness test:

```text
the coefficient magnitudes can move somewhat,
but the tradeoff directions do not flip.                                (71-8)
```

The stable sign pattern says:

```text
- smaller supports are preferred,
- longer spans are penalized,
- disconnectedness is rewarded relative to span,
- deeper terminal supports are rewarded.                                (71-9)
```

So the live law is already more invariant than the single tuple from E79.70.

## 5. Consequence

After E79.71, the open problem is no longer:

```text
"does any simple rule exist?"                                           (71-10)
```

It is:

```text
"why this sign pattern is the right structural tradeoff?"               (71-11)
```

That is a much better question. It shifts the burden from coefficient search to
interpretation.

## 6. Status

```text
proved by probe:
  the E79.70 selector persists on a real local coefficient region and is not a
  single fragile point;

clarified:
  what is stable is the sign pattern of the tradeoff, not just one exact tuple;

reduced:
  the live burden from "find coefficients" to "explain the stable sign pattern
  structurally";

open:
  derive or normalize that sign pattern from a more intrinsic gain-vs-cost
  principle;

next:
  search for an invariant reformulation of the same tradeoff, such as gain per
  added shell, per span, or per deferred depth.
```
