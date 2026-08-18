# 114.a.29 — H7-K: the outer-label compatibility gate

```
+--------------------------------------------------------------------------+
| LAURENT     P_mn has first/first outer labels; algebraic separation is   |
|             reduced to H7-DFLAT. a_30 closes a bounded revised family.   |
| CROSS       C_mn has first/second outer labels; real membership is       |
|             proved in a_28, but separation H7-XI is open.                |
| WARNING     Their ordinary folds agree, but the generic trees do not.   |
| GATE        Prove H7-DFLAT for the bounded a_30 Laurent tree, or H7-XI.  |
| FORBIDDEN   Do not identify them by total commutativity: that collapses  |
|             Z tensor_F Z to Z.                                          |
+--------------------------------------------------------------------------+
```

## 1. The two scalar trees

For vectors `a=(a_j)` and `b=(b_j)`, let `delta_1` and `delta_2` denote the
corollas supplied by the two copies of `Z` in

\[
 B=\mathbb Z_1\otimes_{\mathbb F\{\pm1\}}\mathbb Z_2.   \tag{1.1}
\]

The first-additive Laurent scalar used in `114_a_25` is

\[
 P(a,b)=delta_1\circ\mathrm{diag}(i_1(a_j)i_2(b_j))
                    \circ\delta_1^t.                    \tag{1.2}
\]

The genuinely bounded cross-contraction of `114_a_28` is

\[
 C(a,b)=igl(\delta_1\circ\mathrm{diag}(i_1(a_j))\bigr)
          \circ
          \bigl(\mathrm{diag}(i_2(b_j))\circ\delta_2^t\bigr).
                                                               \tag{1.3}
\]

After associativity, (1.3) has outer labels `(1,2)`, whereas (1.2) has
outer labels `(1,1)`. The tree presentation in Haran 2017
(10.9)--(10.22) records both the root and coroot labels. Therefore
associativity within a label does not identify (1.2) and (1.3).

Both have the same ordinary diagonal fold:

\[
 \mathrm{fold}\,P(a,b)
 =\sum_j a_jb_j
 =\mathrm{fold}\,C(a,b).                            \tag{1.4}
\]

Equality after fold is not equality in `B`; `114_a_20` proves that the fold
has only `exp(O(m+n))` possible bounded rational values and hence cannot
certify a family of size `exp(Theta(mn))`.

## 2. Why the real proof selects the cross tree

At a real-real chart, Haran's local F-ring consists of operators preserving
Euclidean unit balls (2017 (4.6)). With

\[
 a_j=p^j/p^m\ (0\le j<m),\qquad b_j=c_j/q^n,
                                                               \tag{2.1}
\]

`114_a_28` proves `||a||_2<1` and `||b||_2<=1`. Thus the two factors in
(1.3) are local and their composition is local.

The analogous factorization of (1.2) would require the second weighted
column

\[
 \mathrm{diag}(i_2(b_j))\delta_1^t                \tag{2.2}
\]

to lie in the product chart. Its ordinary coefficient vector has norm at
most one, but the coefficient map from a generalized product chart to
ordinary matrices is not asserted to be surjective; Haran explicitly notes
after (4.6) that even coefficient-map injectivity can fail in residue-field
examples. Hence ordinary norm control does not prove membership of (2.2).

Call the missing statement:

> **H7-WV.** Weighted first-ruling vectors with second-ruling line-bundle
> coefficients and Euclidean coefficient norm at most one belong to every
> relevant product chart.

`114_a_30` closes H7-WV for a revised Laurent family by replacing the wide
weighted corolla with a binary tree of local dyadic contractions.

## 3. Why algebraic separation presently selects the Laurent tree

The power characters in `114_a_25` and the Laurent normal-form equivalence
in `114_a_26` concern the ordinary scalar ring selected by first addition.
They apply to (1.2). They do not evaluate the second-labeled coroot in
(1.3). Thus H7-DFLAT would prove separation of `P`, not of `C`.

Call the alternative missing statement:

> **H7-XI.** For `a_j=p^j/p^m`, the map
> `c -> C(a,c/q^n)` is injective on `I_m(q^n)`.

Either pair

\[
 (\mathrm{H7\!\!-DFLAT}+\underbrace{\mathrm{H7\!\!-WV}}_{\text{closed in }a_{30}})
 \quad\text{or}\quad
 \mathrm{H7\!\!-XI}                                    \tag{3.1}
\]

would produce one and the same scalar family that is both bounded and
injective. On the Laurent side, `a_30` supplies H7-WV and quadratic entropy.
`114_a_31` subsequently proves that full H7-DFLAT/LNF would violate H7-U,
so only selective separation can complete the raw-cardinality package.

## 4. Total commutativity is not a repair

The interchange

\[
 \delta_1\circ(\delta_2\oplus\delta_2)
 =\delta_2\circ(\delta_1\oplus\delta_1)                 \tag{4.1}
\]

would allow unrestricted swapping of the two outer labels. Haran 2017
(7.17) proves that, together with restrictions to two leaves, (4.1) forces
`delta_1=delta_2` and

\[
 \mathbb Z\otimes_{\mathbb F\{\pm1\}}\mathbb Z
 =\mathbb Z.                                             \tag{4.2}
\]

That destroys the off-diagonal arithmetic plane. Therefore no proof may
silently use total interchange to combine (1.2) and (1.3).

## 5. Acceptance rule

The H7-K lower bound remains open until a **single typed family** has both:

1. off-diagonal injectivity after all Haran relations; and
2. membership in every finite and real chart of the same bundle.

The Laurent and cross results cannot be spliced across different outer
labels. This acceptance rule is structural and has no numerical verifier;
the cited verifiers check the algebraic entropy and norm inequalities only.
