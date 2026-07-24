# E79.3l - The deepest edge block couples to the extra-root scale, not to the remainder

**Scope:** `GAP-Z` only, first global coupling audit beyond local shell anatomy.  
**Class:** REDUCCION GENUINA + AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** the natural
global coupling partner of the deep edge tail is not the tiny interior
remainder. It is the explicit `ZERO^extra` term. The remainder is far too small
to balance any substantial part of the deep active edge.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct cloud bookkeeping only.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. Everything is computed from spec(K_N).
```

## 1. Starting point

After E79.3k, local signed cancellation inside the active edge was ruled out.
So the next honest possibility was a **global** compensation:

```text
perhaps a deeper part of the active edge cancels not with nearby shells,
but with one of the two small external pieces:
  ZERO^extra  or  remainder99.                                         (T-1)
```

That is exactly what this probe tests.

## 2. Probe

Companion files:

```text
E79_3L_EDGE_COUPLING_PROBE.py
E79_3L_edge_coupling_results.json
```

For the `99%` active edge, the probe splits the signed edge package into four
long blocks `Q1,Q2,Q3,Q4` by normalized depth quartiles. Here `Q4` is the
deepest quarter of the active edge. It then compares each block to:

```text
ZERO^extra,
remainder99 = ZERO^common - outer99.                                   (T-2)
```

The key diagnostics are the ratios

```text
|Qj| / |ZERO^extra|,
|Qj| / |remainder99|.                                                  (T-3)
```

## 3. Result: the deep edge tail lives on the extra-root scale

At `sigma = 1`, zeta gives for the deepest block `Q4`:

```text
N    |Q4| / |extra|      |Q4| / |remainder99|
8    0.1578             25.79
10   0.3051             25.20
12   0.5238              9.26
14   0.9785              8.91
16   1.7069             10.88
```

This is the key structural fact:

```text
the deep tail of the active edge progressively enters the same scale as
ZERO^extra, while staying an order of magnitude larger than remainder99.  (T-4)
```

So the plausible coupling is:

```text
deep edge tail  <->  extra-root term,                                   (T-5)
```

not:

```text
deep edge tail  <->  interior remainder.                                (T-6)
```

That second option is numerically dead on the audited ladder.

## 4. Reading

This is a real change in the map of plausible mechanisms.

Up to now, the common-cloud problem had been treated almost entirely internally:

```text
common cloud = active edge + remainder.                                 (T-7)
```

But the data say the remainder is too small to carry the missing gain. The
first nontrivial scale match instead appears between:

```text
the deepest quarter of the active edge
and
the explicit extra-root package.                                        (T-8)
```

That is exactly the sort of coupling a purely common-cloud analysis would miss.

## 5. A mild but useful correction

The combined package `outer99 + extra` does **not** itself show a dramatic
cancellation on the audited ladder:

```text
|outer99 + extra| / |outer99| = 1.135, 1.109, 1.081, 1.068, 1.053
for N = 8,10,12,14,16.                                                 (T-9)
```

So the story is not "the whole active edge cancels with extra". That would be
false. The only plausible scale match is with the **deep tail**, not with the
whole edge.

## 6. Consequence

This sharpens the live object in a materially new way:

```text
COMMON-GAP-Z
  = [shallow + middle edge package]
    + [deep edge tail on the extra-root scale]
    + [tiny interior remainder].                                        (T-10)
```

That is a genuine refinement. It says the global coupling worth chasing is not
inside the common cloud but across the boundary:

```text
deep-edge / extra-root interaction.                                     (T-11)
```

## 7. Status

```text
proved by probe:
  the deepest active-edge block enters the same scale as ZERO^extra,
  while remainder99 stays far too small to be the relevant coupling
  partner;

observed:
  the whole outer99 edge package does not cancel dramatically with extra,
  so only the deep edge tail is a plausible coupling object;

reduced:
  the global gain mechanism is more plausibly a deep-edge / extra-root
  coupling than anything involving the tiny interior remainder;

open:
  test whether a signed combination of the deep edge tail with ZERO^extra
  is more stable/smaller than either piece separately;

next:
  build the explicit paired observable
      DEEP-TAIL + ZERO^extra
  and audit whether its scale beats the raw edge budget.
```
