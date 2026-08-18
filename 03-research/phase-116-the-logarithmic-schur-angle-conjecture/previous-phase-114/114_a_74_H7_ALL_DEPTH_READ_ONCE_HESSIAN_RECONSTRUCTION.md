# 114.a.74 — H7: Hessians reconstruct unsigned read-once trees at every depth

> **Signed extension (`a_75`).** Unit-vector evaluations recover every leaf
> sign.  Passing to the corresponding orthant reduces to this positive
> Hessian theorem, so all signed read-once trees are prime-regular as well.

```
+-------------------------------------------------------------------------+
| TARGET      The real homogeneous endomorphism bio of a49, with u>1.    |
| DOMAIN      Positive inputs; both alternating additions are smooth.     |
| ROOT 1      Components of the mixed-Hessian graph of F are its children.|
| ROOT 2      Components of the mixed-Hessian graph of F^(1/u) are its     |
|             children.                                                   |
| DETECT ROOT The other one of these two graphs is connected.              |
| RECURSE     Zero the complementary variables and repeat on every child.  |
| RESULT      Every reduced unsigned read-once tree, at any depth/arity,   |
|             is separated; multiplication by every prime cancels there.  |
| OPEN        Repeated variables, signs, contractions, two-sided cut data. |
+-------------------------------------------------------------------------+
```

## 1. Analytic realization on the positive orthant

Fix `u>1` and put `r=1/u`.  The signed-power construction of `a_39` and the
full homogeneous-bio map of `a_49` evaluate the two additions on positive
inputs as

\[
 \delta_1(x_1,\ldots,x_m)=\sum_i x_i,
 \qquad
 \delta_2(x_1,\ldots,x_m)=\left(\sum_i x_i^r\right)^{1/r}.             \tag{1.1}
\]

Consider a finite rooted tree whose leaves are distinct labelled variables,
whose internal vertices have at least two children, and whose colors
`1,2` alternate along every edge.  Associativity and commutativity at a
vertex are already absorbed by treating its children as an unordered set.
Call this a **reduced unsigned read-once tree**.  Its evaluation is a positive
smooth homogeneous function

\[
 F_T:(0,\infty)^X\longrightarrow(0,\infty).                            \tag{1.2}
\]

Every such tree has the ordinary sum as diagonal fold, independently of its
shape and colors.

## 2. Mixed-Hessian graphs

For a smooth function `F` on the positive orthant, let `H(F)` be the graph
on its variables in which `i--j` is an edge when

\[
 \frac{\partial^2F}{\partial x_i\partial x_j}
\]

is not identically zero.  The elementary identity

\[
 \frac{\partial^2}{\partial x_i\partial x_j}
 (A+B)^\alpha
 =\alpha(\alpha-1)(A+B)^{\alpha-2}
   \frac{\partial A}{\partial x_i}
   \frac{\partial B}{\partial x_j}                                   \tag{2.1}
\]

holds when `A,B` use disjoint variable sets and `i` belongs to `A`, `j` to
`B`.  All first derivatives of the functions (1.2) are positive.  Hence for
`alpha notin {0,1}` every pair of different summands contributes a genuine
cross edge.

### Lemma 2.1 (root-color decomposition)

Let the root children of `T` have leaf sets `X_1,...,X_m`.

1. If the root has color `1`, the connected components of `H(F_T)` are
   exactly `X_1,...,X_m`, while `H(F_T^r)` is connected.
2. If the root has color `2`, the connected components of `H(F_T^r)` are
   exactly `X_1,...,X_m`, while `H(F_T)` is connected.

### Proof

For a color-`1` root,

\[
 F_T=\sum_jF_{T_j}.                                                     \tag{2.2}
\]

There are no cross derivatives between different `X_j`.  Each non-leaf
child has color `2`; its function has the form
`(sum_k F_{jk}^r)^(1/r)`.  Equation (2.1), with `alpha=1/r`, supplies cross
edges between every two child blocks, so its Hessian graph is connected.
Leaf children are singleton components.  This proves the component claim.
Applying (2.1) with `alpha=r` to (2.2) supplies all cross-child edges, hence
`H(F_T^r)` is connected.

For a color-`2` root,

\[
 F_T^r=\sum_jF_{T_j}^r.                                                 \tag{2.3}

The same argument, with the colors reversed, gives the components of
`H(F_T^r)`.  Equation (2.1) applied to
`F_T=(sum_jF_{T_j}^r)^(1/r)` makes `H(F_T)` connected.  QED.

## 3. Faithful reconstruction at arbitrary depth

### Theorem 3.1 (Hessian reconstruction)

The map `T -> F_T` is injective on reduced unsigned read-once trees of every
finite depth and arity.

### Proof

For a one-leaf tree there is nothing to prove.  Otherwise compute the two
graphs `H(F)` and `H(F^r)`.  By Lemma 2.1 exactly one is disconnected.  This
determines the root color, and its connected components recover the leaf set
of every root child.

For a component `X_j`, let all variables outside `X_j` tend to zero.  Both
operations have zero as additive identity, so the continuous boundary value
is exactly `F_{T_j}`.  Apply the same procedure recursively.  Finite
induction recovers every vertex, its color and its child partition.  QED.

This is a genuine all-depth normal form **for the stated read-once sector**.
It does not claim that raw Haran tree representatives outside that sector
have unique syntax.

## 4. Prime cancellation on the read-once sector

Fix a prime `ell`.  Under the first structural map, multiplication by `ell`
becomes ordinary pointwise multiplication of `F_T` by the positive real
number `ell`.

### Corollary 4.1

For reduced unsigned read-once trees `T,U`,

\[
 \ell T=\ell U\quad\Longrightarrow\quad T=U.                           \tag{4.1}
\]

### Proof

Apply the real full-bio map.  Equality gives `ell F_T=ell F_U`; cancel
`ell` in `R`, then use Theorem 3.1.  QED.

Thus H7-RF-FOLD and H7-PRIME-REG are proved on all unsigned read-once tree
fibers, with no depth or arity bound.  The finite cubic proofs `a_72`--`a_73`
are the discrete depth-one/two shadows of this analytic reconstruction.

## 5. Exact remaining core

Haran's full operation classes are more general than (1.2): their graph data
can reuse variables through contraction, carry leaf signs, contain both
input and output trees joined by a bijection, and change presentation by the
cut-commutativity relation.  Hessian reconstruction does not yet descend
through all those operations.

The remaining gate is therefore sharpened to

> **H7-RF-CUT.** Prove prime cancellation for signed/repeated two-sided tree
> data modulo contraction and cut-commutativity, on an affine cover at every
> pro-level; equivalently extend the faithful analytic invariant beyond the
> unsigned read-once sector.

Any counterexample to H7-PRIME-REG must use at least one of those features;
depth and arity alone can no longer produce it.

`a_75` subsequently removes isolated leaf signs from this list.  The
remaining features are repetition/contraction and genuinely two-sided cut
data (H7-RF-BICUT).

## 6. Verification scope

`114_a_74_h7_read_once_hessian_verify.py` checks the exact cross-Hessian
identity, recursive component reconstruction on generated trees through
depth six, root-color detection and scope markers.  The uniform mathematical
proof is Lemma 2.1 and Theorem 3.1.  The verifier does not assert H7-RF-CUT.
