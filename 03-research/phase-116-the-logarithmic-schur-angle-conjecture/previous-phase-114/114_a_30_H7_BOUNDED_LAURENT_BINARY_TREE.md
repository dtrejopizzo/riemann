# 114.a.30 — H7-WV: a genuinely bounded Laurent tree

> **Geometric typing correction (`a_63`).** The tree family and its scalar
> bounds survive. Its realization inside the displayed completed bundle on
> `Y` is conditional on H7-PB-REG/H7-PRIME-REG.

```
+--------------------------------------------------------------------------+
| NODE        A(x,y)=(1/2,1/2) o (x direct-sum y) o (1/2,1/2)^t.          |
| REAL        Both node vectors have Euclidean norm 1/sqrt(2).             |
| TREE        Depth d gives weight 4^{-d} to each of 2^d leaves.           |
| DIGITS      Repeat leaf c_j/q^n exactly 3^j times.                       |
| THEOREM     The resulting first-additive Laurent scalar is a genuine     |
|             bounded section of bidegree (2d,n).                          |
| ENTROPY     r_d~d log(2)/log(3), so log #I_{r_d}(q^n)=Theta(dn).         |
| OPEN        H7-DFLAT gives lower injectivity, but a_31 proves full LNF   |
|             is incompatible with the required upper bound H7-U.          |
+--------------------------------------------------------------------------+
```

## 1. A local binary averaging node

Work with the prime `2` on the first ruling and a distinct prime `q` on the
second. In the rational localization of the first ruling put

\[
 u=(1/2,1/2)\in B_{[1],[2]}                              \tag{1.1}
\]

and define, for scalars `x,y`,

\[
 A(x,y)=u\circ(x\oplus y)\circ u^t.                     \tag{1.2}
\]

In the scalar ring selected by first addition,

\[
 A(x,y)=\frac{x+y}{4}.                                  \tag{1.3}
\]

At the real chart, Haran 2017 (4.6) gives

\[
 \|u\|_2=\sqrt{(1/2)^2+(1/2)^2}=1/\sqrt2<1.            \tag{1.4}
\]

Thus both `u` and `u^t` are local contraction operators. At the finite prime
`2`, the two factors `1/2` contribute total valuation `-2`; hence (1.2)
consumes exactly `L_2^2`. At every other finite prime they are units.

## 2. The depth-d Laurent tree

Iterate (1.2) in a complete binary tree of depth `d`. It has `2^d` leaves,
and induction using (1.3) gives

\[
 A_d(z_1,\ldots,z_{2^d})
 =4^{-d}\sum_{k=1}^{2^d}z_k.                            \tag{2.1}
\]

Every root and coroot in this tree belongs to the first ruling. Therefore
(2.1) is a first-additive Laurent scalar, not the first/second
cross-contraction of `114_a_28`.

Define

\[
 r_d=\max\left\{r\ge1:\sum_{j=0}^{r-1}3^j
                         =\frac{3^r-1}{2}\le2^d\right\}.
                                                               \tag{2.2}
\]

Equivalently,

\[
 r_d=\left\lfloor\log_3(2^{d+1}+1)\right\rfloor,
 \qquad r_d=\frac{\log2}{\log3}d+O(1).                 \tag{2.3}
\]

For `c=(c_0,...,c_{r_d-1}) in I_{r_d}(Q)`, `Q=q^n`, fill exactly `3^j`
leaves with the second-ruling scalar `i_2(c_j/Q)` and fill the unused leaves
with zero. The resulting scalar is

\[
 T_{d,n}(c)=4^{-d}\sum_{j=0}^{r_d-1}3^j i_2(c_j/Q).
                                                               \tag{2.4}
\]

The value is independent of the placement of equal leaves because the
first addition is commutative and associative.

## 3. Genuine local and pro-section membership

### Theorem 3.1 (H7-WV for the binary Laurent family)

For every `d,n>=1` and `c in I_{r_d}(q^n)`,

\[
 T_{d,n}(c)\in
 \mathcal O_Y\left(p_1^*L_2^{2d}\otimes p_2^*L_q^n\right)_{[1],[1]}.
                                                               \tag{3.1}
\]

### Proof

At every real occurrence of the first factor, (1.4) puts the row and column
of each internal node in the Euclidean operator ball. Each second-ruling
leaf satisfies `|c_j/Q|<=1`, because `||c||_1<=Q`. Closure of the local
F-ring under direct sum, transpose and composition proves real and
real-real membership recursively.

At the finite prime `2`, every root-to-leaf path contains `d` nodes and two
factors `1/2` per node. Multiplication by the local trivializer `2^{2d}` of
`L_2^{2d}` clears them. At `q`, multiplication by `Q` clears the common leaf
denominator; first-additive composition does not multiply that denominator
between distinct leaves. Other finite primes see only units. The same fixed
rational tree is used at every finite stage, so the pro-condition (11.13)
holds. QED.

This proves genuine membership of the **same outer-label family** to which
the Laurent criterion `114_a_26` applies. It closes H7-WV for this revised
family.

## 4. Quadratic entropy and conditional noncollision

The exact domain size is

\[
 \#I_{r_d}(Q)=
 \sum_{k=0}^{\min(r_d,Q)}2^k{r_d\choose k}{Q\choose k}. \tag{4.1}
\]

For comparable `d,n`, (2.3) and the cross-polytope squeeze give

\[
 \log\#I_{r_d}(q^n)
 =\frac{\log2\,\log q}{\log3}dn-O(d\log d+n).           \tag{4.2}
\]

In terms of first bidegree `M=2d`, the leading constant is
`log(2)log(q)/(2log(3))` times `Mn`; it is positive and quadratic.

If H7-LNF holds, equality of two values in (2.4) yields, under every power
character,

\[
 \sum_j3^j\mathrm{sgn}(c_j)|c_j|^\sigma
 =\sum_j3^j\mathrm{sgn}(c'_j)|c'_j|^\sigma.       \tag{4.3}
\]

Independence of the functions `a^sigma`, followed by uniqueness of balanced
base-3 digits, gives `c=c'` exactly as in `114_a_25`. Thus H7-DFLAT from
`114_a_27` would prove injectivity of this lower-bound family. However,
`114_a_31` proves that full H7-LNF makes the entire bounded scalar set
superquadratic, contradicting H7-U. A selective normal form H7-SEL or a
normalized dimension is therefore required for the complete package.

## 5. Why this does not use total commutativity

Every internal row and column in (1.2) comes from the first ruling. The
second ruling occurs only in scalar leaf coefficients. No interchange of
`delta_1` with `delta_2` is used. Hence the construction does not invoke the
total-commutativity relation that collapses the arithmetic plane.

## 6. Verification scope

`114_a_30_h7_bounded_laurent_tree_verify.py` checks the exact node norm,
tree coefficient, leaf capacity, formula for `r_d`, finite valuations,
cross-polytope count and quadratic leading constant. The local membership
argument is the recursive application of Haran's definitions, not a
numerical approximation. The verifier does not assert H7-DFLAT.
