# E79.3w - The two-block geometry collapses further to a tiny sparse terminal packet

**Scope:** `GAP-Z` only, intrinsic reduction of the deep-edge / extra-root
coupling object.  
**Class:** REDUCCION GENUINA + AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** the best
two-block terminal object can be reduced further to a very small positive-support
packet inside the last few active-edge shells. On the audited zeta ladder this
packet improves the two-block geometry again, especially in the hard `N=12`
case. But it is not yet a clean convergence-side discriminant, because the
planted build also exhibits strong small-packet matches on part of its ladder.

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

E79.3v showed that the best short object was often not a contiguous suffix but a
union of two tiny terminal blocks. The next candid question was whether that was
still too geometric:

```text
is the real object just a very sparse packet on the last few shells?      (W-1)
```

Before probing that, the hard zeta-side cases `N=12` and `N=16` were checked
directly shell by shell. Their active terminal shells are all positive, so the
new object should be sought as a sparse positive-support packet, not as an
alternating signed pattern.

## 2. Probe

Companion files:

```text
E79_3W_TERMINAL_SPARSE_PACKET_PROBE.py
E79_3W_terminal_sparse_packet_results.json
```

For each section, inside the last `M` active shells with

```text
M in {4,5,6},                                                            (W-2)
```

the probe searches supports of size

```text
k in {1,2,3},                                                            (W-3)
```

and picks the packet minimizing

```text
|packet - ZERO^extra| / max(|packet|, |ZERO^extra|).                     (W-4)
```

This is still a brute-force search, but over a much smaller and more intrinsic
class than the two-block geometry.

## 3. Result: the best zeta-side object is now a tiny sparse packet

At `sigma = 1`, zeta gives:

```text
N= 8:  best = W4-K3, support = {6,7,8},   mismatch = 0.02288
N=10:  best = W6-K1, support = {5},       mismatch = 0.02948
N=12:  best = W4-K1, support = {7},       mismatch = 0.02299
N=14:  best = W4-K3, support = {10,11,12}, mismatch = 0.02148
N=16:  best = W4-K2, support = {11,13},   mismatch = 0.03554           (W-5)
```

The decisive comparison is:

```text
N      best two-block   best sparse packet
8      0.02288          0.02288
10     0.00870          0.02948
12     0.20524          0.02299
14     0.02148          0.02148
16     0.03554          0.03554                                         (W-6)
```

Mean mismatch on the audited zeta ladder:

```text
best two-block       0.05877...
best sparse packet   0.02648...                                          (W-7)
```

So the sparse packet is a real further reduction of the live object.

## 4. Reading

The main structural gain is this:

```text
the hard zeta-side cases no longer require "two blocks" as a primitive object.
They collapse to a support of at most two or three individual terminal shells. (W-8)
```

The key cases are especially revealing:

```text
N=12: support = {7}       already captures ZERO^extra to 2.3%
N=16: support = {11,13}   reproduces the disconnected 1+1+1 geometry         (W-9)
```

So the live deep-edge coupling object is now better thought of as:

```text
a tiny sparse terminal packet,
not a terminal suffix,
and not even necessarily two literal blocks.                            (W-10)
```

## 5. But it is not yet a discriminant

The plant side prevents any premature celebration:

```text
N= 8:  best sparse packet mismatch = 0.01528
N=10:  best sparse packet mismatch = 0.01378
N=12:  best sparse packet mismatch = 0.83679
N=14:  best sparse packet mismatch = 0.71504
N=16:  best sparse packet mismatch = 0.81458                            (W-11)
```

So the planted build shows a split behavior:

```text
small-packet matches can be excellent at low N,
then collapse badly later.                                              (W-12)
```

That means:

```text
the sparse packet is an excellent anatomical reduction,
but not yet an admissible convergence-side separator.                   (W-13)
```

This is exactly the kind of candid outcome the phase needs.

## 6. Consequence

The live object sharpens once more:

```text
COMMON-GAP-Z
  = [broad shallow/middle package]
    + [tiny sparse terminal packet - ZERO^extra]
    + [tiny interior remainder].                                        (W-14)
```

This is the smallest finite object reached so far on the common-cloud side.

The candid next question is now very narrow:

```text
what intrinsic terminal statistic picks out that sparse support,
without brute-force subset search?                                      (W-15)
```

Plausible next candidates are:

```text
1. a terminal shell ranking by local contribution-to-extra,
2. a sparse packet extracted from drop points of the shell profile,
3. a one-point or two-point terminal moment that reproduces the same support. (W-16)
```

## 7. Status

```text
proved by probe:
  the best short two-block object reduces further to a tiny sparse terminal
  packet on the audited zeta ladder;

observed:
  the zeta-side hard case N=12 collapses dramatically, from 0.205 to 0.023,
  under the sparse-packet reduction;

observed:
  the planted build also has strong sparse-packet matches at low N, so this is
  not yet a clean discriminant or theorem-grade selector;

reduced:
  the live deep-edge / extra-root coupling object from "two-block terminal
  object" to "tiny sparse terminal packet";

open:
  identify an intrinsic non-combinatorial statistic that reproduces the same
  sparse support;

next:
  test terminal ranking or moment rules that recover the sparse packet without
  subset search.
```
