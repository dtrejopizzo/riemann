# 113.05 — Canonical conventions, the closed forms of $\star$ and $\widetilde{(\cdot)}$, and which pairing is the real one

## 0. Why this note exists

Everything downstream of the corner pairing — d1's compatibility
computation, d3's $h^0$, d4's duality — is a computation *in coordinates*.
Three conventions in the corpus disagree, and one of the disagreements is
not cosmetic: it is the difference between a form that can detect RH and one
that cannot.  A fourth item, 107\_239 §4's deferral of $\star$ and
$\widetilde{(\cdot)}$, has never been discharged, which is the stated reason
113\_04 §2 could not run its computation.

This note fixes all four.  Nothing here is deep; all of it is load-bearing.

## 1. The Mellin convention

Two conventions are in use.

> **(A)** $\widehat f_A(w):=\int_0^\infty f(r)\,r^{-w}\,d^\times r
> =\int_{\mathbb R}\tilde f(x)e^{-wx}dx$
> — 110\_02, 111\_00/01 (Lemma 111.1.2 pins it: $\widehat f(1)=\int\tilde
> f(x)e^{-x}dx$), and by inheritance 113\_01–113\_04.
>
> **(B)** $\widehat f(s):=\int_0^\infty f(u)\,u^{s}\,d^\times u
> =\int_{\mathbb R}\tilde f(x)e^{sx}dx$
> — 107\_241 §1, 112\_01/112\_03, phase-35 doc 100, phase-34 doc 91.

They are related by $\widehat f_A(w)=\widehat f(-w)$.

> ### Decision 1.1 (convention B is canonical)
> From here on $\widehat f(s)=\int_0^\infty f(u)u^{s}d^\times u$.

Three reasons, in order of weight.

1. **It is the convention of the object being computed.**  107\_241 (2.1) is
   the pairing in coordinates and 112 is the effective cone; both are in B.
   A translation error there propagates into every statement about d2–d5.
2. **The two polar coordinates are the two rulings only in B.**  In B,
   $\widehat f(0)=\int_0^\infty f(r)\frac{dr}r$ and
   $\widehat f(1)=\int_0^\infty f(r)\,dr$ — exactly the two degrees
   $D_f\cdot F_v$, $D_f\cdot F_h$ used in 112\_03 §1.  In A, $\widehat
   f_A(1)=\int_0^\infty f(r)\frac{dr}{r^2}$, which is not any intersection
   number in the programme.
3. **Only in B is the involution the functional equation.**  Lemma 2.3 below
   gives $\widehat{\widetilde g}(s)=\overline{\widehat g(1-\bar s)}$: the
   reflection $s\mapsto1-\bar s$, whose fixed line is $\Re s=\tfrac12$.  In A
   the same involution reads $w\mapsto-1-\bar w$, fixed line $\Re w=-\tfrac12$.
   Requirement d4 is going to be built out of this reflection, and it must be
   the one the functional equation supplies.

> ### Proposition 1.2 (what the translation changes, and what it does not)
> Under $w\mapsto -s$:
> * $\widehat f_A(0)=\widehat f(0)$ — the mass coordinate is **unchanged**;
> * $\widehat f_A(1)=\widehat f(-1)\ne\widehat f(1)$ — the second polar
>   coordinate is a **different functional**;
> * $\widehat f_A(\rho)=\widehat f(-\rho)$, and the zero set $Z$ is symmetric
>   under $\rho\mapsto1-\rho$ but **not** under $\rho\mapsto-\rho$.

**Consequence, stated exactly.**  111\_01 evaluates at the points
$\{0,1\}\cup Z$ — which are B's evaluation points — while defining
$\widehat f$ by A's integral.  That is an internal inconsistency in 111\_01.
It is, however, **harmless for every conclusion 111\_01 draws**, for a reason
worth recording rather than hoping:

> ### Lemma 1.3 (the $\eta>1$ threshold is convention-independent)
> For $\tilde f\in\mathcal S_\eta$ the integral $\int\tilde f(x)e^{-wx}dx$
> converges absolutely for $|\Re w|<\eta$, and likewise
> $\int\tilde f(x)e^{sx}dx$ for $|\Re s|<\eta$.  The two strips are the
> reflections of one another, both symmetric about the origin, both
> containing $[0,1]$ exactly when $\eta>1$.

**Proof.**  $\mathcal S_\eta$ is a *two-sided* bound, $|\tilde f(x)|\le
C_0e^{-\eta|x|}$; the estimate in 111\_01 Theorem 111.1.3's proof uses only
$|e^{-wx}|=e^{-\Re(w)x}\le e^{|\Re w||x|}$, which is invariant under
$\Re w\mapsto-\Re w$. $\square$

