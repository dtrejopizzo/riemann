# Li Fejer trigonometric moment gate

## Purpose

`161_LI_TOEPLITZ_MOMENT_GATE.md` states the positive boundary-measure route
as infinite Toeplitz moment positivity.  This note rewrites that gate in the
equivalent trigonometric-polynomial language and records exactly what a
Fejer or Dirichlet-kernel proof would have to prove.

The result is a sharper target, not a closure of A1.

## Toeplitz form

Let \((m_k)_{k\in\mathbb Z}\) be the completed disk moment sequence attached
to the Euler--Gamma Li transform, with
\[
  m_{-k}=\overline{m_k}.
\]

The infinite Toeplitz gate is
\[
  T_N(m):=\left[m_{j-k}\right]_{0\le j,k\le N}\ge0
  \qquad(N\ge0).
\tag{1}
\]

Equivalently, for every \(N\) and every vector
\(c=(c_0,\ldots,c_N)\in\mathbb C^{N+1}\),
\[
  Q_m(c)
  :=
  \sum_{j,k=0}^N c_j\overline{c_k}\,m_{j-k}
  \ge0.
\tag{2}
\]

This is only a useful A1 route if the \(m_k\) are constructed from the
completed Euler--Gamma data before assuming critical-line support.

## Trigonometric-polynomial form

Let
\[
  P(\zeta)=\sum_{j=0}^N c_j\zeta^j,
  \qquad |\zeta|=1.
\]

If a finite positive measure \(\nu\) on \(\partial\mathbb D\) has moments
\[
  m_\ell=\int_{\partial\mathbb D}\zeta^\ell\,d\nu(\zeta),
\tag{3}
\]
then
\[
  Q_m(c)
  =
  \int_{\partial\mathbb D}|P(\zeta)|^2\,d\nu(\zeta)
  \ge0.
\tag{4}
\]

Conversely, if (2) holds for every finite vector \(c\), then the functional
\[
  \Phi\!\left(\sum_{\ell=-N}^{N} a_\ell\zeta^\ell\right)
  =
  \sum_{\ell=-N}^{N} a_\ell m_\ell
\tag{5}
\]
is nonnegative on every trigonometric polynomial that is a square
\(|P|^2\).  Since every nonnegative trigonometric polynomial is a squared
modulus by the Fejer--Riesz theorem,
\[
  R(\zeta)\ge0
  \quad\Longrightarrow\quad
  R(\zeta)=|P(\zeta)|^2,
\tag{6}
\]
the same condition is equivalent to
\[
  \Phi(R)\ge0
  \qquad
  \hbox{for every nonnegative trigonometric polynomial }R.
\tag{7}
\]

By the Herglotz/Riesz representation theorem on the circle, (7) is
equivalent to the existence of a positive representing measure \(\nu\) with
moments (3).

Thus the exact gate is
\[
  \boxed{
  \Phi_{\rm EG}(R)\ge0
  \quad\hbox{for every nonnegative trigonometric polynomial }R,
  }
\tag{8}
\]
where \(\Phi_{\rm EG}\) is the moment functional obtained from the completed
Euler--Gamma Li data.

## Fejer kernels

The Fejer kernel is the special square
\[
  F_N(e^{i\theta})
  =
  {1\over N}\left|\sum_{j=0}^{N-1}e^{ij\theta}\right|^2
  =
  \sum_{|\ell|<N}\left(1-{|\ell|\over N}\right)e^{i\ell\theta}.
\tag{9}
\]

Testing only the untranslated \(F_N\) gives the necessary inequalities
\[
  \sum_{|\ell|<N}\left(1-{|\ell|\over N}\right)m_\ell\ge0
  \qquad(N\ge1).
\tag{10}
\]

More generally, translating the Fejer kernel by \(\alpha\in\partial\mathbb D\)
gives
\[
  \sum_{|\ell|<N}\left(1-{|\ell|\over N}\right)
  \alpha^\ell m_\ell\ge0.
\tag{11}
\]

The untranslated tests (10) are only a subfamily of (8).  The fully
translated tests (11), however, have a stronger interpretation.  Define
\[
  \sigma_N(\theta)
  =
  \sum_{|\ell|<N}\left(1-{|\ell|\over N}\right)
  m_\ell e^{i\ell\theta}.
\tag{12}
\]

