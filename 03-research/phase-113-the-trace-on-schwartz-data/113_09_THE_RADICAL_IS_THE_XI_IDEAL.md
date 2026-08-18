# 113.09 — d1: the radical of the intersection pairing is the ξ-ideal, and the rulings live in 𝒟

> **What this file does.** Requirement **d1** of the backward map asks for a
> "principal" subspace $\mathcal P$ contained in the radical of $I_\partial$, so
> that the pairing descends to a nondegenerate form on a quotient. The programme
> never defined $\mathcal P$; the candidates built on the groupoid side were
> refuted (108_38 Theorem 3.1: $\mathrm{Prin}'$ invariance is **false**;
> 108_50/52/53: no comparison map at generator level).
>
> This file takes the other road. In the coordinate model of 113_08 the radical
> is not a thing to be guessed — **it can be computed**, and it comes out as an
> explicit ideal:
> $$\mathrm{rad}\,I_\partial=\bigl\{f\in\mathcal D:\ \widehat f(s)=s(s-1)\,\xi(s)\,v(s),\ v\ \text{holomorphic in the strip}\bigr\}.$$
> It is a nonzero $*$-ideal of the algebra $\mathcal D$, $I_\partial$ descends to
> a nondegenerate Hermitian form on $\mathcal D/\mathrm{rad}$, and — the
> part that was not expected — **the two rulings are realised by candid elements
> of $\mathcal D$**:
> $$\widehat f_v(s)=-2(s-1)\xi(s),\qquad \widehat f_h(s)=2s\,\xi(s),\qquad
> \widehat{(f_v+f_h)}(s)=2\xi(s).$$
> This closes 113_08 Remark 2.3, makes Connes' Lemma 2.1 literally applicable
> with $E=\mathcal D$, and yields the splitting
> $\mathcal D=\mathcal D^\circ\oplus\mathbb Cf_v\oplus\mathbb Cf_h$.
>
> **And it makes the polarization checkable against the primes.** For each of
> these elements the spectral side of the Weil identity is a small integer known
> in advance, while the arithmetic side is a sum over prime powers plus a
> $\Gamma$-kernel integral in which **no zero of $\xi$ appears at all**. So
> $F_v^2=0$, $F_v\!\cdot\!F_h=1$, $H^2=2$, $(F_v-F_h)^2=-2$ become statements
> about primes. All five are confirmed to $10^{-10}$.

$$\boxed{\texttt{RADICAL: COMPUTED EXACTLY, = THE }s(s-1)\xi(s)\texttt{-IDEAL}}$$
$$\boxed{\texttt{RADICAL IS A NONZERO *-IDEAL; }I_\partial\texttt{ DESCENDS NONDEGENERATELY}}$$
$$\boxed{\texttt{RULINGS REALISED IN }\mathcal D\texttt{: 113\_08 Remark 2.3 CLOSED}}$$
$$\boxed{\texttt{d2 INTERSECTION NUMBERS VERIFIED ARITHMETICALLY (no zeros used)}}$$
$$\boxed{\texttt{d1 AS ORIGINALLY POSED (}\mathcal P\texttt{ from an independent geometry): STILL OPEN}}$$

---

## 1. A membership criterion for 𝒟

Recall (113_07 Definition 1.3) that $f\in\mathcal D_\theta$ means the balanced
profile $F(x)=e^{x/2}f(e^x)$ lies in
$\mathcal S_\theta=\{F:|F(x)|\le C_N(1+|x|)^{-N}e^{-\theta|x|}\ \forall N\}$, and
$\mathcal D=\bigcup_{\theta>3/2}\mathcal D_\theta$. Since
$\widehat f(s)=\widehat F(s-\tfrac12)$, membership is a statement about $\widehat f$.

