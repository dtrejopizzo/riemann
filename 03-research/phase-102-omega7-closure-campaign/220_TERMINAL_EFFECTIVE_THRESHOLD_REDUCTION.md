# Terminal effective threshold reduction

## Purpose

`207` gives an A0 bridge for the terminal Laguerre interval, `208` shows
that canonical VK cutoffs make the terminal load only logarithmic, and
`217` closes the base sign \(C_8^\ast>0\).  This note records the exact
remaining terminal threshold problem.

The outcome is:

1. the terminal interval is absorbed for all sufficiently large \(n\);
2. the effective numerical threshold is not yet computed;
3. the missing computation is now a finite, explicit certificate once the
   canonical cutoff policy and base constants are fixed.

This does not close A1, because `219` reduces the former mixed intervals
to a separate single-Laguerre weighted \(L^1\) theorem.

## Exact terminal majorant

Let
\[
  \Theta_n
  =
  {n^2\over 12(n-1)^2}\,B_{n-1}
  \log {1+T_n\over 1+T_{n-1}}
  \qquad(n\ge9).
\tag{1}
\]

By `207`,
\[
\boxed{
  \mathcal T_n(\varepsilon)\le \Theta_n.
}
\tag{2}
\]

Thus the terminal interval is controlled whenever
\[
\boxed{
  \mathcal B_n\ge \Theta_n.
}
\tag{3}
\]

Using the exact budget formula from `210`, define the finite terminal
defect
\[
\boxed{
\begin{aligned}
  \mathfrak D_n
  &=
  C_8^\ast
  +
  {n(n+1)-72\over16}\Delta_8^\ast\\
  &\quad+
  \sum_{k=8}^{n-1}
  {1\over2}
  \left({n(n+1)\over k(k+1)}-1\right)
  \left(1+{3\over4}D_k^{\rm arch}\right)
  -
  \Theta_n .
\end{aligned}
}
\tag{4}
\]

Then the terminal portion of the absolute route is exactly reduced to
\[
\boxed{
  \mathfrak D_n\ge0\qquad(n\ge9).
}
\tag{5}
\]

All quantities in (4) are finite once \(T_7,T_8,T_n\), the archimedean
formula, \(B_{n-1}\), and the finite compact constants \(C_7^\ast,C_8^\ast\)
are fixed.

## Large-\(n\) absorption is closed

By `213`,
\[
  \Gamma_{\mathcal B}
  =
  {I_7(T_7)-I_8(T_8)\over16}.
\tag{6}
\]

Choose the auxiliary base cutoff as in `215`,
\[
  0<T_7\le \min(\log2,1/130).
\tag{7}
\]
Then
\[
  I_7(T_7)>-1.
\tag{8}
\]

By `217`, A0 implies
\[
  C_8^\ast>0.
\tag{9}
\]
Using the compact definition from `215`,
\[
  C_8^\ast
  =
  -8-I_8(T_8)+{3\over4}\lambda_8^{\rm arch},
\tag{10}
\]
and \(0<\lambda_8^{\rm arch}<1\), (9) gives
\[
  I_8(T_8)<-{29\over4}.
\tag{11}
\]

Consequently
\[
  I_7(T_7)-I_8(T_8)>{25\over4},
\]
and hence
\[
\boxed{
  \Gamma_{\mathcal B}>{25\over64}.
}
\tag{12}
\]

From `210`,
\[
  \mathcal B_n
  =
  \Gamma_{\mathcal B}n^2+O(n\log n).
\tag{13}
\]
From `208`, for canonical VK cutoffs,
\[
  \Theta_n=O(\log n).
\tag{14}
\]

Combining (12)--(14),
\[
\boxed{
  \mathfrak D_n>0
  \quad\hbox{for all sufficiently large }n.
}
\tag{15}
\]

Thus the terminal interval no longer has an asymptotic obstruction after
the \(n=8\) certificate.  The only terminal work left is to make the word
"sufficiently" effective and check the finite range below that threshold.

## Exact effective certificate still required

An effective closure of the terminal interval is now the following finite
data package.

Choose and record:

1. a canonical cutoff policy \(T_n\), for example the minimal VK cutoffs of
   `208`;
2. explicit rational intervals for \(C_7^\ast\) and \(C_8^\ast\), or
   equivalently for \(I_7(T_7)\) and \(I_8(T_8)\);
3. explicit rational intervals for \(A_k=\lambda_k^{\rm arch}\) sufficient
   to enclose every \(D_k^{\rm arch}\) in the finite range;
4. an explicit all-\(n\ge N_0\) cutoff-ratio bound
   \[
     \log {1+T_n\over1+T_{n-1}}
     \le
     R_n
   \tag{16}
   \]
   with \(R_n=O(1/n)\);
5. a finite verification of
   \[
     \mathfrak D_n\ge0
     \qquad(9\le n<N_0).
   \tag{17}
   \]

Equivalently, once the intervals in items 1--4 are fixed, the certificate
is a rational interval proof that the right side of (4) is nonnegative for
every \(n\ge9\).

## Why `217` is not by itself a numerical threshold

`217` supplies a strong lower bound for \(C_8^\ast\), hence the positive
quadratic coefficient \(\Gamma_{\mathcal B}\).  However, the finite
threshold also depends on the constant and linear-size pieces in (4),
including
\[
  C_8^\ast,\qquad
  \Delta_8^\ast=C_8^\ast-C_7^\ast,
\tag{18}
\]
and on the actual cutoff ratios.  Positivity of
\(\Gamma_{\mathcal B}\) proves eventual domination, but does not produce a
numerical \(N_0\) unless those constants are enclosed.

Therefore the terminal problem is not mathematically open in the asymptotic
sense, but its effective finite certificate has not yet been executed.

## Relation to A1

Even if (5) is certified for all \(n\ge9\), A1 still requires the collapsed
single-Laguerre weighted \(L^1\) estimate isolated in
`219_MIXED_LAGUERRE_TELESCOPING_COLLAPSE.md`.

The full absolute-route target remains
\[
  \mathcal B_n
  \ge
  \mathcal M_n(\varepsilon)+\mathcal T_n(\varepsilon),
\tag{19}
\]
not merely
\[
  \mathcal B_n\ge\mathcal T_n(\varepsilon).
\tag{20}
\]

## Status

Closed as an effective-threshold reduction for the terminal interval.

The terminal asymptotic obstruction is removed: under the small-\(T_7\)
normalization, `217` gives \(\Gamma_{\mathcal B}>25/64\), while canonical
VK terminal load is \(O(\log n)\).  The remaining terminal task is a finite
rational interval certificate for (4).  A1 remains open because the
collapsed single-Laguerre \(L^1\) load from `219` is not yet controlled.
