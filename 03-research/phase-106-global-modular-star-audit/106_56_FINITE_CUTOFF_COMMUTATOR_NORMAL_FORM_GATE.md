# 106.56 — Finite-cutoff commutator normal form and the diagonal obstruction

## Purpose

The proposed final factorization was

\[
 L_{\varepsilon,N}^2-\frac12L_{\varepsilon,N}
 =\mathcal C_{\varepsilon,N}^*\mathcal C_{\varepsilon,N}
  +\mathcal J_{\varepsilon,N}
  +[L_{\varepsilon,N},Y_{\varepsilon,N}]
  +\mathcal R_{\varepsilon,N},                     \tag{1}
\]

with \(\mathcal J_{\varepsilon,N}\geq0\), followed by a trace against a
finite Riesz projection.  This note performs the finite-cutoff algebra
exactly.  It has three conclusions.

1.  The physical Doob operator has an exact square-plus-residual
    factorization, including the intermediate-position defect.
2.  An \(L\)-commutator can remove every off-cluster block of the residual,
    but it cannot alter its compression to a reducing spectral cluster.
3.  On a subthreshold cluster, the compressed residual of every
    positive-square version of (1) has strictly negative trace.

Thus a commutator is a valid bookkeeping device, but it cannot by itself
turn the remaining signed arithmetic statement into positivity.  The note
is an adversarial gate, not a closure of the cluster-current inequality.

## 1. Finite-cutoff setting

Fix \(\varepsilon>0\) and \(N<\infty\).  Work after the unitary
ground-state conjugation of 106.54 in \(L^2(\mathbb R,dx)\).  Write

\[
 H=H_{\varepsilon,N},\qquad
 T=M_\eta H M_\eta,\qquad
 \widetilde L=V-T,                                  \tag{2}
\]

where \(H=H^*\) is the symmetric finite convolution and \(V=V^*\) is the
multiplication operator by the total Doob rate.  The common cutoff measure
has finite mass.  Since \(K\) is bounded, \(h\geq1\), and \(\eta\) is
bounded, \(H,T,V,\widetilde L\) are bounded.  All identities below are
therefore bounded-operator identities; no domain interchange is involved.

Put

\[
 \mathcal D
 =M_\eta H(I-M_{\eta^2})HM_\eta
 =C_D^*C_D,
 \qquad
 C_D=M_{\sqrt{1-\eta^2}}HM_\eta.                   \tag{3}
\]

By 106.54,

\[
 T^2=M_\eta H^2M_\eta-\mathcal D.                  \tag{4}
\]

### Theorem 1 — Exact physical square and residual

At every common finite cutoff,

\[
\boxed{
\begin{aligned}
 \widetilde L^2-\frac12\widetilde L
  &=T^*T+B_T,\\
 B_T
  &=V^2-VT-TV-\frac12V+\frac12T,
\end{aligned}}                                      \tag{5}
\]

and, equivalently,

\[
\boxed{
\begin{aligned}
 \widetilde L^2-\frac12\widetilde L
  &=(HM_\eta)^*(HM_\eta)+B_H,\\
 B_H&=B_T-\mathcal D.
\end{aligned}}                                      \tag{6}
\]

#### Proof

Expanding \(\widetilde L=V-T\) gives

\[
 \widetilde L^2-\frac12\widetilde L
 =V^2-VT-TV+T^2-\frac12V+\frac12T,                 \tag{7}
\]

which is (5).  Moreover

\[
 (HM_\eta)^*(HM_\eta)=M_\eta H^2M_\eta=T^2+\mathcal D
\]

by (3)--(4), proving (6).  \(\square\)

Formula (6) fixes the sign of the intermediate-position correction: the
primitive convolution square overcounts the physical two-step walk, and
the exact residual contains \(-\mathcal D\), not \(+\mathcal D\).

There is also the cutoff-independent algebraic completion

\[
\boxed{
 \widetilde L^2-\frac12\widetilde L
 =\left(\widetilde L-\frac14I\right)^2-\frac1{16}I.} \tag{8}
\]

The negative scalar in (8) is the simplest form of the threshold
obstruction.

## 2. What a reducing trace does to a commutator

Let \(P\) be a finite-rank spectral projection of \(\widetilde L\), and
put \(Q=I-P\).  Thus

\[
 P\widetilde L=\widetilde LP.                       \tag{9}
\]

### Lemma 2 — Trace annihilation

For every bounded \(Y\),

\[
\boxed{
 \mathrm{Tr}\,\bigl(P[\widetilde L,Y]\bigr)=0.} \tag{10}
\]

#### Proof

Because \(P\) has finite rank, cyclicity is legitimate, and (9) gives

\[
\begin{aligned}
 \mathrm{Tr}(P\widetilde LY-PY\widetilde L)
 &=\mathrm{Tr}(\widetilde LPY-\widetilde LPY)=0.
\end{aligned}
\]

\(\square\)

Consequently, if an identity of the form

\[
 A=C^*C+J+[\widetilde L,Y]+R,
 \qquad
 A=\widetilde L^2-\frac12\widetilde L,\qquad J\geq0, \tag{11}
\]

