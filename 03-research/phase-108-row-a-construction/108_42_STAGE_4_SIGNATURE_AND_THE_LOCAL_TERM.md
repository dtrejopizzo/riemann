# 108.42 — Stage 4 geometry, II: signature of $B_\infty$, and the local term

## 0. Result

108_41 built $W_\infty=A\oplus A^-\oplus B\oplus B^*$ and $B_\infty$, and
showed the $B\oplus B^*$ block *can be made to match* Stage 0's polar block
by explicit stipulation (108_41 §4, revised: this is a construction fact,
not a theorem — see 108_41.md for the corrected status of G2). This note
finishes the geometry: it computes the full inertia of $B_\infty$ (G3),
attempts the local-term recovery (G4), and — the genuine new content of
this note — proves an unconditional structural incompatibility between
$W_\infty$ and Stage 0.

> \[
>  \boxed{\;n_+(B_\infty)=n_-(B_\infty)=\aleph_0\ \text{(both countably
>  infinite), unconditionally};\qquad
>  B_\infty\big(U,R(a)\big)=\pi\cot\tfrac{\pi a}2\ \text{(a true identity
>  that reduces to Mittag-Leffler and this construction's own input;
>  see §3.4)};}
> \]
> \[
>  \boxed{\;\text{if RH holds, no isometric injection }(W_\infty,B_\infty)
>  \hookrightarrow(V,\overline I_\partial)\text{ exists (§4, new).}\;}
> \]
>
> **G3 is proved, and its content is real:** the signature carries no
> arithmetic invariant — it is the same for every instance of this
> construction, with no dependence on any zero of $\zeta$ or $\xi$ — in
> sharp contrast to 107_241 Corollary 3.3, where the Stage-0 signature
> $(1,\cdot)$ is exactly equivalent to RH.
>
> **G4 is not established as a geometric result.** The identity
> $B_\infty(U,R(a))=\pi\cot(\pi a/2)$ is true (proved in §3), but it
> unwinds to the classical Mittag-Leffler expansion of $\cot$, applied to a
> vector $U$ whose coefficients were chosen, with no independent
> justification, to make the pairing sum reproduce exactly that expansion.
> The expansion itself states that $\cot$'s poles are at $2\Z$ with constant
> residue — which is 108_40 Proposition 6.1, the fact used to *define*
> $\mathrm{spec}\,\Theta$ in the first place. Nothing is produced here
> that was not already an input. §3.4 states this without softening.
>
> **The genuine new theorem is §4's embedding no-go**, built from Theorem
> 2.1 (G3, unconditional) and 107_241 Corollary 3.3 (RH-equivalence): the
> archimedean form is unconditionally *too positive* to sit inside Stage
> 0's corner form as a sub-object, if RH holds. This is not a proof of RH
> or of its negation, and is stated as a structural constraint on how a
> later stage could relate the two forms, not as a step toward RH.

## 1. The Gram operator is bounded and boundedly invertible

> ### Proposition 1.1
> $B_\infty$ (108_41 Def. 3.2) extends from the algebraic span of the basis
> to a bounded, self-adjoint, boundedly invertible operator $\mathcal G$ on
> the Hilbert space completion $W_\infty=A\oplus A^-\oplus B\oplus B^*$, via
> $B_\infty(x,y)=\langle \mathcal Gx,y\rangle$ ($\langle\cdot,\cdot\rangle$
> the $\ell^2$ inner product). Consequently $B_\infty$ is nondegenerate on
> all of $W_\infty$: $\mathrm{rad}\,B_\infty=\{0\}$.

