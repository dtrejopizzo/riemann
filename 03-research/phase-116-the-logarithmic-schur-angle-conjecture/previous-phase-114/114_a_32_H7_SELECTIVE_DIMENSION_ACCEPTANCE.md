# 114.a.32 — H7-SEL: acceptance test and the convolution obstruction

```
+--------------------------------------------------------------------------+
| POSITIVE    The bounded balanced family of a_30 has the required         |
|             exp(Theta(Mn)) size and a canonical binary dimension with    |
|             Theta(Mn) growth.                                            |
| OBSTRUCTION The family is not closed under multiplication: products      |
|             contain several Laurent labels at one ternary weight.        |
| FORBIDDEN   Combining those labels by [a]+[b]=[a+b] collapses the         |
|             off-diagonal two-addition information used for the lower     |
|             bound.                                                       |
| GATE        H7-SEL must prove separation, an O(Mn) upper bound and        |
|             multiplicative compatibility simultaneously.                |
+--------------------------------------------------------------------------+
```

## 1. The surviving balanced family

Retain the notation of `114_a_30`. Thus

\[
 r_d=\lfloor\log_3(2^{d+1}+1)\rfloor,
 \qquad Q=q^n,
\]

and, before the harmless common factor `4^{-d}`, encode

\[
 B_r(c)=\sum_{j=0}^{r-1}3^j[c_j],
 \qquad c\in I_r(Q).                                    \tag{1.1}
\]

Here `[a]` denotes the Laurent/group-algebra label of the second-ruling
scalar `a`; zero coordinates are omitted. Theorem 3.1 of `a_30` proves
that the corresponding binary trees are genuine bounded scalar sections.
Their parameter entropy is

\[
 \log\#I_{r_d}(q^n)
 =\frac{\log2\,\log q}{\log3}dn-O(d\log d+n).           \tag{1.2}
\]

In first bidegree `M=2d`, this is a positive multiple of `Mn`.

There is also a natural **candidate normalized dimension** on this selected
domain: the Connes--Consani minimal-generator dimension of `a_11` gives

\[
 \dim_{r_d}(q^n)
 =\frac{\log q}{\log3}dn+O(d\log d+n)                  \tag{1.3}
\]

for comparable `d,n`, hence

\[
 \dim_{r_{M/2}}(q^n)
 =\frac{\log q}{2\log3}Mn+O(M\log M+n).                \tag{1.4}
\]

Equations (1.2)--(1.4) solve the numerical growth problem **on the selected
parameter space**. They do not yet define `H^0` or an RR-compatible
dimension on the literal square.

## 2. Exact multiplication obstruction

Multiplication of Laurent labels satisfies `[a][b]=[ab]`. Consequently

\[
 B_r(c)B_s(e)
 =\sum_{j=0}^{r-1}\sum_{k=0}^{s-1}
       3^{j+k}[c_je_k].                                  \tag{2.1}
\]

Already for `r=s=2`, the middle ternary weight is

\[
 3\bigl([c_0e_1]+[c_1e_0]\bigr).                        \tag{2.2}
\]

A balanced code of the original form has only one Laurent label at that
weight. If `c_0e_1` and `c_1e_0` are distinct and nonzero, Laurent
faithfulness makes (2.2) a two-point support, so it cannot equal `3[h_1]`
for any scalar `h_1`. Thus:

### Proposition 2.1

The families `B_r(I_r(Q))` are not multiplicatively closed in the faithful
Laurent algebra, even before imposing a norm or a divisor bound.

### Proof

Choose, for example, `c=(1,1)` and `e=(1,2)`. The weight-three part of
their product is `3([2]+[1])`, whose support has two elements. A term
`3[h_1]` has support one. Equality is impossible in the group algebra.
QED.

The tempting repair is the coefficient-additivity relation

\[
 [a]+[b]=[a+b].                                         \tag{2.3}
\]

But (2.3) identifies the first additive sum of second-ruling scalars with
ordinary addition in the second ruling. Iterating it sends (1.1) to the
single diagonal scalar

\[
 B_r(c)\longmapsto\left[\sum_j3^jc_j\right].            \tag{2.4}
\]

The image of `I_r(Q)` in (2.4) lies in an interval with only
`O(3^rQ)` integral numerator values. Since `r=O(d)` and `Q=q^n`, its
logarithmic size is `O(d+n)`, not `Theta(dn)`. This is the diagonal ceiling
of `a_20` in the present coordinates. Hence (2.3) repairs multiplication
only by destroying the required mixed entropy.

## 3. Necessary acceptance clauses

A proposed selective quotient, normalized dimension or complexity
truncation will be called an **H7-SEL candidate** only if it supplies all of:

1. **Typing and boundedness:** classes are genuine `[1],[1]` bounded
   sections of the stated Haran line bundle, not merely diagonal scalars.
2. **Balanced separation:** the family (1.1) has
   `exp(Theta(Mn))` distinct classes, or normalized dimension `Theta(Mn)`.
3. **Upper control:** all admitted classes in bidegree `(M,n)` have total
   size/dimension `exp(O(Mn))`/`O(Mn)`.
4. **Multiplicative compatibility of the ambient invariant:** the quotient
   or dimension, not necessarily the lower-bound witness family, respects
   products in bidegrees `(M,n)` and `(M',n')` sufficiently for RR.
5. **No diagonal collapse:** the quotient does not imply (2.3), total
   commutativity, or any relation that reduces (1.1) to (2.4).
6. **Geometric canonicity:** the selection depends only on the divisor and
   the pro-square structure; auxiliary choices of tree, prime or expansion
   are either absent or proved to induce canonical isomorphisms.
7. **RR interface:** the resulting dimension has an intersection-theoretic
   leading coefficient and an error term strong enough for the intended
   Riemann--Roch argument.

Clauses 1--3 separately exist as partial ingredients (`a_30`, `a_31` and
(1.3)), but no construction currently satisfies clauses 2--5 together.
Proposition 2.1 shows only that declaring the balanced family itself to be
the whole section space fails clause 4. It does not invalidate that family
as a lower-bound witness inside a larger ambient invariant; `a_33` develops
this distinction. Relation (2.3) still fails clauses 2 and 5.

## 4. Consequence for row A

The live route is now narrower:

\[
 \boxed{\text{bounded balanced code}
 \;\longrightarrow\;\mathrm{H7\!\!-SEL}
 \;\longrightarrow\;\text{intersection/RR}
 \;\longrightarrow\;\Lambda/\xi\text{ link}.}
\]

The first arrow's source is constructed; its target is not. Full Laurent
faithfulness is ruled out by `a_31`, and diagonal coefficient-additivity is
ruled out by Proposition 2.1 plus (2.4). Therefore row A remains open at a
single explicit algebraic-geometric design problem rather than at the old
undifferentiated request for a Haran gauge.

## 5. Verification scope

`114_a_32_h7_selective_acceptance_verify.py` checks the finite convolution
support obstruction, the diagonal range bound and the quadratic versus
linear growth separation. It does not assert existence of H7-SEL.
