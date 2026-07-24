# Finite Toeplitz blocks are not a Herglotz construction

## Purpose

The disk Herglotz route requires the infinite Toeplitz positivity condition
\[
  T_L(g):=[g_{j-k}]_{j,k=0}^{L}\succeq0
  \qquad(L=0,1,2,\ldots),
\]
equivalently positivity on every squared trigonometric polynomial.  This is
the condition that constructs a positive boundary measure.

This note records the sharp finite obstruction: checking any fixed finite
family of Toeplitz blocks, even perfectly, does not imply the next block or
the existence of a Herglotz measure.

## Parametric counterexample

Fix \(N\ge0\) and choose \(M>1\).  Define a Hermitian sequence by
\[
  g_0=1,\qquad
  g_{\pm(N+1)}=M,\qquad
  g_m=0\quad(0<|m|\ne N+1).
\]

For every \(0\le L\le N\), the Toeplitz block \(T_L(g)\) only sees
differences \(|j-k|\le L\le N\).  Hence it does not see \(g_{\pm(N+1)}\),
and
\[
  T_L(g)=I_{L+1}\succeq0
  \qquad(0\le L\le N).
\]

But the next block \(T_{N+1}(g)\) contains the two-by-two principal
submatrix on the coordinates \(0,N+1\):
\[
  \begin{pmatrix}
    1&M\\
    M&1
  \end{pmatrix}.
\]
Its eigenvalues are \(1+M\) and \(1-M\).  Since \(M>1\), the block is not
positive semidefinite.  Equivalently,
\[
  (e_0-e_{N+1})^\ast T_{N+1}(g)(e_0-e_{N+1})
  =
  2(1-M)<0.
\]

Therefore:
\[
\boxed{
  T_L(g)\succeq0\ (0\le L\le N)
  \quad\not\Longrightarrow\quad
  T_{N+1}(g)\succeq0.
}
\]

## Consequence for Omega7

The Herglotz/RDI route cannot be closed by any fixed finite list of
Toeplitz checks.  A non-circular global proof must provide at least one of
the following:

1. positivity of every Toeplitz block \(T_L(g)\);
2. positivity on every squared trigonometric polynomial;
3. a positive boundary measure constructed before using zero support;
4. a limiting theorem in which each fixed block is positive in the limit,
   with genuine coefficient convergence.

This complements:

- `290_RADIAL_ABEL_POSITIVITY_NOT_HERGLOTZ_NO_GO.md`, which rules out purely
  radial positivity;
- `300_CENTERED_FEJER_TESTS_NOT_TOEPLITZ_NO_GO.md`, which rules out centered
  Fejer diagonal tests;
- `310_REAL_RAY_CONVERGENCE_NOT_LI_COEFFICIENT_NO_GO.md`, which rules out
  real-ray convergence as a coefficient bridge.

Thus finite Toeplitz evidence may certify a finite computation, but it is
not a Herglotz-measure construction and cannot by itself close Omega7 or
the compact A1 target.

## Status

Closed as a no-go for finite-block Herglotz shortcuts.  The remaining global
route is infinite Toeplitz/Carathéodory positivity with a valid limiting
bridge; the compact A1 route still needs its separate pointwise margin or
tail certificate.
