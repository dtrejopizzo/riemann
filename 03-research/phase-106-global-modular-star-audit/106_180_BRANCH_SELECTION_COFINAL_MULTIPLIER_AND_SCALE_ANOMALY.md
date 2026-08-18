# 106.180 — Branch selection, the cofinal return multiplier, and the scale anomaly

## 1. Purpose

The Dirichlet normalization of 106.179 fixes the local metric, but three
cofinal questions must be separated before attempting nuclear descent:

1. whether the return average is always a contraction;
2. which invariant Julia graph is selected by the arithmetic Green form;
3. whether scale covariance alone fixes the finite-part normalization.

All three questions admit exact answers.  The contraction is
unconditional.  The negative Julia graph is the unique branch carrying
the inverse of the physical Green defect, and after the normalization of
106.179 it carries the Green defect itself.  The normalized return
operator has no ordinary cofinal limit at nonzero Mellin frequency.
Finally, cancellation of scale anomalies does not by itself remove an
additive scalar ambiguity, because the scalar metric has the same
weight-one covariance.  The canonical scalar is instead fixed by the
joined CCM Gamma--polar trace formula.

## 2. Contraction and unweighted branch pullbacks

Let

\[
 C=\sum_iw_i,qquad A=\sum_iw_iU_i,qquad T=C^{-1}A,
\tag{1}
\]

where \(w_i>0\), each \(U_i\) is unitary, and the family is symmetric
under adjoint with equal weights.  Then \(A=A^*\) and

\[
 \boxed{\|T\|\le C^{-1}\sum_iw_i\|U_i\|=1.}
\tag{2}
\]

Thus \(D=(I-T^2)^{1/2}\) and the Julia involution of 106.178 exist for
every finite return family; no spectral hypothesis is needed.

For the unweighted Krein form

\[
 \mathfrak k(v,w)=-C\langle Sv,w\rangle,
\tag{3}
\]

the invariant graph maps \(\iota_\pm f=(f,K_\pm f)\) satisfy

\[
 S\iota_\pm=\pm\iota_\pm.
\tag{4}
\]

Using 106.179(9) gives the exact pullbacks

\[
 \boxed{
 \begin{aligned}
 \iota_+^*\mathfrak k\,\iota_+
   &=-2C(I+T)^{-1}
    =-2C^2(CI+A)^{-1},\\
 \iota_-^*\mathfrak k\,\iota_-
   &=+2C(I-T)^{-1}
    =+2C^2(CI-A)^{-1}.
 \end{aligned}}
\tag{5}
\]

The signs and denominators select the branch without convention:
\(K_-\) is positive for the Krein form and contains the inverse of the
physical Green operator \(CI-A\); \(K_+\) is negative and contains
\(CI+A\).  The Dirichlet weight of 106.179 transforms the second line of
(5) from the inverse defect into \(CI-A\) itself.

## 3. The negative endpoint is separated at every finite cutoff

Assume the symmetric return family contains \(U,U^*\) and
\(U^2,U^{*2}\), with individual oriented weights \(w_1,w_2>0\).

### Theorem 3.1 — Explicit lower bound at \(-1\)

For every unit vector \(f\),

\[
 \boxed{
 \langle(I+T)f,f\rangle
 \ge {4\over
 C\bigl(w_2^{-1/2}+2w_1^{-1/2}\bigr)^2}.}
\tag{6}
\]

Consequently \(-1\notin\sigma(T)\) at every finite cutoff.

#### Proof

Put \(\delta=\langle(I+T)f,f\rangle\).  Every symmetric return pair
contributes a nonnegative quantity to \(C\delta\).  Retaining only the
two stated pairs gives

\[
 w_1\|(U+I)f\|^2\le C\delta,
 \qquad
 w_2\|(U^2+I)f\|^2\le C\delta.
\tag{7}
\]

The identity

\[
 (U^2-I)f=U(U+I)f-(U+I)f
\tag{8}
\]

implies \(\|(U^2-I)f\|\le2\|(U+I)f\|\).  Hence

\[
 \begin{aligned}
 2
 &=\|2f\|\\
 &\le\|(U^2+I)f\|+\|(U^2-I)f\|\\
 &\le\sqrt{C\delta}\left(w_2^{-1/2}+2w_1^{-1/2}\right).
 \end{aligned}
\tag{9}
\]

Squaring proves (6). \(\square\)

For the ordinary return bank one may take \(U=U_2\),

\[
 w_1=(\log2)2^{-1/2},\qquad w_2=(\log2)2^{-1}.
\tag{10}
\]

