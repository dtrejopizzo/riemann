# 113.07 — $h(1)$ is a norm: the admissibility constraint is both impossible and unnecessary

> **What this file does.** It computes the functional $h(1)$ in closed form and
> finds that it is the $L^2(\mathbb R_+,du)$ **norm** of $f$:
> $$(f\star\widetilde g)(1)=\int_0^\infty f(u)\overline{g(u)}\,du
> =\frac1{2\pi}\int_{\mathbb R}\widehat f(\tfrac12+it)\overline{\widehat g(\tfrac12+it)}\,dt .$$
> Two consequences follow immediately, one destructive and one liberating.
>
> **Destructive.** The admissible class $\mathcal A$ of 113_03 requires
> $h(1)=0$. On a diagonal element $h=f\star\widetilde f$ that reads
> $\|f\|^2_{L^2(du)}=0$, i.e. $f=0$. **$\mathcal A$ contains no nonzero
> diagonal element at all** — so the class on which 113_03, 113_04 and 111_03
> were trying to build row (d) is precisely empty of the elements row (d) is
> about. 111_03 §5's open item ("is the admissible class nonempty for the
> quadratic form?") is therefore not open: the answer is *no*.
>
> **Liberating.** The constraint was never needed. By 113_06 Theorem 2.2 the
> Weil identity holds on all of $\mathcal S_{>1}$ with no condition on $h(1)$.
> So we discard $\mathcal A$ and replace it by a $*$-algebra $\mathcal D$ that
> is stable under $\star$ and under the involution, contains the diagonal, and
> on which the pairing is defined outright. The obstruction dissolves rather
> than being circumvented.

$$\boxed{\texttt{IDENTITY\_FUNCTIONAL\_CLOSED\_FORM: PROVED}}$$
$$\boxed{\texttt{ADMISSIBLE\_CLASS }\mathcal A\texttt{ FOR ROW (d): REFUTED (empty on the diagonal)}}$$
$$\boxed{\texttt{PAIRING\_DOMAIN }\mathcal D\texttt{: CONSTRUCTED, }*\texttt{-ALGEBRA, CONTAINS THE DIAGONAL}}$$
$$\boxed{\texttt{111\_03 §5 OPEN ITEM: CLOSED (negatively, then dissolved)}}$$

---

## 1. Balanced coordinates

Convention B of 113_05 throughout. The involution and the convolution are

$$(f\star g)(u)=\int_0^\infty f(y)\,g(u/y)\,\frac{dy}{y},
\qquad \widetilde g(u)=\frac{\overline{g(1/u)}}{u}. \tag{1.1}$$

Everything in this phase has been carried in the profile $\tilde f(x)=f(e^x)$,
where the involution reads $\widetilde{f}^{\,\sim}(x)=\overline{\tilde f(-x)}e^{-x}$
— an asymmetric formula that costs a full unit of exponential decay on one
side and has been the source of the bookkeeping trouble. One change of
variable removes it.

> ### Definition 1.1 (balanced profile)
> $$F(x):=e^{x/2}\tilde f(x)=e^{x/2}f(e^x).$$

> ### Lemma 1.2 (the three operations in balanced coordinates)
> Let $F,G$ be the balanced profiles of $f,g$. Then
> 1. $\;\widetilde g$ has balanced profile $\;x\mapsto\overline{G(-x)}$;
> 2. $\;f\star g$ has balanced profile $\;F*G$ (ordinary additive convolution on $\mathbb R$);
> 3. $\;\widehat f(s)=\widehat F(s-\tfrac12)$, where $\widehat F(w)=\int F(x)e^{wx}dx$;
>    in particular $\widehat f(\tfrac12+it)=\mathcal F F(t):=\int F(x)e^{itx}dx$.

**Proof.** (1) $\widetilde g^{\,\sim}(x)=\overline{\tilde g(-x)}e^{-x}$, so its
balanced profile is $e^{x/2}\overline{\tilde g(-x)}e^{-x}
=\overline{e^{(-x)/2}\tilde g(-x)}=\overline{G(-x)}$.
(2) $(f\star g)^\sim=\tilde f*\tilde g$, and
$e^{x/2}(\tilde f*\tilde g)(x)=\int e^{t/2}\tilde f(t)\,e^{(x-t)/2}\tilde g(x-t)\,dt=(F*G)(x)$.
(3) $\widehat f(s)=\int\tilde f(x)e^{sx}dx=\int F(x)e^{(s-1/2)x}dx$. $\square$

