# 109.02 — The radical of the one-sided pairing: computed, not guessed

## 0. Pre-registration (written before the computation, per the mission's
## anti-circularity requirement — see 109_00 §3 for the full statement)

Restated here in compressed form, exactly as it must be read against what
follows:

* **Confirms the hypothesis** only if $\mathrm{rad}\,B=\{f:\hat f(0)=0,\
  \hat f(1)=0,\ \hat f(\rho)=0\ \forall\text{ zeros }\rho\text{ of }\xi\}$,
  proved from $B$'s actual definition, without invoking the archimedean
  completion (Stage 4, not built for row (a); 108_36 §3 says so explicitly).
* **Refutes it** if an explicit nonzero $f\in\mathrm{rad}\,B$ is exhibited
  whose (continued) Mellin transform does not vanish at zeros of $\xi$ —
  or if $\mathrm{rad}\,B$ has a clean description with no reference to
  $\zeta$'s zeros at all.
* Anything in between (neither confirmed nor cleanly refuted) is reported
  as its own outcome, and Step 3 is skipped.

## 1. Setup

Work throughout inside $\mathcal G_B$ (109_01 Definition 1.2), the vector
space on which $B(f,g)=\sum_{n\ge2}\Lambda(n)f(n)g(n)$ (109_01 Lemma 1.4) is
proved to converge absolutely and be bilinear (109_01 Theorem 2.1). This is
the candid domain for a radical: every $g$ used below to probe candidate
radical elements is compactly supported, hence trivially in $\mathcal G_B$
(a finite sum has at most finitely many nonzero terms).

> ### Definition 1.1 (the radical)
> $\mathrm{rad}\,B:=\{f\in\mathcal G_B:\ B(f,g)=0\ \text{for every }g\in
> \mathcal G_B\}$.

> ### Definition 1.2 (the prime-power-vanishing space)
> $\mathcal V_{PP}:=\{f\in\mathcal G_B:\ f(p^k)=0\ \text{for every prime }p
> \text{ and every }k\ge1\}$ — equivalently, $f(n)=0$ at every prime power
> $n\ge2$ (no constraint on $f$ off the prime powers).

## 2. The exact computation

> ### Theorem 2.1 (the radical, exactly)
> $\mathrm{rad}\,B=\mathcal V_{PP}$.

**Proof.**

*($\mathcal V_{PP}\subseteq\mathrm{rad}\,B$.)* If $f\in\mathcal V_{PP}$ then
$f(n)=0$ for every prime power $n$, so every term $\Lambda(n)f(n)g(n)$ of
$B(f,g)=\sum_n\Lambda(n)f(n)g(n)$ vanishes identically (the sum only runs
over prime powers, since $\Lambda(n)=0$ elsewhere), for **every** $g$, with
no appeal to any convergence estimate: each term is exactly zero, term by
term, so the sum is exactly zero. Hence $f\in\mathrm{rad}\,B$.

*($\mathrm{rad}\,B\subseteq\mathcal V_{PP}$.)* Suppose $f\in\mathcal G_B$ and
$f\notin\mathcal V_{PP}$, i.e. $f(n_0)\ne0$ for some prime power
$n_0=p_0^{k_0}$. Prime powers are isolated points of $(0,\infty)$ (they are
positive integers), so there is $\varepsilon>0$ with
$(n_0-\varepsilon,n_0+\varepsilon)$ containing no prime power other than
$n_0$ and no other integer either (take $\varepsilon<\tfrac12$). Define
$g\in\mathcal G=C^0((0,\infty))$ by the triangular bump
$$g(x)=\max\Big(0,\ 1-\tfrac{|x-n_0|}{\varepsilon}\Big),$$
continuous, compactly supported in $(n_0-\varepsilon,n_0+\varepsilon)$,
with $g(n_0)=1$ and $g\equiv0$ outside the interval — in particular $g$ is
constant $0$ at every prime power other than $n_0$. Since $g$ has bounded
support, $\sum_n\Lambda(n)|g(n)|^2$ has at most one nonzero term
($n=n_0$), so $g\in\mathcal G_B$ trivially. Then
$$B(f,g)=\sum_n\Lambda(n)f(n)g(n)=\Lambda(n_0)f(n_0)g(n_0)=\Lambda(n_0)f(n_0)\ne0,$$
every other term vanishing because $g(n)=0$ for $n\ne n_0$, and
$\Lambda(n_0)=\log p_0>0$, $f(n_0)\ne0$, $g(n_0)=1$. So $f\notin
\mathrm{rad}\,B$. Contrapositive gives the inclusion. $\square$

