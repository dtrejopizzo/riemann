# 114.a.25 — H7-KI: a power-evaluation criterion for mixed injectivity

```
+--------------------------------------------------------------------------+
| MAP         Use p-adic layers p^j/p^m, 0<=j<=m, with p>=3.              |
| CRITERION   Real evaluations send the second integer c to               |
|             sgn(c)|c|^sigma for every sigma>0.                           |
| THEOREM     Under that criterion the scalar mixed map is injective.      |
| PROOF       Independence of a^sigma + balanced base-p uniqueness.        |
| SOURCE GAP  Haran gives the R_+ power action on a boundary rig/spectrum, |
|             but not the required faithful scalar evaluation theorem.     |
+--------------------------------------------------------------------------+
```

## 1. A valuation-layer mixed map

Fix distinct primes `p,q` with `p>=3`, put `P=p^m`, `Q=q^n`, and use the
`m+1` canonical `p`-adic layers

\[
 g_j=p^j/P,\qquad 0\le j\le m.                           \tag{1.1}
\]

Every `g_j` is a scalar section of `L_p^m`.  For

\[
 c=(c_0,\ldots,c_m)\in I_{m+1}(Q),                       \tag{1.2}
\]

define

\[
 \mathcal P_{m,n}(c)
 =\mathop{+_{(1)}}_{j=0}^{m}
       p_1^*(p^j/P)\,p_2^*(c_j/Q).                       \tag{1.3}
\]

As in `114_a_24`, every collapsed absolute-value test gives

\[
 |\Delta^*\mathcal P_{m,n}(c)|
 \le\sum_j\frac{p^j}{P}\frac{|c_j|}{Q}
 \le1.                                                   \tag{1.4}
\]

The domain has quadratic entropy:

\[
 \log\#I_{m+1}(q^n)=mn\log q-O(m\log m+n).               \tag{1.5}
\]

## 2. The exact evaluation hypothesis

Let `A` denote the scalar ring of the localized generic arithmetic plane,
viewed with its first addition.  Assume there is a family of ring-valued
evaluations

\[
 E_\sigma:A\longrightarrow\mathbb R,
 \qquad \sigma>0,                                        \tag{2.1}
\]

such that on the two rational rulings

\[
 E_\sigma(p_1^*a)=a,
 \qquad
 E_\sigma(p_2^*b)=\operatorname{sgn}(b)|b|^\sigma.       \tag{2.2}
\]

Only faithfulness on the finite family (1.3) is needed: equality in `A` must
imply equality of all evaluations.  The reverse implication is unnecessary.

## 3. Conditional injectivity theorem

### Theorem 3.1

Under (2.1)--(2.2), the map

\[
 \mathcal P_{m,n}:I_{m+1}(Q)\longrightarrow A            \tag{3.1}
\]

is injective for every `m,n` and every prime `p>=3`.

### Proof

Suppose `P_{m,n}(c)=P_{m,n}(d)`.  Apply `E_sigma` and cancel the common
positive denominators. For every `sigma>0`,

\[
 \sum_{j=0}^{m}p^j\operatorname{sgn}(c_j)|c_j|^\sigma
 =\sum_{j=0}^{m}p^j\operatorname{sgn}(d_j)|d_j|^\sigma.  \tag{3.2}
\]

Group terms by the positive magnitude `a`.  The functions
`a^sigma=e^{sigma log a}` for distinct positive integers `a` are linearly
independent on every open interval of `sigma`: order the `a` and let
`sigma->infinity`, then remove the largest term inductively.  Consequently,
for every `a>=1`,

\[
 \sum_{|c_j|=a}p^j\operatorname{sgn}(c_j)
 =\sum_{|d_j|=a}p^j\operatorname{sgn}(d_j).              \tag{3.3}
\]

Balanced base-`p` digits are unique for `p>=3`.  Indeed, if
`sum e_jp^j=0` with `e_j in {-2,-1,0,1,2}` and `k` is the largest nonzero
index, then

\[
 |e_k|p^k\ge p^k>
 2\sum_{j<k}p^j=2\frac{p^k-1}{p-1},                     \tag{3.4}
\]

where the strict inequality holds for `p>=3`.  Thus all `e_j` vanish.
Applying this to (3.3) shows, for every coordinate `j` and magnitude `a`, that
`c_j=a`, `c_j=-a`, or neither exactly when the same is true of `d_j`. Hence
`c=d`. QED.

## 4. What the source gives and the remaining source lemma

Haran 2017 equations (10.23)--(10.25) construct rings associated with
`Z tensor_F [0,infinity)` and the action

\[
 x\longmapsto x^\sigma,\qquad\sigma\in\mathbb R_+,       \tag{4.1}
\]

on the boundary rig and its spectrum.  This is the precise motivation for
(2.1)--(2.2), but it is not yet the theorem required here: an action on the
target spectrum does not automatically furnish a morphism from the localized
scalar ring of `Z box_F Z`, nor prove (2.2) with signs.

The remaining injectivity gate is therefore a single typed statement:

> **H7-EVAL.** Construct the evaluations (2.1) on the relevant localized
> commutative bio (or another separating family satisfying (3.2)).

H7-EVAL plus genuine real-boundary membership would prove the H7-K lower
bound through (1.5).  The global upper bound H7-U would still remain.

`114_a_28` removes the top layer `j=m` and proves genuine real-boundary
membership for an `m`-layer cross-contraction. This preserves the quadratic
domain entropy. The cross-contraction has different outer tree labels from
the first-additive family here, so its injectivity is the separate gate
H7-XI; it must not be inferred from H7-DFLAT.

## 5. Verification scope

`114_a_25_h7_power_evaluation_verify.py` checks finite exponential
independence through Vandermonde determinants, balanced-base uniqueness, the
mass inequality and domain entropy.  It does not assert H7-EVAL.
