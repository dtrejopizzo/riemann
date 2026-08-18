# 108.91 — The symmetrization collapse: why Stages 2–5 lost the zeros, and what Stage 6 must not do

## 0. Status of this note

§§1–3 are **theorems**, with written proofs and a verifier.  §4 is a
**synthesis with retrodictive support**, in the sense of 108_90 §0 — a design
condition, not a theorem.  The two are kept strictly apart.

This note answers a question the phase had not asked explicitly: *why* did
Stages 2, 3, 4 and 5 all produce correct identities that turned out to carry
no arithmetic information?  There is a single mechanism, it is elementary,
and it is diagnosable in advance.  It is **not** the rigidity-versus-finiteness
clash of 108_90; that condition is about equivariance versus support, and it
is orthogonal to this one.

No zero of $\xi$ is used in any definition below.

## 1. The collapse

> ### Definition 1.1
> $A(s):=\dfrac{\zeta'}{\zeta}(s)+\dfrac{\zeta'}{\zeta}(1-s)$, the
> **mirror-symmetrized** logarithmic derivative of $\zeta$.
>
> $G:=\log\Gamma_\R$, $\Gamma_\R(s)=\pi^{-s/2}\Gamma(s/2)$, and
> $P(s):=\frac1s+\frac1{s-1}$, the logarithmic derivative of the polar factor
> $\frac{s(s-1)}2$ of $\xi$.

> ### Theorem 1.2 (the symmetrization collapse)
> \[
>  \boxed{\;A(s)\;=\;-\,G'(s)-G'(1-s)\;=\;\log\pi-\tfrac12\psi\!\big(\tfrac
>  s2\big)-\tfrac12\psi\!\big(\tfrac{1-s}2\big).\;}
> \]
> In particular $A$ is an **elementary function of $\Gamma$ alone**: it
> contains no prime, no Euler factor, and no zero of $\zeta$.

**Proof.**  $\xi(s)=\frac{s(s-1)}2\Gamma_\R(s)\zeta(s)$ satisfies
$\xi(s)=\xi(1-s)$.  Differentiating that identity gives
$\xi'(s)=-\xi'(1-s)$, hence $F(s)+F(1-s)=0$ for $F:=\xi'/\xi$.  Expanding
$F=P+G'+\zeta'/\zeta$ and using $P(s)+P(1-s)=0$ (108_39 Theorem 2.1) leaves
$\big[G'(s)+G'(1-s)\big]+A(s)=0$. $\square$

> ### Corollary 1.3 (holomorphy at the zeros)
> $A$ is holomorphic on $\C\setminus\Z$.  In particular $A$ is holomorphic at
> every zero $\rho$ of $\xi$, all of which satisfy $0<\Re\rho<1$
> (classical, unconditional).

**Proof.**  $\psi$ has poles exactly at the non-positive integers, so
$\psi(s/2)$ has poles exactly at $s\in-2\Z_{\ge0}$ and $\psi((1-s)/2)$ exactly
at $s\in1+2\Z_{\ge0}$; both sets lie in $\Z$.  Apply Theorem 1.2. $\square$

Note what Corollary 1.3 does **not** need: no cancellation argument between
the two summands of $A$ is required once the closed form is available.  The
poles of $\zeta'/\zeta(s)$ and of $\zeta'/\zeta(1-s)$ at a zero $\rho$ do in
fact cancel — that is the content of the collapse — but having Theorem 1.2 in
hand, holomorphy is read off the right-hand side directly.

> ### Corollary 1.4 (the Stage-2/3 assembly is prime-free)
> The Stage-2 object $\Phi(s)=\pi\cot\frac{\pi s}2-A(s)$ (108_38) satisfies
> \[
>  \Phi(s)=2\psi(1-s)-\tfrac12\psi\!\big(\tfrac s2\big)
>  -\tfrac12\psi\!\big(\tfrac{1-s}2\big)-\log4\pi,
> \]
> an elementary combination of digamma values.  Its poles are exactly the
> integers; its zeros are determined by $\Gamma$ alone.

