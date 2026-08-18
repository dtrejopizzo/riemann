# 107.128 -- Local minimal-model residue channel witness

## 1. Purpose

`107_123` through `107_127` exact-check that the current finite local
source rule of Phase 107 is too coarse for the current target if
\(c_p\) is retained.

This note records the first positive witness on the same forcing pair:
an actual local arithmetic signal, available from real curve data,
which does separate the pair.

The point is not to claim that this signal already belongs to the
current Phase 107 source grammar.  It does not.
The point is to identify concretely what a genuinely new local channel
could look like.

## 2. Real forcing pair

The verifier uses the same genuine elliptic curves over \(\mathbf Q\):

\[
20a1@2,\qquad 36a4@2.
\]

Their current target states are

\[
(IV^\ast,3,\text{additive}),
\qquad
(IV^\ast,1,\text{additive}).
\]

The current finite source row of `107_03`--`107_04` identifies them.

## 3. New local channel tested

Sage provides the local minimal model at \(p=2\) through
`E.local_data(2).minimal_model()`.

For the forcing pair, the verifier extracts the minimal-model
Weierstrass coefficient tuple

\[
\mathbf a_{\min}(E,2)=(a_1,a_2,a_3,a_4,a_6)
\]

and also its residue class modulo \(8\).

The computed outputs are:

\[
\mathbf a_{\min}(20a1,2)=(0,1,0,4,4),
\]

\[
\mathbf a_{\min}(36a4,2)=(0,0,0,-135,-594),
\]

so modulo \(8\):

\[
(0,1,0,4,4)\not\equiv(0,0,0,1,6)\pmod 8.
\]

Thus the local minimal-model residue channel distinguishes the same pair
that the current finite source rule collapses.

## 4. Binary outcome

The verifier asks whether the minimal-model residue channel separates the
real forcing pair.

Running it on Saturday, August 1, 2026 returns

```text
VERDICT: YES
```

So there exists at least one concrete local arithmetic channel on real
data that separates the pair.

## 5. Interpretation

This witness does **not** prove that Phase 107 can already use this
channel.
It proves a narrower but useful fact:

1. the blocking pair is not indistinguishable to *all* local arithmetic
   information;
2. what is missing is specifically absent from the current finite source
   rule, not absent from local arithmetic reality;
3. a future source upgrade that aims to keep \(c_p\) in the target must
   add some channel of this flavor: local arithmetic data finer than the
   present prime-weight/Euler vocabulary.

So the correct reading is:

\[
\text{current source rule blocked,}
\]
\[
\text{but a concrete finer local arithmetic channel already separates the pair.}
\]
