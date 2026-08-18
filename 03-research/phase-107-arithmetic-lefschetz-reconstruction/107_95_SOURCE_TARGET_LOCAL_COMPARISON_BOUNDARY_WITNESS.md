# 107.95 -- Source-vs-target local comparison boundary witness

## 1. Purpose

`107_04` proves that the current finite source row contributes exactly
\(\log p\) in the prime-power case.  `107_93` and `107_94` now provide
real local target-side witnesses on actual bad fibers of elliptic curves
over \(\mathbf Q\).  This makes one sharp comparison possible:
does the present source row already see local geometry, or does it only
see the standard finite-place scalar weight?

This note exact-checks that boundary.

## 2. Objects compared

The verifier `107_95_source_target_local_comparison_boundary_witness.py`
compares:

1. the current source-side local law of `107_04`, which assigns the
   scalar \(\log p\) to a prime-power transition and nothing more at the
   finite stage;
2. the real local target-side fibers used in `107_93` and `107_94`,
   including:
   `14.a5 @ p=2` with Kodaira type \(I_2\),
   `102.a1 @ p=3` with Kodaira type \(I_2\), and
   `14.a1 @ p=2` with Kodaira type \(I_9\).

The key contrast is between the two fibers at the same prime \(p=2\):
they share the same source-side \(\log 2\), but have different
target-side intersection matrices.

## 3. Exact checks performed

The verifier:

1. instantiates the source-side local prediction
   \(\mathrm{ord}_{\mathrm{fin}}=\log p\);
2. constructs the real target-side affine-Dynkin matrices for
   \(I_2\) and \(I_9\);
3. checks that two different real Kodaira types at the same prime
   \(p=2\) receive the same source scalar \(\log 2\);
4. checks that those same two real fibers have genuinely different
   target-side intersection matrices;
5. checks that repeated real \(I_2\) fibers at different primes have
   the same geometry but different source/target scalar weights
   \(\log 2\) and \(\log 3\).

So the witness isolates the present comparison boundary:

\[
 \text{current source row sees prime weighting},
 \qquad
 \text{real target row also sees fiber geometry}.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All source-vs-target local comparison boundary checks passed.
```

So the workspace now contains a reproducible witness that the current
source local row, as presently formalized in `107_04`, does not yet
distinguish real local fiber geometry beyond the standard finite-place
weight \(\log p\).

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. the current source-side local law of `107_04` is compatible with the
   scalar finite-place normalization seen on real bad fibers;
2. that same source row does not yet recover the target-side component
   geometry, since it gives the same \(\log 2\) to real \(I_2\) and
   real \(I_9\) fibers at the same prime;
3. the first genuine geometric comparison boundary of Phase 107 is now
   written as an exact, falsifiable statement on real objects.

It does **not** prove:

1. that no refinement of the Phase 107 source row could recover this
   geometry;
2. a global realization theorem;
3. the terminal identity or RH.

So the correct reading is:

\[
 \text{real local source-vs-target boundary exact-checked},
 \qquad
 \text{source recovery of local geometry still open}.
 \]