So in balanced coordinates the involution is the plain conjugate-reflection
$G\mapsto\overline{G(-\cdot)}$ — an **isometry of every $\mathcal S_\theta$,
losing nothing** — and the reflection $s\mapsto1-\bar s$ of 113_05 Lemma 2.3
becomes $w\mapsto-\bar w$, the reflection of the strip $|\!\mathrm{Re}\,w|<\theta$
in its own axis. This is the coordinate the problem was always asking for.

> ### Definition 1.3 (the pairing domain)
> For $\theta>0$ put $\mathcal D_\theta:=\{f:\ F\in\mathcal S_\theta\}$ with
> $\mathcal S_\theta$ as in (1.2) of 113_06, and
> $$\boxed{\ \mathcal D:=\bigcup_{\theta>3/2}\mathcal D_\theta.\ }$$

> ### Lemma 1.4 ($\mathcal D_\theta$ is a commutative $*$-algebra, and $\mathcal D\subset\mathcal S_{>1}$)
> For every $\theta>0$:
> 1. $f,g\in\mathcal D_\theta\Rightarrow f\star g\in\mathcal D_\theta$;
> 2. $g\in\mathcal D_\theta\Rightarrow\widetilde g\in\mathcal D_\theta$, and $\widetilde{\widetilde g}=g$;
> 3. $f\in\mathcal D_\theta\Rightarrow\widehat f$ is holomorphic on
>    $|\!\mathrm{Re}\,s-\tfrac12|<\theta$ and decays faster than every
>    polynomial on each closed substrip;
> 4. $f\in\mathcal D_\theta\Rightarrow\tilde f\in\mathcal S_{\theta-1/2}$.
>
> Consequently, for $f,g\in\mathcal D$ the element $h=f\star\widetilde g$ lies
> in $\mathcal D$ and satisfies $\tilde h\in\mathcal S_{>1}$, so **113_06
> Theorem 2.2 applies to it**.

**Proof.** (1) $\mathcal S_\theta*\mathcal S_\theta\subseteq\mathcal S_\theta$:
if $|F(x)|\le C_N(1+|x|)^{-N}e^{-\theta|x|}$ and likewise for $G$, then
$|F*G|(x)\le C_N^2e^{-\theta|x|}\int(1+|t|)^{-N}(1+|x-t|)^{-N}e^{\theta(|x|-|t|-|x-t|)}dt$;
the exponent is $\le0$ by the triangle inequality, and
$\int(1+|t|)^{-N}(1+|x-t|)^{-N}dt\le C(1+|x|)^{-N}$ for $N\ge2$. Derivatives:
$(F*G)'=F'*G$. (2) Immediate from Lemma 1.2(1), since $x\mapsto\overline{G(-x)}$
has the same decay and smoothness as $G$; the involution is an involution
because conjugate-reflection squares to the identity. (3) Lemma 1.1 of 113_06
applied to $F$, transported by Lemma 1.2(3). (4) $\tilde f(x)=e^{-x/2}F(x)$,
so $|\tilde f(x)|\le C_N(1+|x|)^{-N}e^{-x/2-\theta|x|}$, and
$-x/2-\theta|x|\le-(\theta-\tfrac12)|x|$ for both signs of $x$. For the last
sentence, $\theta>3/2$ gives $\theta-\tfrac12>1$. $\square$

$\mathcal D$ is not thin. Every $f$ with $F$ a Gaussian times a polynomial
lies in $\mathcal D_\theta$ for **every** $\theta$; e.g.
$f(u)=u^{-1/2}e^{-(\log u)^2}$ has $\widehat f(s)=\sqrt\pi\,e^{(s-1/2)^2/4}$,
entire and rapidly decaying on every vertical line. This is exactly the point
recorded in the phase-111 notes: compact support dies because Paley–Wiener
demands finite exponential type and $\xi$ has infinite type, whereas Schwartz
data survives.

---

## 2. The identity functional in closed form

