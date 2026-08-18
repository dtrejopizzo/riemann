# 107.148 -- The Connes--Consani Jacobian cannot receive the signed source divisor group

## 1. Result

Connes--Consani, *On the Jacobian of* \(\overline{\operatorname{Spec}\mathbb Z}\)
(arXiv:2602.15941), construct a Picard monoid whose elements are
isomorphism classes of torsion-free rank-one subgroups of \(\mathbb Q\).
Addition of generalized divisors corresponds to tensor product.  Their
arithmetic Abel--Jacobi map sends

\[
 p\longmapsto H_p:=\mathbb Z[1/p].
 \tag{1.1}
\]

The source of Phase 107 is instead the signed free abelian group

\[
 \operatorname{Div}_{\mathrm{EF}}
 =\mathbb ZF_{\rm v}\oplus\mathbb ZF_{\rm h}
 \oplus\mathbb Z\Delta\oplus\mathbb ZZ_\infty
 \oplus\bigoplus_{p,k}\mathbb Z Z_{p,k}.
 \tag{1.2}
\]

> **Theorem (signed-divisor no-go).**  There is no additive map
> \[
>  \mathcal A:\operatorname{Div}_{\mathrm{EF}}
>  \longrightarrow\operatorname{Pic}(\overline{\operatorname{Spec}\mathbb Z})
> \]
> into the Connes--Consani Picard monoid that sends a prime-return
> generator to its published Abel--Jacobi boundary class \(H_p\).
> Passing to the Grothendieck group does not repair the problem: every
> \(H_p\) becomes zero there.

Thus the Connes--Consani Jacobian is a geometric support and a monoidal
boundary target, but it is not the signed Picard/height group required by
`107_11`.  A successful III-B construction needs a different group-valued
refinement carrying nontrivial prime-return classes and their inverses.

## 2. The published idempotent relation

The divisor corresponding to \(H_p\) is \(D_p=\infty[p]\).  Since
generalized divisor addition uses \(\infty+\infty=\infty\),

\[
 D_p+D_p=D_p.
 \tag{2.1}
\]

Equivalently, localization is idempotent:

\[
 H_p\otimes_{\mathbb Z}H_p
 \cong\mathbb Z[1/p]=H_p.
 \tag{2.2}
\]

Connes--Consani explicitly call the image of configurations of primes
the idempotent stratum of the arithmetic Jacobian.

## 3. Group-to-monoid obstruction

### Lemma 3.1

Let \(G\) be an abelian group and \(M\) a commutative monoid.  The image
of every monoid homomorphism \(f:G\to M\) is contained in the unit group
\(M^\times\).

### Proof

For \(g\in G\),

\[
 f(g)+f(-g)=f(0)=0_M.
\]

Thus \(f(-g)\) is an additive inverse of \(f(g)\) in \(M\), so \(f(g)\)
is a unit. \(\square\)

### Lemma 3.2

The class \(H_p\) is not a unit of the Connes--Consani Picard monoid.

### Proof

In generalized-divisor coordinates, the coefficient \(\infty\) at
\(p\) cannot be cancelled because \(\infty+n=\infty\) for every allowed
coefficient \(n\).  Hence \(D_p+D\) can never be principal with finite
coefficient at \(p\). \(\square\)

Applying Lemma 3.1 to (1.2) and Lemma 3.2 to (1.1) proves the first
claim of the theorem.

## 4. Group completion collapses the prime classes

Let \(K(M)\) be the Grothendieck group of the Picard monoid.  Relation
(2.1) becomes

\[
 [H_p]+[H_p]=[H_p].
\]

Cancellation in \(K(M)\) gives

\[
 [H_p]=0.
 \tag{4.1}
\]

Therefore a realization through the published Abel--Jacobi classes kills
every finite-prime generator after group completion.  It cannot be
faithful, preserve return lengths \(k\log p\), or transport the Paper A
pairing.

## 5. Relation with Morishita's bridge

Morishita's map \(\Psi_F:\mathfrak X_F\to\mathscr X_F\) does not itself
create a forbidden kernel on the current source:
\(\operatorname{Div}_{\mathrm{EF}}\) contains one connected symbol
\(Z_{p,k}\) per prime power, not one symbol for every circle
\(\gamma_{p,\bar a}\) in Deninger's packet.  Differences between packet
circles are outside the present source domain.

But the bridge cannot repair (4.1).  On the Connes--Consani side it lands
on the periodic orbit represented by the same idempotent boundary class
\(H_p\).  Thus Morishita is adequate for matching periodic support in row
(b), but not for the signed group-valued Picard realization needed by
rows (a), (c), and (d).  Packet monodromy must land in a new
non-idempotent target if it is to contribute arithmetic information.

## 6. Scope

This theorem rejects the published Connes--Consani Jacobian monoid, and
its ordinary Grothendieck group, as the codomain of `107_11`.  It does
not reject a derived or spectral enhancement with non-idempotent prime
classes, a genuine metrized Picard group on a regular proper arithmetic
surface, or an extension retaining Deninger's packet monodromy.

