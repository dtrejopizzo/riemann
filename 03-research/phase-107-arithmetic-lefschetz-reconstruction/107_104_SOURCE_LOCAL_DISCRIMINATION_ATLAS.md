# 107.104 -- Source local discrimination atlas

## 1. Purpose

`107_93` through `107_103` now give a real local target-side atlas:
actual bad fibers over \(\mathbf Q\) realize several distinct local
regimes, with different Kodaira geometries, different Tamagawa
behavior, and in some cases finer split/nonsplit separation.

This note turns back to the actual current source-side local row of
Paper A.  In the present Phase 107 tree, that row is still represented
only by the scalar finite-place weight

\[
 p \longmapsto \log p.
 \]

The verifier below measures, exactly on the pinned real examples, how
much local target information collapses under that current source map.

## 2. Real local states compared here

The verifier `107_104_source_local_discrimination_atlas.py` uses the
same real local states already fixed in earlier witnesses:

1. `14.a1 @ p=2`, type \(I_9\), \(c_2=1\), nonsplit multiplicative;
2. `14.a5 @ p=2`, type \(I_2\), \(c_2=2\), nonsplit multiplicative;
3. `489762.dv3 @ p=2`, type \(I_2\), \(c_2=2\), split multiplicative;
4. `20.a1 @ p=2`, type \(IV\), \(c_2=1\), additive;
5. `36.a4 @ p=2`, type \(IV\), \(c_2=3\), additive;
6. `36.a4 @ p=3`, type \(III\), \(c_3=2\), additive;
7. `4225.m2 @ p=5`, type \(III\), \(c_5=2\), additive.

Each row is a genuine local bad fiber of a genuine elliptic curve over
\(\mathbf Q\).

## 3. Exact checks performed

The verifier defines:

1. the current source local signature, namely just \(\log p\);
2. a target local signature used here, namely the tuple
   \((\text{Kodaira type}, c_p, \text{reduction label})\).

It then checks:

1. all five pinned bad fibers above \(p=2\) collapse to the same source
   signature \(\log 2\);
2. those same five rows realize five different target signatures;
3. the source row therefore cannot distinguish any of the current
   \(p=2\) local sectors: \(I_9\), \(I_2\) nonsplit, \(I_2\) split,
   \(IV\) with \(c_p=1\), and \(IV\) with \(c_p=3\);
4. changing the prime does separate source signatures
   (\(\log 2\), \(\log 3\), \(\log 5\)), but that is far coarser than
   the target-side local atlas.

So the current source-side local behavior is recorded exactly as

\[
 \text{many distinct real local target states}
 \longmapsto
 \text{one source scalar class at fixed }p.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All source local discrimination atlas checks passed.
```

So the workspace now contains an exact local statement, on real
examples, of how coarse the present Paper A finite-place row still is.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. the current source row of `107_04` is now measured against the full
   real local atlas rather than against one or two isolated examples;
2. at least on the pinned real states, source-side discrimination is
   purely by prime and not by the finer local arithmetic or geometric
   regime;
3. any future promotion of Paper A toward a realized local comparison
   must improve that discrimination if it claims to recover actual bad
   fiber data.

It does **not** prove:

1. that the present source row can never be refined within the Phase
   107 program;
2. which exact target-side local invariant the final source package
   must reproduce;
3. any global realization theorem, the terminal identity, or RH.

So the correct reading is:

\[
 \text{source local discrimination atlas exact-checked},
 \qquad
 \text{full source-to-target local recovery still open}.
 \]
