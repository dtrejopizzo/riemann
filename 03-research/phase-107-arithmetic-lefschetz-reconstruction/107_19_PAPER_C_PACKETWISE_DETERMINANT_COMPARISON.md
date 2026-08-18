# 107.19 -- Paper C, Part VII: packetwise comparison with the determinant-line package

## 1. Purpose

This note is the first direct bridge from the concrete Part III
construction candidates back to the already proved Part I arithmetic
package.

The goal is precise:

\[
 \text{packetwise framed-cycle intersections}
 \longrightarrow
 \text{the determinant lines of `107_04`.}
 \tag{1.1}
\]

Until this comparison exists, the candidate models of `107_15`--`107_18`
remain only geometric scaffolding.  The present note turns them into an
explicit comparison problem with definite local equations.

## 2. Inputs

Four components are now available.

1. `107_04` gives the finite determinant line
   \(\langle Z_m,Z_n\rangle_{\rm fin}\) and its normalized Apostol
   support law.
2. `107_15` gives candidate realized cycles on \(\mathcal X_T^{(1)}\).
3. `107_17` gives local chart equations for diagonals and graph closures.
4. `107_18` replaces the abstract framing coordinate by finite rooted
   cyclotomic packets \((n,\chi)\).

These are enough to formulate packetwise determinant compatibility.

## 3. Packet cycles at level \(T\)

Fix \(T>0\), visible order set \(\mathcal N_T\), and visible rooted dual
\(X_T^\vee\) as in `107_18`.

### Definition 3.1: packet chart

For \(n\in\mathcal N_T\) and \(\chi\in X_T^\vee\) of exact order
\(n\), define the corresponding packet chart

\[
 \mathcal P_{n,\chi}
 \tag{3.1}
\]

to be the local framed-divisor chart labeled by \((n,\chi)\).

### Definition 3.2: packet incidence cycle

Inside the square chart of `107_17`, define the packet incidence cycle

\[
 \Gamma_{m;(n,\chi)}
 \tag{3.2}
\]

for \(m\in\mathcal N_T\) by the local equations

\[
 (n_2,\chi_2)=\mu_m(n,\chi),
 \qquad
 q_2=q_1,
 \qquad
 \theta_2=\theta_1.
 \tag{3.3}
\]

This is the packetwise refinement of the graph closure
\(\overline{\Gamma}_m^{\rm fr}\).

## 4. Forgetful map to cyclotomic order

The determinant package of `107_04` depends only on cyclotomic orders,
not on the extra rooted character label.

### Definition 4.1: order-forgetting projection

Define

\[
 \pi_{\rm ord}:\mathcal P_{n,\chi}\longrightarrow Z_n=V(\Phi_n)
 \tag{4.1}
\]

by forgetting the rooted label \(\chi\) and keeping only the visible
order \(n\).

At the level of charts, this is simply

\[
 (n,\chi,q,\theta)\longmapsto n.
 \tag{4.2}
\]

The map is not intended to be faithful.  Its role is to compare
packetwise geometry to the order-sensitive determinant lines already
proved in Part I.

## 5. Off-diagonal packet intersections

### Proposition 5.1: packet intersections factor through visible orders

For distinct visible orders \(m\neq n\), the off-diagonal intersection
behavior of packet charts \(\mathcal P_{m,\chi_1}\) and
\(\mathcal P_{n,\chi_2}\) factors through the order pair \((m,n)\).

Proof.  By `107_17`, off-diagonal packet geometry is determined by
finite equalities in the chart coordinates.  By `107_18`, the finite
action \(\mu_r\) changes the rooted label inside the visible torsion
packet but preserves the visible cyclotomic order bookkeeping needed for
the determinant support.  Therefore the local support question for
packet intersections reduces to the same order comparison as in the
cyclotomic strata of `107_04`.  \(\square\)

This is the basic structural reason the determinant comparison can even
be asked.

## 6. Packetwise support law

The first concrete compatibility statement is the support law.

### Conjecture 6.1: packetwise Apostol support

Let \(m,n\in\mathcal N_T\) with \(m\neq n\), and let
\(\chi_1,\chi_2\in X_T^\vee\) be visible rooted labels.  Then the local
packet intersection line

\[
 \langle \mathcal P_{m,\chi_1},\mathcal P_{n,\chi_2}\rangle_{\rm pkt}
 \tag{6.1}
\]

has normalized finite order

\[
 \mathrm{ord}_{\rm pkt}(m,\chi_1;n,\chi_2)
 =
 \begin{cases}
 \log p,&m/n=p^a,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{6.2}
\]

