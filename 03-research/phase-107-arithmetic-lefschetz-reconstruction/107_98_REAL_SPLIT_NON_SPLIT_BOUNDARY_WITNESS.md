# 107.98 -- Real split/non-split boundary witness

## 1. Purpose

`107_97` locates the current source row below real local fiber geometry
and below fuller local arithmetic data such as \(c_p\).  There is one
more sharper local distinction visible on actual fibers:
even after fixing the prime, the Kodaira type, and the Tamagawa number,
real bad reduction can still differ through its split versus nonsplit
multiplicative character.

This note exact-checks that finest local boundary on real examples.

## 2. Real objects used here

The verifier `107_98_real_split_non_split_boundary_witness.py` uses a
pinned snapshot of LMFDB local data for two actual elliptic curves over
\(\mathbf Q\):

1. `14.a5 @ p=2`, with
   \(c_2=2\), Kodaira type \(I_2\), and nonsplit multiplicative
   reduction;
2. `489762.dv3 @ p=2`, with
   \(c_2=2\), Kodaira type \(I_2\), and split multiplicative reduction.

So every coarse datum in the current local source row matches:
same prime, same \(\log p\), same fiber type, same basic affine
intersection matrix, same \(c_p\).

## 3. Exact checks performed

The verifier checks:

1. both real fibers lie over the same prime \(p=2\), so the current
   source-side row of `107_04` assigns both exactly the same scalar
   \(\log 2\);
2. both real fibers have the same affine-Dynkin matrix \(I_2\);
3. both real fibers have the same Tamagawa number \(c_2=2\);
4. the real reduction labels still differ:
   one is split multiplicative and the other is nonsplit
   multiplicative.

So the witness isolates the next local boundary:

\[
 \text{source scalar}
 \subsetneq
 \text{fiber geometry}
 \subsetneq
 \text{component-group size}
 \subsetneq
 \text{full local reduction datum}.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All real split/non-split boundary checks passed.
```

So the workspace now contains a reproducible witness that even matching
\(\log p\), Kodaira type, and \(c_p\) still does not exhaust the real
local arithmetic target data.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. the current local source row of `107_04` is much coarser than the
   full real bad-reduction datum;
2. even an eventual refinement that recovered affine fiber geometry and
   \(c_p\) would still not automatically recover all local arithmetic
   structure;
3. the local comparison boundary of Phase 107 is now explicit down to
   split versus nonsplit multiplicative behavior on real fibers.

It does **not** prove:

1. that split/non-split multiplicative structure is exactly the local
   datum Phase 107 must reproduce;
2. any global realization theorem;
3. the terminal identity or RH.

So the correct reading is:

\[
 \text{real split/non-split boundary exact-checked},
 \qquad
 \text{full local target recovery still open}.
 \]
