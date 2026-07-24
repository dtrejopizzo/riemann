# Schoenberg increment Toeplitz gate

## Purpose

`169_LI_SCHOENBERG_VANISHING_KERNEL.md` isolates the anchored kernel
\[
  K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}.
\]

This note rewrites positivity of \(K\) as an equivalent Toeplitz positivity
problem for its discrete increments.  The new sequence is
\[
  g_0=2\lambda_1,\qquad
  g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}\quad(m\ge1).
\]

This is a sharper version of the Schoenberg route.  It is not a proof of
A1; it identifies the exact second-difference positivity theorem that would
imply Li.

## Anchored kernel

Set
\[
  \lambda_0=0,\qquad \lambda_{-m}=\lambda_m.
\]

For \(j,k\ge1\), define
\[
  K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}.
\tag{1}
\]

Extend \(K\) by
\[
  K(0,k)=K(j,0)=0.
\tag{2}
\]

The Schoenberg target is
\[
  [K(j,k)]_{1\le j,k\le N}\ge0
  \qquad(N\ge1).
\tag{3}
\]

Since
\[
  K(n,n)=2\lambda_n,
\tag{4}
\]
(3) implies Li positivity.

## Increment kernel

Define the mixed discrete increment
\[
  G(j,k)
  =
  K(j,k)-K(j-1,k)-K(j,k-1)+K(j-1,k-1)
\tag{5}
\]
for \(j,k\ge1\).

If \(j\ne k\), with \(m=|j-k|\ge1\), the terms depending on
\(\lambda_j\) and \(\lambda_k\) cancel, and
\[
  G(j,k)
  =
  \lambda_{m+1}-2\lambda_m+\lambda_{m-1}.
\tag{6}
\]

If \(j=k\), then
\[
  G(j,j)=2\lambda_1.
\tag{7}
\]

Thus
\[
  G(j,k)=g_{|j-k|},
\tag{8}
\]
where
\[
  \boxed{
  g_0=2\lambda_1,\qquad
  g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}\quad(m\ge1).
  }
\tag{9}
\]

So the increment kernel is Toeplitz.

## Equivalence

Let \(L_N\) be the lower-triangular summation matrix
\[
  (L_N)_{jr}=1_{\{r\le j\}},
  \qquad 1\le r\le j\le N.
\]

The relation between \(K\) and \(G\) is
\[
  K_N=L_N\,G_N\,L_N^\ast,
\tag{10}
\]
where
\[
  K_N=[K(j,k)]_{1\le j,k\le N},
  \qquad
  G_N=[g_{|j-k|}]_{1\le j,k\le N}.
\]

Conversely,
\[
  G_N=D_N\,K_N\,D_N^\ast,
\tag{11}
\]
where \(D_N=L_N^{-1}\) is the first-difference matrix.

Therefore
\[
  \boxed{
  K_N\ge0\ \hbox{for every }N
  \quad\Longleftrightarrow\quad
  [g_{|j-k|}]_{1\le j,k\le N}\ge0\ \hbox{for every }N.
  }
\tag{12}
\]

The Schoenberg kernel route is exactly a Toeplitz moment problem for the
second-difference sequence \(g\).

## Generating function

Let
\[
  \mathcal L(z)=\sum_{n\ge1}\lambda_n z^n.
\]

For \(m\ge1\),
\[
  g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}.
\]

Hence the one-sided generating function is
\[
\begin{aligned}
  \mathcal G_+(z)
  &:=
  g_0+\sum_{m\ge1}g_m z^m\\
  &=
  2\lambda_1+
  \sum_{m\ge1}(\lambda_{m+1}-2\lambda_m+\lambda_{m-1})z^m\\
  &=
  \lambda_1+{(1-z)^2\over z}\mathcal L(z).
\end{aligned}
\tag{13}
\]

Since
\[
  \mathcal L(z)
  =
  z{d\over dz}\log\xi\!\left({1\over1-z}\right),
\tag{14}
\]
the increment Toeplitz gate has the explicit Euler--Gamma generator
\[
  \boxed{
  \mathcal G_+(z)
  =
  \lambda_1+
  (1-z)^2{d\over dz}\log\xi\!\left({1\over1-z}\right).
  }
\tag{15}
\]

This removes one integration from the growing Li sequence and is compatible
with the renormalization obstruction in `167`: the second-difference object
is closer to a finite boundary distribution than the original unweighted
zero divisor.

## The theorem needed

The new exact target is:

**Increment Toeplitz theorem.**  Construct the completed Euler--Gamma
sequence \(g_m\) from (9), with the pole-prime-Gamma pairing inherited from
\(\mathcal L\), and prove
\[
  [g_{|j-k|}]_{1\le j,k\le N}\ge0
  \qquad(N\ge1)
\tag{16}
\]
without assuming critical-line support.

Then (12) gives \(K_N\ge0\) for every \(N\), and the diagonal identity
\[
  K(n,n)=2\lambda_n
\]
gives
\[
  \lambda_n\ge0\qquad(n\ge1).
\]

Thus Omega7 follows by Li.

For compact A1 after A0, one still needs the stronger diagonal margin
\[
  K(n,n)\ge2\lambda_n^{\rm arch}\qquad(n\ge8),
\tag{17}
\]
or an independent bridge from increment positivity to the A1 cutoff
quantity.

## Eliminated shortcut

It is not enough to show
\[
  g_m\ge0\qquad(m\ge0).
\]

Toeplitz positivity requires all quadratic forms
\[
  \sum_{j,k=1}^{N}c_j\overline{c_k}g_{|j-k|}\ge0.
\]

Thus the increment route is a full positive-definite sequence theorem, not
coefficientwise convexity of the Li sequence.

## Status

Closed as an exact equivalence.  A1 remains open.

The next live theorem is positivity of the completed Euler--Gamma
second-difference Toeplitz matrices \( [g_{|j-k|}] \), or a stronger
archimedean-margin version sufficient for compact A1.
