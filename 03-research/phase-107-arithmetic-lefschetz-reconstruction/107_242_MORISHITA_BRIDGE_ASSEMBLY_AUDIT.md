# 107.242 -- The Morishita bridge: what it assembles and what it destroys

## 0. Source

M. Morishita, *On a relation between Deninger's foliated dynamical systems
and Connes--Consani's adelic spaces*, arXiv:2508.15971v5, read in full
(`Puente/arXiv-2508.15971v5`), including the proof of Theorem 3.6.

Purpose: decide whether row (b) -- Deninger's correspondence -- can be
assembled as a component of the row-(a) construction, which lives in the
Connes--Consani adelic setting.

## 1. What the bridge actually is

Morishita constructs, for a finite abelian \(F/\mathbb Q\),

\[
 \Psi_F:\ \mathfrak X_F\longrightarrow\mathscr X_F ,
 \tag{1.1}
\]

from the Deninger system to the Connes--Consani adelic space.  The
construction: for a point \((\mathfrak P,P)\) of \(\dot X_{\mathbb Q^{ab}}
(\mathbb C)\), restrict the ring homomorphism
\(P:W_{\rm rat}(\kappa(\mathfrak P))\to\mathbb C\) to the roots of unity,

\[
 \psi(\mathfrak P,P):=\chi_{(\mathfrak P,P)}
 \in\dot H={\rm Hom}(\mu_\infty,\mu_\infty)\cong\widehat{\mathbb Z},
\]

pass to the colimit over \(\mathbb N\) ordered by divisibility to get
\(\check H\cong\mathbb A^{\rm f}\), cross with \(\mathbb R_+\), quotient by
\(\mathbb Q_+\), and compose with the inversion \(\tau\) on the archimedean
component.

> **Theorem 3.6 (Morishita).**  \(\Psi_F\) is a continuous map, \(\mathbb
> R_+\)-**anti**-equivariant and \({\rm Gal}(F/\mathbb Q)\)-equivariant, the
> square with the covering maps commutes, and an \(\mathbb R_+\)-orbit
> \(\gamma_p\subset\Gamma_p\) is sent **onto** the circle \(C_p\).

## 2. What this assembles -- the indexing dictionary

The theorem does give a genuine and usable identification at one level.

> **Corollary 2.1 (orbit dictionary).**  Deninger's periodic packet
> \(\Gamma_p\) and Connes--Consani's circle \(C_p\) are matched by
> \(\Psi_{\mathbb Q}\), compatibly with the Galois action and with the flow
> up to inversion.  Both carry period \(\log p\).

This is not decorative for Phase 107.  107_239 §2 localizes the corner
trace at exactly the closed fibers whose isotropy is \(\mathbb Q_v^\times\),
i.e. at the circles \(C_p\).  Corollary 2.1 says these are precisely the
images of Deninger's periodic orbits.  So:

> The local terms of the corner pairing \(I_\partial\) are indexed by
> Deninger's periodic orbits.

Row (b) is therefore assembled **as an indexing structure**: the primes, the
periods \(\log p\), and the Galois action agree on both sides.

## 3. What it does not assemble

Three limitations, all read off the statement and proof.

**(a) It is a map, not an equivalence.**  Morishita claims neither
injectivity nor surjectivity of \(\Psi_F\); he proves that specified orbits
map *onto* specified circles.  Nothing in the paper makes \(\Psi_F\) proper,
flat, or finite.  Consequently there is no pushforward or pullback of cycles,
and a correspondence on one side does not transport to the other.

**(b) It is restricted to abelian extensions of \(\mathbb Q\).**  Deninger's
theory covers arbitrary arithmetic schemes; the bridge is built inside
\(\mathbb Q^{ab}\) using the cyclotomic character.  A square
\(\overline{\Spec\mathbb Z}\times\overline{\Spec\mathbb Z}\) is not in that
range.

