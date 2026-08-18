# 108.07 — The archimedean local term of $\mathfrak T_S$ on the graded family

## 0. What this settles

108_06 computed the local term $W_p(f_a)$ at every finite place and found it
convergent exactly on the critical strip $0<\Re a<1$. This note computes the
remaining local term, at the archimedean place, in closed form:

\[
 \boxed{\;W_\infty(f_a)=\pi\cot\!\Big(\frac{\pi a}{2}\Big)\;},\qquad 0<\Re a<1,
\]

proves that this integral converges on **exactly the same strip** as the
finite places (not a larger or smaller one), and checks that the closed form
is regular throughout the open strip, with $W_\infty(f_{1/2})=\pi$.

No zero of $\xi$ or $\zeta$ enters anything below.

## 1. Setup and normalization convention

Embedding through the module as in 108_06 §3, $f_a(u^{-1})=|u|^a$ for
$u\in\mathbb R^\times$, and

\[
 W_\infty(f_a)=\int_{\mathbb R^\times}{}'\frac{|u|^a}{|1-u|}\,d^\times u,
 \qquad d^\times u=\frac{du}{|u|},
\]

so, as a $du$-integral, the integrand is $|u|^{a-1}/|1-u|$. Two conventions
are fixed explicitly, since the problem does not determine them on its own:

* **Absolute value.** $\mathbb R$ is a real place, so $|\cdot|$ is the
  ordinary absolute value on $\mathbb R$ (not squared, as it would be for a
  complex place). This is the direct real-place analogue of 108_06's
  $p$-adic $|\cdot|_p$.
* **Principal value.** The only non-integrable point on $\mathbb R^\times$
  is $u=1$ (verified in §4 below: $u=0$ and $u=\infty$ are ordinary
  convergence questions, not singularities, once $0<\Re a<1$). "PV" means
  the symmetric limit
  \[
   \text{PV}\!\int_0^\infty \frac{u^{a-1}}{1-u}\,du
   :=\lim_{\varepsilon\to0^+}\left(\int_0^{1-\varepsilon}+\int_{1+\varepsilon}^\infty\right)
   \frac{u^{a-1}}{1-u}\,du .
  \]
  No power of a negative number is ever taken: the $u<0$ branch is always
  reduced to $|u|$ before any exponentiation (Proposition 2.1), so no branch
  choice of $u^{a-1}$ for $u<0$ is needed anywhere in this computation.

## 2. The $u<0$ half: a Beta integral

> ### Proposition 2.1
> \[
>  \int_{-\infty}^{0}\frac{|u|^{a-1}}{|1-u|}\,du=\int_0^\infty\frac{v^{a-1}}{1+v}\,dv .
> \]

**Proof.** Substitute $u=-v$, $v>0$; $du=-dv$, and as $u$ runs over
$(-\infty,0)$, $v$ runs over $(0,\infty)$ with the orientation reversed, so
$\int_{-\infty}^0 F(u)\,du=\int_0^\infty F(-v)\,dv$. Here
$F(u)=|u|^{a-1}/|1-u|$ and $F(-v)=v^{a-1}/|1+v|=v^{a-1}/(1+v)$ since $v>0$.
$\square$

> ### Theorem 2.2
> For $0<\Re a<1$,
> \[
>  \int_0^\infty\frac{v^{a-1}}{1+v}\,dv=\frac{\pi}{\sin(\pi a)} .
> \]

**Proof.** Substitute $v=t/(1-t)$, $t\in(0,1)$; then $dv=dt/(1-t)^2$ and
$1+v=1/(1-t)$, so
\[
 \frac{v^{a-1}}{1+v}\,dv
 = t^{a-1}(1-t)^{1-a}\cdot(1-t)\cdot\frac{dt}{(1-t)^2}
 = t^{a-1}(1-t)^{-a}\,dt .
\]
Hence the integral equals the Beta integral $B(a,1-a)=\int_0^1
t^{a-1}(1-t)^{-a}dt$, convergent precisely for $\Re a>0$ and $\Re(1-a)>0$,
i.e. $0<\Re a<1$. By the standard identity $B(a,1-a)=\Gamma(a)\Gamma(1-a)$
and Euler's reflection formula $\Gamma(a)\Gamma(1-a)=\pi/\sin(\pi a)$
(classical; e.g. via the Weierstrass product for $1/\Gamma$), the claim
follows. $\square$

This half needs **no** principal value: the integrand $v^{a-1}/(1+v)$ has no
pole on $(0,\infty)$.

## 3. The $u>0$ half: a cotangent integral, in principal value

> ### Theorem 3.1
> For $0<\Re a<1$,
> \[
>  \text{PV}\!\int_0^\infty\frac{u^{a-1}}{1-u}\,du=\pi\cot(\pi a).
> \]

