# 108.15 — Route C: the primitive restriction does not annihilate the
# constant (except vacuously)

## 0. Result

$\sum_pC_p$ enters the assembly of 108_11/108_12 as a fixed scalar
multiplying the smooth density $c_g(a)\,da$, $c_g$ the entire function of
108_06 Proposition 2.1. 107_241 Corollary 3.4 restricts a *different*
pairing to the primitive subspace $\hat f(0)=\hat f(1)=0$ and finds the
polar/generic-point contribution vanishes identically there. This note
tests whether the analogous restriction on $g$ kills $\sum_pC_p$'s
contribution here.

> **It does not, except vacuously. The transported primitive condition
> constrains $c_g$ at finitely many points; the constant multiplies $c_g$
> in bulk over the whole open interval $(0,1)$. An entire function that
> vanishes at finitely many points need not vanish on an interval — and,
> conversely, an entire function that vanishes on a whole open interval
> already vanishes everywhere, forcing $g\equiv0$. So the only restriction
> of $g$ that annihilates the constant for every test function is the
> trivial one. Route C, in the form proposed, fails to close Stage 1.**

An explicit, non-primitive-in-the-naive-sense counterexample is
constructed and verified numerically in §4: a nonzero, compactly supported
$g$ with $\hat g(0)=\hat g(1)=0$ exactly, whose $c_g$ is nonetheless
nonzero throughout the interior of $(0,1)$. No zero of $\xi$ is used
anywhere.

## 1. Setup

108_06 Proposition 2.1: for $g\in C_c^\infty(0,\infty)$ and
$\tilde g(x)=\overline{g(1/x)}$,

\[
 c_g(a)=\int_0^\infty t^{-a}\,\overline{g(t)}\,d^\times t,
\]

entire in $a$ (108_06, stated after the proposition). Write, matching
107_241 §1's convention,

\[
 \hat g(s):=\int_0^\infty g(t)\,t^{s}\,d^\times t,
\]

also entire since $g$ is compactly supported away from $0$ and $\infty$.

> ### Lemma 1.1
> For real $a$, $c_g(a)=\overline{\hat g(-a)}$; both sides continue to the
> same entire function of $a\in\mathbb C$.

**Proof.** For real $a$, $\overline{\hat g(-a)}=\overline{\int_0^\infty
g(t)t^{-a}d^\times t}=\int_0^\infty\overline{g(t)}\,t^{-a}d^\times t=c_g(a)$
(the exponent $t^{-a}$ is real for real $a,t>0$). Both $a\mapsto c_g(a)$ and
$a\mapsto\overline{\hat g(-\bar a)}$ are entire and agree on the real axis,
hence agree everywhere by the identity theorem. On the real axis
$\overline{\hat g(-\bar a)}=\overline{\hat g(-a)}$, giving the stated
formula there; for complex $a$ the correct entire continuation is
$c_g(a)=\overline{\hat g(-\bar a)}$, which restricts to the real-axis
formula used below. $\square$

## 2. The transported primitive condition

107_241 Corollary 3.4 restricts a test class element $f\in\mathcal A$ to
$\hat f(0)=\hat f(1)=0$. Here $f_a$ (the graded family element) is *not* in
$\mathcal A$ — 108_05 Proposition 2.1 shows $f_a$ has no Mellin transform at
all — so the condition cannot be imposed on $f_a$. The only Mellin-side
object available to restrict is $g$, the genuine test-class element that
determines $c_g$. The transported condition is therefore

\[
 \boxed{\hat g(0)=0,\qquad\hat g(1)=0.}
 \tag{2.1}
\]

By Lemma 1.1, in terms of $c_g$, these are $c_g(0)=0$ and (note the
asymmetry, a direct consequence of 108_06's unshifted involution
$\tilde g(x)=\overline{g(1/x)}$, as opposed to 107_239's shifted
$\tilde f(x)=x^{-1}\overline{f(1/x)}$ used for the bilinear pairing)
$c_g(-1)=0$. Either way, (2.1) is a condition at **two fixed points**, one
of which ($a=0$) is an endpoint of the strip and the other of which
($a=1$, equivalently $-1$ under $c_g$) lies at or outside it.

