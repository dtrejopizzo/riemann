# Strong margin second-difference audit

## Purpose

`172_SCHOENBERG_INCREMENT_TOEPLITZ_GATE.md` rewrites the Schoenberg kernel
of Li coefficients in terms of the Toeplitz second-difference sequence
\[
  g_0=2\lambda_1,\qquad
  g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}\quad(m\ge1).
\]

`194_STRONG_MARGIN_GENERATOR_SECOND_PASS.md` shows that compact A1 follows
from the strong margin
\[
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}\qquad(n\ge8).
\tag{1}
\]

This note expresses (1) entirely in the second-difference Toeplitz
coordinates and records the exact extra margin needed beyond positivity of
the \(g\)-Toeplitz matrices.

## Recovering Li from second differences

Let
\[
  G_N=[g_{|j-k|}]_{1\le j,k\le N}.
\]
From `172`,
\[
  K_N=L_NG_NL_N^\ast,
\tag{2}
\]
where \(K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}\) and \(L_N\) is the
lower-triangular summation matrix.

Taking the \(n,n\) diagonal of \(K_N\) gives
\[
  K(n,n)=2\lambda_n.
\tag{3}
\]

Equivalently, if \(\mathbf 1_n=(1,\ldots,1)^t\in\mathbb C^n\), then
\[
  K(n,n)=\mathbf 1_n^\ast G_n\mathbf 1_n.
\tag{4}
\]

Thus
\[
\boxed{
  2\lambda_n
  =
  \mathbf 1_n^\ast G_n\mathbf 1_n
  =
  n g_0+2\sum_{m=1}^{n-1}(n-m)g_m.
}
\tag{5}
\]

The strong margin (1) is therefore exactly
\[
\boxed{
  n g_0+2\sum_{m=1}^{n-1}(n-m)g_m
  \ge
  \lambda_n^{\rm arch}
  \qquad(n\ge8).
}
\tag{6}
\]

This is the second-difference margin theorem.

## Moment-measure form

If the increment Toeplitz theorem is proved, then by Herglotz there is a
finite positive measure \(\nu_g\) on \(\partial\mathbb D\) such that
\[
  g_m=\int_{\partial\mathbb D}\zeta^m\,d\nu_g(\zeta)
  \qquad(m\in\mathbb Z).
\tag{7}
\]

Then
\[
\begin{aligned}
  \mathbf 1_n^\ast G_n\mathbf 1_n
  &=
  \int_{\partial\mathbb D}
  \left|\sum_{j=0}^{n-1}\zeta^j\right|^2
  d\nu_g(\zeta).
\end{aligned}
\tag{8}
\]

Therefore the strong margin is equivalent to the Fejer/Dirichlet lower
bound
\[
\boxed{
  \int_{\partial\mathbb D}
  \left|1+\zeta+\cdots+\zeta^{n-1}\right|^2
  d\nu_g(\zeta)
  \ge
  \lambda_n^{\rm arch}
  \qquad(n\ge8).
}
\tag{9}
\]

Or, with the normalized Fejer kernel
\[
  F_n(\zeta)={1\over n}\left|\sum_{j=0}^{n-1}\zeta^j\right|^2,
\tag{10}
\]
the condition is
\[
\boxed{
  n\int_{\partial\mathbb D}F_n(\zeta)\,d\nu_g(\zeta)
  \ge
  \lambda_n^{\rm arch}.
}
\tag{11}
\]

This is the margin version of the increment Toeplitz theorem.

## What positivity of \(g\) supplies

Toeplitz positivity of \(g\) gives
\[
  \mathbf 1_n^\ast G_n\mathbf 1_n\ge0.
\tag{12}
\]

Equivalently,
\[
  \int_{\partial\mathbb D}
  \left|1+\zeta+\cdots+\zeta^{n-1}\right|^2d\nu_g(\zeta)\ge0.
\tag{13}
\]

This is Li positivity:
\[
  \lambda_n\ge0.
\tag{14}
\]

