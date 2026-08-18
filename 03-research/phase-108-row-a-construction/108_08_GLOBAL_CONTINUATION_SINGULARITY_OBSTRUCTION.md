# 108.08 — Analytic continuation of the two global halves: the singularities do not cancel

## 0. What this settles

108_06 Theorem 4.1 proved that the naive prime sum $\sum_p W_p(f_a)$
diverges everywhere on the critical strip, because it splits into two
Dirichlet-type series
\[
 A(a):=\sum_p\frac{p^{-a}}{1-p^{-a}}\ \ (\Re a>1),
 \qquad
 B(a):=\sum_p\frac{p^{a-1}}{1-p^{a-1}}\ \ (\Re a<0),
 \qquad B(a)=A(1-a),
\]
each convergent only in a half-plane disjoint from the strip. This note
asks whether **analytic continuation** (not a cutoff) can repair this, by
continuing $A$ and $B$ past their half-planes and adding them.

The answer is **no, not by this route**: both halves continue (on the real
segment of the strip, by an absolutely convergent series) with genuine
non-removable logarithmic singularities at a countable, boundary‑accumulating
set of points, the two singular sets meet at exactly one point — $a=1/2$,
forced by the $a\leftrightarrow1-a$ symmetry — and there the two divergences
have the **same sign** and **add**, rather than cancelling. This is proved
below, on the real segment $a\in(0,1)$ of the strip.

No zero of $\zeta$ or $\xi$ is used in any definition below. Zeros are
mentioned once, in §9, purely to describe an obstruction to extending the
result off the real axis — exactly the use §0 rule 4 of the phase permits.

## 1. Setup: the two halves as sums of the prime zeta function

Write $P(s)=\sum_p p^{-s}$ ($\Re s>1$) for the prime zeta function. Expanding
the geometric series in $p^{-a}$,
\[
 A(a)=\sum_p\sum_{k\ge1}p^{-ka}=\sum_{k\ge1}P(ka),
\]
which is 108_06 Theorem 4.1's own identification of $A$ with a sum over
prime powers, re-summed by exponent $k$. This is given, not re-derived.

Also given (stated in Phase 108's task description; classical, attributed
to the Euler product of $\zeta$): for $\Re s>1$,
\[
 \log\zeta(s)=\sum_{k\ge1}\frac1k\,P(ks),
 \qquad\text{inverted by Möbius as}\qquad
 P(s)=\sum_{m\ge1}\frac{\mu(m)}{m}\log\zeta(ms).
 \tag{1.1}
\]
The forward identity is immediate from $\log\zeta(s)=-\sum_p\log(1-p^{-s})
=\sum_p\sum_{k\ge1}p^{-ks}/k=\sum_k P(ks)/k$; the Möbius inversion (1.1) is
standard and is used here as given.

## 2. Reformulation: $A(a)$ as a single series indexed by the totient

> ### Proposition 2.1
> For $\Re a>1$,
> \[
>  A(a)=\sum_{N=1}^\infty \frac{\varphi(N)}{N}\,\log\zeta(Na),
> \]
> where $\varphi$ is Euler's totient.

**Proof.** Substituting (1.1) into $A(a)=\sum_{k\ge1}P(ka)$,
\[
 A(a)=\sum_{k\ge1}\sum_{m\ge1}\frac{\mu(m)}{m}\log\zeta(mka).
\]
For $\Re a>1$ every term $mka$ has real part $>1$, where the double series
converges absolutely (each $\log\zeta(mka)=O(2^{-mka})$ by §3 below, and
$\sum_{m,k}|\mu(m)/m|\,2^{-mka}<\infty$), so the terms may be regrouped by
$N=mk$:
\[
 A(a)=\sum_{N=1}^\infty\Big(\sum_{m\mid N}\frac{\mu(m)}{m}\Big)\log\zeta(Na)
 =\sum_{N=1}^\infty\frac{\varphi(N)}{N}\log\zeta(Na),
\]
using the classical identity $\sum_{d\mid N}\mu(d)\,(N/d)=\varphi(N)$
(equivalently $\varphi=\mu*\mathrm{id}$), so
$\sum_{m\mid N}\mu(m)/m=\tfrac1N\sum_{m\mid N}\mu(m)(N/m)=\varphi(N)/N$.
$\square$

