# 107.122 -- Current 107.03/107.04 source packet to A4 no-go

## 1. Purpose

`107_121` proves that the Frobenius coefficient \(a_p^\flat\) used by
`A4` is not a function of the scalar observable

\[
S_{107.04}(row)=\log p.
\]

This note removes the remaining ambiguity:
perhaps \(a_p^\flat\) is not a function of \(\log p\) alone, but it
could still be a function of the *full current finite source packet*
actually exposed by `107_03` and `107_04`.

The present gate answers that sharper question.

## 2. Full current finite source packet

At the connected finite level, `107_03` and `107_04` currently expose:

1. the prime \(p\);
2. the raw bidegree of the connected prime return,
   \[
   \deg_{\mathrm{raw}}(\Gamma_{p,1})=(1,p);
   \]
3. the balanced weight,
   \[
   w(\Gamma_{p,1})=p^{-1/2};
   \]
4. the normalized finite order coming from `107_04`,
   \[
   \operatorname{ord}_{\mathrm{fin}}=\log p.
   \]

So the exact current source packet tested here is

\[
\mathcal S_{\mathrm{cur}}(row)=
\bigl(p,\ (1,p),\ p^{-1/2},\ \log p\bigr).
\]

Crucially, this packet still depends only on the prime and not on the
curve realizing the local row.

## 3. Fixed real atlas

The verifier fixes the same six real rows as `107_121`:

1. `14a1 @ p=2`;
2. `14a5 @ p=7`;
3. `21a1 @ p=7`;
4. `20a1 @ p=2`;
5. `36a4 @ p=2`;
6. the genus-2 supersingular control
   \[
   y^2+y=x^5+x^2
   \]
   over \(\mathbf Q\), with PARI bad prime \(10037\).

The target quantity is again the Frobenius coefficient \(a_p^\flat\)
used by `A4`:

1. for elliptic rows, the actual Sage value `E.ap(p)`;
2. for the genus-2 control row, the atlas value \(0\) used in
   `107_120`.

## 4. Exact real obstruction

Running the verifier shows that the full current packet
\(\mathcal S_{\mathrm{cur}}\) still collides on rows with different
Frobenius coefficients.

### Prime \(2\)

The rows

\[
14a1@2,\qquad 20a1@2,\qquad 36a4@2
\]

all have the same current source packet

\[
\bigl(2,(1,2),2^{-1/2},\log 2\bigr),
\]

but

\[
a_p^\flat=-1,\qquad 0,\qquad 0.
\]

### Prime \(7\)

The rows

\[
14a5@7,\qquad 21a1@7
\]

have the same current source packet

\[
\bigl(7,(1,7),7^{-1/2},\log 7\bigr),
\]

but

\[
a_p^\flat=1,\qquad -1.
\]

So \(a_p^\flat\) is not a function of the full current finite source
packet either.

## 5. Binary outcome

The verifier asks whether equal current source packets imply equal
\(a_p^\flat\)-values on the fixed atlas.

Running it on Saturday, August 1, 2026 returns

```text
VERDICT: NO
```

Therefore the present `107_03`/`107_04` finite source route does **not**
derive the Frobenius coefficient required by `A4`.

## 6. Consequence

This strengthens `107_121` from the scalar observable to the full
current finite source packet.

What is now exact-checked is:

1. `A4` succeeds on the fixed real atlas;
2. `A4` does not come from \(\log p\) alone;
3. `A4` does not come from the full current finite packet
   \(\bigl(p,(1,p),p^{-1/2},\log p\bigr)\) either.

So any future attempt to derive the Frobenius-shaped `A4` packet inside
Phase 107 must add genuinely new source structure beyond what
`107_03` and `107_04` presently expose at the finite connected level.