holds, then

\[
\boxed{
 \mathrm{Tr}(PA)
 =\|CP\|_{\rm HS}^2+\mathrm{Tr}(PJ)
  +\mathrm{Tr}(PR).}                         \tag{12}
\]

In particular, the commutator may rearrange the integrand, but it supplies
no trace budget on a reducing cluster.

## 3. Exact off-cluster commutator normal form

The preceding observation has an operator-level converse: all the part
which a commutator *can* remove is exactly the off-cluster part.

Let \(S=C^*C+J\geq0\) be any bounded positive operator and set

\[
 B=A-S.                                              \tag{13}
\]

Assume that the cluster is spectrally isolated,

\[
 d=\mathrm{dist}\,\{\sigma(\widetilde L|_{P\mathcal H}),
                          \sigma(\widetilde L|_{Q\mathcal H})\}>0. \tag{14}
\]

### Theorem 3 — Sylvester commutator normal form

There is a bounded skew-adjoint, purely off-diagonal operator \(Y\) such
that

\[
\boxed{
 A=S+[\widetilde L,Y]+R,\qquad
 R=PBP+QBQ.}                                        \tag{15}
\]

The unique \(QP\) block \(Z=QYP\) is

\[
\boxed{
 Z=\iint\frac{1}{\lambda-\mu}\,
 dE_Q(\lambda)\,QBP\,dE_P(\mu),}                  \tag{16}
\]

and \(Y=Z-Z^*\).  Moreover

\[
 \|Z\|_{\rm HS}\leq d^{-1}\|QBP\|_{\rm HS}.       \tag{16a}
\]

#### Proof

The double operator integral in (16) is bounded because of (14), and it
solves the Sylvester equation

\[
 \widetilde L_QZ-Z\widetilde L_P=QBP.               \tag{17}
\]

With respect to \(P\mathcal H\oplus Q\mathcal H\), the operator
\(Y=Z-Z^*\) is skew-adjoint and has zero diagonal blocks.  Equation (17)
and its adjoint show that the \(QP\) and \(PQ\) blocks of
\([\widetilde L,Y]\) are respectively \(QBP\) and \(PBQ\).  Its
diagonal blocks vanish.  Hence

\[
 B=[\widetilde L,Y]+PBP+QBQ,
\]

which proves (15).  Since \(P\) has finite rank, \(QBP\) is
Hilbert--Schmidt.  The spectral representation (16) multiplies each
\((\lambda,\mu)\) matrix coefficient by
\((\lambda-\mu)^{-1}\), whose absolute value is at most \(d^{-1}\).
This proves (16a), and in particular \(Z\) is bounded.  \(\square\)

Thus even the optimally selected commutator leaves on the cluster

\[
\boxed{PRP=PAP-PSP.}                                \tag{18}
\]

This diagonal block cannot be altered by another \(\widetilde L\)-commutator.

Taking the physical square \(S=T^*T\) and the explicit operator \(B_T\)
from (5), define

\[
 Z_T=\iint\frac{1}{\lambda-\mu}\,
 dE_Q(\lambda)\,QB_TP\,dE_P(\mu),
 \qquad Y_T=Z_T-Z_T^*.                              \tag{18a}
\]

The requested finite-cutoff factorization is therefore the completely
explicit identity

\[
\boxed{
 \widetilde L^2-\frac12\widetilde L
 =T^*T+[\widetilde L,Y_T]
  +PB_TP+QB_TQ,}                                    \tag{18b}
\]

where

\[
 B_T=V^2-VT-TV-\frac12V+\frac12T.                  \tag{18c}
\]

Likewise, using the primitive square in (6) gives

\[
\boxed{
 \widetilde L^2-\frac12\widetilde L
 =(HM_\eta)^*(HM_\eta)+[\widetilde L,Y_H]
  +PB_HP+QB_HQ,}                                    \tag{18d}
\]

with \(B_H=B_T-\mathcal D\) and \(Y_H\) obtained from (18a) by replacing
\(B_T\) with \(B_H\).  Equations (18b)--(18d) contain no unspecified
operator.  Their only unsigned object is the diagonal residual.

## 4. The residual sign on a subthreshold cluster

Suppose now that

\[
 \sigma(\widetilde L|_{P\mathcal H})\subset(0,1/2),
 \qquad P\ne0.                                      \tag{19}
\]

If the eigenvalues in the cluster are \(\lambda_1,\ldots,\lambda_m\),
then

\[
 \mathrm{Tr}(PA)
 =\sum_{k=1}^m\lambda_k(\lambda_k-1/2)<0.           \tag{20}
\]

Combining (12) and (20) gives the exact obstruction.

### Corollary 4 — Every positive-square factorization pays a negative residual

Under (19), every identity (11) with \(J\geq0\) satisfies

\[
\boxed{
 \mathrm{Tr}(PR)
 =\sum_{k=1}^m\lambda_k(\lambda_k-1/2)
  -\|CP\|_{\rm HS}^2-\mathrm{Tr}(PJ)<0.}     \tag{21}
\]

