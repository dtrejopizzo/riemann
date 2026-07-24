# E79.72 - The E79.70 selector collapses to a three-term normalized gain-vs-cost rule

**Scope:** `GAP-Z` only, invariant normalization of the penalized selector from
E79.70-E79.71.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the apparent
five-term selector from E79.70 is algebraically redundant. Because

```text
span = cardinality + gaps,                                              (72-1)
```

the rule collapses to a three-term gain-vs-cost form:

```text
score = mismatch
        - 0.22 card
        + 0.14 gaps
        + 0.36 start.                                                   (72-2)
```

And this reduced rule keeps the exact `5/5` audited recovery.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Pure algebraic rewrite of the audited E79.70 family.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Why this rewrite matters

E79.71 showed that the live content of E79.70 is the sign pattern, not one
isolated coefficient tuple. The natural next move is therefore to remove any
algebraic redundancy before interpreting that sign pattern.

Here there is an immediate identity on every support:

```text
span = card + gaps.                                                     (72-3)
```

So the raw five-term rule is over-parameterized from the start.

## 2. Reduction

Starting from E79.70,

```text
score
  = mismatch
    - 1.00 card
    + 0.78 span
    - 0.64 gaps
    + 0.36 start,                                                       (72-4)
```

substitute `(72-3)`:

```text
score
  = mismatch
    + (-1.00 + 0.78) card
    + ( 0.78 - 0.64) gaps
    + 0.36 start
  = mismatch
    - 0.22 card
    + 0.14 gaps
    + 0.36 start.                                                       (72-5)
```

So the live selector is already equivalent to a three-term tradeoff:

```text
reward for support size,
cost of disconnectedness / spread,
cost of terminal delay / lateness.                                      (72-6)
```

## 3. Probe

Companion files:

```text
E79_72_NORMALIZED_GAIN_COST_RULE_probe.py
E79_72_normalized_gain_cost_rule_results.json
```

The probe checks two things:

```text
1. the reduced rule gives the same audited picks as E79.70;
2. a local box around the reduced coefficients still contains exact `5/5`
   solutions.                                                           (72-7)
```

## 4. Result

The reduced rule keeps the same exact audited selector:

```text
N= 8  -> {6,7,8}
N=10 -> {5}
N=12 -> {7}
N=14 -> {10,11,12}
N=16 -> {11,13}.                                                        (72-8)
```

So the base reduced rule still has:

```text
exact audited recovery = 5 / 5.                                         (72-9)
```

And the local coefficient box around the reduced form still contains a real set
of exact solutions, so the algebraic compression does not destroy robustness.

## 5. Reading

This is a better way to phrase the live law than E79.70.

The selector is not fundamentally about `span` and `gaps` separately. It is
about:

```text
1. mismatch to ZERO^extra,
2. a mild reward for adding support sites,
3. a mild penalty for geometric spread / disconnectedness,
4. a stronger penalty for delaying the support too far into the terminal
   edge.                                                                (72-10)
```

So the intrinsic tradeoff is already close to a "gain vs structural cost" rule.

## 6. Consequence

After E79.72, the open problem is sharper again. We no longer need to explain a
five-term fit. We need to explain why the right normalized selector looks like:

```text
mismatch
minus a support-size reward
plus a spread/disconnectedness cost
plus a terminal-delay cost.                                             (72-11)
```

That is much nearer to a theorem-grade finite object.

## 7. Status

```text
proved by algebra + probe:
  the E79.70 selector is exactly equivalent to a reduced three-term
  gain-vs-cost rule, and the reduced rule preserves exact `5/5` audited
  recovery;

reduced:
  the live selector from a five-term coefficient fit to a normalized
  mismatch/cardinality/gaps/start rule;

clarified:
  the real content is a tradeoff between mismatch, support-size reward,
  spread/disconnectedness cost, and terminal-delay cost;

open:
  explain structurally why those three normalized terms are the right ones;

next:
  test whether the same selector can be derived from a gain-per-added-site or
  deferred-depth principle rather than from coefficient sweep.
```
