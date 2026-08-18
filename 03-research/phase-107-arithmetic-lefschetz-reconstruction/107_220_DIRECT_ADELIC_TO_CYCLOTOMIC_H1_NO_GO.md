# 107.220 -- No direct additive morphism from adelic H1 to cyclotomic H1

## 1. Published source object

Connes--Consani define the first cohomology of an Arakelov divisor by

\[
 H^1(D)=(H\mathbb A_\mathbb Q,\mathcal R_D),
 \tag{1.1}
\]

where the underlying \(\mathbb S[\pm1]\)-module is the
Eilenberg--Mac Lane module of the additive adele group, and
\(\mathcal R_D\) is the tolerance relation induced by

\[
 \mathbb Q\times\mathcal O(D)\longrightarrow\mathbb A_\mathbb Q,
 \qquad(q,a)\longmapsto q+a.
\]

The Eilenberg--Mac Lane embedding of abelian groups into
\(\mathbb S\)-modules is full and faithful.  Therefore any morphism from
(1.1) to an Eilenberg--Mac Lane target has an underlying additive group
homomorphism.

## 2. Divisibility obstruction

### Lemma 2.1

The additive group \(\mathbb A_\mathbb Q\) is divisible.

### Proof

Let \(N\ge1\) and \(a=(a_v)_v\in\mathbb A_\mathbb Q\).  Define
\(b_v=a_v/N\) at every place.  Outside the finite set consisting of the
nonintegral places of \(a\) and the primes dividing \(N\), one has
\(b_p\in\mathbb Z_p\).  Thus \(b\) is again an adele and \(Nb=a\).
\(\square\)

### Lemma 2.2

Every homomorphic image of a divisible abelian group is divisible.  The
only finite divisible abelian group is zero.

The second statement follows because, for a nonzero finite group \(G\),
any prime \(r\mid |G|\) makes multiplication by \(r\) nonsurjective.

### Theorem 2.3 (direct-comparison no-go)

Let \(C\) be any nontrivially twisted cyclotomic component complex of
107_217 or 107_219.  Since \(H^1(C)\) is finite,

\[
 \mathrm{Hom}_{\mathbf{Ab}}
 (\mathbb A_\mathbb Q,H^1(C))=0.
 \tag{2.1}
\]

Consequently every morphism of tolerant \(\mathbb S[\pm1]\)-modules

\[
 H^1(D)\longrightarrow H(H^1(C))
\]

has zero underlying additive map.  It cannot recover the nonzero
cyclotomic torsion of 107_217--107_219.

This obstruction is independent of the tolerance radius and of the
Arakelov divisor \(D\).

## 3. Correct surviving interfaces

The result rejects only the direct additive comparison proposed after
107_219.  It does not reject:

1. applying Pontryagin duality first, turning the adelic cokernel into a
   lattice of characters;
2. a derived functor such as \(\mathrm{Ext}\,\), where divisible
   source groups and finite torsion can interact differently;
3. a nonlinear evaluation into a moduli stack;
4. a correspondence rather than a homomorphism.

The published Serre duality

\[
 H^0(K-D)\simeq
 \underline{\mathrm{Hom}}(H^1(D),H^1(K))
\]

makes the first route canonical.  Therefore the next admissible
comparison must be constructed on the Pontryagin-dual character lattice,
not as a map out of \(\mathbb A_\mathbb Q\).

## 4. Falsifier

`107_220_direct_adelic_to_cyclotomic_h1_no_go.sage` recomputes the actual
finite cyclotomic \(H^1\) targets from the fixed mixed atlas of 107_219.
For every nontrivial target it detects a prime for which multiplication
is nonsurjective, proving that the target has no nonzero divisible
subgroup.  A lattice negative control verifies that nonzero maps from
\(\mathbb Z\) do exist, so the obstruction is specifically divisibility
of the adelic source.

