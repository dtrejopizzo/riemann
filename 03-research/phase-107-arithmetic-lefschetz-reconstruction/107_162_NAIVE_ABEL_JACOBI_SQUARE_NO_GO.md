# 107.162 -- No-go for the base-sheaf Abel--Jacobi square

## 1. Published input

Connes--Consani construct the visible Abel--Jacobi pullback

\[
 \pi:\mathcal X_{\mathbb Q}\longrightarrow
 \overline{\operatorname{Spec}\mathbb Z}.
\]

Its fiber over a finite prime \(p\) is the periodic orbit

\[
 C_p=\mathbb R/(\log p)\mathbb Z.
\]

Their 2026 arithmetic-Jacobian paper also constructs the structure sheaf
\(\mathcal O_{\overline{\operatorname{Spec}\mathbb Z}}\) and the divisor
modules \(\mathcal O(\mathcal D)\) on the base curve.  It does not define
a relative structure sheaf on \(\mathcal X_{\mathbb Q}\).

The first possible square is therefore the fiber product

\[
 Y=\mathcal X_{\mathbb Q}\times_{\overline{\operatorname{Spec}\mathbb Z}}
 \mathcal X_{\mathbb Q}
 \tag{1.1}
\]

equipped only with the inverse-image sheaf from the base.  This note
tests and rejects precisely that construction.

## 2. General lemma

Let \(\pi:Z\to X\) be a continuous map and equip \(Z\) with
\(\pi^{-1}\mathcal O_X\).  Put \(W=Z\times_X Z\), with structure sheaf
generated only by the two base pullbacks.  Since

\[
 \pi\circ\operatorname{pr}_1=\pi\circ\operatorname{pr}_2,
\]

both pullbacks are the same inverse-image sheaf on \(W\).

**Lemma.**  The zero locus of every local section of this sheaf is
fiber-saturated on its domain.  In particular, if a fiber \(Z_x\) has
no isolated points, neither its diagonal in \(Z_x\times Z_x\) nor the
graph of a self-homeomorphism of \(Z_x\) is locally principal in \(W\).

**Proof.**  A germ of the inverse-image sheaf is represented, after
shrinking, by a section \(f\in\mathcal O_X(U)\).  Its zero locus is

\[
 V\cap\pi_W^{-1}(V(f))
\]

on a suitable open \(V\subseteq\pi_W^{-1}(U)\).  Thus, once it vanishes
at a point over \(x\), it vanishes on the whole local fiber contained
in \(V\).  By contrast, the diagonal and any graph in
\(Z_x\times Z_x\) have empty interior when \(Z_x\) has no isolated
points.  They therefore cannot agree locally with such a zero locus.
\(\square\)

The statement is about Cartier/local-principal geometry.  Arbitrary
set-theoretic ideal sheaves could be imposed by hand, but that would add
the missing relative structure rather than derive it from the base.

## 3. Application to the arithmetic pullback

Every \(C_p\) is a circle and has no isolated points.  The fiber of
(1.1) at \(p\) is the torus

\[
 Y_p=C_p\times C_p.
\]

Hence neither

\[
 \Delta_p=\{(z,z):z\in C_p\}
\]

nor a graph

\[
 \Gamma_{p,n}=\{(z,nz):z\in C_p\}
\]

is a Cartier divisor for the base-pullback sheaf.  Consequently their
intersection number cannot be defined by this ringed-space structure.
The topological fiber product has the two rulings, but it does not have
the local equations required by rows (b)--(d).

This proves

\[
 \boxed{\text{the naive base-sheaf Abel--Jacobi square is not the Phase
 107 space.}}
\]

## 4. Exact requirement left open

A viable refinement must provide a sheaf \(\mathcal O_{\rm rel}\) on
\(\mathcal X_{\mathbb Q}\), or directly on its square, with sections
sensitive to the orbit coordinate and with local elements

\[
 t_1-t_2,\qquad t_2-n t_1
\]

or their characteristic-one analogues cutting the diagonal and graph.
It must also restrict compatibly to the CC divisor modules on the base,
retain the cross-prime monodromy of the universal Abel--Jacobi cover,
and admit the bounded integral dimension from 107_150--107_151.

Morishita's map cannot supply this by itself: Theorem 3.6 constructs a
continuous equivariant map of dynamical spaces, not a morphism of ringed
topoi or a pullback of relative function sheaves.

This no-go does not rule out the Abel--Jacobi architecture.  It isolates
the new mathematical object it needs: a relative orbit sheaf, rather
than another modification of the base divisor sheaf.

## 5. Falsifier

The verifier uses the actual prime atlas \(2,3,5,7,11\) and cyclic
approximations to the corresponding periodic fibers.  It enumerates
every fiber-constant zero mask and verifies that none cuts either the
diagonal or the multiplication graph.  A relative-coordinate negative
control cuts both, so the test can detect the missing structure rather
than merely restating the expected answer.
