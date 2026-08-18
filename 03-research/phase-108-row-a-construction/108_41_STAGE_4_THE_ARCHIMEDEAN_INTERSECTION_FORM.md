# 108.41 — Stage 4 geometry, I: the archimedean space and its form

## 0. Result

108_39 gave Stage 4 an *identity* form; 108_40 gave it an *operator* form and
stated explicitly (§7) what was still missing: a space with an intersection
pairing, not merely a spectrum with a determinant. This note supplies that
space.

> \[
>  \boxed{\;W_\infty := A\oplus A^-\oplus B\oplus B^*,\quad
>  B_\infty:\ W_\infty\times W_\infty\to\mathbb C\ \text{explicit, symmetric,
>  built only from }\Theta.\;}
> \]
>
> $W_\infty$ is built from **three elementary transforms of one operator**:
> $\Theta$ itself, $\Theta^-:=-\Theta$, and $\Theta^*:=1-\Theta$ — equivalently,
> from the pole sets of $\Gamma_\R(s)$, $\Gamma_\R(-s)$, $\Gamma_\R(1-s)$ and
> nothing else. No zero of $\xi$, no Li coefficient, and no positive part of a
> Weil-type form enters any definition below.
>
> The $B\oplus B^*$ block of $B_\infty$ contains an explicit rank-2 subspace
> whose Gram matrix **is set, by Definition 3.2, to equal**
> $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ — the same
> matrix as the Stage-0 polar block $H_{\mathrm{ruling}}$ of 107_241 Theorem
> 3.1(1), in the corresponding basis (evaluation at $s=0$ and $s=1$).
>
> **This is a matching by construction, not a theorem.** §3's residue
> calculation shows only that the two relevant residues are *constant in
> $n$* (Corollary 2.2); it supplies no derivation of the isotropy
> $B_\infty(b_n,b_n)=0$, which is the entire content of "hyperbolic," and
> none was found. §4 states this precisely: what is proved is that a form
> matching Stage 0's polar block *exists* on $W_\infty$ by explicit
> stipulation; 108_39 Corollary 2.2's identification is not thereby upgraded
> to a proof. (G2: see §4 for the exact, deliberately unglamorous, status.)

## 1. Three mirrors of $\Theta$

Recall (108_40 Definition 1.1) $\Theta$ on $\mathcal H=\ell^2(\Z_{\ge0})$,
orthonormal basis $\{e_n\}_{n\ge0}$, $\Theta e_n=-2n\,e_n$, each eigenvalue
simple; and (108_40 Proposition 6.1) $\operatorname{spec}\Theta=\{-2n:n\ge0\}$
is exactly the pole set of $\Gamma_\R(s)=\pi^{-s/2}\Gamma(s/2)$.

> ### Definition 1.1 (the two mirrors)
> On the same underlying vector space, define
> \[
>  \Theta^-:=-\Theta,\qquad \Theta^*:=1-\Theta,
> \]
> i.e. $\Theta^-e_n=2n\,e_n$ and $\Theta^*e_n=(1+2n)\,e_n$. Both are algebraic
> functions of $\Theta$ alone; no new operator, spectrum, or external datum is
> introduced.

> ### Lemma 1.2 (pole correspondence for the mirrors)
> $\operatorname{spec}\Theta^-=\{2n:n\ge0\}$ is exactly the pole set of
> $s\mapsto\Gamma_\R(-s)$, and $\operatorname{spec}\Theta^*=\{1+2n:n\ge0\}$ is
> exactly the pole set of $s\mapsto\Gamma_\R(1-s)$; all poles in both sets are
> simple.

**Proof.** By 108_40 Proposition 6.1, $\Gamma_\R(w)$ has simple poles exactly
at $w=-2m$, $m\ge0$. Substituting $w=-s$: $-s=-2m\iff s=2m$. Substituting
$w=1-s$: $1-s=-2m\iff s=1+2m$. $\square$

So $\Theta$, $\Theta^-$, $\Theta^*$ are read off, respectively, the pole sets
of $\Gamma_\R(s)$, $\Gamma_\R(-s)$, $\Gamma_\R(1-s)$ — three evaluations of one
function. The verifier confirms Lemma 1.2 by the same pole-growth test 108_40
used for $\Theta$ itself (check "1").

## 2. The residue Lemma