In particular, no choice of \(Y\) can make \(PRP\geq0\).  For the exact
physical square in (5),

\[
 \mathrm{Tr}(PR_T)
 =\mathrm{Tr}(PA)-\|TP\|_{\rm HS}^2<0.      \tag{22}
\]

For the primitive square in (6), the residual is smaller still by the
nonnegative intermediate defect.

This does not prove that an ordinary-prime subthreshold cluster exists.
It proves that a positive residual cannot be obtained from algebraic
commutator bookkeeping alone: proving its positivity would already exclude
the cluster and is therefore the force-bearing arithmetic theorem.

## 5. Why coefficient positivity of \(j_2\) is not the missing square

At prime cutoff \(N\), put

\[
 B_N=\sum_{n\leq N}\frac{j_2(n)}{\sqrt n}S_{\log n},
 \qquad b_n=\frac{j_2(n)}{\sqrt n}\geq0.             \tag{23}
\]

As proved in 106.53,

\[
 B_N+B_N^*=2\kappa_N^{(2)}I-2G_N^{(2)},
 \qquad G_N^{(2)}\geq0.                             \tag{24}
\]

Therefore the centered \(j_2\) energy occurs with a negative sign.  Also,
coefficient positivity does not imply positivity of \(B_N+B_N^*\): for a
single displacement \(a>0\) and coefficient \(b>0\), its Fourier
multiplier is

\[
 2b\cos(a\xi),                                      \tag{25}
\]

which is negative at \(\xi=\pi/a\).

A proposed cell square does not repair this coefficientwise.  Indeed, for

\[
 \Delta_{a,b}=(S_a-I)(S_b-I),
\]

the multiplier of \(\Delta_{a,b}^*\Delta_{a,b}\) is

\[
 |e^{ia\xi}-1|^2|e^{ib\xi}-1|^2\geq0.              \tag{26}
\]

Expanding (26) introduces translations at
\(\pm a,\pm b,\pm(a+b),\pm(a-b)\).  Hence every such square contains the
product and ratio channels together with additional diagonal and
single-step terms.  It is not the pure operator with coefficient
\(\delta\Lambda+\Lambda*\Lambda\).  Any valid use of these cell squares
must prove the sign of the full remainder after those extra channels and
the Gamma--polar terms are retained.

## 6. Finite reversible falsifier

Let

\[
 P_1=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
 \qquad L_\lambda=\lambda P_1,
 \qquad0<\lambda<\frac12.                           \tag{27}
\]

Then \(L_\lambda\) is the generator of a reversible two-state positive
jump chain: its constant vector has eigenvalue zero and its antisymmetric
vector has eigenvalue \(\lambda\).  Taking \(P=P_1\),

\[
\boxed{
 \mathrm{Tr}\,P
 \left(L_\lambda^2-\frac12L_\lambda\right)
 =\lambda(\lambda-1/2)<0.}                          \tag{28}
\]

For \(\lambda=1/4\), the value is \(-1/16\).  Thus positive jump weights,
reversibility, commuting moves, and finite-rate Bochner squares do not
imply the desired cluster sign.  A proof which uses only those abstract
properties is falsified by (27).  The literal ordinary-prime--Gamma
identity must use additional arithmetic information which fails in this
model.

## 7. Surviving theorem

The common-cutoff algebra is now complete.  The strongest possible
commutator reduction is (15), and its surviving diagonal assertion is

\[
\boxed{
 P\left(\widetilde L_{\varepsilon,N}^2
 -\frac12\widetilde L_{\varepsilon,N}
 -C^*C-J\right)P\geq0}                              \tag{29}
\]

for a specifically constructed physical \(C\) and \(J\geq0\), uniformly
through the joint cutoff limit.  By (18)--(21), this is not supplied by the
commutator; it is at least as strong as the cluster-current inequality
itself.  Equivalently, without prematurely selecting \(C\) and \(J\), the
remaining literal-prime statement is still

\[
\boxed{
 \mathrm{Tr}\,P
 \left(L^2-\frac12L\right)\geq0}                    \tag{30}
\]

for every finite Riesz projection of the complete generator.  Any next
attack must establish the diagonal sign in (30) from the common-cutoff
three-point formula.  Moving signed components into an
\(L\)-commutator cannot change that sign.

## 8. Finite-matrix verification

The normal form (15) was checked on random complex matrices of dimensions
\(3\) through \(12\).  In each test, \(\widetilde L\) was diagonal with a
two-dimensional cluster in \((0,1/2)\), the complementary spectrum was
placed above \(0.7\), and \(S=C^*C+J\) used independent random complex
matrices with \(J\geq0\).  Formula (16) was evaluated entrywise.  Over 500
tests, the largest operator-identity or commutator-trace discrepancy was
\(1.31\times10^{-14}\).  The two-state value (28) was also checked at
\(\lambda=0.1,0.25,0.49\), giving respectively
\(-0.04,-0.0625,-0.0049\).
