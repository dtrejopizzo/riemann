# Small-\(T_7\) prime-block elimination

## Purpose

`226_DIRECT_TELESCOPED_PRIME_COEFFICIENT_CERTIFICATE.md` gives the direct
signed coefficient formula in three prime-power ranges:
\[
  \log m<T_7,\qquad
  T_7\le\log m<T_8,\qquad
  T_8\le\log m\le T_n.
\]

The auxiliary normalization from `215` is
\[
  0<T_7\le \min(\log2,1/130).
\]

This note records the consequence for the direct signed certificate: the
first prime-power range is empty.  Thus the arithmetic sum in `226` has
only two coefficient regimes.

## No prime powers below \(T_7\)

For every prime power \(m=p^r\ge2\),
\[
  \log m\ge \log2.
\]

Under the strict auxiliary choice
\[
  0<T_7<\log2,
\tag{1}
\]
therefore
\[
\boxed{
  \{m\ge2:\Lambda(m)\ne0,\ \log m<T_7\}=\varnothing.
}
\tag{2}
\]

If one allows \(T_7=\log2\), the endpoint \(m=2\) lies at the boundary.
Since endpoint values do not affect the compact integrals but do affect
the convention for finite sums, the clean normalization for this phase is
to choose
\[
\boxed{
  0<T_7<\min(\log2,1/130).
}
\tag{3}
\]

This is compatible with every use of the small-\(T_7\) condition in `215`.

## Two-regime prime coefficient

With (3), the direct signed certificate of `226` becomes
\[
\boxed{
  \mathcal A_n-P_n
  +
  \sum_{\substack{m\le e^{T_n}\\T_7\le\log m<T_8}}
  \Lambda(m)\Omega_n^{\rm low}(m)
  +
  \sum_{\substack{m\le e^{T_n}\\T_8\le\log m}}
  \Lambda(m)\Omega_n^{\rm high}(m)
  \ge0,
}
\tag{4}
\]
where, with \(N=n-1\) and \(a=\log m\),
\[
\boxed{
\begin{aligned}
  \Omega_n^{\rm high}(m)
  &=
  e^{-T_n}L_N^{(1)}(T_n)
  -
  e^{-a}L_N^{(1)}(a),
\end{aligned}
}
\tag{5}
\]
and
\[
\boxed{
\begin{aligned}
  \Omega_n^{\rm low}(m)
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
  \right],
\end{aligned}
}
\tag{6}
\]
with
\[
  \alpha_n={n(n+1)-56\over16}.
\]

The discarded \(\log m<T_7\) coefficient from `226` contributes to no
prime-power term.

## What remains in the first interval

The interval \((0,T_7)\) does not disappear from the compact problem.  It
still contributes to the pole coefficient
\[
  P_n=\int_0^{T_n}\mathcal H_n(u)\,du.
\]

However, it is no longer an arithmetic prime-power block.  It is a fixed
endpoint-polynomial contribution depending on \(T_7\), \(T_8\), and \(n\).

Thus the only genuine arithmetic sign correlation left in the direct
certificate is over:

1. the finite low block \(2\le m<e^{T_8}\);
2. the high oscillatory block \(e^{T_8}\le m\le e^{T_n}\).

## Status

Closed as a small-\(T_7\) simplification of the direct signed certificate.

A1 remains open.  The prime-power sum has been reduced from three regimes
to two, but the high oscillatory block still requires a signed arithmetic
theorem.