> ### Lemma 2.1 (log-derivative residue)
> If $f$ is meromorphic near $s_0$ with a simple pole there, then $f'/f$ has
> residue $-1$ at $s_0$.

**Proof.** Write $f(s)=\dfrac{c}{s-s_0}(1+g(s))$ near $s_0$, $c\ne0$, $g$
holomorphic with $g(s_0)=0$. Then $f'/f(s)=-\dfrac1{s-s_0}+\dfrac{g'(s)}
{1+g(s)}$, and the second term is holomorphic at $s_0$. $\square$

> ### Corollary 2.2 (the two residues used below)
> Write $G:=\log\Gamma_\R$ as in 108_39. Then
> \[
>  \operatorname*{Res}_{s=-2n}G'(s)=-1,\qquad
>  \operatorname*{Res}_{s=1+2n}G'(1-s)=+1,\qquad n\ge0.
> \]

**Proof.** $G'=\Gamma_\R'/\Gamma_\R$, and $\Gamma_\R$ has a simple pole at
$s=-2n$ (108_40 Prop. 6.1), so the first identity is Lemma 2.1 applied to
$f=\Gamma_\R$. For the second, let $h(s):=\Gamma_\R(1-s)$; by Lemma 1.2, $h$
has a simple pole at $s=1+2n$, and $h'(s)=-\Gamma_\R'(1-s)$, so
$h'/h(s)=-G'(1-s)$. By Lemma 2.1, $h'/h$ has residue $-1$ at $s=1+2n$, hence
$G'(1-s)$ has residue $+1$ there. $\square$

Both residues are checked numerically (central-difference in $s$, with a
step-halving convergence test) at four values of $n$; see verifier check
"2"/"3". This reproduces, from first principles, the constant residues that
already drove 108_39 Theorem 1.1 (the finite part of the Stage-2 assembly is
$G'(s)+G'(1-s)$).

## 3. The space and the form

> ### Definition 3.1 ($W_\infty$)
> Let $A,A^-,B,B^*$ be four copies of $\ell^2$-type spaces:
> \[
>  A=\ell^2(\Z_{\ge0}),\ \text{basis }\{a_n\}_{n\ge0},\quad
>  A^-=\ell^2(\Z_{\ge1}),\ \text{basis }\{a_n^-\}_{n\ge1},
> \]
> \[
>  B=\ell^2(\Z_{\ge0}),\ \text{basis }\{b_n\}_{n\ge0},\quad
>  B^*=\ell^2(\Z_{\ge0}),\ \text{basis }\{b_n^*\}_{n\ge0},
> \]
> each carrying (a copy of) $\Theta$, $\Theta^-$, $\Theta$, $\Theta^*$
> respectively: $\Theta a_n=-2n\,a_n$, $\Theta^- a_n^-=2n\,a_n^-$,
> $\Theta b_n=-2n\,b_n$, $\Theta^* b_n^*=(1+2n)b_n^*$. Set
> \[
>  W_\infty:=A\oplus A^-\oplus B\oplus B^*.
> \]

> ### Definition 3.2 (the bilinear form $B_\infty$)
> On the algebraic span of the basis vectors, define the symmetric
> $\C$-bilinear form $B_\infty$ by
> \[
>  B_\infty(a_n,a_m)=2\delta_{nm},\quad
>  B_\infty(a_n^-,a_m^-)=2\delta_{nm},\quad
>  B_\infty(a_\bullet,a_\bullet^-)=0,
> \]
> \[
>  B_\infty(b_n,b_m^*)=B_\infty(b_m^*,b_n)=\delta_{nm},\qquad
>  B_\infty(b_n,b_m)=B_\infty(b_n^*,b_m^*)=0,
> \]
> and $B_\infty$ vanishes on every pair drawn from different summands of
> $\{A\oplus A^-\}$ vs. $\{B\oplus B^*\}$.

This is fully explicit: every entry of the (infinite) Gram matrix, in the
basis $\{a_n\}\cup\{a_n^-\}\cup\{b_n\}\cup\{b_n^*\}$, is written down above.
Nothing is asserted to exist abstractly; the matrix is given.

