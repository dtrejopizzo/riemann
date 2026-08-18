# 107.243 -- Cartwright's tropical Hodge index: the missing row-(d) input, and the exact transfer target

## 0. What was found

107_241 produced the Hodge-index statement for the corner pairing *from the
explicit formula*, hence as an equivalence with RH, hence doing no work.  The
missing piece was a Hodge index proved **from geometry**.

It exists, and has since 2015.

> D. Cartwright, *Combinatorial tropical surfaces*, arXiv:1506.02023,
> **Theorem 1.1.**  Let \(\Delta\) be a tropical surface which is locally
> connected through codimension 1.  Then the intersection pairing on
> \(NS(\Delta)\otimes_{\mathbb Z}\mathbb Q\) is a nondegenerate bilinear form
> whose matrix has **at most one positive eigenvalue**.

Read from source (`mas-papers/arXiv-1506.02023v1/surfaces.tex`).  The proof
is entirely combinatorial.  The same paper proves Noether's formula and
constructs a **tropical exponential sequence**, giving
\(\Pic_{\rm ridge}(\Delta)\cong H^1(\Delta,\mathcal A_{\mathbb Z})\) --
i.e. an \(H^1\), which is what 1805.10501 declares open.

## 1. The architecture of Cartwright's proof

Three ingredients, all verified below.

