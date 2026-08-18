# Gamma_B compact base identity

## Purpose

`212_BASE_BUDGET_TELESCOPING_REDUCTION.md` reduces the large-\(n\) budget
coefficient to
\[
  \Gamma_{\mathcal B}
  =
  {1+\Delta_8^\ast\over16}
  -{3\over64}(\lambda_8^{\rm arch}-\lambda_7^{\rm arch}).
\]

This note substitutes the actual compact definition of
\(\Delta_8^\ast\).  The archimedean finite difference cancels, and the
coefficient becomes a purely compact arithmetic base comparison:
\[
\boxed{
  \Gamma_{\mathcal B}
  =
  {I_7(T_7)-I_8(T_8)\over16}.
}
\]

Thus the terminal absolute budget coefficient is positive exactly when
\[
  I_7(T_7)>I_8(T_8).
\]

This is sharper than `212`: the infinite archimedean series is gone, and
even the finite archimedean threshold is absorbed into the compact base
normalization.

## Definitions

From `156`,
\[
  I_n(T)=
  \int_0^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du,
\tag{1}
\]
and
\[
  C_n(T)
  =
  -n-I_n(T)+{3\over4}\lambda_n^{\rm arch}.
\tag{2}
\]

On the moving diagonal,
\[
  C_n^\ast=C_n(T_n),
  \qquad
  \Delta_8^\ast=C_8^\ast-C_7^\ast.
\tag{3}
\]

Therefore
\[
\begin{aligned}
  \Delta_8^\ast
  &=
  \left[-8-I_8(T_8)+{3\over4}\lambda_8^{\rm arch}\right]
  -
  \left[-7-I_7(T_7)+{3\over4}\lambda_7^{\rm arch}\right]\\
  &=
  -1+I_7(T_7)-I_8(T_8)
  +{3\over4}(\lambda_8^{\rm arch}-\lambda_7^{\rm arch}).
\end{aligned}
\tag{4}
\]

Substitute (4) into `212`:
\[
  \Gamma_{\mathcal B}
  =
  {1+\Delta_8^\ast\over16}
  -{3\over64}(\lambda_8^{\rm arch}-\lambda_7^{\rm arch}).
\tag{5}
\]

The constant \(1\) and the archimedean difference cancel, leaving
\[
\boxed{
  \Gamma_{\mathcal B}
  =
  {I_7(T_7)-I_8(T_8)\over16}.
}
\tag{6}
\]

Equivalently,
\[
\boxed{
  \Gamma_{\mathcal B}>0
  \quad\Longleftrightarrow\quad
  I_7(T_7)>I_8(T_8).
}
\tag{7}
\]

## Single signed base integral

Using
\[
  L_7^{(2)}(u)-L_6^{(2)}(u)=L_7^{(1)}(u),
\tag{8}
\]
one may write
\[
\begin{aligned}
  I_7(T_7)-I_8(T_8)
  &=
  \int_0^{T_7}E(e^u)e^{-u}
  \left(L_6^{(2)}(u)-L_7^{(2)}(u)\right)\,du\\
  &\quad
  -
  \int_{T_7}^{T_8}E(e^u)e^{-u}L_7^{(2)}(u)\,du\\
  &=
  -\int_0^{T_7}E(e^u)e^{-u}L_7^{(1)}(u)\,du
  -
  \int_{T_7}^{T_8}E(e^u)e^{-u}L_7^{(2)}(u)\,du.
\end{aligned}
\tag{9}
\]

Thus the sign of \(\Gamma_{\mathcal B}\) is a finite signed arithmetic
comparison involving only the base cutoffs \(T_7,T_8\).  It is not decided
by archimedean positivity.

## Relation to the finite Li certificate

The finite certificate for \(1\le n\le7\) proves
\[
  \lambda_n>0
  \qquad(1\le n\le7).
\]

That is a global Li statement for those indices.  It is not the same as
the compact cutoff comparison
\[
  I_7(T_7)>I_8(T_8),
\]
because the latter contains:

1. the chosen A0/base cutoffs \(T_7,T_8\);
2. incomplete compact moments rather than completed Li coefficients;
3. a comparison involving the \(n=8\) compact moment.

Therefore the finite Li certificate does not automatically prove
\(\Gamma_{\mathcal B}>0\).  A separate finite/base certificate is required
if the absolute terminal route is to use the positive-budget case.

## Exact remaining theorem

The terminal large-\(n\) budget coefficient is positive if and only if
\[
\boxed{
  I_7(T_7)>I_8(T_8).
}
\tag{10}
\]

If (10) is proved, then `208` and `210` absorb the terminal VK load for all
sufficiently large \(n\), after explicit thresholds and finite initial
checks.  The mixed off-diagonal theorem of `211` remains necessary for the
full absolute route.

If (10) fails, then \(\Gamma_{\mathcal B}\le0\), and the terminal absolute
comparison cannot be obtained from the base budget alone.

## Status

Closed as an exact compact-base identity for \(\Gamma_{\mathcal B}\).

A1 remains open.  The sign of \(\Gamma_{\mathcal B}\) is no longer an
infinite archimedean problem; it is a finite signed comparison of base
compact arithmetic moments.
