# Raised Laguerre dual hierarchy

## Purpose

`145_LAGUERRE_LOBE_DUAL_BALANCE.md` integrates the compact A1 core once.
This note records the full hierarchy obtained by repeated integration by
parts.  The key identity is that differentiating the weighted Laguerre
kernel raises the Laguerre parameter by one:
\[
  {d\over du}\left(e^{-u}L_m^{(\alpha)}(u)\right)
  =
  -e^{-u}L_m^{(\alpha+1)}(u).
\]

Thus A1 can be written as a family of exact signed inequalities involving
smoother and smoother cumulative prime-pole balances.

## Repeated cumulative balances

Let
\[
  E(e^u)=\psi(e^u)-e^u.
\]
Define
\[
  B_0(u)=E(e^u)
\]
and, for \(r\ge1\),
\[
  B_r(U)
  =
  \int_0^U B_{r-1}(v)\,dv
  =
  {1\over (r-1)!}
  \int_0^U (U-v)^{r-1}E(e^v)\,dv.
\tag{1}
\]

For every \(r\ge1\), finite Fubini gives the exact arithmetic formula
\[
  \boxed{
  B_r(U)
  =
  {1\over r!}\sum_{m\le e^U}\Lambda(m)(U-\log m)^r
  -
  e^U
  +
  \sum_{k=0}^{r-1}{U^k\over k!}.
  }
\tag{2}
\]

Indeed, the prime-power part is
\[
  {1\over (r-1)!}
  \sum_{m\le e^U}\Lambda(m)
  \int_{\log m}^U (U-v)^{r-1}\,dv
  =
  {1\over r!}\sum_{m\le e^U}\Lambda(m)(U-\log m)^r,
\]
and the continuous pole part is
\[
  {1\over (r-1)!}\int_0^U (U-v)^{r-1}e^v\,dv
  =
  e^U-\sum_{k=0}^{r-1}{U^k\over k!}.
\]

Thus \(B_r\) is the \(r\)-fold integrated pole-prime cancellation.  It is
finite and contains no separated divergent term.

## Raising identity

The Laguerre derivative and adjacent-parameter identities imply, for
\(\alpha>-1\),
\[
  {d\over du}L_m^{(\alpha)}(u)=-L_{m-1}^{(\alpha+1)}(u),
\]
and
\[
  L_m^{(\alpha+1)}(u)=L_m^{(\alpha)}(u)+L_{m-1}^{(\alpha+1)}(u).
\]

Therefore
\[
\begin{aligned}
  {d\over du}\left(e^{-u}L_m^{(\alpha)}(u)\right)
  &=
  e^{-u}\left[-L_{m-1}^{(\alpha+1)}(u)-L_m^{(\alpha)}(u)\right]  \\
  &=
  -e^{-u}L_m^{(\alpha+1)}(u).
\end{aligned}
\tag{3}
\]

Iterating,
\[
  {d^r\over du^r}\left(e^{-u}L_m^{(\alpha)}(u)\right)
  =
  (-1)^r e^{-u}L_m^{(\alpha+r)}(u).
\tag{4}
\]

## Exact hierarchy for the A1 core

Let
\[
  m=n-1,\qquad
  \Phi_{n,j}(u)=e^{-u}L_{n-1}^{(2+j)}(u)
  \qquad(j\ge0).
\tag{5}
\]

By `144_LAGUERRE_CORE_SIGN_PARTITION.md`, the compact integral in A1 is
\[
  I_n(T)=\int_0^T E(e^u)\Phi_{n,0}(u)\,du.
\tag{6}
\]

Since
\[
  \Phi_{n,j}'(u)=-\Phi_{n,j+1}(u),
\tag{7}
\]
integration by parts gives
\[
  I_n(T)
  =
  B_1(T)\Phi_{n,0}(T)
  +
  \int_0^T B_1(u)\Phi_{n,1}(u)\,du.
\tag{8}
\]

Repeating this \(r\) times gives the exact identity
\[
  \boxed{
  I_n(T)
  =
  \sum_{j=1}^{r} B_j(T)\Phi_{n,j-1}(T)
  +
  \int_0^T B_r(u)\Phi_{n,r}(u)\,du.
  }
\tag{9}
\]

All lower-end boundary terms vanish because \(B_j(0)=0\).

Thus A1 is equivalent, for every fixed \(r\ge0\), to
\[
  \boxed{
  \sum_{j=1}^{r} B_j(T_n)e^{-T_n}L_{n-1}^{(1+j)}(T_n)
  +
  \int_0^{T_n} B_r(u)e^{-u}L_{n-1}^{(2+r)}(u)\,du
  \le
  {3\over4}\lambda_n^{\rm arch}-n.
  }
\tag{10}
\]

For \(r=0\), this is the original collapsed-kernel form.  For \(r=1\), it
is the global version of the dual balance in `145`.

## Why the hierarchy is not a proof by smoothing

The functions \(B_r\) become smoother as \(r\) grows, but the Laguerre
kernel remains oscillatory:
\[
  L_{n-1}^{(2+r)}
\]
still has \(n-1\) simple positive zeros.  Therefore no finite \(r\) removes
the signed problem.  Replacing the last integral in (10) by an absolute
bound again falls into the eliminated A0-style proof class.

The hierarchy is useful only if one proves a signed theorem of the form:

for some explicitly chosen \(r=r(n)\) or fixed \(r\), the \(r\)-fold
cumulative balance \(B_r\), with the endpoint terms in (10), is aligned
one-sidedly with the raised Laguerre kernel \(L_{n-1}^{(2+r)}\) strongly
enough to imply (10).

## Endpoint-zero option

If the cutoff \(T_n\) is chosen to be a common zero of one of the endpoint
Laguerre factors in (10), the corresponding boundary term disappears.  But
A0 supplies \(T_n\) from a tail domination condition, not from Laguerre
zeros.  Therefore this option can be used only if a new cutoff theorem
proves simultaneously:

1. the A0 tail budget;
2. cancellation or control of all endpoint terms in (10);
3. the remaining signed raised-kernel inequality.

This is another form of the moving-cutoff gate; it is not supplied by A0
alone.

## Minimal raised-balance theorem

A concrete route to A1 is now:

find \(r\ge1\), or a rule \(r=r(n)\), and prove from the exact formula (2)
that
\[
  \sum_{j=1}^{r} B_j(T_n)e^{-T_n}L_{n-1}^{(1+j)}(T_n)
  +
  \int_0^{T_n} B_r(u)e^{-u}L_{n-1}^{(2+r)}(u)\,du
  \le
  {3\over4}\lambda_n^{\rm arch}-n
\tag{11}
\]
for all \(n\ge8\).

This theorem is exactly A1 in raised dual coordinates.  It becomes a genuine
proof only when the inequality is established by a one-sided arithmetic
argument for \(B_r\), not by assuming Li positivity or by defining a
positive zero-side measure.

## Status

Closed as an exact hierarchy.  The new identities are the arithmetic formula
for \(B_r\), the raising rule (3), and the A1 equivalence (10).

A1 remains open.  The sharpened live target is the minimal raised-balance
theorem (11).
