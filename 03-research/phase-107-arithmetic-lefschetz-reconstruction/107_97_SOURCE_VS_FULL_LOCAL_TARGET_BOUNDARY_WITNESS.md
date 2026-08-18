# 107.97 -- Source-vs-full-local-target boundary witness

## 1. Purpose

`107_95` shows, on real local fibers, that the current source-side row
of `107_04` captures the scalar \(\log p\) layer but not the local
fiber geometry.  `107_96` then shows that even the real affine-fiber
geometry does not exhaust the full local arithmetic datum.

This note packages those two real boundaries into one exact local
comparison witness.

## 2. Objects compared

The verifier `107_97_source_vs_full_local_target_boundary_witness.py`
compares:

1. the current source-side local law of `107_04`, namely the scalar
   \(\log p\);
2. the real target-side local geometry represented by affine-Dynkin
   bad-fiber intersection matrices;
3. the additional real local arithmetic datum represented here by the
   Tamagawa number \(c_p\).

The pinned real examples are:

1. `14.a5 @ p=2`, with type \(I_2\) and \(c_2=2\);
2. `14.a1 @ p=2`, with type \(I_9\) and \(c_2=1\);
3. `102.a1 @ p=3`, with type \(I_2\) and \(c_3=2\).

## 3. Exact checks performed

The verifier checks:

1. at the source level, both real fibers above \(p=2\) receive exactly
   the same scalar \(\log 2\);
2. at the target geometric level, those same fibers have different
   affine-Dynkin intersection matrices \(I_2\) and \(I_9\);
3. at the fuller local arithmetic level, the same prime \(p=2\) also
   carries different Tamagawa data \(c_2=2\) and \(c_2=1\) on those
   two fibers;
4. repeated real \(I_2\) fibers at \(p=2\) and \(p=3\) have the same
   underlying geometry and the same \(c_p=2\), while only the scalar
   source weight changes from \(\log 2\) to \(\log 3\).

So the witness records the full current local comparison boundary:

\[
 \text{current source row} \subsetneq
 \text{real local geometry} \subsetneq
 \text{full local target datum}.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All source-vs-full-local-target boundary checks passed.
```

So the workspace now contains a reproducible local witness locating the
current Phase 107 source row strictly below the full local arithmetic
target.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. the current finite source row of `107_04` still captures only the
   scalar prime-weight layer;
2. recovering real local fiber geometry would already require more than
   the present source row provides;
3. even recovering real local fiber geometry would still not exhaust the
   full local arithmetic datum visible on actual bad fibers.

It does **not** prove:

1. that the full local target datum is exactly what Phase 107 must
   reproduce;
2. any global realization theorem;
3. the terminal identity or RH.

So the correct reading is:

\[
 \text{real local source-vs-full-target boundary exact-checked},
 \qquad
 \text{full local target recovery still open}.
 \]