## 3. The constant cannot be annihilated by a finite-point condition

> ### Theorem 3.1
> Let $g\in C_c^\infty(0,\infty)$, $g\not\equiv0$. Then $c_g$ does not
> vanish identically on $(0,1)$; consequently there exists
> $\varphi\in C_c^\infty((0,1))$, $\varphi\ge0$, with
> \[
>  \int_0^1\varphi(a)\,c_g(a)\,da\;\ne\;0 .
> \]
> This holds regardless of whether $g$ satisfies (2.1) or any other
> constraint at finitely many points.

**Proof.** *Step 1 (Mellin injectivity).* Write $t=e^x$ and
$G(x):=g(e^x)$, a $C^\infty$ function of compact support in $x\in\mathbb R$
(since $g$ has compact support in $(0,\infty)$). Then for $s=i\xi$ purely
imaginary,
\[
 \hat g(i\xi)=\int_0^\infty g(t)\,t^{i\xi}\,d^\times t
 =\int_{-\infty}^\infty G(x)\,e^{i\xi x}\,dx,
\]
the ordinary Fourier transform of $G$. If $\hat g\equiv0$ on all of
$\mathbb C$, in particular $\hat g(i\xi)=0$ for every real $\xi$, so
$\widehat G\equiv0$; by Fourier injectivity on $C_c^\infty(\mathbb R)$
(standard: $G\in L^1\cap L^2$, its Fourier transform vanishing identically
forces $G=0$ a.e., hence $G\equiv0$ by continuity), $G\equiv0$, hence
$g\equiv0$. Contrapositive: $g\not\equiv0\Rightarrow\hat g\not\equiv0$ as an
entire function.

*Step 2 (transfer to $c_g$).* By Lemma 1.1, $c_g\equiv0$ on $\mathbb C$
would force $\hat g\equiv0$ on $\mathbb C$ (the map $a\mapsto-\bar a$ is a
bijection of $\mathbb C$), hence $g\equiv0$ by Step 1. So
$g\not\equiv0\Rightarrow c_g\not\equiv0$ as an entire function of $a$.

*Step 3 (entire + vanishing on an interval $\Rightarrow$ vanishing
everywhere).* If $c_g$ vanished identically on the open interval $(0,1)
\subset\mathbb R\subset\mathbb C$, then since $(0,1)$ has an accumulation
point in $\mathbb C$, the identity theorem for holomorphic functions forces
$c_g\equiv0$ on all of $\mathbb C$ — contradicting Step 2 when
$g\not\equiv0$. Hence $c_g\not\equiv0$ on $(0,1)$.

*Step 4 (a bump function detects it).* Since $c_g$ is continuous and not
identically $0$ on $(0,1)$, there is $a_0\in(0,1)$ with $c_g(a_0)\ne0$; by
continuity $\operatorname{Re}\big(e^{-i\theta}c_g(a)\big)$ has a fixed sign
($\theta:=\arg c_g(a_0)$) on some open interval $I\ni a_0$, $I\subset(0,1)$.
Take $\varphi\ge0$ smooth, supported in $I$, $\varphi\not\equiv0$; then
$\operatorname{Re}\big(e^{-i\theta}\int_0^1\varphi(a)c_g(a)\,da\big)
=\int_I\varphi(a)\operatorname{Re}(e^{-i\theta}c_g(a))\,da\ne0$ (a
nonnegative, not-identically-zero integrand of fixed sign), so the integral
itself is nonzero. $\square$

Nothing in this argument used (2.1) — it holds for *every* nonzero $g$,
subject to *any* finite set of point conditions on $\hat g$ or $c_g$,
because such conditions never make an entire, not-identically-zero function
vanish on an open real interval.

