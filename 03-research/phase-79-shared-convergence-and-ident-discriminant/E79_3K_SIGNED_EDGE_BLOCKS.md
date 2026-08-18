# E79.3k - The active zeta edge is locally sign-coherent

**Scope:** `GAP-Z` only, signed local cancellation inside the active edge.  
**Class:** AUTOPSIA UTIL + REDUCCION FRANCA.  
**What we know after this document that we did not know before:** on the zeta
side, the active edge does not hide meaningful cancellation at the scale of
neighboring shells or short local blocks. The edge is locally coherent in sign.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct cloud bookkeeping only.
E72.16/E77.7az: respected. Convergence-side anatomy only.
Circularity: respected. Everything is computed from spec(K_N).
```

## 1. Starting point

After E79.3j, the main surviving suspicion was:

```text
maybe the missing gain does not appear in absolute-value profiles because it is
hidden in signed cancellation between nearby edge shells.               (T-1)
```

That is the most natural remaining local mechanism once width and normalized
shape have both been audited.

## 2. Probe

Companion files:

```text
E79_3K_SIGNED_EDGE_BLOCKS_PROBE.py
E79_3K_signed_edge_blocks_results.json
```

Inside the active edge of width `m_theta(N)`, the probe compares the absolute
edge mass against four signed reductions:

```text
1. pair blocks      (size 2),
2. quad blocks      (size 4),
3. alternating sum,
4. full signed sum.                                                    (T-2)
```

The key ratios are

```text
pair_abs / abs_mass,
quad_abs / abs_mass,
alt_abs  / abs_mass,
signed_total / abs_mass.                                               (T-3)
```

If substantial local cancellation were present, the pair/quad ratios would drop
well below `1`.

## 3. Result: no local block cancellation on the zeta side

At `sigma = 1`, for the `theta = 0.9` edge, zeta gives:

```text
N    pair/abs   quad/abs   alt/abs      signed/abs
8    1.0        1.0        0.08166      1.0
10   1.0        1.0        0.01916      1.0
12   1.0        1.0        0.06277      1.0
14   1.0        1.0        0.02757      1.0
16   1.0        1.0        0.02976      1.0
18   1.0        1.0        0.02795      1.0
20   1.0        1.0        0.06485      1.0
22   1.0        1.0        0.05057      1.0
24   1.0        1.0        0.05231      1.0
```

This is the decisive local-cancellation fact:

```text
on the zeta side, the active edge is fully coherent in sign at pair and
size-4 block scales.                                                   (T-4)
```

There is essentially no cancellation whatsoever in those local reductions.

The only mild reduction comes from the alternating sum:

```text
mean(alt/abs) = 0.0463...
range         = 0.0192 ... 0.0817.                                     (T-5)
```

The same conclusion persists for the tighter `theta = 0.99` edge, where the
alternating ratio is even smaller on several steps, but pair and quad ratios
still stay exactly `1`.

## 4. Reading

This is a very useful autopsy:

```text
the missing gain is not hidden in obvious shell-by-shell oscillation or in
short-range signed block cancellation inside the active edge.           (T-6)
```

What the alternating ratio does show is that the edge profile is smooth enough
that a rapidly oscillating sign pattern would cancel strongly if it existed. But
the actual zeta edge does not realize that pattern: it stays overwhelmingly of
one sign locally.

So the local edge picture is now quite rigid:

```text
wide,
N^-2 per shell,
moderate profile taper,
and locally sign-coherent.                                             (T-7)
```

## 5. Plant is again structurally different

The planted build behaves differently at small `N`, where pair and quad ratios
can be well below `1`. But that regime is irregular and eventually collapses to
the trivial one-shell picture on parts of the ladder.

So the planted data again serve mainly as contrast, not as a stable law.

## 6. Consequence

The live object sharpens one more time:

```text
COMMON-GAP-Z
  = [locally sign-coherent linear edge width]
    x [local N^-2 shell profile with a broad plateau]
    + [tiny interior correction].                                       (T-8)
```

This rules out another plausible hiding place for the missing summability gain.
At this point the remaining candidates are more global and more delicate:

```text
1. cancellations only visible on longer block scales,
2. coupling between the broad plateau and the tiny interior correction,
3. a nonlocal identity tying the edge package to the extra-root term or to
   another build-neutral piece of ZERO.                                 (T-9)
```

## 7. Status

```text
proved by probe:
  the zeta-side active edge has no meaningful pairwise or short-block signed
  cancellation; it is locally sign-coherent;

observed:
  only the alternating test shows a small reduction, consistent with smoothness
  rather than genuine oscillatory cancellation;

reduced:
  the missing summability gain cannot come from naive local signed
  cancellation inside the edge either;

open:
  search for a more global cancellation or coupling mechanism than any local
  shell/block profile can see;

next:
  test longer block scales and compare the signed edge package against the tiny
  interior correction and the extra-root term.
```