**Proof.** On $A\oplus A^-$, $\mathcal G=2\cdot\mathrm{Id}$ by Def. 3.2's
diagonal entries: bounded (norm $2$), boundedly invertible (inverse
$\tfrac12\mathrm{Id}$). On $B\oplus B^*$, identify $B\cong B^*\cong\ell^2(
\Z_{\ge0})$ via $b_n\leftrightarrow b_n^*$; then $\mathcal G$ acts as the
swap $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ on each
matched pair $(b_n,b_n^*)$, i.e. $\mathcal G(x,y)=(y,x)$ for $(x,y)\in
B\oplus B^*\cong\ell^2\oplus\ell^2$: an isometric involution, hence bounded
(norm $1$) with bounded inverse (itself). The four sectors are
$B_\infty$-orthogonal (Def. 3.2), so $\mathcal G$ is the direct sum of these
two bounded, boundedly invertible pieces, hence itself bounded and boundedly
invertible on $W_\infty$. A bounded operator with bounded inverse has
trivial kernel, so $B_\infty(x,\cdot)\equiv0\Rightarrow\mathcal Gx=0
\Rightarrow x=0$. $\square$

This is the Hilbert-space-level nondegeneracy statement; 107_240/107_241
establish nondegeneracy of $\overline I_\partial$ on the numerical quotient
$V$ by a different (radical-quotient) route, but the conclusion — a
genuinely nondegenerate pairing, not merely one that is nondegenerate after
an ad hoc truncation — is the same type of statement.

## 2. G3: the inertia of $B_\infty$

> ### Theorem 2.1 (signature, blockwise)
> $B_\infty$ decomposes $B_\infty$-orthogonally as
> \[
>  W_\infty=\underbrace{\bigoplus_{n\ge0}\langle a_n\rangle\ \oplus\
>  \bigoplus_{n\ge1}\langle a_n^-\rangle}_{\text{definite sector}}
>  \ \oplus\ \underbrace{\bigoplus_{n\ge0}H_n}_{\text{hyperbolic sector}},
>  \qquad H_n:=\mathrm{span}\,\{b_n,b_n^*\},
> \]
> where each line $\langle a_n\rangle,\langle a_n^-\rangle$ carries the form
> $2x\bar x$ (signature $(1,0)$) and each $H_n$ carries the matrix
> $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ (signature
> $(1,1)$). Consequently
> \[
>  \boxed{n_+(B_\infty)=\aleph_0,\qquad n_-(B_\infty)=\aleph_0,}
> \]
> both realized as maximal definite subspaces of countably infinite
> dimension, and $\mathrm{rad}\,B_\infty=\{0\}$ (Prop. 1.1).

**Proof.** Orthogonality across sectors and within each is immediate from
Def. 3.2 (every cross term not listed there is $0$ by definition). The
definite sector is an orthogonal sum of countably many positive lines
(coefficient $2>0$ on the diagonal), contributing $(\aleph_0,0)$. Each $H_n$
is the $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$-block,
eigenvalues $\pm1$ (same computation as 108_41 Thm. 4.1 / 107_241 Thm.
3.1(1)), contributing $(1,1)$; summing over $n\ge0$ gives $(\aleph_0,
\aleph_0)$. Adding the two sectors: $n_+=\aleph_0+\aleph_0=\aleph_0$,
$n_-=0+\aleph_0=\aleph_0$. Nondegeneracy is Proposition 1.1. $\square$

### Contrast with Stage 0

