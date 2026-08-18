# Poisson--Carathéodory support gate

## Purpose

The Fejer--Toeplitz gate can also be written in Abel--Poisson form.  This
note records the exact equivalence and the precise obstruction.

The useful output is twofold:

1. Poisson real-part positivity is not weaker than infinite Toeplitz
   positivity.  It is the same circle moment problem in radial coordinates.
2. If the resulting Carathéodory function has the transformed nontrivial
   zero divisor as its singularity set, then real-part positivity forbids
   any singularity inside the disk.  Therefore the missing step is exactly
   the non-circular Euler--Gamma proof of that real-part positivity.

A1 is not closed here.

## Hermitian moments and Abel sums

Let \((m_k)_{k\in\mathbb Z}\) be a Hermitian sequence,
\[
  m_{-k}=\overline{m_k},
\]
with finite \(m_0\).  Define the Abel--Poisson sums
\[
  S_r(\theta)
  =
  \sum_{k\in\mathbb Z} r^{|k|}m_k e^{ik\theta},
  \qquad 0\le r<1.
\tag{1}
\]

When the analytic series converges in the disk, put
\[
  H(z)=m_0+2\sum_{k\ge1}m_k z^k .
\tag{2}
\]
Then
\[
  \operatorname{Re}H(re^{i\theta})=S_r(\theta).
\tag{3}
\]

Thus the Poisson version of the gate is
\[
  \boxed{
  S_r(\theta)\ge0
  \qquad(0\le r<1,\ \theta\in\mathbb R).
  }
\tag{4}
\]

Equivalently, in analytic language,
\[
  \boxed{
  \operatorname{Re}H(z)\ge0
  \qquad(|z|<1).
  }
\tag{5}
\]

## Poisson moment theorem

For a Hermitian sequence with finite \(m_0\), the following conditions are
equivalent.

1. The Toeplitz matrices are positive semidefinite:
   \[
     [m_{j-k}]_{0\le j,k\le N}\ge0
     \qquad(N\ge0).
   \tag{6}
   \]
2. There is a positive finite measure \(\nu\) on \(\partial\mathbb D\) such
   that
   \[
     m_k=\int_{\partial\mathbb D}\zeta^k\,d\nu(\zeta)
     \qquad(k\in\mathbb Z).
   \tag{7}
   \]
3. The Abel--Poisson inequalities (4) hold for every \(r,\theta\).
4. If the series (2) is the associated analytic object, then \(H\) is a
   Carathéodory function, i.e. (5) holds in the disk.

The equivalence of (1) and (2) is the trigonometric moment theorem.  If
\(\nu\) exists, then
\[
  S_r(\theta)
  =
  \int_{\partial\mathbb D}
  P_r(\theta+\arg\zeta)\,d\nu(\zeta),
\tag{8}
\]
where
\[
  P_r(\phi)=\sum_{k\in\mathbb Z}r^{|k|}e^{ik\phi}
  ={1-r^2\over |1-re^{i\phi}|^2}\ge0.
\tag{9}
\]
Hence \(S_r(\theta)\ge0\).

Conversely, if \(S_r(\theta)\ge0\), then
\[
  d\nu_r(\theta)=S_r(\theta){d\theta\over2\pi}
\tag{10}
\]
is a positive measure of total mass \(m_0\).  Its \(k\)-th Fourier
coefficient is \(r^{|k|}m_k\).  Letting \(r\uparrow1\), a weak-* limit of
the positive measures \(\nu_r\) has Fourier coefficients \(m_k\).  This
gives (2), hence Toeplitz positivity.

Therefore
\[
  \boxed{
  \hbox{Poisson real-part positivity}
  \Longleftrightarrow
  \hbox{infinite Toeplitz positivity}.
  }
\tag{11}
\]

This is an equivalence, not a shortcut.

## Interior singularities are impossible

A Carathéodory function cannot have a pole inside the disk.  More generally,
if a meromorphic function has nonnegative real part in a punctured
neighborhood of an interior point \(a\), then the singularity at \(a\) is
removable.