> ### Lemma 1.1 (sufficient condition)
> Let $\theta>0$ and let $\Phi$ be holomorphic on the closed strip
> $|\mathrm{Re}\,s-\tfrac12|\le\theta'$ for some $\theta'>\theta$, with
> $$\int_{\mathbb R}\bigl|\Phi(\sigma+it)\bigr|\,(1+|t|)^N\,dt<\infty
> \qquad\text{for every }N\ge0\text{ and every }|\sigma-\tfrac12|\le\theta'.$$
> Then $F(x):=\frac1{2\pi}\int_{\mathbb R}\Phi(\tfrac12+it)e^{-itx}\,dt$ lies in
> $\mathcal S_\theta$, and $f(u):=u^{-1/2}F(\log u)$ lies in $\mathcal D_\theta$
> with $\widehat f=\Phi$.

**Proof.** Put $\Psi(w)=\Phi(\tfrac12+w)$, so
$F(x)=\frac1{2\pi i}\int_{\mathrm{Re}\,w=0}\Psi(w)e^{-wx}\,dw$. The
integrand is holomorphic and integrable on every vertical line in
$|\mathrm{Re}\,w|\le\theta'$, so the contour may be shifted to
$\mathrm{Re}\,w=a$ with $|a|\le\theta$, giving
$$|F(x)|\le e^{-ax}\cdot\frac1{2\pi}\int_{\mathbb R}|\Psi(a+it)|\,dt .$$
Choosing $a=\theta\mathrm{sgn}(x)$ yields $|F(x)|\le C\,e^{-\theta|x|}$.
For the polynomial factor, integrate by parts $N$ times on the shifted line:
$x^NF(x)=\frac{1}{2\pi i}\int_{\mathrm{Re}\,w=a}\Psi^{(N)}(w)e^{-wx}\,dw$,
and $\Psi^{(N)}$ is bounded on that line by Cauchy's estimate from the strip
$|\mathrm{Re}\,w|\le\theta'$ together with the hypothesis at
$\sigma=\tfrac12\pm\theta'$. Hence $|x^NF(x)|\le C_Ne^{-\theta|x|}$ for every
$N$, which is $\mathcal S_\theta$. Mellin inversion (113_06 Lemma 1.2) gives
$\widehat f=\Phi$. $\square$

> ### Lemma 1.2 (the ξ-factor supplies the hypothesis for every θ)
> Let $p$ be a polynomial and $v$ holomorphic and polynomially bounded on
> $|\mathrm{Re}\,s-\tfrac12|\le\theta'$. Then $\Phi=p\cdot\xi\cdot v$
> satisfies the hypothesis of Lemma 1.1 for that $\theta'$. Consequently
> $p\,\xi\,v$ is $\widehat f$ for some $f\in\mathcal D_\theta$, for **every**
> $\theta>0$; in particular such $f$ lie in $\mathcal D$.

**Proof.** $\xi$ is entire, so $\Phi$ is holomorphic on the strip. On any
vertical line $\mathrm{Re}\,s=\sigma$ in a bounded strip, Stirling gives
$$|\xi(\sigma+it)|=\tfrac12|s(s-1)|\,\pi^{-\sigma/2}\,|\Gamma(\tfrac{s}2)|\,|\zeta(s)|
=O\bigl(|t|^{A(\sigma)}e^{-\pi|t|/4}\bigr),$$
using $|\Gamma(\tfrac{\sigma+it}2)|\sim c|t|^{(\sigma-1)/2}e^{-\pi|t|/4}$ and the
polynomial bound for $\zeta$ in a vertical strip. The exponential factor
defeats every polynomial, so all the integrals converge. $\square$

Lemma 1.2 is the engine of this file, and it is worth naming what it says:
**multiplying by $\xi$ pushes a function into $\mathcal D_\theta$ for every
$\theta$ at once.** The completed zeta function is not merely a bookkeeping
device here; its $e^{-\pi|t|/4}$ decay is what makes the ξ-ideal live inside the
Schwartz class the pairing is defined on. Note also that the source rule permits
this: ξ itself may be used; only a *zero* of ξ may not.

---

## 2. The radical

> ### Definition 2.1
> $\mathrm{rad}\,I_\partial:=\{f\in\mathcal D:\ I_\partial(f,g)=0\ \text{for all }g\in\mathcal D\}$.

