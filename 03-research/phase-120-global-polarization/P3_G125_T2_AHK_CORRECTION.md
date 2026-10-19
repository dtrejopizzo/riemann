# Phase 120 — G-125.B/T2 correction and the AHK persistence gate

## Status

Correction to `P3_SEMANTIC_AUDIT_AND_NEW_CONSTRUCTIONS.md`.  No claim of row
(d), and no paper change.

**Subsequent resolution.**  `P3_MATROID_FUSION_NO_GO.md` proves that the
repaired matroid carrier cannot encode faithful Frobenius iteration: flat join
is idempotent, whereas the exponent law is additive and faithful.  It also
shows that the configuration repair is D.142's factorial Fock descent.  Thus
Candidate A and the Morse variant are retired; the persistence lemma below
remains correct but has no compatible arithmetic matroid system to act on.

## 1. Two missed internal obstructions

The first audit did not route Candidates A and B through the strongest
pre-existing obstruction to their mechanism.

* `phase-41-build-G2/125-construction-of-the-intersection-form.md` already constructs
  the finite toy square $C_p\times C_p$, obtains Gram signature $(1,2)$,
  and proves negativity on its primitive plane.  Therefore a correct finite
  signature is not new evidence by itself.
* Its gap G-125.B invokes Babaee--Huh: tropical intersection objects can have
  the wrong Hodge signature.  A combinatorial or tropical intersection theory
  does not acquire Hodge--Riemann merely because it has a product, a degree
  map, Poincare duality or Hard Lefschetz.
* T2 of Doc 119 says that signature is not continuous under the regularized
  finite-to-infinite limits required here without a uniform spectral gap.
  Row (d) has no such gap available.

Consequently the original $\{2,3,4\}$ gate was necessary but insufficient.
It tested the arithmetic differential; it did not test the mechanism that
produces the sign or transports it cofinally.

## 2. The discrete-Morse overclaim

An acyclic matching produces a chain-homotopy-equivalent complex and identifies
critical cells.  Concentration of homology in odd degree does **not** imply
that a separately given bilinear form is negative on those critical cells.
The assertion

\[
 B_{\rm nuc,T}(f,f)=-\|P_1^{\rm crit}f\|^2
\]

needs a Hodge--Riemann theorem in addition to the matching.  Candidate B is
therefore demoted from an independent sign mechanism to a possible tool for
constructing the boundary complex and proving Poincare duality.

## 3. What AHK actually supplies

Adiprasito--Huh--Katz construct, for every finite loopless matroid $M$, a
finite graded Chow ring $A^*(M)$, a degree map and a cone of strictly convex
piecewise-linear Lefschetz classes.  They prove:

1. Poincare duality;
2. Hard Lefschetz for multiplication by a Lefschetz class;
3. the Hodge--Riemann sign on the primitive part.

The third item is independent of the first two.  Their introduction explicitly
contrasts the theorem with the Babaee--Huh tropical example, which satisfies
Poincare duality and Hard Lefschetz but not Hodge--Riemann.

The proof is finite and inductive: matroidal flips decompose the Chow ring into
the previous ring and contraction pieces; local HR on stars supplies HL; a
controlled deformation of the Lefschetz class transfers the HR signature while
the finite-dimensional Poincare pairing remains nondegenerate.  This is the
missing sign mechanism for Candidate A at a finite stage.  It does not supply
an infinite-rank theorem or resolve T2.

Primary source: K. Adiprasito, J. Huh, E. Katz, *Hodge theory for
combinatorial geometries*, Ann. of Math. 188 (2018), 381--452,
arXiv:1511.02888, especially the introduction, Theorems 6.19 and 8.8.

## 4. Repaired Candidate A: arithmetic Bergman configuration rings

The configuration proposal survives only in the following stronger form.
For every finite arithmetic contact set $S$, construct from rows (a)--(b),
without using $B_{\rm nuc}$, a finite combinatorial geometry $M_S$ such
that:

1. its flats are the nested collision strata of the compactified
   configuration space;
2. same-prime nesting realizes
   $C_{p^i}\circ C_{p^j}\to C_{p^{i+j}}$;
3. mixed-prime mergers have zero arithmetic residue;
4. the two Tate faces define the degree/augmentation map;
5. the exact archimedean datum defines a Lefschetz class
   $\ell_{\infty,S}$ before the trace comparison;
6. the intersection pairing in $A^*(M_S)$ subsequently satisfies

\[
 q_S(D_f,D_g)=B_{\rm nuc,S}(f,g).                     \tag{4.1}
\]

If $M_S$ is genuinely a matroid and $\ell_{\infty,S}$ is genuinely in its
strictly convex cone, AHK supplies finite Hodge--Riemann independently of
(4.1).  This evades Babaee--Huh by belonging to the special matroidal class,
not by asserting a tropical Hodge theorem for arbitrary surfaces.

The continuous Gamma boundary is the main structural danger.  It cannot be
inserted as a finite list of fitted weights.  Either it defines the Lefschetz
class functorially through the already constructed quarter-shift metric, or
the AHK repair fails.  Approximation by unrelated Riemann sums would re-enter
T2.