## 3. Restriction to the real segment, and why

The rest of this note works with **real** $a\in(0,1)$. The reason is not a
simplification of convenience: it removes every dependence on the location
of zeros of $\zeta$ from the argument, by the following elementary fact.

> ### Lemma 3.1
> $\zeta(s)$ has **no zero on the real axis for $s>0$**: $\zeta(s)>0$ for
> $s>1$, and $\zeta(s)<0$ for $0<s<1$.

**Proof.** For $s>1$ the Euler product $\zeta(s)=\prod_p(1-p^{-s})^{-1}$ has
every factor $>0$, so $\zeta(s)>0$. For $0<s<1$, use
$\zeta(s)(1-2^{1-s})=\eta(s):=\sum_{n\ge1}(-1)^{n-1}n^{-s}$ (Dirichlet eta
function). $\eta(s)>0$ by the alternating series test ($n^{-s}$ decreasing
to $0$). And $1-2^{1-s}<0$ because $1-s\in(0,1)\Rightarrow 2^{1-s}\in(1,2)$.
Hence $\zeta(s)=\eta(s)/(1-2^{1-s})<0$. $\square$

Consequently, for real $a>0$, $\zeta(Na)$ is a nonzero real number for every
positive integer $N$ with $Na\ne1$; $\log\zeta(Na)$ is single-valued once a
branch of $\log$ of a (possibly negative) real number is fixed, and its
**real part**, $\log|\zeta(Na)|$, is branch-independent. Everything proved
below is a statement about $\Re[\log\zeta(Na)]=\log|\zeta(Na)|$, so no
branch choice and no location of a complex zero of $\zeta$ ever enters.

> ### Proposition 3.2 (convergence of the reformulated series)
> For real $a>0$ with $a\ne1/N$ for every $N\ge1$, the series
> $\sum_N(\varphi(N)/N)\log\zeta(Na)$ converges absolutely.

**Proof.** For $w\ge2$, $|\zeta(w)-1|\le\sum_{n\ge2}n^{-w}\le
2^{-w}+\int_2^\infty x^{-w}dx\le C\,2^{-w}$ for an absolute constant $C$, so
$\log\zeta(w)=\log(1+(\zeta(w)-1))=O(2^{-w})$ as $w\to\infty$. Fix $a>0$ with
$a\notin\{1/N\}$. Only finitely many $N$ have $Na<2$; for the rest,
$|\varphi(N)/N\cdot\log\zeta(Na)|=O(2^{-Na})$, summable in $N$ since $a>0$.
$\square$

This is the precise sense in which $A(a):=\sum_N(\varphi(N)/N)\log\zeta(Na)$
is analytically continued past $\Re a>1$: the same series, shown to converge
absolutely on all of $a\in(0,\infty)\setminus\{1/N:N\ge1\}$, not a different
construction. On $\Re a>1$ it agrees with the original $A(a)$ of §1 by
Proposition 2.1.

## 4. The local model of the singularity: the simple pole of $\zeta$

> ### Lemma 4.1
> $\zeta(s)-\dfrac1{s-1}$ extends to a function holomorphic near $s=1$
> (classical; the constant term is the Euler–Mascheroni $\gamma$). Hence, as
> real $w\to1$,
> \[
>  \log|\zeta(w)| = -\log|w-1| + O(1).
> \]

**Proof.** The stated Laurent expansion of $\zeta$ at its unique pole is
classical (e.g. via $\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}dx$,
convergent and holomorphic for $\Re s>0$). Writing $\zeta(w)=\frac1{w-1}+g(w)$
with $g$ continuous near $w=1$, $|\zeta(w)|\cdot|w-1|=|1+(w-1)g(w)|\to1$ as
$w\to1$, i.e. $\log|\zeta(w)|+\log|w-1|\to0$. $\square$

