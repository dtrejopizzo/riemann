# Single-transform fixed-cutoff generator

## Purpose

`230_SINGLE_TRANSFORM_A1_FRONTIER.md` reduces compact A1 to a signed
inequality for
\[
  S_n(T)=
  \sum_{m\le e^T}{\Lambda(m)\over m}L_{n-1}^{(1)}(\log m).
\]

This note packages \(S_n(T)\) into a fixed-cutoff generating function.  It
is the single-transform version of the fixed-cutoff generators in `125`
and `149`.

The output is exact, but it is still not a proof of A1, because A1 uses the
moving cutoffs \(T=T_n\).

## Generating function for \(S_n(T)\)

For \(|z|<1\),
\[
  \sum_{n\ge1}L_{n-1}^{(1)}(u)z^n
  =
  {z\over(1-z)^2}
  \exp\!\left(-{uz\over1-z}\right).
\tag{1}
\]

Therefore, for fixed \(T>0\),
\[
\boxed{
\begin{aligned}
  \mathcal S_T(z)
  &:=
  \sum_{n\ge1}S_n(T)z^n\\
  &=
  {z\over(1-z)^2}
  \sum_{m\le e^T}{\Lambda(m)\over m}
  \exp\!\left(-{\log m\,z\over1-z}\right)\\
  &=
  {z\over(1-z)^2}
  \sum_{m\le e^T}{\Lambda(m)\over m^{1/(1-z)}}.
\end{aligned}
}
\tag{2}
\]

Thus the moving arithmetic transform is a coefficient of a finite
Dirichlet polynomial composed with \(s=(1-z)^{-1}\).

## Generating function for the continuous side

For fixed \(T\), the right side in `230` is
\[
  R_n(T)
  =
  E(e^T)e^{-T}L_{n-1}^{(1)}(T)
  +
  1-L_n^{(0)}(T)
  +
  {3\over4}\lambda_n^{\rm arch}
  -
  n.
\tag{3}
\]

The first term has generating function
\[
\boxed{
  E(e^T)e^{-T}
  {z\over(1-z)^2}
  \exp\!\left(-{Tz\over1-z}\right).
}
\tag{4}
\]

Using
\[
  \sum_{n\ge0}L_n^{(0)}(T)z^n
  =
  {1\over1-z}\exp\!\left(-{Tz\over1-z}\right),
\tag{5}
\]
we get
\[
\boxed{
  \sum_{n\ge1}\left(1-L_n^{(0)}(T)\right)z^n
  =
  {1\over1-z}
  \left[
    1-\exp\!\left(-{Tz\over1-z}\right)
  \right].
}
\tag{6}
\]

Finally,
\[
  \sum_{n\ge1}nz^n={z\over(1-z)^2},
\tag{7}
\]
and the archimedean generating function is the one recorded in `125`.

Thus the fixed-\(T\) coefficient form of A1 is
\[
\boxed{
  [z^n]\mathcal D_T(z)\ge0,
}
\tag{8}
\]
where
\[
\boxed{
\begin{aligned}
  \mathcal D_T(z)
  &:=
  E(e^T)e^{-T}
  {z\over(1-z)^2}
  \exp\!\left(-{Tz\over1-z}\right)\\
  &\quad+
  {1\over1-z}
  \left[
    1-\exp\!\left(-{Tz\over1-z}\right)
  \right]\\
  &\quad+
  {3\over4}\mathcal A(z)
  -
  {z\over(1-z)^2}
  -
  \mathcal S_T(z).
\end{aligned}
}
\tag{9}
\]

Here
\[
  \mathcal A(z)=\sum_{n\ge1}\lambda_n^{\rm arch}z^n.
\tag{10}
\]

## Relation to fixed-cutoff A1

For every fixed \(T\),
\[
  [z^n]\mathcal D_T(z)
  =
  C_n(T).
\tag{11}
\]

Therefore coefficient positivity of \(\mathcal D_T\) for all \(n\ge8\)
would prove compact positivity at that fixed cutoff.

However, A1 needs
\[
  [z^n]\mathcal D_{T_n}(z)\ge0
  \qquad(n\ge8),
\tag{12}
\]
where the cutoff changes with the coefficient index.  This is not
coefficient positivity of a single holomorphic function.

## Exact remaining fixed-cutoff-to-moving gate

The fixed-cutoff route can close A1 only if one proves at least one of the
following.

1. Uniform coefficient positivity:
   \[
     [z^n]\mathcal D_T(z)\ge0
     \qquad(n\ge8,\ T\in\mathcal T_n),
   \]
   for a cutoff range containing every admissible \(T_n\).
2. A signed monotone-transfer theorem moving from a fixed cutoff to
   \(T_n\) without losing the Laguerre sign.
3. A moving-cutoff positive transform whose \(n\)-th coefficient is
   \([z^n]\mathcal D_{T_n}(z)\).

Without one of these, (9) is only a normal form.

## Status

Closed as the single-transform fixed-cutoff generator.

A1 remains open.  The missing theorem is coefficient positivity along the
moving cutoff \(T=T_n\), or an equivalent signed/RH-strength route.
