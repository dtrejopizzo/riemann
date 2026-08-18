# 107.112 -- Global source upgrade necessity gate

## 1. Purpose

`107_110` and `107_111` already show two exact finite global
obstructions on actual elliptic curves over \(\mathbf Q\):

1. the bad-prime support profile is too coarse;
2. even the full finite packet of bad-prime weights \(\{\log p\}\) is
   still too coarse.

This note turns those two obstructions into one governance gate for
future finite global source upgrades in Phase 107.

The point is simple:
any finite global source package that claims to recover pinned real
local target data must distinguish at least one concrete pair of actual
curves that the present coarse global packets do not separate.

## 2. Real pair used here

The verifier `107_112_global_source_upgrade_necessity_gate.py` uses the
same genuine elliptic curves as `107_110` and `107_111`:

1. `14.a1`, conductor \(14\), bad primes \(\{2,7\}\), finite
   log-weight packet \(\{\log 2,\log 7\}\), pinned local signature at
   \(p=2\) equal to \( (I_9,1,\text{nonsplit multiplicative}) \);
2. `14.a5`, conductor \(14\), bad primes \(\{2,7\}\), finite
   log-weight packet \(\{\log 2,\log 7\}\), pinned local signature at
   \(p=2\) equal to \( (I_2,2,\text{nonsplit multiplicative}) \).

These are genuine curves over \(\mathbf Q\), not symbolic placeholders.

## 3. Exact necessity gate

The verifier defines two coarse finite global source profiles:

1. support profile
   \[
    G_0(E)=\{\text{bad primes of }E\};
   \]
2. finite log-weight packet
   \[
    G_1(E)=\{\log p : p \text{ bad for }E\}.
   \]

It then checks:

1. `14.a1` and `14.a5` have the same \(G_0\);
2. `14.a1` and `14.a5` have the same \(G_1\);
3. their pinned local target signatures at \(p=2\) are different;
4. therefore any future finite global source package that claims to
   recover the pinned real local target data must distinguish this pair
   by information strictly finer than \(G_0\) and strictly finer than
   \(G_1\).

So the exact governance consequence is:

\[
 \text{global upgrade claim}
 \Longrightarrow
 \text{break both }G_0\text{- and }G_1\text{-factorization on this pair}.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All global source upgrade necessity gate checks passed.
```

So the workspace now contains a concrete finite global necessity gate
for future source-side upgrades.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. future finite global source upgrades in Phase 107 now have an exact
   pairwise lower-bound test on actual curves over \(\mathbf Q\);
2. merely tracking the set of bad primes or the current finite
   \(\log p\)-packet is no longer enough to count as a meaningful
   global upgrade if pinned local target recovery is claimed;
3. the global governance of Paper A/Part III is now sharper than a
   general request for “more arithmetic content”.

It does **not** prove:

1. which finer finite global packet is sufficient to distinguish the
   pair;
2. that any present Phase 107 source package already distinguishes it;
3. any global realization theorem, the terminal identity, or RH.

So the correct reading is:

\[
 \text{global source upgrade necessity gate exact-checked},
 \qquad
 \text{full refined global realization problem still open}.
 \]
