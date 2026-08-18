# 114.a.51 — H7-FMD-ALL on fixed rays via finite twisted bios

> **All-arity use (`a_72`).** Retaining the full target bio, rather than only
> its unary moment shadow, separates the arbitrary-arity block families of
> `a_21` and their one-output versions from `a_22`.  This proves prime
> cancellation on those same-fold fibers, not on every nested tree class.

```
+--------------------------------------------------------------------------+
| PRIME       Choose p>A with no odd prime <=4r dividing p-1.             |
| EXPONENTS   s=1,3,...,4r-1 are units mod p-1.                           |
| FIELD LAW   x -> x^s is a multiplicative bijection and transports a     |
|             second field addition on F_p.                               |
| FULL BIO    a_49 gives a bio map for every s, hence every scalar tree    |
|             has an s-th finite evaluation.                              |
| SEPARATE    Odd moments are a Vandermonde system in x^2.                 |
| COFINAL     Accumulating dyadic levels gives compatible O(t^2) targets.  |
| RESULT      H7-FMD-ALL is closed on every fixed effective ray.           |
| LATER       a_55 refutes sharp RR for the complete bounded image.       |
+--------------------------------------------------------------------------+
```

## 1. A controlled prime with many invertible odd exponents

Fix a rank `r`, denominator height `Q`, and put

\[
 A=\max(2Q,3^r,2^{4r}),\qquad
 P_r=\prod_{\substack{\ell\le4r-1\\ \ell\ {m odd\ prime}}}\ell.       \tag{1.1}
\]

Choose the unique integer `a` in `(A,A+P_r]` with `a=2 mod P_r`, and choose
by Bertrand a prime `R` with `a<R<2a`. Set `N=P_rR`. Then `(a,N)=1`.

Let `p` be the least prime congruent to `a` modulo `N`. Linnik's theorem
gives absolute `L,C` such that

\[
 p\equiv a\pmod N,qquad p\le C N^L.                                    \tag{1.2}
\]

Since `p` is either `a` itself or at least `a+N`, one has `p>A`. Moreover,
for every odd prime `ell<=4r-1`,

\[
 p-1\equiv1\pmod\ell.                                                     \tag{1.3}
\]

Thus

\[
 \gcd(s,p-1)=1\qquad
 (s=1,3,\ldots,4r-1).                                                     \tag{1.4}
\]

The Chebyshev bound `log P_r=O(r)`, Bertrand and (1.2) give

\[
 \boxed{\log p=O(r+\log Q).}                                             \tag{1.5}
\]