**(c) The flow is anti-equivariant.**  Cosmetic -- absorbed by \(r\mapsto
r^{-1}\) -- but it must be tracked in any composite, since 107_239 fixes a
direction through \(\theta(u)\xi(a)=\xi(u^{-1}a)\).

## 4. The sharp obstruction: the bridge collapses the transverse direction

The proof of Theorem 3.6(2) works as follows.  For \(\mathfrak P\) over
\(p\), \(\kappa(\mathfrak P)=\overline{\mathbb F}_p\), so
\(\mu_\infty(\kappa(\mathfrak P))=\mu_{(p)}\) has order prime to \(p\).
Hence \(\chi_{(\mathfrak P,P)}=\chi_a\) with

\[
 \boxed{a_p=0 .}
 \tag{4.1}
\]

That vanishing is *why* the orbit lands on \(C_p\): \(C_p\) is cut out by the
vanishing of the \(p\)-component.

Now compare with 107_239 (2.2).  There the local Weil term arises as a
transverse kernel trace at the closed fiber,

\[
 \int_{\mathbb Q_v}\delta((u-1)x)\,dx=|1-u|_v^{-1},
 \tag{4.2}
\]

with transverse space \(\mathbb Q_v\).  At \(v=p\) the transverse space is
\(\mathbb Q_p\), i.e. exactly the \(p\)-component.

> ### Theorem 4.1 (transverse collapse)
>
> \(\Psi\) sets the \(p\)-component to zero at every point over \(p\).  The
> \(p\)-component is the transverse space whose kernel trace produces the
> local factor \(|1-u|_p^{-1}\) of the corner pairing.  Therefore \(\Psi\)
> collapses precisely the direction that carries the local intersection
> multiplicity.

**Proof.**  (4.1) is Morishita's computation.  (4.2) is the identification in
107_239 §2.  The local factor \(|1-u|_p^{-1}\) is nonconstant on
\(\mathbb Q_p^\times\), so the collapsed direction is not a null direction of
the pairing. \(\square\)

### Consequence

The bridge transports *which* orbits exist, and nothing about *how they
meet*.  It cannot carry (b) into the intersection theory of (a), and it
cannot be used to import the value \(N\) either -- it destroys the data that
produces \(N\) fiberwise.

This is not a defect of Morishita's theorem, which answers the question
Deninger posed in §7 of [D7].  It is a statement about what that answer can
and cannot be used for here.

## 5. Status of row (b)

\[
 \boxed{\texttt{ROW\_B\_STATUS: SOLVED\_AS\_OBJECT, ASSEMBLED\_AS\_INDEXING\_ONLY}}
\]

* **Solved as an object.**  Deninger's \(W_{\rm rat}(X)\) exists and gives
  periodic orbits in bijection with closed points, of length
  \(\log|\kappa(x)|\).  Nothing remains to be constructed.
* **Assembled as indexing.**  Corollary 2.1: the corner pairing's local terms
  are indexed by Deninger's orbits, Galois-equivariantly.
* **Not assembled as a correspondence.**  Theorem 4.1: the bridge collapses
  the transverse direction, so no cycle-level transport is available through
  it.

What would be needed to assemble (b) fully: a map between the two settings
that is transverse-preserving at closed fibers, or a construction of the
Frobenius graphs directly inside the row-(a) divisor group.  The second is
the candid route, and it is a row-(a) task.

## 6. Verifier

`107_242_morishita_bridge_assembly_audit.py` checks the two group-theoretic
facts carrying the argument -- that \(\overline{\mathbb F}_p^\times=\mu_{(p)}\)
has order prime to \(p\), and that \(\chi_a(\mu_\infty)\subseteq\mu_{(p)}\)
iff \(a_p=0\) -- that the orbit periods \(\log p\) agree on both sides, and
that the transverse local factor \(|1-u|_p^{-1}\) is nonconstant, so
Theorem 4.1 collapses a non-null direction.
