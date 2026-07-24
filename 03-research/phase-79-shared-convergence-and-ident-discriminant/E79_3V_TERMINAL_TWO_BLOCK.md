# E79.3v - Two short terminal blocks beat every contiguous suffix tested so far

**Scope:** `GAP-Z` only, deep-edge / extra-root coupling beyond a single
contiguous suffix.  
**Class:** REDUCCION GENUINA + AUTOPSIA HONESTA.  
**What we know after this document that we did not know before:** the best
coupling object on the audited zeta ladder is often not one contiguous terminal
tail at all. Allowing a union of two short terminal blocks, separated by a tiny
gap, improves the pairing sharply and beats every contiguous suffix family
tested so far.

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

After E79.3u, the live ambiguity had become very tight:

```text
all suffix-based selectors looked too rigid.                             (V-1)
```

The good cancellations were real, but one contiguous suffix kept failing in the
same places. The smallest admissible next object was therefore:

```text
a union of two short terminal blocks, with a tiny gap allowed between them. (V-2)
```

This is the first object in the phase that is more global than a single suffix,
but still finite, explicit, and purely combinatorial on the active edge shells.

## 2. Probe

Companion files:

```text
E79_3V_TERMINAL_TWO_BLOCK_PROBE.py
E79_3V_terminal_two_block_results.json
```

Inside the active `99%` common edge, the probe searches unions of the form

```text
[one short block] + [tiny gap] + [last short block],                    (V-3)
```

with

```text
first-block length  in {1,2,3},
gap length          in {0,1,2},
last-block length   in {1,2,3}.                                         (V-4)
```

For each combination, it measures

```text
|two-block sum - ZERO^extra| / max(|two-block sum|, |ZERO^extra|).      (V-5)
```

## 3. Result: the two-block object is the best short object so far

At `sigma = 1`, zeta gives:

```text
N= 8:  best = 1+0+2, mismatch = 0.02288
N=10:  best = 1+0+3, mismatch = 0.00870
N=12:  best = 1+2+1, mismatch = 0.20524
N=14:  best = 1+0+2, mismatch = 0.02148
N=16:  best = 1+1+1, mismatch = 0.03554                            (V-6)
```

The comparison with the best contiguous objects is the decisive point:

```text
N      hybrid best   best tail sweep   best two-block
8      0.8422        0.02288           0.02288
10     0.00870       0.00870           0.00870
12     0.4762        0.3588            0.2052
14     0.02148       0.02148           0.02148
16     0.1569        0.4141            0.03554                      (V-7)
```

Mean mismatch over the audited zeta ladder:

```text
hybrid contiguous suffix   0.3011...
best tail sweep            0.1652...
best two-block             0.0588...                                 (V-8)
```

So this is not just a cosmetic variant. It is a real geometric improvement.

## 4. Reading

The phase has now crossed a structural threshold:

```text
the deep-edge / extra-root cancellation is not, in general, a one-suffix
phenomenon.                                                            (V-9)
```

Two concrete signatures show up:

```text
1. In the easy cases (N=8,10,14), the best two-block object collapses back to
   the same best contiguous terminal tail.
2. In the hard cases (N=12,16), the best object is genuinely disconnected:
      N=12 -> 1+2+1
      N=16 -> 1+1+1.                                                  (V-10)
```

This is exactly the kind of mixed behavior one would expect if the right object
is a short signed profile carried by a few terminal sites, rather than by one
solid suffix.

## 5. What the plant says

The plant does not exhibit a comparable clean law:

```text
N= 8: best mismatch = 0.8749
N=10: best mismatch = 0.0700
N=12: no admissible two-block combo in the tiny active edge
N=14: best mismatch = 0.7150
N=16: no admissible two-block combo                                    (V-11)
```

This is not yet a discriminant theorem, and it must not be used as one on the
convergence side. But it is useful anatomy:

```text
the two-block geometry that sharpens the zeta side does not produce a parallel
stable pattern on the plant ladder.                                     (V-12)
```

## 6. Consequence

The live object sharpens again:

```text
COMMON-GAP-Z
  = [shallow + middle package]
    + [two-block terminal object - ZERO^extra]
    + [tiny interior remainder].                                        (V-13)
```

This is better than every previous tail selector because it explains the hard
cases `N=12` and `N=16` that one contiguous suffix could not.

The honest next question is now:

```text
is there an intrinsic signed moment or profile rule whose value is exactly this
two-block terminal object, without brute-force combinatorial search?     (V-14)
```

Likely next candidates:

```text
1. a signed 2-point or 3-point terminal moment,
2. a tiny terminal alternating packet rather than a raw suffix,
3. a selector built from the terminal shell signs and the short gaps between
   them, not from cumulative tail length.                                (V-15)
```

## 7. Status

```text
proved by probe:
  allowing a union of two short terminal blocks beats every contiguous suffix
  family tested so far on the audited zeta ladder;

observed:
  the hard cases N=12 and N=16 are genuinely disconnected:
  their best objects are 1+2+1 and 1+1+1 rather than one suffix;

reduced:
  the live deep-edge / extra-root coupling object from "best short suffix" to
  "best short two-block terminal object";

open:
  identify the intrinsic non-combinatorial rule behind that two-block object;

next:
  test whether a tiny signed terminal moment/packet reproduces the same
  two-block geometry without brute-force block search.
```