Only the existence of an absolute Linnik exponent is needed. One may use
[Xylouris, arXiv:0906.2749](https://arxiv.org/abs/0906.2749), which proves an
explicit admissible exponent.

The extra term `2^(4r)` will be used in `a_55`: for the `2r` odd
exponents in (1.4), the ordinary integers `2^s` are pairwise distinct
modulo `p`. It does not change (1.5).

## 2. Finite twisted-field bios

For every odd `s` in (1.4), let `e_s` be its inverse modulo `p-1` and define

\[
 T_s(x)=x^{e_s},qquad U_s(x)=x^s                                      \tag{2.1}
\]

on `F_p`, with both maps fixing zero. They are inverse multiplicative
bijections. Transport ordinary addition by

\[
 x+_{(s)}y=U_s\bigl(T_s(x)+T_s(y)\bigr).                                 \tag{2.2}

Then `F_{p,s}=(F_p,+_(s),multiplication)` is a field sharing its
multiplication with ordinary `F_p`. Its unique integral map is

\[
 n\longmapsto (n\bmod p)^s.                                              \tag{2.3}

Apply the homogeneous-endobio construction of `a_49` over the finite set
`F_p`. The ordinary and transported ring bios map simultaneously into a
finite commutative bio, and its involutive double supplies a target for the
two structural maps from `P_Z`. By the coproduct property there is therefore
a bio map from Haran's full scalar plane, not merely its Laurent subring.

On unary scalars, projection to the common multiplication action gives

\[
 \varepsilon_{p,s}:A_{\rm full}(1)\longrightarrow\mathbb F_p,            \tag{2.4}

with

\[
 \varepsilon_{p,s}(i_1(a)i_2(b))=a b^s\pmod p.                           \tag{2.5}

All fixed ray denominators are invertible because `p>A`.

### Theorem 2.1 (full-tree descent)

The product

\[
 \mathcal E^{\rm all}_{r,Q}
 =\prod_{k=0}^{2r-1}\varepsilon_{p,,2k+1}                               \tag{2.6}

is defined on every unary scalar tree and is compatible with the selected
first addition and multiplication. Hence it defines a finite normalized
quotient of the complete bounded scalar section set in that degree.

This is stronger than H7-FMD descent in `a_33`: no Laurent normal form or
cofinality assumption is used to define (2.6).

## 3. Odd-Vandermonde separation

Suppose a difference of two balanced codes has distinct positive labels
`x_1,...,x_v`, `v<=2r`, and grouped coefficients `C_i`. The first `v` odd
moments have matrix

\[
 V=(x_i^{2k+1})_{0\le k<v,1\le i\le v}.                                 \tag{3.1}

Its determinant is

\[
 \det V=\left(\prod_i x_i\right)
        \prod_{i<j}(x_j^2-x_i^2).                                       \tag{3.2}

Write `x_i=a_i/Q`, with `1<=a_i<=Q`. Since `p>2Q`, distinct `a_i` are
neither equal nor opposite modulo `p`; (3.2) is nonzero. Therefore every
`C_i=0 mod p`. But `|C_i|<3^r<p`, so every `C_i` is zero over the integers.
Balanced ternary uniqueness finishes the separation.

### Theorem 3.1

The full-tree quotient (2.6) is injective on the complete balanced code and
has target size

\[
 \log\#(\mathbb F_p)^{2r}=2r\log p
 =O(r^2+r\log Q).                                                        \tag{3.3}

On the balanced ray `r=Theta(t)`, `log Q=Theta(t)`, this is `O(t^2)` and
matches the `Omega(t^2)` lower bound.

## 4. Compatible cofinal full-tree system

At dyadic scales `T_j=2^j`, choose `p_j` by Section 1 for `(r_j,Q_j)`. Let

\[
 \mathcal V_j=
 \prod_{i=0}^j\prod_{k=0}^{2r_i-1}\mathbb F_{p_i},                       \tag{4.1}

and use all the corresponding bio evaluations. The transition
`V_{j+1}->V_j` is coordinate projection, so it is exact and compatible with
addition and products. The newest block separates every code of degree
`t<=T_j`.

By (1.5),

\[
 \log\#\mathcal V_j
 =\sum_{i=0}^j2r_i\log p_i
 =O\left(\sum_{i=0}^jT_i^2\right)=O(T_j^2).                              \tag{4.2}

Thus compatibility does not inflate the quadratic exponent.

## 5. Status of H7-FMD-ALL and RR

For every fixed effective ray, define the normalized scalar size in degree
`t` as the logarithm of the image of the complete bounded scalar section set
in the least cofinal target `V_j` with `t<=T_j`. Theorems 2.1--3.1 give a
quadratic upper bound on all scalar trees and the matching balanced-code
lower bound. Therefore:

\[
 \boxed{\text{H7-FMD-ALL is closed on every fixed effective ray.}}        \tag{5.1}

Still open:

1. a presentation-independent choice valid simultaneously for arbitrary
   divisor rays and principal-divisor changes;
2. compatibility with sheaf restrictions and exact sequences, rather than
   only scalar addition/product and degree transitions;
3. identification of a suitable selective polarized leading term with a
   global intersection pairing.

`a_55` later proves that item 3 cannot use the complete bounded image in
these targets: bounded cross-interpolation saturates a full block with the
wrong quadratic coefficient. The surviving replacement is H7-SEL-RR/EXACT.

## 6. Verification scope

`114_a_51_h7_full_tree_bio_moment_verify.py` checks the prime congruence,
invertible odd exponents, transported field laws, full-tree homogeneity,
odd-Vandermonde determinants and exhaustive balanced-code separation in
finite examples. Linnik's theorem supplies the uniform asymptotic prime-size
bound used in (1.5).
