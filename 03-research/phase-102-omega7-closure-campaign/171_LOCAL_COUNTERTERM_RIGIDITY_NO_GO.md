# Local counterterm rigidity no-go

## Purpose

`170_VANISHING_KERNEL_PAIRING_NO_GO.md` shows that the local
functional-equation cross-pairing is indefinite on a non-fixed orbit
\[
  \{w,\sigma(w)\},\qquad \sigma(w)={1\over\overline w}.
\]

This note rules out the most tempting repair: adding a positive local or
global counterterm that preserves the Li-square values on every test
\[
  e_n(z)=1-z^n.
\]

The obstruction is finite-dimensional and exact.  On a non-fixed orbit, the
first two Li tests already span all local evaluation directions.
Globally, the whole family \(\{e_n:n\ge1\}\) spans
\((z-1)\mathbb C[z]\), so any positive counterterm invisible on every Li
diagonal is identically zero.

## Local value space

Fix
\[
  w\ne\sigma(w),\qquad w\ne1,\qquad \sigma(w)\ne1.
\]

For \(p\in(z-1)\mathbb C[z]\), write its local value vector as
\[
  E_w(p)=(p(w),p(\sigma(w)))\in\mathbb C^2.
\]

The Li test values are
\[
  v_n=E_w(e_n)=\left(1-w^n,\ 1-\sigma(w)^n\right).
\tag{1}
\]

For \(n=1,2\),
\[
  v_1=(1-w,\ 1-\sigma),
\]
and
\[
  v_2=(1-w^2,\ 1-\sigma^2)
      =((1-w)(1+w),\ (1-\sigma)(1+\sigma)).
\]

Their determinant is
\[
\begin{aligned}
  \det(v_1,v_2)
  &=
  (1-w)(1-\sigma^2)-(1-w^2)(1-\sigma)\\
  &=
  (1-w)(1-\sigma)\bigl[(1+\sigma)-(1+w)\bigr]\\
  &=
  (1-w)(1-\sigma)(\sigma-w).
\end{aligned}
\tag{2}
\]

By the assumptions, this is nonzero.  Hence
\[
  \operatorname{span}\{v_1,v_2\}=\mathbb C^2.
\tag{3}
\]

## Positive counterterm rigidity

Let \(B\) be a positive semidefinite Hermitian form on the local value space
\(\mathbb C^2\).  Suppose \(B\) is a local counterterm that does not change
any Li-square value:
\[
  B(v_n,v_n)=0
  \qquad(n\ge1).
\tag{4}
\]

Since \(B\ge0\), the Cauchy--Schwarz inequality for semidefinite forms gives
\[
  B(x,x)=0
  \quad\Longrightarrow\quad
  B(x,y)=0\quad\hbox{for every }y.
\tag{5}
\]

In particular, (4) for \(n=1,2\) implies that \(B\) vanishes on both
spanning vectors \(v_1,v_2\).  By (3),
\[
  B\equiv0
  \quad\hbox{on }\mathbb C^2.
\tag{6}
\]

Thus there is no nonzero positive local counterterm that preserves all
Li-square values on a non-fixed orbit.

## Diagonal repair corollary

The preceding rigidity contains the diagonal repair as a special case, but
it is useful to write it explicitly.

Add to the cross-pairing the diagonal form
\[
  d_{a,b}(x,y)=a|x|^2+b|y|^2,
  \qquad a,b\in\mathbb R.
\tag{7}
\]
The repaired local matrix is
\[
  M_{a,b}=
  \begin{pmatrix}
    a&1\\
    1&b
  \end{pmatrix}.
\tag{8}
\]
It is positive semidefinite if and only if
\[
  a\ge0,\qquad b\ge0,\qquad ab\ge1.
\tag{9}
\]

On the first Li test \(e_1(z)=1-z\), the added diagonal value is
\[
  d_{a,b}(v_1)
  =
  a|1-w|^2+b|1-\sigma(w)|^2.
\tag{10}
\]
Since \(w,\sigma(w)\ne1\), exact preservation of the Li value for \(e_1\)
forces \(a=b=0\).  This contradicts \(ab\ge1\).