> ### Theorem 2.1
> Let $f,g\in\mathcal D_\theta$, $\theta>0$, and $h=f\star\widetilde g$. Then
> $$\boxed{\;L(f,g):=h(1)=\int_0^\infty f(u)\,\overline{g(u)}\,du
> \;=\;\int_{\mathbb R}F(x)\overline{G(x)}\,dx
> \;=\;\frac1{2\pi}\int_{\mathbb R}\widehat f(\tfrac12+it)\,\overline{\widehat g(\tfrac12+it)}\,dt.\;}
> \tag{2.1}$$
> In particular $L$ is a **positive definite** Hermitian inner product:
> $L(f,f)=\|F\|_{L^2(\mathbb R)}^2=\|f\|^2_{L^2(\mathbb R_+,du)}>0$ for $f\ne0$.

**Proof.** $h(1)=\tilde h(0)=H(0)$ where, by Lemma 1.2, $H=F*\overline{G(-\cdot)}$.
Hence
$$H(0)=\int F(t)\,\overline{G(-(0-t))}\,dt=\int F(t)\overline{G(t)}\,dt.$$
Undoing the balancing, $\int F\overline G\,dx=\int\tilde f(x)\overline{\tilde g(x)}e^{x}dx
=\int_0^\infty f(u)\overline{g(u)}\,u\,\frac{du}{u}=\int_0^\infty f\overline g\,du$.
The last equality in (2.1) is Plancherel for the Fourier transform
$\mathcal FF(t)=\widehat f(\tfrac12+it)$ of Lemma 1.2(3), with the convention
$\int|F|^2dx=\frac1{2\pi}\int|\mathcal FF|^2dt$. Positivity is then read off
the middle expression. $\square$

Note what the critical line is doing in (2.1): $s\mapsto1-\bar s$ fixes
$\mathrm{Re}\,s=\tfrac12$ pointwise, so on that line the mirrored pairing
of 113_05 Theorem 3.1 collapses to the diagonal one. The line $\mathrm{Re}\,s=\frac12$
is not put in by hand; it is the fixed locus of the involution the algebra
already carries.

> ### Corollary 2.2 (correction to 113_04 §2)
> 113_04 §2 treats $L(g):=h(1)$ as "a specific linear functional of $g$ alone"
> and argues that three linear functionals plausibly have a common kernel. By
> (2.1), $L$ is a **positive definite Hermitian form**, not a linear functional.
> The plausibility argument of 113_04 §2 does not apply, and its conclusion is
> false in the diagonal case by Corollary 2.3.

> ### Corollary 2.3 (the admissible class is empty on the diagonal — refutation)
> Let $\mathcal A=\{h:\tilde h\in\mathcal S_{>1},\,h(1)=0\}$ be the admissible
> class of 113_03 Definition 1.1. Then for $f\in\mathcal D$,
> $$f\star\widetilde f\in\mathcal A\iff\|f\|_{L^2(\mathbb R_+,du)}=0\iff f=0 .$$
> Hence $\mathcal A$ contains **no** nonzero element of the form
> $f\star\widetilde f$, and the quadratic form $Q(f)=\mathfrak T(f\star\widetilde f)$
> — the only thing row (d) is about — is identically undefined on $\mathcal A$.

This is a hard refutation, and it is the correct verdict on a line of work
that 113_03, 113_04 and 111_03 §5 had left as "not established". It was not
that the admissible example was hard to construct; there is none.

> ### Remark 2.4 (why 113_04's numerics did not catch this)
> $L(f,g)$ for $f\ne g$ **can** vanish, and the phase-113 notes exhibited a
> case: taking $\widehat f=\xi\widehat g$ on the critical line gives, since
> $\xi(\tfrac12+it)\in\mathbb R$,
> $$L(f,g)=\frac1{2\pi}\int_{\mathbb R}\xi(\tfrac12+it)\,|\widehat g(\tfrac12+it)|^2\,dt,
> \tag{2.2}$$
> which is a real *indefinite* form because $\xi$ is real and sign-changing on
> the critical line — $\xi(\tfrac12)=0.4971$, $\xi(\tfrac12+14i)=+2.013\times10^{-4}$,
> $\xi(\tfrac12+14.5i)=-4.068\times10^{-4}$, $\xi(\tfrac12+16i)=-7.687\times10^{-4}$,
> $\xi(\tfrac12+21.1i)=+1.304\times10^{-6}$ — so mass can be balanced between a
> region where $\xi>0$ and one where $\xi<0$ to make $L(f,g)=0$ by the
> intermediate value theorem. That is consistent with Theorem 2.1: an inner
> product is definite only on the diagonal. The off-diagonal vanishing is
> genuine and is what the earlier exploration found; it simply does not help,
> because row (d) needs the diagonal.