## 5. Algebraic persistence lemma: what would evade T2

The correct cofinal mechanism is not continuity of signatures.

**Lemma (pointwise HR persistence).**  Let
$(V_S,q_S)$ be a directed system of real vector spaces with injective maps
$i_{S,S'}$ such that

\[
 q_{S'}(i_{S,S'}x,i_{S,S'}y)=q_S(x,y)                 \tag{5.1}
\]

and $q_S\leq0$ on the compatible primitive subspaces $P_S$.  Then the
induced form is nonpositive on the algebraic colimit
$P_{\rm alg}=\varinjlim P_S$.

**Proof.**  Every $x\in P_{\rm alg}$ is represented in some $P_S$, and
$q(x,x)=q_S(x_S,x_S)\leq0$.  Compatibility (5.1) makes the value independent
of the representative.  No signature limit is taken.  $\square$

If $a_S=-q_S$ is compatible and closable in the row-(c) test topology, its
positive closure remains positive.  If row (c) identifies that closure with
$-B_{\rm nuc}$, row (d) follows by density.  Thus T2 is avoided only by the
ordered chain

\[
 \text{finite HR at every stage}
 \longrightarrow \text{exact isometric compatibility}
 \longrightarrow \text{positive form completion}
 \longrightarrow \text{row-(c) comparison}.          \tag{5.2}
\]

It is not avoided by convergence of finite Gram matrices or stability of
their inertia.

## 6. The strengthened finite/cofinal gate

The first gate now has two layers.

### Layer I — arithmetic discrimination on $S=\{2,3,4\}$

Before evaluating the Weil matrix:

1. build the collision lattice and prove it is the lattice of flats of a
   finite matroid $M_S$;
2. prove $C_2\circ C_2\to C_4$, zero $2$--$3$ residue and
   $\partial^2=0$;
3. construct $\ell_{\infty,S}$ and prove strict convexity without fitting a
   Gamma coefficient;
4. run the same construction for the shifted object $\Xi_a$.  Its local
   rank-two package must break a stated clause above.  If it still produces a
   matroidal HR package with the same trace comparison, the construction does
   not discriminate and is rejected.

The forced Gamma coefficient remains a death test but is not counted as
positive evidence, since the functional equation already pins it.

### Layer II — persistence, before any claim of progress toward row (d)

For $S\subset S'$, construct a graded ring map

\[
 A^*(M_S)\longrightarrow A^*(M_{S'})                 \tag{6.1}
\]

preserving product, degree, primitive subspace, Lefschetz class and the
pairing exactly.  Then prove closability of the positive algebraic-colimit
form.  A finite success without (6.1) has exactly the status of Doc 125's
$C_p\times C_p$ toy and is not promoted.

This is stronger than asking for a uniform spectral gap and better adapted to
row (d): nonpositivity, unlike a full signature count, passes pointwise through
an exactly compatible algebraic union.

## 7. Candidate C reduced to its actual one-page gate

No higher-Chow theory should be built before deciding whether its Mellin
parameter survives the pairing.  The coefficient pairing necessarily uses

\[
 \mathcal L_\tau\otimes\mathcal L_{-\tau}\longrightarrow\mathbf 1. \tag{7.1}
\]

There are only two outcomes:

1. the regulator cup/biextension pairing forgets $\tau$ after (7.1), or
   retains only a derivative at the central Eisenstein parameter; Candidate C
   collapses to the phase-15-arithmetic-hodge-index height/special-value obstruction and dies;
2. the harmonic Green representative depends nontrivially on $\tau$ and its
   local Fourier multiplier is exactly
   $\log\pi-\operatorname{Re}\psi(1/4+i\tau/2)$; this escapes Attempt 6,
   but the sign must then be shown to come from a regulator Hodge theorem and
   not from a Quillen/scattering determinant already audited.

The required calculation is therefore the twisted regulator pairing of one
graph cycle $Z_p$, as a function of $\tau$.  Until that function is
computed, Candidate C is a gate, not an implementation.

## 8. Revised verdict

* The original finite configuration gate remains a good arithmetic
  discriminator, especially when run simultaneously on $\Xi_a$.
* It is not evidence for row (d) unless the carrier is proved matroidal, AHK
  supplies HR, and exact transition maps give the algebraic persistence lemma.
* Discrete Morse may prove cellular equivalences and Poincare duality; it
  cannot provide the Hodge--Riemann sign by itself.
* Candidate C should receive exactly one calculation: whether $\tau$
  survives.  No surrounding higher-Chow construction is justified first.

The active mathematical target is now sharper:

\[
 \boxed{
 \begin{gathered}
 \text{construct }M_{\{2,3,4\}},\ \ell_{\infty},
 \text{ and its arithmetic collision orientation};\\
 \text{prove the local rank-two }\Xi_a\text{ package violates one axiom};\\
 \text{construct the exact transition }A^*(M_S)\to A^*(M_{S'}).
 \end{gathered}}                                      \tag{8.1}
\]

Only the conjunction addresses arithmetic discrimination, G-125.B and T2.
