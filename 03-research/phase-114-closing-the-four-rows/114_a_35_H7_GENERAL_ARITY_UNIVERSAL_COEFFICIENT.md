# 114.a.35 — General-arity bounded trees and the universal mixed coefficient

```
+--------------------------------------------------------------------------+
| NODE        u_k=(1/k,...,1/k) gives a genuine k-ary Euclidean            |
|             contraction and scalar average k^(-2) sum_(1).               |
| DEPTH d     N=k^d leaves, coefficient k^(-2d), finite divisor            |
|             2d div(k) on the first ruling.                               |
| CODE        r=floor(log_3(2k^d+1)) signed slots are optimal.             |
| UNIVERSAL   h_code ~ deg(D_1)deg(D_2)/(2log 3), independent of k and     |
|             of the prime factorizations.                                |
| STATUS      Bounded family and coefficient are closed; global moment     |
|             descent and RR promotion remain open.                        |
+--------------------------------------------------------------------------+
```

## 1. The `k`-ary contraction

Fix an integer `k>=2` and put

\[
 u_k=(1/k,\ldots,1/k)\in\mathbb R^k,
 \qquad \|u_k\|_2=k^{-1/2}\le1.                        \tag{1.1}
\]

Using only the first ruling, define the scalar node

\[
 A_k(x_1,\ldots,x_k)
 =u_k\circ(x_1\oplus\cdots\oplus x_k)\circ u_k^t
 =\frac1{k^2}\sum_{i=1}^k{}_{(1)}x_i.                 \tag{1.2}
\]

Both the row and column in (1.2) lie in Haran's real Euclidean unit ball.
A complete depth-`d` iteration has

\[
 N=k^d\quad\text{leaves},\qquad
 A_{k,d}(x)=k^{-2d}\sum_{i=1}^{k^d}{}_{(1)}x_i.        \tag{1.3}
\]

At a finite prime `p`, the denominator contributed by the internal nodes is
`p^{2d v_p(k)}`. Hence it is cleared by the first-ruling divisor

\[
 D_1(k,d)=2d\sum_{p\mid k}v_p(k)L_p,
 \qquad \deg D_1(k,d)=2d\log k.                        \tag{1.4}
\]

## 2. An arbitrary effective second-ruling denominator

Let

\[
 E=\sum_q b_qL_q,\qquad
 Q(E)=\prod_q q^{b_q},\qquad \deg E=\log Q(E).          \tag{2.1}
\]

Set

\[
 r_{k,d}=\lfloor\log_3(2k^d+1)\rfloor.                \tag{2.2}
\]

For `c in I_{r_{k,d}}(Q(E))`, put `3^j` copies of the leaf
`i_2(c_j/Q(E))` into (1.3), and fill the unused leaves with zero. The
resulting scalar is

\[
 T_{k,d,E}(c)=k^{-2d}
 \sum_{j=0}^{r_{k,d}-1}3^j i_2(c_j/Q(E)).              \tag{2.3}
\]

### Theorem 2.1 (general bounded family)

Every (2.3) is a genuine bounded scalar pro-section of

\[
 p_1^*\mathcal O(D_1(k,d))\otimes p_2^*\mathcal O(E).  \tag{2.4}
\]

### Proof

The real assertion follows recursively from (1.1)--(1.2) and
`|c_j|<=Q(E)`. At each `p|k`, (1.4) clears the internal denominator. At each
`q|Q(E)`, the second divisor clears the common leaf denominator. All other
finite primes see units. The same rational tree works at every refinement,
so Haran's pro-section condition (11.13) holds. Finally,

\[
 \sum_{j<r_{k,d}}3^j=(3^{r_{k,d}}-1)/2\le k^d,
\]

so all prescribed leaves fit. QED.

By `a_34`, (2.2) is the maximal possible signed integer-multiplicity rank
for `k^d` leaves.

## 3. Universal coefficient

As `d` and `deg E` grow on a fixed positive ray,

\[
 r_{k,d}=\frac{d\log k}{\log3}+O(1).                  \tag{3.1}
\]

The cross-polytope count therefore gives

\[
 \log\#I_{r_{k,d}}(Q(E))
 =\frac{d\log k}{\log3}\deg E
   -O(d\log d+\deg E).                                \tag{3.2}
\]

Using (1.4), its leading term is

\[
 \boxed{\quad
 \frac{1}{2\log3}\deg D_1(k,d)\deg E.
 \quad}                                                \tag{3.3}
\]

Thus the coefficient found in `a_34` does not depend on choosing the prime
`2`, the prime `q`, or even binary arity. It depends only on the two idelic
degrees and the optimal three-symbol signed capacity.

## 4. Independence of presentation along divisor rays

Let

\[
 A=\sum_pa_pL_p,\qquad P=\prod_pp^{a_p},
 \qquad B=\sum_qb_qL_q,\qquad Q=\prod_qq^{b_q}.        \tag{4.1}
\]

For the ray `(2tA,tB)`, take `k=P`, depth `d=t` and `E=tB`. Then

\[
 \log\#I_{r_{P,t}}(Q^t)
 =\frac{\log P\log Q}{\log3}t^2-O(t\log t).           \tag{4.2}
\]

Replacing `k=P` and depth `t` by `k=P^a` and depth `t/a` whenever `a|t`
does not change the leaf count `P^t`, the internal coefficient `P^{-2t}`,
the rank (2.2), or the leading term. Unique factorization makes `P` and `Q`
intrinsic to the effective divisor presentations. Hence the code
coefficient is functorial under regrouping of prime factors on these rays.

This closes the prime/arity dependence left in `a_34`. At this stage it did
not prove invariance under principal divisor relations or extend the
finite-moment quotient to all alternating scalar trees.

`a_51` later closes the alternating-tree extension on every fixed ray.
Principal-divisor and arbitrary-presentation invariance remain global gates.

## 5. Verification scope

`114_a_35_h7_general_arity_verify.py` checks all local norm, leaf,
valuation, presentation-independence and universal-coefficient identities
for many finite choices. H7-FMD descent is proved later in `a_49`; this
verifier does not assert the later full-tree theorem `a_51` or H7-RR0.
