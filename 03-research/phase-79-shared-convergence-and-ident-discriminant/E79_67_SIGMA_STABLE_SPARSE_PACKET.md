# E79.67 - On the zeta ladder, the best sparse terminal packet is sigma-stable

**Scope:** `GAP-Z` only, transport of the sparse terminal packet across the safe
axis.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the sparse
packet isolated in E79.3w is not just a sectionwise accident at one sampled
point. On the audited zeta ladder, the same best terminal support is selected at
`sigma = 1` and `sigma = 2` in every case. So the live object sharpens from
"best sparse packet at one sigma" to "sigma-transported sparse packet" on the
zeta side.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only previously audited sparse-packet / two-block data.
E72.16/E77.7az: respected. The reduction is made on the convergence side and is
                stated only as zeta-side structure; plant instability is
                recorded as anatomy, not as a forcing separator.
Circularity: respected. Everything comes from existing `spec(K_N)` bookkeeping.
```

## 1. Why this is the next candid question

E79.3w reduced the common-cloud side to a tiny sparse terminal packet, but only
sectionwise and primarily at `sigma = 1`. The next admissible question is:

```text
does that packet persist as sigma moves on the safe axis,
or is it just a one-sigma combinatorial coincidence?                    (67-1)
```

If the support moves wildly with sigma, then the sparse packet is still too raw
to count as a structural object. If it stays put, the reduction becomes much
stronger.

## 2. Probe

Companion files:

```text
E79_67_SIGMA_STABLE_SPARSE_PACKET_probe.py
E79_67_sigma_stable_sparse_packet_results.json
```

The probe re-reads the audited outputs of:

```text
E79.3v  (best two-block terminal object),
E79.3w  (best sparse terminal packet),                                  (67-2)
```

and compares, for each section and each build, the best object at:

```text
sigma = 1, 2.                                                           (67-3)
```

It records:

```text
1. whether the best sparse support is identical at both sigmas,
2. whether the best sparse rule name is identical at both sigmas,
3. whether the sparse packet matches the best two-block object in effective
   mismatch quality at each sigma.                                       (67-4)
```

## 3. Result: exact sigma-stability on the zeta ladder

For zeta, the best sparse support is identical at `sigma = 1` and `sigma = 2`
for every audited section:

```text
N= 8:  {6,7,8}       at both sigmas
N=10:  {5}           at both sigmas
N=12:  {7}           at both sigmas
N=14:  {10,11,12}    at both sigmas
N=16:  {11,13}       at both sigmas.                                    (67-5)
```

So the zeta summary is:

```text
sigma-stable support count = 5 / 5,
sigma-stable rule count    = 5 / 5.                                     (67-6)
```

The mismatches stay in the same small band:

```text
sigma=1:  0.0229, 0.0295, 0.0230, 0.0215, 0.0355
sigma=2:  0.0274, 0.0269, 0.0205, 0.0242, 0.0334.                      (67-7)
```

So the support stability is not bought by sacrificing the quality of the match.

## 4. Reading

This is a genuine strengthening of E79.3w.

The sparse packet is no longer just:

```text
"the best tiny support found by brute force at sigma = 1".              (67-8)
```

It is now:

```text
"a terminal support that transports rigidly across the sampled safe sigmas on
 the zeta ladder."                                                       (67-9)
```

That matters because the whole `GAP-Z` object is a local-uniform-in-sigma
statement. Any finite reduction that collapses immediately when sigma moves is
too brittle to be load-bearing. This one survives that first transport test.

## 5. Relation to the two-block geometry

On the zeta ladder, the best sparse packet matches the best two-block quality
at both sigmas in:

```text
N=8,14,16.                                                               (67-10)
```

Two important exceptions remain:

```text
N=10: the sparse packet is slightly worse than the best two-block object,
      though still sigma-stable;
N=12: the sparse packet is strictly better than the best two-block object,
      and this improvement is sigma-stable as well.                      (67-11)
```

So the correct picture is:

```text
the sigma-stable object is already sparse;
the two-block geometry is mostly a temporary wrapper around the same support,
except for one case where sparsification genuinely improves it.          (67-12)
```

## 6. What the plant says

The plant does **not** show comparable sigma-stability:

```text
N= 8: support changes from {10,11} to {6,7,11}
N=10: support changes from {11,13,15} to {0}
N=12: support changes from {0} to {0,1}
N=14: support stays {0,1}
N=16: support changes from {0} to {0,1}.                                (67-12)
```

This is useful anatomy, but by the E72.16 / E77.7az discipline it is not to be
used as a convergence-side forcing step. The admissible takeaway is only:

```text
the zeta-side sparse packet has a transport rigidity that is absent in the
falsifier data.                                                          (67-13)
```

## 7. Consequence

The live common-cloud object sharpens once more:

```text
COMMON-GAP-Z
  = [broad shallow/middle package]
    + [sigma-stable sparse terminal packet - ZERO^extra]
    + [tiny interior remainder].                                         (67-14)
```

This is better than E79.3w because it upgrades the packet from a one-sigma
artifact to a transported terminal support.

The next candid question is now narrower:

```text
which intrinsic terminal statistic picks out that same sigma-stable support,
without brute-force subset search?                                       (67-15)
```

At this point the candidate rule should probably be sigma-aware but support-rigid
rather than purely amplitude-based.

## 8. Status

```text
proved by probe:
  on the audited zeta ladder, the best sparse terminal packet has exactly the
  same support at sigma = 1 and sigma = 2 in every tested section;

clarified:
  the two-block geometry is mostly an intermediate wrapper around the same
  sparse support, except for the mild zeta-side exception N=10;

observed:
  the plant does not display comparable support stability under sigma
  transport, but this remains anatomical rather than forcing information;

reduced:
  the live common-cloud object from "best sparse packet at one sigma" to
  "sigma-stable sparse packet on the zeta ladder";

open:
  identify the intrinsic support rule behind that sigma-stable packet;

next:
  test whether a sigma-aware terminal prominence or short-range curvature score
  recovers the same support without subset search.
```
