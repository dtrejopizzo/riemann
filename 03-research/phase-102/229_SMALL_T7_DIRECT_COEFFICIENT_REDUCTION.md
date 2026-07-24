# Small-\(T_7\) direct coefficient reduction

## Purpose

`226_DIRECT_TELESCOPED_PRIME_COEFFICIENT_CERTIFICATE.md` gives the current
direct signed A1 target
\[
  \mathcal A_n-P_n+\sum_{m\le e^{T_n}}\Lambda(m)\Omega_n(m)\ge0.
\tag{1}
\]

`227_SMALL_T7_PRIME_BLOCK_ELIMINATION.md` removes the empty
\(\log m<T_7\) branch, and `228_HIGH_BLOCK_LAGUERRE_CORRELATION_FORM.md`
isolates the high block.  This note combines those reductions into one
compressed formula.

Use the strict small auxiliary cutoff normalization compatible with
`215_BASE_CUTOFF_NORMALIZATION_GAMMA_POSITIVITY.md`,
\[
  0<T_7< \min(\log2,1/130),
\tag{2}
\]
to remove the empty low-prime branch in `226`.  Since no prime power
\(m\ge2\) has \(\log m<T_7\), the only prime-power corrections occur in
the fixed base window \(T_7\le\log m<T_8\).

Thus (1) reduces to a global Laguerre--Chebyshev transform plus a finite
base correction.

## No prime powers below \(T_7\)

For \(m\ge2\),
\[
  \log m\ge\log2>T_7.
\tag{3}
\]
The case \(\log m<T_7\) in `226` therefore contributes nothing to the
prime-power sum, because \(m=1\) has \(\Lambda(1)=0\).

Put
\[
  N=n-1,\qquad X_n=e^{T_n},
\tag{4}
\]
and define the strict base-window Chebyshev sums
\[
\boxed{
  \Psi_8^-=\sum_{\substack{m\ge2\\ \log m<T_8}}\Lambda(m),
}
\tag{5}
\]
\[
\boxed{
  \mathfrak L_8
  =
  \sum_{\substack{m\ge2\\ \log m<T_8}}
  {\Lambda(m)\over m}L_7^{(1)}(\log m).
}
\tag{6}
\]

The strict inequality is used because the endpoint \(a=T_8\) belongs to
the high-interval formula in `226`; if \(T_8\) is not itself the logarithm
of a prime power, strict and non-strict conventions coincide.

## Collapsed prime-power sum

From `226`, for every prime power with \(\log m\ge T_8\),
\[
  \Omega_n(m)
  =
  e^{-T_n}L_N^{(1)}(T_n)
  -
  {1\over m}L_N^{(1)}(\log m).
\tag{7}
\]

For \(T_7\le\log m<T_8\), the only additional term is
\[
  \alpha_n
  \left[
    {1\over m}L_7^{(1)}(\log m)
    -
    e^{-T_8}L_7^{(1)}(T_8)
  \right],
\tag{8}
\]
where
\[
  \alpha_n={n(n+1)-56\over16}.
\tag{9}
\]

Consequently
\[
\boxed{
\begin{aligned}
  \sum_{m\le X_n}\Lambda(m)\Omega_n(m)
  &=
  e^{-T_n}L_N^{(1)}(T_n)\psi(X_n)\\
  &\quad-
  \sum_{m\le X_n}{\Lambda(m)\over m}L_N^{(1)}(\log m)\\
  &\quad+
  \alpha_n
  \left(
    \mathfrak L_8
    -
    e^{-T_8}L_7^{(1)}(T_8)\Psi_8^-
  \right).
\end{aligned}
}
\tag{10}
\]

All non-terminal corrections in the prime-power sum are now finite,
fixed-base data independent of the moving upper cutoff except through the
quadratic multiplier \(\alpha_n\).

## Closed form for \(P_n\)

The pole polynomial from `226` is
\[
\begin{aligned}
  P_n
  &=
  -\int_0^{T_n}L_N^{(2)}(u)\,du\\
  &\quad+
  \int_0^{T_7}L_7^{(2)}(u)\,du
  +
  \beta_n\int_0^{T_7}L_7^{(1)}(u)\,du
  +
  \alpha_n\int_{T_7}^{T_8}L_7^{(2)}(u)\,du,
\end{aligned}
\tag{11}
\]
where
\[
  \beta_n={n(n+1)-72\over16}.
\tag{12}
\]

Using
\[
  {d\over du}L_{r+1}^{(\alpha-1)}(u)=-L_r^{(\alpha)}(u),
\tag{13}
\]
and the endpoint values
\[
  L_n^{(1)}(0)=n+1,\qquad L_8^{(1)}(0)=9,\qquad L_8^{(0)}(0)=1,
\tag{14}
\]
we get
\[
\boxed{
\begin{aligned}
  P_n
  &=
  L_n^{(1)}(T_n)-(n+1)\\
  &\quad+
  9-L_8^{(1)}(T_7)
  +
  \beta_n\left(1-L_8^{(0)}(T_7)\right)\\
  &\quad+
  \alpha_n\left(L_8^{(1)}(T_7)-L_8^{(1)}(T_8)\right).
\end{aligned}
}
\tag{15}
\]

Thus the continuous pole term is also an endpoint expression plus fixed
degree-8 data.

## Reduced direct A1 certificate

Substituting (10) and (15) into (1), compact A1 for \(n\ge9\) follows from
\[
\boxed{
\begin{aligned}
  0
  &\le
  \mathfrak C_n^{\rm dir}\\
  &:=
  \mathcal A_n
  -
  P_n\\
  &\quad+
  e^{-T_n}L_{n-1}^{(1)}(T_n)\psi(e^{T_n})\\
  &\quad-
  \sum_{m\le e^{T_n}}{\Lambda(m)\over m}
  L_{n-1}^{(1)}(\log m)\\
  &\quad+
  \alpha_n
  \left(
    \mathfrak L_8
    -
    e^{-T_8}L_7^{(1)}(T_8)\Psi_8^-
  \right),
\end{aligned}
}
\tag{16}
\]
with \(P_n\) given by (15).

This is equivalent to the direct certificate of `226` under the strict
small-\(T_7\) normalization of `227`.  It has only one moving prime-power
sum:
\[
\boxed{
  \sum_{m\le e^{T_n}}{\Lambda(m)\over m}
  L_{n-1}^{(1)}(\log m).
}
\tag{17}
\]

All other arithmetic data are either endpoint values at \(T_n\) or fixed
base-window sums below \(e^{T_8}\).

## What remains open

The transform (17) is still signed.  Its kernel
\[
  L_{n-1}^{(1)}(\log m)
\]
oscillates through the Laguerre bulk, and the weights \(\Lambda(m)/m\) are
positive.  Therefore (16) is not a consequence of monotonicity of
\(\psi\), nor of a symmetric PNT-size envelope.

The remaining theorem is a signed Chebyshev--Laguerre correlation:
\[
  \sum_{m\le e^{T_n}}{\Lambda(m)\over m}
  L_{n-1}^{(1)}(\log m)
\]
must be controlled sharply enough, with its sign, to make
\(\mathfrak C_n^{\rm dir}\ge0\) for every \(n\ge9\).

## Status

Closed as a small-\(T_7\) reduction of the direct signed certificate.

A1 remains open.  The moving arithmetic content has been isolated to the
single signed transform (17), plus fixed base-window constants.
