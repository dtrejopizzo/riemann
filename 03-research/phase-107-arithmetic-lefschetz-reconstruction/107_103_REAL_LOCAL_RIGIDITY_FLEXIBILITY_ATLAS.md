# 107.103 -- Real local rigidity/flexibility atlas

## 1. Purpose

`107_100`, `107_101`, and `107_102` now give exact real local witnesses
in three different sectors:

1. multiplicative \(I_n\), where Frobenius can change \(c_p\) or even
   preserve \(c_p\) while still changing the finer reduction label;
2. additive \(IV\), where Frobenius changes \(c_p\) already at the
   component-group level;
3. additive \(III\), where the pinned examples behave rigidly once the
   geometry is fixed.

This note packages those cases into one exact atlas.  The point is not
another isolated example, but a structural distinction:
there are at least two different notions of local rigidity in Phase 107

\[
 \text{\(c_p\)-rigidity}
 \qquad\text{and}\qquad
 \text{full-datum rigidity}.
 \]

## 2. Real sectors compared here

The verifier `107_103_real_local_rigidity_flexibility_atlas.py` uses
only real rows already pinned in earlier witnesses:

1. multiplicative `14.a1 @ p=2`, type \(I_9\), nonsplit, \(c_2=1\);
2. multiplicative `14.a1 @ p=7`, type \(I_2\), split, \(c_7=2\);
3. multiplicative `14.a5 @ p=2`, type \(I_2\), nonsplit, \(c_2=2\);
4. multiplicative `489762.dv3 @ p=2`, type \(I_2\), split, \(c_2=2\);
5. additive `20.a1 @ p=2`, type \(IV\), \(c_2=1\);
6. additive `36.a4 @ p=2`, type \(IV\), \(c_2=3\);
7. additive `36.a4 @ p=3`, type \(III\), \(c_3=2\);
8. additive `4225.m2 @ p=5`, type \(III\), \(c_5=2\).

## 3. Exact checks performed

The verifier records three local regimes.

### 3.1 \(I_n\): two different layers of flexibility

For multiplicative \(I_n\), the geometric component group is
\(\mathbf Z/n\mathbf Z\).

1. The split action fixes all \(n\) elements, so \(c_p=n\).
2. The nonsplit action fixes \(\gcd(2,n)\) elements.

This creates two subregimes:

1. for odd \(n\), such as \(I_9\), \(c_p\) itself is flexible;
2. for \(n=2\), \(c_p\) is rigid at \(2\), but the finer local datum is
   still flexible because split and nonsplit reduction remain distinct.

### 3.2 \(IV\): flexibility already at the \(c_p\)-level

For additive \(IV\), the affine \(A_2\) triangle has geometric
component group of order \(3\).

1. trivial Frobenius gives \(c_p=3\);
2. a 3-cycle gives \(c_p=1\).

So this sector is already flexible at the \(c_p\)-level.

### 3.3 \(III\): rigidity at both visible levels

For additive \(III\), the affine \(A_1\) geometry gives a component
group of order \(2\), and the pinned real examples both realize
\(c_p=2\).

So in the currently visible data this sector is rigid both at the
\(c_p\)-level and at the full reduction-label level used in the Phase
107 local witnesses.

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All real local rigidity/flexibility atlas checks passed.
```

So the workspace now contains one exact real local classification
statement instead of only separate local examples.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. Phase 107 local comparison now has an exact distinction between
   sectors that are flexible already in \(c_p\), sectors rigid in
   \(c_p\) but flexible in finer reduction data, and sectors rigid at
   both visible levels;
2. the local arithmetic problem is therefore not uniform across Kodaira
   types, even on genuine elliptic bad fibers over \(\mathbf Q\);
3. future source-side comparisons can now be judged against a typed
   target atlas rather than against isolated local anecdotes.

It does **not** prove:

1. that this atlas is complete for all Kodaira types;
2. that the current Phase 107 source package reproduces the typed local
   behavior recorded here;
3. any global realization theorem, the terminal identity, or RH.

So the correct reading is:

\[
 \text{real local rigidity/flexibility atlas exact-checked},
 \qquad
 \text{full Phase 107 geometric realization still open}.
 \]
