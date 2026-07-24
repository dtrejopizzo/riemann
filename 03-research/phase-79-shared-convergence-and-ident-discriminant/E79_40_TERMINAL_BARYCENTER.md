# E79.40 - Simple terminal barycenters are still too monotone

**Scope:** `GAP-Z` only, relational terminal selectors beyond quantiles.  
**Class:** AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** a terminal
barycenter with a minimal dispersion correction behaves no better than the
terminal quantile rules. It can recover the isolated `N=12` singleton, but it
still misses the hard `N=14` and `N=16` zeta-side geometry. So the live object
is not governed by a simple center-of-mass rule either.

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

After E79.3z, the natural next candidate was:

```text
a terminal center-of-mass or barycentric statistic, perhaps widened by a small
dispersion estimate.                                                     (40-1)
```

This is the simplest relational statistic that is more flexible than one-point
rankings or quantile cuts while still avoiding subset search.

## 2. Probe

Companion files:

```text
E79_40_TERMINAL_BARYCENTER_PROBE.py
E79_40_terminal_barycenter_results.json
```

Inside the last `W in {4,5,6}` active shells, the probe computes the mass
barycenter and variance of the absolute shell profile, then tests four support
templates:

```text
B1         = nearest shell to the barycenter,
B2adj      = nearest adjacent pair around the barycenter,
Bdisp      = barycenter plus one radius from the local dispersion,
Bfloorceil = floor/ceil pair around the barycenter.                      (40-2)
```

Each template is audited against `ZERO^extra` through

```text
|packet - ZERO^extra| / max(|packet|, |ZERO^extra|).                     (40-3)
```

## 3. Result: barycenter selectors do not beat the sparse packet

At `sigma = 1`, zeta gives:

```text
N      sparse packet                  best barycenter rule
8      {6,7,8}   0.02288             B1-W6      {4}         0.04607
10     {5}       0.02948             B1-W6      {6}         0.07625
12     {7}       0.02299             B1-W5      {7}         0.02299
14     {10,11,12} 0.02148            Bdisp-W4   {9,10,11}   0.10765
16     {11,13}   0.03554             B1-W4      {11}        0.13614    (40-4)
```

Mean mismatch:

```text
sparse packet   0.02648...
best bary       0.07782...                                                (40-5)
```

So the barycenter family is not an improvement. It is effectively in the same
class as the terminal quantile rules.

## 4. Reading

The failures are the important part:

```text
N=10: the barycenter shifts the singleton from {5} to {6};
N=14: the dispersion template forces the contiguous triple one shell too early;
N=16: the barycenter collapses the disconnected pair {11,13} to {11}.   (40-6)
```

This is a clean negative result:

```text
the live terminal object is not determined by a simple center-of-mass rule,
even with a first dispersion correction.                                 (40-7)
```

So the packet geometry is not just “where the terminal mass sits on average.”

## 5. Plant side

The plant side behaves in the same spirit, and often worse:

```text
N= 8: sparse 0.0153, bary 0.8852
N=10: sparse 0.0138, bary 0.2733
N=12: sparse 0.8368, bary 0.8368
N=14: sparse 0.7150, bary 0.7150
N=16: sparse 0.8146, bary 0.8146                                        (40-8)
```

So the barycenter family is not a useful anatomical summary on that side either.

## 6. Consequence

This closes one more whole family of natural explanations:

```text
the live object is not governed by
  - one-point scores,
  - fixed motifs,
  - cumulative mass quantiles,
  - or simple terminal barycenters.                                      (40-9)
```

What remains plausible is something more explicitly non-monotone and
pattern-sensitive, for example:

```text
1. a short 2-step or 3-step relational score,
2. a non-monotone barycentric correction that can prefer gaps,
3. a cumulative matching rule that explicitly rewards disconnected support. (40-10)
```

## 7. Status

```text
proved by probe:
  simple barycenter and barycenter-plus-dispersion selectors do not recover the
  sparse packet except in the isolated N=12 zeta case;

observed:
  the hard zeta-side cases N=14 and N=16 remain badly misspecified by simple
  center-of-mass geometry;

reduced:
  the live object is not determined by a monotone center-of-mass statistic;

open:
  find the first non-monotone relational statistic that can prefer the
  disconnected support when needed;

next:
  test a short 2-step or 3-step relational score rather than any monotone mass
  or barycentric selector.
```