---

## 3. The constraint was unnecessary

> ### Theorem 3.1 (the pairing on $\mathcal D$, unconstrained)
> For $f,g\in\mathcal D$ set $h=f\star\widetilde g$ and
> $$\boxed{\;I_\partial(f,g):=\widehat h(0)+\widehat h(1)-\sum_{\rho\in Z}m_\rho\widehat h(\rho)\;}
> \tag{3.1}$$
> Then:
> 1. $I_\partial$ is well defined (the zero sum converges absolutely) and
>    equals $P(h)+W_\infty(h)$ by 113_06 Theorem 2.2 — **no hypothesis on
>    $h(1)$ is used**;
> 2. in coordinates, with $\rho'=1-\bar\rho$,
>    $$I_\partial(f,g)=\widehat f(0)\overline{\widehat g(1)}+\widehat f(1)\overline{\widehat g(0)}
>    -\sum_\rho m_\rho\,\widehat f(\rho)\,\overline{\widehat g(\rho')}\,;
>    \tag{3.2}$$
> 3. $I_\partial$ is sesquilinear and Hermitian: $I_\partial(g,f)=\overline{I_\partial(f,g)}$;
> 4. the diagonal is available: for every $f\in\mathcal D$,
>    $$Q(f):=I_\partial(f,f)=2\mathrm{Re}\,\bigl[\widehat f(0)\overline{\widehat f(1)}\bigr]
>    -\sum_\rho m_\rho\,\widehat f(\rho)\,\overline{\widehat f(\rho')}\in\mathbb R .
>    \tag{3.3}$$

**Proof.** (1) Lemma 1.4 puts $\tilde h\in\mathcal S_{>1}$; apply 113_06
Theorem 2.2. (2) 113_05 Theorem 3.1 gives
$\widehat h(s)=\widehat f(s)\overline{\widehat g(1-\bar s)}$; evaluate at
$s=0,1,\rho$, using $1-\bar 0=1$ and $1-\bar1=0$. Note $\widehat g$ is defined
at $0$ and $1$ because $\theta>3/2>\tfrac12$ puts both inside the strip
$|\!\mathrm{Re}\,s-\tfrac12|<\theta$. (3) $\widetilde{f\star\widetilde g}=g\star\widetilde f$
by Lemma 1.2(1)–(2), and (3.2) visibly conjugate-swaps: the zero set $Z$ is
stable under $\rho\mapsto\rho'$ with $m_{\rho'}=m_\rho$ (from $\xi(s)=\xi(1-s)$
and $\overline{\xi(\bar s)}=\xi(s)$), so the sum reindexes. (4) Set $g=f$ in
(3.2); Hermitian symmetry makes the value real. $\square$

> ### What replaces the "renormalisation" story
> 107_239 (1.4) defines $\mathfrak T_S$ as a truncated trace minus a
> counterterm $2h(1)\log\Lambda$, and 113_03 imposed $h(1)=0$ to kill it.
> 113_06 Theorem 4.1 showed that on $h(1)=0$ data every *place-by-place* Tate
> integral converges absolutely. The present file shows that requirement is
> unsatisfiable on the diagonal. The resolution is that the **Weil regrouping
> is convergent anyway**: $\sum_n\Lambda(n)[h(n)+h(1/n)/n]$ and the $\Gamma$-kernel
> integral $A(h)$ each converge absolutely for every $\tilde h\in\mathcal S_{>1}$
> (113_06 Theorem 2.2, Steps 4–5), $h(1)$ or no $h(1)$. The divergence that
> $2h(1)\log\Lambda$ was cancelling is an artefact of splitting the archimedean
> place into a Tate local integral, not a feature of the pairing.
>
> The candid cost is recorded plainly: **for $h(1)\ne0$, $I_\partial$ is no
> longer presented as an operator trace.** Assumption T2 of 113_06 §5 is
> stated for $\mathcal A$; on $\mathcal D$ it would need the renormalised
> version. Nothing in rows (a)–(d) requires the trace interpretation —
> $I_\partial$ is used as a Hermitian pairing on divisors, and (3.1) defines it
> outright.

---

## 4. Where this leaves row (d)

With Theorem 3.1 the coordinate model of 107_241 is now available on a genuine
$*$-algebra containing the diagonal. Recall 107_241 Theorem 3.1: on the
coordinate space $\mathbb C^{\{0,1\}}\oplus\mathbb C^Z$ the form (3.2) has

$$n_+=1+\#P,\qquad n_-=1+\#L+\#P,$$

$P$ = off-critical mirror pairs $\{\rho,\rho'\}$, $L$ = critical zeros, and
Corollary 3.3: $\mathrm{RH}\iff n_+=1$. Concretely: the two polar coordinates
$(\widehat f(0),\widehat f(1))$ carry a hyperbolic plane of signature $(1,1)$;
each critical zero contributes $-m_\rho|\widehat f(\rho)|^2\le0$; each
off-critical mirror pair contributes a hyperbolic plane of signature $(1,1)$.

> ### Proposition 4.1 (the exact remaining statement of row (d))
> Let $\mathcal D^\circ:=\{f\in\mathcal D:\widehat f(0)=\widehat f(1)=0\}$. Then
> $$\mathrm{RH}\iff Q(f)\le0\ \text{ for all }f\in\mathcal D^\circ
> \iff -\sum_\rho m_\rho\widehat f(\rho)\overline{\widehat f(\rho')}\le0
> \ \text{ on }\mathcal D^\circ .$$

**Proof.** ($\Leftarrow$) If some $\rho_0$ is off the line, pick
$f\in\mathcal D^\circ$ with $\widehat f(\rho_0)=1$, $\widehat f(\rho_0')=-1$ and
$\widehat f$ small at every other zero and at $0,1$; then $Q(f)>0$ by the
computation of 113_05 Remark 3.3. ($\Rightarrow$) If all $\rho=\rho'$ then
every term is $-m_\rho|\widehat f(\rho)|^2\le0$. $\square$

The interpolation in ($\Leftarrow$) needs $\mathcal D^\circ$ to be rich enough
to prescribe two values and control the rest; that is a Paley–Wiener style
statement about $\mathcal D$, **and it is not proved here**. What is proved is
the ($\Rightarrow$) direction and the algebraic content of the equivalence in
the coordinate model.

So row (d) is now a clean, self-contained inequality on a well-defined
$*$-algebra, with no admissibility side condition, no renormalisation, and no
undischarged trace assumption. That is progress of the "the statement is finally
correctly posed" kind. **It is not a proof of the inequality, and this file
does not claim one.** The inequality is Weil positivity.

---

## 5. Correction ledger

| # | where | defect | correction |
|---|---|---|---|
| 1 | 113_04 §2 | $L(g):=h(1)$ called "a linear functional of $g$ alone"; three-linear-functionals-have-a-common-kernel argument | Theorem 2.1: $L$ is a positive definite Hermitian form. Argument withdrawn (Cor 2.2). |
| 2 | 113_03 Def 1.1, and everything built on $\mathcal A$ | the class $\mathcal A$ is empty of nonzero diagonal elements | Corollary 2.3. Replace $\mathcal A$ by $\mathcal D$ (Def 1.3). |
| 3 | 111_03 §5 "not established: the admissible class is nonempty for the quadratic form" | listed as open | **closed, negatively** (Cor 2.3), then dissolved (Thm 3.1) |
| 4 | 113_03 §3, 113_04 §3 | $h(1)=0$ treated as necessary for the pairing to exist | Theorem 3.1(1): not needed; 113_06 Thm 2.2 has no such hypothesis |
| 5 | phase-113 working notes | "$L(g)=0$ is achievable by IVT, so admissibility is fine" | true off-diagonal, false on the diagonal (Remark 2.4) |

Corrections 1–3 retire a line of work. Correction 4 opens the replacement.
None of them bears on RH.

---

## 6. Scope

**Proved here.** Lemma 1.2 (the three operations in balanced coordinates).
Lemma 1.4 ($\mathcal D_\theta$ is a $*$-algebra under $\star$; $\mathcal D\subset\mathcal S_{>1}$).
Theorem 2.1 (closed form of $h(1)$; positive definiteness). Corollaries 2.2,
2.3. Theorem 3.1 ($I_\partial$ on $\mathcal D$, sesquilinear, Hermitian,
diagonal available, equal to the Weil right-hand side). Proposition 4.1
(($\Rightarrow$) fully; ($\Leftarrow$) modulo an unproved interpolation
statement about $\mathcal D$, flagged as such).

**Read from source, not re-derived.** 113_05 Decision 1.1, Lemma 2.3,
Theorem 3.1, Proposition 4.1. 113_06 Lemma 1.1, Theorem 2.2. 107_241
Lemma 2.2, Theorem 3.1, Corollaries 3.3, 3.4 (the signature count in the
coordinate model). $\xi(s)=\xi(1-s)$ and $\overline{\xi(\bar s)}=\xi(s)$.

**Verified numerically.** All three expressions in (2.1) agree; $L(f,f)>0$ on
five probes and equals $\|F\|_2^2$; $(f\star\widetilde f)(1)=\|f\|^2>0$, so
$f\star\widetilde f\notin\mathcal A$; the balanced involution formula of
Lemma 1.2(1); 113_06 Theorem 2.2 holds on the diagonal element
$h=f\star\widetilde f$ with $h(1)=\sqrt{\pi/2}\ne0$ — i.e. on exactly the data
$\mathcal A$ excludes; formula (3.3) for $Q(f)$ agrees with $P(h)+W_\infty(h)$;
the sign changes of $\xi$ on the critical line quoted in Remark 2.4.

Also — and this is the check that most directly earns the file — **$\mathcal D^\circ$
is exhibited nonempty**, at exactly the place $\mathcal A$ was empty. Take the
balanced profile
$$F(x)=e^{-ax^2}\cos(bx),\qquad b=14,\ a=\tfrac b{2\pi},$$
so that $\widehat f(s)=\sqrt{\pi/a}\,e^{((s-1/2)^2-b^2)/4a}\cos\bigl((s-\tfrac12)b/2a\bigr)$
and $b/4a=\pi/2$ forces $\widehat f(0)=\widehat f(1)=0$ identically
($|\widehat f(0)|=|\widehat f(1)|=9.7\times10^{-26}$ numerically). Then
$$Q(f)=-0.702117236,\qquad P(h)+W_\infty(h)=-0.702117236,\qquad
\text{residual }4.0\times10^{-14},$$
with $|\widehat f(\tfrac12+i\gamma_1)|=0.5925$, so the zero sum genuinely
carries the value — the data point is not vacuous. ($b=14$ is a round number,
not a zero ordinate; no zero of $\xi$ enters the construction of the probe.
Choosing $b$ near the low zeros is what makes the test bite: a probe with mass
only near $t=0$ has $|\widehat f(\rho)|\sim10^{-22}$ and tests nothing.)
Note $h(1)=\|F\|_2^2=0.4198\ne0$ for this $f$ as well — the two constraints
$h(1)=0$ and $\widehat f(0)=\widehat f(1)=0$ are independent, and it is the
first that is unsatisfiable, not the second.

**Not established, and explicitly not claimed.** Weil positivity, i.e.
$Q\le0$ on $\mathcal D^\circ$ (Proposition 4.1) — this is row (d) and it is
open. The interpolation richness of $\mathcal D$ used in Proposition 4.1
($\Leftarrow$). Any trace interpretation of $I_\partial$ for $h(1)\ne0$.
Anything about rows (a), (b), (c). Anything about RH.

## 7. Verifier

`113_07_the_identity_functional_is_a_norm.py` — exits 0 with
`VERDICT: ALL CHECKS PASS`. Zeros of $\xi$ appear only inside the numerical
check of the classical identity quoted from 113_06; no definition in this file
uses a zero of $\xi$, a Li coefficient, or a positive part of a Weil-type form.
The evaluations of $\xi$ on the critical line in Remark 2.4 are evaluations of
$\xi$, which the source rule permits.
