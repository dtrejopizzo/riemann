# An arithmetic Frobenius family on semilocal idele class groups

`C_S` is the quotient of the semilocal idele group of `Q` by the positive `S`-units, with the
convolution algebra, involution and functional `T` (the sum of Weil's local terms) of
[Paper 43](../43-row-a-torsion-theory/).

For each positive integer `n` whose prime divisors lie in `S`, the paper defines a probability
measure `Frob_n` on `C_S`: the Haar measure of a coset of a compact subgroup. It proves that

- `Frob_m ⋆ Frob_n = Frob_mn`, and the `Frob_n` with their adjoints generate a commutative inverse
  semigroup, a semilattice of free abelian groups; the family is not the restriction of a weakly continuous
  one-parameter semigroup of measures;
- on smooth approximations of `Frob_n`, the finite local terms of `T` sum to `Λ(n) n^{-1/2}` times
  the value of the archimedean profile at `1/n`; for `n` with two distinct prime divisors the
  support of `Frob_n` meets no local slice, and the archimedean term carries a congruence factor
  depending on the level of the approximation;
- `T` does not extend by weak continuity to `Frob_n`, nor to any probability measure that is a weak
  limit of densities;
- averaging over the maximal compact subgroup gives the radial family, on which `T` is given by
  the terms of the explicit formula at the places of `S`;
- the Hermitian form `T(F ⋆ G†)` on both families is computed, with its divergence at the unit, and
  its finite-place part is indefinite on primitive radial functions;
- an integral complex attached to `n` has cohomology `Z/Φ_n(1)`, where `log Φ_n(1) = Λ(n)`.

What is known: the coefficients `(log p) p^{-k/2}` are those of Weil's explicit formula, and the
reading of the local terms as intersections with the diagonal is due to Connes, Consani and
Marcolli. The family `Frob_n` and the statements above for composite `n` were not found in the
literature; they are elementary.

- Source: [`main.tex`](main.tex)
- PDF: [`arithmetic-frobenius-family-idele-class-group.pdf`](arithmetic-frobenius-family-idele-class-group.pdf) (35 pages)