Indeed, if
\[
  H(z)=c_q(z-a)^{-q}+c_{q-1}(z-a)^{1-q}+\cdots
  \qquad(c_q\ne0)
\tag{12}
\]
has a pole of order \(q\ge1\), then on \(z=a+\rho e^{i\phi}\) the leading
real part is
\[
  \rho^{-q}\operatorname{Re}(c_qe^{-iq\phi})+O(\rho^{1-q}).
\tag{13}
\]
As \(\phi\) varies, \(\operatorname{Re}(c_qe^{-iq\phi})\) takes both signs.
For sufficiently small \(\rho\), \(\operatorname{Re}H\) is therefore negative
somewhere.  This contradicts real-part positivity.

Thus if a completed Euler--Gamma Carathéodory function is positive in the
disk, all of its non-removable singularities must lie on the boundary.

## Consequence for transformed zeta zeros

In Li disk coordinates,
\[
  w_\rho=1-{1\over\rho}.
\tag{14}
\]
For \(\rho=\sigma+it\),
\[
  |w_\rho|^2
  =
  {|\rho-1|^2\over|\rho|^2}
  =
  1+{1-2\sigma\over|\rho|^2}.
\tag{15}
\]
Hence
\[
  |w_\rho|<1 \Longleftrightarrow \sigma>{1\over2},
  \qquad
  |w_\rho|=1 \Longleftrightarrow \sigma={1\over2}.
\tag{16}
\]

If a positive Carathéodory function built from completed Euler--Gamma data
has singularities exactly at the transformed nontrivial zeros, then (16)
and the no-interior-singularity lemma rule out every zero with
\(\sigma>1/2\).  The functional equation then rules out every zero with
\(\sigma<1/2\).  Thus all nontrivial zeros lie on the critical line.

This is the precise force of the Poisson route:
\[
  \boxed{
  \operatorname{Re}H_{\rm EG}\ge0
  \hbox{ in }\mathbb D
  +
  \hbox{exact transformed-zero singularities}
  \Longrightarrow
  RH.
  }
\tag{17}
\]

## Exact no-go

The Poisson formulation eliminates three possible shortcuts.

First, positivity only on one radius or one angle is insufficient.  For
example \(S_r(0)\ge0\) tests only a radial Abel average and does not test
the polarized Toeplitz forms
\[
  \sum_{j,k=0}^{N}c_j\overline{c_k}m_{j-k}.
\tag{18}
\]

Second, positivity of the Li coefficients cannot be read as Poisson
positivity.  The Li tests correspond to the special square energies
\[
  Q(1-z^n)=2(m_0-m_n),
\tag{19}
\]
not to all Toeplitz directions.

Third, if the singularities are inserted from a zero divisor that is already
assumed to be supported on \(\partial\mathbb D\), the argument is circular.
The proof must construct \(H_{\rm EG}\) from completed Euler--Gamma data and
prove (5) before using boundary support.

Equivalently, any meromorphic candidate whose exact singularity set contains
some \(w_\rho\) with \(|w_\rho|<1\) automatically fails the
Carathéodory inequality.  A regularization that cancels such an interior
singularity changes the singularity theorem and no longer proves support
for the original divisor.

## Relation to compact A1

Bare Poisson positivity gives Li positivity through the boundary measure:
\[
  Q(1-z^n)\ge0
  \qquad(n\ge1).
\tag{20}
\]
The compact A1 inequality after the A0 tail budget needs a margin, as in
`164_A1_TOEPLITZ_SCHUR_MARGIN.md`:
\[
  Q(1-z^n)\ge A_n=\lambda_n^{\rm arch}
  \qquad(n\ge8),
\tag{21}
\]
or the stronger prediction-error margin.

Thus the Poisson route has two possible closure strengths:

1. real-part positivity plus exact singularities closes RH and hence
   Omega7 by Li;
2. real-part positivity plus the margin (21), together with A0, closes the
   compact A1 route directly.

Neither theorem is proved here.  The first is the completed boundary-support
theorem in Poisson form; the second is the same theorem with the
archimedean margin needed by the compact cutoff assembly.

## Status

Closed as a Poisson--Carathéodory normal form and no-go.

A1 remains open.  The exact live theorem is now:

\[
  \operatorname{Re}H_{\rm EG}(z)\ge0\quad(|z|<1),
\]
for a non-circular completed Euler--Gamma Carathéodory function whose
singularities are exactly the transformed nontrivial zero divisor; and, for
the compact A1 assembly, the additional Toeplitz square margin
\[
  Q(1-z^n)\ge\lambda_n^{\rm arch}\qquad(n\ge8).
\]
