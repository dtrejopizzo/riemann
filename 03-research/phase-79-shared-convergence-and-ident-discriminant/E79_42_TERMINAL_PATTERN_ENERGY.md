# E79.42 - A short relational energy is still too weak to recover the sparse packet

**Scope:** `GAP-Z` only, first genuinely relational terminal score.  
**Class:** AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** even a short
relational energy that rewards separation among chosen shells does not recover
the sparse packet benchmark. It improves over neither the sparse packet nor the
already-failed ranking family, and in practice often collapses back to nearby
singletons or short contiguous clusters.

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

After E79.41, the next honest family was:

```text
a very short relational energy on supports of size at most 3 inside the last
4 active shells.                                                         (42-1)
```

This is the first probe in the phase that explicitly scores support geometry
rather than ranking shells one by one or using a monotone mass summary.

## 2. Probe

Companion files:

```text
E79_42_TERMINAL_PATTERN_ENERGY_PROBE.py
E79_42_terminal_pattern_energy_results.json
```

Inside the last 4 active shells, for support size `k in {1,2,3}`, the probe
chooses the support maximizing

```text
E(S) = mass(S) - alpha * span(S) + beta * sep(S),                       (42-2)
```

where:

```text
mass(S) = sum_{j in S} |a_j|,
span(S) = max(S)-min(S),
sep(S)  = sum_{i<j in S} |j-i|.                                         (42-3)
```

The tested parameters are

```text
alpha in {0.25, 0.50, 1.0},
beta  in {0.0, 0.25, 0.50, 1.0}.                                        (42-4)
```

The resulting support is then audited against `ZERO^extra` through

```text
|packet - ZERO^extra| / max(|packet|, |ZERO^extra|).                    (42-5)
```

## 3. Result: the relational energy does not recover the benchmark

At `sigma = 1`, zeta gives:

```text
N      sparse packet                  best relational energy
8      {6,7,8}   0.02288             {5}         0.11512
10     {5}       0.02948             {7,8,9}     0.10288
12     {7}       0.02299             {8}         0.03450
14     {10,11,12} 0.02148            {9,11,12}   0.05598
16     {11,13}   0.03554             {10}        0.26619               (42-6)
```

Mean mismatch:

```text
sparse packet      0.02648...
relational energy  0.11494...                                            (42-7)
```

So the energy family is not a viable intrinsic replacement for the sparse
packet benchmark.

## 4. Reading

This is another strong negative result:

```text
the live object is not controlled by a very short mass/span/separation energy
either.                                                                 (42-8)
```

The failures are exactly where they matter:

```text
N=10: the energy prefers a wrong contiguous triple {7,8,9};
N=12: it shifts the singleton from {7} to {8};
N=16: it collapses the disconnected pair {11,13} to the singleton {10}. (42-9)
```

So even after allowing an explicit separation bonus, the family still does not
know how to pick the correct disconnected terminal geometry.

## 5. Plant side

The plant side is at least as unfavorable:

```text
N= 8: sparse 0.0153, energy 0.8749
N=10: sparse 0.0138, energy 0.2455
N=12: sparse 0.8368, energy 0.8368
N=14: sparse 0.7150, energy 0.7150
N=16: sparse 0.8146, energy 0.8146                                      (42-10)
```

So this family is not even a good anatomical summary on that side.

## 6. Consequence

This closes one more candidate family:

```text
the live object is not governed by a short local energy built only from mass,
span, and pairwise separation.                                          (42-11)
```

At this point the phase has ruled out:

```text
- one-point rankings,
- one-step drops,
- fixed motifs,
- cumulative quantiles,
- simple barycenters,
- greedy repulsion,
- short mass/span/separation energies.                                   (42-12)
```

What remains plausible now is something genuinely more contextual, for example:

```text
1. a 2-step or 3-step score tied to neighboring shell transitions rather than
   to support geometry alone,
2. a tiny dynamic-programming selector over the terminal window,
3. a matching functional that uses the common cloud and extra-root together in
   one equation, rather than recovering support from the common cloud alone.  (42-13)
```

## 7. Status

```text
proved by probe:
  a short relational energy based on mass, span, and separation does not
  recover the sparse packet benchmark;

observed:
  the hard zeta-side cases N=10,12,16 remain badly misspecified by this energy;

reduced:
  the live object is not governed by any simple low-complexity support energy
  of the tested form;

open:
  find the first terminal statistic that uses genuinely contextual information
  beyond support geometry alone;

next:
  test either a short dynamic-programming selector on the terminal window or a
  common-cloud/extra-root coupled functional.
```