The compact A1 bridge through A0 needs the quantitative strengthening
\[
  \mathbf 1_n^\ast G_n\mathbf 1_n\ge\lambda_n^{\rm arch}.
\tag{15}
\]

Thus the missing data are not another positivity statement for the same
matrix.  They are a lower scale bound for the specific Dirichlet-vector
energy.

## Formal no-go: positive second differences do not imply the margin

The implication
\[
  G_N\ge0\quad(\forall N)
  \Longrightarrow
  \mathbf 1_n^\ast G_n\mathbf 1_n\ge\lambda_n^{\rm arch}
\tag{16}
\]
is false as a theorem of Toeplitz-positive sequences, even if the total mass
\[
  g_0=\nu_g(\partial\mathbb D)
\tag{17}
\]
is fixed and positive.

Fix \(n\ge2\).  Let \(\nu\) be any positive measure supported on nontrivial
\(n\)-th roots of unity:
\[
  \zeta^n=1,\qquad \zeta\ne1.
\tag{18}
\]

For every point in this support,
\[
  1+\zeta+\cdots+\zeta^{n-1}=0.
\tag{19}
\]

Hence
\[
  \int_{\partial\mathbb D}
  \left|1+\zeta+\cdots+\zeta^{n-1}\right|^2d\nu(\zeta)=0.
\tag{20}
\]

The moment sequence
\[
  g_m=\int\zeta^m\,d\nu(\zeta)
\tag{21}
\]
is Toeplitz positive, because it comes from a positive measure, but the
strong margin at this \(n\) fails for every
\[
  \lambda_n^{\rm arch}>0.
\tag{22}
\]

Therefore even positive-definiteness plus fixed positive total mass does not
force the external archimedean margin.  The measure must have quantitative
mass seen by the Dirichlet kernel at every \(n\ge8\), and that is additional
information.

This is a no-go for formal inference from the increment Toeplitz theorem
alone.  It is not a construction of zeta data.

## Equivalent margin targets

The second-difference strong-margin theorem can be stated in any of the
following forms.

### Toeplitz quadratic form

\[
  \mathbf 1_n^\ast G_n\mathbf 1_n
  \ge
  \lambda_n^{\rm arch}
  \qquad(n\ge8).
\tag{23}
\]

### Weighted moment lower bound

\[
  \int_{\partial\mathbb D}|D_n(\zeta)|^2\,d\nu_g(\zeta)
  \ge
  \lambda_n^{\rm arch},
  \qquad
  D_n(\zeta)=\sum_{j=0}^{n-1}\zeta^j.
\tag{24}
\]

### Fejer lower bound

\[
  \int_{\partial\mathbb D}F_n(\zeta)\,d\nu_g(\zeta)
  \ge
  {\lambda_n^{\rm arch}\over n}.
\tag{25}
\]

### Coefficient second-difference form

\[
  n g_0+2\sum_{m=1}^{n-1}(n-m)g_m
  \ge
  \lambda_n^{\rm arch}
  \qquad(n\ge8).
\tag{26}
\]

### Strong-margin generator form

Using `194`,
\[
  [z^n]\left(\mathcal L-{1\over2}\mathcal A\right)\ge0
  \qquad(n\ge8).
\tag{27}
\]

Equations (23)--(27) are the same margin in different coordinates.

## Exact theorem still needed

The increment Toeplitz route would close compact A1 via A0 if it proved:

1. the completed Euler--Gamma second-difference sequence \(g_m\) is
   Toeplitz positive;
2. the associated positive measure or Toeplitz matrices satisfy the
   quantitative Dirichlet lower bounds (23), equivalently (24)--(26), for
   every \(n\ge8\).

The first item is global Li/RH-strength positivity.  The second item is the
extra strong-margin scale.  It cannot be dropped or inferred formally from
the first item.

## Status

Closed as a second-difference margin audit.  A1 remains open.

The strong margin is exactly a lower bound for the Dirichlet-vector energy
of the increment Toeplitz measure.  Positivity of the second-difference
Toeplitz matrices gives only nonnegativity of that energy, not domination of
the archimedean sequence.
