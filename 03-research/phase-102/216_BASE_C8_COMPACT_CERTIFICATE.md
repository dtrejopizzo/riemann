# Base C8 compact certificate

## Purpose

`215_BASE_CUTOFF_NORMALIZATION_GAMMA_POSITIVITY.md` shows that, after
choosing the auxiliary cutoff \(T_7\) small, the terminal budget sign
\(\Gamma_{\mathcal B}>0\) follows from the ordinary base condition
\[
  C_8^\ast=C_8(T_8)\ge0.
\]

This note expands that base condition into an exact finite prime-power
certificate.  It does not prove the certificate; it removes any ambiguity
about what remains to be checked at the base of the diagonal induction.

## Base compact quantity

By definition,
\[
  C_8(T_8)
  =
  -8-I_8(T_8)+{3\over4}A_8,
  \qquad
  A_8=\lambda_8^{\rm arch},
\tag{1}
\]
where
\[
  I_8(T_8)
  =
  \int_0^{T_8}E(e^u)e^{-u}L_7^{(2)}(u)\,du.
\tag{2}
\]

Therefore
\[
\boxed{
  C_8^\ast\ge0
  \quad\Longleftrightarrow\quad
  I_8(T_8)
  \le
  -8+{3\over4}A_8.
}
\tag{3}
\]

Equivalently,
\[
\boxed{
  -I_8(T_8)
  \ge
  8-{3\over4}A_8.
}
\tag{4}
\]

The right side is explicit and positive.  Using the certified bound from
`151`, \(0<A_8<1\), it is \(>29/4\).

## Finite prime-power expansion

Write
\[
  P_8(u)=L_7^{(2)}(u)=\sum_{q=0}^{7}p_{8,q}u^q.
\tag{5}
\]

As in `214`,
\[
  I_8(T_8)
  =
  \sum_{m\le e^{T_8}}\Lambda(m)\Phi_8(\log m,T_8)
  -
  \Psi_8(T_8),
\tag{6}
\]
where
\[
  \Phi_8(x,T)
  =
  \int_x^T e^{-u}L_7^{(2)}(u)\,du
\tag{7}
\]
and
\[
  \Psi_8(T)
  =
  \int_0^T L_7^{(2)}(u)\,du.
\tag{8}
\]

Explicitly, if (5) is used, then
\[
\boxed{
  \Phi_8(x,T)
  =
  \sum_{q=0}^{7}p_{8,q}q!
  \left[
    e^{-x}\sum_{\ell=0}^{q}{x^\ell\over\ell!}
    -
    e^{-T}\sum_{\ell=0}^{q}{T^\ell\over\ell!}
  \right],
}
\tag{9}
\]
and
\[
\boxed{
  \Psi_8(T)
  =
  \sum_{q=0}^{7}p_{8,q}{T^{q+1}\over q+1}.
}
\tag{10}
\]

Substituting (6) into (4), the base certificate is
\[
\boxed{
  \Psi_8(T_8)
  -
  \sum_{m\le e^{T_8}}\Lambda(m)\Phi_8(\log m,T_8)
  \ge
  8-{3\over4}A_8.
}
\tag{11}
\]

This is a finite arithmetic inequality once \(T_8\) is fixed.

## Relation to Li positivity at \(n=8\)

The base compact certificate is not the same as proving \(\lambda_8\ge0\).
The exact tail identity from `150` gives
\[
  C_8(T_8)
  =
  \lambda_8
  -
  {1\over4}A_8
  -
  R_8(T_8).
\tag{12}
\]

A0 gives only
\[
  |R_8(T_8)|\le {1\over4}A_8.
\tag{13}
\]
Therefore a finite proof of \(\lambda_8\ge0\) would not by itself imply
\(C_8(T_8)\ge0\).  A sufficient finite alternative is the strong base
margin
\[
\boxed{
  \lambda_8\ge {1\over2}A_8,
}
\tag{14}
\]
because then (12)--(13) imply \(C_8(T_8)\ge0\).

Thus the base can be closed in either of two finite ways:

1. prove the compact certificate (11) directly;
2. prove the finite strong margin (14).

Both are finite statements, but neither is currently supplied by the
finite \(1\le n\le7\) certificate.

## Status

Closed as the exact finite certificate for the base condition
\(C_8^\ast\ge0\).

A1 remains open.  In the absolute-route branch, the terminal budget sign is
now reduced to this base certificate, while the mixed off-diagonal load of
`211` remains a separate uniform theorem.
