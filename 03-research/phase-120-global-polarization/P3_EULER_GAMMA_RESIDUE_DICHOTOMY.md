# Phase 120 — Euler--Gamma residue dichotomy

## Status

This note resolves the ordinary Landau--Ginzburg/Grothendieck-residue
implementation of the infinite Gorenstein target.  It proves an algebraic
dichotomy: isolated singularities have the polarization theorem but collapse
the faithful Frobenius tower; non-isolated singularities retain the tower but
do not carry the required perfect residue pairing.  Therefore the remaining
object must be an infinite energy form, not a limit of socle residues.

## 1. The contact residue is canonical but singular

For one place \(p\), put \(e_{p,j}=x_p^j\).  The contact moments have the
literal residue representation

\[
 \operatorname {Res}_{x_p=1}
 x_p^{i+j}\frac{\log p\,dx_p}{x_p-1}=\log p.       \tag{1.1}
\]

Thus the constant rank-one place block is not an arbitrary trace: it is the
simple-pole residue at the augmentation character \(x_p=1\).  Its radical is

\[
 \left\{\sum_j a_jx_p^j:\sum_j a_j=0\right\},      \tag{1.2}
\]

so it cannot itself be a Poincare-duality polarization.  The missing global
term must remove this radical while coupling the different augmentation
fibres by the quarter-Gamma datum.

## 2. Isolated-potential no-go

### Theorem 2.1

Let \(W\) be a holomorphic or formal potential with an isolated critical
point and finite Milnor number, and let

\[
 J(W)=\mathcal O/(\partial_1W,\ldots,\partial_dW)
\]

be its Jacobian algebra.  There is no injective multiplicative realization

\[
 \Gamma_{p^j}\longmapsto x_p^j\in J(W),\qquad j\geq0,                \tag{2.1}
\]

of a faithful Frobenius prime-power tower.

#### Proof

The isolated-critical-point hypothesis makes \(J(W)\) finite dimensional.
Multiplication by \(x_p\) is consequently an algebraic endomorphism.  If
\(m_p(t)=\sum_{k=0}^r a_kt^k\) is its minimal polynomial, then

\[
 \sum_{k=0}^r a_kx_p^{j+k}=0
\]

for every \(j\geq0\).  Hence the labelled powers are linearly dependent and
cannot represent the noncollapsed tower faithfully.  This contradiction is
independent of the choice of residue primitive form.  QED.

The theorem applies to every finite-dimensional Artinian Gorenstein carrier,
not only to polynomial complete intersections.  It is therefore stronger
than the depth-transition obstruction: a single isolated potential cannot
replace the incompatible finite socle traces.

## 3. Non-isolated repair loses the sign theorem

If \(W\) has an infinite-dimensional Jacobian algebra, the algebraic
obstruction in Theorem 2.1 disappears.  But the usual Grothendieck residue is
perfect precisely under the finite/isolated hypothesis.  For a non-isolated
critical locus the Koszul quotient is not finite over the base, the local
residue is not a canonical nondegenerate trace on the full quotient, and the
finite-dimensional Lefschetz/Hodge--Riemann theorem used in the Gorenstein
candidate does not apply.

Passing to finite isolated approximants does not repair this: Theorem 4.1 of
`P3_GORENSTEIN_FUSION_ALGEBRA_GATE.md` proves that their normalized socle
traces are incompatible with the depth quotients.  Thus there is no hidden
cofinal residue theorem waiting behind the truncations.

## 4. Factorization obstruction to the Green term

Suppose a proposed global potential is a sum of independent local potentials,

\[
 W=W_\infty+\sum_pW_p.                              \tag{4.1}
\]

Whenever its residue pairing is defined, Thom--Sebastiani factorization makes
the pairing a tensor product of local pairings.  After restricting to the
one-place contact sectors, this produces either block diagonal place terms or
products of independent local moments.  It cannot produce the forced
nonseparable cross-place compression of

\[
 \log\pi-\Re\psi(1/4+i\tau/2).                     \tag{4.2}
\]

An interaction term is therefore mandatory.  Choosing that term by matching
(4.2) after computing row (c) would merely insert the desired Green
functional.  A valid interaction must instead be forced by the additive
Euler generator and the two Tate boundary functionals before the trace
comparison.

## 5. Consequence: the carrier type is forced

Combining Sections 1--4 leaves one possible algebraic type:

1. the faithful algebra is the untruncated monoid algebra of prime powers;
2. the contact functional is the canonical augmentation residue (1.1);
3. the global completion is not a socle trace, but a closed energy form on a
   Hilbert completion of the augmentation ideal;
4. its finite-place functoriality must be with respect to the additive
   generator \(L_S\), because \(L_{S\cup T}=L_S+L_T\) is the only exact
   cofinal law;
5. the quarter-Gamma interaction must enter as the boundary energy of the two
   Tate functionals, not as an independently fitted mixed residue.

This changes the active question.  The target is no longer an ``infinite
socle''.  It is a source-defined Dirichlet form

\[
 \mathcal E_S(G)=\mathcal E_\infty(G)+
                 \sum_{p\in S}(\log p)\mathcal E_p(G)              \tag{5.1}
\]

whose state space and boundary quotient are functorial in \(L_S\), and whose
Green identity on \(F=(-\partial_t^2+1/4)G\) yields the signed Weil supply.
The sign must follow from closedness/Markovianity of (5.1), not from a residue
chosen to equal that supply.

## 6. Classification

- simple-pole realization of the local contact: **PROVED**;
- isolated Landau--Ginzburg realization of the faithful tower:
  **IMPOSSIBLE**;
- recovery by finite isolated approximants: **IMPOSSIBLE**;
- separated local potential as source of the forced Green coupling:
  **IMPOSSIBLE**;
- infinite additive-generator energy form: **THE ONLY SURVIVING VERSION**;
- construction of its Tate boundary quotient and global square: **OPEN**.