> ### Corollary 3.2 (Route C fails, except vacuously)
> The only $g\in C_c^\infty(0,\infty)$ for which
> $\big(\sum_pC_p\big)\int_0^1\varphi(a)c_g(a)\,da$ is annihilated for
> *every* $\varphi\in C_c^\infty((0,1))$ is $g\equiv0$. Restricting to the
> primitive subspace (2.1) — a codimension-2, still infinite-dimensional
> condition on $g$ — does **not** achieve this: Theorem 3.1 applies
> unchanged to every nonzero $g$ satisfying (2.1), and §4 exhibits an
> explicit example.

## 4. Why this differs from 107_241, and what is lost

In 107_241, primitivity ($\hat f(0)=\hat f(1)=0$) removes the two-point
evaluations $\hat f(0),\hat f(1)$ from the bilinear form's evaluation
coordinates (Lemma 2.2 there); the pairing $I_\partial$ is a *sum of
point-evaluations at* $0,1$ and $\{\rho\}$ (formula (2.1) of 107_241,
$\S2$), so killing two of those point-evaluations kills exactly the two
terms that use them.

Here the constant is different in kind: $\sum_pC_p$ multiplies $c_g(a)$,
which is not evaluated only at the boundary points $a=0,1$ — it is
integrated in bulk against $\varphi$ over the whole open interior. A
boundary condition (vanishing of $c_g$, or of $\hat g$, at two fixed
points) cannot control a bulk integral of a function that is otherwise free
to be anything on the interior, and Theorem 3.1 shows it provably does not.

**What would be lost, if it worked.** Even setting Theorem 3.1 aside: were
some restriction to force $c_g\equiv0$ on $(0,1)$, Corollary 3.2 shows this
forces $g\equiv0$, i.e. the "residual object" after restriction would carry
no information at all — Stage 1 would then hold only for the zero test
function, which is not a meaningful sense in which "Stage 1 closes." This
is exactly why the conditional in the task statement ("if it does, say so
in exactly those terms") is not triggered: it does not.

## 5. Scope

**Proved:** Lemma 1.1 (the $c_g$–$\hat g$ correspondence); Theorem 3.1 and
Corollary 3.2 (no nontrivial finite-codimension restriction on $g$
annihilates the constant's contribution to the assembly, for every test
function).

**Verified numerically (§6):** an explicit nonzero $g$ satisfying the exact
primitive condition (2.1), with $c_g$ numerically confirmed nonzero on the
interior of $(0,1)$, illustrating Theorem 3.1 concretely rather than only
abstractly.

**Not addressed:** whether some restriction of $g$ *not* of finite-point
type (e.g. a restriction on the support, or a genuinely infinite family of
moment conditions collapsing $c_g$ on a whole subinterval) could work;
Theorem 3.1's proof shows any such restriction that keeps $g\not\equiv0$
automatically keeps $c_g\not\equiv0$ on $(0,1)$, so in fact **no**
restriction on $g$ alone (short of $g\equiv0$) can annihilate the constant
for every $\varphi$ — this is a complete answer to Route C as posed, not a
partial one. Complex $a$ is not addressed.

`ROW_A_STATUS` remains `partial`. Nothing here bears on RH.

## 6. Verifier

`108_15_route_c_primitive_no_go.py` constructs an explicit compactly
supported window $g$ on $[1,2]$, solves the two linear constraints (2.1)
exactly (via quadrature-computed moments, a $2\times2$ linear system) for a
nonzero coefficient vector, verifies $\hat g(0)=\hat g(1)=0$ to quadrature
accuracy, then evaluates $c_g(a)$ by direct numerical quadrature at a grid
of $a\in(0,1)$ and confirms it is *not* identically zero — exhibiting
Theorem 3.1's conclusion concretely — and finally checks that
$\int_0^1\varphi(a)c_g(a)\,da\ne0$ for an explicit bump $\varphi$ supported
away from the endpoints.
