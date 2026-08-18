# Lobe-block partial summation gate

## Purpose

`298_LAGUERRE_LOBE_BLOCK_COMPENSATION_GATE.md` identifies the minimal
direct A1 unit after termwise positivity fails: oriented compensation among
Laguerre sign lobes.

This note rewrites each lobe block by exact partial summation.  It shows
that the remaining arithmetic input is an oriented Chebyshev-error theorem
on each lobe, not an absolute estimate for the error.

## Lobe block

Keep the notation of `298`:
\[
  G_N(u)=e^{-u}L_N^{(1)}(u),\qquad N=n-1,
\]
\[
  \omega_n(u)=G_N(T_n)-G_N(u),
\]
and let
\[
  [a,b]\subset[T_8,T_n]
\]
be one sign lobe for \(\omega_n\).  The corresponding prime-power block is
\[
\boxed{
  H_{[a,b)}
  =
  \sum_{a\le\log m<b}\Lambda(m)\omega_n(\log m).
}
\tag{1}
\]

Endpoint conventions only change finite boundary terms.  The convention
above is left-closed and right-open.

## Local Chebyshev step function

Define
\[
\boxed{
  \Theta_a(u)=\sum_{a\le\log m<u}\Lambda(m)
  =
  \psi(e^u)-\psi(e^a-),
  \qquad a\le u\le b.
}
\tag{2}
\]

Then
\[
  H_{[a,b)}=\int_{[a,b)}\omega_n(u)\,d\Theta_a(u).
\]

Since
\[
  G_N'(u)=-e^{-u}L_N^{(2)}(u),
  \qquad
  \omega_n'(u)=e^{-u}L_N^{(2)}(u),
\tag{3}
\]
Stieltjes integration by parts gives
\[
\boxed{
  H_{[a,b)}
  =
  \Theta_a(b)\omega_n(b)
  -
  \int_a^b\Theta_a(u)e^{-u}L_N^{(2)}(u)\,du.
}
\tag{4}
\]

If \(b\) is a zero of \(\omega_n\), as in the coarsest sign partition
except possibly at \(b=T_n\), the boundary term vanishes.

## Main term plus Chebyshev discrepancy

Write
\[
  \Theta_a(u)=(e^u-e^a)+\mathcal E_a(u),
\]
where
\[
\boxed{
  \mathcal E_a(u)
  =
  \psi(e^u)-e^u-\left(\psi(e^a-)-e^a\right).
}
\tag{5}
\]

Then (4) becomes
\[
\boxed{
\begin{aligned}
  H_{[a,b)}
  &=
  H_{[a,b)}^{\rm main}
  +
  H_{[a,b)}^{\rm err},                                      \\
  H_{[a,b)}^{\rm main}
  &=
  (e^b-e^a)\omega_n(b)
  -
  \int_a^b(e^u-e^a)e^{-u}L_N^{(2)}(u)\,du,                  \\
  H_{[a,b)}^{\rm err}
  &=
  \mathcal E_a(b)\omega_n(b)
  -
  \int_a^b\mathcal E_a(u)e^{-u}L_N^{(2)}(u)\,du.
\end{aligned}
}
\tag{6}
\]

The main part is continuous and explicit.  The arithmetic part is exactly
the signed Chebyshev discrepancy against the lobe kernel
\[
  e^{-u}L_N^{(2)}(u).
\]

## Oriented lobe condition

Summing (6) over the sign-lobe partition of `298`, the direct certificate
\[
  B_n^{\rm base}+H_n\ge0
\]
is equivalent to
\[
\boxed{
  B_n^{\rm base}
  +
  \sum_j H_{n,j}^{\rm main}
  +
  \sum_j H_{n,j}^{\rm err}
  \ge0.
}
\tag{7}
\]

Thus the missing theorem may be stated as the oriented discrepancy lower
bound
\[
\boxed{
  \sum_j H_{n,j}^{\rm err}
  \ge
  -B_n^{\rm base}-\sum_jH_{n,j}^{\rm main}.
}
\tag{8}
\]

This is the lobe-block partial-summation form of direct A1.

## Why absolute Chebyshev bounds are still insufficient

An estimate of the form
\[
  |\mathcal E_a(u)|\le W_a(u)
\]
gives at best
\[
  H_{[a,b)}^{\rm err}
  \ge
  -|\mathcal E_a(b)\omega_n(b)|
  -
  \int_a^b W_a(u)e^{-u}|L_N^{(2)}(u)|\,du.
\]

After summing lobes, this is an absolute-load estimate.  The previous
absolute routes show that such estimates have the wrong bulk scale unless
they are far stronger than known PNT-type inputs.  Therefore (8) must be
proved as an oriented theorem for the actual signs of the Chebyshev error
relative to the Laguerre lobe kernels.

## Relation to previous forms

- `231` gives a high-block partial summation form for the weighted
  correlation with \(\Lambda(m)/m\).
- This note gives the corresponding lobe-level partial summation for the
  direct coefficient sum with weights \(\Lambda(m)\).
- `298` supplies the sign partition; this note supplies the Chebyshev-error
  representation on each sign block.

All three are equivalent coordinatizations of the same compact A1 signed
core.  None proves A1 without the oriented discrepancy inequality (8).

## Status

Closed as the lobe-block partial-summation normal form.  A1 remains open
until the oriented Chebyshev-error inequality (8), the equivalent
tail-margin gate \(s_n\ge d_n\), or another Fejer/Herglotz/RDI route is
proved.
