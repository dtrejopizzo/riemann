# 107.234 -- Arithmetic-divisor sheaves descend monoidally to the square

## 1. Published input and exact scope

Connes--Consani, *On the Jacobian of* \(\overline{\operatorname{Spec}\mathbb Z}\)
(arXiv:2602.15941v1), prove three separate statements:

1. the Riemann sector \(X_{\mathbb Q}\) is canonically the arithmetic Picard
   monoid of pairs \(\mathcal D=(L,\|\cdot\|)\);
2. multiplication of adeles is tensor product of the rank-one groups and
   their seminorms;
3. every \(\mathcal D\) defines an \(\mathcal O_{\overline{\operatorname{Spec}
   \mathbb Z}}\)-module \(\mathcal O(\mathcal D)\), whose archimedean
   sections satisfy the mass bound
   \(\sum_x\|\phi(x)\|\leq1\).

The paper does not state the strong-monoidality assertion below.  That is the
new step proved here.  It closes module-level tensor descent, not cohomology or
Riemann--Roch on the square.

## 2. Algebraic tensor lemma

Let \(L_1,L_2\subset\mathbb Q\) be torsion-free groups of rank one and let

\[
 \mu:L_1\otimes_{\mathbb Z}L_2\longrightarrow\mathbb Q,
 \qquad x\otimes y\longmapsto xy.
 \tag{2.1}
\]

### Lemma 2.1

The image of \(\mu\) is the product group \(L_1L_2\), and \(\mu\) is an
isomorphism

\[
 L_1\otimes_{\mathbb Z}L_2\simeq L_1L_2.
 \tag{2.2}
\]

### Proof

Surjectivity onto the product group is its definition.  Both groups have
rational rank one.  Since every torsion-free \(\mathbb Z\)-module is flat,
\(L_1\otimes L_2\) is torsion-free.  The kernel of the nonzero map \(\mu\)
has rational rank zero and is therefore torsion.  It is consequently zero.
\(\square\)

In particular there is no hidden derived term:

\[
 \operatorname{Tor}^{\mathbb Z}_1(L_1,L_2)=0.
 \tag{2.3}
\]

## 3. Exact archimedean projective norm

Write \(\|x\|_i=\lambda_i|x|\), with \(\lambda_i\geq0\).  On the
one-dimensional real tensor product, the projective seminorm is

\[
 \|z\|_\pi=
 \inf_{z=\sum_r x_r y_r}\sum_r\|x_r\|_1\|y_r\|_2
 =\lambda_1\lambda_2|z|.
 \tag{3.1}
\]

Indeed, the triangle inequality gives the lower bound.  Lemma 2.1 gives a
pure factorization for every element of the product group and hence the
reverse bound.  For a finite section \(\phi=(z_s)_s\), projectivizing the
published mass functional therefore gives exactly

\[
 \|\phi\|_{\pi,1}
 =\sum_s\|z_s\|_\pi
 =\lambda_1\lambda_2\sum_s|z_s|.
 \tag{3.2}
\]

Thus the unit ball obtained by projective tensor is precisely the unit ball
used by Connes--Consani for the product arithmetic divisor.  This is the
rank-one instance of
\(\ell^1(I)\widehat\otimes_\pi\ell^1(J)=\ell^1(I\times J)\); no trace norm
enters.

## 4. Strong monoidality and the square

### Theorem 4.1

For arithmetic divisors \(\mathcal D_1,\mathcal D_2\), multiplication of
values induces a canonical isomorphism of projectively completed modules

\[
 \boxed{
 \mathcal O(\mathcal D_1)\widehat\otimes_{\mathcal O,\pi}
 \mathcal O(\mathcal D_2)
 \;\simeq\;
 \mathcal O(\mathcal D_1\mathcal D_2).}
 \tag{4.1}
\]

At finite primes this follows from Lemma 2.1 and flatness.  At infinity it
follows from (3.2).  Restrictions are inclusions of regular elements and
commute with multiplication, so the local isomorphisms glue.  The unit and
associativity constraints are inherited from multiplication in \(\mathbb Q\)
and multiplication of the seminorm constants.

Let \(\mathscr C=\overline{\operatorname{Spec}\mathbb Z}\) with the published
absolute structure sheaf, and let \(\mathscr C^2\) be its product topos.  Put

\[
 \mathcal O_{\mathscr C^2}:=
 \operatorname{pr}_1^{-1}\mathcal O_{\mathscr C}
 \widehat\otimes_\pi
 \operatorname{pr}_2^{-1}\mathcal O_{\mathscr C}.
 \tag{4.2}
\]

The external module

\[
 \mathcal O(\mathcal D_1)\boxtimes\mathcal O(\mathcal D_2)
 :=\operatorname{pr}_1^*\mathcal O(\mathcal D_1)
 \widehat\otimes_{\mathcal O_{\mathscr C^2},\pi}
 \operatorname{pr}_2^*\mathcal O(\mathcal D_2),
 \tag{4.3}
\]

where
\(\operatorname{pr}_i^*M=\mathcal O_{\mathscr C^2}
\widehat\otimes_{\operatorname{pr}_i^{-1}\mathcal O,\pi}
\operatorname{pr}_i^{-1}M\).

It is consequently canonical and independent of adelic representatives.  Here
each displayed tensor sheaf means the sheafification of the corresponding
projective tensor presheaf; (3.2) identifies its archimedean stalk rather than
assuming that identification.  This
is the global module carrier whose **base change** must be compared with the
local external \(H^0\) construction of 107_232--107_233.  The direct
unextended comparison is ruled out in 107_235.

The rooted refinement of arXiv:2602.15941 is also monoidal, so passing to the
square does not force the phase/Galois datum to be forgotten.  This removes
the cross-prime *carrier* obstruction; it does not prove that the tropical
periodic modules are the restrictions of (4.3).

## 5. What is now closed and what is not

The following work package is closed:

\[
 \boxed{\texttt{ARITHMETIC\_DIVISOR\_SHEAF\_TENSOR\_DESCENT: CLOSED}.}
\]

In particular, the continuous archimedean coefficient is retained in the
metric kernel rather than sent to a finite-rank \(c_1\), exactly as required
by 107_224--107_227.

This result does **not** prove any of the following:

- the comparison of (4.3) with Scaling-Site periodic \(H^0\);
- representability or properness of the product topos as an arithmetic
  surface;
- \(H^1\), Serre duality, or Riemann--Roch on the square;
- the diagonal intersection or the terminal Weil identity.

Therefore row (a) remains `partial`. Tensor descent itself is closed; 107_235
shows that the next map must first extend scalars to \(\mathbb R_{\max}\) (or
pass through analytic tropicalization) before comparison with the periodic
external modules computed in 107_233.

## 6. Machine certificate

Run

```bash
/home/trabajo/miniforge3/bin/python \
  107_234_arithmetic_divisor_sheaf_tensor_descent.py
```

The program reads the real 2026 source, checks the required published
statements, and tests exact valuation splitting and projective mass equality
on a fixed atlas of arithmetic divisors.  Every check contributes to the
binary verdict.
