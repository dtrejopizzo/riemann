# E79.68 - Sigma-aware terminal prominence and curvature scores are still too crude

**Scope:** `GAP-Z` only, intrinsic recovery of the sigma-stable sparse packet
from E79.67.  
**Class:** AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** even after
coupling `sigma = 1` and `sigma = 2`, a natural family of intrinsic terminal
scores built from local size, one-step drop, local curvature, and optional tail
bias still does not recover the sigma-stable sparse support. So the live object
is not determined by any cheap sigma-aware one-point score either.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only direct common-cloud shell data from spec(K_N).
E72.16/E77.7az: respected. Convergence-side geometry only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Why this is the next honest test

E79.67 upgraded the common-cloud object from a one-sigma sparse packet to a
sigma-transported sparse packet:

```text
the same best support survives at sigma = 1 and sigma = 2
on the full audited zeta ladder.                                        (68-1)
```

The smallest admissible next hope was therefore:

```text
maybe that transported support is picked by a cheap sigma-aware local score,
not by subset search.                                                   (68-2)
```

The most natural ingredients are:

```text
1. local shell size,
2. one-step drop to the next shell,
3. local discrete curvature,
4. a mild tail bias,
5. and a simple coupling of sigma = 1 and sigma = 2.                    (68-3)
```

## 2. Probe

Companion files:

```text
E79_68_SIGMA_AWARE_TERMINAL_SCORE_AUTOPSY_probe.py
E79_68_sigma_aware_terminal_score_autopsy_results.json
```

The probe reconstructs the zeta-side active common-cloud shells directly from
`spec(K_N)` at `sigma = 1, 2` and tests a family of scores of the form

```text
score(i) = combine_sigma(
    local_feature_1(i) * local_feature_2(i) * x_1(i)^p1 * tail(i)^t,
    local_feature_1(i) * local_feature_2(i) * x_2(i)^p2 * tail(i)^t
),                                                                       (68-4)
```

where:

```text
combine_sigma in {sum, product, min},
local features in {x, drop, laplacian},
p1,p2 in {0,1,2},
t in {0,1}.                                                              (68-5)
```

For each section, the rule picks the top-`k` shells, where `k` is the true
cardinality of the sigma-stable sparse support from E79.67.

## 3. Result: no exact recovery at all

Across the whole tested family, the best score has:

```text
exact support matches = 0 / 5.                                           (68-6)
```

The best family found is typified by:

```text
sigma-coupled drop x curvature scores, without tail weighting,           (68-7)
```

and it still picks:

```text
N= 8  -> {2,4,6}    instead of {6,7,8}
N=10 -> {6}         instead of {5}
N=12 -> {8}         instead of {7}
N=14 -> {6,8,11}    instead of {10,11,12}
N=16 -> {10,12}     instead of {11,13}.                                 (68-8)
```

So even the best sigma-aware local score stays systematically too shallow and
too interior compared with the real transported sparse packet.

## 4. Reading

This is the clean negative conclusion:

```text
the sigma-stable sparse packet is not selected by any cheap one-point
sigma-aware prominence/curvature score.                                  (68-9)
```

The failure pattern is coherent:

```text
- it prefers interior curvature/drop peaks,
- it misses the true late terminal supports,
- and it cannot reproduce the disconnected pair {11,13} at N=16.        (68-10)
```

So the missing support rule is not just "local salience, but coupled across
sigmas". Something more relational is still needed.

## 5. Consequence

This closes another whole class of plausible selectors:

```text
not one-point amplitude ranking,
not one-point drop ranking,
not tiny motif dictionaries,
not monotone quantiles,
not sigma-aware local prominence/curvature scores either.                (68-11)
```

That leaves only richer terminal rules, for example:

```text
1. a short multi-point support score,
2. a rule based on cumulative matching to ZERO^extra rather than local salience,
3. a terminal interaction statistic that can prefer a disconnected support. (68-12)
```

## 6. Status

```text
proved by probe:
  a natural sigma-aware family of local terminal scores does not recover the
  sigma-stable sparse support even once on the audited zeta ladder;

observed:
  the best such scores consistently over-select shells that are too shallow /
  interior relative to the actual sparse packet;

reduced:
  the live support rule cannot be a cheap one-point sigma-aware selector;

open:
  find the first genuinely relational terminal statistic that reproduces the
  sigma-stable sparse packet without subset search;

next:
  test small multi-point support scores or cumulative matching rules that can
  explicitly represent disconnected support.
```