So 111\_01 Theorems 111.1.3, 111.1.4, 111.1.5, its sech counterexample
(sech is even, hence fixed by the reflection) and 113\_02's threshold all
stand verbatim in B.  What must **not** be carried over without re-deriving
is any statement that distinguishes the two polar coordinates from each
other — in particular $H=(1,1,0,\dots)$ (112) and anything about $K$ (d4).

## 2. The closed forms, imported and discharged

107\_239 §4 defines the pairing as $I_\partial(D_f,D_g)=\mathfrak T(f\star
\widetilde g)$ and defers $\star$ and $\widetilde{(\cdot)}$ "to Phase 107",
where they are never written.  They exist in the corpus, in phase 34 (doc 91,
Definitions 1.1, 1.2, 1.5) and phase 35 (doc 100), already in convention B.

> ### Definition 2.1 (multiplicative convolution and adjoint; imported)
> For $f,g$ on $\mathbb R^\times_+$,
> $$(f\star g)(x):=\int_0^\infty f(y)\,g(x/y)\,\frac{dy}y,
> \qquad
> \widetilde g(x):=\frac{\overline{g(1/x)}}{x}.$$

> ### Lemma 2.2 (convolution theorem)
> $\widehat{f\star g}(s)=\widehat f(s)\,\widehat g(s)$, whenever both
> transforms converge absolutely on $\Re s=\sigma$.

**Proof.**  $\int_0^\infty\!\!\int_0^\infty f(y)g(x/y)\frac{dy}y x^{s}
\frac{dx}x$; substitute $x=yz$, $\frac{dx}x=\frac{dz}z$, $x^s=y^sz^s$, and
Fubini (justified by absolute convergence). $\square$

> ### Lemma 2.3 (the adjoint is the functional-equation reflection)
> $$\boxed{\ \widehat{\widetilde g}(s)=\overline{\widehat g(1-\bar s)}\ }$$

**Proof.**  $\widehat{\widetilde g}(s)=\int_0^\infty
\overline{g(1/u)}\,u^{-1}u^{s}\,\frac{du}u$.  Put $u=1/v$,
$\frac{du}u=-\frac{dv}v$ with the orientation reversing, $u^{s-1}=v^{1-s}$:
$$=\int_0^\infty\overline{g(v)}\,v^{1-s}\,\frac{dv}v
=\overline{\int_0^\infty g(v)\,v^{1-\bar s}\,\frac{dv}v}
=\overline{\widehat g(1-\bar s)}.\qquad\square$$

> ### Corollary 2.4
> 107\_239 §4's deferral is discharged: Definition 2.1 is the involution and
> modular normalization it refers to, and Lemma 2.3 **is** 107\_241 (1.1),
> which 107\_241 states without proof.  In particular the modular factor
> $1/x$ in $\widetilde g$ is not a convention — it is forced, as the unique
> weight making the adjoint act on Mellin transforms by the functional
> equation's own reflection.

## 3. Which pairing is the real one