**Proof.**  Substitute Theorem 1.2 into the definition of $\Phi$, giving
$\Phi(s)=\pi\cot\frac{\pi s}2+\frac12\psi(\frac s2)+\frac12\psi(\frac{1-s}2)
-\log\pi$.  Then apply the reflection $\psi(1-x)-\psi(x)=\pi\cot\pi x$ at
$x=s/2$ to replace $\pi\cot\frac{\pi s}2$ by $\psi(1-\frac s2)-\psi(\frac s2)$,
and the duplication $\psi(z)+\psi(z+\frac12)=2\psi(2z)-2\log2$ at
$z=\frac{1-s}2$ to replace $\psi(1-\frac s2)$ by
$2\psi(1-s)-2\log2-\psi(\frac{1-s}2)$.  Collecting terms and using
$2\log2+\log\pi=\log4\pi$ gives the stated form. $\square$

Verified to $7\times10^{-40}$ against both other expressions for $\Phi$ at
eight real and three complex arguments; $\Phi(1/2)=-2.2305907656358723438$,
matching 108_38 Theorem 3.2.

## 2. The strip: one zero, and it is simple

> ### Theorem 2.1
> On $(0,1)$,
> \[
>  \Phi'(s)=-\psi_1(1-s)-\tfrac14\psi_1\!\big(\tfrac s2\big)
>  -\tfrac14\psi_1\!\big(1-\tfrac s2\big)\;<\;0,
> \]
> where $\psi_1$ is the trigamma function.  Hence $\Phi$ is strictly
> decreasing on $(0,1)$.

**Proof.**  Differentiating Corollary 1.4 gives
$\Phi'(s)=-2\psi_1(1-s)-\frac14\psi_1(\frac s2)+\frac14\psi_1(\frac{1-s}2)$.
Differentiating the duplication formula once yields
$\psi_1(z)+\psi_1(z+\frac12)=4\psi_1(2z)$; at $z=\frac{1-s}2$ this reads
$\psi_1(\frac{1-s}2)+\psi_1(1-\frac s2)=4\psi_1(1-s)$, i.e.
$\frac14\psi_1(\frac{1-s}2)=\psi_1(1-s)-\frac14\psi_1(1-\frac s2)$.
Substituting collapses the $\psi_1(1-s)$ terms to a single one and gives the
displayed form.  For $s\in(0,1)$ the three arguments $1-s$, $s/2$ and
$1-s/2$ all lie in $(0,1)\subset(0,\infty)$, where
$\psi_1(z)=\sum_{n\ge0}(z+n)^{-2}>0$.  All three terms are therefore
strictly negative. $\square$

> ### Corollary 2.2
> $\Phi$ has **exactly one** zero in $(0,1)$, and it is **simple**:
> $s^*=0.301692388160422091519371\ldots$, with $\Phi'(s^*)\ne0$.

**Proof.**  As $s\to0^+$, only $-\frac12\psi(\frac s2)$ is singular and
$\Phi(s)\sim+1/s\to+\infty$; as $s\to1^-$, putting $u=1-s$, the singular part
is $2\psi(u)-\frac12\psi(u/2)\sim-2/u+1/u=-1/u\to-\infty$.  A strictly
decreasing continuous function running from $+\infty$ to $-\infty$ has
exactly one zero, and $\Phi'<0$ there makes it simple. $\square$

Both residues are $+1$: $\varepsilon\Phi(\varepsilon)\to1$ and
$\varepsilon\Phi(1+\varepsilon)\to1$, verified across
$\varepsilon=10^{-3},\dots,10^{-8}$.

> ### Corollary 2.3
> $\operatorname{rad}\Lambda^0$, restricted to the open strip, is
> **one-dimensional**, spanned by the single point mass $\delta_{s^*}$.

**Proof.**  108_38 Theorem 3.3 identifies the radical as the span of point
masses at zeros of $\Phi$; Corollary 2.2 says there is one such zero in
$(0,1)$. $\square$