The lower bound is of order \(C^{-1}\), so it does not give a uniform
cofinal gap.  By contrast, on the translation representation the point
\(+1\) belongs to the spectrum through Følner approximate invariants.
Thus the arithmetically selected branch \(K_-\) is precisely the branch
singular at the generic unitary endpoint.

## 4. The normalized return operator does not converge naively

Let the ordinary-prime bank include all oriented powers with
\(p^k\le X\).  On a Mellin character of frequency \(\tau\), the return
average is scalar.  Prime powers with \(k\ge2\) are lower order in the
normalization, while the prime number theorem and partial summation give

\[
 C_X=4\sqrt X+o(\sqrt X)
\tag{11}
\]

and, for fixed real \(\tau\),

\[
 \boxed{
 T_X(\tau)
 =\operatorname {Re}
   {e^{i\tau\log X}\over1+2i\tau}+o(1).}
\tag{12}
\]

At \(\tau=0\), (12) equals \(1+o(1)\).  At every fixed
\(\tau\ne0\), it oscillates with nonzero amplitude
\((1+4\tau^2)^{-1/2}\) and has no limit as \(X\to\infty\).

#### Derivation

The first return layer gives

\[
 2\sum_{p\le X}{\log p\over\sqrt p}
 \cos(\tau\log p)
 =2\operatorname {Re}
  {X^{1/2+i\tau}\over1/2+i\tau}+o(\sqrt X),
\tag{13}
\]

while its value at \(\tau=0\) is \(4\sqrt X+o(\sqrt X)\).
The higher powers are \(o(\sqrt X)\).  Division gives (12).

Therefore neither \(T_X\to0\) nor \(T_X\to I\) describes the cofinal
operator.  The return star must be used before taking the cutoff limit,
and the remaining limit must be formulated in the nuclear/finite-part
category.

## 5. Scale anomaly and the scalar ambiguity

Suppose a weight-one Hermitian form \(h\) obeys

\[
 h(\vartheta_tu,\vartheta_tv)=e^t h(u,v).
\tag{14}
\]

Let \(m\) be the scalar degree-one metric on the same module.  It has the
same law

\[
 m(\vartheta_tu,\vartheta_tv)=e^t m(u,v).
\tag{15}
\]

### Proposition 5.1 — Covariance cannot select an additive scalar

For every real \(c\),

\[
 h_c=h+c,m
\tag{16}
\]

also satisfies (14).  Equivalently, after normalized scaling
\(U_t=e^{-t/2}\vartheta_t\), both \(h\) and \(m\) are invariant, and so
is every \(h_c\).

#### Proof

Substitute (14)--(15) into (16). \(\square\)

Hence cancellation of the opposite divergent scale anomalies is a
necessary compatibility check, but scale covariance alone cannot fix the
finite scalar shift.  In the present construction the scalar is not left
free: the CCM principal-value distribution, the Gamma factor, and the
two polar terms define the joined global form before the local split.
The local decomposition must reproduce that fixed distribution.  It may
not choose a finite part independently in either sector.

## 6. Exact next comparison

Documents 106.176 and 106.179 reduce the metric comparison to

\[
 \mathfrak h_I
 =g_{D,I}|_{\operatorname {graph}K_-}
  +\mathcal B_I,
\qquad
 \mathcal B_I=\mathcal P_I-C_I\langle\cdot,\cdot\rangle.
\tag{17}
\]

The branch, the local metric, and the finite-cutoff contraction are now
fixed.  The remaining operation is not selection of a renormalization
constant.  It is the chain-level identity asserting that the joined
finite part of (17):

1. vanishes on the CCM restriction range;
2. is preserved by the Fourier-odd graph under normalized scaling;
3. equals the nonreduced CCM Rosati residue form.

That identity must be proved before Hilbert completion, because (12)
precludes an ordinary cofinal operator limit and (20) of 106.179 retains
the endpoint only through the singular graph/vanishing-weight product.

## 7. Status

Proved without RH or zero input:

* unconditional contractivity of every finite return average;
* exact unweighted pullbacks and intrinsic selection of \(K_-\);
* an explicit finite-cutoff gap at the negative endpoint;
* singularity of the selected branch at the positive generic endpoint;
* the PNT asymptotic multiplier showing absence of a naive cofinal
  operator limit;
* impossibility of fixing a scalar finite part by scale covariance alone.

Still required:

* the joined Gamma--polar boundary identity on the nonreduced CCM cone;
* torsion-sensitive descent of the Dirichlet-normalized negative graph;
* equality with the CCM Rosati residue pairing.

