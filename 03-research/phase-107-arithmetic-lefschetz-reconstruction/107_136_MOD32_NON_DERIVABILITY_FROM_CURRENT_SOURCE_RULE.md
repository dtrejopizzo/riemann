# 107.136 -- Mod-32 non-derivability from the current source rule

## 1. Purpose

`107_134` and `107_135` together established a useful tension:

1. the current row (c) is closed by no-go;
2. a new local grammar using minimal-model residue modulo \(32\)
   survives both the fixed visible \(S_3\) atlas and a much larger real
   additive \(IV^\ast\) family.

The remaining exact question is:

\[
\text{could that mod-32 channel already be hidden inside the current}
\]
\[
\text{prime/Gamma/pole source rule of }107.00\text{?}
\]

This note tests that directly on the same enlarged real family used in
`107_135`.

## 2. Current source-rule packet

For the additive \(IV^\ast\) family at \(p=2\) under discussion, the
current finite source-rule vocabulary of `107.00` reduces to

\[
\mathcal S_{\mathrm{rule}}=
\bigl(\Lambda(2),\log 2,2^{-1/2},a_2,L_2^{\mathrm{loc}}\bigr)
=
(\log 2,\log 2,2^{-1/2},0,1).
\]

So on this family the current source-rule packet is constant.

## 3. Real family tested

The verifier uses exactly the enlarged family fixed in `107_135`:

1. elliptic curves over \(\mathbf Q\);
2. local prime \(p=2\);
3. additive reduction;
4. Kodaira type \(IV^\ast\);
5. common coarse local packet
   \[
   (2,4,6,8,4,IV^\ast,2,0,1);
   \]
6. conductor range \(11 \le N \le 2000\).

This yields:

```text
ROWS: 285
```

## 4. Exact obstruction

The verifier groups those same `285` rows by the mod-\(32\) residue of
their local minimal-model coefficient tuple.

Its output is:

```text
ROWS: 285
CURRENT_SOURCE_RULE_PACKET: (log 2, log 2, 2^{-1/2}, 0, 1)
MOD32_CLASSES: 24
MIXED_MOD32_CLASSES: 0
```

So on the same real family:

1. the current source-rule packet is constant;
2. the mod-\(32\) channel is not constant;
3. the mod-\(32\) channel is not arbitrary noise, because its classes do
   not mix \(c_p\).

Therefore the mod-\(32\) channel cannot factor through the current
finite source-rule vocabulary of `107.00`.

## 5. Binary outcome

Running the verifier on Saturday, August 1, 2026 returns:

```text
VERDICT: NO
```

where `NO` means:
the current source rule does **not** already contain the mod-\(32\)
channel on this enlarged real family.

## 6. Consequence

This is the missing governance statement behind `A5`.

It does **not** say that mod-\(32\) is impossible for Phase 107.
It says something sharper:

1. `A5` is a real surviving candidate grammar;
2. but it is not derivable from the current prime/Gamma/pole finite
   source rule of `107.00`;
3. so reopening row (c) requires an actual grammar change, not a
   reinterpretation of the existing one.

So the correct reading is:

\[
\text{current row (c) remains closed,}
\]
\[
\text{A5 survives on real data,}
\]
\[
\text{and A5 is not secretly already inside the current }107.00
\text{ source rule.}
\]