This lemma is used only through $\Re[\log\zeta]=\log|\zeta|$; no zero of
$\zeta$ appears anywhere in its statement or proof.

## 5. The singularities of $A(a)$: one at every $a=1/N$, $N\ge2$

> ### Theorem 5.1
> Fix an integer $N_0\ge2$. As real $a\to1/N_0$ (from either side, within
> $(0,1)$),
> \[
>  \Re[A(a)] = -\frac{\varphi(N_0)}{N_0}\log|N_0a-1| + R_{N_0}(a),
> \]
> where $R_{N_0}$ is continuous (in particular bounded) on a punctured
> neighbourhood of $a=1/N_0$. Consequently $\Re[A(a)]\to+\infty$ as
> $a\to1/N_0$: this is a genuine, non-removable singularity.

**Proof.** For $N\ne N_0$, $Na=1$ at $a=1/N_0$ would force $N/N_0=1$, i.e.
$N=N_0$; so among the countably many points $\{1/N:N\ge1\}$, $a=1/N_0$ is
isolated from all $1/N$ with $N\ne N_0$. Choose a punctured neighbourhood
$U$ of $1/N_0$ containing no other such point. On $U$, split
$\Re[A(a)]=\frac{\varphi(N_0)}{N_0}\log|\zeta(N_0a)|+\sum_{N\ne N_0}
\frac{\varphi(N)}{N}\log|\zeta(Na)|$. The first term is
$-\frac{\varphi(N_0)}{N_0}\log|N_0a-1|+O(1)$ by Lemma 4.1. The remaining
series converges uniformly on a smaller neighbourhood of $1/N_0$ (each term
is continuous there, by Lemma 3.1 avoiding a further zero at $Na$ for
$N\ne N_0$ in that neighbourhood, and the tail is dominated exactly as in
Proposition 3.2, uniformly for $a$ in a bounded set), hence defines a
continuous function $R_{N_0}$ there. $\square$

By symmetry $B(a)=A(1-a)$:

> ### Corollary 5.2
> For every integer $M_0\ge2$, as real $a\to1-1/M_0$,
> \[
>  \Re[B(a)] = -\frac{\varphi(M_0)}{M_0}\log|M_0(1-a)-1| + R'_{M_0}(a),
>  \qquad R'_{M_0}\text{ continuous near }1-1/M_0 .
> \]

## 6. The two singular sets meet at exactly one point

> ### Lemma 6.1
> The only solution in integers $N,M\ge2$ of $\dfrac1N=1-\dfrac1M$ is
> $N=M=2$.

**Proof.** The equation is $\frac1N+\frac1M=1$. WLOG $N\le M$; then
$\frac1N\ge\frac12$, so $N\le2$, forcing $N=2$ (as $N\ge2$). Then
$\frac1M=\frac12$, so $M=2$. $\square$

So the singular set of $A$, $\Sigma_A=\{1/N:N\ge2\}$, and the singular set
of $B$, $\Sigma_B=\{1-1/M:M\ge2\}$, satisfy $\Sigma_A\cap\Sigma_B=\{1/2\}$
— and this is forced structurally, by the $a\leftrightarrow1-a$ symmetry
exchanging $\Sigma_A$ and $\Sigma_B$ and by $1/2$ being that involution's
unique fixed point among these rational sequences.

## 7. The decisive computation: reinforcement, not cancellation

> ### Theorem 7.1
> As real $a\to1/2$ (from either side),
> \[
>  \Re[A(a)+B(a)] = -\log|2a-1| + O(1) \;\longrightarrow\; +\infty .
> \]
> The two singularities do **not** cancel at $a=1/2$: they have the same
> sign and add, so the divergence at the one point common to $\Sigma_A$ and
> $\Sigma_B$ is *twice* as strong as either alone.