**Why two disjoint sectors, not one.** A single copy of $\Theta$ cannot serve
both purposes at once. Section 4 needs $b_0$ to be *isotropic*
($B_\infty(b_0,b_0)=0$), so that the block $\{b_0,b_0^*\}$ is hyperbolic.
Section 5 (108_42, G4) needs $a_0$ to be *non-isotropic* with a specific
positive weight, because it is $a_0$'s self-pairing that supplies the $n=0$
term $1/a$ of the cotangent expansion. These two requirements are
incompatible on one copy of the $n=0$ eigenvector: no single scalar
$B(e_0,e_0)$ is simultaneously $0$ and $2$. This is a genuine obstruction,
not a presentational choice, and it is what forces the direct sum
$A\oplus A^-\oplus B\oplus B^*$ rather than a single undecomposed copy of
$\mathcal H$.

**Motivating $B_\infty$ on $B\oplus B^*$ from residues.** Definition 3.2's
off-diagonal weight $1$ on $B\times B^*$ is not an arbitrary normalization;
with $r_n:=\operatorname*{Res}_{s=-2n}G'(s)=-1$ and
$r_n^*:=\operatorname*{Res}_{s=1+2n}G'(1-s)=+1$ (Corollary 2.2), both
constants **independent of $n$** because every eigenvalue of $\Theta$ is
simple (108_40 Def. 1.1), the natural residue-coupling
\[
 B_\infty(b_n,b_m^*):=-\,r_n\,r_n^*\,\delta_{nm}=-(-1)(1)\delta_{nm}=\delta_{nm}
\]
reproduces Definition 3.2's *off-diagonal* entries exactly. The sign $-1$ in
front is a normalization that fixes $B_\infty(b_0,b_0^*)=+1$ rather than
$-1$; flipping it gives the congruent form $\left(\begin{smallmatrix}0&-1\\
-1&0\end{smallmatrix}\right)$, isomorphic as an abstract form but not
literally equal to the target matrix without also flipping
$b_0^*\mapsto-b_0^*$.

**What this does and does not derive — stated plainly, not left to Scope.**
The residue calculation derives exactly one fact: that whatever off-diagonal
weight is used to couple $b_n$ to $b_n^*$, it can be taken *independent of
$n$* (both $r_n$ and $r_n^*$ are constant), so a single global
normalization works for every block simultaneously. That is a real,
non-trivial input to the construction. It derives **nothing** about the
*diagonal* entries $B_\infty(b_n,b_n)$ and $B_\infty(b_n^*,b_n^*)$: these are
set to $0$ in Definition 3.2 by stipulation. A single simple pole of a
scalar function supplies, via its residue, a linear functional (an
evaluation), not a quadratic self-pairing; nothing in $\Gamma_\R$, $\Theta$,
or the residue calculus of this section forces, suggests, or is even
naturally compared against, a value for $B_\infty(b_n,b_n)$. Isotropy — the
condition that makes the block "hyperbolic" rather than some other rank-2
form — is put in by hand. §4 draws the consequence of this candidly.

## 4. The polar block matches Stage 0 — by construction, not by theorem

Recall (Stage 0, 107_241 §1–§2) the evaluation coordinates
$f\mapsto(\widehat f(0),\widehat f(1),\dots)$ of Lemma 2.2, and Theorem
3.1(1): the polar block $H_{\mathrm{ruling}}=\operatorname{span}\{v_0,v_1\}$
(with $v_0,v_1$ the two polar coordinates, i.e. evaluation of $\widehat f$ at
$s=0$ and $s=1$) carries the Gram matrix $\left(\begin{smallmatrix}0&1\\1&0
\end{smallmatrix}\right)$, from the cross terms $\widehat f(0)\overline{
\widehat g(1)}+\widehat f(1)\overline{\widehat g(0)}$ of (2.1).

> ### Proposition 4.1 (G2: a matching by construction — the circularity
> ### stated in full, not deferred)
> The Gram matrix of $B_\infty$ on $\operatorname{span}\{b_0,b_0^*\}$, in the
> basis $(b_0,b_0^*)$, equals $\left(\begin{smallmatrix}0&1\\1&0
> \end{smallmatrix}\right)$: the same matrix as $I_\partial|_{H_{\mathrm
> {ruling}}}$ in the basis $(v_0,v_1)$.

