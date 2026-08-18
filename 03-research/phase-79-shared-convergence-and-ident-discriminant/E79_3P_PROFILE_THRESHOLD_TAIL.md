# E79.3p - A profile-threshold cut is recurrent, but not uniformly better

**Scope:** `GAP-Z` only, profile-based intrinsic selector for the deep terminal
tail.  
**Class:** AUTOPSIA MIXTA.  
**What we know after this document that we did not know before:** selecting the
tail by a fixed threshold in the local `N^2` shell profile does pick out a
recurrent geometric regime, but it does not uniformly beat the simpler
length-based mesoscopic sweep. So it is a meaningful structural hint, not yet
the stable selector we need.

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

After E79.3o, two facts were in place:

```text
1. a short mesoscopic terminal tail can pair well with ZERO^extra;
2. cumulative absolute mass is NOT the right intrinsic selector.         (T-1)
```

The next natural selector was geometric:

```text
start the tail where the local N^2 shell profile drops below a fixed fraction
of its peak.                                                             (T-2)
```

That is exactly what this probe tests.

## 2. Probe

Companion files:

```text
E79_3P_PROFILE_THRESHOLD_TAIL_PROBE.py
E79_3P_profile_threshold_tail_results.json
```

Inside the active `99%` edge, let `a_r` be the absolute `N^2`-scaled shell
amplitude and `peak = max_r a_r`. For

```text
tau in {0.4, 0.5, 0.6, 0.7, 0.8},                                      (T-3)
```

define the terminal tail as the deepest suffix beginning where `a_r` first rises
above `tau * peak` when scanned inward from the deep end.

Then audit

```text
|tail_tau - ZERO^extra| / max(|tail_tau|, |ZERO^extra|).                (T-4)
```

## 3. Result: tau ≈ 0.4 recurs, but does not stabilize the pairing

At `sigma = 1`, zeta gives the best threshold-based ratios:

```text
N= 8:  0.4629   (best tau = 0.7)
N=10:  0.0087   (best tau = 0.4)
N=12:  0.4762   (best tau = 0.4)
N=14:  0.2683   (best tau = 0.4)
N=16:  0.1569   (best tau = 0.4)
```

So one useful structural fact does emerge:

```text
the threshold tau ≈ 0.4 recurs as the preferred geometric cut on much of the
audited ladder.                                                          (T-5)
```

But the equally important comparison is against the length-based sweep of
E79.3n:

```text
N      best length-tail ratio      best profile-threshold ratio
8      0.0229                      0.4629
10     0.0087                      0.0087
12     0.3588                      0.4762
14     0.0215                      0.2683
16     0.4141                      0.1569
```

This is mixed, not decisive:

```text
the profile-threshold selector improves the pairing at some N (notably N=16),
matches it at N=10, and is much worse at others.                         (T-6)
```

So it is not a uniformly better replacement for the mesoscopic length cut.

## 4. Reading

This is a useful half-step, not a closure.

The positive half:

```text
the edge profile does contain a recurrent geometric marker around tau ~ 0.4.
```

The negative half:

```text
that marker alone does not yet stabilize the deep-tail / extra-root
pairing across the ladder.                                               (T-7)
```

So the right selector is probably not "all shells below a fixed amplitude
threshold" by itself. It likely needs one more piece of structure.

## 5. Consequence

The live object sharpens by combination:

```text
the correct deep terminal tail seems to live near the onset of the decay region
of the N^2 shell profile, but a fixed threshold tau is not by itself enough to
select it non-resonantly.                                                (T-8)
```

That suggests the next selectors should combine two ingredients, for example:

```text
1. a profile threshold plus a minimal/ maximal tail length window,
2. a profile threshold matched to ZERO^extra scale,
3. a plateau-to-decay transition located by slope rather than height.    (T-9)
```

## 6. Status

```text
proved by probe:
  a threshold around tau ~ 0.4 repeatedly identifies a plausible geometric
  deep-tail region inside the active edge;

observed:
  that selector does not uniformly outperform the best fixed-fraction
  mesoscopic tail;

reduced:
  the search for the intrinsic tail selector narrows from "any geometric cut"
  to "a decay-onset cut that probably needs one more matching condition";

open:
  combine the geometric onset marker with a second constraint that stabilizes
  the pairing with ZERO^extra;

next:
  test a hybrid selector: threshold-based onset plus a short admissible length
  window, or threshold-based onset tuned directly to the extra-root scale.
```