Write $\mathcal Z$ for the multiset of zeros of $\xi$ (equivalently the
nontrivial zeros of $\zeta$), with multiplicities $m_\rho$; recall $\xi$ is
entire and its zeros are exactly $\mathcal Z$, all inside $0<\mathrm{Re}\,s<1$,
hence all inside every strip $|\mathrm{Re}\,s-\tfrac12|<\theta$ with
$\theta>\tfrac12$.

> ### Theorem 2.2 (the radical, computed)
> $$\mathrm{rad}\,I_\partial
> =\Bigl\{f\in\mathcal D:\ \widehat f(0)=\widehat f(1)=0\ \text{ and }\
> \mathrm{ord}_\rho\widehat f\ge m_\rho\ \ \forall\rho\in\mathcal Z\Bigr\}
> =\Bigl\{f\in\mathcal D:\ \tfrac{\widehat f(s)}{s(s-1)\xi(s)}\ \text{is holomorphic on the strip}\Bigr\}.$$

**Proof.** The second equality is immediate: $s(s-1)\xi(s)$ is holomorphic on the
strip with zero divisor exactly $\{0\}+\{1\}+\sum_\rho m_\rho[\rho]$ there.

($\supseteq$) If $\widehat f$ vanishes at $0$, at $1$, and to order $m_\rho$ at
each $\rho$, then every term of
$I_\partial(f,g)=\widehat f(0)\overline{\widehat g(1)}+\widehat f(1)\overline{\widehat g(0)}-\sum_\rho m_\rho\widehat f(\rho)\overline{\widehat g(\rho')}$
vanishes.

($\subseteq$) We must separate the coordinates by elements of $\mathcal D$.

*Polar slots.* By Theorem 3.1 below, $f_h$ with $\widehat f_h(s)=2s\,\xi(s)$ lies
in $\mathcal D$ and has $\widehat f_h(0)=0$, $\widehat f_h(1)=2\xi(1)=1$,
$\widehat f_h(\rho)=0$. Then $I_\partial(f,f_h)=\widehat f(0)$, so $f\in\mathrm{rad}$
forces $\widehat f(0)=0$. Symmetrically $f_v$ with $\widehat f_v(s)=-2(s-1)\xi(s)$
gives $I_\partial(f,f_v)=\widehat f(1)=0$.

*Zero slots.* Fix $\rho_0\in\mathcal Z$ and set
$$\widehat g_{\rho_0}(s):=\frac{s(s-1)\,\xi(s)}{(s-\rho_0)^{m_{\rho_0}}}.$$
This is holomorphic on the strip (the pole is cancelled by the zero of $\xi$ of
order exactly $m_{\rho_0}$) and is $\xi$ times a function that is polynomially
bounded there, so by Lemma 1.2 it is $\widehat g$ for some $g\in\mathcal D$. Its
coordinates are $\widehat g(0)=\widehat g(1)=0$, $\widehat g(\rho)=0$ for
$\rho\ne\rho_0$, and
$\widehat g(\rho_0)=\rho_0(\rho_0-1)\,\xi^{(m_{\rho_0})}(\rho_0)/m_{\rho_0}!\ne0$.
Applying this at $\rho_0=\rho'$ gives
$I_\partial(f,g_{\rho'})=-m_\rho\widehat f(\rho)\overline{\widehat g_{\rho'}(\rho')}$,
so $f\in\mathrm{rad}$ forces $\widehat f(\rho)=0$. Iterating with
$\widehat g(s)=s(s-1)\xi(s)(s-\rho')^{j-m_{\rho'}}$ for $j<m_{\rho'}$ — or simply
observing that the argument applies verbatim to $\widehat f$ replaced by
$\widehat f/(s-\rho)^{k}$ — upgrades this to order $m_\rho$. $\square$

> ### Remark 2.3 (on the source rule)
> The functions $g_{\rho_0}$ in the second half of the proof mention a zero of
> $\xi$. They are auxiliary test functions inside a proof that two
> *already-defined* sets are equal; nothing in the programme is defined by them
> and nothing downstream depends on them. Crucially the argument uses only the
> **existence** of the zeros of the entire function $\xi$ and the order of
> vanishing there — it never locates a zero, never assumes anything about
> $\mathrm{Re}\,\rho$, and would read identically if RH were false. The
> inclusion ($\supseteq$), which is the direction all later files use, mentions
> no zero at all. Reviewers who wish to hold the rule at its strictest may read
> Theorem 2.2 as the inclusion ($\supseteq$) plus the polar half of
> ($\subseteq$), both of which are zero-free, and treat the zero-slot half as
> conditional; nothing else in this file or in 113_10–113_14 changes.

> ### Theorem 2.4 (structure)
> 1. $\mathrm{rad}\,I_\partial$ is a $*$-ideal of the commutative $*$-algebra $\mathcal D$.
> 2. It is nonzero: $\widehat w(s)=s(s-1)\xi(s)$ defines $w\in\mathrm{rad}\,I_\partial\setminus\{0\}$.
> 3. $I_\partial$ descends to a nondegenerate Hermitian form on $\mathcal D/\mathrm{rad}\,I_\partial$.

**Proof.** (1) $\mathcal D$ is a convolution algebra and Mellin transforms
multiply: $\widehat{f\star g}=\widehat f\,\widehat g$ (113_07 Lemma 1.4). So the
vanishing conditions of Theorem 2.2 are preserved under multiplication by any
$\widehat g$ — an ideal. For $*$-closure, $\widetilde f$ has
$\widehat{\widetilde f}(s)=\overline{\widehat f(1-\bar s)}$ (113_05 Lemma 2.3);
and the generator is invariant,
$$\overline{(1-\bar s)\bigl((1-\bar s)-1\bigr)\xi(1-\bar s)}
=(1-s)(-s)\,\xi(s)=s(s-1)\,\xi(s),$$
using $\xi(1-s)=\xi(s)$ and $\overline{\xi(\bar s)}=\xi(s)$. Also
$\rho\mapsto\rho'=1-\bar\rho$ permutes $\mathcal Z$ preserving multiplicities, and
swaps $0\leftrightarrow1$. (2) By Lemma 1.2, $w\in\mathcal D$; it is nonzero
because $\widehat w(\tfrac12)=-\tfrac14\xi(\tfrac12)=-0.124280\ldots\ne0$; and it
lies in the radical by Theorem 2.2. (3) Immediate from the definition of the
radical. $\square$

Part (2) is worth pausing on. The radical is not a degenerate accident: it is a
large, natural ideal — every $f$ whose Mellin transform is divisible by
$s(s-1)\xi(s)$ — and the quotient $\mathcal D/\mathrm{rad}$ is precisely the
coordinate space in which 107_241 and 113_08 work. **This is what d1 was for**:
a canonical "linear equivalence" under which the intersection pairing becomes
nondegenerate. It exists, it is explicit, and it required no geometry.

---

## 3. The rulings are realised in 𝒟

> ### Theorem 3.1 (closes 113_08 Remark 2.3)
> Define $f_v,f_h\in\mathcal D$ by
> $$\widehat f_v(s):=-2(s-1)\,\xi(s),\qquad \widehat f_h(s):=2s\,\xi(s).$$
> These lie in $\mathcal D_\theta$ for every $\theta>0$, and their coordinates are
> $$\widehat f_v(0)=1,\ \widehat f_v(1)=0,\ \widehat f_v(\rho)=0;\qquad
> \widehat f_h(0)=0,\ \widehat f_h(1)=1,\ \widehat f_h(\rho)=0 .$$
> Hence $f_v,f_h$ represent $F_v,F_h$ of 113_08 Definition 2.1, and
> $$\widehat{(f_v+f_h)}(s)=2\xi(s)$$
> represents the polarization $H$.

**Proof.** Membership is Lemma 1.2 with $p$ linear and $v\equiv1$. For the
coordinates, $\xi(0)=\xi(1)=\tfrac12$ (the poles of $\Gamma(s/2)$ at $s=0$ and of
$\zeta$ at $s=1$ are simple and are cancelled by the factor $\tfrac12s(s-1)$),
so $\widehat f_v(0)=-2(-1)\tfrac12=1$ and $\widehat f_v(1)=0$; symmetrically for
$f_h$. Both vanish on $\mathcal Z$ because $\xi$ does. Finally
$-2(s-1)\xi(s)+2s\xi(s)=2\xi(s)\bigl(s-(s-1)\bigr)=2\xi(s)$. $\square$

> ### Corollary 3.2 (splitting)
> $\mathcal D=\mathcal D^\circ\oplus\mathbb Cf_v\oplus\mathbb Cf_h$, where
> $\mathcal D^\circ=\{f:\widehat f(0)=\widehat f(1)=0\}$. The projection is
> $$\pi(f)=f-\widehat f(0)\,f_v-\widehat f(1)\,f_h .$$

**Proof.** $\widehat{\pi(f)}(0)=\widehat f(0)-\widehat f(0)\cdot1-\widehat f(1)\cdot0=0$
and likewise at $1$; $f_v,f_h$ are linearly independent (their polar coordinates
are $(1,0)$ and $(0,1)$) and meet $\mathcal D^\circ$ only in $0$. $\square$

> ### Corollary 3.3 (Connes' Lemma 2.1 now applies on the nose)
> Take $E=\mathcal D$, $\xi_0=f_v$, $\xi_1=f_h$ in 113_08 Lemma 3.1. Hypothesis (1)
> holds by Theorem 3.1 plus 113_08 Proposition 2.2, and the projection
> $y=x-\widehat x(0)f_v-\widehat x(1)f_h$ of its proof stays inside $\mathcal D$
> by Corollary 3.2. Hence the conclusion
> $$Q(f)\ \le\ 2\mathrm{Re}\,\bigl[\widehat f(0)\overline{\widehat f(1)}\bigr]
> \qquad\text{for all }f\in\mathcal D$$
> is *equivalent* to Weil positivity on $\mathcal D^\circ$, with no gap.

113_08 Theorem 3.3 established this equivalence in the coordinate space $V$; the
only thing missing there was that $f_v,f_h$ might not be realised by actual
Schwartz data. They are.

> ### Remark 3.4 (what is still not free)
> Corollary 3.3 removes a technical gap; it does not move the mathematics. By
> 113_08 Theorem 3.3 the inequality *is* Weil positivity. The content of d1 is
> structural — the pairing is now a nondegenerate form on an candid quotient of
> an candid algebra, with an explicit hyperbolic plane split off — and that is
> the setting rows d3–d5 need, not a substitute for them.

---

## 4. The intersection numbers, as facts about primes

This is the part with independent evidential weight. For $f,g\in\mathcal D$ put
$h=f\star\widetilde g$; then $\widehat h(s)=\widehat f(s)\overline{\widehat g(1-\bar s)}$
(113_05 Theorem 3.1), the spectral side of the Weil identity is
$I_\partial(f,g)=\widehat h(0)+\widehat h(1)-\sum_\rho m_\rho\widehat h(\rho)$, and by
113_06 Theorem 2.2 it equals the arithmetic side
$$P(h)-A(h),\qquad
P(h)=\sum_n\Lambda(n)\Bigl[h(n)+\tfrac{h(1/n)}n\Bigr],\quad
A(h)=\frac1{2\pi}\int_{\mathbb R}\Bigl[\tfrac12\mathrm{Re}\,\psi(\tfrac14+\tfrac{it}2)-\tfrac12\log\pi\Bigr]G(t)\,dt$$
with $G(t)=\widehat h(\tfrac12+it)+\widehat h(\tfrac12-it)$.

Two simplifications make this computable in closed form. First, everything is
driven by the single real even function $G$: writing $L=\log n$,
$$P(h)=\sum_n\frac{\Lambda(n)}{\sqrt n}\,\bigl[\mathcal G(L)+\mathcal G(-L)\bigr]
=\sum_n\frac{\Lambda(n)}{\sqrt n}\cdot\frac1\pi\int_0^\infty G(t)\cos(tL)\,dt,$$
where $\mathcal G$ is the balanced profile of $h$. Second, on the critical line
$\xi(\tfrac12+it)=\Xi(t)$ is **real**, and $s(s-1)=-(\tfrac14+t^2)$, so every $G$
below is an elementary polynomial in $t$ times $\Xi(t)^2$.

Now take $f,g$ among $f_v,f_h,w$. Because $\xi$ kills every zero coordinate, the
spectral side collapses to $\widehat h(0)+\widehat h(1)$, an explicit small
integer:

| $f\star\widetilde g$ | $\widehat h(s)$ | $G(t)$ | spectral side | meaning |
|---|---|---|---|---|
| $w\star\widetilde w$ | $\bigl[s(s-1)\xi(s)\bigr]^2$ | $2(\tfrac14+t^2)^2\Xi(t)^2$ | $0$ | the radical pairs to zero |
| $f_v\star\widetilde f_v$ | $-4s(s-1)\xi(s)^2$ | $8(\tfrac14+t^2)\Xi(t)^2$ | $0$ | $F_v^2=0$ |
| $f_h\star\widetilde f_h$ | $-4s(s-1)\xi(s)^2$ | $8(\tfrac14+t^2)\Xi(t)^2$ | $0$ | $F_h^2=0$ |
| $f_v\star\widetilde f_h$ | $4(s-1)^2\xi(s)^2$ | $8(\tfrac14-t^2)\Xi(t)^2$ | $1$ | $F_v\!\cdot\!F_h=1$ |
| $(f_v{+}f_h)^{\star2}$ | $4\xi(s)^2$ | $8\,\Xi(t)^2$ | $2$ | $H^2=2$ |
| $(f_v{-}f_h)^{\star2}$ | $-4(2s-1)^2\xi(s)^2$ | $32\,t^2\,\Xi(t)^2$ | $-2$ | $(F_v{-}F_h)^2=-2$ |
| $\xi\star\widetilde\xi$ **(control)** | $\xi(s)^2$ | $2\,\Xi(t)^2$ | $\tfrac12$ | **not** in the radical |

The last row is the control that makes the rest mean something: $\xi$ alone,
without the factor $s(s-1)$, is *not* in the radical — its polar coordinates are
$\xi(0)=\xi(1)=\tfrac12$, not $0$ — and the arithmetic side duly returns
$\tfrac12$ rather than $0$. So the $s(s-1)$ in the generator is load-bearing,
and the machinery is not simply returning zero for everything ξ-divisible.

Note also that $f_v$ and $f_h$ produce the *same* $G$, hence the same arithmetic
side; that is forced, since $\widetilde{f_v}=f_h$ (verified: the involution
$s\mapsto1-\bar s$ swaps the two rulings), and it is a consistency check rather
than an independent one.

> ### Theorem 4.1 (verified)
> For each row of the table, the arithmetic side $P(h)-A(h)$ — a sum over prime
> powers plus an integral of the digamma kernel, **in which no zero of $\xi$
> occurs** — equals the stated integer.

Measured (2328 prime powers up to $2\times10^4$; $t$-grid of 4000 Gauss–Legendre
nodes on $[0,70]$; $\Xi$ from mpmath at 25 digits):

| probe | $P(h)$ | $A(h)$ | $P-A$ | predicted | error | tail $n>1000$ |
|---|---|---|---|---|---|---|
| $w$ (radical) | $-1.699004497$ | $-1.699004497$ | $0.000000000$ | $0$ | $1.3\times10^{-11}$ | $2.6\times10^{-10}$ |
| $f_v$ | $-4.788652386$ | $-4.788652386$ | $0.000000000$ | $0$ | $7.4\times10^{-11}$ | $7.4\times10^{-11}$ |
| $f_h$ | $-4.788652386$ | $-4.788652386$ | $0.000000000$ | $0$ | $7.4\times10^{-11}$ | $7.4\times10^{-11}$ |
| $f_v\star\widetilde f_h$ | $\ \ 4.836741225$ | $\ \ 3.836741225$ | $1.000000000$ | $1$ | $1.0\times10^{-10}$ | $1.0\times10^{-10}$ |
| $H=f_v{+}f_h$ | $\ \ 0.096177678$ | $-1.903822322$ | $2.000000000$ | $2$ | $3.6\times10^{-10}$ | $2.8\times10^{-10}$ |
| $f_v{-}f_h$ | $-19.250787221$ | $-17.250787221$ | $-2.000000000$ | $-2$ | $6.1\times10^{-11}$ | $2.3\times10^{-10}$ |
| $\xi$ alone (control) | $\ \ 0.024044420$ | $-0.475955581$ | $0.500000000$ | $\tfrac12$ | $8.9\times10^{-11}$ | $7.1\times10^{-11}$ |

> ### Why this is more than a consistency check
> The programme has carried "$H=F_v+F_h$, $H^2=2$" since the backward map was
> written, as a statement inside a formal intersection-theory model. Here the
> same number is produced by von Mangoldt's function and the digamma kernel,
> with the model's own machinery switched off. $P$ and $A$ are individually
> irrational, probe-dependent, and of size up to $19$; their difference is
> $0,0,1,2,-2$ to ten decimal places. Nothing in the computation knows about
> rulings, divisors, or intersection numbers — and it reproduces them.
>
> It also gives a second, independent confirmation of 113_06 Theorem 2.2 on data
> of a completely different kind from the Gaussians of 113_07–113_08: these
> probes are $\xi$-divisible, doubly-exponentially concentrated near $u=1$, and
> have $h(1)\ne0$.

---

## 5. What d1 asked for, and what is delivered

**Delivered.**
- The radical is computed exactly (Theorem 2.2) and is a nonzero $*$-ideal
  (Theorem 2.4), so the pairing descends nondegenerately.
- A canonical generator, $s(s-1)\xi(s)$: the "principal" ideal is
  *ξ-divisibility with vanishing polar part*.
- The rulings are candid elements of $\mathcal D$ (Theorem 3.1), the splitting
  $\mathcal D=\mathcal D^\circ\oplus\mathbb Cf_v\oplus\mathbb Cf_h$ holds
  (Corollary 3.2), and Connes' Lemma 2.1 applies without a gap (Corollary 3.3).
- The intersection numbers are arithmetic facts (Theorem 4.1).

**Not delivered — and this is the candid residue of d1.** The programme wanted
$\mathcal P$ to be the group of *principal divisors of an independently
constructed geometric object* (rows a and b), and then to prove
$\mathcal P\subseteq\mathrm{rad}\,I_\partial$ as a theorem linking the two
sides. What is proved here is the analytic half only: the radical is the
ξ-ideal. Whether any geometry over $\mathrm{Spec}\,\mathbb Z$ has a principal
divisor group mapping onto it is untouched. In particular:

- $\mathcal P$ is still not defined anywhere in the corpus. It should now be
  *defined* as the ξ-ideal, and the burden moved to rows a/b: exhibit a space
  whose principal divisors are these.
- 108_38 Theorem 3.1 (invariance of $\mathrm{Prin}'$ is **false**) and
  108_50/52/53 (no comparison map at generator level) remain in force. They
  refute the groupoid-side candidate for $\mathcal P$; they say nothing about
  the ξ-ideal, which is built analytically and never passes through those
  generators. The two are simply not yet connected, and pretending otherwise
  would be the error this file is written to avoid.
- Nothing here supplies a degree map. $\mathrm{rad}$ is defined by
  vanishing, not by mass; $\deg$ and the balanced subgroup are 113_10.

---

## 6. Scope

**Proved here.** Lemma 1.1 (membership criterion). Lemma 1.2 (the ξ-factor
supplies it for every $\theta$). Theorem 2.2 (the radical, computed) — with the
caveat of Remark 2.3 about the zero-slot half. Theorem 2.4 (nonzero $*$-ideal;
descent). Theorem 3.1 (the rulings realised; $\widehat{f_v+f_h}=2\xi$).
Corollaries 3.2, 3.3. The closed-form table of §4 (the identities
$\widehat h=\widehat f\,\overline{\widehat g(1-\bar\cdot)}$ evaluated on
ξ-divisible data, and the reduction of $P(h)$ to a single even real $G$).

**Read from source, not re-derived.** $\xi$ entire with zero set exactly the
nontrivial zeros of $\zeta$, all in $0<\mathrm{Re}\,s<1$; $\xi(1-s)=\xi(s)$;
$\overline{\xi(\bar s)}=\xi(s)$; $\xi(0)=\xi(1)=\tfrac12$; Stirling and the
convexity bound for $\zeta$ in a vertical strip (used in Lemma 1.2). 113_05
Lemma 2.3 and Theorem 3.1; 113_06 Theorem 2.2 and Lemma 1.2; 113_07 Lemma 1.4;
113_08 Proposition 2.2 and Lemma 3.1. 108_38 Theorem 3.1 and 108_50/52/53 (cited
as refutations of a different candidate, not used).

**Verified numerically** (79/79 checks, exit 0). $\xi(0)=\xi(1)=0.5$ to 18
digits; $\xi(1-s)=\xi(s)$ and $\overline{\xi(\bar s)}=\xi(s)$ to $10^{-18}$;
$\Xi(t)$ real; $\xi(\tfrac12)=0.497120778188314$; $|\xi(\rho)|<10^{-20}$ at the
first ten computed zeros. Theorem 3.1's coordinate values. Theorem 2.4(1)
$*$-invariance of the generator, and the sharper fact that the involution
**swaps** $f_v\leftrightarrow f_h$. Lemma 1.1: the contour shift to
$\mathrm{Re}\,s=\tfrac12\pm\theta$ is legal for $\theta=2,3,4$ (shifted and
unshifted evaluations agree), the resulting bound $|F(x)|\le Ce^{-\theta|x|}$
holds, and the hypothesis moments $\int|\widehat f_v(\sigma+it)|(1+|t|)^N dt$
are finite for $N=0,4,8$ at $\sigma=\tfrac12\pm4$. Theorem 4.1: all seven
arithmetic-side values, errors $1.3\times10^{-11}$ to $3.6\times10^{-10}$, with
prime-power tails beyond $n=1000$ of order $10^{-10}$ confirming convergence,
and a non-vacuity check that $P$ and $A$ are each far from the answer.
Corollary 3.2 on a probe with both polar coordinates equal to $0.145506437$.

Negative controls: the Gaussian probe of 113_07 is **not** in the radical (zero
sum $0.702117236$ over ten zeros); $\xi$ without the $s(s-1)$ factor is **not**
in the radical (arithmetic side $\tfrac12$, not $0$); and $w\star(\text{Gaussian})$
*is* in the radical and is nonzero ($|{\cdot}|=0.0235$ at $s=\tfrac12+14i$),
confirming the ideal property is not vacuous.

**Not established, and explicitly not claimed.** That $\mathrm{rad}\,I_\partial$
is the principal divisor group of any geometric object. Rows (a), (b), (c). (E)
and (R) of 113_08 §4. Hypothesis (2) of Connes' Lemma 2.1. Weil positivity. A
degree map. **Anything about RH.**

## 7. Verifier

`113_09_the_radical_is_the_xi_ideal.py` — exits 0 with
`VERDICT: ALL CHECKS PASS`. Zeros of $\xi$ are used only to confirm that
$\widehat f_v,\widehat f_h,\widehat w$ do vanish on them (a check, not a
definition) and in the negative controls. The arithmetic side of Theorem 4.1
uses no zeros whatsoever.
