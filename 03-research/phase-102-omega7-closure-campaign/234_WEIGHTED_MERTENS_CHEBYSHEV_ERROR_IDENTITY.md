# Weighted Mertens--Chebyshev error identity

## Purpose

`231_HIGH_BLOCK_PARTIAL_SUMMATION_FORM.md` reduces the high block to the
weighted discrepancy
\[
  E_8^\sharp(u)=A_8(u)-(u-T_8),
  \qquad
  A_8(u)=\sum_{e^{T_8}\le m\le e^u}{\Lambda(m)\over m}.
\]

This note writes \(E_8^\sharp\) exactly in terms of the ordinary Chebyshev
error
\[
  E(e^u)=\psi(e^u)-e^u.
\]

The identity shows that the current \(E_8^\sharp\)-frontier is not a new
source of positivity.  It is the same signed Chebyshev error, smoothed once
and with endpoint terms.

## Stieltjes identity

With endpoint conventions fixed consistently with the finite sums, write
\[
  A_8(u)=\int_{T_8^-}^{u} e^{-t}\,d\psi(e^t).
\tag{1}
\]

Since
\[
  d\!\left(e^{-t}\psi(e^t)\right)
  =
  e^{-t}\,d\psi(e^t)-e^{-t}\psi(e^t)\,dt,
\tag{2}
\]
we have
\[
\begin{aligned}
  A_8(u)
  &=
  e^{-u}\psi(e^u)-e^{-T_8}\psi(e^{T_8})
  +
  \int_{T_8}^{u}e^{-t}\psi(e^t)\,dt.
\end{aligned}
\tag{3}
\]

Substitute \(\psi(e^t)=e^t+E(e^t)\).  The main terms give \(u-T_8\), so
\[
\boxed{
  E_8^\sharp(u)
  =
  e^{-u}E(e^u)-e^{-T_8}E(e^{T_8})
  +
  \int_{T_8}^{u}e^{-t}E(e^t)\,dt.
}
\tag{4}
\]

Thus \(E_8^\sharp\) is a boundary-plus-integral transform of the same
Chebyshev error used throughout A0/A1.

## Substitution into the discrepancy frontier

The unresolved object from `231` is
\[
  \mathfrak E_n
  =
  E_8^\sharp(T_n)L_{n-1}^{(1)}(T_n)
  +
  \int_{T_8}^{T_n}E_8^\sharp(u)L_{n-2}^{(2)}(u)\,du.
\tag{5}
\]

Using (4), \(\mathfrak E_n\) is exactly
\[
\boxed{
\begin{aligned}
  \mathfrak E_n
  &=
  \left[
    e^{-T_n}E(e^{T_n})-e^{-T_8}E(e^{T_8})
    +\int_{T_8}^{T_n}e^{-t}E(e^t)\,dt
  \right]L_{n-1}^{(1)}(T_n)\\
  &\quad+
  \int_{T_8}^{T_n}
  \left[
    e^{-u}E(e^u)-e^{-T_8}E(e^{T_8})
    +\int_{T_8}^{u}e^{-t}E(e^t)\,dt
  \right]L_{n-2}^{(2)}(u)\,du.
\end{aligned}
}
\tag{6}
\]

By Fubini, the nested integral part can also be written as
\[
\boxed{
  \int_{T_8}^{T_n}
  e^{-t}E(e^t)
  \left[
    L_{n-1}^{(1)}(T_n)
    +
    \int_{t}^{T_n}L_{n-2}^{(2)}(u)\,du
  \right]dt.
}
\tag{7}
\]

Using
\[
  {d\over du}L_{n-1}^{(1)}(u)=-L_{n-2}^{(2)}(u),
\tag{8}
\]
the bracket in (7) equals
\[
  L_{n-1}^{(1)}(t).
\tag{9}
\]

Therefore the nested \(E(e^t)\)-part in \(\mathfrak E_n\) collapses to
\[
\boxed{
  \int_{T_8}^{T_n}e^{-t}E(e^t)L_{n-1}^{(1)}(t)\,dt,
}
\tag{10}
\]
while the non-nested local term
\[
  \int_{T_8}^{T_n}e^{-u}E(e^u)L_{n-2}^{(2)}(u)\,du
\tag{11}
\]
and the explicit endpoint constants at \(T_8\) and \(T_n\) remain.

## Interpretation

Equation (10) contains the original signed compact
Chebyshev--Laguerre pairing on the high interval, and (11) is the raised
local companion forced by partial summation.  The weighted-Mertens
discrepancy form of `231` is therefore not an independent positivity
mechanism.  It is another exact coordinate system for the same signed
Chebyshev-error core.

This is useful because it prevents a false detour:

- proving a two-sided bound for \(E_8^\sharp\) is no stronger than a
  two-sided smoothed Chebyshev bound, and `232` shows that such bounds lose
  in the Laguerre bulk;
- proving the sign of (5) is equivalent to proving a high-interval signed
  correlation between \(E(e^u)\) and the Laguerre pair
  \(L_{n-1}^{(1)},L_{n-2}^{(2)}\), with explicit endpoint corrections.

## Status

Closed as an exact identity between the weighted-Mertens discrepancy and
the Chebyshev error.

A1 remains open.  This identity reduces the `231` frontier back to the
same signed Chebyshev--Laguerre core rather than proving its sign.
