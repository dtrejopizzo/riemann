# E79.75 - The tiny family already collapses to a two-point Pareto frontier

**Scope:** `GAP-Z` only, structural reduction of the E79.69 family before any
linear scoring.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the
suffix/pair/triple family from E79.69 is still over-complete. On every audited
zeta row, one of the three candidates is already Pareto-dominated in the plane

```text
(mismatch, geometric surcharge),                                        (75-1)
```

so the live selector reduces from a 3-way branch to at most a 2-way frontier
before any fitted score is applied.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Pure finite-family comparison using E79.69-E79.73 data.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Starting point

After E79.73 the normalized selector reads

```text
score(S) = mismatch(S) + surcharge(S),                                  (75-2)
```

with

```text
surcharge(S) = -0.22 card(S) + 0.14 gaps(S) + 0.36 start(S).            (75-3)
```

So before asking for a specific linear tradeoff, there is an obvious geometric
question:

```text
is every member of the E79.69 tiny family ever genuinely needed,
or are some candidates already dominated simultaneously in mismatch and
surcharge?                                                              (75-4)
```

If domination is present, the live selector becomes smaller without any further
fitting.

## 2. Probe

Companion files:

```text
E79_75_pareto_frontier_reduction_probe.py
E79_75_pareto_frontier_reduction_results.json
```

For each audited zeta row and each candidate in the E79.69 family, the probe
records:

```text
- mismatch from E79.69,
- surcharge from E79.73,
- Pareto domination inside the 3-candidate family.                      (75-5)
```

Candidate `A` is declared dominated if another candidate `B` satisfies

```text
mismatch(B) <= mismatch(A),
surcharge(B) <= surcharge(A),                                           (75-6)
```

with at least one inequality strict.

## 3. Result

On every audited zeta row, exactly one candidate is removable by Pareto
domination:

```text
N= 8:  suffix is dominated by triple; frontier = {pair, triple}
N=10:  triple is dominated; frontier = {suffix, pair}
N=12:  suffix is dominated; frontier = {pair, triple}
N=14:  pair   is dominated; frontier = {suffix, triple}
N=16:  suffix is dominated; frontier = {pair, triple}.                  (75-7)
```

So the full audited family compression is:

```text
3 candidates  ->  at most 2 Pareto-frontier candidates, row by row.     (75-8)
```

In particular, the hard rows now look cleaner:

```text
N=10:  pair   versus suffix
N=12:  pair   versus triple
N=16:  pair   versus triple.                                            (75-9)
```

At `N=8` the reduction is slightly degenerate rather than conceptually new:
`suffix` and `triple` represent the same support, so only one copy survives on
the frontier and the genuinely different alternative is the disconnected pair.

The third branch is not part of the live burden there anymore.

## 4. Reading

This is a genuine structural reduction, not just another score fit.

The E79.69 family no longer needs to be read as:

```text
suffix OR pair OR triple.                                               (75-10)
```

It can already be read as:

```text
a two-point Pareto frontier between

  (A) the best mismatch-efficient compact packet,
  (B) the best geometry-efficient sparse packet,                        (75-11)
```

with the exact identity of `(A)` and `(B)` depending on the row.

That explains why E79.70-E79.73 worked so quickly once the family was isolated:
the score was not resolving a genuinely ternary branch. It was deciding between
two non-dominated tradeoff points.

## 5. Consequence

The next honest burden sharpens again.

We no longer need to derive a selector on a 3-way family. We need to explain a
choice between two Pareto-frontier packets:

```text
compact / low-mismatch candidate
versus
sparser / geometry-cheaper candidate.                                   (75-12)
```

So the live object is now:

```text
COMMON-GAP-Z packet selector
  = choose the correct point on a 2-point mismatch/surcharge frontier.  (75-13)
```

This is materially smaller than the E79.69 statement.

## 6. Status

```text
proved by probe:
  on every audited zeta row, one member of the E79.69 tiny family is
  already Pareto-dominated in the plane (mismatch, surcharge);

reduced:
  the live support rule from a 3-way family to a 2-point Pareto frontier;

clarified:
  E79.70-E79.73 should be read as choosing between two tradeoff points, not as
  resolving a genuinely ternary branch;

open:
  derive the frontier-choice rule structurally, rather than by a fitted linear
  score;

next:
  test whether the winning choice is determined by a single scalar tradeoff
  ratio:
  mismatch gain per unit surcharge increase along that 2-point frontier.
```
