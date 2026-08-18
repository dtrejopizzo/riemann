# 107.99 -- Real local information hierarchy witness

## 1. Purpose

`107_93` through `107_98` established several real local boundaries one
by one:
the current source row sees the scalar \(\log p\), real fibers add
Kodaira geometry, real local arithmetic adds \(c_p\), and even that
still does not determine split versus nonsplit reduction.

This note packages those real local witnesses into one exact hierarchy
of information.

## 2. Real examples used here

The verifier `107_99_real_local_information_hierarchy_witness.py` uses
the following pinned real local data already confirmed from LMFDB:

1. `14.a5 @ p=2`: \(I_2\), \(c_2=2\), nonsplit multiplicative;
2. `489762.dv3 @ p=2`: \(I_2\), \(c_2=2\), split multiplicative;
3. `14.a1 @ p=2`: \(I_9\), \(c_2=1\), nonsplit multiplicative;
4. `102.a1 @ p=3`: \(I_2\), \(c_3=2\), nonsplit multiplicative.

These four fibers are enough to separate the local layers currently
visible in Phase 107.

## 3. Exact checks performed

The verifier defines four local information layers:

1. source scalar layer: \(p \mapsto \log p\);
2. real geometric layer: affine-Dynkin bad-fiber intersection matrix;
3. component-group-size layer: the Tamagawa number \(c_p\);
4. full local reduction label used here: split versus nonsplit
   multiplicative reduction.

It then checks exact strictness statements:

1. the source scalar layer does not distinguish `14.a5 @ p=2` from
   `14.a1 @ p=2`, while the geometric layer does;
2. the geometric layer does not distinguish `14.a5 @ p=2` from
   `489762.dv3 @ p=2`, while the full local reduction label does;
3. the component-group-size layer does distinguish `14.a1 @ p=2` from
   the two `I_2` examples, but still does not distinguish
   split from nonsplit in the `I_2` pair;
4. repeated `I_2` fibers at \(p=2\) and \(p=3\) have the same geometry
   and the same \(c_p\), while the source scalar layer changes from
   \(\log 2\) to \(\log 3\).

So the verifier records the current real local hierarchy as:

\[
 \text{source scalar layer}
 \;<\;
 \text{fiber geometry}
 \;<\;
 \text{full local reduction datum},
 \]

with \(c_p\) as an intermediate local arithmetic invariant that still
does not exhaust the finest real local distinction visible here.

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All real local information hierarchy checks passed.
```

So the workspace now contains a reusable exact witness for the local
information hierarchy that Phase 107 must eventually confront.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. the local arithmetic comparison problem of Phase 107 now has a
   concrete hierarchy of target-side information layers written on real
   fibers;
2. the present source row of `107_04` is placed explicitly at the
   coarsest layer of that hierarchy;
3. future refinements can now be judged against a structured local
   benchmark rather than against isolated examples only.

It does **not** prove:

1. that these are the only local invariants relevant to Phase 107;
2. any global realization theorem;
3. the terminal identity or RH.

So the correct reading is:

\[
 \text{real local information hierarchy exact-checked},
 \qquad
 \text{full local target recovery still open}.
 \]
