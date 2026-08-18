# Weighted zero-divisor measure gate

## Purpose

`172_SCHOENBERG_INCREMENT_TOEPLITZ_GATE.md` reduces the Schoenberg kernel
route to Toeplitz positivity of the second-difference sequence
\[
  g_0=2\lambda_1,\qquad
  g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}.
\]

This note identifies the zero-side meaning of \(g_m\).  On the critical-line
model, \(g_m\) is the moment sequence of the transformed zero divisor
weighted by
\[
  |1-w_\rho|^2.
\]

This is the first finite-measure version of the Li boundary route that
matches the renormalization obstruction in `167`.

## Critical-line calculation

Let
\[
  w_\rho=1-{1\over\rho}.
\]

On the critical line,
\[
  |w_\rho|=1,\qquad \overline{w_\rho}=w_\rho^{-1}.
\]

For \(m\ge1\), using the paired Li formula,
\[
\begin{aligned}
  g_m
  &=
  \lambda_{m+1}-2\lambda_m+\lambda_{m-1} \\
  &=
  \sum_\rho
  \left[
    (1-w_\rho^{m+1})-2(1-w_\rho^m)+(1-w_\rho^{m-1})
  \right] \\
  &=
  \sum_\rho
  \left[
    2w_\rho^m-w_\rho^{m+1}-w_\rho^{m-1}
  \right] \\
  &=
  \sum_\rho
  |1-w_\rho|^2 w_\rho^m.
\end{aligned}
\tag{1}
\]

For \(m=0\),
\[
  g_0=2\lambda_1
  =
  \sum_\rho(2-w_\rho-w_\rho^{-1})
  =
  \sum_\rho |1-w_\rho|^2.
\tag{2}
\]

Thus, in the boundary model,
\[
  \boxed{
  g_m=\int_{\partial\mathbb D}\zeta^m\,d\nu_{\rm wt}(\zeta),
  \qquad
  d\nu_{\rm wt}
  =
  \sum_\rho |1-w_\rho|^2\delta_{w_\rho}.
  }
\tag{3}
\]

The Toeplitz positivity of `172` is exactly positivity of this weighted
boundary measure.

## Why the weighting is finite

As \(|\rho|\to\infty\),
\[
  w_\rho=1-{1\over\rho},
\]
so
\[
  |1-w_\rho|^2={1\over|\rho|^2}.
\tag{4}
\]

The standard zero-counting bound
\[
  N(T)=O(T\log T)
\]
implies
\[
  \sum_\rho {1\over|\rho|^2}<\infty.
\tag{5}
\]

Therefore the weighted divisor in (3) has finite total mass.  This is the
precise repair of the finite-measure obstruction in
`167_LI_MOMENT_RENORMALIZATION_OBSTRUCTION.md`.

## Non-circular theorem needed

The calculation above assumes \(|w_\rho|=1\).  It is therefore only a model,
not a proof.

The valid theorem is:

**Completed weighted-divisor theorem.**  Construct the sequence \(g_m\) from
the completed Euler--Gamma generator
\[
  \mathcal G_+(z)
  =
  \lambda_1+{(1-z)^2\over z}\mathcal L(z)
\]
and prove, without assuming critical-line support, that
\[
  [g_{|j-k|}]_{1\le j,k\le N}\ge0
  \qquad(N\ge1).
\tag{6}
\]

By Herglotz, (6) gives a finite positive measure \(\nu_{\rm wt}\) on
\(\partial\mathbb D\) with moments \(g_m\).  If the associated Cauchy or
Carathéodory transform has singularities exactly at the transformed
nontrivial zeros with the weighted residues prescribed by (1), then every
zero with nonzero weight must satisfy
\[
  |w_\rho|=1.
\]

Since \(w_\rho=1\) would correspond to \(\rho=\infty\), no finite zero is
lost by the weight.  Hence critical-line support follows.

## Relation to Omega7

The implication chain is:
\[
  \hbox{weighted Toeplitz positivity}
  \Longrightarrow
  \hbox{positive finite weighted boundary measure}
  \Longrightarrow
  |w_\rho|=1\ \hbox{for every nontrivial zero}
  \Longrightarrow
  RH
  \Longrightarrow
  \lambda_n\ge0.
\]

Equivalently, by `172`, weighted Toeplitz positivity implies positivity of
the Schoenberg kernel
\[
  K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|},
\]
and its diagonal gives
\[
  \lambda_n\ge0.
\]

For the compact A1 assembly, the stronger archimedean margin is still
needed if one insists on closing A1 through the A0 cutoff budget rather than
through the global Li/RH route.

## Status

Closed as a zero-side interpretation and exact target.  A1 remains open.

The sharpened global target is now positivity of the completed
Euler--Gamma weighted-divisor moment sequence \(g_m\), together with
non-circular identification of its singularities.
