# Vanishing kernel pairing no-go

## Purpose

`168_RENORMALIZED_VANISHING_TEST_KERNEL_TARGET.md` asks for a positive
Euler--Gamma form on
\[
  \mathcal V=(z-1)\mathbb C[z]
\]
with
\[
  \mathfrak Q(1-z^n,1-z^n)=2\lambda_n.
\]

`169_LI_SCHOENBERG_VANISHING_KERNEL.md` gives the algebraic kernel that
would result on the critical line:
\[
  K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}.
\]

This note records the local obstruction to constructing that form by the
obvious functional-equation pairing.  The obstruction is exact: the pairing
that recovers Li is locally indefinite away from the unit circle.

## Functional-equation involution in the Li disk

Put
\[
  w_\rho=1-{1\over\rho}.
\]

The functional equation pairs a zero \(\rho\) with
\[
  \rho^\ast=1-\overline{\rho}.
\]
In the \(w\)-coordinate this becomes
\[
\begin{aligned}
  w_{\rho^\ast}
  &=1-{1\over 1-\overline{\rho}}       \\
  &={\overline{\rho}\over\overline{\rho}-1}
   ={1\over\overline{w_\rho}}.
\end{aligned}
\tag{1}
\]

Thus the natural involution is
\[
  \sigma(w)={1\over\overline w}.
\tag{2}
\]

Its fixed points are exactly
\[
  \sigma(w)=w
  \quad\Longleftrightarrow\quad
  |w|=1.
\tag{3}
\]

Therefore critical-line support is exactly fixed-point support for the
functional-equation involution in the Li disk.

## The positive square and the Li pairing are different

For \(p\in\mathcal V\), the manifestly positive local square on the orbit
\(\{w,\sigma(w)\}\) is
\[
  |p(w)|^2+|p(\sigma(w))|^2.
\tag{4}
\]

For the Li tests
\[
  e_n(z)=1-z^n,
\]
this gives
\[
  |1-w^n|^2+\left|1-\sigma(w)^n\right|^2.
\tag{5}
\]

This is not the Li contribution unless \(|w|=1\).  The Li pairing uses
the functional-equation partner, not the ordinary Hilbert conjugate:
\[
  (1-w^n)(1-w^{-n})
\tag{6}
\]
and its conjugate counterpart.  Since
\[
  \overline{e_n(\sigma(w))}
  =
  \overline{1-\overline w^{-n}}
  =
  1-w^{-n},
\tag{7}
\]
the local Li pairing is
\[
  q_w(p)
  =
  2\operatorname{Re}\left(p(w)\overline{p(\sigma(w))}\right).
\tag{8}
\]

For \(p=e_n\), this gives
\[
  q_w(e_n)
  =
  2\operatorname{Re}\left((1-w^n)(1-w^{-n})\right),
\tag{9}
\]
which is exactly the quartet contribution to the paired Li sum.

Thus the exact Li normalization is produced by the cross-pairing (8), not
by the positive square (4), unless the orbit lies on the unit circle.

## Local indefiniteness theorem

Assume \(w\ne\sigma(w)\) and \(w,\sigma(w)\ne1\).  The evaluation map
\[
  \mathcal V\longrightarrow\mathbb C^2,
  \qquad
  p\longmapsto (p(w),p(\sigma(w)))
\tag{10}
\]
is onto.

Indeed, write \(p(z)=(z-1)r(z)\).  Given \(x,y\in\mathbb C\), choose a
linear polynomial \(r\) with
\[
  r(w)={x\over w-1},
  \qquad
  r(\sigma(w))={y\over \sigma(w)-1}.
\tag{11}
\]

On the value pair \((x,y)\), the Li cross-pairing (8) is
\[
  q_w(x,y)=2\operatorname{Re}(x\overline y).
\tag{12}
\]

Its Hermitian matrix is
\[
  \begin{pmatrix}
    0&1\\
    1&0
  \end{pmatrix},
\tag{13}
\]
with eigenvalues \(1\) and \(-1\).  Taking \(x=1\), \(y=-1\) gives
\[
  q_w(1,-1)=-2.
\tag{14}
\]

Therefore the functional-equation pairing that recovers the Li square is
not positive on \(\mathcal V\) in the presence of a non-fixed orbit
\(\{w,\sigma(w)\}\).

## Consequence for the vanishing-kernel route

A positive Hilbert form with exact Li diagonal cannot be obtained by the
formal replacement
\[
  \overline{w}\quad\hbox{by}\quad \sigma(w)={1\over\overline w}
\]
inside a square.  That replacement is precisely the step that changes a
positive square into the Li cross-pairing, and it is indefinite off the
unit circle.

Consequently, any successful Euler--Gamma construction must do one of the
following.

1. Prove fixed-point support
   \[
     w=\sigma(w)
   \]
   before using the positive square.  This is exactly critical-line support.

2. Add new Euler--Gamma counterterms or diagonal terms that alter the local
   two-point matrix while preserving the global Li values
   \[
     \mathfrak Q(1-z^n,1-z^n)=2\lambda_n.
   \]
   Those extra terms must be constructed independently and shown to have the
   required cancellations.

3. Prove the Schoenberg kernel positivity
   \[
     \left[\lambda_j+\lambda_k-\lambda_{|j-k|}\right]_{1\le j,k\le N}\ge0
   \]
   directly from Euler--Gamma data, without representing it as the local
   functional-equation cross-pairing at off-circle orbits.

## Exact no-go statement

Let a candidate vanishing-test form be assembled orbit by orbit from the
zero divisor, and suppose that on every two-point functional-equation orbit
\(\{w,\sigma(w)\}\) its principal local residue is the Li cross-pairing
\[
  2\operatorname{Re}\left(p(w)\overline{p(\sigma(w))}\right).
\]

If the form is positive semidefinite on all of \(\mathcal V\), then no
non-fixed orbit can occur.  Equivalently, every transformed zero in the
support of that principal pairing must satisfy
\[
  |w|=1.
\]

Thus this construction either proves critical-line support by an independent
argument, or it is circular.

## Status

Closed as a no-go for the direct functional-equation cross-pairing.
A1 remains open.

The surviving vanishing-kernel target is now sharper: build a genuinely
positive Euler--Gamma form on \((z-1)\mathbb C[z]\) with Li-square diagonal,
or prove the Schoenberg kernel positivity of `169_LI_SCHOENBERG_VANISHING_KERNEL.md`
from arithmetic data without the off-circle cross-pairing.
