# E79.3z - Terminal quantiles are still too monotone to recover the sparse packet

**Scope:** `GAP-Z` only, cumulative terminal statistics for the sparse packet.  
**Class:** AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** cumulative
mass quantiles inside the last few active shells are more elastic than one-point
rankings or a fixed motif dictionary, but they still do not recover the sparse
packet except in isolated cases. So the live terminal object is not determined
by a simple monotone cumulative-mass statistic either.

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

After E79.3y, the next honest candidate was:

```text
an elastic cumulative terminal statistic that can naturally produce singleton,
pair, or triple supports.                                               (Z-1)
```

The simplest such family is given by cumulative mass quantiles in the last few
active shells.

## 2. Probe

Companion files:

```text
E79_3Z_TERMINAL_QUANTILE_PACKET_PROBE.py
E79_3Z_terminal_quantile_packet_results.json
```

Inside the last `W in {4,5,6}` active shells, the probe defines supports by the
shells hit by quantile sets

```text
{0.50},
{0.25,0.75},
{0.25,0.50,0.75},
{0.20,0.50,0.80}.                                                       (Z-2)
```

Then it audits the resulting packet against `ZERO^extra` via

```text
|packet - ZERO^extra| / max(|packet|, |ZERO^extra|).                    (Z-3)
```

## 3. Result: quantiles help once, but fail as a general rule

At `sigma = 1`, zeta gives:

```text
N      sparse packet                  best quantile packet
8      {6,7,8}   0.02288             Q50-W6         {4}        0.04607
10     {5}       0.02948             Q50-W6         {6}        0.07625
12     {7}       0.02299             Q50-W5         {7}        0.02299
14     {10,11,12} 0.02148            Q20Q50Q80-W4   {9,10,11}  0.10765
16     {11,13}   0.03554             Q50-W4         {11}       0.13614   (Z-4)
```

Mean mismatch:

```text
sparse packet   0.02648...
best quantile   0.07782...                                               (Z-5)
```

So quantiles match the sparse packet cleanly only at `N=12`.

## 4. Reading

This is another sharp negative result:

```text
the sparse packet is not determined by a monotone cumulative-mass rule on the
last few shells.                                                        (Z-6)
```

The failures are very revealing:

```text
N=10: quantiles shift the singleton from {5} to {6};
N=14: quantiles force a contiguous triple one shell too early;
N=16: quantiles collapse a disconnected pair {11,13} to the singleton {11}. (Z-7)
```

So even though quantiles are more flexible than fixed motifs, they still impose
too much monotone mass geometry to capture the live object.

## 5. Plant side

The plant side confirms that this family is not the right explanation:

```text
N= 8: sparse 0.0153, quantile 0.8852
N=10: sparse 0.0138, quantile 0.0700
N=12: sparse 0.8368, quantile 0.8368
N=14: sparse 0.7150, quantile 0.7150
N=16: sparse 0.8146, quantile 0.8146                                   (Z-8)
```

So the quantile family is not even a stable anatomical summary on that side.

## 6. Consequence

This closes yet another natural explanation:

```text
the live object is not governed by terminal cumulative mass quantiles either. (Z-9)
```

By now the ledger has ruled out:

```text
- one-point rankings,
- one-step drop rankings,
- fixed motif dictionaries,
- monotone cumulative-mass quantiles.                                   (Z-10)
```

What remains plausible is something more relational, for example:

```text
1. a 2-step or 3-step local pattern score,
2. a terminal moment or barycentric statistic with a non-monotone correction,
3. a short cumulative matching rule that can explicitly prefer disconnected
   support over a monotone interval.                                     (Z-11)
```

## 7. Status

```text
proved by probe:
  terminal quantile packets do not recover the sparse packet except in the
  isolated zeta-side case N=12;

observed:
  the hard zeta-side cases N=14 and N=16 are still badly misspecified by
  monotone cumulative mass rules;

reduced:
  the live object is not determined by terminal cumulative mass quantiles;

open:
  find the first terminal statistic that can prefer disconnected support
  without reverting to unrestricted subset search;

next:
  test a short-pattern or non-monotone barycentric statistic that can deform
  between singleton, contiguous triple, and disconnected pair.
```
