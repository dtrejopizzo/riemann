# 107.94 -- Real Kodaira-type log-weight comparison

## 1. Purpose

`107_93` gave a first local witness on real bad fibers of elliptic
curves over \(\mathbf Q\).  The next sharp question is more focused:
when the same Kodaira fiber type appears at different bad primes, what
is genuinely geometric and what is only the standard finite-place
normalization?

This note exact-checks that distinction on real local data.

## 2. Real objects used here

The verifier `107_94_real_kodaira_type_log_weight_comparison.py` uses a
pinned snapshot of LMFDB local data for the following actual curves over
\(\mathbf Q\):

1. `14.a5`, whose bad fiber at \(p=2\) has Kodaira type \(I_2\);
2. `102.a1`, whose bad fibers at \(p=2\) and \(p=3\) both have Kodaira
   type \(I_2\);
3. `14.a1`, whose bad fiber at \(p=2\) has Kodaira type \(I_9\).

The first two items are the key comparison pair: the same Kodaira type
appears at different primes.

## 3. Exact checks performed

The verifier:

1. constructs the unweighted component-intersection matrix for the real
   \(I_2\) fiber type;
2. checks that every real \(I_2\) fiber in the pinned data carries that
   same unweighted matrix, independent of the prime;
3. forms the weighted Arakelov matrices
   \((\log p)M_{I_2}\) for \(p=2,3\);
4. checks exactly that the difference between those local target-side
   objects is only the scalar \(\log p\), while the underlying
   intersection matrix is unchanged;
5. records one additional \(I_9\) real fiber as a control showing that
   changing Kodaira type really changes the underlying matrix.

So the note isolates, on real arithmetic fibers, the distinction:

\[
 \text{Kodaira type determines the geometry},
 \qquad
 \log p \text{ determines the standard finite-place weight}.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All real Kodaira-type log-weight comparison checks passed.
```

So the workspace now contains a reproducible local witness that the
\(\log p\) factor in these real bad-fiber intersections is standard
target-side normalization layered on top of the same underlying fiber
geometry.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. for repeated real Kodaira types, the underlying finite-place
   intersection geometry is prime-independent at the matrix level;
2. the local Arakelov factor \(\log p\) acts as a scalar weight on that
   geometry rather than changing the combinatorial fiber type itself;
3. Phase 107 now has a real local target-side benchmark for the precise
   distinction between geometry and finite-place normalization.

It does **not** prove:

1. that the current Phase 107 source package reproduces this benchmark;
2. any global realization theorem;
3. the terminal identity or RH.

So the correct reading is:

\[
 \text{real local geometry-vs-log-weight distinction exact-checked},
 \qquad
 \text{full Phase 107 geometric comparison still open}.
 \]
