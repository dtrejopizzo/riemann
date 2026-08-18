# E79.3u - A short window score collapses back to the same 2-shell tail

**Scope:** `GAP-Z` only, mesoscopic height-plus-slope selector for the deep
terminal tail.  
**Class:** AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** combining
height and slope over a 2-4 shell window does correct the worst one-shell
over-cut of the local slope rule, but it does not produce a new stable
selector. On the audited zeta ladder it collapses back to the same 2-shell tail
every time, and usually performs worse than the simpler hybrid rule.

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

After E79.3t, the most plausible remaining selector idea was:

```text
use a short mesoscopic window, not a one-step trigger, and score each candidate
tail start by both its local height and its local decay.                    (U-1)
```

The goal was to keep the onset geometry of E79.3q while making the selector less
brittle than the one-step local slope rule.

## 2. Probe

Companion files:

```text
E79_3U_WINDOWED_ONSET_TAIL_PROBE.py
E79_3U_windowed_onset_tail_results.json
```

Inside the active `99%` edge:

1. locate the usual `tau = 0.4` onset,
2. for each later start and each short window `w in {2,3,4}`, compute

```text
score(start,w)
  = [average normalized shell height over the next w shells]
    x [geometric-mean decay ratio over the same window],                (U-2)
```

3. choose the start minimizing this purely internal score,
4. only after that, audit the resulting tail against `ZERO^extra` through

```text
|tail - ZERO^extra| / max(|tail|, |ZERO^extra|).                        (U-3)
```

So `ZERO^extra` is used only as an audit, not to choose the tail.

## 3. Result: the selector always collapses to the same 2-shell tail

At `sigma = 1`, zeta gives:

```text
N= 8:  best window = 2, take = 2, mismatch = 0.8422
N=10:  best window = 2, take = 2, mismatch = 0.6949
N=12:  best window = 2, take = 2, mismatch = 0.4762
N=14:  best window = 2, take = 2, mismatch = 0.3289
N=16:  best window = 2, take = 2, mismatch = 0.1569                 (U-4)
```

The structural point is not just that `w = 2` wins every time. It is that
`w = 3` and `w = 4` never change the selected start at all on the audited zeta
ladder. The mesoscopic window score immediately collapses to the same shortest
window.

## 4. Comparison with the existing selectors

Against the best audited zeta choices:

```text
N      hybrid best      slope best       window-score best
8      0.8422           0.8422           0.8422
10     0.0087           0.0087           0.6949
12     0.4762           0.4762           0.4762
14     0.0215           0.0215           0.3289
16     0.1569           0.8270           0.1569                         (U-5)
```

Mean mismatch over the audited zeta ladder:

```text
hybrid       0.3011...
slope        0.4351...
window-score 0.4998...                                                  (U-6)
```

So the new score does one useful thing:

```text
it fixes the catastrophic N=16 one-shell over-cut of the slope rule.     (U-7)
```

But it fails to do the more important thing:

```text
it does not preserve the good longer-tail selections at N=10 and N=14.   (U-8)
```

In that sense it is less brittle than the local slope rule, but still not the
missing selector.

## 5. Reading

This is another candid narrowing of the live object.

The key lesson is:

```text
the missing selector ingredient is not just "average the same local geometric
signals over 2-4 shells".                                                (U-9)
```

That kind of mesoscopic smoothing is enough to suppress the worst one-step
misfire, but not enough to recover the genuinely good longer tails.

The plant side reinforces the same reading. There the score degenerates almost
completely to one-shell choices with score `1`, so the method does not uncover a
meaningful neutral geometry there either.

## 6. Consequence

The search space narrows again:

```text
the right selector is not a pure suffix chosen by a local height+slope score,
even after mesoscopic smoothing over 2-4 shells.                         (U-10)
```

What still remains plausible is something with more global structure, for
example:

```text
1. a selector that allows a short union of terminal blocks rather than one
   contiguous suffix,
2. a selector that uses the onset geometry but matches a signed moment/profile
   of the deep edge rather than its raw size alone,
3. an object that explains why N=10 and N=14 want longer tails while N=12 and
   N=16 collapse to 2 shells.                                            (U-11)
```

## 7. Status

```text
proved by probe:
  a short window score combining local height and local decay does not produce
  a new stable deep-tail selector;

observed:
  the method always collapses to the same 2-shell tail on the audited zeta
  ladder;
  it corrects the worst one-shell failure of the slope rule at N=16;
  but it loses badly against the hybrid selector at N=10 and N=14;

reduced:
  the missing ingredient is not mesoscopic smoothing of the same suffix-based
  height/slope geometry;

open:
  test selectors with more global structure than a single contiguous suffix;

next:
  probe whether the deep-edge / extra-root cancellation is carried by a short
  union of terminal blocks, or by a signed profile moment rather than by one
  suffix length.
```
