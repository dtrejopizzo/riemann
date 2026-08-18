# E79.3y - A tiny terminal pattern dictionary still does not explain the sparse packet

**Scope:** `GAP-Z` only, terminal motif reduction beyond one-point scores.  
**Class:** AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** even a small
dictionary of short terminal motifs does not recover the sparse packet of
E79.3w. So the live terminal object is not just one of a few fixed motifs such
as `111`, `101`, or a single distinguished site inside the last 4-6 shells.

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

After E79.3x, the cheapest one-point terminal scores were dead. The next
natural compression was:

```text
maybe the sparse packet is not arbitrary, but belongs to a tiny dictionary of
short terminal motifs.                                                   (Y-1)
```

The minimal useful dictionary was taken to include:

```text
- one distinguished site in the last 4 or 6 shells,
- a contiguous triple,
- a disconnected 101 pair,
- a couple of 2-shell tail/middle pairs.                                (Y-2)
```

## 2. Probe

Companion files:

```text
E79_3Y_TERMINAL_PATTERN_DICTIONARY_PROBE.py
E79_3Y_terminal_pattern_dictionary_results.json
```

The tested motif family was:

```text
P1-left-W6   = {leftmost site in last 6}
P1-mid-W4    = {middle site in last 4}
P111-W4      = {0,1,2 in last 4}
P101-W4      = {0,2 in last 4}
P11-tail-W4  = {2,3 in last 4}
P11-mid-W4   = {1,2 in last 4}.                                         (Y-3)
```

Each motif is audited by

```text
|motif-packet - ZERO^extra| / max(|motif-packet|, |ZERO^extra|).         (Y-4)
```

## 3. Result: the motif dictionary is still too rigid

At `sigma = 1`, zeta gives:

```text
N      sparse packet                   best motif
8      {6,7,8}    0.02288             P101-W4   {5,7}        0.02561
10     {5}        0.02948             P1-left-W6 {5}         0.02948
12     {7}        0.02299             P1-mid-W4 {8}          0.03450
14     {10,11,12} 0.02148             P111-W4   {9,10,11}    0.10765
16     {11,13}    0.03554             P1-mid-W4 {11}         0.13614    (Y-5)
```

Mean mismatch:

```text
sparse packet   0.02648...
best motif      0.06668...                                               (Y-6)
```

So the motif dictionary is plainly worse than the sparse packet benchmark.

## 4. Reading

The failures are informative:

```text
N=10 is the only clean hit.
N=12 is close, but the motif picks the wrong singleton.
N=14 misses badly by forcing the contiguous triple one shell too early.
N=16 misses badly by forcing a one-point motif and losing the disconnected
     support {11,13}.                                                    (Y-7)
```

This gives another clean negative conclusion:

```text
the sparse packet is not determined by membership in a tiny fixed motif
dictionary either.                                                       (Y-8)
```

So the support depends on a slightly more elastic terminal statistic than a
fixed catalog can encode.

## 5. Plant side

The plant side is even less favorable to the motif explanation:

```text
N= 8: sparse 0.0153, motif 0.4138
N=10: sparse 0.0138, motif 0.4488
N=12: sparse 0.8368, motif 0.8368
N=14: sparse 0.7150, motif 0.7150
N=16: sparse 0.8146, motif 0.8146                                      (Y-9)
```

So the tiny pattern dictionary is not even a good anatomical summary there.

## 6. Consequence

This removes one more cheap structural explanation:

```text
the live object is not a fixed tiny motif catalog on the last 4-6 shells. (Y-10)
```

Combined with E79.3x, that means the next candidates must be richer than:

```text
- one-point scores,
- one-step drop scores,
- fixed motif dictionaries.                                              (Y-11)
```

What remains plausible is something like:

```text
1. a terminal moment/center-of-mass rule,
2. a 2-step or 3-step score that can deform continuously between singleton,
   contiguous triple, and disconnected pair,
3. a terminal statistic tied to cumulative matching rather than fixed motifs. (Y-12)
```

## 7. Status

```text
proved by probe:
  a tiny terminal motif dictionary does not recover the sparse packet except in
  isolated cases;

observed:
  the zeta-side cases N=14 and N=16 remain badly misspecified by fixed motifs;

reduced:
  the live object cannot be compressed to a fixed motif catalog on the last
  4-6 shells;

open:
  find the first terminal statistic that is flexible enough to reproduce both
  contiguous and disconnected sparse supports;

next:
  test terminal moment or cumulative-matching statistics that can move
  continuously between those support types.
```
