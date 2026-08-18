# 114.a.22 — H7-S: generic entropy scalarizes to one output

> **Prime-regularity refinement (`a_72`).** The zero-insertion recovery
> identity (1.3) survives the finite full-bio evaluation.  Hence all
> `T_epsilon` are separated inside their common fold fiber and multiplication
> by every prime cancels on this family.

```
+--------------------------------------------------------------------------+
| INPUT       V_epsilon:[2N]->[N], the block defects of a_21.              |
| SCALARIZE   Compose with one N-ary addition a_N:[N]->[1].                |
| RESULT      2^N distinct operations T_epsilon:[2N]->[1].                 |
| RECOVERY    Activate one input block and set all others to zero.         |
| NORM TEST   Every diagonal real specialization has norm sqrt(2N)/R.      |
| LIMIT       a_23: varying input arity does not by itself compute h^0.    |
+--------------------------------------------------------------------------+
```

## 1. One-output construction

Retain the notation of `114_a_21`.  Let

\[
 a_N^{(1)}:[N]\longrightarrow[1]                         \tag{1.1}
\]

be the `N`-ary sum obtained by iterating the first addition generator.  For
`epsilon in {1,2}^N`, define

\[
 T_\epsilon=a_N^{(1)}\circ V_\epsilon:[2N]\longrightarrow[1].             \tag{1.2}
\]

Thus `T_epsilon` belongs to the same output-rank-one arity in which Haran's
rank-one section functor `O(D)_{d_1}` lives, with `d_1=2N`.

### Theorem 1.1 (generic H7-S)

The operations `{T_epsilon}` are pairwise distinct.  Their diagonal folds are
all equal.

### Proof

Let `j_k:[2]->[2N]` insert the two inputs into block `k` and insert zero in
all other input coordinates.  Since zero is the unit for either addition,

\[
 T_\epsilon\circ j_k
 =a_N^{(1)}(0,\ldots,0,v_{\epsilon_k},0,\ldots,0)
 =v_{\epsilon_k}.                                           \tag{1.3}
\]

Consequently equality of `T_epsilon` and `T_eta` implies equality of every
`v_{epsilon_k}` and `v_{eta_k}`. Proposition 1.1 of `a_21` then gives
`epsilon=eta`.

Under the fold, both `v_1` and `v_2` become `v`, so every `T_epsilon` becomes
the ordinary sum of its `2N` inputs. QED.

### Corollary 1.2

The fiber of the generic diagonal map in the single component

\[
 A_{[1],[2N]}\longrightarrow\mathbb Z_{[1],[2N]}          \tag{1.4}
\]

has cardinality at least `2^N`.  With `N=mn`, its logarithmic cardinality is
at least `mn log 2`.

This closes the purely algebraic **one-output typing** lemma from `a_21`.
It does not close the geometric H7-S realization: `114_a_23` proves that
choosing input arity `2N=2mn` can manufacture a quadratic count independently
of surface geometry.

## 2. The collapsed real norm test

Let

\[
 R_{m,n}=p^m q^n,
 \qquad s_{m,n}=p_1^*(p^{-m})p_2^*(q^{-n})                 \tag{2.1}
\]

be the smallest pure denominator section in `B_{m,n}`.  Formally scale
`T_epsilon` by `s_{m,n}`.

After diagonal fold and any ordinary real matrix realization, this is the row
operator

\[
 R_{m,n}^{-1}(1,1,\ldots,1):\mathbb R^{2N}\longrightarrow\mathbb R,        \tag{2.2}
\]

whose Euclidean operator norm is

\[
 \frac{\sqrt{2N}}{p^m q^n}.                              \tag{2.3}
\]

### Proposition 2.1

For `N=mn`, (2.3) tends exponentially to zero; in particular it is at most
one for all sufficiently large `m,n`.

### Proof

Its logarithm is

\[
 \tfrac12\log(2mn)-m\log p-n\log q\longrightarrow-\infty. \tag{2.4}
\]

QED.

Thus the candidate passes every norm test that factors through the diagonal
ordinary-real realization.

## 3. The exact remaining boundedness lemma

Proposition 2.1 is necessary but not sufficient.  The compactified square has
non-totally-commutative local objects at its real boundary.  Membership

\[
 s_{m,n}T_\epsilon\in
 \mathcal O_Y(\mathcal B_{m,n})_{2N}                       \tag{3.1}
\]

must be proved in those local objects themselves; applying the fold first can
erase precisely the off-diagonal distinction being counted.

The load-bearing statement is now:

> **H7-B.** For `N=mn` and all sufficiently large `m,n`, every scaled
> `s_{m,n}T_epsilon` satisfies the finite local conditions and both genuine
> real-boundary contraction conditions of the Haran pro-square.

If H7-B holds, Theorem 1.1 gives the componentwise statement

\[
 \log\#\mathcal O_Y(\mathcal B_{m,n})_{2mn}\ge mn\log2.    \tag{3.2}
\]

but `114_a_23` shows that (3.2) is not yet a quadratic section theorem unless
the arity `2mn` is geometrically intrinsic or the associated minimal-generator
dimension is computed.  H7-B, the arity/rank gate H7-R, and H7-U remain open.

## 4. Verification scope

`114_a_22_h7_scalarization_verify.py` checks bit recovery, exact cardinality,
the common fold and the real collapsed norm.  The genuine real-real local
membership (3.1) is deliberately outside its verdict.
