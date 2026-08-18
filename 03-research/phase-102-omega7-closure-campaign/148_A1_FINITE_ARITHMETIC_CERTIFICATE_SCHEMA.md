# A1 finite arithmetic certificate schema

## Purpose

`147_BALANCE_LAPLACE_JET_FORM.md` writes the raised A1 target as a finite
jet.  This note removes the remaining integral notation from each fixed
instance.  For fixed \(n\), cutoff \(T\), and raise level \(r\), the A1
quantity is a finite arithmetic expression involving:

- prime powers \(m\le e^T\);
- Laguerre coefficients;
- endpoint values at \(T\);
- elementary exponential-polynomial remainders.

This is a certificate schema for individual instances and for symbolic
families.  It is not a proof of the infinite range unless a uniform
inequality for the resulting finite expression is proved.

## Polynomial coefficients

For \(m=n-1\) and \(\alpha>-1\),
\[
  L_m^{(\alpha)}(u)
  =
  \sum_{k=0}^{m}
  (-1)^k {1\over k!}\binom{m+\alpha}{m-k}u^k.
\tag{1}
\]

Write
\[
  L_{n-1}^{(2+r)}(u)=\sum_{k=0}^{n-1}c_{n,r,k}u^k,
  \qquad
  c_{n,r,k}
  =
  (-1)^k {1\over k!}\binom{n+1+r}{n-1-k}.
\tag{2}
\]

Also write the endpoint polynomials
\[
  L_{n-1}^{(1+j)}(T)
  =
  \sum_{k=0}^{n-1}
  (-1)^k {1\over k!}\binom{n+j}{n-1-k}T^k.
\tag{3}
\]

## Elementary exponential moments

For \(q\ge0\), define
\[
  M_q(A)=\int_0^A e^{-t}t^q\,dt.
\tag{4}
\]

For integer \(q\),
\[
  \boxed{
  M_q(A)
  =
  q!\left(1-e^{-A}\sum_{\ell=0}^{q}{A^\ell\over \ell!}\right).
  }
\tag{5}
\]

Every integral below reduces to these \(M_q\).

## Prime-power block

Let
\[
  X=e^T.
\]

The raised compact integral in `146` is
\[
  J_{n,r}(T)
  =
  \int_0^T B_r(u)e^{-u}L_{n-1}^{(2+r)}(u)\,du.
\tag{6}
\]

Insert the exact formula
\[
  B_r(u)
  =
  {1\over r!}\sum_{m\le e^u}\Lambda(m)(u-\log m)^r
  -
  e^u
  +
  \sum_{a=0}^{r-1}{u^a\over a!}.
\tag{7}
\]

The prime-power contribution is
\[
\begin{aligned}
  J_{n,r}^{\rm pp}(T)
  &=
  {1\over r!}
  \sum_{m\le X}\Lambda(m)
  \int_{\log m}^{T}
  (u-\log m)^r e^{-u}L_{n-1}^{(2+r)}(u)\,du  \\
  &=
  {1\over r!}
  \sum_{m\le X}{\Lambda(m)\over m}
  \sum_{k=0}^{n-1}c_{n,r,k}
  \sum_{b=0}^{k}\binom{k}{b}(\log m)^{k-b}
  M_{r+b}(T-\log m).
\end{aligned}
\tag{8}
\]

This is finite because \(m\le X\).

## Continuous pole block

The continuous pole contribution is
\[
  J_{n,r}^{\rm pole}(T)
  =
  -\int_0^T L_{n-1}^{(2+r)}(u)\,du.
\tag{9}
\]

Using (2),
\[
  \boxed{
  J_{n,r}^{\rm pole}(T)
  =
  -\sum_{k=0}^{n-1} c_{n,r,k}{T^{k+1}\over k+1}.
  }
\tag{10}
\]

## Origin polynomial block

The final part of \(B_r\) contributes
\[
  J_{n,r}^{\rm orig}(T)
  =
  \sum_{a=0}^{r-1}{1\over a!}
  \int_0^T u^a e^{-u}L_{n-1}^{(2+r)}(u)\,du.
\tag{11}
\]

Therefore
\[
  \boxed{
  J_{n,r}^{\rm orig}(T)
  =
  \sum_{a=0}^{r-1}{1\over a!}
  \sum_{k=0}^{n-1} c_{n,r,k}M_{a+k}(T).
  }
\tag{12}
\]

Combining (8), (10), and (12),
\[
  \boxed{
  J_{n,r}(T)
  =
  J_{n,r}^{\rm pp}(T)
  +
  J_{n,r}^{\rm pole}(T)
  +
  J_{n,r}^{\rm orig}(T).
  }
\tag{13}
\]

## Endpoint block

The raised hierarchy also contains endpoint terms
\[
  E_{n,r}(T)
  =
  \sum_{j=1}^{r}
  B_j(T)e^{-T}L_{n-1}^{(1+j)}(T).
\tag{14}
\]

Each \(B_j(T)\) is finite:
\[
  B_j(T)
  =
  {1\over j!}\sum_{m\le X}\Lambda(m)(T-\log m)^j
  -
  X
  +
  \sum_{a=0}^{j-1}{T^a\over a!}.
\tag{15}
\]

Each Laguerre endpoint value is given by (3).

## Certificate inequality

For fixed \(n\ge8\), \(T=T_n\), and \(r\ge1\), A1 is equivalent to
\[
  \boxed{
  E_{n,r}(T_n)
  +
  J_{n,r}^{\rm pp}(T_n)
  +
  J_{n,r}^{\rm pole}(T_n)
  +
  J_{n,r}^{\rm orig}(T_n)
  \le
  {3\over4}\lambda_n^{\rm arch}-n.
  }
\tag{16}
\]

All quantities on the left side are explicit finite sums over prime powers
\(m\le e^{T_n}\) and elementary polynomial-exponential functions of
\(T_n-\log m\).

## What a uniform proof must add

The schema (16) is exact, but it is only pointwise unless supplemented by a
uniform theorem.  To close A1, one must prove (16) for all \(n\ge8\) with
the A0-compatible cutoffs \(T_n\), or prove a stronger version with a new
cutoff rule that preserves the A0 tail budget.

The following shortcuts are invalid:

1. verifying (16) for finitely many \(n\) and extrapolating;
2. bounding \(J_{n,r}^{\rm pp}\), \(J_{n,r}^{\rm pole}\), and
   \(J_{n,r}^{\rm orig}\) separately in absolute value;
3. choosing \(T_n\) after seeing the sign unless the moving-cutoff current
   is also controlled;
4. replacing the finite prime-power sum by an unsigned PNT remainder.

## Status

Closed as a finite arithmetic certificate schema.  A1 remains open.

The remaining proof load is a uniform signed inequality for the explicit
finite expression (16).