**Proof.** Apply Theorem 5.1 with $N_0=2$ ($\varphi(2)/2=1/2$):
$\Re[A(a)]=-\frac12\log|2a-1|+R_2(a)$. Apply Corollary 5.2 with $M_0=2$:
$\Re[B(a)]=-\frac12\log|2(1-a)-1|+R'_2(a)=-\frac12\log|1-2a|+R'_2(a)
=-\frac12\log|2a-1|+R'_2(a)$. Adding,
$\Re[A(a)+B(a)]=-\log|2a-1|+(R_2(a)+R'_2(a))$, and $R_2+R'_2$ is bounded
near $a=1/2$ by Theorem 5.1/Corollary 5.2. $\square$

> ### Corollary 7.2 (persistence everywhere else)
> At every $a=1/N_0\in\Sigma_A$ with $N_0\ge3$, $B$ is regular
> (Lemma 6.1: $1/N_0\notin\Sigma_B$), so $A+B$ inherits $A$'s full,
> unmoderated singularity there. Symmetrically at every
> $a=1-1/M_0\in\Sigma_B$, $M_0\ge3$.

**Proof.** Immediate from Theorem 5.1/Corollary 5.2 and Lemma 6.1: at such
a point exactly one of the two summands is singular, the other contributes
its bounded remainder term. $\square$

## 8. The global obstruction, stated precisely

> ### Theorem 8.1
> $A(a)+B(a)$, continued to $a\in(0,1)$ by the absolutely convergent series
> of Proposition 2.1/3.2, has a non-removable logarithmic singularity at
> **every** point of
> \[
>  \Sigma=\Sigma_A\cup\Sigma_B=\{1/N:N\ge2\}\cup\{1-1/M:M\ge2\}\subset(0,1),
> \]
> a countably infinite set accumulating at **both** endpoints $a=0$ and
> $a=1$ of the strip. At the single point $\Sigma_A\cap\Sigma_B=\{1/2\}$
> the two contributions reinforce (Theorem 7.1); everywhere else on
> $\Sigma$ the singularity is inherited from one half alone unmoderated
> (Corollary 7.2). In particular $A(a)+B(a)$ is not continuous, let alone
> holomorphic, on any subinterval of $(0,1)$ that meets $\Sigma$
> arbitrarily close to either endpoint.

**Proof.** Immediate from Theorem 5.1, Corollary 5.2, Theorem 7.1 and
Corollary 7.2; the accumulation at $0$ and at $1$ is clear since
$1/N\to0$ and $1-1/M\to1$. $\square$

This is the precise, real-axis answer to the "decisive question": the
naive analytic-continuation route to a global Stage 1 object **fails**, not
by an accident that might be patched with a different regularization
constant, but structurally — the source of the failure is the same simple
pole of $\zeta$ (Lemma 4.1) recurring at every rational reciprocal $1/N$,
and the one place symmetry could have produced a cancellation, it produces
reinforcement instead.

## 9. What a fix would have to supply

This section records, explicitly labelled as **not established here**,
what would be needed to go further; none of it is claimed.

1. **A distributional reading.** Logarithmic singularities, unlike poles,
   are *locally integrable* in one real dimension. It is conceivable — this
   is a remark, not a theorem — that $A(a)+B(a)$ makes sense as a locally
   integrable function of $a$ (hence a distribution), even though it is not
   continuous. This would be consistent with 108_05 Corollary 4.1, which
   independently found that the correct target for this whole construction
   is measure-valued in $a$, not number-valued. Turning this remark into a
   result would require constructing the distribution explicitly and
   checking it against the covariance-form pairing of 108_05 — not
   attempted here.
2. **The constants $C_p$.** 108_06 left the Tate principal values $C_p$
   (the $a$-independent part of $W_p(f_a)$) unevaluated and their sum over
   $p$ unaddressed. Whether $\sum_p C_p$ interacts with $A+B$ is untouched
   here, exactly as it was untouched in 108_06.
3. **Extension off the real axis.** For complex $a$, each term
   $\log\zeta(Na)$ in Proposition 2.1's series has, in addition to the pole
   singularity at $Na=1$ analyzed above, potential branch points at
   $Na=\rho$ for every nontrivial zero $\rho$ of $\zeta$. Whether these
   coincide, cancel, or genuinely obstruct a continuation off the real
   segment is **not analyzed here** — Lemma 3.1's route (no real zeros)
   is exactly what let the real-axis argument avoid this question, and nothing
   above resolves it for complex $a$. Settling it would require input on
   the location of $\zeta$'s zeros, which by the rules of this phase cannot
   be used in a *definition*, only (as done in this sentence) to *describe*
   the obstruction.

## 10. Scope

Proved (real $a\in(0,1)$ only):

* Proposition 2.1: $A(a)=\sum_N(\varphi(N)/N)\log\zeta(Na)$ on $\Re a>1$;
* Lemma 3.1: $\zeta$ has no real zero on $(0,\infty)$;
* Proposition 3.2: the reformulated series converges absolutely on
  $a\in(0,\infty)\setminus\{1/N\}$, giving the continuation used throughout;
* Lemma 4.1: the local log-pole behaviour of $\zeta$ at $s=1$;
* Theorem 5.1 / Corollary 5.2: the exact singularity of $A$ at every
  $1/N$ ($N\ge2$) and of $B$ at every $1-1/M$ ($M\ge2$);
* Lemma 6.1: the two singular sets meet at exactly $a=1/2$;
* Theorem 7.1: at $a=1/2$ the two singularities **reinforce**, they do
  **not** cancel;
* Corollary 7.2: at every other point of $\Sigma$, the singularity is
  inherited unmoderated from one half;
* Theorem 8.1: the precise global obstruction — a boundary-accumulating
  countable singular set, on which $A+B$ is not continuous.

Verified numerically: the reformulation of Proposition 2.1 against the
direct prime sum for $a=1.5$; the pole law of Lemma 4.1; the sign pattern
of Lemma 3.1; the reinforcement law $\Re[A(a)+B(a)]\approx-\log|2a-1|$ of
Theorem 7.1 by a fit of the growth rate against shrinking $|a-1/2|$; the
contrasting boundedness of $B$ near $a=1/3\in\Sigma_A\setminus\Sigma_B$.

Read from source, not re-derived: the Möbius inversion (1.1) attributed to
the Euler product / prime zeta function relation, and the classical Laurent
expansion of $\zeta$ at $s=1$ (Lemma 4.1), both standard analytic number
theory.

Not established, and explicitly not claimed:

* anything about complex $a$ (§9.3): the singularity structure there is
  open, and it is exactly where zeros of $\zeta$ would enter if anyone
  pursued it;
* any distributional/measure-valued repair (§9.1) — a remark, not a result;
* any treatment of $C_p$ (§9.2);
* that no other regularization route (cutoff, zeta-regularization of the
  outer sum, etc.) could succeed — only the specific route of analytically
  continuing each half and adding is addressed, as the task specified;
* any change to `ROW_A_STATUS`, which remains `partial`;
* nothing here suggests, and nothing should be read as suggesting, that RH
  follows from anything above.

## 11. Verifier

`108_08_global_continuation_singularity.py` implements $\zeta$ on the reals
(away from $s=1$) via Euler–Maclaurin summation, plain Python + numpy only
(no scipy, no mpmath), and checks: the implementation itself against the
known values $\zeta(2)=\pi^2/6$, $\zeta(4)=\pi^4/90$; Lemma 3.1's sign
pattern; Proposition 2.1's reformulation against the direct prime sum at
$a=1.5$; Lemma 4.1's pole law $|\zeta(w)|\,|w-1|\to1$ from both sides;
Theorem 7.1's reinforcement law, by fitting the growth rate of
$\Re[A(a)+B(a)]$ as $a\to1/2$ against the predicted coefficient $-1$ (as
opposed to a cancellation, which would predict a bounded limit); and
Corollary 7.2's contrast, that $B(a)$ stays bounded as $a\to1/3\in\Sigma_A$.