**(i) Locality.**  \(M_\Delta\) is **block diagonal**, one block \(M_v\) per
vertex (`prop:matrix-intersections`: "Because of the block diagonal structure
of \(M_\Delta\), the product \(\mathbf f^TM_\Delta\mathbf f'\) computes the
sum of local contributions for each vertex \(v\)").

**(ii) A local index axiom.**  Each block has **exactly one positive
eigenvalue** (`lem:local-matrix`).  At a vertex this holds *by the definition
of a tropical complex* -- it is an axiom.  At an interior point of an edge it
is proved: the local matrix has rank 2 (kernel of dimension
\(d=\#\link_\Delta(e)\)) and contains the principal submatrix
\(\left(\begin{smallmatrix}0&1\\1&a\end{smallmatrix}\right)\), of determinant
\(-1\), indefinite for every \(a\).

**(iii) An inertia count in which the vertex number cancels.**  He exhibits a
subspace on which the form is
\(\left(\begin{smallmatrix}0&I&0\\I&0&0\\0&0&M_H\end{smallmatrix}\right)\),
with \(n+k-1+m\) positive eigenvalues, inside a form with exactly \(n\)
positive eigenvalues.  Sylvester gives \(n+k-1+m\le n\), i.e.

\[
 \boxed{k+m\le1 .}
\]

> **The theorem is: one positive eigenvalue per place, plus Sylvester's law,
> plus a rank count.**

This is the inertia-additivity / Schur-complement family of arguments
developed independently in Phase 106.  The technique is already owned.

## 2. The chain this completes

Combining with 107_241 Theorem 3.1, which computes for the corner pairing

\[
 n_+(\overline I_\partial)=1+\#P,
 \qquad \#P=\tfrac12\#\{\text{off-line zeros}\},
\]

one gets the implication

\[
 \boxed{
 \text{(the DC corner object is a tropical surface)}
 \;\Longrightarrow\;
 n_+\le1
 \;\Longrightarrow\;
 \#P=0
 \;\Longrightarrow\;
 \mathrm{RH}. }
 \tag{2.1}
\]

So row (d) is no longer an unknown *statement*.  The entire remaining
question of the program is the hypothesis of (2.1).

## 3. Two obstructions, and a correction

### 3.1 Finite generation -- real, and it stands

`cor:finitely-generated`: "Since \(\Delta\) is a **finite complex**, both
\(\Pic_{\rm ridge}(\Delta)\) and \(H^2(\Delta,\mathbb Z)_{\rm tors}\) are
finitely generated, so \(NS(\Delta)\) is also finitely generated."

By 107_224, every homomorphism \((\mathbb R,+)\to\) finitely generated
abelian group vanishes.  So a naive transfer, with \(NS\) finitely generated,
cannot see the archimedean divisor \(\mathbb R\{\infty\}\).

### 3.2 Infinitely many places -- the deeper issue

Step (iii) counts \(n\) = number of vertices.  For \(\Spec\mathbb Z\) the
places are infinite in number, both sides of \(n+k-1+m\le n\) diverge, and
the argument is vacuous as stated.

**But \(n\) cancels.**  The content is the *excess* \(k+m-1\le0\).  And
107_239 already constructs a relative trace built precisely to subtract a
divergent generic contribution,

\[
 \mathfrak T_S(h)=\lim_{\Lambda\to\infty}
 \bigl(\Tr(\theta(h)R_\Lambda)-2h(1)\log\Lambda\bigr).
\]

So the natural target is a **renormalized inertia count**, in which the
divergent place-count is subtracted the same way 107_239 subtracts
\(2h(1)\log\Lambda\).  This is a well-posed question, not a wish.

### 3.3 Correction to the earlier reading

Earlier in this phase the archimedean place was treated as blocked by
107_224.  That conclusion was drawn for the wrong demand.  107_224 forbids a
**homomorphism** \(\mathbb R\{\infty\}\to NS\) with \(NS\) finitely
generated.  Cartwright's proof does not need that; it needs a **local block
at \(\infty\) with exactly one positive eigenvalue**.  These are different
requirements, and the second is *not* refuted by 107_224 -- e.g.
\(\left(\begin{smallmatrix}0&1\\1&-2\end{smallmatrix}\right)\) has inertia
\((1,1)\).

Archimedean local intersection pairings exist in Arakelov theory (Green's
functions).  The archimedean place is therefore **not** excluded from this
route.  It is the first time in the phase that it looks attackable.

## 4. The transfer target, decomposed

The hypothesis of (2.1) splits into two local questions and one global one.

> **(P1) Finite local index.**  Does the local block at a finite place \(p\),
> arising from the corner term \(|1-u|_p^{-1}\) of 107_239 (2.2), have exactly
> one positive eigenvalue?
>
> **(P2) Archimedean local index.**  Is there a local block at \(\infty\)
> with exactly one positive eigenvalue, compatible with the Arakelov
> archimedean pairing?
>
> **(P3) Renormalized count.**  Does step (iii) survive with infinitely many
> places, after subtracting the divergent place-count in the manner of
> 107_239?

(P1) is a computation at a single prime and is the cheapest.  (P2) is a
construction, not obviously blocked.  (P3) is the genuinely new mathematics.

## 5. Status

Established here:

* the missing row-(d) geometric input exists (Cartwright Thm 1.1), read from
  source;
* an \(H^1\) exists in the tropical setting via the sheaf \(\mathcal A\) of PL
  functions and the tropical exponential sequence -- **the obstruction CC
  report in 1805.10501 is an artifact of the idempotent-monoid formulation,
  not of tropical geometry**;
* the implication chain (2.1);
* the proof architecture: locality + local index axiom + Sylvester;
* the correction of §3.3: the archimedean place is not excluded by 107_224.

Not established, and not promoted:

* that the DC corner object is a tropical surface in Cartwright's sense;
* (P1), (P2), (P3);
* `ROW_A_STATUS` remains `partial`; `ROW_D_STATUS` remains
  `HODGE_INDEX_TARGET_SPECIFIED`.  Nothing in this note proves RH.

## 6. Verifier

`107_243_cartwright_transfer_target.py` checks: the local edge block
\(\left(\begin{smallmatrix}0&1\\1&a\end{smallmatrix}\right)\) is indefinite
for every \(a\); that rank 2 together with an indefinite principal \(2\times2\)
forces exactly one positive eigenvalue, on 400 random rank-2 matrices; Cauchy
interlacing; that a block-diagonal form with \(n\) one-positive blocks has
exactly \(n\) positive eigenvalues; Sylvester's restriction inequality on 300
random trials; the inertia of the restricted form of step (iii); the chain
(2.1); and that an archimedean-type local block with inertia \((1,1)\) is not
excluded by 107_224.
