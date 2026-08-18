# Diagonal balance finite certificate

## Purpose

`187_CUMULATIVE_DIAGONAL_BALANCE_FORM.md` rewrites the cumulative diagonal
induction target as
\[
\begin{aligned}
  \mathcal S_n
  &=
  \mathcal A_n
  +
  B(T_n)e^{-T_n}\mathcal H_n(T_n^-)\\
  &\quad
  -
  \int_0^{T_n}B(u)e^{-u}\mathcal R_n(u)\,du\\
  &\quad
  -
  \sum_{j=7}^{n-1}
  B(T_j)e^{-T_j}\Delta\mathcal H_n(T_j).
\end{aligned}
\tag{1}
\]

This note expands every \(B\)-term using the exact arithmetic formula
\[
  B(U)=\sum_{m\le e^U}\Lambda(m)(U-\log m)-e^U+1.
\tag{2}
\]

The result is a finite prime-power certificate for the diagonal balance
route.  It is exact for each \(n\).  Uniform positivity of this certificate
is still the missing A1 theorem.

## Abbreviations

Put
\[
  W_n(u)=e^{-u}\mathcal R_n(u),
\tag{3}
\]
\[
  Q_n=e^{-T_n}\mathcal H_n(T_n^-),
\tag{4}
\]
and, for \(7\le j\le n-1\),
\[
  \Theta_{n,j}=e^{-T_j}\Delta\mathcal H_n(T_j).
\tag{5}
\]

Then (1) becomes
\[
  \mathcal S_n
  =
  \mathcal A_n
  +
  B(T_n)Q_n
  -
  \int_0^{T_n}B(u)W_n(u)\,du
  -
  \sum_{j=7}^{n-1}B(T_j)\Theta_{n,j}.
\tag{6}
\]

## Fubini expansion of the integral term

Because the interval is compact and all sums are finite,
\[
\begin{aligned}
  \int_0^{T_n}B(u)W_n(u)\,du
  &=
  \sum_{m\le e^{T_n}}\Lambda(m)
  \int_{\log m}^{T_n}(u-\log m)W_n(u)\,du\\
  &\quad
  -
  \int_0^{T_n}(e^u-1)W_n(u)\,du .
\end{aligned}
\tag{7}
\]

The first term is finite because the prime-power part of \(B(u)\) contains
\(m\) only after \(u\ge\log m\).

## Prime-power coefficient

For \(m\le e^{T_n}\), define
\[
\boxed{
\begin{aligned}
  \Xi_{n}(m)
  &=
  (T_n-\log m)Q_n
  -
  \int_{\log m}^{T_n}(u-\log m)W_n(u)\,du\\
  &\quad
  -
  \sum_{\substack{7\le j\le n-1\\ \log m\le T_j}}
  (T_j-\log m)\Theta_{n,j}.
\end{aligned}
}
\tag{8}
\]

This coefficient is an elementary exponential-polynomial expression after
the interval partition by the cutoffs \(T_j\), because \(W_n\) is built from
Laguerre polynomials times \(e^{-u}\).

## Continuous pole coefficient

Define the continuous pole contribution
\[
\boxed{
\begin{aligned}
  \Pi_n
  &=
  (-e^{T_n}+1)Q_n
  +
  \int_0^{T_n}(e^u-1)W_n(u)\,du\\
  &\quad
  +
  \sum_{j=7}^{n-1}(e^{T_j}-1)\Theta_{n,j}.
\end{aligned}
}
\tag{9}
\]

The signs in (9) come from the pole part \(-e^U+1\) in (2) and the minus
signs in (6).

## Exact finite certificate

Combining (6)--(9) gives the finite identity
\[
\boxed{
  \mathcal S_n
  =
  \mathcal A_n
  +
  \Pi_n
  +
  \sum_{m\le e^{T_n}}\Lambda(m)\Xi_n(m).
}
\tag{10}
\]

Therefore the diagonal balance route proves A1 if
\[
\boxed{
  \mathcal A_n
  +
  \Pi_n
  +
  \sum_{m\le e^{T_n}}\Lambda(m)\Xi_n(m)
  \ge0
  \qquad(n\ge9),
}
\tag{11}
\]
together with the base condition \(C_8^\ast\ge0\).

Conversely, (11) is not a sufficient relaxation: it is exactly the same
condition as the cumulative diagonal induction inequality, written with all
prime-power and pole terms exposed.

## Interval evaluation

Let
\[
  0=a_0<a_1<\cdots<a_M=T_n
\]
be the ordered partition obtained from the cutoffs
\[
  T_7,T_8,\ldots,T_n
\]
and from the point \(\log m\) when evaluating \(\Xi_n(m)\).

On each open interval \((a_\ell,a_{\ell+1})\),
\[
  W_n(u)=e^{-u}P_{\ell,n}(u)
\tag{12}
\]
for an explicit polynomial \(P_{\ell,n}\) obtained from (2) of `187`.
Hence every integral in (8) and (9) is a finite linear combination of
\[
  \int_a^b u^r e^{-u}\,du,
  \qquad
  \int_a^b u^r\,du.
\tag{13}
\]

These have closed forms in endpoint values:
\[
  \int_a^b u^r e^{-u}\,du
  =
  r!\left[
    e^{-a}\sum_{\ell=0}^r{a^\ell\over \ell!}
    -
    e^{-b}\sum_{\ell=0}^r{b^\ell\over \ell!}
  \right],
\tag{14}
\]
and
\[
  \int_a^b u^r\,du={b^{r+1}-a^{r+1}\over r+1}.
\tag{15}
\]

Thus (11) is, for each fixed \(n\), a completely explicit finite arithmetic
certificate involving only:

- \(\Lambda(m)\) for \(m\le e^{T_n}\);
- Laguerre values at the cutoffs \(T_j\);
- elementary endpoint expressions.

## Why this is still not a proof

The coefficients \(\Xi_n(m)\) are signed.  The jump weights
\(\Theta_{n,j}\) are signed.  The pole block \(\Pi_n\) is signed.

Therefore (10) does not create positivity by exposing prime powers.  It
only shows the exact finite inequality that must be proved uniformly in
\(n\).

A proof must now establish either:

1. the exact finite certificate (11) for all \(n\ge9\);
2. a one-sided theorem forcing the weighted prime-power sum in (10) to stay
   above \(-\mathcal A_n-\Pi_n\);
3. a stronger route, such as the margin or one-sided tail gate, that bypasses
   this certificate.

## Status

Closed as a finite certificate normal form for the diagonal balance route.

A1 remains open.  The sharpened arithmetic target is the uniform inequality
(11), with the signed prime-power coefficients (8), the pole block (9), and
the base-archimedean term \(\mathcal A_n\).