**Proof.** Split at $u=1$ and substitute $x=1/u$ on the outer piece. For
$u\in(1,\infty)$, put $u=1/x$, $x\in(0,1)$; then $du=-dx/x^2$,
$u^{a-1}=x^{1-a}$, $1-u=(x-1)/x$, so
\[
 \frac{u^{a-1}}{1-u}\,du
 = \frac{x^{1-a}}{(x-1)/x}\cdot\Big(-\frac{dx}{x^2}\Big)
 = -\frac{x^{-a}}{1-x}\,dx .
\]
Tracking orientation ($u:1\to\infty$ corresponds to $x:1\to0$),
\[
 \text{PV}\!\int_1^\infty\frac{u^{a-1}}{1-u}\,du
 = -\,\text{PV}\!\int_0^1\frac{x^{-a}}{1-x}\,dx .
\]
Both principal values are symmetric $\varepsilon$-exclusions around the
common point $1$; under $x=1/u$ the interval $u\in(1-\varepsilon,1+\varepsilon)$
maps to $x\in(1-\varepsilon+O(\varepsilon^2),\,1+\varepsilon+O(\varepsilon^2))$,
so the exclusions coincide to $O(\varepsilon^2)$, an error that vanishes as
$\varepsilon\to0$. Adding the two pieces on a **common** excised interval
therefore gives, for $0<\Re a<1$,
\[
 \text{PV}\!\int_0^\infty\frac{u^{a-1}}{1-u}\,du
 = \lim_{\varepsilon\to0}\int_{[0,1]\setminus(1-\varepsilon,1+\varepsilon)}
   \frac{u^{a-1}-u^{-a}}{1-u}\,du .
\]
Near $u=1$ the numerator $u^{a-1}-u^{-a}\to1-1=0$ while the denominator
$\to0$ too; by L'Hôpital the ratio tends to $-(2a-1)$, a **finite** value.
So the combined integrand extends continuously across $u=1$, the
singularity is removable, and the limit is simply the ordinary (absolutely
convergent, for $0<\Re a<1$) integral
\[
 \int_0^1\frac{u^{a-1}-u^{-a}}{1-u}\,du .
\]

It remains to evaluate this. The digamma function has the classical series
$\psi(s)=-\gamma+\sum_{n=0}^\infty\big(\tfrac1{n+1}-\tfrac1{n+s}\big)$
($s\ne0,-1,-2,\dots$) and the equivalent integral representation
(standard; e.g. DLMF 5.9.16)
\[
 \psi(s)=-\gamma+\int_0^1\frac{1-t^{s-1}}{1-t}\,dt,\qquad \Re s>0 .
\]
Applying this at $s=1-a$ and at $s=a$ and subtracting,
\[
 \psi(1-a)-\psi(a)=\int_0^1\frac{t^{a-1}-t^{-a}}{1-t}\,dt .
\]
Finally, logarithmically differentiating Euler's reflection formula
$\Gamma(a)\Gamma(1-a)=\pi/\sin(\pi a)$ (already used in Theorem 2.2) in $a$
gives $\psi(a)-\psi(1-a)=-\pi\cot(\pi a)$, i.e.
$\psi(1-a)-\psi(a)=\pi\cot(\pi a)$. Combining the last two displays proves
the theorem. $\square$

## 4. The combined closed form

> ### Theorem 4.1
> For $0<\Re a<1$,
> \[
>  W_\infty(f_a)=\pi\cot(\pi a)+\frac{\pi}{\sin(\pi a)}=\pi\cot\!\Big(\frac{\pi a}{2}\Big).
> \]

**Proof.** $W_\infty(f_a)$ is the sum of the two halves (Proposition 2.1 +
Theorem 2.2, and Theorem 3.1). It remains to check the trigonometric
identity $\cot x+\csc x=\cot(x/2)$ at $x=\pi a$. Indeed
\[
 \cot x+\csc x=\frac{\cos x+1}{\sin x}
 =\frac{2\cos^2(x/2)}{2\sin(x/2)\cos(x/2)}=\cot(x/2),
\]
using the half-angle identities $\cos x+1=2\cos^2(x/2)$ and
$\sin x=2\sin(x/2)\cos(x/2)$. $\square$

## 5. Convergence: exactly the same strip as the finite places

> ### Theorem 5.1
> The integral defining $W_\infty(f_a)$ (in the PV sense of §1) converges
> if and only if $0<\Re a<1$ — the same open strip as Corollary 3.2 of
> 108_06.

**Proof.** Away from $u=1$ (handled in §3, convergent there for every $a$ by
the removable-singularity argument, with no further constraint on $a$), the
only two remaining convergence questions are at $u=0$ and $u=\infty$.

