# Nonpositive-tail symmetric-envelope no-go

## Purpose

`247_QUARTER_MARGIN_NONPOSITIVE_TAIL_GATE.md` shows that a quarter margin
together with
\[
  R_n(T_n)\le0
\]
would close compact A1.  This note proves that the tail sign cannot be
deduced from any symmetric Chebyshev/PNT envelope alone.

The obstruction is formal: a two-sided estimate is invariant under
flipping the sign of the error, while the signed Laguerre tail is odd in
that error.

## Tail sign in integral form

Let
\[
  E(x)=\psi(x)-x
\]
and
\[
  K_n(u)=e^{-u}L_{n-1}^{(2)}(u).
\]

With the sign convention of `244` and `247`,
\[
  R_n(T_n)
  =
  -\int_{T_n}^{\infty}E(e^u)K_n(u)\,du.
\tag{1}
\]

Thus the desired nonpositive tail is equivalent to
\[
\boxed{
  \int_{T_n}^{\infty}E(e^u)K_n(u)\,du\ge0.
}
\tag{2}
\]

## Symmetric envelope data

Suppose the only available prime-side input is a two-sided envelope
\[
\boxed{
  |E(e^u)|\le W(u)
  \qquad(u\ge T_n),
}
\tag{3}
\]
where \(W(u)\ge0\) and
\[
  \int_{T_n}^{\infty}W(u)|K_n(u)|\,du<\infty.
\tag{4}
\]

This is the information supplied by A0/VK-type tail estimates.

## Sign-flip obstruction

The data (3) are unchanged by the replacement
\[
  E(e^u)\mapsto -E(e^u).
\]

But the tail functional
\[
  \mathcal I_n(E)
  =
  \int_{T_n}^{\infty}E(e^u)K_n(u)\,du
\tag{5}
\]
is odd:
\[
  \mathcal I_n(-E)=-\mathcal I_n(E).
\tag{6}
\]

Therefore no conclusion of the form
\[
  \mathcal I_n(E)\ge0
\tag{7}
\]
can be a consequence of the symmetric envelope (3) alone, unless the
functional is forced to vanish for every admissible error.

It is not forced to vanish.  For example, the admissible model errors
\[
  E_\pm(e^u)=\pm W(u)\operatorname{sgn}K_n(u)
\]
satisfy (3), and give
\[
  \mathcal I_n(E_\pm)
  =
  \pm
  \int_{T_n}^{\infty}W(u)|K_n(u)|\,du.
\tag{8}
\]
If the integral in (8) is positive, the two admissible models have opposite
tail signs.

Hence a symmetric envelope proves at most an absolute bound
\[
  |\mathcal I_n(E)|
  \le
  \int_{T_n}^{\infty}W(u)|K_n(u)|\,du,
\tag{9}
\]
not the one-sided sign (2).

## Consequence for the quarter-margin route

The sufficient route of `247` needs
\[
  \lambda_n\ge {1\over4}A_n
  \qquad\hbox{and}\qquad
  R_n(T_n)\le0.
\]

The second inequality is exactly (2).  By the sign-flip obstruction, it
requires signed arithmetic information about the phase of
\(\psi(e^u)-e^u\) against \(L_{n-1}^{(2)}(u)\).  It cannot be recovered from
VK/PNT envelopes that retain only \(|\psi(x)-x|\).

This is the same obstruction seen in the absolute \(L^1\) no-go documents,
but now in the simpler sign-only form needed by the quarter-margin route.

## Status

Closed as a symmetric-envelope no-go for nonpositive tail.

A1 remains open.  Any proof of \(R_n(T_n)\le0\) must use a genuinely signed
explicit formula, a positive-measure/Loewner mechanism, or a direct compact
argument; it cannot use only A0-style two-sided tail decay.
