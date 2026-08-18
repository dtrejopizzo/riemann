# Laguerre core sign partition

## Purpose

A1 is a signed compact inequality.  This note records the exact sign
partition of its kernel.  The useful point is that the derivative kernel
collapses to one generalized Laguerre polynomial, so the compact core has a
canonical lobe decomposition.

This does not close A1 by itself.  It removes one layer of algebraic
complexity and states the precise lobe-balance theorem that would close it.

## Kernel collapse

Put
\[
  u=\log y,\qquad
  E(e^u)=\psi(e^u)-e^u,
\]
and
\[
  f_{n,0}(y)=y^{-1}L_{n-1}^{(1)}(\log y).
\]

Then
\[
  f'_{n,0}(y)\,dy
  =
  e^{-u}
  \left[
    {d\over du}L_{n-1}^{(1)}(u)-L_{n-1}^{(1)}(u)
  \right]du.
\tag{1}
\]

The Laguerre derivative identity is
\[
  {d\over du}L_{m}^{(\alpha)}(u)=-L_{m-1}^{(\alpha+1)}(u),
\tag{2}
\]
and the adjacent-parameter identity is
\[
  L_m^{(\alpha)}(u)=L_m^{(\alpha+1)}(u)-L_{m-1}^{(\alpha+1)}(u).
\tag{3}
\]

With \(m=n-1\) and \(\alpha=1\), (2)--(3) give
\[
  {d\over du}L_{n-1}^{(1)}(u)-L_{n-1}^{(1)}(u)
  =
  -L_{n-2}^{(2)}(u)-L_{n-1}^{(1)}(u)
  =
  -L_{n-1}^{(2)}(u).
\tag{4}
\]

Therefore
\[
  \boxed{
  f'_{n,0}(y)\,dy=-e^{-u}L_{n-1}^{(2)}(u)\,du.
  }
\tag{5}
\]

Consequently, for any cutoff \(T\),
\[
  K_n(T)
  =
  -n+\int_1^{e^T}E(y)f'_{n,0}(y)\,dy
  =
  -n-\int_0^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\tag{6}
\]

A1 is thus equivalent to
\[
  \boxed{
  \int_0^{T_n}E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \le
  {3\over4}\lambda_n^{\rm arch}-n
  \qquad(n\ge8).
  }
\tag{7}
\]

This is the compact signed inequality in its simplest Laguerre-kernel form.

## Canonical lobe partition

For \(\alpha>-1\), \(L_{n-1}^{(\alpha)}\) has \(n-1\) simple positive zeros.
Let the zeros of \(L_{n-1}^{(2)}\) be
\[
  0<\tau_{n,1}<\tau_{n,2}<\cdots<\tau_{n,n-1}.
\]

Set
\[
  \tau_{n,0}=0,\qquad \tau_{n,n}=T_n,
\]
with the convention that if \(T_n\) falls before the last zero, only the
zeros below \(T_n\) are used.  On each open lobe
\[
  I_{n,j}=(\tau_{n,j},\tau_{n,j+1}),
\]
the sign of \(L_{n-1}^{(2)}\) is constant.  Since
\[
  L_{n-1}^{(2)}(0)=\binom{n+1}{n-1}>0,
\]
the signs alternate:
\[
  \mathrm{sgn}\,L_{n-1}^{(2)}(u)=(-1)^j
  \qquad (u\in I_{n,j}).
\tag{8}
\]

Define the positive lobe weights
\[
  d\nu_n(u)=e^{-u}\left|L_{n-1}^{(2)}(u)\right|\,du
\]
and the lobe averages
\[
  M_{n,j}
  =
  \int_{I_{n,j}} E(e^u)\,d\nu_n(u).
\tag{9}
\]

Then
\[
  \int_0^{T_n}E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  =
  \sum_j (-1)^j M_{n,j}.
\tag{10}
\]

Thus A1 is exactly the alternating lobe inequality
\[
  \boxed{
  \sum_j (-1)^jM_{n,j}
  \le
  {3\over4}\lambda_n^{\rm arch}-n.
  }
\tag{11}
\]

This is not an absolute estimate.  It preserves the signed interaction
between the Chebyshev error and the oscillatory Laguerre kernel.

## Pairing adjacent lobes

A natural non-tautological strengthening is an adjacent-lobe compensation
law.  Pair the positive and negative lobes by
\[
  P_{n,k}=M_{n,2k}-M_{n,2k+1}.
\]

If the terminal unpaired lobe is denoted by \(U_n\), then (11) becomes
\[
  \sum_k P_{n,k}+U_n
  \le
  {3\over4}\lambda_n^{\rm arch}-n.
\tag{12}
\]

Therefore A1 would follow from the following purely compact theorem.

### Adjacent lobe theorem

For the A0 cutoffs \(T_n\), prove
\[
  \sum_k P_{n,k}+U_n
  \le
  {3\over4}\lambda_n^{\rm arch}-n
  \qquad(n\ge8),
\tag{13}
\]
where each \(P_{n,k}\) is formed before taking any absolute value.

This theorem is equivalent to A1 if all lobes below \(T_n\) are included.
It becomes a genuine route only if each \(P_{n,k}\), or a controlled block
of such pairs, is bounded from the Euler--Gamma data without substituting
Li positivity.

## Stieltjes version of the same partition

Because
\[
  E(e^u)=\psi(e^u)-e^u,
\]
one can also write the compact core as a Stieltjes pairing of the continuous
pole mass against the prime-power jumps.  With
\[
  \Phi_n(u)=e^{-u}L_{n-1}^{(2)}(u),
\]
equation (6) says
\[
  K_n(T)=-n-\int_0^T(\psi(e^u)-e^u)\Phi_n(u)\,du.
\tag{14}
\]

Integrating the \(\psi\)-part by parts on each lobe produces boundary terms
at prime powers and at Laguerre zeros.  The Laguerre-zero boundary terms are
canonical: they are the only places where the sign of the kernel may change.
Hence any local proof that splits the compact core must either:

1. pair adjacent Laguerre lobes before estimating;
2. prove a one-sided Stieltjes inequality for the cumulative prime-power
   mass on each signed block; or
3. replace the lobe partition by a stronger global positivity structure
   such as the boundary-measure, Pick/Stieltjes, Hermite--Biehler, or
   heat-flow gates already recorded in the phase.

## Status

Closed as a kernel normal form.  The new exact identity is
\[
  {d\over du}L_{n-1}^{(1)}(u)-L_{n-1}^{(1)}(u)
  =
  -L_{n-1}^{(2)}(u).
\]

The open mathematical load is now sharper: prove the adjacent-lobe
compensation theorem (13), or replace it by one of the stronger global
positivity gates.  No conclusion about A1 is declared here without that
signed compensation theorem.
