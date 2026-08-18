# E79.3r - The scale-matched adaptive tail formalizes the hybrid rule, but does not improve it

**Scope:** `GAP-Z` only, adaptive selector for the deep-edge / extra-root
pairing.  
**Class:** REDUCCION FRANCA + AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** the good
deep-tail / extra-root pairings found by the hybrid rule can be rephrased as an
internal scale-matching selector starting from the `tau = 0.4` onset. But this
selector does not outperform the hybrid or the best pure length sweep; it mainly
explains them.

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

E79.3q suggested that the right selector might be:

```text
[tau ~ 0.4 onset] + [a short adaptive window].                          (T-1)
```

The natural next question was whether that window could be chosen by the most
direct internal rule:

```text
extend inward from the onset until the signed tail best matches ZERO^extra. (T-2)
```

## 2. Probe

Companion files:

```text
E79_3R_SCALE_MATCHED_TAIL_PROBE.py
E79_3R_scale_matched_tail_results.json
```

Inside the active `99%` edge:

1. locate the `tau = 0.4` onset,
2. consider every terminal tail starting at or after that onset,
3. choose the one minimizing

```text
|tail - ZERO^extra| / max(|tail|, |ZERO^extra|).                        (T-3)
```

This is the most literal scale-matched version of the hybrid idea.

## 3. Result: it reproduces the hybrid minima exactly

At `sigma = 1`, zeta gives:

```text
N    onset   best take   best ratio
8      7        2         0.8422
10     7        4         0.0087
12     9        2         0.4762
14     9        3         0.0215
16    12        2         0.1569
```

This is the key structural outcome:

```text
the adaptive scale-matched selector recovers exactly the same best tails as the
previous hybrid rule.                                                   (T-4)
```

So the hybrid signal was not arbitrary. It already had an internal variational
interpretation.

## 4. But it still does not beat the plain length sweep

The equally important comparison is:

```text
adaptive mean best ratio = 0.3011...
length-sweep mean best   = 0.1652...                                    (T-5)
```

and pointwise on the audited zeta ladder:

```text
N      adaptive best      length-only best
8      0.8422            0.0229
10     0.0087            0.0087
12     0.4762            0.3588
14     0.0215            0.0215
16     0.1569            0.4141
```

So the adaptive onset-based selector:

```text
matches some good cases,
improves some,
but still loses badly in others.                                        (T-6)
```

It does not dominate the simpler mesoscopic length sweep.

## 5. Reading

This is still useful progress, because it changes the status of the hybrid rule.

Before E79.3r, the hybrid selector was an empirical two-step recipe. After this
probe, we can say:

```text
the hybrid selector is the optimizer of an internal scale-matching problem
restricted by the tau-onset geometry.                                   (T-7)
```

That is a cleaner object, even if it is not yet the final one.

But the failure to improve further also tells us something:

```text
the missing ingredient is not merely "choose the best tail after the onset by
matching extra".                                                        (T-8)
```

So the selector still lacks one structural ingredient beyond onset and signed
scale matching.

## 6. Consequence

The live object sharpens by interpretation rather than by raw performance:

```text
the deep-edge / extra-root coupling is now governed by a genuine internal
optimization principle, but that principle is not yet sufficient to stabilize
the cancellation.                                                       (T-9)
```

This suggests the next selectors should enrich the objective, for example by:

```text
1. penalizing tails that are too long or too short,
2. matching not only tail size but also local profile slope,
3. optimizing over short unions of terminal blocks rather than one suffix. (T-10)
```

## 7. Status

```text
proved by probe:
  the best hybrid deep-tail selections can be recovered as a scale-matched
  optimization problem starting from the tau-onset;

observed:
  this adaptive selector still does not uniformly outperform the simpler
  mesoscopic length sweep;

reduced:
  the selector search is no longer heuristic only; it now has an explicit
  internal optimization form;

open:
  identify the extra structural ingredient needed on top of onset plus scale
  matching to stabilize the tail selection;

next:
  test enriched objectives, such as onset-plus-scale matching with a shortness
  penalty or with a local slope constraint.
```
