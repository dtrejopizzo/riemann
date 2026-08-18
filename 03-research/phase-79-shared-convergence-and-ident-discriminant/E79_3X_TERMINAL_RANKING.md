# E79.3x - Amplitude and drop-point rankings are too crude to recover the sparse packet

**Scope:** `GAP-Z` only, intrinsic recovery of the sparse terminal packet.  
**Class:** AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** the sparse
terminal packet of E79.3w cannot be explained by the cheapest internal ranking
rules. Neither "pick the largest terminal shells" nor "pick the shells before
the biggest local drops" reproduces the good zeta-side packet geometry except in
isolated cases.

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

E79.3w reduced the zeta-side common-cloud object to a tiny sparse packet on the
last few active shells. The next candid question was:

```text
can that packet be recovered by a simple terminal ranking rule, without any
subset search?                                                          (X-1)
```

The two simplest admissible candidates were:

```text
1. amplitude ranking: keep the largest terminal shells;
2. drop-point ranking: keep the shells immediately before the largest local
   backward drops.                                                      (X-2)
```

## 2. Probe

Companion files:

```text
E79_3X_TERMINAL_RANKING_PROBE.py
E79_3X_terminal_ranking_results.json
```

Inside the last `W in {4,5,6}` active shells, for each `k in {1,2,3}`, the
probe builds:

```text
A-W-K  = top-k by shell amplitude,
D-W-K  = top-k by backward drop magnitude.                              (X-3)
```

Then it audits each rule against `ZERO^extra` via

```text
|packet - ZERO^extra| / max(|packet|, |ZERO^extra|).                    (X-4)
```

The ranking rule itself does not look at `ZERO^extra`; the latter enters only in
the audit.

## 3. Result: the best ranking rules are worse than the sparse packet

At `sigma = 1`, zeta gives:

```text
N      best sparse packet               best ranking rule
8      {6,7,8}   0.02288               A-W5-K1   {4}        0.04607
10     {5}       0.02948               A-W6-K1   {5}        0.02948
12     {7}       0.02299               A-W4-K1   {8}        0.03450
14     {10,11,12} 0.02148              D-W4-K3   {9,11,12} 0.05598
16     {11,13}   0.03554               A-W4-K1   {10}       0.26619        (X-5)
```

Mean mismatch on the audited zeta ladder:

```text
sparse packet    0.02648...
best ranking     0.08644...                                                (X-6)
```

So the ranking rules are not just slightly worse. They miss the geometry in the
cases that matter most.

## 4. Reading

The failures are instructive:

```text
N=12: the correct shell is {7}, but amplitude ranking chooses {8};
N=14: the correct 3-shell packet is contiguous, but drop ranking injects an
      earlier shell {9};
N=16: amplitude ranking collapses to {10} and misses the disconnected support
      {11,13} entirely.                                                  (X-7)
```

This gives a clean negative conclusion:

```text
the sparse packet is not determined by raw terminal amplitude alone,
and not by the largest local drops alone either.                        (X-8)
```

So the packet support carries a more delicate terminal statistic than either of
those one-dimensional rankings.

## 5. Plant side

The plant side tells the same story in a different way.

Only one case lines up cleanly:

```text
N=10: D-W5-K3 reproduces the sparse packet exactly.                      (X-9)
```

But elsewhere the ranking rules are poor or trivial:

```text
N= 8: best ranking mismatch = 0.8852 vs sparse 0.0153
N=12: both collapse to the trivial first shell
N=14: both collapse to the trivial first two shells
N=16: both collapse to the trivial first shell.                         (X-10)
```

So there is no clean ranking law hiding in the plant either.

## 6. Consequence

This removes another whole class of cheap explanations:

```text
the live object is not "top terminal amplitudes",
and not "top terminal drop points".                                     (X-11)
```

The next intrinsic rules must therefore be slightly richer, for example:

```text
1. a terminal moment or center-of-mass rule,
2. a rule based on two-step or three-step local patterns rather than one-point
   scores,
3. a statistic that can prefer a disconnected support over a single local
   maximum.                                                              (X-12)
```

## 7. Status

```text
proved by probe:
  amplitude ranking and drop-point ranking do not recover the sparse packet
  geometry except in isolated cases;

observed:
  the zeta-side hard cases N=12 and N=16 remain unresolved by these cheapest
  internal ranking rules;

reduced:
  the live object cannot be explained by a one-point terminal score;

open:
  find the first intrinsic statistic that can prefer the correct sparse support,
  including disconnected support;

next:
  test terminal moment or short-pattern rules that are richer than amplitude
  or one-step drop rankings, but still far smaller than subset search.
```
