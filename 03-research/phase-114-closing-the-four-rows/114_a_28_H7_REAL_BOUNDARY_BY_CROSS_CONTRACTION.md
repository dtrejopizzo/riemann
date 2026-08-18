# 114.a.28 — H7-B: genuine real-boundary membership

> **Geometric typing correction (`a_63`).** The contraction and bounded scalar
> formulas are unchanged. Calling their target a completed square-bundle
> section requires H7-PB-REG/H7-PRIME-REG.

```
+--------------------------------------------------------------------------+
| REVISION    Use the m layers p^j/p^m, 0<=j<m; omit the top layer 1.      |
| TYPING      The mixed sum is one cross-contraction alpha o beta^t.       |
| REAL BOUND  ||alpha||_2<1 and ||beta||_2<=1.                             |
| THEOREM     Every cross-contraction is a bounded pro-section of B_mn.    |
| ENTROPY     log #I_m(q^n)=mn log q-O(m log m+n).                         |
| STILL OPEN  Cross-contraction noncollision H7-XI and upper bound H7-U.   |
+--------------------------------------------------------------------------+
```

## 1. The revised intrinsic family

Fix distinct primes `p,q`, with `p>=3`, and put `P=p^m`, `Q=q^n`. Use

\[
 \alpha_m=\left(\frac1P,\frac pP,\ldots,
                       \frac{p^{m-1}}P\right),           \tag{1.1}
\]

an `m`-component row from the first ruling. For

\[
 c=(c_0,\ldots,c_{m-1})\in I_m(Q),\qquad
 \sum_j|c_j|\le Q,                                      \tag{1.2}
\]

put

\[
 \beta_c=\left(\frac{c_0}Q,\ldots,rac{c_{m-1}}Q\right)\tag{1.3}
\]

in the second ruling. Define the typed scalar

\[
 \mathcal C_{m,n}(c)
 =p_1^*\alpha_m\circ(p_2^*\beta_c)^t.                   \tag{1.4}
\]

Its input and output are scalar; `m` is the canonical number of
prime-valuation layers, not a freely selected output component.

There is an essential typing distinction. The tree in (1.4) has a
first-ruling row root and a second-ruling column root. It is **not** asserted
to equal the first-additive Laurent family of `114_a_25`, whose two outer
corollas come from the first ruling. Ordinary diagonal fold sends both to the
same dot product, but `114_a_20` shows that the fold cannot detect the needed
off-diagonal distinctions.

## 2. Finite-chart membership

Let

\[
 \mathcal B_{m,n}=p_1^*L_p^m\otimes p_2^*L_q^n.         \tag{2.1}
\]

At every finite chart, trivializing `L_p^m` multiplies (1.1) by `P`, leaving
the integral vector `(1,p,...,p^{m-1})`; trivializing `L_q^n` multiplies
(1.3) by `Q`, leaving the integral vector `c`. At primes different from
`p,q`, the denominators are units. Hence both vectors lie in their local
section modules. Closure of Haran's structure F-ring under transpose and
composition puts (1.4) in the local scalar section of (2.1).

The same rational vectors are used at every finite stage, so pullback
compatibility is automatic. This is precisely the pro-section condition
(11.13).

## 3. Real-chart membership

Haran 2017 (4.6) defines the real local F-ring by real matrices that map the
Euclidean unit ball into itself. A row vector is therefore local exactly
when its Euclidean norm is at most one. For (1.1),

\[
 \|\alpha_m\|_2^2
 =\sum_{j=0}^{m-1}\frac{p^{2j}}{p^{2m}}
 =\frac{1-p^{-2m}}{p^2-1}<1.                            \tag{3.1}
\]

For (1.3),

\[
 \|\beta_c\|_2
 \le\|\beta_c\|_1
 =\frac{\|c\|_1}{Q}\le1.                              \tag{3.2}
\]

These estimates cover the real-real chart simultaneously. On a real-finite
or finite-real chart, use (3.1) or (3.2) on the real factor and the integral
calculation of Section 2 on the other. Since the local F-rings are closed
under transpose and composition, (1.4) lies in every real-boundary chart.

### Theorem 3.1 (H7-B for the intrinsic mixed family)

For every `m,n>=1` and every `c in I_m(q^n)`,

\[
 \mathcal C_{m,n}(c)
 \in\mathcal O_Y(\mathcal B_{m,n})_{[1],[1]}.           \tag{3.3}
\]

It is a genuine bounded pro-section, not merely an element passing the
diagonal absolute-value test.

### Proof

Finite membership and pro-compatibility are Section 2. Equations
(3.1)--(3.2) give membership in each real factor, including their product.
Composition and transpose preserve the local structure F-ring, proving
(3.3). QED.

## 4. Quadratic domain survives the revision

The exact cross-polytope count is

\[
 \#I_m(Q)=\sum_{j=0}^{\min(m,Q)}2^j{m\choose j}{Q\choose j}.               \tag{4.1}
\]

For `Q=q^n` and comparable `m,n`, the same squeeze as `114_a_24` gives

\[
 \log\#I_m(q^n)=mn\log q-O(m\log m+n).                  \tag{4.2}
\]

Omitting one layer changes only lower-order terms. To turn (3.3)--(4.2) into
the H7-K lower bound one needs the separate typed statement

> **H7-XI.** The cross-contraction map `C_mn` in (1.4) is injective on
> `I_m(q^n)` after Haran's tree relations.

H7-DFLAT/H7-LNF concerns the first-additive Laurent family and does not, by
itself, prove H7-XI. Conversely, the present theorem closes genuine boundary
membership for the cross-contraction family but not for the Laurent family.
These are two complementary routes, not one completed argument.

H7-U, the upper bound on all bounded scalar normal forms, remains separate.

## 5. Verification scope

`114_a_28_h7_real_boundary_verify.py` checks the exact Euclidean norm,
finite trivializations, cross-polytope count and quadratic entropy. The
typed local-membership proof uses the source definitions (4.6), (11.7) and
(11.13), not numerical sampling. It does not assert H7-XI.
