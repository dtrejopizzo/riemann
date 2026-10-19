# R170_883 — Covariant Dirichlet derivative for the divisor boundary

> **Finite correction.** The physical series come from `S_N`. The
> interval is replaced by its intersection with `n<=N`. The covariant
> formulas remain exact; the excluded series also includes `n>N`.

## 0. Result

The two incidences of R170_879 and R170_882 form an exact connection.
For `Re s>1`, define

\[
 \mathscr M_{N;T,t}(s)
 :=\sum_{k\ge1}{\mathfrak m_{N;T,t}(k)\over k^s},
 \qquad
 \mathscr L_{N;T,t}(s)
 :=\sum_{k\ge1}{\mathfrak l_{N;T,t}(k)\over k^s}.          \tag{0.1}
\]

Let

\[
 A_{N;T,t}(s)
 :=\sum_{\substack{n\le N\\e^{t-T}\le n\le e^{t+T}}}n^{-s}.\tag{0.2}
\]

Then

\[
\boxed{
 \mathscr M_{N;T,t}(s)={A_{N;T,t}(s)\over\zeta(s)},}      \tag{0.3}
\]

\[
\boxed{
 \mathscr L_{N;T,t}(s)
 ={1\over\zeta(s)}
   \sum_{\substack{n\le N\\e^{t-T}\le n\le e^{t+T}}}
        {\log n\over n^s},}                              \tag{0.4}
\]

and, setting

\[
 \nabla_\zeta:=\partial_s+{\zeta'(s)\over\zeta(s)},       \tag{0.5}
\]

one has the covariant law

\[
\boxed{
 \mathscr L_{N;T,t}=-\nabla_\zeta\mathscr M_{N;T,t}.}   \tag{0.6}
\]

The identity is proved in absolute convergence and is equivalent
coefficient by coefficient to `mu*log=Lambda`. It presupposes no
information about the zeros.

## 1. Proof via generating functions

By R170_879,

\[
 \mathfrak m_{N;T,t}(k)
 =\sum_{n\mid k}1_{\{n\le N\}}1_{[e^{t-T},e^{t+T}]}(n)
        \mu(k/n).                                         \tag{1.1}
\]

This is the Dirichlet convolution

\[
 \mathfrak m_{N;T,t}
 =(1_{\{n\le N\}}1_{[e^{t-T},e^{t+T}]})*\mu.            \tag{1.2}
\]

Multiplying the absolutely convergent series gives (0.3). Likewise,

\[
 \mathfrak l_{N;T,t}
 =\bigl(1_{\{n\le N\}}1_{[e^{t-T},e^{t+T}]}\log\bigr)*\mu,\tag{1.3}
\]

which proves (0.4).

Finally `A_T,t'(s)` is the opposite of the numerator of (0.4). Since
`M=A/zeta`,

\[
 \left(\partial_s+{\zeta'\over\zeta}\right)
 {A\over\zeta}={A'\over\zeta}.                            \tag{1.4}
\]

This proves (0.6).

## 2. Exact series of the excluded routes

R170_882 defines

\[
 \mathfrak e_{N;T,t}(k)=\mathfrak l_{N;T,t}(k)-\Lambda(k). \tag{2.1}
\]

Since

\[
 \sum_k{\Lambda(k)\over k^s}=-{\zeta'(s)\over\zeta(s)},  \tag{2.2}
\]

one obtains

\[
\boxed{
 \sum_k{\mathfrak e_{N;T,t}(k)\over k^s}
 ={\zeta'(s)-A_{N;T,t}'(s)\over\zeta(s)}.}                \tag{2.3}
\]

Equivalently,

\[
\boxed{
 \sum_k{\mathfrak e_{N;T,t}(k)\over k^s}
 =-{1\over\zeta(s)}
   \sum_{\substack{n>N\ \text{or}\\n\notin[e^{t-T},e^{t+T}]}}
       {\log n\over n^s}.}                               \tag{2.4}
\]

The last sum converges for `Re s>1`. It is literally the logarithmic
comb of the excluded routes, multiplied by the Möbius inverse.

## 3. The polar continuum lives on the same variable

The continuum of R161_076/R170_856 is

\[
 C_Nf(t)=e^{-t/2}
   \int_{-\infty}^{t+\log N}e^{y/2}f(y)\,dy.              \tag{3.1}
\]

In Laplace coordinates it has multiplier, with the corpus conventions,

\[
 c_N(s)={N^s\over s}.                                     \tag{3.2}
\]

Hence the polar term cannot cancel (2.4) term by term in `k`: one is
a continuum and the other a comb. The legitimate comparison must be made
between their multipliers in `s`, within the full Poisson
identity. Declaring a coefficient-by-coefficient cancellation would be a
type error.

The continuous analogue of (0.2) is

\[
 A^{\rm cont}_{N;T,t}(s)
 :=\int_{e^{t-T}}^{\min(N,e^{t+T})}x^{-s}\,dx,             \tag{3.3}
\]

with elementary formula

\[
 A^{\rm cont}_{N;T,t}(s)
 ={\min(N,e^{t+T})^{1-s}-e^{(1-s)(t-T)}\over1-s},          \tag{3.4}

when `e^(t-T)<=N`, and it is zero when the interval is empty.
\]

The difference

\[
 \mathscr D_{N;T,t}(s):=A_{N;T,t}(s)-A^{\rm cont}_{N;T,t}(s)\tag{3.5}
\]

is the sum--continuum defect over the moving multiplicative
interval. Its covariant derivative is the correct place to
compare the route residue with `dot C_N`.

## 4. Precise transformed door

Formula R170_856(9.3) completely fixes `dot C_N`; R170_844(3.2b)
fixes its Laplace multiplier. The next admissible equality is to check
that the transform of the block

\[
 \mathfrak R_{\rm route}
 +B P\mathcal P_{C,A}F                                   \tag{4.1}
\]

is the covariant derivative, with the correct Gamma/Tate connection, of
`mathscr D_T,t(s)/zeta(s)`. If this holds, the discrete and
continuous terms are left as a single Poisson discrepancy before taking a sign.

This identification remains open. It is stronger than comparing only
the coefficients and weaker than postulating exterior reciprocity: all its
multipliers are given explicitly.

## 5. Scope audit

* (0.3)--(0.6) are identities proved for `Re s>1`.
* `1/zeta` is not continued across zeros, nor is RH used.
* (3.5) has no declared sign.
* The identification of (4.1) with the derivative of (3.5) does not follow from the
  generating functions alone; it requires the literal order of PC-ren.
* Even if proved, minimality will still be needed to orient
  the resulting discrepancy.

## 6. Status

```text
Dirichlet series of the boundary incidence                   PROVED
log-weighted series                                           PROVED
covariant law L=-nabla_zeta M                                 PROVED
exact series of excluded routes                                PROVED
type comparison with the polar continuum                       PROVED
transformed route+polar identification, §4                     OPEN
sign via minimality                                             OPEN
VIR--LB / D                                                     OPEN
```
