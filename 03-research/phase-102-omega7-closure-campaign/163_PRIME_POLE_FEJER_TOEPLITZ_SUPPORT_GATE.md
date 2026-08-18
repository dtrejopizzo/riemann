# Prime-pole Fejer--Toeplitz support gate

## Purpose

This note refines the prime-pole Pick/Stieltjes route by separating three
different Fejer statements:

1. scalar Cesaro/Fejer averages of Li coefficients;
2. Fejer positivity at one boundary point for a candidate moment sequence;
3. Fejer positivity after every boundary translate.

Only the third statement is equivalent to a positive boundary measure and
hence to the infinite Toeplitz gate.  The first two are useful tests but do
not close A1.

Throughout, no support on \(\partial\mathbb D\) is assumed.  Any support
statement must be derived from completed Euler--Gamma data.

## Moment notation

Let
\[
  F(z)=\log\xi\!\left({1\over1-z}\right),
  \qquad
  \mathcal L(z)=zF'(z)=\sum_{n\ge1}\lambda_n z^n .
\tag{1}
\]

In zero-side disk coordinates write
\[
  w_\rho=1-{1\over\rho}.
\tag{2}
\]

A disk boundary-measure proof would construct Hermitian moments
\[
  m_{-n}=\overline{m_n},\qquad n\ge0,
\tag{3}
\]
from the completed Euler--Gamma data, with the same paired normalization as
the Li transform, such that the associated Carathéodory object has the
transformed zero divisor as its singularity set.

The infinite Toeplitz condition is
\[
  \boxed{
  \sum_{j,k=0}^N c_j\overline{c_k}\,m_{j-k}\ge0
  \quad
  \hbox{for every }N\ge0
  \hbox{ and every }c_0,\ldots,c_N\in\mathbb C .
  }
\tag{4}
\]

By the Herglotz theorem on the circle, (4) is equivalent to the existence of
a positive finite measure \(\nu\) on \(\partial\mathbb D\) such that
\[
  m_n=\int_{\partial\mathbb D}\zeta^n\,d\nu(\zeta).
\tag{5}
\]

If, in addition, the singularities of the Carathéodory function built from
\(\{m_n\}\) are exactly the transformed nontrivial zero divisor, then (5)
forces those singularities to lie on \(\partial\mathbb D\), hence gives RH
and then Omega7 by Li.

## Fejer kernels and the exact equivalence

For \(N\ge1\), let
\[
  K_N(\theta)
  =
  \sum_{|k|<N}
  \left(1-{|k|\over N}\right)e^{ik\theta}
  =
  {1\over N}
  \left|{1-e^{iN\theta}\over1-e^{i\theta}}\right|^2
  \ge0 .
\tag{6}
\]

Given a Hermitian sequence \(\{m_n\}\), define the Fejer means
\[
  \sigma_N(\theta)
  =
  \sum_{|k|<N}
  \left(1-{|k|\over N}\right)m_k e^{ik\theta}.
\tag{7}
\]

The following is the exact Fejer version of the Toeplitz moment gate.

**Lemma 1.** For a Hermitian sequence \(\{m_n\}_{n\in\mathbb Z}\), the
following are equivalent:

1. all Toeplitz matrices \([m_{j-k}]_{0\le j,k\le M}\) are positive
   semidefinite;
2. there exists a positive finite measure \(\nu\) on \(\partial\mathbb D\)
   with moments \(m_n\);
3. for every \(N\ge1\) and every \(\theta\in\mathbb R\),
   \[
     \sigma_N(\theta)\ge0 .
   \tag{8}
   \]

**Proof.** The equivalence of (1) and (2) is the trigonometric moment theorem.
If (2) holds, then
\[
  \sigma_N(\theta)
  =
  \int_{\partial\mathbb D}K_N(\theta+\arg\zeta)\,d\nu(\zeta)\ge0,
\]
so (3) holds.  Conversely, if (3) holds, the trigonometric polynomials
\(\sigma_N(\theta)d\theta/(2\pi)\) are positive measures.  For each fixed
Fourier mode \(k\),
\[
  \widehat{\sigma_N}(k)=
  \left(1-{|k|\over N}\right)m_k
  \quad (N>|k|),
\]
and these Fourier coefficients tend to \(m_k\).  Therefore the positive
measures \(\sigma_N(\theta)d\theta/(2\pi)\) converge to a positive
distribution with Fourier coefficients \(m_k\).  A positive distribution on
the circle is a positive Radon measure.  This gives (2).  \(\square\)

Thus the full translated Fejer theorem is not weaker than Toeplitz
positivity.  It is the same infinite boundary-measure problem in Cesaro
coordinates.

## What scalar Fejer averages cannot prove

The condition
\[
  \sigma_N(0)\ge0\qquad(N\ge1)
\tag{9}
\]
tests only the special Toeplitz quadratic forms with vector
\[
  c=(1,1,\ldots,1)/\sqrt N.
\tag{10}
\]

