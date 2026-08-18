# 106.172 — Exact primitive finite part and the Gamma boundary map

## 1. Purpose

Document 106.161 constructed the common first-mode boundary operator

\[
 (B_sF)_p=\sqrt{\log p}\,p^{-s}zF,\qquad s>\frac12,          \tag{1}
\]

and reduced its unfinished gluing to

\[
 \mathrm{FP}_{s\downarrow1/2}\|B_sF\|^2
 +\|B_\infty F\|^2=0.                                       \tag{2}
\]

This note computes the finite part exactly and constructs \(B_\infty\).
The counterspace is not invented: its two components are the Euler
constant from the Gamma page and the repeated-winding determinant of
106.167. The pole at \(s=1\) removes the sole divergent scalar.

The result closes (2) on the common Hardy coefficient sector of 106.161.
It does not extend that separable sector to the full CCM test space.

## 2. Primitive and repeated prime traces

For \(\Re w>1\), put

\[
 P(w)=\sum_p p^{-w},\qquad
 H(w)=\sum_p\sum_{k\ge2}\frac{p^{-kw}}k.                     \tag{3}
\]

Then

\[
 \log\zeta(w)=P(w)+H(w),                                    \tag{4}
\]

and \(H\) is holomorphic for \(\Re w>1/2\). Differentiation gives

