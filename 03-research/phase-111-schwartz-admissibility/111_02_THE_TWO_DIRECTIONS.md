# 111.02 — The identity constraint, and why phase 110's obstruction does not apply here

## 0. Result

Two things are settled here, and the second is the one that matters.

> **Task 2.** The identity-value constraint of phase 108 does **not** carry
> over.  There, finiteness of the *local* Tate integral at $p$ required the
> test function to vanish on the shell containing the group identity
> ($\varphi_0=0$), and a quasi-character never does.  Here the corner trace
> is **renormalized**: its counterterm $-2h(1)\log\Lambda$ is proportional to
> the identity value and exists precisely to absorb that divergence.  A
> non-zero identity value is subtracted, not forbidden.

> **The structural point.**  Phase 110's obstruction and phase 111's
> convergence question concern **orthogonal directions** in the $w$-plane.
> $\xi$ grows super-exponentially along the **real axis** — that is what
> kills compact support — and decays exponentially along the **critical
> line** — that is what makes the zero sum converge.  These are different
> features of the same function and are in no tension.

## 1. The identity constraint does not carry over

Phase 108 (108_17 Thm 2.2, 3.1) proved: for the local integral
$W_p^{(K)}(\varphi)$, the limit is finite **iff** $\varphi_0=0$, the
divergence being exactly $\varphi_0\cdot K$; and $\varphi_0=f_a(1)=1$ for
every quasi-character, since $\chi(1)=1$.

> ### Proposition 1.1
> That argument does not transfer to $\mathfrak T$.

**Proof.**  $W_p^{(K)}$ is an unrenormalized truncation: nothing is
subtracted, so a nonzero coefficient on the divergent term is fatal.
$\mathfrak T(h)=\lim_\Lambda\big(\mathrm{Tr}(\theta(h)R_\Lambda)-2h(1)
\log\Lambda\big)$ carries a counterterm whose coefficient is *exactly* the
identity value.  The two statements are therefore not in conflict: 108_17
identifies the divergence's coefficient, and $\mathfrak T$'s definition
subtracts a term with that same coefficient.  A nonzero identity value is
the *expected* case, not an obstruction. $\square$

**What this does and does not settle.**  It settles that no vanishing is
*forced*.  It does not prove $\mathfrak T(h)$ converges for Schwartz $h$ —
that requires the operator definitions of $\theta$ and $R_\Lambda$, which
live outside this phase's read scope and are recorded as the one unresolved
item in 111_03 §3.

## 2. The two directions

> ### Theorem 2.1 (real axis: super-exponential growth)
> $\log|\xi(\sigma)|=\tfrac\sigma2\log\sigma-C\sigma+o(\sigma)$ as
> $\sigma\to+\infty$, $C=\tfrac{\log2+1+\log\pi}2$.  Hence
> $\log|\xi(\sigma)|/\sigma\to+\infty$: infinite exponential type.

This is phase 110's obstruction (110_02), restated for contrast.  Verified:
$\log|\xi(\sigma)|/\sigma=0.126,\ 0.958,\ 2.046,\ 3.188$ at
$\sigma=10,10^2,10^3,10^4$.

> ### Theorem 2.2 (critical line: exponential decay)
> $\displaystyle\lim_{t\to\infty}\frac{\log|\xi(\tfrac12+it)|}{t}=-\frac\pi4 .$

**Proof.**  $\xi(s)=\frac{s(s-1)}2\pi^{-s/2}\Gamma(s/2)\zeta(s)$.  At
$s=\tfrac12+it$: the polynomial factor contributes $O(\log t)$;
$|\pi^{-s/2}|=\pi^{-1/4}$ is constant; $\log|\zeta(\tfrac12+it)|=O(\log t)$
by the classical convexity bound.  The whole exponential rate comes from
$\Gamma$: by Stirling, $|\Gamma(x+iy)|\sim\sqrt{2\pi}\,|y|^{x-1/2}
e^{-\pi|y|/2}$ as $|y|\to\infty$, and here $s/2=\tfrac14+\tfrac{it}2$, so
$|y|=t/2$ and the rate is $-\tfrac\pi2\cdot\tfrac t2=-\tfrac{\pi t}4$.
Dividing by $t$ and letting $t\to\infty$ kills the $O(\log t)$ terms.
$\square$

Verified: $\log|\xi(\tfrac12+it)|/t=-0.327,\ -0.668,\ -0.730,\ -0.773,\
-0.782$ at $t=10,50,200,10^3,5\times10^3$, converging to
$-\pi/4=-0.785398$.

