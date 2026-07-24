# E79.73 - The normalized selector is a mismatch plus depth-complexity surcharge

**Scope:** `GAP-Z` only, post-E79.72 structural reading of the reduced selector.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the normalized
selector is best read as raw matching error plus a purely geometric surcharge.
The hard audited branch (`N=10`) is resolved exactly because a small mismatch
gain fails to compensate for a large depth-complexity surcharge.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Pure algebraic repackaging of E79.70/E79.72.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Starting point

E79.72 reduced the E79.70 score to

```text
score(S) = mismatch(S) - 0.22 card(S) + 0.14 gaps(S) + 0.36 start(S).    (73-1)
```

The first useful structural split is to isolate the purely geometric part:

```text
surcharge(S) := -0.22 card(S) + 0.14 gaps(S) + 0.36 start(S),            (73-2)
```

so that

```text
score(S) = mismatch(S) + surcharge(S).                                   (73-3)
```

After E79.72 the selector is therefore no longer a five-term or even a
four-term mystery. It is:

```text
raw matching quality
+ a geometry-only surcharge.                                              (73-4)
```

## 2. What the surcharge means

Each term in `(73-2)` has a fixed sign:

```text
-0.22 card   = mild reward for adding occupied sites,
+0.14 gaps   = mild cost for spreading the support,
+0.36 start  = dominant cost for moving the packet later into the edge.    (73-5)
```

So the normalized selector does **not** reward disconnectedness. In normalized
form it rewards occupied sites but penalizes spread, with the strongest
geometric burden coming from terminal delay.

That makes the selector interpretable as a corrected matching rule:

```text
choose the support whose mismatch gain is large enough to pay for its
depth-complexity surcharge.                                               (73-6)
```

## 3. The hard branch is now transparent

Companion files:

```text
E79_73_depth_complexity_surcharge_probe.py
E79_73_depth_complexity_surcharge_results.json
```

The probe computes `(73-3)` row by row and records the mismatch/surcharge split
for every candidate in the E79.69 tiny family.

The decisive audited case is `N=10`:

```text
suffix:   mismatch = 0.00870, surcharge = 1.64000, score = 1.64870
pair:     mismatch = 0.02948, surcharge = 1.58000, score = 1.60948.      (73-7)
```

So the suffix wins the raw matcher by only

```text
0.02948 - 0.00870 = 0.02078,                                             (73-8)
```

but pays a larger geometric surcharge by

```text
1.64000 - 1.58000 = 0.06000.                                             (73-9)
```

The surcharge overwhelms the mismatch gain, and the singleton survives. This is
exactly the ambiguity that E79.69 could not resolve by cumulative matching
alone.

## 4. Result

On the audited zeta ladder the reduced selector is exactly:

```text
minimize mismatch + depth-complexity surcharge,                          (73-10)
```

with the same exact `5/5` recovery inherited from E79.72.

This gives a cleaner reading of the five audited rows:

```text
- N=8:  suffix/triple tie because both geometry and mismatch coincide;
- N=10: singleton wins because its surcharge savings dominate the suffix's
        small mismatch edge;
- N=12: singleton wins because the competing supports lose on both mismatch
        and surcharge;
- N=14: the compact late block wins because it is simultaneously deep and
        mismatch-efficient;
- N=16: the disconnected pair wins because its mismatch gain beats the mild
        spread penalty while keeping the same depth as the triple.         (73-11)
```

## 5. Consequence

The next honest burden is sharper again.

We no longer need to explain:

```text
"why those five coefficients?"
```

or even

```text
"why that four-term normalized selector?"                                (73-12)
```

We need to explain:

```text
why the common-cloud packet should be selected by raw extra-root matching
corrected by a depth-complexity surcharge.                               (73-13)
```

That is a much smaller theorem-grade target.

## 6. Status

```text
proved by algebra + probe:
  the E79.72 selector is exactly "mismatch plus geometric surcharge";

clarified:
  the normalized rule rewards occupied sites, penalizes spread, and its
  dominant geometric burden is terminal delay;

localized:
  the hard E79.69 ambiguity (especially N=10) is resolved precisely because
  the mismatch gain of the later suffix is too small to pay for its surcharge;

open:
  derive the surcharge structurally from the common-cloud / extra-root
  coupling, instead of reading it off a fitted score;

next:
  test whether the surcharge can be obtained from a one-step acceptance rule:
  add a shell only when its mismatch gain exceeds its incremental geometric
  cost.
```
