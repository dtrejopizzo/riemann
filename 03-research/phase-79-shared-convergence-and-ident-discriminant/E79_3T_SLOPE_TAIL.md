# E79.3t - A local slope cut does not improve the deep-tail selector

**Scope:** `GAP-Z` only, local-slope-based selector for the deep terminal tail.  
**Class:** AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** using a local
drop criterion in the shell profile does not improve the deep-edge / extra-root
pairing over the simpler hybrid selector. In particular it can over-cut the tail
and destroy a good cancellation.

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

After E79.3s, the remaining ambiguity was explicitly between already-short tails.
That made a local geometric discriminator tempting:

```text
cut the tail where the local shell profile finally drops sharply relative to
the previous shell.                                                      (T-1)
```

If the right tail were controlled by a genuine local slope transition, this
should stabilize the selection.

## 2. Probe

Companion files:

```text
E79_3T_SLOPE_TAIL_PROBE.py
E79_3T_slope_tail_results.json
```

Starting from the `tau = 0.4` onset, the probe searches for the first depth
where

```text
a_r / a_{r-1} <= rho,                                                   (T-2)
```

with `rho in {0.9,0.8,0.7,0.6,0.5}`, and uses the resulting suffix as the
terminal tail.

Then it audits the usual pairing

```text
|tail - ZERO^extra| / max(|tail|,|ZERO^extra|).                         (T-3)
```

## 3. Result: the slope cut is not an improvement

At `sigma = 1`, zeta gives:

```text
N= 8:  best rho = 0.5, take = 2, mismatch = 0.8422
N=10:  best rho = 0.5, take = 4, mismatch = 0.0087
N=12:  best rho = 0.5, take = 2, mismatch = 0.4762
N=14:  best rho = 0.8, take = 3, mismatch = 0.0215
N=16:  best rho = 0.5, take = 1, mismatch = 0.8270
```

Compared with the hybrid selector of E79.3q:

```text
N      slope best      hybrid best
8      0.8422          0.8422
10     0.0087          0.0087
12     0.4762          0.4762
14     0.0215          0.0215
16     0.8270          0.1569                                               (T-4)
```

So the slope selector mostly reproduces the same answers as the hybrid rule, but
at `N=16` it over-cuts to a one-shell tail and loses badly.

The aggregate comparison reflects this:

```text
mean slope mismatch  = 0.4351...
mean hybrid mismatch = 0.3011...                                           (T-5)
```

## 4. Reading

This is a straightforward autopsy:

```text
the local drop condition is too brittle to serve as the missing selector
ingredient by itself.                                                     (T-6)
```

It does identify the same short tails in several cases, which means the slope
signal is not meaningless. But it is not robust enough, and can misfire by
choosing a tail that is too short.

So the selector problem is now even more sharply characterized:

```text
the right rule is not simply "first strong local drop".                  (T-7)
```

## 5. Consequence

The search space narrows again:

```text
the missing ingredient is not a naive local slope trigger.               (T-8)
```

What remains plausible is something slightly less local and less brittle, for
example:

```text
1. a slope/height combination over a short window rather than one step,
2. a selector matching several tail statistics to ZERO^extra, not just one,
3. a mesoscopic optimization over 2-4 shell windows near the decay onset. (T-9)
```

## 6. Status

```text
proved by probe:
  a one-step local slope criterion does not improve the deep-tail /
  extra-root selector over the simpler hybrid rule;

observed:
  the slope rule can over-cut the tail and destroy a good cancellation;

reduced:
  the selector ambiguity is not resolved by a naive local-drop trigger;

open:
  test slightly less brittle mesoscopic or multi-statistic selectors near the
  decay onset;

next:
  evaluate short window-based selectors around the onset that combine height
  and slope information instead of using either one alone.
```