More generally, \(\sigma_N(\theta)\ge0\) for one fixed \(\theta\) tests only
the geometric vector
\[
  c_j=e^{ij\theta}/\sqrt N,\qquad 0\le j<N.
\tag{11}
\]

Toeplitz positivity requires all vectors \(c\), or equivalently all
nonnegative trigonometric polynomials \(|Q(e^{i\theta})|^2\).  A proof that
controls only the Fejer averages (9), or only the Cesaro averages of
\(\lambda_n\), therefore cannot construct the boundary measure.

This eliminates the shortcut
\[
  \hbox{Cesaro positivity of Li data}
  \quad\Longrightarrow\quad
  \hbox{Carathéodory/Pick/Stieltjes representation}.
\tag{12}
\]

The missing angular variable in (9) is not cosmetic.  It is exactly the
polarization needed to test every Toeplitz direction.

## Relation to prime-pole data

The prime-pole generator gives
\[
  [z^n]\mathcal P(z)
  =
  -n+\int_1^\infty(\psi(y)-y)f'_{n,0}(y)\,dy
\tag{13}
\]
in the paired boundary sense.  After A0, A1 is the compact signed inequality
\[
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  +{3\over4}\lambda_n^{\rm arch}\ge0
  \qquad(n\ge8).
\tag{14}
\]

Fejer averaging (13) in the index \(n\) only produces Cesaro combinations of
the same signed prime-pole current.  Since the density
\(\psi(e^u)-e^u\) is signed and the Laguerre kernels oscillate, such
averaging does not create a positive measure.

To become a proof, the Fejer route must construct the full family
\(\sigma_N(\theta)\) from the completed Euler--Gamma object and prove
\[
  \sigma_N(\theta)\ge0
  \qquad(N\ge1,\ \theta\in\mathbb R)
\tag{15}
\]
before using the zero divisor as a boundary measure.

## Support consequence

Assume a completed Euler--Gamma construction supplies moments \(\{m_n\}\)
with the following two properties:

1. the Fejer inequalities (15) hold for all \(N,\theta\);
2. the associated Carathéodory function
   \[
     H(z)=m_0+2\sum_{n\ge1}m_nz^n
   \tag{16}
   \]
   has singularities exactly at the transformed nontrivial zero locations
   \(w_\rho=1-1/\rho\), with the prescribed paired multiplicities.

Then Lemma 1 gives a positive boundary measure \(\nu\).  The Herglotz
representation
\[
  H(z)=\int_{\partial\mathbb D}{1+\zeta z\over1-\zeta z}\,d\nu(\zeta)
\tag{17}
\]
has singularities only on \(\partial\mathbb D\).  Hence every transformed
nontrivial zero satisfies
\[
  \left|1-{1\over\rho}\right|=1,
\tag{18}
\]
which is equivalent to \(\Re\rho=1/2\).  Therefore RH follows, and Omega7
follows from Li.

This is a valid force-RH theorem if proved from Euler--Gamma data.  It is
circular only if the construction of \(\{m_n\}\), the proof of (15), or the
singularity identification already assumes boundary support.

## Minimal new theorem

The Fejer route closes A1/Omega7 only if the following theorem is proved.

**Completed Fejer support theorem.** Construct Hermitian moments
\(\{m_n\}_{n\in\mathbb Z}\) from the completed Euler--Gamma data, in the
paired Li normalization, such that:

1. for every \(N\ge1\) and every \(\theta\in\mathbb R\),
   \[
     \sum_{|k|<N}
     \left(1-{|k|\over N}\right)m_k e^{ik\theta}
     \ge0;
   \tag{19}
   \]
2. the Carathéodory function generated by \(\{m_n\}\) is the completed Li
   boundary object up to explicitly harmless analytic terms;
3. its singularities encode exactly the transformed nontrivial zeros, without
   defining the moments from a boundary-supported divisor.

By Lemma 1 this theorem is equivalent to the infinite Toeplitz moment gate.
It is stronger than coefficientwise Li positivity and stronger than scalar
Fejer positivity, but it is a clean positive-measure route.

## Eliminated proof patterns

The following patterns do not close A1:

1. proving only \(\sigma_N(0)\ge0\);
2. proving Cesaro positivity of \(\lambda_n\) without angular polarization;
3. checking finitely many Toeplitz or Fejer inequalities;
4. deriving Fejer positivity from \(\Lambda(m)\ge0\) in \(\Re s>1\) while
   dropping the pole-pairing and Gamma completion;
5. defining \(m_n\) by a divisor already placed on \(\partial\mathbb D\).

Each pattern misses either the infinite moment condition or the non-circular
support construction.

## Status

Closed as a refinement of the Pick/Stieltjes route.

Full translated Fejer positivity is not a new shortcut: it is exactly the
infinite Toeplitz positive-measure theorem in Cesaro form.  Scalar Fejer
averages and finite checks are weaker and do not imply support.  The open
problem remains the completed Euler--Gamma construction of the moments and
the proof of the full inequalities (19).
