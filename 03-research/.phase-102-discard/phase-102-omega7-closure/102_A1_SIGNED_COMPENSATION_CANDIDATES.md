# 102 A1 signed compensation candidates

## Target

The signed core is

[
  C_n(T)
  =
  -n+\int_1^{e^T}(\psi(y)-y)f'_{n,0}(y)\,dy.
]

A1 asks for

[
  C_n(T(n))\ge-{3\over4}\lambda_n^{arch}
  \qquad(n\ge8).
]

## Candidate A: local prime-power blocks

One might group prime powers by intervals in `u=log m` and try to prove a
one-sided lower bound for each block.

This fails as a closure route because the Laguerre derivative changes sign
across its oscillatory region, while the prime powers have no local
positivity law strong enough to compensate the pole.  The required
cancellation is global.  A local block proof would need an additional theorem
that already identifies the missing global compensation.

Status: eliminated as an independent route.

## Candidate B: positive factorization of a finite kernel

One might look for a factorization

[
  C_n(T)+{3\over4}\lambda_n^{arch}
  =
  \|Q_{n,T}\|^2+\hbox{error}.
]

This route is circular unless `Q_{n,T}` is constructed from the Euler--Gamma
data and the error has a one-sided sign before Li positivity is known.  A
factorization obtained by choosing a nonnegative symbol is exactly the
Fejer--Riesz wall already recorded in paper 36.

Status: allowed only if the symbol positivity is proved independently.

## Candidate C: Mellin coboundary

The first viable candidate is a Mellin coboundary identity.  Let

[
  K_n(s)
]

be the Mellin transform of the Laguerre test after the pole subtraction.  A
successful identity would have the schematic form

[
  C_n(T)+{3\over4}\lambda_n^{arch}
  =
  \int_{\mathcal L}
  \Phi_n(s)\,
  d\log\left(\pi^{-s/2}\Gamma(s/2)\zeta(s)\right)
  +\mathcal R_{n,T},
]

followed by a symmetry transformation `s -> 1-s` that turns the main term into
a nonnegative boundary pairing and leaves

[
  \mathcal R_{n,T}\ge0.
]

This would retain pole, Gamma, primes, conjugation and boundary in one
object.  It is not yet proved.

## Candidate D: bordered Euler current

A second viable candidate is a bordered current with a distinguished pole
coordinate.  The desired theorem is:

For every `n>=8`, there exists an explicitly constructed finite-rank
Hermitian form `H_n` from the Euler--Gamma data such that

[
  C_n(T(n))+{3\over4}\lambda_n^{arch}
  =
  \det H_n^{border}/\det H_n^{base},
]

and the quotient is nonnegative by a structural identity that fails for an
off-line Euler--Gamma control.

This is close to the older RDI family, but the target is stricter: it must
output the literal Li inequality, not only a safety statement.

## Status

No candidate in this document proves A1 yet.  The local and finite-symbol
routes are eliminated as independent closures.  The surviving targets are:

- a Mellin coboundary whose boundary pairing is proved nonnegative;
- a bordered Euler current that maps directly to the Li core.

Either target is allowed to carry full RH strength.  The next mathematical
move is to prove one of these two identities, not to rename them.
