# E79.3s - A simple shortness penalty does not change the selected tail

**Scope:** `GAP-Z` only, penalized version of the tau-onset scale-matching
selector.  
**Class:** AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** adding a
simple shortness penalty to the onset-plus-scale-matching objective does not
change the selected deep tail at all on the audited zeta ladder. So the missing
ingredient is not merely "prefer shorter tails a bit more".

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

After E79.3r, the hybrid selector had a clean internal form:

```text
choose the terminal tail after the tau=0.4 onset that best matches ZERO^extra
in signed scale.                                                        (T-1)
```

The obvious next refinement was to penalize long tails directly:

```text
objective = mismatch_ratio + lambda * (tail length / active length).    (T-2)
```

If the resonance problem were just "the optimizer is too willing to take a long
tail", this should have changed the selected tails.

## 2. Probe

Companion files:

```text
E79_3S_PENALIZED_TAIL_PROBE.py
E79_3S_penalized_tail_results.json
```

The probe tests

```text
lambda in {0.0, 0.05, 0.10, 0.20, 0.30}.                               (T-3)
```

For each `lambda`, it minimizes the penalized objective over terminal tails
starting at or after the `tau = 0.4` onset.

## 3. Result: nothing changes

At `sigma = 1`, zeta selects exactly the same tails for all tested penalties:

```text
N= 8: take = 2
N=10: take = 4
N=12: take = 2
N=14: take = 3
N=16: take = 2                                                   (T-4)
```

and the mean mismatch is therefore identical for every tested `lambda`:

```text
mean mismatch = 0.3011069473...                                  (T-5)
```

So the shortness penalty, at least in this simple linear form, is completely
inactive on the audited ladder.

## 4. Reading

This is a useful exclusion result.

It tells us that the tail selected by onset-plus-scale-matching is already so
short that a moderate length penalty never becomes decisive.

In other words:

```text
the ambiguity that remains is not between "long" and "short" tails in any crude
sense. It is between different very short tails.                         (T-6)
```

That is a much sharper statement than we had before.

## 5. Consequence

The live selector problem narrows again:

```text
the missing ingredient is not a generic shortness prior.                (T-7)
```

So the next refinements have to discriminate among already-short candidates by
something more structural, for example:

```text
1. local slope at the tail onset,
2. profile curvature or second-drop information,
3. matching against more than one scalar from the extra-root package.    (T-8)
```

## 6. Status

```text
proved by probe:
  a simple linear shortness penalty leaves the selected tau-onset tails
  unchanged on the audited zeta ladder;

reduced:
  the selector ambiguity is not about suppressing long tails, but about
  distinguishing among already-short tails;

open:
  identify the structural discriminator that separates those short tail
  candidates;

next:
  test onset-plus-slope or onset-plus-curvature selectors rather than
  onset-plus-length penalties.
```