This is a complete, elementary, non-circular computation: it uses nothing
but Definition 1.1/1.2, the closed form of $B$ (109_01 Lemma 1.4), and the
existence of continuous bump functions on $(0,\infty)$ — a structural fact
about $\mathcal G=C^0((0,\infty))$ that is *given* by 108_34 Definition 1.1
(an allowed source), not introduced ad hoc to make the answer come out.

## 3. Comparing the shape

$\mathcal V_{PP}$ is defined by **vanishing at a fixed, explicit, discrete
subset of $(0,\infty)$ — the prime powers** — with no reference anywhere in
Definition 1.2 to $\zeta$, $\xi$, or their zeros. This already differs in
*kind* from Stage 0's radical (107_240 Theorem D), which is defined by
vanishing of a **Mellin/Fourier-type transform** $\hat f$ at $0$, $1$, and
every zero $\rho$ of $\xi$ — a condition on the transform side, not on
point-values of $f$ itself. A priori this difference in *phrasing* would
not, by itself, refute anything: it is conceivable that "$f(p^k)=0$ for all
$p,k$" turns out, after Mellin-transforming, to be equivalent to
"$\hat f(\rho)=0$ for all zeros $\rho$" (that is exactly the content of
Weil's explicit formula, in fact — see Remark 3.2). So the pre-registered
refutation criterion is settled by producing an actual witness, not by the
difference in phrasing alone.

> ### Remark 3.2 (why Weil's explicit formula is not invoked here)
> The classical explicit formula converts a sum $\sum_n\Lambda(n)h(n)$
> (for a single, suitably decaying test function $h$, with Mellin transform
> $\hat h$) into $\hat h(0)+\hat h(1)-\sum_\rho\hat h(\rho)-(\text{archimedean
> term})$. Applying this to $h=fg$ (Mellin transform of $fg$ is the Mellin
> *convolution* $\hat f*\hat g$, not simply a product of $\hat f(\rho)$ and
> $\hat g(\rho)$) would require exactly the archimedean completion that row
> (a) has not built — 108_36 §3 states this in so many words: "Does not
> give. The archimedean term, which is Stage 4." Invoking it here would
> import machinery from outside the three allowed sources and outside what
> Phase 108 actually proved for row (a). So $\mathrm{rad}\,B$ is computed
> directly (Theorem 2.1), in scope, and the comparison with Stage 0's shape
> is made by an explicit witness (Theorem 3.3), not by assuming the explicit
> formula would apply.

> ### Theorem 3.3 (an explicit witness refuting the zero-determined
> hypothesis)
> Let $F(x):=\sin(\pi x)$ for $x\in(0,\infty)$. Then:
> (a) $F\in\mathcal G_B$ and $F\in\mathrm{rad}\,B$ (in fact $F\in
> \mathcal V_{PP}$, exactly, by Theorem 2.1);
> (b) $F\not\equiv0$;
> (c) the Mellin transform of $F$, analytically continued from its strip of
> convergence, is $\hat F(s)=\pi^{-s}\Gamma(s)\sin(\tfrac{\pi s}2)$, and
> $\hat F(\rho)\ne0$ for **every** zero $\rho$ of $\xi$ — not merely the
> first one, but all of them, trivial and nontrivial alike (with the
> single, zeta-irrelevant exception $s=0$, which is not a zero of $\xi$
> anyway since $\xi(0)=\xi(1)=\tfrac12\ne0$).