Then
\[
  \boxed{
  \sigma_N(\theta)\ge0\quad(N\ge1,\ \theta\in\mathbb R)
  }
\tag{13}
\]
is equivalent to Toeplitz positivity, provided \(m_0\) is finite.

Indeed, Toeplitz positivity gives a positive representing measure \(\nu\),
and then \(\sigma_N\) is the convolution of \(\nu\) with the positive Fejer
kernel.  Conversely, if every \(\sigma_N\) is nonnegative, then
\[
  d\nu_N(\theta)=\sigma_N(\theta){d\theta\over2\pi}
\]
is a positive measure with total mass \(m_0\).  Its \(k\)-th Fourier
coefficient is
\[
  \left(1-{|k|\over N}\right)m_k
  \qquad(N>|k|),
\]
which tends to \(m_k\) as \(N\to\infty\).  A weak-* limit of the positive
measures \(\nu_N\) is therefore a positive representing measure with moments
\((m_k)\).

Thus the implication
\[
  \hbox{all translated Fejer tests hold}
  \quad\Longleftrightarrow\quad
  \hbox{Toeplitz positivity}
\tag{14}
\]
is valid.  What is not enough is positivity of the scalar tests (10), or
positivity of finitely many translated tests.

## Dirichlet kernels

The Dirichlet polynomial
\[
  D_N(e^{i\theta})=\sum_{j=0}^{N}e^{ij\theta}
\]
produces the square
\[
  |D_N(e^{i\theta})|^2
  =
  \sum_{|\ell|\le N}(N+1-|\ell|)e^{i\ell\theta}.
\tag{15}
\]

This is just an unnormalized Fejer test.  It is positive and necessary, but
it is not the full Toeplitz cone.

Arbitrary Dirichlet-type squares
\[
  \left|\sum_{j=0}^N c_j e^{ij\theta}\right|^2
\tag{16}
\]
are different: they are exactly the Toeplitz quadratic forms (2).  Hence the
word "Dirichlet" closes no gap unless arbitrary coefficients are included.

## Euler--Gamma closure theorem

The trigonometric version of the A1 global positivity route is:

**Theorem needed.**  Construct a Hermitian moment sequence
\((m_k^{\rm EG})_{k\in\mathbb Z}\) from the completed Euler--Gamma Li data,
with no use of critical-line support, such that:

1. for every nonnegative trigonometric polynomial \(R\),
   \[
     \Phi_{\rm EG}(R)\ge0;
   \]
2. the resulting Herglotz function
   \[
     H(z)=\Phi_{\rm EG}\!\left({1+\zeta z\over1-\zeta z}\right)
   \]
   has singularities exactly at the transformed nontrivial zero divisor;
3. the moment normalization is compatible with the paired Li coefficient
   identity.

Then Herglotz gives a positive boundary measure on
\(\partial\mathbb D\).  The singularity condition forces every transformed
zero \(w_\rho=1-1/\rho\) to satisfy \(|w_\rho|=1\).  Hence every nontrivial
zero lies on the critical line, Li positivity follows, and Omega7 closes.

## A1 relation

The chain is:
\[
  \hbox{Euler--Gamma positivity on all }|P|^2
  \Longrightarrow
  \hbox{positive boundary measure}
  \Longrightarrow
  \hbox{critical-line support}
  \Longrightarrow
  \lambda_n\ge0\quad(n\ge1).
\]

Thus this route is stronger than the compact A1 inequality but would close
it.  It is also nonlocal: it proves all Li tests simultaneously instead of
only the moving compact diagonal \(C_n(T_n)\ge0\).

## Eliminated shortcuts

The following do not close A1:

1. positivity of finitely many Toeplitz matrices;
2. positivity against the untranslated Fejer kernels only;
3. positivity against only finitely many translated Fejer kernels;
4. positivity of the Li coefficients \(\lambda_n\) treated as if they were
   Toeplitz moments;
5. a measure constructed from the zero divisor after assuming
   \(|w_\rho|=1\).

Each item is a necessary test or a useful diagnostic, but none supplies the
full positive boundary-measure theorem.

## Status

Closed as a normal-form gate.  A1 remains open.

The sharpened global positivity target is: prove the Euler--Gamma moment
functional nonnegative on every squared trigonometric polynomial
\[
  \left|\sum_{j=0}^N c_j\zeta^j\right|^2
\]
for all \(N\) and all coefficient vectors \(c\), with a non-circular
identification of the singularities.
