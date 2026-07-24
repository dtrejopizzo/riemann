# High-block Laguerre correlation form

## Purpose

`227_SMALL_T7_PRIME_BLOCK_ELIMINATION.md` reduces the direct signed
certificate to two arithmetic blocks.  The hard one is the high block
\[
  T_8\le \log m\le T_n.
\]

This note rewrites that block in its most transparent form: a Chebyshev
mass term minus an oscillatory Laguerre correlation
\[
  \sum \Lambda(m)m^{-1}L_{n-1}^{(1)}(\log m).
\]

This isolates the exact signed arithmetic theorem still needed.

## High coefficient

From `227`, with \(N=n-1\) and \(a=\log m\),
\[
  \Omega_n^{\rm high}(m)
  =
  e^{-T_n}L_N^{(1)}(T_n)
  -
  e^{-a}L_N^{(1)}(a).
\tag{1}
\]

Since \(e^{-a}=m^{-1}\), this is
\[
\boxed{
  \Omega_n^{\rm high}(m)
  =
  e^{-T_n}L_{n-1}^{(1)}(T_n)
  -
  {1\over m}L_{n-1}^{(1)}(\log m).
}
\tag{2}
\]

## High block split

Define
\[
  \Psi_{[T_8,T_n]}
  =
  \sum_{e^{T_8}\le m\le e^{T_n}}\Lambda(m),
\tag{3}
\]
and
\[
  \mathcal C_n^{\rm high}
  =
  \sum_{e^{T_8}\le m\le e^{T_n}}
  {\Lambda(m)\over m}L_{n-1}^{(1)}(\log m).
\tag{4}
\]

Then the high arithmetic block is exactly
\[
\boxed{
\begin{aligned}
  \mathcal P_n^{\rm high}
  &:=
  \sum_{e^{T_8}\le m\le e^{T_n}}
  \Lambda(m)\Omega_n^{\rm high}(m)\\
  &=
  e^{-T_n}L_{n-1}^{(1)}(T_n)\Psi_{[T_8,T_n]}
  -
  \mathcal C_n^{\rm high}.
\end{aligned}
}
\tag{5}
\]

Thus all high-block difficulty is in the signed correlation
\[
\boxed{
  \mathcal C_n^{\rm high}
  =
  \sum_{e^{T_8}\le m\le e^{T_n}}
  {\Lambda(m)\over m}L_{n-1}^{(1)}(\log m).
}
\tag{6}
\]

## Why PNT size is insufficient

The factor
\[
  {1\over m}
\]
removes the exponential \(e^u\) scale of prime density, so a continuous
main-term heuristic gives
\[
  \sum {\Lambda(m)\over m}F(\log m)
  \approx
  \int F(u)\,du.
\tag{7}
\]

For \(F(u)=L_{n-1}^{(1)}(u)\), this integral is oscillatory and not
sign-definite.  A two-sided error bound for primes does not determine the
sign of (6); it only bounds the size of deviations from a continuous
oscillatory integral.  The actual theorem needed is a signed statement
about how prime powers sample the Laguerre oscillations.

This is precisely the correlation that was hidden inside the compact A1
integral.

## Relation to the pole term

The pole coefficient in `226`,
\[
  P_n=\int_0^{T_n}\mathcal H_n(u)\,du,
\]
contains the continuous counterpart of the prime-power sum.  In the high
range, the continuous analogue of (6) is
\[
  \int_{T_8}^{T_n}L_{n-1}^{(1)}(u)\,du.
\tag{8}
\]

Therefore the signed A1 inequality compares a discrete prime-power
sampling of \(L_{n-1}^{(1)}\) against its continuous pole analogue, plus
the low finite block and the base-archimedean budget.

## Current signed theorem

Let \(\mathcal P_n^{\rm low}\) be the low block from `227`.  Then the
direct signed certificate can be written as
\[
\boxed{
  \mathcal A_n-P_n+\mathcal P_n^{\rm low}
  +
  e^{-T_n}L_{n-1}^{(1)}(T_n)\Psi_{[T_8,T_n]}
  -
  \mathcal C_n^{\rm high}
  \ge0.
}
\tag{9}
\]

Equivalently, A1 now requires
\[
\boxed{
  \mathcal C_n^{\rm high}
  \le
  \mathcal A_n-P_n+\mathcal P_n^{\rm low}
  +
  e^{-T_n}L_{n-1}^{(1)}(T_n)\Psi_{[T_8,T_n]}.
}
\tag{10}
\]

This is the signed high-block correlation theorem.

## Status

Closed as a high-block correlation normal form.

A1 remains open.  The remaining high-block task is the signed inequality
(10), not a size estimate for \(\psi\).