\[
 -P'(w)
 =-\frac{\zeta'(w)}{\zeta(w)}+H'(w).                         \tag{5}
\]

The norm in (1) is

\[
 \|B_sF\|^2=C_s\|F\|^2,\qquad
 C_s=\sum_p(\log p)p^{-2s}=-P'(2s).                          \tag{6}
\]

Near \(w=1\),

\[
 -\frac{\zeta'(w)}{\zeta(w)}
 =\frac1{w-1}-\gamma+O(w-1),                                \tag{7}
\]

where \(\gamma\) is Euler's constant. Moreover,

\[
 H'(1)
 =-\sum_p\sum_{k\ge2}\frac{\log p}{p^k}
 =-\sum_p\frac{\log p}{p(p-1)}.                              \tag{8}
\]

The series in (8) converges absolutely.

### Theorem 2.1 — Exact primitive finite part

\[
 \boxed{
 \mathrm{FP}_{s\downarrow1/2}C_s
 =-\kappa_\infty,}                                          \tag{9}
\]

where

\[
 \boxed{
 \kappa_\infty
 =\gamma-H'(1)
 =\gamma+\sum_p\sum_{k\ge2}\frac{\log p}{p^k}
 =\gamma+\sum_p\frac{\log p}{p(p-1)}>0.}                    \tag{10}
\]

Here finite part means subtraction of \(1/(2s-1)\).

#### Proof

Insert \(w=2s\) in (5) and use (7):

\[
 C_s
 =\frac1{2s-1}-\gamma+H'(1)+O(2s-1).
\]

This proves (9)--(10). Absolute convergence follows by comparison with
\(\sum_{n\ge2}(\log n)/n^2\). Euler's constant is positive, and every
summand in the last expression of (10) is positive. \(\square\)

The divergence, Gamma constant, and repeated prime powers are therefore
not three adjustable regularizations. They are the three terms of the
single differentiated Euler identity (5).

## 3. A source-defined positive counterspace

Let

\[
 \mathscr H_{\rm rw}
 =\ell^2\{(p,k):p\ {\rm prime},\ k\ge2\}                     \tag{11}
\]

and let \((e_{p,k})\) be its standard basis. Add one real Gamma line
\(\mathbb Re_\gamma\), and put

\[
 \mathscr H_\infty
 =\mathbb Re_\gamma\oplus\mathscr H_{\rm rw}.                \tag{12}
\]

Define

\[
 v_\infty
 =\sqrt\gamma\,e_\gamma
  \oplus
  \sum_{p}\sum_{k\ge2}
  \sqrt{\log p}\,p^{-k/2}e_{p,k}.                            \tag{13}
\]

Equation (10) gives

\[
 \boxed{\|v_\infty\|^2=\kappa_\infty.}                       \tag{14}
\]

The first component of (13) is the finite logarithmic derivative of the
Gamma normalization at its unit argument. The remaining components are
the derivative of the nonvanishing Hilbert--Schmidt determinant
\(\det_2(I-D_w)=e^{-H(w)}\) at \(w=1\). Thus (13) is assembled from the
already constructed Gamma and repeated-winding pages.

## 4. Construction of \(B_\infty\)

Let \(\mathcal H_{\rm bd}=H^2(\mathbb D)\) be the common Hardy boundary
module of 106.161. Define

\[
 \boxed{
 B_\infty:\mathcal H_{\rm bd}
 \longrightarrow
 \mathscr H_\infty\widehat\otimes\mathcal H_{\rm bd},
 \qquad
 B_\infty F=v_\infty\otimes F.}                              \tag{15}
\]

This is bounded, injective, and

\[
 B_\infty^*B_\infty=\kappa_\infty I.                         \tag{16}
\]

### Theorem 4.1 — Exact primitive--Gamma cancellation

For every \(F\in H^2(\mathbb D)\),

\[
 \boxed{
 \mathrm{FP}_{s\downarrow1/2}\|B_sF\|^2
 +\|B_\infty F\|^2=0.}                                      \tag{17}
\]

#### Proof

Equations (6) and (9) give

\[
 \mathrm{FP}_{s\downarrow1/2}\|B_sF\|^2
 =-\kappa_\infty\|F\|^2.
\]

Equations (14)--(15) give
\(\|B_\infty F\|^2=\kappa_\infty\|F\|^2\). Their sum is zero.
\(\square\)

This proves the scalar finite-part identity requested in (24) of 106.161.
The counterterm is a positive norm; the negative sign is entirely the
finite part of the divergent primitive plane.  Identifying this scalar
isometry with the complete Gamma/polar chain map remains a separate
compatibility statement.

## 5. Uniqueness of the normalization

Suppose \(\widetilde B_\infty\) is any bounded map on
\(\mathcal H_{\rm bd}\) satisfying (17) for every \(F\). Then

\[
 \widetilde B_\infty^*\widetilde B_\infty
 =\kappa_\infty I.                                          \tag{18}
\]

Thus every solution differs from (15), after quotienting its kernel, by
an isometric embedding of the same scalar boundary module. The norm is
forced by the Euler identity; only a unitary choice of target realization
remains. Formula (13) fixes that choice using the actual Gamma and
repeated-winding pages.

## 6. Relation with the Tate middle plane

For a finite prime set \(S\), the generic Hodge plane of 106.169 has norm

\[
 C_S=\sum_{p\in S}\frac{\log p}{p}.                          \tag{19}
\]

Abel regularization replaces it by

\[
 C_s=\sum_p(\log p)p^{-2s}.                                 \tag{20}
\]

The pole part \(1/(2s-1)\) is the generic-orbit volume. The finite
remainder is \(-\kappa_\infty\), and (15) supplies its Hodge partner.
Therefore the generic plane, repeated winding determinant, Gamma constant,
and polar subtraction form one normalized boundary package.

This is the coefficient-level scalar content of the right-hand side of
the chain comparison (36) in 106.169.  It is not yet the full
archimedean chain map: the latter must also intertwine the differential,
real structure, and Gamma spin grading.

## 7. Scope of the theorem

The map (15) acts on one common Hardy function \(F\). As proved in
Section 9 of 106.161, a general CCM test has independent values
\(f(k\log p)\) and need not lie in this separable diagonal sector.
Therefore Theorem 4.1 closes the exact equation that was posed there but
does not prove the full nuclear localization theorem.

The remaining extension problem is now precise: replace
\(H^2(\mathbb D)\) by the actual nuclear generic-length module and prove
that the finite-part identity (17) holds as an operator-valued identity
on the full adelic summation cone, not only on the common diagonal.

## 8. Status

Proved without RH or zero input:

* the exact Laurent expansion of the primitive boundary norm;
* its canonical positive decomposition into Gamma and repeated windings;
* an explicit bounded, injective \(B_\infty\);
* the exact finite-part identity left open in 106.161;
* uniqueness of its scalar normalization.

Still required:

* extension from the common Hardy sector to the full nuclear
  generic-length module;
* compatibility of that extension with the complete CCM differential;
* the degree-one quasi-isomorphism and Rosati metric identity.

## 9. Numerical audit

The companion script `106_172_primitive_gamma_verify.py` checks the two
independent expressions

\[
 \sum_p\sum_{k\ge2}{\log p\over p^k}
 \quad\hbox{and}\quad
 \sum_p{\log p\over p(p-1)}
\]

at a finite prime cutoff, and verifies positivity of the resulting
partial value of \(\kappa_\infty\).  This is only an arithmetic audit;
Theorem 2.1 is the exact proof.
