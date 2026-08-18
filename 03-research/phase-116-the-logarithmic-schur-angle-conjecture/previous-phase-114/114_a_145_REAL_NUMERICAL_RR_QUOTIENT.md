# 114.a.145 — The real numerical RR quotient is the hyperbolic plane

## 1. Statement

Let

\[
 V=\left(\bigoplus_p\mathbb R e_{p,1}\right)\oplus
   \left(\bigoplus_p\mathbb R e_{p,2}\right)
\]

with finite support, and put

\[
 d_i(x)=\sum_p x_{p,i}\log p.
\]

For any fixed constant `c>0`, define the total Riemann--Roch form

\[
 B_c(x,y)=c\bigl(d_1(x)d_2(y)+d_2(x)d_1(y)\bigr).
\]

### Theorem 1.1

The radical of `B_c` is exactly

\[
 R=\ker(d_1,d_2).
\]

Consequently

\[
 N_A^{\rm RR}:=V/R\simeq\mathbb R^2
\]

through the degree map.  In degree coordinates the descended matrix is

\[
 c\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

so it has signature `(1,1)`.  If `H` is the class with degree vector
`(1,1)`, then `H^2=2c>0`, and on

\[
 H^\perp=\{(a,-a):a\in\mathbb R\}
\]

the quadratic form is `-2ca^2`, hence negative definite.

### Proof

Every vector in `R` is visibly radical.  Conversely, suppose `x` is
radical.  Pairing with `e_(p,1)` gives

\[
 0=B_c(x,e_{p,1})=c\,d_2(x)\log p,
\]

so `d_2(x)=0`.  Pairing with `e_(p,2)` gives `d_1(x)=0`.  This proves the
radical formula.  The degree map is surjective because
`e_(2,i)/log(2)` has degree one in the `i`th coordinate.  The matrix and
Hodge-index calculation are immediate.  QED.

## 2. What this resolves

The infinite signature of the Green complement

\[
 G_c=B_c-C_\Lambda
\]

does not by itself prevent a Hodge-index statement: Hodge index belongs to
the **total** RR intersection `B_c`, and its real numerical quotient is the
two-dimensional hyperbolic plane above.  Contact and Green need not descend
separately to this quotient; only their sum does.

This supplies a canonical finite-dimensional real numerical quotient once
`B_c` exists.  It does **not** prove that the integral Neron--Severi group is
finitely generated.  In fact, on the integral finite-support lattice the
degree maps are injective on each ruling by unique factorization, so the
integral numerical radical is zero and the integral quotient still has
countably infinite rank.  The exact candid formulation is therefore:

- finite-dimensional real numerical RR space: proved;
- finitely generated integral Neron--Severi lattice: not proved;
- Hodge index on the real RR quotient: proved for every `c>0`;
- intrinsic construction and normalization of `B_c`: still required.

## 3. Why this does not fix the calibration

The Hodge-index conclusion is invariant under replacing `c` by any positive
constant.  It therefore cannot select the coefficient of the RR determinant.
The interpolation construction's base dependence remains a logically
separate problem.

