# Moving diagonal A1 generator

## Purpose

The finite arithmetic certificate in `148` is pointwise in \(n\).  This note
puts those pointwise certificates into generating-function form.

For a fixed cutoff \(T\), the A1 compact quantity has a clean holomorphic
generator.  The actual A1 theorem, however, uses the moving cutoffs
\(T=T_n\).  Therefore the infinite-range problem is not ordinary coefficient
positivity of one fixed function; it is a moving diagonal positivity problem
through a family of fixed-cutoff generators.

## Fixed-cutoff compact generator

Let
\[
  E(e^u)=\psi(e^u)-e^u
\]
and
\[
  \Phi_n(u)=e^{-u}L_{n-1}^{(2)}(u).
\]

From `144_LAGUERRE_CORE_SIGN_PARTITION.md`,
\[
  C_n(T)
  =
  -n-\int_0^T E(e^u)\Phi_n(u)\,du
  +{3\over4}\lambda_n^{\rm arch}.
\tag{1}
\]

The Laguerre generating identity is
\[
  \sum_{n\ge1}L_{n-1}^{(2)}(u)z^n
  =
  {z\over(1-z)^3}
  \exp\!\left(-{uz\over1-z}\right).
\tag{2}
\]

Therefore
\[
\begin{aligned}
  \sum_{n\ge1}
  \left[
    \int_0^T E(e^u)\Phi_n(u)\,du
  \right]z^n
  &=
  {z\over(1-z)^3}
  \int_0^T
  E(e^u)
  \exp\!\left(-{u\over1-z}\right)\,du.
\end{aligned}
\tag{3}
\]

Let \(\mathcal A(z)\) denote the archimedean Li generator from
`140_EULER_GAMMA_LI_GENERATOR.md`:
\[
  \mathcal A(z)=\sum_{n\ge1}\lambda_n^{\rm arch}z^n.
\]

Then the fixed-cutoff A1 generator is
\[
  \boxed{
  \mathcal C_T(z)
  =
  -{z\over(1-z)^2}
  +{3\over4}\mathcal A(z)
  -
  {z\over(1-z)^3}
  \int_0^T
  E(e^u)
  \exp\!\left(-{u\over1-z}\right)\,du.
  }
\tag{4}
\]

It satisfies
\[
  [z^n]\mathcal C_T(z)=C_n(T).
\tag{5}
\]

For fixed \(T<\infty\), this is a holomorphic function in the Li disk.  All
singular behavior from the prime side has been truncated into an entire
Laplace kernel.

## Raised fixed-cutoff generator

For the raised hierarchy, put
\[
  \Phi_{n,j}(u)=e^{-u}L_{n-1}^{(2+j)}(u).
\]

The generating identity becomes
\[
  \sum_{n\ge1}L_{n-1}^{(2+r)}(u)z^n
  =
  {z\over(1-z)^{3+r}}
  \exp\!\left(-{uz\over1-z}\right).
\tag{6}
\]

The raised identity in `146` gives
\[
  \int_0^T E(e^u)\Phi_{n,0}(u)\,du
  =
  \sum_{j=1}^{r}B_j(T)e^{-T}L_{n-1}^{(1+j)}(T)
  +
  \int_0^T B_r(u)e^{-u}L_{n-1}^{(2+r)}(u)\,du.
\tag{7}
\]

Therefore the same generator can be written as
\[
\boxed{
\begin{aligned}
  \mathcal C_{T,r}(z)
  &=
  -{z\over(1-z)^2}
  +{3\over4}\mathcal A(z)\\
  &\quad-
  \sum_{j=1}^{r}
  B_j(T)e^{-T}
  {z\over(1-z)^{2+j}}
  \exp\!\left(-{Tz\over1-z}\right)\\
  &\quad-
  {z\over(1-z)^{3+r}}
  \int_0^T
  B_r(u)
  \exp\!\left(-{u\over1-z}\right)\,du .
\end{aligned}
}
\tag{8}
\]

For every \(r\ge0\),
\[
  \mathcal C_{T,r}(z)=\mathcal C_T(z)
\tag{9}
\]
as a coefficient identity, because (7) is exact.  The raised forms are not
new functions; they are different signed decompositions of the same
fixed-cutoff generator.

## Moving diagonal obstruction

A1 requires
\[
  C_n(T_n)\ge0\qquad(n\ge8),
\tag{10}
\]
where \(T_n\) is chosen to make the A0 tail budget valid.

This is not the same as coefficient positivity for one fixed \(T\):
\[
  [z^n]\mathcal C_T(z)\ge0\qquad(n\ge8).
\tag{11}
\]

Instead, A1 is the diagonal condition
\[
  \boxed{
  [z^n]\mathcal C_{T_n}(z)\ge0
  \qquad(n\ge8).
  }
\tag{12}
\]

Thus a fixed-cutoff positivity theorem closes A1 only if it is accompanied
by one of the following extra inputs:

1. a universal cutoff \(T_\ast\) compatible with A0 for all \(n\);
2. a monotonicity theorem showing that \(C_n(T)\) preserves the needed sign
   as \(T\) moves from a fixed cutoff to \(T_n\);
3. a direct moving-diagonal theorem proving (12);
4. a stronger global positive-boundary theorem that implies all fixed and
   moving cutoff coefficients simultaneously.

`126_UNIVERSAL_CUTOFF_GATE_AUDIT.md` records that the current A0 theorem
does not supply item 1.  `127_MOVING_CUTOFF_FLOW_NORMAL_FORM.md` records
that item 2 requires a one-sided boundary-current theorem.

## Coefficient target

The exact moving-diagonal generator theorem is:

prove, from the Euler--Gamma data and the A0 cutoff construction, that
\[
  [z^n]\left[
  -{z\over(1-z)^2}
  +{3\over4}\mathcal A(z)
  -
  {z\over(1-z)^3}
  \int_0^{T_n}
  E(e^u)
  \exp\!\left(-{u\over1-z}\right)\,du
  \right]\ge0
\tag{13}
\]
for every \(n\ge8\).

Equivalently, use the raised form (8) with \(T=T_n\).  This is exactly the
finite arithmetic certificate of `148` in generating-function coordinates.

## Status

Closed as a fixed-cutoff generator and moving-diagonal normal form.

A1 remains open.  The missing theorem is coefficient positivity along the
moving diagonal \(T=T_n\), or one of the stronger gates listed above.