> ### Theorem 3.1 (the evaluated pairing is the mirrored one)
> For $f,g$ with $h:=f\star\widetilde g$ admissible,
> $$\widehat h(s)=\widehat f(s)\,\overline{\widehat g(1-\bar s)},$$
> and consequently, applying the explicit formula to $h$,
> $$I_\partial(D_f,D_g)=\widehat f(0)\overline{\widehat g(1)}
> +\widehat f(1)\overline{\widehat g(0)}
> -\sum_{\rho\in Z}m_\rho\,\widehat f(\rho)\,\overline{\widehat g(\rho')},
> \qquad \rho':=1-\bar\rho.$$

**Proof.**  Lemma 2.2 then Lemma 2.3.  Evaluate at $s=0$: $\widehat
h(0)=\widehat f(0)\overline{\widehat g(1)}$; at $s=1$: $\widehat
h(1)=\widehat f(1)\overline{\widehat g(0)}$; at $s=\rho$: $\widehat
h(\rho)=\widehat f(\rho)\overline{\widehat g(1-\bar\rho)}$. $\square$

This is 107\_241 (2.1) exactly.  It is **not** the form displayed in
107\_240's proof of Theorem D, nor the form quoted at the head of 111\_01,
both of which use the diagonal $\widehat f(s)\overline{\widehat g(\bar s)}$.

> ### Corollary 3.2 (the diagonal displays are transcription defects; the
> radical is unaffected)
> The set
> $$\mathrm{rad}\,I_\partial=\{f:\ \widehat f(0)=\widehat f(1)=0,\
> \widehat f(\rho)=0\ \forall\rho\in Z\}$$
> is the same for both forms.

**Proof.**  $g\mapsto(\widehat g(0),\widehat g(1),(\widehat g(\rho))_{\rho})$
has image meeting every finite coordinate block in full (107\_241 Lemma 2.2,
from linear independence of the characters $u\mapsto u^{s_j}$).  Composing
with the involution $\rho\mapsto\rho'$ permutes the blocks and swaps the two
polar slots, a bijection.  So "vanishes against every $g$" imposes the same
conditions on $\widehat f$ either way. $\square$

> ### Remark 3.3 (why the distinction is not cosmetic)
> On the primitive subspace $\widehat f(0)=\widehat f(1)=0$ the two forms are
> $$Q_{\rm diag}(f)=-\sum_\rho m_\rho|\widehat f(\rho)|^2\ \le\ 0
> \quad\text{always},
> \qquad
> Q(f)=-\sum_\rho m_\rho\,\widehat f(\rho)\overline{\widehat f(\rho')} .$$
> $Q_{\rm diag}\le0$ holds whatever the zeros do; it is negative semidefinite
> for any function with a zero set at all, and carries no arithmetic.  $Q$ is
> 107\_241 Corollary 3.4, and $Q\le0\iff$ RH: an off-line mirror pair
> $\{\rho,\rho'\}$ contributes $-2m_\rho\Re(\widehat f(\rho)
> \overline{\widehat f(\rho')})$, which takes **both signs**, giving
> 107\_241 Theorem 3.1's signature-$(1,1)$ plane $H_\rho$.
>
> So the diagonal form cannot carry row (d), and the mirrored one can.  Every
> statement in the corpus that quotes the diagonal form must be re-read as
> quoting the mirrored one; by Corollary 3.2, none of the *conclusions* about
> the radical changes, and by Remark 3.3, every conclusion about *signature*
> would have.  111\_01's convergence analysis is unaffected: it bounds each
> term in absolute value, and $|\widehat g(\rho')|$ obeys the same bounds as
> $|\widehat g(\rho)|$ (Lemma 111.1.4 is uniform on $0\le\sigma\le1$, and
> $\rho'$ lies in the same strip).

## 4. The identity-value functional, in closed form

The immediate payoff, and the reason 113\_04 §2 could not be run.

> ### Proposition 4.1
> $$\boxed{\ h(1)=(f\star\widetilde g)(1)=\int_0^\infty
> f(u)\,\overline{g(u)}\,du\ }$$

**Proof.**  $(f\star\widetilde g)(1)=\int_0^\infty f(y)\widetilde
g(1/y)\frac{dy}y$ and $\widetilde g(1/y)=\overline{g(y)}\cdot y$, so the
integrand is $f(y)\overline{g(y)}\,dy$. $\square$

So the identity-value condition $h(1)=0$ of 113\_01 Theorem 4.1 is an
**orthogonality condition** between $f$ and $g$ in $L^2(0,\infty;du)$ — not
an evaluation, and in particular not a linear condition on $g$ once $f$ is
tied to $g$.  113\_06 takes this up.

## 5. Scope

**Proved here.**  Lemma 1.3; Lemma 2.2; Lemma 2.3 (which 107\_241 (1.1)
asserts without proof); Theorem 3.1; Corollary 3.2; Remark 3.3's sign
computation; Proposition 4.1.

**Read from source, not re-derived.**  Definition 2.1, imported verbatim
from phase-34 doc 91 Definitions 1.1/1.2/1.5 and phase-35 doc 100.
107\_241 Lemma 2.2 (surjectivity onto finite coordinate blocks).
107\_241 Theorem 3.1 and Corollary 3.4.  111\_01 Lemma 111.1.4.

**Corrections issued against the corpus.**  (i) 111\_01 defines $\widehat f$
in convention A but evaluates at convention-B points; harmless by Lemma 1.3,
but the file should be restated.  (ii) 107\_240's proof of Theorem D and
111\_01's opening display show the diagonal pairing; the correct one is
Theorem 3.1's mirrored form.  Theorem D's *radical* is unaffected
(Corollary 3.2).  (iii) 107\_239 §4's deferral is discharged by
Definition 2.1.

**Not established, and explicitly not claimed.**  That every statement in
110/111/113 has been re-derived in convention B — only that the thresholds
and the radical are invariant (Lemma 1.3, Corollary 3.2), and that
statements distinguishing the polar coordinates are *not* covered by that
invariance.  Anything about RH.

`ROW_A_STATUS` unchanged.  No zero of $\xi$ enters any definition here.

## 6. Verifier

`113_05_canonical_conventions.py` checks numerically: Lemma 2.2 and Lemma
2.3 against direct quadrature for an explicit probe; Theorem 3.1's three
evaluations; that the diagonal and mirrored forms give **different** numbers
on an explicit pair (so Corollary 3.2's "same radical, different form" is
not vacuous); that the diagonal form is negative semidefinite on a synthetic
off-line zero configuration while the mirrored form takes a positive value
there (Remark 3.3); Proposition 4.1 against direct quadrature; and the
convention dictionary $\widehat f_A(w)=\widehat f(-w)$.
