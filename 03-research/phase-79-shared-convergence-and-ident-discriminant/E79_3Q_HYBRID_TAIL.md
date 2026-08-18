# E79.3q - The hybrid selector recovers some good tails, but still does not dominate

**Scope:** `GAP-Z` only, hybrid intrinsic selector for the deep terminal tail.  
**Class:** REDUCCION PARCIAL + AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** combining the
geometric onset marker `tau ~ 0.4` with a short admissible tail length does
recover several of the best deep-tail / extra-root pairings. But it still does
not uniformly outperform the plain mesoscopic length sweep.

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

After E79.3p, two partial truths were in hand:

```text
1. short length-based terminal tails can cancel very well against ZERO^extra;
2. a geometric onset marker around tau ~ 0.4 repeatedly appears in the profile. (T-1)
```

The natural next move was therefore hybrid:

```text
use the tau-onset to locate the decay region,
then restrict to a short admissible terminal length.                     (T-2)
```

## 2. Probe

Companion files:

```text
E79_3Q_HYBRID_TAIL_PROBE.py
E79_3Q_hybrid_tail_results.json
```

The probe fixes

```text
tau = 0.4
```

to define the decay-onset index inside the active `99%` edge, then compares
tails of short lengths `{2,3,4,5}` starting no earlier than that onset.

The paired observable is, as before,

```text
tail - ZERO^extra,                                                       (T-3)
```

measured by

```text
|tail - ZERO^extra| / max(|tail|, |ZERO^extra|).                        (T-4)
```

## 3. Result: the hybrid selector recovers several strong pairings

At `sigma = 1`, zeta gives:

```text
N= 8:  onset=7,  best len=2, ratio=0.8422
N=10:  onset=7,  best len=4, ratio=0.0087
N=12:  onset=9,  best len=2, ratio=0.4762
N=14:  onset=9,  best len=3, ratio=0.0215
N=16:  onset=12, best len=2, ratio=0.1569
```

This contains a real positive result:

```text
the hybrid selector recovers the excellent pairings at N=10 and N=14,
and improves substantially over the crude Q4 coupling at N=16.           (T-5)
```

So the onset marker is not decorative. It does help identify a better terminal
region when combined with a short length cap.

## 4. But the hybrid rule still does not dominate the plain length sweep

Compare against the best pure length-based ratios from E79.3n:

```text
N      best hybrid ratio      best length-only ratio
8      0.8422                0.0229
10     0.0087                0.0087
12     0.4762                0.3588
14     0.0215                0.0215
16     0.1569                0.4141
```

So:

```text
the hybrid selector wins at some N, ties at others, and loses badly at N=8 and
still noticeably at N=12.                                                (T-6)
```

The mean comparison over the audited ladder reflects that:

```text
mean best hybrid ratio   = 0.3011...
mean best length ratio   = 0.1652...                                    (T-7)
```

So the hybrid rule is more structured, but not yet better in a uniform sense.

## 5. Reading

This is still a useful refinement.

What it proves:

```text
the good deep-tail / extra-root cancellation can be partially recaptured by a
selector with real geometric content, not only by brute-force length search.  (T-8)
```

What it does **not** prove:

```text
that the correct selector is simply "tau=0.4 onset + short fixed window". (T-9)
```

So the onset marker is part of the right story, but not the whole story.

## 6. Consequence

The live object sharpens one more step:

```text
the correct deep terminal tail appears to be:
  [near the tau ~ 0.4 decay onset]
  + [restricted to a short window],
but the short window itself still drifts with N.                         (T-10)
```

That is enough to prune the search again. The next selectors should probably be
slightly more adaptive, for example:

```text
1. tau-onset plus window chosen by matching ZERO^extra scale directly,
2. tau-onset plus a local slope/drop criterion,
3. tau-onset plus a cumulative signed rather than unsigned rule.         (T-11)
```

## 7. Status

```text
proved by probe:
  the geometric onset marker tau ~ 0.4 does carry real information: when
  combined with a short length cap it recovers some of the strongest observed
  deep-tail / extra-root cancellations;

observed:
  the resulting hybrid selector is still not uniformly better than the best
  pure length-based mesoscopic sweep;

reduced:
  the selector search narrows from "any hybrid rule" to "a tau-onset rule
  needing one more adaptive ingredient";

open:
  determine the second ingredient that stabilizes the short window beyond the
  tau-onset marker;

next:
  test a scale-matched hybrid rule where the tail is extended inward from the
  tau-onset until its signed size best matches ZERO^extra.
```
