# E79.69 - A tiny cumulative-matching family already recovers the sigma-stable sparse packet

**Scope:** `GAP-Z` only, first relational recovery of the sigma-stable sparse
packet from E79.67.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** once the
selector is allowed to be relational and match cumulative packet mass directly
to `ZERO^extra` across `sigma = 1,2`, the sigma-stable sparse packet is no
longer mysterious. It is recovered exactly by a tiny family of support types:
terminal suffixes, bounded-gap pairs, and short triples.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only common-cloud shell data and the audited extra-root
       target from the same spec(K_N) bookkeeping.
E72.16/E77.7az: respected. This is a convergence-side structural reduction, not
                a build-separating forcing step.
Circularity: respected. No endpoint identity is imported.
```

## 1. Starting point

E79.67 and E79.68 together left the front in a clean position:

```text
- the live object is a sigma-stable sparse terminal packet;
- it is NOT selected by any cheap one-point local score.                (69-1)
```

So the smallest admissible next move was no longer "find a better salience
score", but:

```text
let the selector be relational and ask which tiny support family best matches
ZERO^extra simultaneously at sigma = 1 and sigma = 2.                   (69-2)
```

## 2. Probe

Companion files:

```text
E79_69_RELATIONAL_MATCHING_SELECTOR_probe.py
E79_69_relational_matching_selector_results.json
```

Using the reconstructed active common-cloud arrays from E79.68, the probe tests
three tiny support families:

```text
1. terminal suffixes,
2. bounded-gap pairs (including singletons),
3. short triples of span <= 4.                                          (69-3)
```

Each candidate support is scored by direct cumulative matching to `ZERO^extra`
across both sigmas:

```text
mismatch = max(
  |packet_sigma1 - extra_sigma1| / max(packet_sigma1, extra_sigma1),
  |packet_sigma2 - extra_sigma2| / max(packet_sigma2, extra_sigma2)
).                                                                       (69-4)
```

## 3. Result

The sigma-stable sparse packet is recovered exactly in every audited zeta case
by at least one of those three families:

```text
N= 8:  target {6,7,8}    = best suffix = best triple
N=10:  target {5}        = best bounded-gap pair (singleton case)
N=12:  target {7}        = best bounded-gap pair (singleton case)
N=14:  target {10,11,12} = best suffix = best triple
N=16:  target {11,13}    = best bounded-gap pair.                       (69-5)
```

So the union of the three families has:

```text
union exact recovery = 5 / 5.                                            (69-6)
```

Family hit counts are:

```text
suffix  -> 2 / 5
pair    -> 3 / 5
triple  -> 2 / 5
union   -> 5 / 5.                                                       (69-7)
```

But the minimizer across the three families is not yet identical to the sparse
packet in every case:

```text
best-of-three minimizer = 4 / 5,
with the sole exception N=10, where the best cumulative matcher is the suffix
{7,8,9,10}, while the sigma-stable sparse packet is the singleton {5}.   (69-8)
```

## 4. Reading

This is the first real intrinsic compression after E79.67.

The sparse packet is not being chosen by local salience at all. It is living
inside a tiny cumulative-matching family:

```text
small relational supports whose cumulative mass matches ZERO^extra
simultaneously at the sampled safe sigmas.                               (69-8)
```

And the geometry splits cleanly into two regimes:

```text
suffix regime:
  N=8,14  -> short terminal intervals;

pair regime:
  N=10,12,16 -> singleton / disconnected sparse supports.               (69-9)
```

So the right next object is no longer "support chosen by a score on shells", but
"support chosen by a tiny cumulative-matching family near ZERO^extra", with one
remaining ambiguity at `N=10`.

## 5. Consequence

The live common-cloud object sharpens again:

```text
COMMON-GAP-Z
  = [broad shallow/middle package]
    + [tiny cumulative matcher to ZERO^extra]
    + [tiny interior remainder].                                         (69-10)
```

And that matcher already lives inside a very small combinatorial family:

```text
suffix OR bounded-gap pair OR short triple.                              (69-11)
```

This is substantially better than E79.67, because the packet is no longer just
an observed stable support. It is now the optimizer of a tiny relational
matching problem up to one remaining branch ambiguity.

## 6. Open point

This is not the final intrinsic law yet, because it still branches across three
support families. The next candid question is:

```text
is there a single relational selector that resolves the remaining branch
ambiguity, especially the `N=10` suffix-vs-singleton split, without separate
family search?                                                           (69-12)
```

Natural candidates now are:

```text
1. a penalized cumulative matching functional,
2. a tiny dynamic-programming selector with a short support budget,
3. a support rule based on matching gain per added shell.                (69-13)
```

## 7. Status

```text
proved by probe:
  the sigma-stable sparse packet is recovered exactly in all audited zeta
  sections by the union of three tiny relational support families:
  suffixes, bounded-gap pairs, and short triples;

reduced:
  the live support rule from "unknown relational selector" to "tiny
  cumulative-matching family near ZERO^extra", with only one unresolved branch
  ambiguity at N=10;

clarified:
  the geometry splits into a suffix regime and a pair regime on the audited
  zeta ladder;

open:
  unify those tiny support families into one intrinsic relational selector;

next:
  test a penalized cumulative-matching rule that can interpolate between the
  suffix and bounded-gap pair regimes without branching by hand.
```
