# 107.111 -- Same finite log-weight packet global no-go

## 1. Purpose

`107_110` exact-checks a first finite global obstruction:
two genuine elliptic curves over \(\mathbf Q\) can share the same set of
bad primes and still differ in their pinned real local target data.

This note restates that obstruction in the language closest to the
current finite-place source package of `107_04`.
At the present stage, the source sees prime towers through the weights
\(\log p\).  So the natural coarse global packet is the multiset of
finite bad-prime weights

\[
 \{\log p : p \text{ bad for }E\}.
 \]

The verifier below shows that even this whole finite log-weight packet
is still too coarse to recover the pinned real local atlas.

## 2. Real curves used here

The verifier `107_111_same_finite_log_weight_packet_global_no_go.py`
uses the same two genuine elliptic curves as `107_110`:

1. `14.a1`, conductor \(14=2\cdot7\), with pinned local signature at
   \(p=2\) equal to \( (I_9,1,\text{nonsplit multiplicative}) \);
2. `14.a5`, conductor \(14=2\cdot7\), with pinned local signature at
   \(p=2\) equal to \( (I_2,2,\text{nonsplit multiplicative}) \).

For both curves the finite bad-prime log-weight packet is

\[
 \{\log 2,\log 7\}.
 \]

## 3. Exact no-go statement

The verifier defines the coarse global source packet

\[
 W(E)=\{\log p : p \text{ bad for }E\}.
 \]

It then checks:

1. `14.a1` and `14.a5` have the same packet \(W(E)=\{\log 2,\log 7\}\);
2. their pinned visible local target signatures at \(p=2\) differ;
3. therefore no global comparison map factoring only through the finite
   log-weight packet \(W(E)\) can recover even the pinned \(p=2\) local
   target state faithfully on this pair.

So the exact obstruction is:

\[
 \text{same finite log-weight packet}
 \centernot\Longrightarrow
 \text{same real local target atlas}.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All same finite log-weight packet global no-go checks passed.
```

So the workspace now contains a global obstruction phrased directly in
the present finite-place source language of `107_04`.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. even the whole finite multiset of current source-side prime weights
   is still too coarse to recover the pinned real local target data;
2. the global obstruction is therefore not an artifact of using only
   the set of bad primes; it persists in the more faithful `107_04`
   language of finite \(\log p\)-packets;
3. any future global finite-support realization claim in Phase 107 must
   carry more structure than the present finite log-weight packet if it
   aims to recover actual local target states.

It does **not** prove:

1. that every global Phase 107 source package factors only through
   \(W(E)\);
2. that no richer finite global packet could distinguish this pair;
3. any global realization theorem, the terminal identity, or RH.

So the correct reading is:

\[
 \text{same finite log-weight packet global no-go exact-checked},
 \qquad
 \text{full refined global realization problem still open}.
 \]
