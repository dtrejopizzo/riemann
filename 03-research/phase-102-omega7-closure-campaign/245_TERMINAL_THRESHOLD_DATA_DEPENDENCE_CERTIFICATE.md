# Terminal threshold data-dependence certificate

## Purpose

`220_TERMINAL_EFFECTIVE_THRESHOLD_REDUCTION.md` reduces the terminal
absolute interval to the explicit defect
\[
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
  \Theta_n,
\end{aligned}
\tag{1}
\]
where
\[
  \Theta_n
  =
  {n^2\over 12(n-1)^2}\,B_{n-1}
  \log {1+T_n\over1+T_{n-1}}.
\tag{2}
\]

This note records the exact data dependence of the remaining finite
terminal certificate.  It prevents the terminal task from being confused
with A1 itself: the terminal asymptotic sign is already closed, but an
effective finite threshold cannot be computed until the cutoff and interval
data below are fixed.

## What is already closed

From `217_N8_BASE_MARGIN_CERTIFICATE.md`,
\[
  C_8^\ast>0.
\tag{3}
\]

With the small-\(T_7\) normalization of `215`, this implies
\[
\boxed{
  \Gamma_{\mathcal B}>{25\over64}.
}
\tag{4}
\]

From `208_VK_CUTOFF_RATIO_TERMINAL_SCALE.md`, canonical VK cutoffs satisfy
\[
  \log {1+T_n\over1+T_{n-1}}
  =
  {5\over3n}+{2\over n\log n}+o(1/n),
\tag{5}
\]
so the terminal load is logarithmic:
\[
  \Theta_n=O(\log n).
\tag{6}
\]

Combining (4) and (6) gives
\[
\boxed{
  \mathfrak D_n>0
  \quad\hbox{for all sufficiently large }n
}
\tag{7}
\]
under canonical VK cutoff growth.

Thus the terminal interval has no remaining asymptotic obstruction.

## Minimal data needed for an effective threshold

An effective terminal certificate is exactly the following finite data
package.

1. A declared cutoff policy \(T_n\) for every \(n\ge8\), not just an
   asymptotic scale.  For example, one may choose the minimal \(T_n\) beyond
   the VK monotonicity range satisfying the A0 inequality.
2. A computable upper enclosure for the ratio
   \[
     \log {1+T_n\over1+T_{n-1}}
   \]
   valid for every \(n\ge N_0\).
3. A computable upper enclosure for the A0 constant \(B_{n-1}\) appearing
   in (2), compatible with the chosen cutoff policy.
4. Lower enclosures for \(C_8^\ast\) and
   \(\Delta_8^\ast=C_8^\ast-C_7^\ast\).
5. Lower enclosures for every finite archimedean summand
   \[
     1+{3\over4}D_k^{\rm arch}
   \]
   required before the asymptotic lower bound for \(\mathcal B_n\) takes
   over.
6. A finite interval check of
   \[
     \mathfrak D_n\ge0
     \qquad(9\le n<N_0).
   \]

Once these six items are supplied, (1) is a rational interval computation.
No additional analytic theorem is hidden in the terminal finite check.

## Why the current files do not determine \(N_0\)

The existing certificates provide:
\[
  \Gamma_{\mathcal B}>25/64
\]
and
\[
  \Theta_n=O(\log n).
\]

They do not yet provide numerical constants \(c_1,c_2,c_3,N_0\) such that
\[
  \mathcal B_n\ge {25\over64}n^2-c_1n\log n-c_2n-c_3
\tag{8}
\]
and
\[
  \Theta_n\le c_4\log n+c_5
\tag{9}
\]
for all \(n\ge N_0\), with compatible finite data below \(N_0\).

Without (8)--(9), the statement "sufficiently large" in `220` is a valid
asymptotic theorem but not an executable threshold.  Any numerical \(N_0\)
chosen before fixing these constants would not be certified.

## Relation to A1

Even a completed terminal threshold certificate would prove only
\[
  \mathcal B_n\ge\mathcal T_n(\varepsilon),
\]
the terminal part of the absolute route.

A1 still requires either:

1. domination of the collapsed single-Laguerre bulk from `219`--`221`;
2. a signed compact theorem;
3. strong margin;
4. one-sided tail surplus;
5. comparative Loewner domination.

Therefore the terminal finite check is a subordinate finite obligation, not
the remaining A1 theorem.

## Status

Closed as a terminal data-dependence certificate.

The terminal asymptotic sign is closed, but the effective finite threshold
is not executable until the six data items above are fixed.  A1 remains
open for the independent signed/comparative reason recorded in `238`--`244`.