107_241 Theorem 3.1 computes, for the *same style* of blockwise argument
applied to the Stage-0 pairing $\overline I_\partial$ on $V$,
\[
 n_+(\overline I_\partial)=1+\#P,\qquad n_-(\overline I_\partial)=1+\#L+\#P,
\]
where $\#P$ counts *off-line* zero-pairs of $\xi$ and $\#L$ counts on-line
zeros. Since $\xi$ has infinitely many nontrivial zeros, at least one of
$\#L,\#P$ is infinite, so Stage 0's inertia is *generically* also
$(\aleph_0,\cdot)$-type — but 107_241 Corollary 3.3 shows the sharp
statement $n_+=1$ (i.e. $\#P=0$, the *finite*, smallest possible value) is
**equivalent to RH**. The content of that equivalence is that the *size* of
$n_+$, specifically whether it collapses to $1$, encodes arithmetic
information.

Theorem 2.1 shows $B_\infty$ has no such collapse to look for: $n_+(B_\infty)
=\aleph_0$ unconditionally, forced by the pure existence of infinitely many
eigenvectors $a_n$ (each contributing a fixed positive line) — nothing about
zeros of any $L$-function enters. This is compatible with, and gives a
concrete, blockwise-computed instance of, the paper's premise that $\Phi$'s
purely archimedean content carries no arithmetic information: the geometric
invariant that *would* encode RH in Stage 0 (the finiteness/size of $n_+$)
is, in the purely archimedean model, forced to its generic infinite value by
construction, with nothing left to test. We state this as an illustration,
not a proof of the "no arithmetic content" claim (which is a statement about
$\Phi$, established by the given closed form, and not re-derived here).

## 3. G4: recovering $\pi\cot(\pi a/2)$ from $B_\infty$

This is the test that decides whether $W_\infty$ is real geometry or
decoration. We run it in full, including the one place it requires an
candid disclosure (the pairing vector $U$ below is not square-summable).

### 3.1 The attachment map

> ### Definition 3.1 (resolvent vector)
> For $a\in\C\setminus2\Z$ (avoiding $\mathrm{spec}\,\Theta\cup
> \mathrm{spec}\,\Theta^-=2\Z$), define $R(a)\in A\oplus A^-$ by
> \[
>  R(a):=\frac1a\,a_0\ +\ \sum_{n\ge1}\frac1{a+2n}\,a_n\ +\
>  \sum_{n\ge1}\frac1{a-2n}\,a_n^-.
> \]
> Equivalently, $R(a)=(a\cdot\mathrm{Id}-\Xi)^{-1}$ applied formally, where
> $\Xi:=\Theta\oplus\Theta^-$ has eigenvalue $2m$ at the basis vector indexed
> by $m\in\Z$ (identifying $a_n\leftrightarrow m=-n$, $a_n^-\leftrightarrow
> m=n$).

This *is* the attachment map $a\mapsto R(a)$ requested by (G4): it is the
resolvent of $\Xi$, the operator whose spectrum is exactly $2\Z$ — the pole
set of $s\mapsto\Gamma_\R(s)\Gamma_\R(-s)$, hence built from $\Gamma_\R$
alone, per Lemma 1.2. (108_07 is out of scope for this note by the reading
rules stated for this task; the map is specified here in full, self-
contained detail, and does not rely on 108_07's internal machinery.)

> ### Lemma 3.2 ($R(a)\in A\oplus A^-$ genuinely)
> $R(a)\in A\oplus A^-$ (square-summable) for every $a\in\C\setminus2\Z$.

**Proof.** The $n$-th coefficient is $O(1/n)$ as $n\to\infty$ (both in the
$a_n$ and $a_n^-$ series), so its square is $O(1/n^2)$, summable. $\square$

### 3.2 The pairing vector, disclosed

> ### Definition 3.3 (the constant vector $U$)
> Let $U:=\sum_{n\ge0}a_n+\sum_{n\ge1}a_n^-$ (all coefficients equal to $1$).

**Disclosure.** $U\notin A\oplus A^-$: its coefficients do not decay, so
$\sum|{\rm coeff}|^2=\infty$. $U$ is *not* a vector of the Hilbert space
$W_\infty$ constructed in 108_41. What follows makes the pairing
$B_\infty(U,R(a))$ rigorous anyway, by proving that the *specific, prescribed
grouping* of terms indexed by $n$ (not an arbitrary rearrangement) converges
absolutely — the same regularization classically used to define the
Mittag-Leffler expansion of $\cot$ itself, and no more.

> ### Lemma 3.4 (the grouped pairing converges absolutely)
> Define $\lambda_n(a):=2\big[\tfrac1{a+2n}+\tfrac1{a-2n}\big]$ for $n\ge1$
> and $\lambda_0(a):=2/a$. Then $\sum_{n\ge0}|\lambda_n(a)|<\infty$ for every
> $a\in\C\setminus2\Z$, and
> \[
>  \Lambda(a):=\lambda_0(a)+\sum_{n\ge1}\lambda_n(a)
> \]
> is a well-defined, absolutely convergent sum.

**Proof.** For $n\ge1$, $\lambda_n(a)=2\cdot\dfrac{2a}{a^2-4n^2}=
\dfrac{4a}{a^2-4n^2}$, so $|\lambda_n(a)|=O(1/n^2)$ as $n\to\infty$
(uniformly for $a$ in any fixed compact set avoiding $2\Z$), hence
$\sum_n|\lambda_n(a)|<\infty$ by comparison with $\sum1/n^2$. $\square$

Note the mechanism: the *individual* coefficients of $U$ against $R(a)$
(coefficient of $a_n$ times coefficient of $R(a)$ at $a_n$, i.e.
$1\cdot\tfrac1{a+2n}$) are only $O(1/n)$ — not summable alone, which is
exactly why $U$ is not in $W_\infty$ and the naive inner product diverges.
It is the *pairing of $a_n$ and $a_n^-$ together*, forced by their shared
index $n$, that cancels the leading $1/n$ behavior down to $O(1/n^2)$. This
is precisely why the construction needs the specific grouping by $n$ (i.e.
by shared eigenvalue-pair under $\Theta\leftrightarrow\Theta^-$), not an
arbitrary enumeration of $A\oplus A^-$.

> ### Definition 3.5 (the extended pairing)
> $B_\infty(U,R(a)):=\Lambda(a)$, i.e. the value of $B_\infty$ on $(A\oplus
> A^-)\times(A\oplus A^-)$, extended from the algebraic span (108_41 Def.
> 3.2, weight $2$ on each diagonal entry) to the pair $(U,R(a))$ by the
> specific $n$-grouped summation of Lemma 3.4. This is an extension of
> $B_\infty$ to $\widehat W_\infty\times W_\infty$ where $\widehat W_\infty
> \supsetneq W_\infty$ is the space of all formal series in the basis
> vectors for which this grouped sum converges; it is not claimed to be
> defined, or continuous, on all of $\widehat W_\infty\times W_\infty$, only
> on the specific pairs used here.

### 3.3 The identity

> ### Theorem 3.6 (G4: exact recovery of the local term)
> For every $a\in\C\setminus2\Z$,
> \[
>  B_\infty\big(U,R(a)\big)=\pi\cot\frac{\pi a}2 .
> \]

**Proof.** By Definition 3.5 and Lemma 3.4,
\[
 B_\infty(U,R(a))=\frac2a+\sum_{n\ge1}\Big[\frac2{a+2n}+\frac2{a-2n}\Big].
\]
The classical Mittag-Leffler partial-fraction expansion of the cotangent
(e.g. Ahlfors, *Complex Analysis*, or DLMF 4.19.6) states
\[
 \pi\cot(\pi z)=\frac1z+\sum_{n\ge1}\Big[\frac1{z-n}+\frac1{z+n}\Big],
\]
the series converging in the symmetric ($n$-grouped) sense of Lemma 3.4.
Substituting $z=a/2$: $\tfrac1{a/2-n}=\tfrac2{a-2n}$, $\tfrac1{a/2+n}=
\tfrac2{a+2n}$, $\tfrac1{a/2}=\tfrac2a$, so
\[
 \pi\cot\frac{\pi a}2=\frac2a+\sum_{n\ge1}\Big[\frac2{a-2n}+\frac2{a+2n}
 \Big]=B_\infty(U,R(a)). \qquad\square
\]

This is an **exact identity of the two entire meromorphic functions of $a$
on both sides** (both sides are recognized in closed form; the equality is
not asymptotic). §4 verifies it numerically by confirming $O(1/N)$
convergence of the truncated sum to $\pi\cot(\pi a/2)$ under refinement, at
a real and a complex value of $a$ — a convergence test, not a threshold.

### 3.4 What Theorem 3.6 actually reduces to — retracting the "real test" framing

An earlier draft of this note read Theorem 3.6 as evidence that "the
geometry is not decorative on this test." **That sentence is retracted.**
It is not supported, for the following reason, stated in full rather than
left implicit.

**The reduction chain.** Unwind Definitions 3.1, 3.3, 3.5 and Theorem 3.6's
own proof:

1. $R(a)$ is, by Definition 3.1, exactly the sequence of residues of the
   resolvent of $\Xi=\Theta\oplus\Theta^-$ — equivalently, by Lemma 1.2 of
   108_41, the sequence $\big(\tfrac1{a-\lambda}\big)_{\lambda\in2\Z}$ over
   the pole set of $\Gamma_\R(s)\Gamma_\R(-s)$.
2. $U$ is, by Definition 3.3, the all-ones sequence over the same index
   set. **This is not a canonical or derived choice.** For *any* sequence
   $(c_n)_{n\ge0}\cup(c_n^-)_{n\ge1}$ for which the grouped sum converges
   (Lemma 3.4's argument goes through unchanged for any bounded sequence),
   the identical construction produces
   \[
    B_\infty(U_c,R(a))=2c_0/a+\sum_{n\ge1}\Big[2c_n\cdot\tfrac1{a+2n}
    +2c_n^-\cdot\tfrac1{a-2n}\Big],
   \]
   which is an arbitrary meromorphic function with simple poles on $2\Z$
   and prescribed residues $2c_n,2c_n^-$ — i.e. *any* function with a
   partial-fraction expansion over $2\Z$ subject to a mild decay condition,
   not only $\cot$. Setting $U=$ all-ones is exactly the choice that makes
   the residues *constant*, which is exactly what reproduces $\cot$'s
   Mittag-Leffler expansion, because $\cot$'s residues are constant. The
   vector $U$ was reverse-engineered from the target.
3. Given that choice of $U$, Theorem 3.6's content **is** the classical
   Mittag-Leffler expansion of $\cot$ (an external, classical fact about
   the function $\cot$, not derived from $\Theta$ anywhere in this note) —
   applied to the statement that $2\Z$, with constant residue, is the pole
   set of $\Gamma_\R(s)\Gamma_\R(-s)$. That statement is exactly 108_40
   Proposition 6.1 (extended to $\Gamma_\R(-s)$ by 108_41 Lemma 1.2): the
   fact used to *define* $\mathrm{spec}\,\Theta$ (and $\Theta^-$) at
   the very start of this construction.

**So Theorem 3.6 $\iff$ Mittag-Leffler for $\cot$ $\iff$ 108_40 Proposition
6.1 (the input).** Nothing came out of the pairing $B_\infty(U,R(a))$ that
was not put into the choice of $U$ and the definition of $\Theta$'s
spectrum. The identity is true, and the bookkeeping that makes it a bona
fide bilinear-form evaluation (Lemma 3.4's convergence argument, the
disclosure that $U\notin W_\infty$) is candid work — but it is bookkeeping,
not evidence that $W_\infty$ carries independent geometric content. **G4 is
not established as a geometric result.** It is a correctly-derived but
contentless repackaging of the construction's own input, in the same sense
that 108_40 §7 already cautioned against reading a spectral repackaging as
geometry.

**What is not affected by this retraction.** The polar-block matching of
108_41 §4 and the local-term identity here are proved on **disjoint**
sectors of $W_\infty$ ($B\oplus B^*$ vs. $A\oplus A^-$), exactly as flagged
in 108_41 §3 ("why two disjoint sectors, not one"): a single copy of
$\Theta$ cannot support both, since $b_0$ needs to be isotropic and $a_0$
needs a fixed nonzero self-pairing. Combined with the circularity just
identified in both constructions, the candid reading is that $W_\infty$ is
**two unrelated stipulated constructions living in a direct sum**, each
independently built to hit one target (a matrix from 107_241, a function
from 108_07), not a single geometric object from which both facts emerge.
§4 below is the one place in this pair of notes where a fact is derived
that was *not* built in for the purpose of matching a known target.

## 4. An unconditional no-go: $W_\infty$ cannot embed in Stage 0 under RH

This is the one result in 108_41–108_42 that was **not** built by
stipulating a target and matching it. It follows from Theorem 2.1 (proved
independently of any comparison with Stage 0) combined with 107_241
Corollary 3.3 (proved independently, before this note existed), and it uses
only the *manifestly* uncontested part of $B_\infty$ — the diagonal,
positive sector $A\oplus A^-$ of Definition 3.2 — so that it does not rest
on §3's disputed choice of $U$ or on 108_41 §4's stipulated matching.

> ### Definition 4.1 (isometric injection)
> Let $(W,B_W)$ and $(V,B_V)$ be complex vector spaces with symmetric (or
> Hermitian) bilinear forms. An **isometric injection**
> $\psi:(W,B_W)\to(V,B_V)$ is an injective linear map $\psi:W\to V$ with
> $B_V(\psi x,\psi y)=B_W(x,y)$ for all $x,y\in W$.
>
> For a form $B$ on a space $U$, write
> \[
>  n_+(B):=\sup\{\dim P:\ P\subseteq U\text{ a subspace on which }B\text{ is
>  positive definite}\},
> \]
> a cardinal (possibly $\aleph_0$ or, in principle, a larger cardinal,
> though not here). This is the same convention used, blockwise, by 107_241
> Theorem 3.1 and by Theorem 2.1 above: $n_+$ is realized by summing the
> dimensions of positive-definite blocks in an orthogonal decomposition.

> ### Lemma 4.2 (isometric injections do not decrease $n_+$)
> If $\psi:(W,B_W)\to(V,B_V)$ is an isometric injection, then
> $n_+(B_V)\ge n_+(B_W)$.

**Proof.** Let $P\subseteq W$ be any subspace on which $B_W$ is positive
definite, of dimension $d$. Since $\psi$ is injective and linear,
$\psi(P)\subseteq V$ is a subspace of the same dimension $d$ (an injective
linear map is a linear isomorphism onto its image). For $x\in P$,
$x\ne0\Rightarrow\psi(x)\ne0$ (injectivity) and $B_V(\psi x,\psi x)=B_W(x,x)
>0$ (isometry, positive-definiteness of $B_W|_P$), so $B_V$ is positive
definite on $\psi(P)$. Hence $\psi(P)$ witnesses $n_+(B_V)\ge d$ for every
$d$ realized by some positive-definite $P\subseteq W$; taking the
supremum over such $P$, $n_+(B_V)\ge n_+(B_W)$. $\square$

> ### Theorem 4.3 (embedding forces infinitely many off-line zeros)
> If there exists an isometric injection $\psi:(W_\infty,B_\infty)\to
> (V,\overline I_\partial)$, then $\xi$ has infinitely many distinct
> off-line zeros ($\#P=\infty$ in the notation of 107_241 §3).

**Proof.** $A\subseteq W_\infty$ (108_41 Def. 3.1–3.2, the $A$-summand
alone) is positive definite: $B_\infty(a_n,a_n)=2>0$ for each $n\ge0$, and
$A=\bigoplus_{n\ge0}\langle a_n\rangle$ is a $B_\infty$-orthogonal sum of
such lines (Def. 3.2: all cross terms $B_\infty(a_n,a_m)$, $n\ne m$, and all
terms $B_\infty(a_n,\cdot)$ against any other summand, vanish), so $B_\infty
|_A$ is positive definite of dimension $\aleph_0$ (this alone gives
$n_+(B_\infty)\ge\aleph_0$; it does not require Theorem 2.1's full
computation, nor §3's $A^-$ or 108_41 §4's $B\oplus B^*$ sector). By Lemma
4.2, $n_+(\overline I_\partial)\ge n_+(B_\infty)\ge\aleph_0$. By 107_241
Theorem 3.1, $n_+(\overline I_\partial)=1+\#P$. If $\#P$ were finite,
$1+\#P$ would be finite, contradicting $1+\#P\ge\aleph_0$. Hence $\#P=
\infty$. $\square$

> ### Corollary 4.4 (RH $\Rightarrow$ no such embedding)
> If RH holds, there is no isometric injection $(W_\infty,B_\infty)\to
> (V,\overline I_\partial)$.

**Proof.** By 107_241 Corollary 3.3, RH is equivalent to $n_+(\overline
I_\partial)=1$, equivalently (Corollary 3.2 there) to $\#P=0$. If an
isometric injection existed, Theorem 4.3 would force $\#P=\infty$,
contradicting $\#P=0$. $\square$

**What this is, and what it explicitly is not.** This is a genuine,
non-circular theorem: it was not obtained by choosing $B_\infty$ or $U$ to
match a pre-known target of Stage 0. It uses only the diagonal
positive-definiteness of $A$ (an immediate consequence of Definition 3.2's
weight $2>0$ on the diagonal — not a stipulation reverse-engineered from
107_241) and the already-proved, independent facts Theorem 2.1 (or even
just its one-line special case used here) and 107_241 Theorem 3.1/Corollary
3.3.

**This is not a proof of RH, and not a proof of its negation.** It is a
one-directional structural incompatibility: *if* RH holds, *then* the
specific archimedean object built in 108_41–108_42 cannot sit inside Stage
0's corner form as a sub-object via any linear, form-preserving embedding.
Equivalently and unconditionally (no RH hypothesis needed for this
direction): *any* such embedding, if one is ever exhibited, would itself
constitute a proof that $\xi$ has infinitely many off-line zeros. Nothing
here decides which of these obtains.

**Meaning for the programme.** The archimedean form $B_\infty$ is, in a
precise and now-proved sense, *too positive* to be a sub-object of the
corner form: its positive part alone is already infinite-dimensional and
unconditional, while Stage 0's positive part is capped at $1$ exactly when
the arithmetic is at its most rigid (RH). If Stage 6, or any later stage,
wants the archimedean fibre to participate in Stage 0's intersection
geometry, it cannot do so by exhibiting $W_\infty$ as a sub-space with the
inherited form: Theorem 4.3 rules that out (conditionally on RH; and
unconditionally rules out a *literal, on-the-nose* embedding of this
specific $B_\infty$, full stop, since $\#P<\infty$ is not otherwise known
to be false — this note does not claim $\#P=\infty$ outright, only that
embeddability forces it). The remaining routes — a **quotient** map
$(V,\overline I_\partial)\to(W_\infty,B_\infty)$-shaped data, an
**orthogonal complement** construction, or a relation carrying the
**opposite sign** on the positive part — are not excluded by this theorem
and are, on this evidence, the ones a later stage should try. That is a
real, load-bearing constraint on the design of any such stage, and it is
the most substantive output of Stage 4's geometry.

## 5. Scope

**Proved here.** Proposition 1.1 (bounded, boundedly invertible Gram
operator; nondegeneracy on the full Hilbert space); Theorem 2.1 (exact
inertia $(\aleph_0,\aleph_0)$, blockwise); Lemma 3.2, 3.4 (well-posedness of
the resolvent vector and the grouped pairing); Theorem 3.6 (the identity
$B_\infty(U,R(a))=\pi\cot(\pi a/2)$ — true, but see §3.4 for why it is not
evidence of geometric content); **Lemma 4.2 and Theorem 4.3/Corollary 4.4
(the embedding no-go — the one non-circular structural theorem in this pair
of notes).**

**Read from source, not re-derived.** The classical Mittag-Leffler
(partial-fraction) expansion of $\cot$ (Ahlfors; DLMF 4.19.6) — identified
in §3.4 as, together with 108_40 Prop. 6.1, the entire content of Theorem
3.6; 107_241 Theorem 3.1 and Corollary 3.3 (cited for the contrast in §2
and used as a hypothesis of Theorem 4.3/Corollary 4.4, not re-derived); the
value $\pi\cot(\pi a/2)$ as 108_07's archimedean local term (given verbatim
in this task's brief; 108_07 itself was not read, per the file-access rule
for this task).

**Explicitly searched for and not found.** A choice of the pairing vector
$U$ (Definition 3.3) that is forced by some property of $\Theta$ independent
of already knowing the target $\pi\cot(\pi a/2)$. As shown in §3.4, any
bounded sequence of coefficients in place of "all ones" gives an equally
valid pairing reproducing a *different* meromorphic function with poles on
$2\Z$; nothing found here singles out $\cot$'s residue pattern except
already knowing it.

**Verified numerically.** Theorem 2.1's block eigenvalues ($\pm1$ and $2$)
on finite truncations, by exact linear algebra (`fractions`/`sympy`, integer
matrices), confirming the pattern is stable, not a finite-size artifact.
Theorem 3.6, at a real and a complex $a$, by computing the truncated sum at
increasing cutoffs $N$ and confirming the error against $\pi\cot(\pi a/2)$
(computed independently via `mpmath`) shrinks under refinement, consistent
with the $O(1/N)$ tail bound implied by Lemma 3.4's $O(1/n^2)$ term
estimate. Theorem 4.3/Corollary 4.4's mechanism, on finite truncations: the
definite sector's positive-definite dimension grows without bound while a
Stage-0 model with $\#P=0$ (the RH case) admits a positive-definite
subspace of dimension exactly $1$ regardless of how large the model is
made, confirmed by exact eigenvalue computation (`sympy`), so no isometric
injection can exist once the source truncation reaches dimension $2$.

**Not established, and explicitly not claimed.**

* That $n_+=n_-=\aleph_0$ "proves" $\Phi$ has no arithmetic content — that
  claim rests on the closed form supplied for this task (verified there,
  not here) and on 108_39/108_40's identity/operator theorems; Theorem 2.1
  is offered only as a compatible, independently-computed geometric fact,
  not as a new proof of that separate claim.
* That Theorem 3.6 is evidence of geometric content in $W_\infty$. §3.4
  shows it reduces to Mittag-Leffler applied to this construction's own
  input (108_40 Prop. 6.1), via a pairing vector $U$ chosen with the target
  already known. **G4 is not established as a geometric result.**
* That $B_\infty(b_n,b_n)=0$ (108_41 §4's isotropy) follows from anything
  proved in this note either; §4 here deliberately avoids depending on it.
* That Theorem 4.3/Corollary 4.4 says anything about whether RH is true.
  It is a one-directional structural statement (§4's proof), not a step
  toward deciding RH in either direction.
* Anything else about $\RH$ beyond Corollary 4.4's stated conditional. No
  zero of $\zeta$ or $\xi$ enters any *definition* in this note (Corollary
  4.4's *proof*, unlike every definition, does invoke 107_241's zero-based
  form $\overline I_\partial$ and its RH-equivalence, both read from
  source, not re-derived — this is unavoidable for a theorem *about* the
  relation between the two forms).

`ROW_A_STATUS` unchanged. See 108_43 for the consolidated verdict.

## 6. Verifier

`108_42_stage_4_signature_and_the_local_term.py`:

1. Builds finite truncations of the definite sector ($2\cdot\mathrm{Id}$,
   size $N$) and of $M$ hyperbolic blocks $H_0,\dots,H_{M-1}$ as exact
   integer matrices, computes eigenvalues via `sympy` (exact) and confirms
   they are exactly $\{2\}$ (definite sector) and exactly $\{+1,-1\}$ with
   equal multiplicity (hyperbolic sector) for several truncation sizes —
   the blockwise content of Theorem 2.1.
2. Confirms Proposition 1.1's operator norms directly: the definite-sector
   Gram matrix and its inverse both have bounded (in fact constant) norm
   across truncations; the hyperbolic-sector Gram matrix is its own
   inverse (an involution), checked by exact matrix multiplication.
3. Confirms Lemma 3.2/3.4's decay rates numerically: the coefficients of
   $R(a)$ decay like $1/n$ while the grouped pairing terms $\lambda_n(a)$
   decay like $1/n^2$, by regression on $\log|\text{coeff}|$ vs $\log n$.
4. Confirms Theorem 3.6 at a real $a=1.3$ and a complex $a=0.7+0.3i$: the
   truncated sum at cutoffs $N=10,20,40,\dots,640$ is compared against
   $\pi\cot(\pi a/2)$ (via `mpmath`), and the error is checked to shrink
   under each doubling of $N$ (a genuine convergence test).

All checks print PASS/FAIL individually; the script exits 0 with
`VERDICT: ALL CHECKS PASS` only if every check passes.