> ### Corollary 2.3 (no tension)
> Phase 110's impossibility is a statement about growth as $\sigma\to+\infty$
> along $\R$; the convergence of $\sum_\rho\widehat f(\rho)
> \overline{\widehat g(\rho)}$ is a statement about decay as $|t|\to\infty$
> along $\Re w=\tfrac12$.  A single entire function may — and $\xi$ does —
> grow in the first direction and decay in the second.  Nothing in 110_02
> bears on the zero sum.

Both rates are carried by $\Gamma$, not by $\zeta$: $\log\zeta(\sigma)\to0$
on the real axis, and $\log|\zeta(\tfrac12+it)|=O(\log t)$ on the line.

## 3. The $\xi$-divisible probe

Take $g(r)=e^{-(\log r)^2}$, so $\widehat g(w)=\sqrt\pi\,e^{w^2/4}$
(110_02), and set $\widehat f=\xi\cdot\widehat g$.

> ### Proposition 3.1
> $|\widehat f(\tfrac12+it)|$ decays faster than $e^{-t^2/4}$.

**Proof.**  $|\widehat g(\tfrac12+it)|=\sqrt\pi\,e^{(1/4-t^2)/4}$, decaying
like $e^{-t^2/4}$; by Theorem 2.2, $|\xi|$ contributes a further
$e^{-\pi t/4+o(t)}$. $\square$

Verified: $|\widehat f(\tfrac12+it)|=7.1\times10^{-1},\ 9.9\times10^{-13},\
2.2\times10^{-286},\ 8.6\times10^{-4407}$ at $t=1,10,50,200$.  Against the
classical zero density $N(T)\sim(T/2\pi)\log T$, the sum
$\sum_\rho\widehat f(\rho)\overline{\widehat g(\rho)}$ converges absolutely
by an enormous margin.

> ### Proposition 3.2 ($\xi$-divisibility is not by itself membership)
> $\xi(0)=\xi(1)=\tfrac12\ne0$, so $\widehat f=\xi\widehat g$ gives
> $\widehat f(0)=\tfrac12\widehat g(0)$ and $\widehat f(1)=\tfrac12
> \widehat g(1)$, which need not vanish.  Membership in
> $\operatorname{rad}I_\partial$ additionally requires $\widehat g(0)=
> \widehat g(1)=0$.

**Proof.**  Direct, from $\xi(0)=\xi(1)=\tfrac12$ (verified numerically) and
$\operatorname{rad}I_\partial=\{f:\widehat f(0)=\widehat f(1)=0,\
\widehat f(\rho)=0\;\forall\rho\}$ (107_240 Thm D). $\square$

This is an extra linear condition on $g$, cutting a codimension-2 subspace.
It is **not** an obstruction — for the probe above,
$\widehat f(0)=0.886$ and $\widehat f(1)=1.138$, both nonzero, so that
particular $g$ must be corrected; but two linear conditions on an
infinite-dimensional space are freely satisfiable.

## 4. Scope

**Proved here.** Proposition 1.1; Theorem 2.2 (with the classical Stirling
and convexity bounds quoted); Corollary 2.3; Propositions 3.1, 3.2.

**Read from source, not re-derived.** 108_17 Theorems 2.2 and 3.1;
107_240 Theorem D and the definition of $\mathfrak T$; 110_02's growth
theorem and its $\widehat g=\sqrt\pi e^{w^2/4}$ example; Stirling's
asymptotic for $|\Gamma(x+iy)|$; the convexity bound for $\zeta$ on the
critical line; the zero density $N(T)\sim(T/2\pi)\log T$.

**Verified numerically.** Both rates of §2, by refinement in $\sigma$ and in
$t$, against their predicted limits $+\infty$ and $-\pi/4$; the decay of the
probe at four heights; $\xi(0)=\xi(1)=\tfrac12$; that $\log\zeta(\sigma)\to0$.

**Not established, and explicitly not claimed.** Convergence of
$\mathfrak T(h)$ itself on Schwartz data — see §1 and 111_03 §3; that a $g$
satisfying $\widehat g(0)=\widehat g(1)=0$ *together with* every other
admissibility requirement exists (the two conditions are freely satisfiable
in isolation, which is a weaker statement); anything about $\RH$.

`ROW_A_STATUS` unchanged. Nothing here bears on $\RH$.

## 5. Verifier

`111_02_the_two_directions.py` checks both growth rates of §2 by refinement
against their predicted limits (with a control clause rejecting the opposite
sign, so the test discriminates between growth and decay); the probe's decay
at four heights; $\xi(0)=\xi(1)=\tfrac12$ and hence Proposition 3.2's
non-vanishing; that the $\zeta$ factor contributes nothing to either rate;
and, as a control on Corollary 2.3, that a single function really does show
both behaviours — i.e. the two limits have opposite signs for the same $\xi$.
