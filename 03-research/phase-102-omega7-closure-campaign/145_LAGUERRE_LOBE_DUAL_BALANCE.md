# Laguerre lobe dual balance

## Purpose

`144_LAGUERRE_CORE_SIGN_PARTITION.md` reduces the compact A1 kernel to
\[
  -e^{-u}L_{n-1}^{(2)}(u).
\]
This note takes the next dual step: integrate the Chebyshev error once on
each Laguerre lobe.  The result replaces the raw oscillatory integral by a
balance of cumulative prime-pole error against the variation of the lobe.

This is useful because the cumulative balance has an exact arithmetic
formula.  It is still a signed theorem, not an A1 proof.

## Cumulative prime-pole balance

Let
\[
  E(e^u)=\psi(e^u)-e^u.
\]
Define the cumulative balance
\[
  B(U)=\int_0^U E(e^u)\,du.
\tag{1}
\]

Since
\[
  \psi(e^u)=\sum_{m\le e^u}\Lambda(m),
\]
Fubini on the finite triangle \(0\le v\le U\) gives
\[
  \int_0^U\psi(e^u)\,du
  =
  \sum_{m\le e^U}\Lambda(m)(U-\log m).
\]
Also
\[
  \int_0^U e^u\,du=e^U-1.
\]
Hence
\[
  \boxed{
  B(U)
  =
  \sum_{m\le e^U}\Lambda(m)(U-\log m)-e^U+1.
  }
\tag{2}
\]

This is the once-integrated pole-prime cancellation.  It is finite and
contains no separated divergent boundary pieces.

For a lobe starting at \(a\), write the local balance
\[
  B_a(u)=\int_a^u E(e^v)\,dv=B(u)-B(a).
\tag{3}
\]

## Dual form on a complete Laguerre lobe

Let
\[
  \Phi_n(u)=e^{-u}L_{n-1}^{(2)}(u).
\tag{4}
\]

The compact A1 integral in `144` is
\[
  I_n(T)=\int_0^T E(e^u)\Phi_n(u)\,du.
\tag{5}
\]

Let \(a<b\) be consecutive zeros of \(L_{n-1}^{(2)}\), or let \(a=0\) and
\(b\) be the first zero.  In both cases
\[
  B_a(a)=0,\qquad \Phi_n(b)=0,
\]
and if \(a>0\), also \(\Phi_n(a)=0\).  For \(a=0\), the boundary term at
\(a\) is still zero because \(B_a(a)=0\).

Integration by parts therefore gives the exact lobe duality
\[
  \boxed{
  \int_a^b E(e^u)\Phi_n(u)\,du
  =
  -\int_a^b B_a(u)\Phi'_n(u)\,du.
  }
\tag{6}
\]

Thus each complete lobe contribution depends on the accumulated
prime-pole balance inside the lobe, not on pointwise values of \(E\).

## Terminal incomplete lobe

If the cutoff \(T\) falls inside a final lobe \([a,T]\), then
\[
  \int_a^T E(e^u)\Phi_n(u)\,du
  =
  B_a(T)\Phi_n(T)-\int_a^T B_a(u)\Phi'_n(u)\,du.
\tag{7}
\]

This is the only extra boundary term created by the finite cutoff.  It is
not an artifact: it is exactly the moving-cutoff boundary current of the
phase, now expressed in the collapsed Laguerre kernel.

## Exact A1 dual statement

Let the complete lobes below \(T_n\) be \([a_j,b_j]\), and let
\([a_*,T_n]\) be the possible terminal incomplete lobe.  Then A1 is
equivalent to
\[
  -\sum_j\int_{a_j}^{b_j}B_{a_j}(u)\Phi'_n(u)\,du
  +B_{a_*}(T_n)\Phi_n(T_n)
  -\int_{a_*}^{T_n}B_{a_*}(u)\Phi'_n(u)\,du
  \le
  {3\over4}\lambda_n^{\rm arch}-n.
\tag{8}
\]

If \(T_n\) is itself a Laguerre zero, the terminal boundary term vanishes
and the formula is just the sum of complete lobe dual pairings.

## Sufficient signed balance theorem

A non-tautological route to A1 is now the following theorem.

For every \(n\ge8\), prove the dual lobe bound
\[
  -\sum_j\int_{a_j}^{b_j}B_{a_j}(u)\Phi'_n(u)\,du
  +B_{a_*}(T_n)\Phi_n(T_n)
  -\int_{a_*}^{T_n}B_{a_*}(u)\Phi'_n(u)\,du
  \le
  {3\over4}\lambda_n^{\rm arch}-n
\tag{9}
\]
using the explicit arithmetic formula (2), the pole-prime pairing and the
A0 cutoff convention.

This theorem is equivalent to A1 when no additional estimates are inserted.
It becomes a genuine proof route only if the left side is bounded through
one-sided information on \(B_a\) against \(\Phi'_n\), or through a block
pairing in which adjacent lobe balances cancel before absolute values are
taken.

## Why ordinary PNT input is not enough

An absolute PNT bound gives
\[
  |B_a(u)|\le \int_a^u |E(e^v)|\,dv.
\]
Substituting this into (8) gives a true estimate, but it destroys the signed
compensation and returns to the eliminated A0-style proof class.  The dual
form is valuable only if the sign of \(B_a\), its monotone excursions, or
its paired lobe averages can be controlled directly.

The missing theorem is therefore not a new explicit PNT remainder.  It is a
one-sided accumulated balance theorem:
\[
  B_a(u)
  =
  \sum_{e^a<m\le e^u}\Lambda(m)(u-\log m)
  + (u-a)\sum_{m\le e^a}\Lambda(m)
  -e^u+e^a
\]
must have enough signed alignment with \(\Phi'_n\) across the Laguerre
lobes to imply (9).

## Relation to previous gates

This dual balance is the lobe-level version of three existing gates:

1. the one-sided tail gate, because the terminal boundary term is the same
   moving-cutoff current;
2. the bordered-current gate, because (8) is a finite boundary-current
   identity with a Schur-complement sign missing;
3. the positive boundary-measure gate, because a global support theorem
   would imply the needed one-sided lobe balances for all Li tests at once.

## Status

Closed as a dual normal form.  The exact new formula is the cumulative
prime-pole balance (2) and the lobe duality (6)--(8).

A1 remains open.  The sharpened missing theorem is the signed dual lobe
bound (9), proved from the arithmetic balance \(B_a\) before applying
absolute values.