This is a sharpening of 108_38, which recorded the radical only as "spanned
by point masses at the zeros of $\Phi$" without counting them.

## 3. What the collapse costs

> ### Proposition 3.1
> Let $\mathcal F$ be any functional of the arithmetic side whose value is a
> function of $s$ expressible as $c\cdot A(s)$ plus terms depending only on
> $\Gamma$ and elementary functions.  Then $\mathcal F$ is holomorphic at
> every zero of $\xi$, and its zero set, pole set and residues are
> independent of the location of the zeros of $\zeta$.

**Proof.**  Immediate from Theorem 1.2 and Corollary 1.3: such an
$\mathcal F$ equals an elementary function of $\Gamma$. $\square$

Three recorded consequences, each proved elsewhere, all instances of
Proposition 3.1:

| where | statement | consequence |
|---|---|---|
| Stage 2/3 | $\Phi$ prime-free (Cor. 1.4) | the assembly is an identity of $\Gamma$-functions |
| Stage 4 | the archimedean form has $n_+=\aleph_0$ unconditionally | no Hodge-index invariant to test |
| Stage 5 | $\operatorname{rad}\Lambda^0$ vs $\operatorname{rad}I_\partial$ | Condition III fails |

The Stage-5 entry is the sharpest.  $\operatorname{rad}I_\partial$ is
generated by the zeros of $\xi$ (107_240 Theorem D); $\operatorname{rad}
\Lambda^0$ is generated by $\delta_{s^*}$ with $s^*$ a root of an elementary
$\Gamma$-expression (Cor. 2.3).  By Proposition 3.1 the second cannot depend
on the first.

## 4. The design condition (synthesis, not a theorem)

> ### Symmetrization versus content
> **Summing a functional over the mirror orbit $\{s,1-s\}$ cancels its poles
> at the zeros of $\xi$.  Pairing two functionals across the mirror does not.**
>
> A construction that reaches well-posedness by *symmetrizing one object*
> under $s\mapsto1-s$ pays for it with the entire zero set.  A construction
> that reaches well-posedness by *pairing two objects* across the same
> involution keeps it.

The contrast is exact, and both sides of it are already in the programme.

* **Symmetrized (content destroyed).**  $A(s)=\zeta'/\zeta(s)+\zeta'/\zeta(1-s)$.
  At a zero $\rho$, the residues of the two summands are $+m_\rho$ and
  $-m_\rho$ and cancel.  Result: Theorem 1.2.
* **Paired (content preserved).**  The Weil scalar product
  $\langle f,g\rangle_W=\sum_\rho\widehat f(\rho)\widehat g(1-\bar\rho)$, and
  Stage 0's $I_\partial(D_f,D_g)=\widehat f(0)\overline{\widehat g(0)}
  +\widehat f(1)\overline{\widehat g(1)}-\sum_\rho\widehat f(\rho)
  \overline{\widehat g(\rho)}$ (107_240 Theorem D).  Here the involution
  relates the *two arguments*; nothing is summed over an orbit, no residues
  meet, and the zeros survive as coordinates — which is exactly why 107_241
  can compute a signature equivalent to RH.

So the two halves of the programme differ by precisely this: Stage 0 pairs,
Stages 2–4 symmetrize.  That is the mechanism behind Stage 5's impossibility,
and it is visible without doing Stage 5's work.

### 4.1 Retrodictions

Applied backwards, the condition predicts what was found:

1. Stage 1's divergent constant was removed by passing to **mass-zero
   differences** (108_33) — a symmetrizing move.  Prediction: the resulting
   pairing is arithmetically empty.  Found: Corollary 1.4.
2. Stage 4's polar page cancels identically under $s\mapsto1-s$ (108_39
   Theorem 2.1).  Prediction: the polar data carries no invariant.  Found:
   the block is hyperbolic, signature $(1,1)$, contributing $0$.
