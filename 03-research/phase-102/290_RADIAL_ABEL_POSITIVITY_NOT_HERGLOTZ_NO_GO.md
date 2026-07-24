# Radial Abel positivity is not Herglotz positivity

## Purpose

The global increment-measure route needs a positive Herglotz/Carathéodory
representation for
\[
  H_\xi(z)=2{\xi'\over\xi}\!\left({1\over1-z}\right),
  \qquad |z|<1.
\]

Equivalently, it needs
\[
  \Re H_\xi(z)\ge0
  \qquad(|z|<1),
\]
or positivity of every Toeplitz block of the increment sequence \(g_m\).

This note records a basic no-go: positivity or favorable growth on the
real radius \(0<r<1\) is not enough.  Radial Abel data do not imply disk
Herglotz positivity.

## What radial Abel data control

The one-dimensional Abel probe is
\[
  H(r)=g_0+2\sum_{m\ge1}g_mr^m,
  \qquad 0<r<1.
\]

For the Euler--Gamma generator, this radial function has the logarithmic
scale recorded in `204`, `265`, and `266`.  But the Herglotz theorem
requires positivity of the real part for every angular point:
\[
  \Re H(re^{i\theta})\ge0
  \qquad(0\le r<1,\ -\pi\le\theta\le\pi).
\tag{1}
\]

Equivalently, for every trigonometric polynomial \(p\),
\[
  \sum_{j,k}c_j\overline{c_k}\,g_{j-k}\ge0.
\tag{2}
\]

The radial test only probes the single direction \(\theta=0\).  It does
not test the Toeplitz cone.

## Explicit polynomial obstruction

Consider
\[
  H(z)=1+3z^2.
\tag{3}
\]

On the positive radius,
\[
  H(r)=1+3r^2>0
  \qquad(0\le r<1).
\tag{4}
\]

Thus every radial Abel value is positive.

However, on the imaginary radius,
\[
  \Re H(ir)=1-3r^2,
\]
which is negative for \(r>1/\sqrt3\).  Hence \(H\) is not a
Carathéodory/Herglotz function on the disk.

The same failure appears in the Toeplitz moments.  In Carathéodory
normalization,
\[
  H(z)=g_0+2g_2z^2,
  \qquad
  g_0=1,\quad g_1=0,\quad g_2={3\over2}.
\]

The \(3\times3\) Toeplitz block contains
\[
  \begin{pmatrix}
    g_0 & g_1 & g_2\\
    g_1 & g_0 & g_1\\
    g_2 & g_1 & g_0
  \end{pmatrix}
  =
  \begin{pmatrix}
    1 & 0 & 3/2\\
    0 & 1 & 0\\
    3/2 & 0 & 1
  \end{pmatrix}.
\tag{5}
\]

Testing the vector \((1,0,-1)\) gives
\[
  (1,0,-1)
  \begin{pmatrix}
    1 & 0 & 3/2\\
    0 & 1 & 0\\
    3/2 & 0 & 1
  \end{pmatrix}
  \begin{pmatrix}1\\0\\-1\end{pmatrix}
  =
  -1<0.
\tag{6}
\]

So radial positivity and Toeplitz positivity are logically different.

## Consequence for the Euler--Gamma route

The estimates
\[
  H_\xi(r)=\log {1\over1-r}+O(1)
\]
or
\[
  H_\xi(r)\ge c\log {1\over1-r}-O(1)
\]
along \(0<r<1\) do not construct the positive increment measure
\(\nu_g\).  They provide only Abel information in one direction.

To close the global Herglotz route one must prove at least one of the
following genuinely multidirectional statements:

1. \(\Re H_\xi(z)\ge0\) for every \(|z|<1\);
2. positivity of every Toeplitz block \([g_{j-k}]\);
3. a positive boundary measure whose Herglotz transform is \(H_\xi\);
4. an equivalent RH-strength theorem such as the half-plane positivity of
   `174`--`175`.

For compact A1, even this global measure is not enough unless paired with
the quantitative Fejer mass theorem isolated in `271`--`273`, or with the
tail/margin bridge.

## Status

Closed as a radial-Abel no-go.  A1 and Omega7 remain open: the missing
global input is disk/half-plane Herglotz positivity, not merely positivity
or logarithmic growth on the positive radius.
