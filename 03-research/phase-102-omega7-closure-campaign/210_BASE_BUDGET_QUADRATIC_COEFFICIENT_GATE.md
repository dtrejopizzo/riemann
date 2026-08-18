# Base-budget quadratic coefficient gate

## Purpose

`208_VK_CUTOFF_RATIO_TERMINAL_SCALE.md` shows that the terminal absolute
load is only \(O(\log n)\) for canonical VK cutoffs.  `209` shows that the
individual archimedean recurrence summands do not give a free positive
reserve.

This note isolates the exact coefficient that decides the large-\(n\)
behavior of the base budget
\[
  \mathcal B_n
  =
  C_8^\ast
  +
  {n(n+1)-72\over16}\Delta_8^\ast
  +
  \sum_{k=8}^{n-1}
  w_{n,k}\left(1+{3\over4}D_k^{\rm arch}\right),
\tag{1}
\]
where
\[
  w_{n,k}={1\over2}\left({n(n+1)\over k(k+1)}-1\right).
\tag{2}
\]

The result is a sharp gate: \(\mathcal B_n\) is asymptotically quadratic
with an explicit coefficient \(\Gamma_{\mathcal B}\).  If this coefficient
is positive, then the terminal \(O(\log n)\) load from `208` is absorbed
for all sufficiently large \(n\).  If it is nonpositive, no such conclusion
follows from the base budget alone.

## Convergence of the archimedean series

Put
\[
  a_k=1+{3\over4}D_k^{\rm arch}.
\tag{3}
\]
By `209`,
\[
  a_k=1-{3\over8}\log k+O(1).
\tag{4}
\]
Therefore
\[
  \sum_{k=8}^{\infty}{a_k\over k(k+1)}
\tag{5}
\]
converges absolutely up to the harmless logarithmic weight, since
\[
  \sum_{k\ge8}{\log k\over k^2}<\infty.
\]

Define the explicit coefficient
\[
\boxed{
  \Gamma_{\mathcal B}
  =
  {\Delta_8^\ast\over16}
  +
  {1\over2}
  \sum_{k=8}^{\infty}{a_k\over k(k+1)}.
}
\tag{6}
\]

As shown later in `212_BASE_BUDGET_TELESCOPING_REDUCTION.md`, the infinite
archimedean part telescopes:
\[
\boxed{
  \Gamma_{\mathcal B}
  =
  {\Delta_8^\ast\over16}
  +
  {1\over16}
  +
  {3(A_7-A_8)\over64}.
}
\tag{6'}
\]

Thus this number is not determined by archimedean positivity alone.  It
depends on the finite base difference \(\Delta_8^\ast\) and the two
explicit archimedean values \(A_7,A_8\).

## Asymptotic expansion of \(\mathcal B_n\)

Using (1)--(2),
\[
\begin{aligned}
  \mathcal B_n
  &=
  C_8^\ast-{72\over16}\Delta_8^\ast
  +
  {n(n+1)\over16}\Delta_8^\ast \\
  &\quad+
  {n(n+1)\over2}
  \sum_{k=8}^{n-1}{a_k\over k(k+1)}
  -
  {1\over2}\sum_{k=8}^{n-1}a_k.
\end{aligned}
\tag{7}
\]

Subtract and add the tail of the convergent series:
\[
  \sum_{k=8}^{n-1}{a_k\over k(k+1)}
  =
  \sum_{k=8}^{\infty}{a_k\over k(k+1)}
  -
  \sum_{k=n}^{\infty}{a_k\over k(k+1)}.
\tag{8}
\]
Since \(a_k=O(\log k)\),
\[
  \sum_{k=n}^{\infty}{a_k\over k(k+1)}
  =
  O\!\left({\log n\over n}\right),
\tag{9}
\]
and
\[
  \sum_{k=8}^{n-1}a_k=O(n\log n).
\tag{10}
\]

Therefore
\[
\boxed{
  \mathcal B_n
  =
  \Gamma_{\mathcal B} n^2
  +
  O(n\log n).
}
\tag{11}
\]

This is the exact large-scale budget law.

## Terminal absorption consequence

For canonical VK cutoffs, `208` gives
\[
  \mathcal T_n(\varepsilon)
  \le
  {5\over72}\log n+O(1).
\tag{12}
\]

Hence:

- If
  \[
  \boxed{\Gamma_{\mathcal B}>0,}
  \tag{13}
  \]
  then \(\mathcal B_n\ge \mathcal T_n(\varepsilon)\) for all sufficiently
  large \(n\).  The remaining terminal work is finite verification of the
  initial range and explicit constants.

- If
  \[
  \boxed{\Gamma_{\mathcal B}<0,}
  \tag{14}
  \]
  then \(\mathcal B_n\to-\infty\) quadratically, so the absolute terminal
  comparison cannot be obtained from this base budget.

- If
  \[
  \boxed{\Gamma_{\mathcal B}=0,}
  \tag{15}
  \]
  then the \(O(n\log n)\) secondary terms decide the question; a sharper
  expansion of (7) is required.

Thus the terminal absolute route is reduced to verifying the finite
condition
\[
\boxed{
  4\Delta_8^\ast+4+3(A_7-A_8)>0
}
\tag{15'}
\]
and, in the positive case, making the threshold and finite range explicit.

## Why this does not close A1

Even a proof of \(\Gamma_{\mathcal B}>0\) would only absorb the terminal
load isolated in `201` and scaled in `208`.  The full absolute theorem still
requires
\[
  \mathcal B_n
  \ge
  \int_0^{T_n}\varepsilon(u)|\mathcal H_n(u)|\,du,
\tag{16}
\]
including all earlier intervals where \(\mathcal H_n\) is a cumulative
Laguerre mixture.  Those loads may be larger than the terminal interval and
are not controlled by (11).

Therefore the new exact finite target is:

1. certify the finite sign condition (15');
2. if it is positive, close the terminal finite range;
3. separately dominate the mixed-interval \(L^1\) loads, or return to a
   signed A1 theorem.

## Status

Closed as a base-budget coefficient gate.

A1 remains open.  The terminal absolute route now has an exact finite
coefficient condition, but that condition has not been certified in this
note and the mixed intervals remain outside its scope.