3. Stage 5's Condition III asks a symmetrized radical to match a paired
   radical.  Prediction: mismatch.  Found: proved mismatch.

These are retrodictions, not tests.  The condition earns its keep only if it
constrains Stage 6, which is §4.2.

### 4.2 The pre-test for Stage 6

Stage 6 is the primitive inequality — row (d), the Hodge-index step.  The
condition says:

> **Do not symmetrize the arithmetic side before pairing.**  Stage 6 must
> pair $f$ against $g$ across the mirror, keeping $\widehat f(\rho)$ and
> $\overline{\widehat g(\rho)}$ as separate coordinates.  Any step that
> replaces a two-argument pairing by a one-argument symmetrized functional
> discards the zeros, and by Proposition 3.1 the resulting object provably
> cannot detect them.

A concrete consequence, and the reason this matters rather than being a
slogan: 107_241 Corollary 3.4's primitive form
$Q(f)=-\sum_\rho m_\rho\widehat f(\rho)\overline{\widehat f(\rho')}$ is
**quadratic in one function but is not a symmetrization** — it evaluates
$\widehat f$ at $\rho$ and at the mirror point $\rho'$ *simultaneously* and
multiplies them, rather than summing a fixed functional over the orbit.  That
distinction is the whole game, and Stage 6 must preserve it.

## 5. Scope

**Proved here.** Theorem 1.2 and Corollaries 1.3, 1.4 (the collapse and the
closed form); Theorem 2.1 and Corollaries 2.2, 2.3 (monotonicity on the
strip, uniqueness and simplicity of $s^*$, one-dimensionality of the
restricted radical); Proposition 3.1.

**Read from source, not re-derived.** $\xi(s)=\xi(1-s)$ and the entirety of
$\xi$ (classical); the reflection and duplication formulas for $\psi$ and
their once-differentiated forms (classical); $\psi_1>0$ on $(0,\infty)$
(classical, from the series); 108_39 Theorem 2.1; 108_38 Theorems 3.2, 3.3;
107_240 Theorem D; 107_241 Theorem 3.1 and Corollaries 3.3, 3.4;
$0<\Re\rho<1$ for all zeros of $\xi$ (classical, unconditional).

**Verified numerically.** The three expressions for $\Phi$ agreeing to
$7\times10^{-40}$; the collapsed derivative of Theorem 2.1 against numerical
differentiation to $5\times10^{-29}$; strict negativity of $\Phi'$ across
$(0,1)$; a single sign change on a $500$-point grid; the residues $+1$ at
$s=0,1$ by refinement; $\Phi(1/2)$ and $s^*$ against 108_38.

**Not established, and explicitly not claimed.**

* §4 is a synthesis, exactly as 108_90 §0 says of its own condition.  It has
  retrodictive support and one forward prediction (§4.2); it is not a
  theorem and nothing is derived from it.
* That the collapse is *unavoidable* — Theorem 1.2 says symmetrizing $\zeta'/
  \zeta$ destroys the zeros, not that every route to well-posedness must
  symmetrize.  Whether a non-symmetrizing route to Stage 1's well-posedness
  exists is **open**, and is the natural thing to ask next.
* Anything about $\RH$.  `ROW_A_STATUS` is not promoted.

## 6. Verifier

`108_91_the_symmetrization_collapse.py` checks: Theorem 1.2 at real and
complex arguments, computing $A(s)$ from $\zeta'/\zeta$ and the right-hand
side from $\psi$, by independent code paths; Corollary 1.3 by evaluating
$A$ at the first five zeros of $\zeta$ and confirming finiteness, against a
control showing each individual summand blows up there; Corollary 1.4's
closed form against both other expressions for $\Phi$; Theorem 2.1's
collapsed derivative against numerical differentiation with a step-halving
convergence test, and its strict negativity on a grid; Corollary 2.2 by
bracketing the unique sign change and confirming the residues converge to
$+1$ under refinement of $\varepsilon$ (not a bare threshold); and
$\psi_1>0$ on the three relevant argument ranges.