*Near $u=0$*: $|1-u|\to1$, so the integrand behaves like $|u|^{a-1}$, and
$\int_0|u|^{a-1}du$ converges at the lower endpoint iff $\Re(a-1)>-1$, i.e.
$\Re a>0$.

*Near $u=\infty$*: $|1-u|\sim|u|$, so the integrand behaves like
$|u|^{a-1}/|u|=|u|^{a-2}$, and $\int^\infty|u|^{a-2}du$ converges at the
upper endpoint iff $\Re(a-2)<-1$, i.e. $\Re a<1$.

Both conditions are necessary (each governs an independent endpoint) and,
together, sufficient (§2–§3 supply absolute or removable-singularity
convergence everywhere else once $0<\Re a<1$). $\square$

> **This is worth stating plainly**, echoing 108_06 §3: the critical strip
> reappears here purely from elementary power-counting of a real integral at
> its two endpoints — no zero, no functional equation, no $p$-adic input.
> The finite places (108_06) and the archimedean place (here) converge on
> *exactly* the same strip, independently derived.

## 6. Regularity at $a=\tfrac12$

> ### Corollary 6.1
> $\pi\cot(\pi a/2)$ is holomorphic on the whole open strip $0<\Re a<1$: its
> poles are at $a=0,\pm2,\pm4,\dots$, none of which lie in the strip. In
> particular it is regular at $a=\tfrac12$, where
> \[
>  W_\infty(f_{1/2})=\pi\cot\!\Big(\frac\pi4\Big)=\pi .
> \]

**Proof.** $\cot(z)$ has simple poles exactly at $z\in\pi\mathbb Z$; with
$z=\pi a/2$ this is $a\in2\mathbb Z$, disjoint from $0<\Re a<1$. At
$a=1/2$: $\pi a/2=\pi/4$, $\cot(\pi/4)=1$. $\square$

Contrast: 108_06's $C_p$ (the Tate principal value at $|u|_p=1$) is a
genuinely $a$-independent finite-place constant left unevaluated there;
here the *entire* archimedean term is in closed form and is manifestly
regular at $a=1/2$ — there is no analogous unresolved constant at the
archimedean place.

## 7. Scope

Proved:

* Proposition 2.1 and Theorem 2.2: the $u<0$ half equals $\pi/\sin(\pi a)$,
  by reduction to the Beta integral and Euler's reflection formula;
* Theorem 3.1: the $u>0$ half, in the principal-value sense of §1, equals
  $\pi\cot(\pi a)$, by a removable-singularity reduction plus the digamma
  reflection formula (itself derived here from Euler's reflection formula
  by logarithmic differentiation);
* Theorem 4.1: the closed form $W_\infty(f_a)=\pi\cot(\pi a/2)$;
* Theorem 5.1: the archimedean integral converges if and only if
  $0<\Re a<1$, matching the finite-place strip of 108_06 Corollary 3.2
  exactly;
* Corollary 6.1: $\pi\cot(\pi a/2)$ is regular throughout the open strip,
  in particular at $a=1/2$ where it equals $\pi$.

Verified numerically: the two half-integrals against symmetric-midpoint
quadrature (which realizes the principal value directly, since grid points
never land on the pole and symmetric pairs cancel its leading term) for six
grades, three real and three complex, at two grid resolutions, confirming
error shrinkage consistent with the quadrature order; the endpoint power
laws near $u=0$ and $u=\infty$ by threshold-free log–log slope fits against
$\Re a$ and $\Re a-1$ respectively, for grades both inside and outside the
strip; the elementary trigonometric identity $\cot x+\csc x=\cot(x/2)$; the
value $\pi$ at $a=1/2$.

Not established, and explicitly not claimed:

* any global (multi-place) statement — this note is purely the archimedean
  local term, exactly parallel to 108_06's purely finite-place local terms;
* measure-valuedness in $a$ (as in 108_06 §6, this is a holomorphic-in-$a$
  statement on the strip, not yet a distributional one);
* any comparison with the zero side of the explicit formula, and no zero of
  $\zeta$ or $\xi$ has been used anywhere above;
* any change to `ROW_A_STATUS`, which remains `partial`.

## 8. Verifier

`108_07_archimedean_local_term.py` checks: Theorem 2.2 and Theorem 3.1
against symmetric-midpoint quadrature at two resolutions (error shrinkage
consistent with a second-order rule) for six grades $a$ with $0<\Re a<1$
(three real, three complex); the combined value against $\pi\cot(\pi a/2)$;
the trigonometric identity of Theorem 4.1; the endpoint convergence
conditions of Theorem 5.1 via threshold-free log–log exponent fits, both
inside and outside the strip; and the value $\pi$ at $a=1/2$ from
Corollary 6.1.
