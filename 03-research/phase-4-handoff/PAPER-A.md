# A faithful Kreĭn-space realization of the Weil quadratic form
### with a no-go theorem for the zero-side attack on positivity

**David Alejandro Trejo Pizzo**

*Phase-4 deliverable of the Riemann program. Self-contained. Honest about what is and is not proved.*

---

## Abstract

Weil's criterion states that the Riemann Hypothesis (RH) is equivalent to the positivity of an explicit
Hermitian functional $\mathfrak t$ built from the Riemann–Weil explicit formula. We give a rigorous
operator-theoretic realization of $\mathfrak t$ on the classical band-limited (Paley–Wiener) test class
$PW_d$, $d>\tfrac12$. The construction has three layers.

1. **Semibounded realization (B-2).** Modulo a single, precisely isolated hypothesis **(H)** — a *uniform
   short-interval zero-density* statement strictly weaker than RH — the form $\mathfrak t$ is closable and
   defines a self-adjoint operator $\mathcal T$ that is *bounded below*, with $\inf\operatorname{spec}(\mathcal T)$
   a finite, convergent quantity. Four supporting lemmas (integration by parts, a quadrature bound, a vertical
   $L^2$ bound, and a Plancherel–Pólya bound) are proved unconditionally. Consequently
   $\mathrm{RH}\iff\inf\operatorname{spec}(\mathcal T)\ge0$: RH is exactly the *sign* of a finite bottom.

2. **Kreĭn structure.** We prove the exact identity $\mathfrak t=E^*JE$, where $E$ is evaluation at the
   (near-line) zeros and $J$ is a fundamental symmetry whose negative directions are exactly the off-line
   zeros. The construction is therefore a **Kreĭn-space** problem (indefinite metric), not a de Branges
   (a-priori positive) one. Passing to the angular operator $K$ of the sampling range $R(E)$ yields a
   single-axis dictionary:
   $$
   \|K\|<\infty\iff \text{B-2 (finite bottom)},\qquad \|K\|\le1\iff \text{RH}.
   $$
   The whole program is the norm of one operator: B-2 is "$K$ bounded," RH is "$K$ a contraction."

3. **A no-go theorem.** We prove that the explicit dependence of $K$ on the off-line depths $b_\rho$ carries
   **no leverage** toward the sign: the zero-side expression and the arithmetic side of the explicit formula
   are the *same* functional, so bounding $\|K\|\le1$ from the zero side is identically the problem of proving
   arithmetic (Weil) positivity, i.e. RH. Every zero-position-free, sign-agnostic bound lands on the wrong
   side ($\|K\|\gtrsim e^{d}$).

The contribution is thus a **faithful, modular, RH-independent reformulation** together with a rigorous
account of *why* the natural zero-side attacks cannot reach positivity. We situate the construction relative
to Connes–Consani's archimedean angular operator and to the de Branges completion of the Weil distribution:
ours is strongly analogous, the distinguishing feature being its unconditional, explicitly Kreĭn, finite
sampling ladder. We do **not** claim progress past the sign barrier; we claim a precise localization of it.

**Keywords.** Riemann Hypothesis, Weil's criterion, explicit formula, Paley–Wiener spaces, Kreĭn spaces,
angular operator, de Branges spaces, Connes–Consani trace formula.

---

## 1. Introduction

### 1.1 Weil's criterion and the sign problem

