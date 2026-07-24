# Gamma-B base finite certificate

## Purpose

`213_GAMMA_B_COMPACT_BASE_IDENTITY.md` proves
\[
  16\Gamma_{\mathcal B}=I_7(T_7)-I_8(T_8).
\tag{1}
\]

This note expands the right side into a finite prime-power certificate.
Thus the positivity of the large-\(n\) terminal budget coefficient is not
only a finite compact statement; it is an explicit finite arithmetic
inequality once \(T_7,T_8\) are fixed.

## Compact moment expansion

For \(n\ge1\), put
\[
  P_n(u)=L_{n-1}^{(2)}(u)
\]
and
\[
  I_n(T)=\int_0^T E(e^u)e^{-u}P_n(u)\,du,
  \qquad E(e^u)=\psi(e^u)-e^u.
\tag{2}
\]

Since
\[
  \psi(e^u)=\sum_{m\le e^u}\Lambda(m),
\]
Fubini on the compact interval gives
\[
\boxed{
  I_n(T)
  =
  \sum_{m\le e^T}\Lambda(m)\Phi_n(\log m,T)
  -
  \Psi_n(T),
}
\tag{3}
\]
where
\[
\boxed{
  \Phi_n(x,T)=\int_x^T e^{-u}P_n(u)\,du
  \qquad(0\le x\le T),
}
\tag{4}
\]
and
\[
\boxed{
  \Psi_n(T)=\int_0^T P_n(u)\,du.
}
\tag{5}
\]

Because \(P_n\) is a polynomial of degree \(n-1\), both \(\Phi_n\) and
\(\Psi_n\) are elementary endpoint expressions.  If
\[
  P_n(u)=\sum_{q=0}^{n-1}p_{n,q}u^q,
\tag{6}
\]
then
\[
\boxed{
  \Phi_n(x,T)
  =
  \sum_{q=0}^{n-1}p_{n,q}q!
  \left[
    e^{-x}\sum_{\ell=0}^{q}{x^\ell\over\ell!}
    -
    e^{-T}\sum_{\ell=0}^{q}{T^\ell\over\ell!}
  \right],
}
\tag{7}
\]
and
\[
\boxed{
  \Psi_n(T)
  =
  \sum_{q=0}^{n-1}p_{n,q}{T^{q+1}\over q+1}.
}
\tag{8}
\]

## Certificate for \(16\Gamma_{\mathcal B}\)

Subtract (3) at \((n,T)=(7,T_7)\) and \((8,T_8)\):
\[
\begin{aligned}
  16\Gamma_{\mathcal B}
  &=
  I_7(T_7)-I_8(T_8)\\
  &=
  \sum_{m\le e^{T_7}}\Lambda(m)
  \left[
    \Phi_7(\log m,T_7)-\Phi_8(\log m,T_8)
  \right]\\
  &\quad
  -
  \sum_{e^{T_7}<m\le e^{T_8}}\Lambda(m)
  \Phi_8(\log m,T_8)\\
  &\quad
  -\Psi_7(T_7)+\Psi_8(T_8),
\end{aligned}
\tag{9}
\]
assuming \(T_8\ge T_7\).  If the chosen base convention has \(T_8<T_7\),
the same formula is used after swapping the interval decomposition; the
identity (3) remains the authoritative form.

Thus
\[
\boxed{
  \Gamma_{\mathcal B}>0
}
\tag{10}
\]
is equivalent to the finite inequality
\[
\boxed{
\begin{aligned}
  &\sum_{m\le e^{T_7}}\Lambda(m)
  \left[
    \Phi_7(\log m,T_7)-\Phi_8(\log m,T_8)
  \right]
  -
  \sum_{e^{T_7}<m\le e^{T_8}}\Lambda(m)
  \Phi_8(\log m,T_8)\\
  &\qquad
  -\Psi_7(T_7)+\Psi_8(T_8)>0.
\end{aligned}
}
\tag{11}
\]

Every term in (11) is explicit:

1. the sums are finite;
2. \(\Lambda(m)\) is needed only for \(m\le e^{\max(T_7,T_8)}\);
3. the functions \(\Phi_7,\Phi_8,\Psi_7,\Psi_8\) are finite polynomial
   endpoint expressions.

## Equivalent single-kernel form

Using the identity from `213`,
\[
  L_7^{(2)}(u)-L_6^{(2)}(u)=L_7^{(1)}(u),
\]
one also has
\[
\boxed{
\begin{aligned}
  16\Gamma_{\mathcal B}
  &=
  -\int_0^{T_7}E(e^u)e^{-u}L_7^{(1)}(u)\,du\\
  &\quad
  -\int_{T_7}^{T_8}E(e^u)e^{-u}L_7^{(2)}(u)\,du.
\end{aligned}
}
\tag{12}
\]

Expanding (12) gives an equivalent certificate with one low interval and
one base-terminal interval.  Formula (11) is usually cleaner for direct
prime-power computation because it uses the already-defined moments
\(I_7,I_8\).

## Status

Closed as a finite certificate schema for \(\Gamma_{\mathcal B}>0\).

A1 remains open.  Proving (11) would settle only the large-\(n\) terminal
budget sign for the absolute route.  The finite terminal threshold and the
mixed off-diagonal load from `211` would still have to be closed.
