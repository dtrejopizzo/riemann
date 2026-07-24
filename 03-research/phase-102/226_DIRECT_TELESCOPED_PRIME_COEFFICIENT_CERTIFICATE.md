# Direct telescoped prime-coefficient certificate

## Purpose

`222_SIGNED_BALANCE_TELESCOPED_CERTIFICATE.md` integrates the signed
pairing once and expresses A1 through the cumulative error \(B(U)\).
`223` then shows that a symmetric envelope for \(B\) cannot close the
problem.

This note removes that unnecessary layer for the signed route.  Expanding
\(\psi(e^u)\) directly gives prime-power coefficients
\[
  \Omega_n(m)=\int_{\log m}^{T_n}e^{-u}\mathcal H_n(u)\,du.
\]
After the telescoping collapse of `219`, every \(\Omega_n(m)\) has an
explicit endpoint formula involving only \(L_{n-1}^{(1)}\) and fixed
degree-7 Laguerres.

This is now the smallest direct finite signed certificate for A1.

## Direct expansion of the signed compact pairing

The signed pairing in the cumulative diagonal route is
\[
  J_n=\int_0^{T_n}(\psi(e^u)-e^u)e^{-u}\mathcal H_n(u)\,du.
\tag{1}
\]

Since
\[
  \psi(e^u)=\sum_{m\le e^u}\Lambda(m),
\]
finite Fubini gives
\[
\boxed{
  J_n=
  \sum_{m\le e^{T_n}}\Lambda(m)\Omega_n(m)
  -
  P_n,
}
\tag{2}
\]
where
\[
\boxed{
  \Omega_n(m)=
  \int_{\log m}^{T_n}e^{-u}\mathcal H_n(u)\,du,
}
\tag{3}
\]
and
\[
\boxed{
  P_n=
  \int_0^{T_n}\mathcal H_n(u)\,du.
}
\tag{4}
\]

Thus A1 follows from
\[
\boxed{
  \mathcal A_n
  +
  \sum_{m\le e^{T_n}}\Lambda(m)\Omega_n(m)
  -
  P_n
  \ge0
  \qquad(n\ge9),
}
\tag{5}
\]
where \(\mathcal A_n\) is the base-archimedean budget of `222`.

Equation (5) is equivalent to the signed target in `222`, but it avoids
introducing \(B(U)\), its raised kernel, and the two \(B(T_j)\) jumps.

## Telescoped kernel

From `219`, put \(N=n-1\).  Then
\[
\mathcal H_n(u)=
\begin{cases}
 -L_N^{(2)}(u)+L_7^{(2)}(u)+\beta_nL_7^{(1)}(u),
   &0<u<T_7,\\
 -L_N^{(2)}(u)+\alpha_nL_7^{(2)}(u),
   &T_7<u<T_8,\\
 -L_N^{(2)}(u),
   &T_8<u<T_n,
\end{cases}
\tag{6}
\]
where
\[
  \alpha_n={n(n+1)-56\over16},
  \qquad
  \beta_n={n(n+1)-72\over16}.
\tag{7}
\]

Use the antiderivative identity
\[
\boxed{
  {d\over du}\left(e^{-u}L_m^{(\alpha-1)}(u)\right)
  =
  -e^{-u}L_m^{(\alpha)}(u).
}
\tag{8}
\]

## Prime coefficients for \(\log m\ge T_8\)

If
\[
  a=\log m\ge T_8,
\]
then only the last line of (6) contributes:
\[
\boxed{
  \Omega_n(m)
  =
  e^{-T_n}L_N^{(1)}(T_n)
  -
  e^{-a}L_N^{(1)}(a).
}
\tag{9}
\]

Thus every high prime-power coefficient is just a two-endpoint Laguerre
difference.

## Prime coefficients for \(T_7\le\log m<T_8\)

If
\[
  T_7\le a=\log m<T_8,
\]
then
\[
\boxed{
\begin{aligned}
  \Omega_n(m)
  &=
  e^{-T_n}L_N^{(1)}(T_n)
  -
  e^{-a}L_N^{(1)}(a)\\
  &\quad+
  \alpha_n
  \left[
    e^{-a}L_7^{(1)}(a)
    -
    e^{-T_8}L_7^{(1)}(T_8)
  \right].
\end{aligned}
}
\tag{10}
\]

Only a fixed degree-7 correction is added.

## Prime coefficients for \(\log m<T_7\)

If
\[
  0\le a=\log m<T_7,
\]
then
\[
\boxed{
\begin{aligned}
  \Omega_n(m)
  &=
  e^{-T_n}L_N^{(1)}(T_n)
  -
  e^{-a}L_N^{(1)}(a)\\
  &\quad+
  \left[
    e^{-a}L_7^{(1)}(a)
    -
    e^{-T_7}L_7^{(1)}(T_7)
  \right]\\
  &\quad+
  \beta_n
  \left[
    e^{-a}L_7^{(0)}(a)
    -
    e^{-T_7}L_7^{(0)}(T_7)
  \right]\\
  &\quad+
  \alpha_n
  \left[
    e^{-T_7}L_7^{(1)}(T_7)
    -
    e^{-T_8}L_7^{(1)}(T_8)
  \right].
\end{aligned}
}
\tag{11}
\]

This is again a high-degree endpoint term plus fixed degree-7 corrections.

## Pole coefficient

The pole contribution in (5) is
\[
  P_n=\int_0^{T_n}\mathcal H_n(u)\,du.
\tag{12}
\]

Because \(\mathcal H_n\) is a polynomial on each interval, \(P_n\) is an
ordinary polynomial endpoint expression:
\[
\boxed{
\begin{aligned}
  P_n
  &=
  -\int_0^{T_n}L_N^{(2)}(u)\,du\\
  &\quad+
  \int_0^{T_7}L_7^{(2)}(u)\,du
  +
  \beta_n\int_0^{T_7}L_7^{(1)}(u)\,du
  +
  \alpha_n\int_{T_7}^{T_8}L_7^{(2)}(u)\,du.
\end{aligned}
}
\tag{13}
\]

Equivalently, by expanding Laguerre polynomials into powers, each integral
is a finite rational combination of endpoint powers.  No zeros or
transcendental special functions are needed.

## Direct finite A1 target

Combining (5), (9), (10), (11), and (13), the direct signed target is:
\[
\boxed{
  \mathcal A_n
  -
  P_n
  +
  \sum_{m\le e^{T_n}}\Lambda(m)\Omega_n(m)
  \ge0
  \qquad(n\ge9),
}
\tag{14}
\]
with \(\Omega_n(m)\) given explicitly by the three cases above.

This is the same A1 theorem as `222`, but in a lower-order form:

1. no \(B\)-envelope appears;
2. no raised \(L_{n-1}^{(3)}\) kernel appears;
3. prime powers are weighted by endpoint values of \(e^{-u}L_{n-1}^{(1)}\)
   plus fixed low-degree corrections.

## What remains open

The coefficient
\[
  e^{-T_n}L_N^{(1)}(T_n)-e^{-\log m}L_N^{(1)}(\log m)
\]
still changes sign as \(m\) moves through the Laguerre oscillatory region.
Thus (14) is not automatic from monotonicity of \(\psi\) or positivity of
\(\Lambda(m)\).

The remaining theorem is a genuine signed prime-power correlation:
prime powers must be distributed so that the weighted sum in (14) stays
above \(P_n-\mathcal A_n\) for every \(n\ge9\).

## Status

Closed as the direct telescoped prime-coefficient certificate.

A1 remains open.  The signed target has been reduced from the integrated
\(B\)-form of `222` to the direct endpoint coefficient inequality (14).