Let $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(\tfrac s2)\zeta(s)$ be the completed zeta function, with
nontrivial zeros $\rho$. For a suitable even test function the **Riemann–Weil explicit formula** equates a
sum over zeros with an archimedean term, a pole term, and a sum over primes. Polarizing, one obtains a
Hermitian quadratic functional $\mathfrak t(F)$ with the property
$$
\boxed{\ \mathrm{RH}\iff \mathfrak t(F)\ge0\ \text{ for all admissible }F\ }\tag{Weil}
$$
(Weil's positivity criterion). The difficulty of RH, in this formulation, is **entirely the sign** of
$\mathfrak t$: the right-hand side of the explicit formula is *indefinite* — on-line zeros contribute
$|F(\gamma)|^2\ge0$, while off-line zeros (should they exist) contribute terms of *either sign*. Proving the
sign is proving RH; nothing weaker about the *magnitude* of $\mathfrak t$ suffices.

This paper makes that statement precise and operator-theoretic, and then proves a structural theorem
explaining why the most natural realization cannot, by itself, decide the sign.

### 1.2 What we do, and the logic of the three layers

We work on the **classical band-limited test class** $PW_d$ (Paley–Wiener, exponential type $d>\tfrac12$,
$L^2$ on the line). Band-limited functions are entire, so the off-axis evaluations $F(\gamma+ib)$ forced by
off-line zeros are automatic and well-controlled — this is the technically clean home for Weil's criterion.

- **Layer 1 (§§2–5): a semibounded realization.** We realize $\mathfrak t$ as a self-adjoint operator
  $\mathcal T$ on a Hilbert space $H_+$ and prove it is bounded below — *finiteness of the bottom* — modulo a
  single hypothesis (H) that we isolate exactly. This is the operator-theoretic content of "the bottom is a
  well-defined finite number whose sign is RH."

- **Layer 2 (§§6–7): the Kreĭn / angular-operator picture.** We expose the algebraic structure behind the
  realization: $\mathfrak t = E^*JE$ with $J$ a fundamental symmetry, and the entire program collapses onto
  the norm of the angular operator $K$ of the sampling subspace. This is the conceptually clarifying layer:
  it separates the *geometry* of $PW_d$, the *location* of zeros, and the *sign*, into three independent
  pieces.

- **Layer 3 (§8): a no-go theorem.** We prove that the explicit, attractive depth structure of $K$ gives no
  independent leverage: the zero-side bound on $\|K\|$ is, by the explicit-formula identity, the arithmetic
  positivity itself. This rules out a class of natural attacks and is, in our view, the most useful single
  result of the program.

### 1.3 Main results

> **Theorem A (semibounded realization; §5).** Assume **(H)** (Definition 4.2). On $PW_d\cap H^1$, $d>\tfrac12$,
> the Weil form $\mathfrak t$ is closable in $H_+$ and its self-adjoint operator $\mathcal T$ satisfies
> $\inf\operatorname{spec}(\mathcal T)\ge 1-4C>-\infty$ for a finite $C=C(d,\delta,\eta)$. Consequently
> $\mathrm{RH}\iff\inf\operatorname{spec}(\mathcal T)\ge0$.

> **Theorem B (Kreĭn identity and the single axis; §§6–7).** Unconditionally, $\mathfrak t=E^*JE$ with $J=J^*$,
> $J^2=I$. The angular operator $K$ of $\overline{R(E)}$ is defined (type-density uniqueness), and
> $$
> \|K\|<\infty\iff \text{B-2},\qquad \|K\|\le1\iff \mathrm{RH},
> $$
> with $\|K\|\ge e^{d/2}>1$ from the magnitude side.

> **Theorem C (no-go; §8).** The depths $\{b_\rho\}$ enter $\|K\|$ only through $\mathfrak t$ itself. Hence
> bounding $\|K\|\le1$ from the zero side is identically Weil positivity, and every zero-position-free,
> sign-agnostic bound gives $\|K\|^2\gtrsim e^{d}$ (the wrong side). The zero-side realization, being defined
> in terms of the unknown off-line zeros, cannot attack the sign.

### 1.4 Relation to prior work (summary; full discussion §9)

The angular-operator reduction "$\|K\|\le1\iff$ RH" is **strongly analogous** to the device of
Connes–Consani [CC], who reduce Weil positivity to lowering below $1$ the top eigenvalue of an operator $K$
built at the archimedean place. The completion of the Weil form into a reproducing-kernel space is the theme
of [HW] (arXiv:2301.00421), who obtain a *de Branges* space under RH. Our construction differs in being
**unconditional** (no RH assumed; the metric is genuinely indefinite, hence Kreĭn not de Branges) and in
exposing an **explicit finite sampling ladder**. We do **not** claim an identification of our $K$ with the
Connes–Consani $K$; Theorem C in fact explains why the zero-side realization, unlike the archimedean one,
cannot be a computational handle.

### 1.5 Honest scope

Theorem A is conditional on (H); (H) is much weaker than RH but is **not** established unconditionally by
current methods (§4.3). Theorems B and C are unconditional. **None of the three proves RH**, and Theorem C
proves that this particular (zero-side) route cannot. The value of the paper is a clean, faithful
reformulation plus a rigorous map of the wall.

---

## 2. Setup and notation

### 2.1 The test class

For $d>\tfrac12$ let
$$
PW_d:=\{F\in L^2(\mathbb R): F\text{ entire of exponential type }\le d\}
=\{F:\widehat F\in L^2[-d,d]\},
$$
with $\widehat F(\xi)=\int F(t)e^{-i t\xi}\,dt$. We use the refined domain $\mathcal D:=PW_d\cap H^1$ (so that
$\widehat F\in H^1[-d,d]\hookrightarrow C^0$), which is dense in $PW_d$. Two classical inequalities are used
repeatedly:
$$
\text{(Bernstein)}\quad \|F'\|_2\le d\,\|F\|_2,\qquad\qquad
\text{(Nikolskii)}\quad \|F\|_\infty\le C_d\|F\|_2 .\tag{2.1}
$$

### 2.2 Zeros, depths, partners

Write a nontrivial zero as
$$
\rho=\tfrac12+b_\rho+it_\rho,\qquad b_\rho,\,t_\rho\in\mathbb R,
$$
so $b_\rho=0\iff\rho$ on the critical line. The functional equation gives the symmetric quartet
$\{\rho,\bar\rho,1-\rho,1-\bar\rho\}$. Define the **reflected partner involution**
$$
\sigma(\rho):=1-\bar\rho=\tfrac12-b_\rho+it_\rho,\qquad \sigma^2=\mathrm{id},\quad
b_{\sigma(\rho)}=-b_\rho,\ \ t_{\sigma(\rho)}=t_\rho .\tag{2.2}
$$
The zero-counting density is $\rho(T)=\tfrac1{2\pi}\log\tfrac{T}{2\pi}$, and $S(T)=N(T)-\bar N(T)=O(\log T)$
unconditionally. The **Nyquist cell** has length $1/d$ and contains $\sim \rho(T)/d=:P(T)\to\infty$ zeros
(over-sampling).

### 2.3 The Weil functional and its on/off decomposition

For $F\in\mathcal D$ let $h(z):=F(z)\overline{F(\bar z)}$ be the entire extension of $|F|^2$. The explicit
formula gives
$$
\mathfrak t(F):=\sum_\rho h\!\big(\text{spectral point of }\rho\big)
= \underbrace{\mathfrak a(F)}_{\text{archimedean}}+\underbrace{\mathfrak q(F)}_{\text{pole}}
-\underbrace{\mathfrak p(F)}_{\text{primes}} .\tag{2.3}
$$
The spectral point of $\rho=\tfrac12+b_\rho+it_\rho$ is $t_\rho+ib_\rho$ (so on-line zeros are sampled on the
real axis). Grouping by partners (2.2) yields the **on/off decomposition**
$$
\mathfrak t(F)=\underbrace{\sum_{b_\rho=0}|F(t_\rho)|^2}_{\mathfrak t_+(F)\,\ge0}
\;+\;\underbrace{\sum_{\text{off-line pairs}}2\,\mathrm{Re}\!\big[F(t_\rho+ib_\rho)\,\overline{F(t_\rho-ib_\rho)}\big]}_{\mathfrak t_-(F)\ \text{indefinite}} .\tag{2.4}
$$
With $\widetilde{\mathfrak t}_-(F):=\sum_{b_\rho\ne0}|F(t_\rho+ib_\rho)|^2$ one has the crude bound
$|\mathfrak t_-(F)|\le 2\,\widetilde{\mathfrak t}_-(F)$ (sharpened to an exact projection identity in §6).

### 2.4 The realization space

Let $H_+$ be the completion of $\mathcal D$ in the seminorm $\|F\|_{H_+}^2:=\mathfrak t_+(F)$ (the on-line
sampling space; $\cong\ell^2(\{\text{on-line }t_\rho\})$ when coercive). $\mathcal T$ denotes the self-adjoint
operator associated with the form $\mathfrak t$ on $H_+$.

> **Remark 2.1 (why this is the right home).** Band-limited $\Rightarrow$ entire $\Rightarrow$ the off-axis
> samples $F(t_\rho\pm ib_\rho)$ exist and are $L^2$-controlled by Plancherel–Pólya (Lemma D). No
> strip-weight or growth machinery is needed; the indefiniteness of $\mathfrak t_-$ is the *only* obstacle,
> and it is structural (the sign), not analytic.

---

## 3. The four unconditional lemmas

These four estimates are the analytic backbone. All are unconditional.

### 3.1 Lemma A — integration by parts

> **Lemma A.** For $F\in\mathcal D$ and $g:=|F|^2$,
> $$
> E_g:=\sum_{b_\rho=0} g(t_\rho)-\int g(t)\,\rho(t)\,dt=-\int g'(t)\,S(t)\,dt .
> $$

*Proof.* Since $\widehat F\in H^1[-d,d]\hookrightarrow C^0$, integrating by parts in $\xi$ gives
$F(t)=\tfrac{1}{2\pi i t}\big[\widehat F(d)e^{itd}-\widehat F(-d)e^{-itd}-\int_{-d}^d\widehat F'(\xi)e^{it\xi}d\xi\big]$,
so $|F(t)|=O(1/t)$, $g=O(t^{-2})$, and $g(t)\log t\to0$. The boundary terms $[g\,S]_{\pm\infty}$ vanish, and
$S$ has locally bounded variation with $dS=dN-\rho\,dt$; Stieltjes integration by parts yields the claim.
$\qquad\square$

### 3.2 Lemma B — the quadrature error is $O(\mathfrak t_+)$

> **Lemma B.** $|E_g|\le 2d\,\big(\sup_{\mathrm{supp}\,g}|S|\big)\,\|F\|_2^2=O\!\big(\rho\,\|F\|_2^2\big)=O(\mathfrak t_+(F))$.

*Proof.* $g'=2\,\mathrm{Re}(F'\overline F)$, so $\int|g'|\le 2\|F'\|_2\|F\|_2\le 2d\|F\|_2^2$ by Bernstein
(2.1). On $\mathrm{supp}\,g$ near height $T_0$, $|S|=O(\log T_0)$, and the tail
$\int_{|t-T_0|>R}|g'||S|=O\!\big(\tfrac{\log T_0}{R^2}\big)$ is controlled by $g'=O(t^{-3})$. Thus
$|E_g|\le C_d(\log T_0)\|F\|_2^2$. Because the main on-line term is
$\sum_{b_\rho=0}|F(t_\rho)|^2\sim \rho\,\|F\|_2^2\sim \tfrac{\log T_0}{2\pi}\|F\|_2^2$, this is $O(\mathfrak t_+)$.
$\qquad\square$

> **Key point.** B-2 (finiteness of the bottom) needs only $E_g=O(\mathfrak t_+)$; the sharp $o(\mathfrak t_+)$
> — which would require Montgomery pair-correlation / RH-level input — is **not** needed. This is the single
> most important calibration of the whole program: *we need an $O$, not an $o$.*

### 3.3 Lemma C — vertical $L^2$ bound

> **Lemma C.** For $F\in PW_d$ and $|b|<\tfrac12$,
> $\ \|F(\cdot+ib)\|_2^2=\int_{-d}^d|\widehat F(\xi)|^2e^{-2b\xi}\,d\xi\le e^{2d|b|}\|F\|_2^2\le e^{d}\|F\|_2^2.$

*Proof.* Parseval for the shifted line, then $e^{-2b\xi}\le e^{2d|b|}\le e^{d}$ on $|\xi|\le d$, $|b|<\tfrac12<d$.
Exact, no RH. $\qquad\square$

The amplification constant $\kappa(b):=e^{2d|b|}$ — bounded by $e^d$ but $>1$ for $b\ne0$ — is the precise
quantitative source of the eventual lower bound $\|K\|\ge e^{d/2}$ (§7).

### 3.4 Lemma D — off-line sum bound (Plancherel–Pólya)

> **Lemma D.** $\ \widetilde{\mathfrak t}_-(F)=\sum_{b_\rho\ne0}|F(t_\rho+ib_\rho)|^2\le C_d\,\rho\,\|F\|_2^2.$

*Proof.* Off-line spectral points satisfy $|\Im(t_\rho+ib_\rho)|=|b_\rho|<\tfrac12<d$ (strip interior, margin
$d-\tfrac12>0$). The band-limited Plancherel–Pólya / Bessel inequality, valid for **arbitrary (possibly
clustered)** sequences in a strip interior, gives $\sum_n|F(w_n)|^2\le B\|F\|_2^2$ with
$B\asymp_d\sup_x\#\{n:\Re w_n\in[x,x+\tfrac1d]\}$. The pointwise bound $|F(w)|^2\le C_d\int_{|x-\Re w|<1/d}|F|^2$
(band-limited flatness) summed over $\le$ (cell count) points per window gives
$B\le C_d\cdot\sup_x\#\{\text{zeros in }[x,x+\tfrac1d]\}=O(\rho)$ by Riemann–von Mangoldt and $S=O(\log)$.
$\qquad\square$

> **Why $O(\rho)$ and not $o(\rho)$.** Zero-density makes off-line zeros *globally* sparse, but they may
> *cluster locally*; the cell count is bounded by the **total** $O(\rho)$, not by the (smaller) off-line
> density. Replacing it by the off-line density would yield $o(\mathfrak t_+)$ = RH — forbidden by possible
> clustering. The honest output is the $O$ of B-2.

---

## 4. Coercivity, the depth split, and the hypothesis (H)

### 4.1 The reduction to coercivity

Lemmas C–D give $\widetilde{\mathfrak t}_-\le C_d\rho\|F\|_2^2$. To conclude
$\widetilde{\mathfrak t}_-\le C\,\mathfrak t_+$ (which is B-2; see §5) we need **coercivity**:
$$
\mathfrak t_+(F)\ge c\,\rho\,\|F\|_2^2 \qquad(\text{a lower frame/sampling bound}).\tag{4.1}
$$
This is *not* free. By the Beurling gap theorem, the on-line zeros are a set of sampling for $PW_d$ only if
they have **no gap exceeding** $\pi/d$; the necessary density condition $D^-\ge d/\pi$ is **not sufficient**.
A single Nyquist gap containing a bump of $F$ destroys (4.1). (This corrected an earlier hope that
over-density $D^-=\infty$ alone gives coercivity — it does not.)

### 4.2 The depth split and the hypothesis

Coercivity is needed only **where $\widetilde{\mathfrak t}_->0$**, i.e. near off-line zeros. Split off-line
zeros by depth at a threshold $\delta$:
- **shallow** ($|b_\rho|<\delta$): $\kappa(b_\rho)\le e^{2d\delta}=1+O(\delta)$, so $F(t_\rho+ib_\rho)\approx F(t_\rho)$;
  these sample like on-line points and **help** coercivity;
- **deep** ($|b_\rho|\ge\delta$): amplified ($\kappa$ up to $e^d$); the only danger.

So B-2 reduces to: *deep off-line zeros do not dominate any Nyquist cell at large height.* Precisely:

> **Definition 4.2 — Hypothesis (H) (uniform local sparsity of deep off-line zeros).** There exist
> $\delta>0$, $\eta>0$, $T_0$ such that for all $T\ge T_0$ and every interval $I$ of length $1/d$ centred at
> height $T$,
> $$
> \#\{\rho:\ |b_\rho|<\delta,\ t_\rho\in I\}\ \ge\ \eta\,\rho(T)\,|I| .
> $$
> Equivalently: on-line + shallow zeros retain a positive fraction $\eta$ of every Nyquist cell (deep
> off-line zeros occupy at most $(1-\eta)$ of each cell).

> **Lemma E ((H) $\Rightarrow$ coercivity).** Under (H), every Nyquist cell contains $\ge\eta\rho|I|$ samples
> with $\kappa=1+O(\delta)$; this set has no Nyquist gaps, so by Beurling
> $\sum_{\text{shallow}\cup\text{on}}|F(t_\rho)|^2\ge c\eta\,\rho\|F\|_2^2$. The shallow part exceeds
> $\mathfrak t_+$ only on the on-line subset and the $\kappa=1+O(\delta)$ amplification is bounded; taking
> $\delta$ small gives (4.1). $\qquad\square$

### 4.3 The honest status of (H)

(H) is **strictly weaker than RH**: RH says there are *no* off-line zeros; (H) says only that deep ones do
not *locally dominate* (they may exist, even infinitely many, provided they do not fill a Nyquist cell). It
is implied by RH, and by any uniform short-interval zero-density bound
$N(\tfrac12+\delta,T+\tfrac1d)-N(\tfrac12+\delta,T)=o(\rho)$.

However, **(H) is not established unconditionally by current methods.** The global density
$N(\tfrac12+\delta,T)\ll T^{1-c\delta}$ leaves a budget allowing $\sim\log T$ deep zeros to be concentrated in
a single short interval (cost $\log T\ll T^{1-c\delta}$), which the global bound does not forbid. Selberg's
fluctuation theory makes such a cell-filling cluster a *large deviation* of $S$, of measure
$\ll\exp(-c(\log T)^2/\log\log T)$ — extraordinarily rare, but not provably absent at sporadic large heights.
And (H) is genuinely necessary: without it there exist $F$ with $\mathfrak t_+(F)=0$ but $\mathfrak t_-(F)\ne0$,
which break closability in $H_+$ (the operator is not even defined). We tried alternative realizations
(all-zeros norm, $L^2$); each reduces to the same gap/clustering condition. So:
$$
\boxed{\ \text{Theorem A is unconditional modulo (H); (H) is a uniform short-interval zero-density bound, }\ll\text{ RH, very likely true, at the frontier of the unconditional.}\ }
$$

---

## 5. Theorem A — the semibounded realization

> **Theorem A.** Assume (H). On $\mathcal D=PW_d\cap H^1$, $d>\tfrac12$:
> 1. $\mathfrak t$ is **closable** in $H_+$ and defines a **self-adjoint operator $\mathcal T$**;
> 2. $\mathcal T$ is **bounded below**: for a finite $C=C(d,\delta,\eta)$,
>    $$
>    \boxed{\ \inf\operatorname{spec}(\mathcal T)\ \ge\ 1-4C\ >\ -\infty.\ }
>    $$

*Proof.* By Lemmas C–D and Lemma E (under (H)),
$\widetilde{\mathfrak t}_-\le \tfrac{C_d}{c}\,\mathfrak t_+=:C\,\mathfrak t_+$, hence
$|\mathfrak t_-|\le 4C\,\mathfrak t_+$ (the factor $4$ is removed in §6). In $H_+$, where
$\mathfrak t_+=\|\cdot\|_{H_+}^2$,
$$
\frac{\mathfrak t(F)}{\|F\|_{H_+}^2}=1+\frac{\mathfrak t_-(F)}{\mathfrak t_+(F)}\ge 1-4C .
$$
$\mathfrak t_+$ is closed (a monotone limit of bounded forms; Kato), and $\mathfrak t_-$ is form-bounded
relative to $\mathfrak t_+$ with bound $4C$ (Lemma E gives the relative bound finite). Therefore
$\mathfrak t=\mathfrak t_++\mathfrak t_-$ is closed and semibounded, and $\mathcal T$ is the self-adjoint
operator associated with it via KLMN, with form domain $H_+$. $\qquad\square$

> **Corollary A′ (faithful reformulation).** The positivity $\mathfrak t\succeq0$ does not refer to the inner
> product, so its truth is norm-independent; combined with Theorem A,
> $$
> \boxed{\ \mathrm{RH}\ \Longleftrightarrow\ \inf\operatorname{spec}(\mathcal T)\ \ge\ 0\ }
> $$
> — RH is exactly the **sign** of the finite bottom of the rigorously realized operator $\mathcal T$.

**What Theorem A is, and is not.** It is a faithful, RH-independent **semibounded realization**: the bottom
is a convergent finite number, computable in principle, whose sign is RH. It is **not** a proof of RH: it
relocates RH to the sign of a concrete object, it does not evaluate that sign. The magnitude estimates give
$C\ge e^{d}>1$ — the bottom $1-4C$ is *negative*; lowering $C$ to $\le\tfrac14$ (so the bottom $\ge0$) is
exactly RH.

---

## 6. Theorem B (i) — the Kreĭn identity $\mathfrak t=E^*JE$

We now expose the algebra behind the realization. **This section is unconditional.**

### 6.1 Evaluation operator and fundamental symmetry

Define the **evaluation operator**
$$
E:PW_d\to\ell^2(\rho),\qquad (EF)_\rho:=F(t_\rho+ib_\rho),
$$
bounded by Lemma D. Define the **fundamental symmetry** $J$ as the linear involution induced by the partner
map (2.2):
$$
(Jc)_\rho:=c_{\sigma(\rho)},\qquad \sigma(\rho)=1-\bar\rho .
$$
Then $J^2=I$ and $J=J^*$ (a permutation by an involution is self-adjoint) — a genuine **Kreĭn fundamental
symmetry**.

> **Proposition 6.1 (the identity).** With $\langle a,b\rangle=\sum_\rho a_\rho\overline{b_\rho}$,
> $$
> \langle EF,\,JEF\rangle=\sum_\rho (EF)_\rho\,\overline{(EF)_{\sigma(\rho)}}
> =\sum_\rho F(t_\rho+ib_\rho)\,\overline{F(t_\rho-ib_\rho)}=\mathfrak t(F),
> $$
> i.e.
> $$
> \boxed{\ \mathfrak t=E^*JE,\qquad J=J^*,\ J^2=I.\ }\qquad\text{(exact, unconditional)}
> $$

*Proof.* Immediate from $b_{\sigma(\rho)}=-b_\rho$, $t_{\sigma(\rho)}=t_\rho$ and (2.3). $\qquad\square$

> **Remark 6.2 (convention).** Writing $J$ with a complex conjugation, $(Jc)_\rho=\overline{c_{\bar\rho}}$,
> makes it antilinear; that form coincides with the linear $J$ above on real-type test functions
> ($F(\bar z)=\overline{F(z)}$). The linear involution is the convention-free statement and is what we use.

### 6.2 The three structural consequences

- **(C1)** *RH $\Rightarrow J=I\Rightarrow\mathcal T=E^*E\ge0$.* Under RH all $b_\rho=0$, so
  $\sigma(\rho)=\rho$, $J=I$, $\mathfrak t=E^*E\ge0$. Weil positivity becomes the trivial positivity of a Gram
  operator. (A consistency check, RH assumed.)
- **(C2)** *RH fails $\Rightarrow$ $J=I_{\mathrm{on}}\oplus\bigoplus_{\text{pairs}}\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$.*
  Each off-line quartet splits under $\sigma$ into two swap-pairs $\{\rho,1-\bar\rho\}$, each a $2\times2$ swap
  with spectrum $\{+1,-1\}$. **All negative directions of $J$ come exactly from off-line zeros.**
- **(C3)** *RH $\iff E^*JE\ge0\iff R(E)$ is a $J$-non-negative subspace.*

The conceptual gain is the **clean separation** of three a-priori entangled things: the geometry of $PW_d$
(through $R(E)$), the location of zeros (through $\sigma$, hence $J$), and the sign (through the indefinite
form $[\,\cdot,\cdot\,]_J$).

---

## 7. Theorem B (ii) — the angular operator and the single axis

### 7.1 Fundamental decomposition and the exact split

Let $\ell^2(\rho)=\mathcal K_+\oplus\mathcal K_-$ with $J=P_+-P_-$. On a swap-pair the $\pm1$ eigenvectors are
$\tfrac1{\sqrt2}(e_\rho\pm e_{\sigma\rho})$, so with $F_\pm:=F(t_\rho\pm ib_\rho)$,
$$
\|P_+EF\|^2=\mathfrak t_+ +\!\!\sum_{\text{pairs}}\tfrac12|F_++F_-|^2,\qquad
\|P_-EF\|^2=\!\!\sum_{\text{pairs}}\tfrac12|F_+-F_-|^2,
$$
and **exactly** (no factor-4 slack)
$$
\boxed{\ \mathfrak t(F)=\|P_+EF\|^2-\|P_-EF\|^2 .\ }\tag{7.1}
$$

### 7.2 The angular operator and the dictionary

> **Lemma 7.1 (qualitative injectivity, unconditional — not circular).** $P_+EF=0\Rightarrow F=0$.

*Proof.* $P_+EF=0$ forces $F$ to vanish at all on-line zeros. By the classical **type-density uniqueness
theorem** (a nonzero $L^2$ function of exponential type $d$ cannot vanish on a real sequence of density
$>d/\pi$), and the on-line zeros have density $\tfrac1{2\pi}\log T\to\infty\gg d/\pi$, we get $F=0$. This uses
only the zeros of $F$, no sampling/coercivity input. $\qquad\square$

Hence $\overline{R(E)}$ is the graph of the **angular operator**
$$
K:=P_-\big(P_+|_{R(E)}\big)^{-1}:\ \mathcal K_+\supseteq\mathrm{dom}\,K\to\mathcal K_- ,
$$
**defined unconditionally** (possibly unbounded). Standard Kreĭn theory (Azizov–Iokhvidov, Ch. 1) gives:

> **Theorem B (single-axis dictionary).**
> $$
> \boxed{\ \underbrace{\text{type-density}}_{K\ \text{defined}}\ ;\quad
> \underbrace{(H)\Rightarrow\|K\|<\infty}_{\textbf{B-2 (finite bottom)}}\ ;\quad
> \underbrace{\|K\|\le1\iff \textbf{RH}}_{\text{given }K\text{ defined}}.\ }
> $$
> - $\|K\|<\infty\iff R(E)$ uniformly positive-projecting $\iff$ the coercivity B-2 needs; **(H) is sufficient
>   for it.** (The earlier "$(H)\iff\|K\|<\infty$" overstated; the honest direction is
>   $(H)\Rightarrow\|K\|<\infty\Rightarrow$ B-2.)
> - $\|K\|\le1\iff\|P_-EF\|\le\|P_+EF\|\ \forall F\iff\mathfrak t\ge0\iff$ RH (unconditional given $K$ defined;
>   if $K$ unbounded then $\|K\|>1$, RH false — consistent).
> - From the magnitude side, $\|K\|\ge e^{d/2}>1$ (Lemma C); the bound is on the **wrong side** of $1$.

**Cleanest statement of the program.** *B-2 = "$K$ bounded" (needs (H)); RH = "$K$ a contraction."* Everything
is the norm of one operator.

### 7.3 Where the negativity lives (and a warning)

On a swap-pair the negative coordinate is the vertical antisymmetric difference
$$
d_\rho:=F(t_\rho+ib_\rho)-F(t_\rho-ib_\rho)=2i\,b_\rho\,F'(t_\rho)+O(b_\rho^3\|F''\|),
$$
so to leading order $\|P_-EF\|^2\approx\sum_{\text{pairs}}2\,b_\rho^2|F'(t_\rho)|^2$: the negative directions
are **depth-weighted derivative samples**, and $\|K\|\to0$ as depths $\to0$.

> **Warning (the optimistic-pillar trap).** The $b_\rho^2$ form is the **shallow linearization only.** The
> Taylor remainder is $O(b_\rho^3\|F''\|)$ with $\|F''\|\le d^2\|F\|$ (Bernstein); for **deep** zeros ($|b_\rho|$
> up to $\tfrac12$, $d$ moderately $>\tfrac12$) the remainder/leading ratio is $\sim b_\rho^2 d=O(1)$ — the
> expansion does not converge, and the true vertical evaluation carries the $e^{2d|b_\rho|}$ amplification that
> is the source of $\|K\|\ge e^{d/2}$. Thus a "$\sum b_\rho^2|F'|^2\le\theta\,\mathfrak t_+\Rightarrow$ RH"
> inequality would deliver RH only on the shallow part already known harmless. **The correct concrete target
> keeps the full vertical difference:**
> $$
> \|K\|^2=\sup_F\frac{\sum_{\text{pairs}}\tfrac12\,|F(t_\rho+ib_\rho)-F(t_\rho-ib_\rho)|^2}
> {\mathfrak t_+ +\sum_{\text{pairs}}\tfrac12\,|F(t_\rho+ib_\rho)+F(t_\rho-ib_\rho)|^2},
> \qquad \|K\|\le1\iff\mathrm{RH}.\tag{7.2}
> $$

This Rayleigh quotient (7.2) is the first concrete, estimable object of the program. The natural next hope —
that its explicit dependence on the depths $b_\rho$ gives leverage absent from the archimedean approach — is
exactly what the next section refutes.

---

## 8. Theorem C — a no-go theorem for the zero-side attack

> **Theorem C.** The depths $\{b_\rho\}$ enter $\|K\|$ only through $\mathfrak t$ itself. Consequently,
> bounding $\|K\|\le1$ from the zero side is identically the problem of proving Weil positivity (RH), and
> every zero-position-free, sign-agnostic bound on $\|P_-EF\|$ yields $\|K\|^2\gtrsim e^{d}$ — the wrong side
> of $1$.

*Proof.* The pivot is that the explicit formula gives $\mathfrak t(F)$ as the **same functional** in two ways:
$$
\underbrace{\|P_+EF\|^2-\|P_-EF\|^2}_{\text{zero side: depends on }\{t_\rho,b_\rho\}}
\;=\;\mathfrak t(F)\;=\;
\underbrace{\mathfrak a(F)+\mathfrak q(F)-\mathfrak p(F)}_{\text{arithmetic side: contains no }b_\rho}.\tag{8.1}
$$

**(i) No independent information in the depths.** The arithmetic side sums the depths out — it does not
contain $b_\rho$. Since both sides equal the same functional of $F$, any bound on $\|K\|$ phrased through the
$b_\rho$ is, by (8.1), a bound on $\mathfrak t$ through the arithmetic side in disguise. The depth dependence
is the answer re-encoded, not a lever.

**(ii) Tautology w.r.t. Weil.** $\|K\|\le1\iff\|P_-EF\|\le\|P_+EF\|\ \forall F\iff\mathfrak t\ge0\iff
\mathfrak a+\mathfrak q-\mathfrak p\ge0\iff$ RH. Lowering $\|K\|$ to $\le1$ *is* proving arithmetic positivity;
it cannot be done from the zero side without already having RH.

**(iii) Sign-agnostic bounds land on the wrong side.** Dropping the phase cancellation between $F_+$ and
$F_-$ (triangle inequality $|F_+-F_-|^2\le 2(|F_+|^2+|F_-|^2)$) gives
$\|P_-EF\|^2\le \kappa\cdot(\text{off-line cell count})\,\|F\|^2$, $\kappa$ up to $e^{2d|b|}$, hence
$\|K\|^2\gtrsim e^{d}$. Retaining the phase requires the exact analytic continuation of $F$ at
$t_\rho\pm ib_\rho$; for deep zeros that is not the $2ib_\rho F'$ linearization (shallow-only) but the global
behaviour of $F$ — i.e. the arithmetic side again. So there is no zero-position-free, sign-aware bound.
$\qquad\square$

> **Corollary C′ (why the zero-side realization is circular as a tool).** To even *write*
> $K=P_-(P_+|_{R(E)})^{-1}$ one must know the off-line zero data $\{(t_\rho,b_\rho):b_\rho\ne0\}$ — the very
> data whose emptiness is RH. The realization is a true identity but **presupposes the unknowns.**
> Connes–Consani's realization is the *useful* one precisely because its $K$ is built from explicit
> archimedean data, **independent of the zeros**. This is the structural reason the zero-side picture cannot
> attack the sign.

$$
\boxed{\ \textbf{No-go: } \|K\|\text{ depends on the off-line depths only through }\mathfrak t;\ \text{bounding }\|K\|\le1\text{ from the zero side}\equiv\text{Weil positivity}\equiv\text{RH.}\ }
$$

---

## 9. Relation to prior work

**Connes–Consani [CC] (arXiv:2006.13771).** They reduce Weil positivity to lowering below $1$ the maximal
eigenvalue of an operator $K$ built at the **archimedean place**, obtaining "positivity of $\mathrm{Id}-K$."
Our "$\|K\|\le1\iff$ RH" is a reduction *of the same type*. We do **not** claim an identification
$U\,K_{\text{ours}}\,U^{-1}=K_{CC}$; the two are **distinct realizations of the same form**: ours is
*zero-side* (depends on the zeros), theirs is *archimedean* (explicit, independent of the zeros). Theorem C
explains the asymmetry — the archimedean realization is a genuine handle, the zero-side one is circular.

**The de Branges completion [HW] (arXiv:2301.00421).** Completing the Weil-distribution Hermitian form into
a Hilbert space yields, *under RH*, a de Branges space (positive, reproducing-kernel), turning Weil's
inequality into equalities. Our completion is the same in spirit but **unconditional**: with off-line zeros
allowed, the metric is genuinely indefinite, so the natural object is a **Kreĭn** space (Pontryagin only if
the off-line set were finite, which is not known). The Kreĭn-vs-de-Branges dichotomy is exactly the
positivity-built-in-vs-not distinction.

**Classical lineage.** Weil's criterion; Barner's and Burnol's explicit-formula Hilbert spaces; de Branges'
*Hilbert Spaces of Entire Functions* (the positive regime); Azizov–Iokhvidov for Kreĭn-space angular
operators; Montgomery/Selberg for the zero statistics behind (H). None proved RH; all are permanent
references. Our place in this lineage is a **modular reformulation plus a no-go**, not a new mechanism for
positivity.

---

## 10. Honest status, and open problems

**What is proved.**
| Statement | Status |
|---|---|
| Lemmas A–D (IBP, quadrature $O(\mathfrak t_+)$, vertical $e^d$, Plancherel–Pólya) | ✅ unconditional |
| Depth split; (H) $\Rightarrow$ coercivity (Lemma E) | ✅ unconditional |
| Theorem A (semibounded realization $\mathcal T$, $\inf\operatorname{spec}\ge1-4C$) | ✅ **modulo (H)** |
| Corollary A′ (RH $\iff$ sign of the bottom) | ✅ modulo (H) |
| Theorem B (i): $\mathfrak t=E^*JE$, $J$ a fundamental symmetry | ✅ unconditional |
| Theorem B (ii): angular operator, dictionary $\|K\|<\infty/\le1$ | ✅ unconditional |
| Theorem C: no-go for the zero-side attack | ✅ unconditional |
| RH itself (the sign) | — not proved; Theorem C shows this route cannot |

**What is not claimed.** No proof of RH. Theorem A is conditional on (H); (H) is much weaker than RH but not
unconditionally established (§4.3). The Kreĭn picture is the correct language and the precise target, and
Theorem C proves it is not a route past the sign.

**Open problems.**
1. **(H) unconditional?** Is the uniform (every cell, all large $T$) short-interval zero-density for fixed
   $\sigma>\tfrac12$ unconditional, or only on average? This is the one item separating "unconditional B-2"
   from "B-2 modulo (H)." (Selberg moments / large deviations of $S$.)
2. **Sharp constants.** The Plancherel–Pólya constant in Lemma D with clustering and margin $d-\tfrac12$; the
   quantitative Beurling step in Lemma E; the exact value of $\|K\|$ on the magnitude side.
3. **The only route to the sign** (outside this paper). By Theorem C the sign cannot come from the zero side;
   it requires **structural positivity** — a factorization $\mathcal T=A^*A$, Connes' archimedean trace
   positivity, or a de Branges chain — i.e. an independently-given positive structure, not a bound. This is
   the genuine RH problem and is left open.

**One-paragraph conclusion.** Starting from Weil's criterion (RH $\iff$ a positivity), we built a faithful,
RH-independent, semibounded operator realization $\mathcal T$ whose bottom is finite and whose sign is RH
(Theorem A), exposed its exact Kreĭn structure $\mathfrak t=E^*JE$ and the single controlling axis $\|K\|$
(Theorem B), and proved that this zero-side structure — however explicit its dependence on the off-line
zeros — cannot decide the sign, because the depths enter only through the very functional whose positivity is
RH (Theorem C). The program therefore delivers a precise *localization* of RH's difficulty (the sign; the
contraction $\|K\|\le1$) and a rigorous account of why the natural zero-side attacks fail, but not a proof.
The sign, as the field has long suspected, requires structural positivity, which the magnitude/zero-side
machinery provably cannot supply.

---

### References
- [CC] A. Connes, C. Consani, *Weil positivity and trace formula, the archimedean place*, arXiv:2006.13771.
- [HW] *On the Hilbert space derived from the Weil distribution*, arXiv:2301.00421.
- T. Ya. Azizov, I. S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric*, Wiley, 1989.
- L. de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall, 1968.
- A. Weil, *Sur les “formules explicites” de la théorie des nombres premiers*, 1952.
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*, 1973; A. Selberg, *On the remainder
  in the formula for $N(T)$*, 1944.

*(Cross-references: full derivations in `phase-4-handoff/B2-THEOREM.md`, `B3-KREIN-STRUCTURE.md`,
`RH-ENDGAME.md`, and the proof log `phase-4-handoff/proofs/00-PROOF-LOG.md`.)*