In particular, the rooted labels do not alter the prime-power support;
they only refine the visible packet decomposition above that support.

This is the packetwise lift of Proposition 5.1 of `107_04`.

## 7. Determinant-line comparison morphism

### Definition 7.1: packet-to-cyclotomic comparison line

For visible distinct orders \(m\neq n\), define the comparison morphism

\[
 \Comp_{m,n}^{\chi_1,\chi_2}:
 \langle \mathcal P_{m,\chi_1},\mathcal P_{n,\chi_2}\rangle_{\rm pkt}
 \longrightarrow
 \langle Z_m,Z_n\rangle_{\rm fin}
 \tag{7.1}
\]

to be the line map induced by the order-forgetting projections
\(\pi_{\rm ord}\) on the two packet factors.

The intended statement is not that the packet line equals the cyclotomic
line literally, but that after forgetting rooted refinement they carry
the same finite support and canonical norm.

### Conjecture 7.1: packetwise determinant compatibility

For \(m\neq n\), the comparison line (7.1) is an isomorphism on the
finite support and identifies canonical sections up to a rooted-unit
factor of norm \(1\).

Equivalently, after forgetting the rooted label,

\[
 \bigl\|\Comp_{m,n}^{\chi_1,\chi_2}(s_{\rm pkt})\bigr\|
 =
 \left|\mathrm{Res}(\Phi_m,\Phi_n)\right|.
 \tag{7.2}
\]

This is the first true comparison theorem target between Part III and
the proved Part I package.

## 8. Why the rooted labels should not change the norm

### Proposition 8.1: rooted refinement is expected to be unitary over the finite support

The visible rooted label \(\chi\) should refine components without
changing the local finite norm.

Proof sketch.  `106.164` realizes the rooted datum in one common compact
root space on which the multiplicative semigroup acts isometrically.
The finite determinant support of `107_04` depends only on which
cyclotomic orders meet, not on an additional metric weight attached to a
rooted character.  Hence the natural expectation is that changing
\(\chi\) only selects a packet component and contributes a norm-one
unitary factor.  This is not yet a proof, but it is the exact structural
prediction supplied by the rooted-Jacobian package. \(\square\)

This explains why the comparison isomorphism of Conjecture 7.1 is
plausible.

## 9. Diagonal caution

The diagonal comparison remains unresolved.

### Proposition 9.1: packetwise diagonal still lands in excess intersection

For any visible packet \((n,\chi)\), the self-intersection problem for
\(\mathcal P_{n,\chi}\) does not produce a finite scalar at the purely
finite stage.

Proof.  The order-forgetting projection takes the packet diagonal to the
cyclotomic diagonal \(Z_n\cap^{\mathbf L}Z_n\), which `107_04` proves is
an excess-intersection line rather than a scalar.  Packet refinement
cannot repair that at the finite stage without violating the coherence
rules of Part I.  \(\square\)

Thus the packet comparison respects the same diagonal stop test as the
original determinant package.

## 10. Compatibility with transpose and composition

The comparison must also preserve the categorical structure.

### Conjecture 10.1: packet transpose compatibility

The packet comparison line is invariant under exchanging the two packet
factors, matching Proposition 9.1 of `107_04`.

### Conjecture 10.2: packet composition compatibility

If packet correspondences compose through the local finite action
\(\mu_r\), then the packetwise determinant comparison is compatible with
iterated derived intersections after passing to visible orders.

These are the packetwise lifts of Propositions 9.1 and 9.2 of `107_04`.

## 11. What this note closes and what it does not

What is now closed:

1. the next bridge from Part III to Part I is precisely identified;
2. packet charts, graph packets, and order-forgetting maps are fixed;
3. the local support law, determinant comparison morphism, and diagonal
   caution are all formulated explicitly.

What remains open:

1. construction of the packet intersection line
   \(\langle \mathcal P_{m,\chi_1},\mathcal P_{n,\chi_2}\rangle_{\rm pkt}\);
2. proof of Conjectures 6.1 and 7.1;
3. proof that the rooted labels contribute only norm-one unitary
   refinements;
4. full comparison with the regularized global model
   \(\mathcal X_T^{(1)}\).

## 12. Next technical front

The natural next step is no longer to search for more abstract
compactification language.  It is to define the packet intersection line
directly from the local packet charts and to prove that its norm
descends to Apostol's resultant after forgetting the rooted labels.

That would be the first genuine proof-bearing comparison theorem inside
Part III.
