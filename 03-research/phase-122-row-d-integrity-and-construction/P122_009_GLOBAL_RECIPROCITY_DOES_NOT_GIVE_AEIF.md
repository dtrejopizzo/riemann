# P122.009 — global reciprocity does not give active-ideal tangency

## Verdict

A product formula or global residue theorem for the oriented `K_2` class is
strictly weaker than the active Euler-ideal preservation required by AEIF.
It constrains the sum/product of local tame symbols, not each local symbol.
Therefore “add global reciprocity” does not complete the phase-121 carrier
unless an additional effectivity or one-sign theorem is proved.

## 1. Linearized product formula

For a global function field or a regular proper curve, the tame-symbol
reciprocity law has the form

\[
 \prod_x\partial_x\{f,g\}=1.                         \tag{1.1}
\]

For dual-number symbols `1+epsilon c_x`, equation (1.1) linearizes to

\[
 \sum_x c_x=0.                                      \tag{1.2}
\]

The phase-121 oriented Euler symbol at a simple divisor point has
`c_x=+/- K_F(x)`.  AEIF instead requires

\[
 K_F(x)=0.                                          \tag{1.3}
\]

at every zero of each active Euler factor.  Equation (1.2) does not imply
(1.3).

## 2. Exact counterexample

On the projective line, the meromorphic differential

\[
 \omega=c\,{dz\over z}-c\,{dz\over z-1},\qquad c\ne0,\tag{2.1}
\]

has two nonzero opposite residues and satisfies the global residue theorem.
The dual-number tame-symbol version is the pair

\[
 (1+\epsilon c,1-\epsilon c),                       \tag{2.2}
\]

whose product is one although neither symbol is trivial.  This is exactly
the antisymmetric port that row C forgets.

Thus properness and reciprocity alone permit the obstruction which F2 is
supposed to eliminate.

## 3. Finite active-prime consequence

For fixed `T`, only finitely many primes are active.  One scalar reciprocity
relation per active prime imposes only finitely many continuous linear
conditions on the infinite-dimensional Paley--Wiener source space.  Adding
the two Tate moments still leaves an infinite-dimensional common kernel.
Such relations cannot force an entire transform to vanish on every harmonic
lattice.

This dimension statement is not the main proof—the two-residue example
already separates reciprocity from local triviality—but it shows why adding
several active places does not repair the implication automatically.

## 4. What would make reciprocity sufficient

Reciprocity would imply local vanishing if D independently supplied a cone
or norm with both properties:

1. every oriented local contribution of an equality state lies in one
   pointed positive cone;
2. their global sum is zero.

Then pointedness would force every contribution to vanish.  But property 1
is precisely a new effectivity/polarization theorem; it is not contained in
Milnor `K_2`, the product formula, Real covariance or scalar supertrace.

## 5. Decision for the D-source track

The existing phase-121 `K_2` and Rees carriers cannot be closed merely by
asserting global tame reciprocity.  A surviving source candidate must add a
proved one-sign/effectivity law before scalarization, or a localization
theorem that makes each critical/active point separately testable.  Either
addition must have an independent geometric construction and a
Davenport--Heilbronn/shifted-pair falsifier.
