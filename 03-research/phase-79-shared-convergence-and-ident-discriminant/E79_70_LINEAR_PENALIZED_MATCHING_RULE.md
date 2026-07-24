# E79.70 - A simple linear penalty already resolves the suffix-vs-pair ambiguity on the audited zeta ladder

**Scope:** `GAP-Z` only, unification of the tiny relational family isolated in
E79.69.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the residual
branch ambiguity of E79.69 is not arbitrary. On the audited zeta ladder, one
simple linear penalized score on the tiny relational family already selects the
correct support type in every case.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the tiny relational family from E79.69.
E72.16/E77.7az: respected. This is convergence-side structure only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Starting point

E79.69 compressed the sigma-stable sparse packet to a tiny family:

```text
suffix OR bounded-gap pair OR short triple,                              (70-1)
```

but left one real ambiguity:

```text
the best raw cumulative matcher still picks the suffix at N=10,
while the transported sparse packet is the singleton {5}.               (70-2)
```

So the next honest question was whether a single tiny penalized rule can choose
the right member of that family without branching by hand.

## 2. Probe

Companion files:

```text
E79_70_LINEAR_PENALIZED_MATCHING_RULE_probe.py
E79_70_linear_penalized_matching_rule_results.json
```

The rule is tested only on the family already isolated in E79.69. For a
candidate support `S`, with mismatch `m(S)` from E79.69 and support statistics

```text
card(S), span(S), gaps(S), start(S),                                   (70-3)
```

the audited score is:

```text
score(S)
  = m(S)
    - 1.00 card(S)
    + 0.78 span(S)
    - 0.64 gaps(S)
    + 0.36 start(S).                                                    (70-4)
```

This was the first exact solution found by the grid sweep over simple linear
penalties on the tiny family.

## 3. Result

On the audited zeta ladder, this one rule selects the correct support in every
case:

```text
N= 8  -> suffix/triple support {6,7,8}
N=10 -> bounded-gap pair singleton {5}
N=12 -> bounded-gap pair singleton {7}
N=14 -> suffix/triple support {10,11,12}
N=16 -> bounded-gap pair {11,13}.                                      (70-5)
```

So:

```text
exact audited recovery = 5 / 5.                                         (70-6)
```

## 4. Reading

This is the first true unification of the E79.69 branch structure.

The sparse packet is no longer just known to lie in a tiny family. It is
selected by a single score that balances:

```text
1. cumulative matching quality,
2. support size,
3. support span,
4. disconnectedness penalty/reward,
5. terminal depth.                                                      (70-7)
```

The sign pattern is informative:

```text
- larger cardinality is penalized,
- larger span is penalized,
- gaps are rewarded relative to span,
- later supports are rewarded.                                          (70-8)
```

So the rule is explicitly telling us what the old raw matcher missed:

```text
N=10 is not "wrong" because the suffix matches badly;
it is wrong because that suffix buys a tiny mismatch gain at too high a support
cost relative to a very late singleton.                                 (70-9)
```

## 5. Consequence

The live common-cloud object sharpens again:

```text
COMMON-GAP-Z
  = [broad shallow/middle package]
    + [penalized cumulative matcher to ZERO^extra]
    + [tiny interior remainder].                                        (70-10)
```

This is stronger than E79.69: the family split has collapsed into one explicit
selector on the audited ladder.

## 6. Open point

This is still an audited selector, not yet a theorem-grade intrinsic law. The
next honest question is:

```text
can the coefficients/signs of the linear penalty be explained structurally,
rather than discovered by sweep?                                        (70-11)
```

Likely next moves:

```text
1. test robustness of the same sign pattern under nearby coefficient changes,
2. normalize the score into a more invariant gain-per-shell or gain-per-span
   form,
3. see whether the same rule remains stable on an extended sigma set.    (70-12)
```

## 7. Status

```text
proved by probe:
  one simple linear penalized score on the tiny E79.69 family selects the
  correct support in all five audited zeta cases;

reduced:
  the live support rule from "tiny family with one branch ambiguity" to
  "one penalized cumulative matcher on that family";

clarified:
  the N=10 ambiguity is resolved by trading tiny mismatch gain against support
  complexity and terminal depth;

open:
  explain and stabilize the penalty structurally rather than empirically;

next:
  test robustness of the sign pattern and search for a more invariant
  normalization of the same selector.
```
