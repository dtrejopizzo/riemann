# 107.96 -- Real component-group boundary witness

## 1. Purpose

`107_93`, `107_94`, and `107_95` already isolate real local bad-fiber
geometry and the standard \(\log p\) weighting.  One more local target-
side distinction is immediately visible on actual elliptic curves over
\(\mathbf Q\):
the affine-Dynkin intersection matrix of a bad fiber does not by itself
exhaust the arithmetic local data, because the Tamagawa number
\(c_p\) can still differ from what the raw component geometry suggests.

This note exact-checks that boundary on real examples.

## 2. Real objects used here

The verifier `107_96_real_component_group_boundary_witness.py` uses the
same pinned local-data snapshots already confirmed from LMFDB for:

1. `14.a1 @ p=2`, with Kodaira type \(I_9\), nonsplit multiplicative,
   and Tamagawa number \(c_2=1\);
2. `14.a1 @ p=7`, with Kodaira type \(I_2\), split multiplicative, and
   Tamagawa number \(c_7=2\);
3. `14.a5 @ p=2`, with Kodaira type \(I_2\), nonsplit multiplicative,
   and Tamagawa number \(c_2=2\).

These are genuine local fibers of genuine elliptic curves over
\(\mathbf Q\).

## 3. Exact checks performed

The verifier:

1. constructs the affine-Dynkin intersection matrices for the real
   fibers \(I_9\) and \(I_2\);
2. computes an exact reduced cofactor witness for each matrix by deleting
   one row and one column;
3. checks that the reduced \(I_2\) cofactor equals \(2\), matching the
   Tamagawa number in both the split and nonsplit `I_2` examples;
4. checks that the reduced \(I_9\) cofactor equals \(9\), while the real
   nonsplit `I_9` example has Tamagawa number \(c_2=1\);
5. records therefore that local target-side data contains more than the
   affine intersection geometry and the scalar \(\log p\) weight alone.

So the witness isolates the next local arithmetic boundary:

\[
 \text{fiber geometry}
 \neq
 \text{full local arithmetic datum}.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All real component-group boundary checks passed.
```

So the workspace now contains a reproducible local witness that the real
finite-place target data of bad fibers contains arithmetic information
beyond the current affine intersection matrix and its \(\log p\)
weighting.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. even after passing to real local bad-fiber geometry, one has not yet
   captured all local target-side arithmetic data;
2. the current Phase 107 local source row is therefore still farther
   from the full real local target than the \(\log p\)-comparison alone
   might suggest;
3. the local arithmetic boundary is now written as an exact statement on
   genuine fibers.

It does **not** prove:

1. any global realization theorem;
2. that Tamagawa numbers themselves are the exact local invariant Phase
   107 must reproduce;
3. the terminal identity or RH.

So the correct reading is:

\[
 \text{real local geometry-vs-arithmetic boundary exact-checked},
 \qquad
 \text{full local target recovery still open}.
 \]
