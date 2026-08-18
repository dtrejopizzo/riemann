# E79.3n - A short mesoscopic tail beats the crude quartile, but no universal cut emerges

**Scope:** `GAP-Z` only, optimization sweep for the deep-edge / extra-root
pairing.  
**Class:** REDUCCION GENUINA + AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** the crude last
quartile `Q4` is not the best deep-tail object. Much shorter mesoscopic tails
can cancel against `ZERO^extra` far better. But the optimal tail fraction is not
yet universal across the audited ladder.

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

E79.3m showed that

```text
Q4 - ZERO^extra                                                         (T-1)
```

is the first genuine global cancellation object, but still resonance-like. That
left an obvious refinement:

```text
is the quartile cut itself the problem?                                 (T-2)
```

So this probe sweeps a family of shorter or longer deep tails.

## 2. Probe

Companion files:

```text
E79_3N_TAIL_SWEEP_PROBE.py
E79_3N_tail_sweep_results.json
```

Inside the active `99%` edge of length `m99`, define `tail_alpha` as the last
`alpha` fraction of that edge, with

```text
alpha in {0.20, 0.30, 0.40, 0.50, 0.60}.                               (T-3)
```

For each `alpha`, the probe measures

```text
|tail_alpha - ZERO^extra| / max(|tail_alpha|, |ZERO^extra|).            (T-4)
```

Small values indicate good signed pairing.

## 3. Result: shorter tails help a lot, but the best alpha drifts

At `sigma = 1`, zeta gives:

```text
N= 8: best alpha = 0.30, ratio = 0.0229
N=10: best alpha = 0.30, ratio = 0.0087
N=12: best alpha = 0.20, ratio = 0.3588
N=14: best alpha = 0.20, ratio = 0.0215
N=16: best alpha = 0.20, ratio = 0.4141
```

So two real facts emerge at once:

```text
1. much shorter tails than the crude quartile can pair far better with extra;
2. the best tail fraction is not stable yet: it shifts from ~30% to ~20%.  (T-5)
```

This is already a genuine reduction, because the quartile cut is now clearly
too blunt.

## 4. Mean behavior by tail fraction

Still at `sigma = 1`, the mean pairing quality over the audited zeta ladder is:

```text
alpha = 0.20   mean ratio 0.405
alpha = 0.30   mean ratio 0.338
alpha = 0.40   mean ratio 0.662
alpha = 0.50   mean ratio 0.771
alpha = 0.60   mean ratio 0.835
```

This is the decisive optimization fact:

```text
the useful pairing regime is concentrated in relatively short tails,
roughly 20%-30% of the active 99% edge.                                (T-6)
```

Longer tails rapidly destroy the cancellation.

So the live object is no longer "some deep tail" in the abstract. It is a
**short mesoscopic tail**.

## 5. Reading

This is more than a cosmetic improvement. It changes the geometry of the live
coupling object:

```text
the correct partner of ZERO^extra is not the whole deep quartile,
but a shorter terminal segment of the active edge.                      (T-7)
```

That is exactly the kind of refinement the phase needed. The pairing was real in
E79.3m; now we know the relevant tail is thinner than the last quarter.

But the equally candid correction is:

```text
there is still no single alpha that is uniformly optimal.               (T-8)
```

So the tail cut is still somewhat resonance-sensitive.

## 6. Consequence

The live object sharpens again:

```text
COMMON-GAP-Z
  = [shallow + middle edge package]
    + [short mesoscopic terminal tail - ZERO^extra]
    + [tiny interior remainder].                                        (T-9)
```

This is better than E79.3m because it replaces the arbitrary quartile by a much
more plausible family of candidates.

The candid next question is now narrower:

```text
what is the intrinsic way to locate that short terminal tail,
so that the pairing with ZERO^extra becomes stable rather than drifting
between 20% and 30%?                                                    (T-10)
```

Likely answers include:

```text
1. a tail cut determined by cumulative mass rather than raw length,
2. a cut at the onset of the plateau-to-decay transition seen in E79.3j,
3. a normalized tail selected by matching the N^2 shell profile to extra-root. (T-11)
```

## 7. Status

```text
proved by probe:
  a short mesoscopic tail (around 20%-30% of the active 99% edge) pairs with
  ZERO^extra much better than the crude quartile Q4;

observed:
  there is still no universal fixed tail fraction that stabilizes the pairing
  across the whole audited ladder;

reduced:
  the deep-edge / extra-root coupling object from "quartile tail" to "short
  mesoscopic terminal tail";

open:
  identify the intrinsic rule that selects the right terminal tail
  non-resonantly;

next:
  try a mass-based or profile-based tail cut instead of a fixed length
  fraction.
```
