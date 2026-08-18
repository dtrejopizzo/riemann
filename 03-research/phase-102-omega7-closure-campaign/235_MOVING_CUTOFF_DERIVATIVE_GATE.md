# Moving-cutoff derivative gate

## Purpose

`233_SINGLE_TRANSFORM_FIXED_CUTOFF_GENERATOR.md` shows that fixed-cutoff
coefficient positivity is not enough for A1, because A1 needs the diagonal
values \(C_n(T_n)\).

This note computes the exact derivative of \(C_n(T)\) with respect to the
cutoff.  The result is a sharp moving-cutoff gate:
\[
  {d\over dT}C_n(T)
  =
  -(\psi(e^T)-e^T)e^{-T}L_{n-1}^{(2)}(T)
\]
away from prime-power jumps, and \(C_n(T)\) is continuous at those jumps.

## Compact cutoff form

From `230`, for fixed \(T\),
\[
\boxed{
  C_n(T)
  =
  -n
  +
  E(e^T)e^{-T}L_{n-1}^{(1)}(T)
  -
  S_n(T)
  +
  \int_0^T L_{n-1}^{(1)}(u)\,du
  +
  {3\over4}\lambda_n^{\rm arch},
}
\tag{1}
\]
where
\[
  E(e^T)=\psi(e^T)-e^T
\]
and
\[
  S_n(T)=\sum_{m\le e^T}{\Lambda(m)\over m}
  L_{n-1}^{(1)}(\log m).
\]

## Continuity at prime-power jumps

At a prime-power point \(T=\log m\), \(E(e^T)\) jumps by \(\Lambda(m)\),
so the boundary term
\[
  E(e^T)e^{-T}L_{n-1}^{(1)}(T)
\]
jumps by
\[
  {\Lambda(m)\over m}L_{n-1}^{(1)}(\log m).
\]

The transform \(S_n(T)\) jumps by the same amount.  Since it appears in
(1) with a minus sign, the two jumps cancel:
\[
\boxed{
  \Delta C_n(\log m)=0.
}
\tag{2}
\]

Thus \(C_n(T)\) is continuous as a function of \(T\).

## Derivative between jumps

On an interval with no prime-power logarithm, \(S_n(T)\) is constant and
\[
  {d\over dT}E(e^T)=-e^T.
\]

Differentiating (1), the continuous main terms cancel and
\[
\begin{aligned}
  {d\over dT}C_n(T)
  &=
  E(e^T)e^{-T}
  \left[
    {d\over dT}L_{n-1}^{(1)}(T)-L_{n-1}^{(1)}(T)
  \right].
\end{aligned}
\]

Since
\[
  {d\over dT}L_{n-1}^{(1)}(T)=-L_{n-2}^{(2)}(T)
\]
and
\[
  L_{n-1}^{(2)}(T)=L_{n-1}^{(1)}(T)+L_{n-2}^{(2)}(T),
\]
we obtain
\[
\boxed{
  {d\over dT}C_n(T)
  =
  -E(e^T)e^{-T}L_{n-1}^{(2)}(T).
}
\tag{3}
\]

## Transfer formula

For any \(0<U<V\),
\[
\boxed{
  C_n(V)-C_n(U)
  =
  -\int_U^V
  (\psi(e^T)-e^T)e^{-T}L_{n-1}^{(2)}(T)\,dT.
}
\tag{4}
\]

The integral is ordinary because \(C_n\) is continuous and the
prime-power jumps cancel.

## Consequence for fixed-cutoff positivity

Suppose one proves \(C_n(U)\ge0\) at some fixed or convenient cutoff \(U\).
To transfer this to \(T_n\), one still needs
\[
\boxed{
  \int_U^{T_n}
  (\psi(e^T)-e^T)e^{-T}L_{n-1}^{(2)}(T)\,dT
  \le
  C_n(U).
}
\tag{5}
\]

A monotonicity theorem would require a sign statement for
\[
  (\psi(e^T)-e^T)L_{n-1}^{(2)}(T).
\]

No such sign statement follows from A0 or VK size estimates.  A symmetric
bound again gives an absolute \(L^1\) Laguerre load and falls under the
bulk obstructions of `221`, `223`, and `232`.

## Status

Closed as the exact moving-cutoff derivative gate.

A1 remains open.  Fixed-cutoff positivity can transfer to the moving cutoff
only through the signed integral condition (5), a one-sided tail theorem,
or another RH-strength route.