**"Proof."** By Definition 3.2, $B_\infty(b_0,b_0)=0$, $B_\infty(b_0^*,b_0^*)
=0$, $B_\infty(b_0,b_0^*)=1$ — because Definition 3.2 *sets* these values.
There is no independent computation here: the isotropy $B_\infty(b_0,b_0)=0$
and the off-diagonal value $B_\infty(b_0,b_0^*)=1$ are exactly the numbers
written into Definition 3.2, and Definition 3.2 was written with this target
matrix in view. Comparing the result to 107_241 Theorem 3.1(1) and finding
agreement is therefore not a discovery about $W_\infty$; it is a check that
the stipulation was transcribed correctly. $\square$ (in the only sense
available: the arithmetic is right.)

**This is not a theorem, and 108_41 §0's original framing overclaimed it as
one.** The candid content of G2, after this correction, is:

* A rank-2 bilinear-form space matching Stage 0's $H_{\mathrm{ruling}}$
  *can be exhibited* inside a space built from $\Theta$ and its algebraic
  reflections — i.e. the target matrix is not *forbidden* by the
  archimedean data, and can be realized using only quantities ($\Theta$'s
  simple spectrum, the pole set of $\Gamma_\R(1-s)$) that are themselves
  legitimately archimedean.
* But *which* rank-2 form to put on $\operatorname{span}\{b_0,b_0^*\}$ was a
  free choice at Definition 3.2, constrained only by "match the target,"
  not derived from any property of $\Theta$, $\Gamma_\R$, or their residues
  that would have produced *this* matrix (rather than, say, $2\delta_{nm}$,
  or any other symmetric form) if the target had not been known in advance.
  §3 identified exactly what *is* derived (the off-diagonal coupling is
  $n$-independent) and what is not (isotropy, i.e. the vanishing of the
  diagonal). The vanishing is the entire content of "hyperbolic plane," and
  it is stipulated.

108_39 Corollary 2.2's identification of the polar page with the Stage-0
hyperbolic block is therefore **still a prose identification**, now dressed
in an explicit matrix that can be checked to agree — not a proof that it
must agree. We were unable to find, and did not find, an independent
derivation of isotropy that would upgrade this to a genuine theorem; see
§5 for the search that was made and came up empty.

> ### Remark 4.2 (the coordinate labels agree; this does not rescue the
> ### circularity)
> $s=0$ is a pole of $\Gamma_\R$ (108_40 Prop. 6.1); $\xi(s)=\tfrac{s(s-1)}2
> \Gamma_\R(s)\zeta(s)$ is entire, so the elementary factor $s$ in
> $\tfrac{s(s-1)}2$ exists *precisely* to cancel this pole of $\Gamma_\R$ at
> $s=0$ — the structural reason 107_241's evaluation coordinate $v_0$ and our
> $b_0$ sit at the same labeled point $s=0$. Likewise $s=1$ is the
> reflection of $s=0$ under $s\mapsto1-s$ in both constructions. This is a
> genuine, non-circular observation about *where* the two coordinates sit.
> It says nothing about the *values* of the form at those coordinates,
> which is the content actually being matched in Proposition 4.1 and which
> remains a stipulation. $v_1$'s pole at $s=1$ has an arithmetic cause (the
> pole of $\zeta$); $b_0^*$'s eigenvalue $1$ has an algebraic cause
> ($\Theta^*=1-\Theta$). Matching coordinate labels while stipulating the
> form values is not the same as proving the forms coincide for a reason.

## 5. Scope

**Proved here.** Lemma 1.2 (pole sets of the two mirrors of $\Gamma_\R$);
Lemma 2.1 and Corollary 2.2 (the two constant residues, and *only* that they
are constant — no isotropy claim follows from them); Definition 3.1–3.2
($W_\infty$, $B_\infty$, fully explicit); Proposition 4.1 (the polar block
*equals*, by explicit stipulation checked against 107_241, the matrix
$\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ — a construction
fact, not a derivation); Remark 4.2 (the two coordinate labels $0,1$ agree
for a structural reason; the form *values* at them do not thereby agree for
a structural reason).

**Explicitly searched for and not found.** A non-circular derivation of the
isotropy condition $B_\infty(b_n,b_n)=0$ — i.e. a property of $\Gamma_\R$,
$\Theta$, or their residues, fixed *before* Stage 0's matrix is consulted,
that forces the diagonal to vanish. A single simple pole supplies, via its
residue, only a linear functional; nothing found in this construction
supplies a quadratic self-pairing at all, let alone one that vanishes. If
such a derivation exists it was not located here, and this note does not
claim to have ruled out its existence — only that Definition 3.2 does not
supply one.