**Proof.**

(a) $F(n)=\sin(\pi n)=0$ for every positive integer $n$ (since $\pi n$ is
an integer multiple of $\pi$), in particular at every prime power. Hence
every term of $\sum_n\Lambda(n)|F(n)|^2$ is zero, so $F\in\mathcal G_B$ with
this sum $=0<\infty$; and $F(p^k)=0$ for every $p,k\ge1$ puts $F\in
\mathcal V_{PP}=\mathrm{rad}\,B$ by Theorem 2.1.

(b) $F(x)=\sin(\pi x)\ne0$ for $x\notin\mathbb Z$, e.g. $F(1.5)=-1\ne0$.

(c) The classical Mellin pair $\int_0^\infty x^{s-1}\sin(x)\,dx=
\Gamma(s)\sin(\tfrac{\pi s}2)$ holds for $0<\Re s<1$ (a standard, elementary
special-function identity, verified numerically below, independent of
anything about $\zeta$). Substituting $x\mapsto\pi x$: $\int_0^\infty
(\pi x)^{s-1}\sin(\pi x)\,\pi\,dx=\Gamma(s)\sin(\tfrac{\pi s}2)$, i.e.
$\hat F(s)=\int_0^\infty x^{s-1}\sin(\pi x)\,dx=\pi^{-s}\Gamma(s)
\sin(\tfrac{\pi s}2)$ on $0<\Re s<1$, continued meromorphically to all of
$\mathbb C$ by the same formula (both factors are already entire/meromorphic
there: $\Gamma$ is meromorphic with poles only at $s=0,-1,-2,\dots$, never
zero anywhere it is defined; $\sin(\tfrac{\pi s}2)$ is entire). $\Gamma(s)$
has **no zeros** (standard fact: $1/\Gamma$ is entire and $\Gamma$ is
nowhere $0$), and $\pi^{-s}\ne0$ always, so $\hat F(s)=0$ iff
$\sin(\tfrac{\pi s}2)=0$ iff $s\in2\mathbb Z$ (even integers). Every zero
$\rho$ of $\xi$ — trivial ($\rho=-2,-4,-6,\dots$ for $\zeta$ itself, but
$\xi$ has no trivial zeros since $\xi$ absorbs the $\Gamma$-factor that
produces them) or nontrivial ($\rho=\tfrac12+i\gamma$, $\gamma\ne0$ real
under RH or in general $0<\Re\rho<1$ unconditionally) — has $\rho\notin
2\mathbb Z$: nontrivial zeros are not real (so certainly not even integers)
except possibly on the real axis inside $(0,1)$, which contains no even
integer; and $\xi$'s zero set is exactly the nontrivial zeros of $\zeta$ by
construction, with none at even integers. Hence $\hat F(\rho)\ne0$ for
every zero $\rho$ of $\xi$. $\square$

This is a complete, closed-form refutation: $F=\sin(\pi x)$ lies in
$\mathrm{rad}\,B$ (proved exactly, Theorem 2.1) while its transform is
**zero-free on the entire zero set of $\xi$** (proved exactly, from
$\Gamma$'s zero-freeness and $\sin$'s explicit zero set — no numerics
required for the proof, though the formula is checked numerically in the
verifier as an independent sanity control).

## 4. Verdict

