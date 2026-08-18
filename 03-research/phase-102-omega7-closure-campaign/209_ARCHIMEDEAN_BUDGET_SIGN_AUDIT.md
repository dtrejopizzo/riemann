# Archimedean budget sign audit

## Purpose

`207_A0_TERMINAL_CUTOFF_BRIDGE_AUDIT.md` reduces the terminal absolute
route to a comparison against the base-archimedean budget
\[
  \mathcal B_n
  =
  C_8^\ast
  +
  {n(n+1)-72\over16}\Delta_8^\ast
  +
  \sum_{k=8}^{n-1}
  w_{n,k}\left(1+{3\over4}D_k^{\rm arch}\right).
\]

This note checks whether the summands
\[
  1+{3\over4}D_k^{\rm arch}
\]
give an automatic positive reserve.  They do not.  In fact
\[
  D_k^{\rm arch}=-{1\over2}\log k+O(1),
\]
so the archimedean forcing summand is eventually negative.

Thus the absolute route still needs an independent lower bound for
\(\mathcal B_n\), including the base terms.  Positivity of the weights
\(w_{n,k}\) is not enough.

## Asymptotic of \(D_n^{\rm arch}\)

From `205`,
\[
  A_n=\lambda_n^{\rm arch}={1\over2}n\log n+O(n).
\tag{1}
\]

Recall from `157` that
\[
  D_n^{\rm arch}
  =
  nA_{n+1}-(2n+1)A_n+(n+1)A_{n-1}.
\tag{2}
\]

Apply (2) to the model function
\[
  A(x)={1\over2}x\log x.
\]
Using Taylor expansion at \(n\),
\[
\begin{aligned}
  A_{n+1}&=A_n+A'_n+{1\over2}A''_n+O(n^{-2}),\\
  A_{n-1}&=A_n-A'_n+{1\over2}A''_n+O(n^{-2}),
\end{aligned}
\]
where
\[
  A'_n={1\over2}(\log n+1),
  \qquad
  A''_n={1\over2n}.
\]

Substitution gives
\[
\begin{aligned}
  nA_{n+1}-(2n+1)A_n+(n+1)A_{n-1}
  &=
  -A'_n+{2n+1\over2}A''_n+O(n^{-1})\\
  &=
  -{1\over2}\log n+O(1).
\end{aligned}
\tag{3}
\]

The same leading term follows directly from the exact summand formula in
`157`,
\[
  D_n^{\rm arch}
  =
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}
  \left[
  \left(1-{1\over r}\right)^{n-1}
  \left({1\over r}+{n\over r^2}\right)
  -{1\over r}
  \right],
\tag{4}
\]
by splitting the odd sum at \(r\asymp n\).

Therefore
\[
\boxed{
  D_n^{\rm arch}
  =
  -{1\over2}\log n+O(1).
}
\tag{5}
\]

Consequently,
\[
\boxed{
  1+{3\over4}D_n^{\rm arch}
  =
  1-{3\over8}\log n+O(1),
}
\tag{6}
\]
and this expression is negative for all sufficiently large \(n\).

## Consequence for \(\mathcal B_n\)

The weights
\[
  w_{n,k}
  =
  {1\over2}\left({n(n+1)\over k(k+1)}-1\right)
\]
are positive for \(8\le k\le n-1\).  But positive weights multiplying
eventually negative summands do not give a positive budget.

Thus the implication
\[
  w_{n,k}>0
  \quad\Longrightarrow\quad
  \mathcal B_n>0
\]
is invalid.

The only possible positive reserve in \(\mathcal B_n\) must come from the
full combination
\[
  C_8^\ast
  +
  {n(n+1)-72\over16}\Delta_8^\ast
  +
  \sum_{k=8}^{n-1}
  w_{n,k}\left(1+{3\over4}D_k^{\rm arch}\right),
\tag{7}
\]
not from the archimedean forcing summands separately.

## Impact on the terminal bridge

`207` gives the sufficient terminal estimate
\[
  \mathcal T_n
  \le
  {n^2\over12(n-1)^2}B_{n-1}
  \log {1+T_n\over1+T_{n-1}}.
\tag{8}
\]

To use it in the absolute route, one still needs
\[
\boxed{
  \mathcal B_n
  \ge
  {n^2\over12(n-1)^2}B_{n-1}
  \log {1+T_n\over1+T_{n-1}}.
}
\tag{9}
\]

The sign audit above shows that (9) cannot be justified by saying that the
archimedean forcing part of \(\mathcal B_n\) is positive.  A separate
theorem must estimate the entire budget (7), including the base terms
\(C_8^\ast\) and \(\Delta_8^\ast\).

## Exact remaining theorem

The absolute diagonal route now needs the following budget theorem before
the terminal bridge can be used:
\[
\boxed{
  \mathcal B_n>0
  \quad\hbox{and}\quad
  \mathcal B_n
  \hbox{ dominates the terminal and mixed }L^1\hbox{ loads uniformly.}
}
\tag{10}
\]

This is strictly stronger than archimedean positivity of
\(\lambda_n^{\rm arch}\).  The latter says
\[
  \lambda_n^{\rm arch}>0\qquad(n\ge8),
\]
whereas \(\mathcal B_n\) uses a second-order recurrence combination that is
asymptotically negative in its individual forcing summands.

## Status

Closed as a sign audit for the base-archimedean budget.

A1 remains open.  The absolute route cannot use the archimedean recurrence
forcing as a free positive reserve; it must prove a full budget domination
theorem.