**Read from source, not re-derived.** 108_40 Definition 1.1 and Proposition
6.1 ($\Theta$, its spectrum, and its identification with the pole set of
$\Gamma_\R$); 107_241 Lemma 2.2, Theorem 3.1(1) and (2.1) (Stage-0 evaluation
coordinates, $H_{\mathrm{ruling}}$ and its Gram matrix); the fact that
$\xi(s)=\tfrac{s(s-1)}2\Gamma_\R(s)\zeta(s)$ is entire (used only in Remark
4.2, classical).

**Verified numerically.** Lemma 1.2's pole locations, by the same
distance-doubling growth test 108_40 used for $\Theta$ (verifier check "1").
Corollary 2.2's two residues, at $n=0,1,2,3$, by a central-difference
quotient with a step-halving convergence check, not a bare threshold
(checks "2","3"). The algebraic identity $-r_nr_n^*=1$ for all four tested
$n$ (check "4"). The literal equality of the two $2\times2$ Gram matrices in
Proposition 4.1, via exact integer arithmetic (check "5") — confirming the
stipulation was transcribed correctly, not an independent derivation.

**Not established, and explicitly not claimed.**

* That $B_\infty(b_n,b_n)=0$ (isotropy) follows from any property of
  $\Theta$, $\Gamma_\R$, or the residue calculus of §2–§3. It is stipulated
  in Definition 3.2. **G2 is therefore not proved as a theorem: it is a
  matching by construction**, and Proposition 4.1 is stated, and named, to
  say exactly that.
* That $\varphi$ extends to an isomorphism of the *entire* forms
  $(V,\overline I_\partial)$ and $(W_\infty,B_\infty)$. It does not: 108_42
  computes the full inertia of $B_\infty$ and shows it is unconditionally
  $(\aleph_0,\aleph_0)$, independent of any arithmetic input, whereas
  107_241 Corollary 3.3 shows Stage 0's inertia is $(1,\cdot)$ **iff** RH
  holds. Indeed 108_42 proves something stronger and unconditional: no
  isometric injection $(W_\infty,B_\infty)\hookrightarrow(V,\overline
  I_\partial)$ can exist unless $\xi$ has infinitely many off-line zeros
  (108_42, new §4).
* That $W_\infty$ is the cohomology, or fibre, of any algebraic variety,
  scheme, or motive, or that $B_\infty$ is an intersection pairing arising
  from actual algebraic cycles. $W_\infty$ is a Hilbert space with an
  explicit bounded symmetric form, built from a spectrum and its algebraic
  reflections — the same epistemic status as 108_40's $\Theta$.
* Anything about $\RH$. No zero of $\xi$ enters any definition in this note.

## 6. Verifier

`108_41_stage_4_the_archimedean_intersection_form.py` implements, using
`mpmath` at 30 digits:

1. Lemma 1.2: growth of $|\Gamma_\R(-s)|$ near $s=0,2,4,6$ and
   $|\Gamma_\R(1-s)|$ near $s=1,3,5,7$, confirming pole-like (doubling)
   behavior as the offset halves — the same test 108_40 used for $\Theta$
   itself.
2. Corollary 2.2, first identity: $\operatorname*{Res}_{s=-2n}G'(s)=-1$ at
   $n=0,1,2,3$, via central difference with step $h$ and $h/2$, confirming
   the residual shrinks.
3. Corollary 2.2, second identity: $\operatorname*{Res}_{s=1+2n}G'(1-s)=+1$
   at $n=0,1,2,3$, same convergence test.
4. The algebraic identity $-r_nr_n^*=1$ at the four tested $n$, from the
   numerically computed residues.
5. Proposition 4.1: the Gram matrix of $B_\infty$ on $\{b_0,b_0^*\}$, built
   directly from Definition 3.2, equals $\left(\begin{smallmatrix}0&1\\1&0
   \end{smallmatrix}\right)$ exactly (exact integer comparison), and this is
   compared, entry by entry, against the Stage-0 matrix as recorded from
   107_241 Theorem 3.1(1) (a hard-coded citation of that theorem's stated
   matrix, not a re-derivation of Stage 0). This check confirms the
   stipulation of Definition 3.2 was transcribed correctly; per §4, it is
   not evidence of anything beyond that.

All checks print PASS/FAIL individually; the script exits 0 with
`VERDICT: ALL CHECKS PASS` only if every check passes.
