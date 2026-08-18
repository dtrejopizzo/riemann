# E79.41 - Repulsive greedy selection collapses back to the failed ranking family

**Scope:** `GAP-Z` only, first explicitly non-monotone terminal selector.  
**Class:** AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** adding a
small repulsion between already chosen shells does not recover the sparse packet.
In practice the selector collapses back to the same family already seen in
E79.3x: singleton amplitude picks in the hard zeta-side cases, plus one
near-contiguous multi-point choice at `N=14`.

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

After E79.40, the next natural move was to try the smallest genuinely
non-monotone relational rule:

```text
choose shells greedily by terminal amplitude, but penalize new shells that lie
too close to ones already selected.                                     (41-1)
```

This was meant to give the selector a chance to prefer separated support such as
the zeta-side `N=16` packet `{11,13}`.

## 2. Probe

Companion files:

```text
E79_41_TERMINAL_REPULSIVE_GREEDY_PROBE.py
E79_41_terminal_repulsive_greedy_results.json
```

Inside the last `W in {4,5,6}` active shells, for support size `k in {1,2,3}`,
the probe selects shells greedily by

```text
score(j) = |a_j| - rho * max_amp * sum_{i already chosen} 1/(1+|j-i|),  (41-2)
```

with `rho in {0.25,0.50,0.75,1.0,1.5}`.

This is the smallest pattern-sensitive family tried so far that can explicitly
reward separation.

## 3. Result: the repulsive rule does not beat the sparse packet

At `sigma = 1`, zeta gives:

```text
N      sparse packet                  best repulsive rule
8      {6,7,8}   0.02288             W5-K1-R0.25   {4}        0.04607
10     {5}       0.02948             W6-K1-R0.25   {5}        0.02948
12     {7}       0.02299             W4-K1-R0.25   {8}        0.03450
14     {10,11,12} 0.02148            W4-K3-R0.75   {9,11,12}  0.05598
16     {11,13}   0.03554             W4-K1-R0.25   {10}       0.26619   (41-3)
```

Mean mismatch:

```text
sparse packet      0.02648...
repulsive greedy   0.08644...                                            (41-4)
```

So this family is strictly worse than the sparse packet benchmark, and not even
competitive with it on the hard `N=16` case.

## 4. Reading

The key negative conclusion is:

```text
repulsion by itself does not generate the right disconnected support.    (41-5)
```

The selector still behaves like a dressed-up one-point ranking:

```text
N=10: exact singleton hit {5}
N=12: wrong singleton {8} instead of {7}
N=16: wrong singleton {10} instead of disconnected pair {11,13}.        (41-6)
```

And at `N=14` the extra freedom only produces a mildly separated near-contiguous
triple `{9,11,12}`, still inferior to the sparse packet `{10,11,12}`.

So the problem is not simply that previous rules lacked a penalty for adjacency.

## 5. Plant side

The plant side reinforces the same reading:

```text
N= 8: sparse 0.0153, repulsive 0.8749
N=10: sparse 0.0138, repulsive 0.0138
N=12: sparse 0.8368, repulsive 0.8368
N=14: sparse 0.7150, repulsive 0.7150
N=16: sparse 0.8146, repulsive 0.8146                                   (41-7)
```

So the repulsive rule helps only in the already-easy `N=10` case and otherwise
collapses to the same trivial supports as earlier selectors.

## 6. Consequence

This closes another natural family:

```text
the live object is not a greedy amplitude selector with a simple proximity
penalty either.                                                          (41-8)
```

Combined with E79.3x, E79.3y, E79.3z, and E79.40, the evidence now says the
missing statistic must be richer than:

```text
- one-point scores,
- fixed motifs,
- monotone cumulative mass,
- simple barycenters,
- or greedy repulsion of local peaks.                                    (41-9)
```

What remains plausible is a genuinely short relational score, for example a
2-step or 3-step pattern energy that can reward a disconnected support while
still tracking the neighboring mass around it.

## 7. Status

```text
proved by probe:
  repulsive greedy terminal selection does not recover the sparse packet except
  in isolated easy cases;

observed:
  the hard zeta-side cases N=12 and N=16 remain unresolved, and N=16 still
  collapses to the wrong singleton;

reduced:
  the live object is not governed by a simple non-monotone proximity penalty;

open:
  find the first genuinely short relational score that can prefer the correct
  disconnected support without reverting to subset search;

next:
  test a 2-step or 3-step pattern energy rather than any greedy local rule.
```
