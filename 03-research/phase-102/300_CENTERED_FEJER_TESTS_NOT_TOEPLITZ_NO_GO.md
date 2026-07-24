# Centered Fejer tests are not Toeplitz positivity

## Purpose

The increment-measure route needs positivity of every Toeplitz block
\[
  [g_{j-k}]_{j,k=0}^{N}\succeq0,
\]
equivalently a positive Herglotz boundary measure.  The compact strong
margin route, by contrast, tests only the centered Fejer quantities
\[
  \int F_n\,d\nu_g.
\]

This note records the finite-dimensional separation: positivity of all
centered Fejer sums does not imply Toeplitz positivity.  Therefore centered
Fejer/Li diagonal data cannot be used as a construction of the positive
increment measure.

## Centered Fejer sums

Given a Hermitian sequence \(g_{-m}=g_m\), define the formal centered Fejer
sum
\[
\boxed{
  \mathcal F_n(g)
  =
  g_0+2\sum_{m=1}^{n-1}\left(1-{m\over n}\right)g_m.
}
\tag{1}
\]

If \(g_m\) comes from a positive measure, then
\[
  \mathcal F_n(g)=\int_{\partial\mathbb D}F_n\,d\nu\ge0.
\]

The converse is false.

## Explicit counterexample

Set
\[
  g_0=1,\qquad g_1=0,\qquad g_2={3\over2},\qquad g_m=0\quad(m\ge3),
\]
and extend by \(g_{-m}=g_m\).

For \(n=1\),
\[
  \mathcal F_1(g)=1.
\]
For \(n=2\),
\[
  \mathcal F_2(g)=1+2\left(1-{1\over2}\right)g_1=1.
\]
For \(n\ge3\),
\[
\begin{aligned}
  \mathcal F_n(g)
  &=
  1+2\left(1-{2\over n}\right){3\over2}  \\
  &=
  4-{6\over n}
  \ge2.
\end{aligned}
\tag{2}
\]

Thus every centered Fejer sum is positive:
\[
\boxed{\mathcal F_n(g)>0\qquad(n\ge1).}
\tag{3}
\]

But the \(3\times3\) Toeplitz block is
\[
  T_2=
  \begin{pmatrix}
    1&0&3/2\\
    0&1&0\\
    3/2&0&1
  \end{pmatrix}.
\]

Testing \(v=(1,0,-1)\) gives
\[
  v^*T_2v
  =
  -1<0.
\tag{4}
\]

Therefore the Hermitian sequence has all centered Fejer tests positive but
does not have a positive representing measure.

## Consequence for the phase

The identities
\[
  2\lambda_n=n\int F_n\,d\nu_g
\]
or their formal centered Fejer analogues test only the diagonal Li
directions \(1-z^n\).  They do not verify the full Toeplitz cone
\[
  \sum_{j,k}c_j\overline{c_k}g_{j-k}\ge0
\]
for arbitrary trigonometric polynomials.

Thus:

1. centered Fejer positivity is not a Herglotz-measure construction;
2. strong-margin Fejer lower bounds are compact A1 data, not global
   Toeplitz positivity data;
3. constructing \(\nu_g\ge0\) still requires all translated Fejer tests, or
   an equivalent Carathéodory/Herglotz theorem.

This complements `290`, which eliminates radial Abel positivity as a
Herglotz shortcut, and `281`, which eliminates radial Abel spikes as a
Fejer-margin shortcut.

## Status

Closed as a centered-Fejer versus Toeplitz no-go.  A1 remains open, and the
positive increment measure remains an independent global theorem unless
full translated Fejer/Toeplitz positivity is proved non-circularly.