Hence no diagonal local Euler--Gamma patch can simultaneously make the
off-circle two-point matrix positive and preserve the Li-square
normalization.

## Global positive-counterterm rigidity

The same rigidity does not depend on orbitwise localization.

Let
\[
  \mathcal V=(z-1)\mathbb C[z],
\]
and let \(D\) be any positive semidefinite Hermitian form on \(\mathcal V\).
Assume \(D\) is a global counterterm added after the Li normalization has
already been fixed, so it must preserve every Li square value:
\[
  D(e_n,e_n)=0
  \qquad(n\ge1).
\tag{11}
\]

For a positive semidefinite form, Cauchy--Schwarz gives
\[
  |D(e_j,e_k)|^2
  \le
  D(e_j,e_j)D(e_k,e_k)=0.
\tag{12}
\]
Hence
\[
  D(e_j,e_k)=0
  \qquad(j,k\ge1).
\tag{13}
\]

The Li tests span \(\mathcal V\).  Indeed, if
\[
  p(z)=\sum_{j=0}^{N}c_jz^j,\qquad p(1)=0,
\]
then \(c_0=-\sum_{j=1}^{N}c_j\), and therefore
\[
  p(z)=\sum_{j=1}^{N}c_j(z^j-1)
       =-\sum_{j=1}^{N}c_j e_j(z).
\tag{14}
\]
Equations (13)--(14) imply
\[
  D\equiv0\quad\hbox{on }\mathcal V.
\tag{15}
\]

Thus no nontrivial positive counterterm, local or nonlocal, can be added to
an already Li-normalized form while leaving all values
\[
  Q(1-z^n,1-z^n)=2\lambda_n
\]
unchanged.

## Consequence for the cross-pairing

The local Li cross-pairing from `170` is
\[
  q_w(x,y)=2\operatorname{Re}(x\overline y),
\tag{16}
\]
with Hermitian matrix
\[
  \begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{17}
\]

It has a negative direction.  If one tries to repair it by
\[
  q_w+B,
\tag{18}
\]
where \(B\ge0\) and \(B(v_n,v_n)=0\) for all Li tests, then \(B=0\) by
(6).  Therefore \(q_w+B=q_w\) remains indefinite.

This proves:

**Local rigidity theorem.**  On a non-fixed functional-equation orbit, no
positive semidefinite local counterterm can both:

1. leave every local Li value \(q_w(v_n)\) unchanged;
2. turn the local cross-pairing into a positive semidefinite form.

## What remains possible

The theorem does not rule out every conceivable Euler--Gamma construction.
It rules out positive counterterms added after the cross-pairing has already
been normalized to the Li diagonal.

The surviving possibilities are narrower:

1. a form that is positive and Li-normalized from the start, not obtained as
   the indefinite cross-pairing plus a positive invisible correction;
2. a sign-indefinite algebraic correction whose total sum reorganizes into a
   different positive Euler--Gamma form, with positivity proved only after
   the reorganization;
3. a direct proof of the Schoenberg kernel positivity
   \[
     [\lambda_j+\lambda_k-\lambda_{|j-k|}]\ge0
   \]
   from arithmetic data;
4. an independent support theorem, such as completed Carathéodory positivity
   with exact transformed-zero singularities.

Any proof in classes (1)--(2) must be genuinely global.  It cannot be
assembled as the old cross-pairing plus a nonzero positive form that is
invisible on all Li diagonals.

## Relation to A1

The compact A1 route after A0 would follow from a stronger diagonal margin
for the renormalized form.  This no-go says that such a margin cannot be
created by local positive terms that leave the Li diagonal unchanged orbit by
orbit, nor by any positive global counterterm invisible on the Li tests.  The
required margin, if true, must come from a different global Euler--Gamma
mechanism.

## Status

Closed as a local and global positive-counterterm no-go.  A1 remains open.

The next viable target is a new Li-normalized positive Euler--Gamma form, a
sign-reorganizing global construction, an independent support theorem, or a
direct arithmetic proof of the Schoenberg kernel positivity.