> ### Corollary 4.1 (Step 2's outcome)
> $\mathrm{rad}\,B=\mathcal V_{PP}$ is **neither zero-determined** (Stage 0's
> shape: Theorem 3.3 exhibits a witness in $\mathrm{rad}\,B$ whose transform
> vanishes at *no* zero of $\xi$, so $\mathrm{rad}\,B\not\subseteq
> \{f:\hat f(\rho)=0\ \forall\rho\}$) **nor $\Gamma$-determined** (Stage 2's
> shape: $\mathcal V_{PP}$ is defined by infinitely many independent
> vanishing conditions, one at each prime power, and is enormous —
> $\{f\in\mathcal G_B:f(2)=f(3)=f(4)=f(5)=f(7)=f(8)=f(9)=\cdots=0\}$, of
> infinite codimension-worth of *constraints* but itself infinite
> dimensional and certainly not the one-dimensional span of a single point
> mass at a single elementary zero $s^*$). It is a **third shape**:
> **prime-power-determined** — governed by evaluation at the discrete set
> $\{p^k:p\text{ prime},k\ge1\}\subset(0,\infty)$, a set with no established
> relation to the zero set of $\xi$.
>
> **The hypothesis of Phase 109 is refuted.** Excluding the identity shell
> does produce a genuine bilinear pairing (Step 1, positive), but that
> pairing's degeneracy has nothing to do with the zeros of $\xi$: its kernel
> is exactly the functions that happen to vanish on the integers $2,3,4,5,
> 7,8,9,\dots$ that are prime powers — an elementary, zero-blind condition,
> in the same structural sense (though not the same object) that 108_91's
> $\Phi$ was zero-blind. Per the mission's rule, Step 3 (signature) is
> skipped: 109_03 records why.

## 5. Scope

**Proved here:** Theorem 2.1 (exact radical, both inclusions, from the
definition alone); Theorem 3.3 (the explicit witness and its transform,
both inclusions of the refutation, in closed form); Corollary 4.1.

**Read from source, not re-derived:** 109_01's $B$ and $\mathcal G_B$;
108_36 Theorem 1.1 (used only via 109_01); the classical Mellin pair
$\int_0^\infty x^{s-1}\sin x\,dx=\Gamma(s)\sin(\pi s/2)$ (standard special-
function fact, not specific to this programme, checked numerically below as
an independent control, not assumed blindly); $\Gamma$'s zero-freeness
(standard).

**Verified numerically:** the Mellin-pair formula for $F$, by numerical
(oscillatory) integration against the closed form, at several real $s$ in
$(0,1)$; $F(n)\approx0$ to available precision at prime powers; $B(F,g)=0$
(to machine precision, tracking exactly with $F$'s residual at prime
powers) against several partner functions $g$, with a control clause that
perturbing $F$ at one prime power produces a nonzero $B$ of the exactly
predicted size; $\hat F(\rho)$ evaluated at the first several nontrivial
zeros of $\zeta$ (via `mpmath.zetazero`), bounded away from $0$, contrasted
with $\hat F(2)=0$ exactly (a genuine even-integer zero, showing the check
can and does detect an actual zero when one is present).

**Not established, and explicitly not claimed:** anything about a possible
*different* bilinearization of the one-sided shells whose radical might
come out zero-determined — Theorem 2.1 rules out only the canonical,
forced construction of 109_01 Definition 1.1, not every conceivable one;
no claim is made that no such alternative exists, only that this one, the
non-circular one, does not have the hoped-for shape.

## 6. Verifier

`109_02_the_radical.py` checks: Theorem 2.1's radical membership exactly
(finite truncated sum, zero to machine precision) for the witness $F$, with
a control clause (perturbing $F$ at one prime power produces the exact
predicted nonzero value, not merely "some" nonzero value); the Mellin-pair
closed form for $F$ against numerical oscillatory integration on
$0<\Re s<1$; $\hat F(\rho)\ne0$ at the first five nontrivial zeros of
$\zeta$ from `mpmath.zetazero`, each individually bounded away from zero by
a margin, contrasted with the control clause $\hat F(2)=0$ exactly (Gamma
finite and nonzero there, $\sin(\pi\cdot2/2)=\sin\pi=0$ exactly).
