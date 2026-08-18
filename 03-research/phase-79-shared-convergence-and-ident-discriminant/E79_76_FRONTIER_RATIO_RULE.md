# E79.76 - The two-point frontier is decided by a unit tradeoff ratio

**Scope:** `GAP-Z` only, scalarization of the E79.75 two-point frontier.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** once the
family is reduced to its 2-point Pareto frontier, the winner is decided by a
single scalar ratio: mismatch gain divided by surcharge increase. The audited
selector crosses exactly at ratio `1`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Pure algebra on the E79.75 frontier data.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Starting point

E79.75 reduced the live selector to at most two non-dominated candidates in the
plane

```text
(mismatch, surcharge).                                                  (76-1)
```

Write them as:

```text
L = lower-surcharge point,
H = higher-surcharge point,                                             (76-2)
```

with

```text
Delta_m := mismatch(L) - mismatch(H) >= 0,
Delta_s := surcharge(H) - surcharge(L) >= 0.                            (76-3)
```

Then the E79.73 score difference is exactly

```text
score(H) - score(L) = Delta_s - Delta_m.                               (76-4)
```

So `H` wins exactly when

```text
Delta_m / Delta_s > 1,                                                  (76-5)
```

and `L` wins when the ratio is below `1`, provided `Delta_s > 0`. The
near-degenerate cases `Delta_s ~= 0` or `Delta_m = 0` must be handled
separately.

## 2. Probe

Companion files:

```text
E79_76_frontier_ratio_rule_probe.py
E79_76_frontier_ratio_rule_results.json
```

The probe reads the E79.75 frontier pairs, orders them by surcharge, and
records:

```text
- Delta_m  = mismatch gain from paying the extra surcharge,
- Delta_s  = surcharge increase,
- ratio    = Delta_m / Delta_s,
- whether the audited winner is the low- or high-surcharge point.       (76-6)
```

## 3. Result

On the genuine tradeoff rows, the ratio rule is exact:

```text
N=10: ratio = 0.346...  < 1   -> choose low-surcharge point  (pair)
N=12: ratio = 1.102...  > 1   -> choose high-surcharge point (pair)
N=16: ratio = 1.052...  > 1   -> choose high-surcharge point (pair).    (76-7)
```

The remaining rows are degenerate:

```text
N= 8: surcharge tie between pair and triple; winner collapses to pure mismatch.
N=14: exact support duplicate on the frontier; no tradeoff remains.      (76-8)
```

So after E79.75, the genuine tradeoff rows are already governed by one scalar
criterion:

```text
pay extra geometry iff the mismatch gain per surcharge unit exceeds 1.   (76-9)
```

## 4. Reading

This is a real compression of the live burden.

We no longer need to think of the audited selector as balancing several terms
at once. After the Pareto reduction, the only question left on non-degenerate
rows is:

```text
is the mismatch gain worth the extra surcharge, at unit exchange rate?   (76-10)
```

That is the entire frontier-choice problem.

## 5. Consequence

The live common-cloud selector now has a much cleaner form:

```text
1. reduce to the 2-point mismatch/surcharge frontier;
2. compare mismatch gain against surcharge cost at exchange rate 1.      (76-11)
```

So the remaining structural burden is not a multi-parameter support law
anymore. It is:

```text
why the common-cloud / extra-root coupling induces this unit exchange rate
between mismatch gain and surcharge cost.                                (76-12)
```

That is substantially smaller than the original E79.69 burden.

## 6. Status

```text
proved by algebra + probe:
  on every genuine audited frontier row, the winner is decided
  exactly by whether Delta_m / Delta_s is above or below 1;

reduced:
  the live selector from a score on a 3-way family to a unit-threshold
  comparison on a 2-point frontier;

clarified:
  the hard tradeoff rows N=10,12,16 are all instances of the same scalar law;

open:
  derive the unit exchange rate structurally from the common-cloud /
  extra-root coupling;

next:
  inspect whether Delta_m and Delta_s themselves already come from one shared
  mesoscopic quantity, so that the threshold `1` is forced rather than fitted.
```
