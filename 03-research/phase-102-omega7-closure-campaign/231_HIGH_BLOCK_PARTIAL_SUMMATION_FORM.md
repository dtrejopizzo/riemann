# High-block partial summation form

## Purpose

`228_HIGH_BLOCK_LAGUERRE_CORRELATION_FORM.md` isolates the high correlation
\[
  \mathcal C_n^{\rm high}
  =
  \sum_{e^{T_8}\le m\le e^{T_n}}
  {\Lambda(m)\over m}L_{n-1}^{(1)}(\log m).
\]

This note applies exact partial summation to that correlation.  The result
replaces point sampling of \(L_{n-1}^{(1)}\) by an integral of the weighted
prime-power counting function against \(L_{n-2}^{(2)}\).

## Weighted prime-power counting function

Define, for \(T_8\le u\le T_n\),
\[
\boxed{
  A_8(u)
  =
  \sum_{e^{T_8}\le m\le e^u}{\Lambda(m)\over m}.
}
\tag{1}
\]

Then
\[
\boxed{
  \mathcal C_n^{\rm high}
  =
  \int_{T_8}^{T_n}L_{n-1}^{(1)}(u)\,dA_8(u).
}
\tag{2}
\]

Since
\[
  {d\over du}L_{n-1}^{(1)}(u)=-L_{n-2}^{(2)}(u),
\tag{3}
\]
Stieltjes integration by parts gives
\[
\boxed{
  \mathcal C_n^{\rm high}
  =
  A_8(T_n)L_{n-1}^{(1)}(T_n)
  +
  \int_{T_8}^{T_n}A_8(u)L_{n-2}^{(2)}(u)\,du.
}
\tag{4}
\]

Endpoint prime powers can be assigned consistently to adjacent finite
blocks; this convention changes no compact integral and only changes a
finite endpoint bookkeeping term.

## Main term and discrepancy

The continuous main term for \(A_8(u)\) is \(u-T_8\).  Write
\[
\boxed{
  A_8(u)=u-T_8+E_8^\sharp(u).
}
\tag{5}
\]

Then
\[
\boxed{
\begin{aligned}
  \mathcal C_n^{\rm high}
  &=
  (T_n-T_8)L_{n-1}^{(1)}(T_n)
  +
  \int_{T_8}^{T_n}(u-T_8)L_{n-2}^{(2)}(u)\,du\\
  &\quad+
  E_8^\sharp(T_n)L_{n-1}^{(1)}(T_n)
  +
  \int_{T_8}^{T_n}E_8^\sharp(u)L_{n-2}^{(2)}(u)\,du.
\end{aligned}
}
\tag{6}
\]

The first line is continuous and explicit.  The second line is the true
arithmetic discrepancy.

## Remaining high-block theorem

Substituting (4) into the high-block inequality of `228`, A1 requires
\[
\boxed{
\begin{aligned}
  &A_8(T_n)L_{n-1}^{(1)}(T_n)
  +
  \int_{T_8}^{T_n}A_8(u)L_{n-2}^{(2)}(u)\,du\\
  &\quad\le
  \mathcal A_n-P_n+\mathcal P_n^{\rm low}
  +
  e^{-T_n}L_{n-1}^{(1)}(T_n)\Psi_{[T_8,T_n]}.
\end{aligned}
}
\tag{7}
\]

Equivalently, after inserting (6), the unresolved signed object is
\[
\boxed{
  E_8^\sharp(T_n)L_{n-1}^{(1)}(T_n)
  +
  \int_{T_8}^{T_n}E_8^\sharp(u)L_{n-2}^{(2)}(u)\,du.
}
\tag{8}
\]

## Why this is still a signed theorem

The kernel \(L_{n-2}^{(2)}\) oscillates in the bulk.  Therefore a two-sided
bound for \(|E_8^\sharp(u)|\) again gives only an absolute \(L^1\)
estimate.  After `221` and `223`, that is not the mechanism needed for
A1.

Partial summation changes the arithmetic object from point sampling to a
weighted discrepancy integral, but it does not turn the problem into a
positivity theorem.

## Status

Closed as an exact partial-summation normal form for the high block.

A1 remains open.  The high block is now equivalent to the signed
discrepancy integral (8).
