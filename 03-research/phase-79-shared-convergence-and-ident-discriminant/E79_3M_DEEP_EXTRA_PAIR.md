# E79.3m - The deep-edge / extra-root pairing shows a real but non-uniform cancellation

**Scope:** `GAP-Z` only, explicit test of the deep-edge / extra-root coupling
isolated in E79.3l.  
**Class:** REDUCCION GENUINA + AUTOPSIA HONESTA.  
**What we know after this document that we did not know before:** the signed
combination

```text
Q4 - ZERO^extra
```

does produce a genuine cancellation, sometimes very strong, but not yet in a
uniform way across the audited ladder. So the deep-edge / extra-root coupling is
real, but it is not yet the final stable forcing object.

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

E79.3l identified the first plausible global coupling object:

```text
deep edge tail  <->  ZERO^extra.                                        (T-1)
```

That was only a scale match. The next real question is whether the **signed**
paired observable

```text
Q4 - ZERO^extra                                                         (T-2)
```

is actually smaller than the pieces separately.

## 2. Probe

Companion files:

```text
E79_3M_DEEP_EXTRA_PAIR_PROBE.py
E79_3M_deep_extra_pair_results.json
```

For the deepest quartile block `Q4` of the active `99%` edge, the probe records:

```text
Q4,
ZERO^extra,
Q4 + ZERO^extra,
Q4 - ZERO^extra,                                                        (T-3)
```

and compares `|Q4 - ZERO^extra|` against the larger of the two pieces.

## 3. Result: the pairing is real, but not uniformly small

At `sigma = 1`, zeta gives:

```text
N    |Q4 - extra| / max(|Q4|,|extra|)     N^2 |Q4 - extra|
8    0.8422                               0.02834
10   0.6949                               0.02136
12   0.4762                               0.01363
14   0.02148                              0.000560
16   0.4141                               0.01719
```

The same phenomenon is visible at `sigma = 2`:

```text
N    |Q4 - extra| / max(|Q4|,|extra|)
8    0.8431
10   0.6965
12   0.4780
14   0.02425
16   0.4128
```

This is the key fact:

```text
the pairing Q4 - ZERO^extra does produce a genuine reduction, and around
N = 14 it becomes almost perfectly cancelled.                           (T-4)
```

So the deep-edge / extra-root coupling is not a fake lead. It is a real
interaction in the correct signed direction.

## 4. But it is not yet a stable law

The equally important correction is:

```text
the reduction is not uniform on the audited ladder.                     (T-5)
```

The ratio

```text
|Q4 - extra| / max(|Q4|,|extra|)
```

drops dramatically from `0.84` to `0.02`, but then rebounds to `0.41`. So the
coupling is structurally real yet still resonance-like, not a stable small
parameter.

This is exactly the kind of mixed outcome that matters:

```text
not a dead end,
but not a closure either.                                               (T-6)
```

## 5. Reading

The program can now say something sharper than before:

```text
the first global cancellation candidate that actually cancels in the right sign
is DEEP-TAIL - ZERO^extra.                                              (T-7)
```

That is stronger than the scale-match statement of E79.3l.

But the current data also say:

```text
the observable Q4 - ZERO^extra is still too raw; it has not yet been normalized
or repackaged in the right way to expose a stable gain.                 (T-8)
```

So the next refinement has to be structural, not just more of the same ladder.

## 6. Consequence

The live object sharpens again:

```text
COMMON-GAP-Z
  = [shallow + middle edge package]
    + [deep edge tail - extra-root coupling]
    + [tiny interior remainder],                                        (T-9)
```

with the new crucial information that the middle bracket is a **real signed
cancellation object**, but not yet a stable one.

That narrows the next honest moves considerably. The likely missing ingredient
is one of:

```text
1. a better tail block than the crude last quartile Q4,
2. a normalized version of Q4 matched to the exact extra-root geometry,
3. a coarser mesoscopic block scale where the resonance at N=14 becomes stable. (T-10)
```

## 7. Status

```text
proved by probe:
  the signed combination Q4 - ZERO^extra genuinely cancels, and can cancel very
  strongly on the audited ladder;

observed:
  that cancellation is not yet uniform or stable enough to close GAP-Z;

reduced:
  the first viable global cancellation object is now explicit:
      deep-edge tail minus extra-root;

open:
  find the correct normalization or tail block definition that turns this
  resonance-like cancellation into a stable law;

next:
  replace the crude quartile tail Q4 by a tunable deep-tail block and search
  for the mesoscopic cut where the pairing with ZERO^extra is most stable.
```
