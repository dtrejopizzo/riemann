# 109.04 — The coefficient side is blind, for every kernel

## 0. Why this note exists

109_01 Definition 1.1 calls its pairing "canonical … literally forced …
no free parameter is chosen here."  **That overstates it.**  What is forced
is only that a *single* linear functional has one rank-one square.  The
actual choice made in 109_01 is to assemble the individual squares
**diagonally**, i.e. to pair $\Gamma_{p,k}(f)$ against $\Gamma_{p,k}(g)$ at
the *same* index.  A general bilinear form built from the same functionals is
\[
 B_K(f,g)=\sum_{n,m\ge2}K(n,m)\,f(n)\,g(m),
\]
and 109_01 took $K(n,m)=\Lambda(n)\delta_{nm}$.  That is a choice, not a
consequence, and 109_02's verdict — that $\operatorname{rad}B$ is
prime-power-determined — is therefore, as stated there, a fact about one
kernel.

This note repairs the overstatement in the only way that is worth anything:
by proving the conclusion for **every** kernel.  The result is stronger than
109_02's, and it does not depend on the disputed word "forced".

## 1. The theorem

> ### Theorem 1.1 (the coefficient side is blind)
> Let $K:\{n\ge2\}^2\to\C$ be **any** kernel supported on prime powers, and
> let $B_K(f,g)=\sum_{n,m}K(n,m)f(n)g(m)$ on any domain where the sum
> converges absolutely.  Put
> \[
>  Z:=\{f:\ f(p^k)=0\ \text{for every prime }p\text{ and every }k\ge1\}.
> \]
> Then $Z\subseteq\operatorname{rad}B_K$.

**Proof.**  If $f\in Z$ then $f(n)=0$ at every $n$ in the support of $K$, so
every term $K(n,m)f(n)g(m)$ vanishes and $B_K(f,g)=0$ for all $g$.  $\square$

The proof is one line, and that is the point: it uses nothing about $K$.

> ### Theorem 1.2 (the witness)
> $F(x):=\sin(\pi x)$ is a nonzero element of $Z$, and its Mellin transform
> \[
>  \widehat F(s)=\int_0^\infty\sin(\pi x)\,x^{s-1}\dd x
>  =\pi^{-s}\,\Gamma(s)\,\sin\!\big(\tfrac{\pi s}2\big),
>  \qquad 0<\Rel s<1,
> \]
> **vanishes at no zero of $\xi$.**

**Proof.**  $F(n)=\sin(\pi n)=0$ for every integer $n$, in particular at
every prime power, so $F\in Z$; and $F\not\equiv0$.  For the transform:
$\Gamma$ has no zeros anywhere, $\pi^{-s}$ is zero-free, and
$\sin(\pi s/2)=0$ exactly at $s\in2\Z$.  Every zero $\rho$ of $\xi$ satisfies
$0<\Rel\rho<1$ (classical, unconditional), so $\rho\notin2\Z$ and
$\widehat F(\rho)\ne0$. $\square$

Verified: $|\sin(\pi n)|<5\times10^{-30}$ at ten prime powers, and
$|\widehat F(\rho)|=0.70710678\ldots$ at each of the first six zeros.

That constant value is not an artifact, and it is not an asymptotic either.

> ### Lemma 1.2$'$ (exact modulus on the critical line)
> $\big|\widehat F(\tfrac12+it)\big|=\tfrac1{\sqrt2}$ for **every** real $t$.

**Proof.**  $|\pi^{-1/2-it}|=\pi^{-1/2}$; the classical reflection value
$|\Gamma(\tfrac12+it)|^2=\pi/\cosh(\pi t)$; and
\[
 \Big|\sin\Big(\tfrac\pi4+\tfrac{i\pi t}2\Big)\Big|^2
 =\sin^2\tfrac\pi4+\sinh^2\tfrac{\pi t}2
 =\tfrac12+\sinh^2\tfrac{\pi t}2
 =\tfrac12\Big(1+2\sinh^2\tfrac{\pi t}2\Big)
 =\tfrac{\cosh(\pi t)}2 ,
\]
the last step by $\cosh(\pi t)=1+2\sinh^2(\pi t/2)$.  Multiplying,
$|\widehat F(\tfrac12+it)|^2=\pi^{-1}\cdot\frac{\pi}{\cosh\pi t}
\cdot\frac{\cosh\pi t}2=\frac12$. $\square$

So on the critical line the witness's transform has **constant** modulus
$1/\sqrt2$: it is not merely nonzero at the zeros of $\xi$, it is bounded
away from zero along the whole line, uniformly in $t$.  Corollary 1.3 below
therefore does not depend on where the zeros happen to lie — it would hold
for any hypothetical zero on the critical line, and (by continuity of
$\widehat F$ and non-vanishing of $\Gamma$ off $2\Z$) for off-line zeros too.

> ### Corollary 1.3
> For every kernel $K$ supported on the prime powers,
> $\operatorname{rad}B_K$ is **not** contained in the zero-determined space
> $\{f:\widehat f(0)=\widehat f(1)=0,\ \widehat f(\rho)=0\ \forall\rho\}$ of
> 107_240 Theorem D.

**Proof.**  $F\in Z\subseteq\operatorname{rad}B_K$ by Theorems 1.1–1.2, while
$\widehat F(\rho)\ne0$. $\square$

## 2. What this actually says

> **The zeros of $\zeta$ are not in the coefficients $\Lambda(n)$.  They are
> in the analytic continuation of $\sum_n\Lambda(n)n^{-s}$.**

A pairing that reads its arguments only through their values at the prime
powers is reading the coefficient sequence.  No such pairing can see the
zeros, because the zeros are not a property of that sequence — they are a
property of the continued function.  This is why Theorem 1.1 needs no
hypothesis on $K$: the blindness is not a defect of a particular
construction, it is a feature of the *side of the transform* the
construction lives on.

Stage 0's pairing escapes this because it reads $f$ through $\widehat f(\rho)$
— evaluation of the continuation *at* the zeros.  That is a genuinely
different kind of access to $f$.

## 3. The corrected trichotomy

The phase-108 diagnosis (108_91) said: symmetrizing destroys the zeros,
pairing across the mirror preserves them.  That was right but incomplete,
and it is what motivated phase 109's hypothesis.  With Theorem 1.1 the
picture is:

| pairing | side of the transform | mirror | sees the zeros? |
|---|---|---|---|
| phase 109, one-sided | **coefficient** | — | **no** — Thm 1.1, any kernel |
| Stage 2, two-sided | continuation | symmetrized | **no** — collapses to $\Gamma$ (108_91) |
| Stage 0, corner | continuation | paired, not summed | **yes** — but defined via the explicit formula, hence circular |

So one-sidedness was **not** the operative variable.  Two things are needed
at once, and phase 109 supplied only the second:

1. the pairing must live on the **continuation** side, reading $\widehat f$
   at points, not $f$ at prime powers;
2. it must pair across the mirror rather than sum over it.

Row (a)'s target is therefore sharper than before: **a continuation-side,
non-symmetrized pairing whose definition does not invoke the zeros.**  Only
the third row of the table has properties (1) and (2), and it fails the
zero-free requirement — which is exactly 107_240 §4.1's observation that the
radical of the corner pairing is zero-determined, restated as a design
target rather than an obstruction.

## 4. Consequence for the phase-109 hypothesis

The hypothesis tested by phase 109 was that excluding the identity shell
($k\ge1$ only) would evade the divergence that closed Stage 1 while
retaining the zeros.  Outcome, in two parts:

* **The first half held.**  109_01 Theorem 2.1: a genuine, absolutely
  convergent, bilinear pairing exists on the one-sided data, and the
  identity-shell obstruction of 108_17 does not arise. That was a real and
  non-obvious possibility, and it is now settled affirmatively.
* **The second half failed, and could not have held.**  The retained object
  $-\zeta'/\zeta(s)$ has poles at the zeros, but the *pairing* built from
  the same shells reads only coefficients, and by Theorem 1.1 no kernel on
  that data sees the zeros. The hypothesis conflated "the assembled
  Dirichlet series has poles at the zeros" with "the pairing detects the
  zeros"; those are statements about opposite sides of the Mellin transform.

## 5. Scope

**Proved here.** Lemma 1.2$'$ (exact modulus on the critical line); Theorem 1.1 (blindness, for every kernel supported on the
prime powers); Theorem 1.2 (the witness and its transform); Corollary 1.3.

**Read from source, not re-derived.** 107_240 Theorem D (the zero-determined
radical); 108_91 (the symmetrization collapse); 109_01 Definitions 1.1–1.3
and Theorem 2.1; 108_17 (the identity-shell criterion); the Mellin transform
$\int_0^\infty\sin(x)x^{s-1}\dd x=\Gamma(s)\sin(\pi s/2)$ on $0<\Rel s<1$
(classical); $0<\Rel\rho<1$ for zeros of $\xi$ (classical, unconditional);
$\Gamma$ is zero-free (classical).

**Verified numerically.** Vanishing of $\sin(\pi n)$ at ten prime powers;
non-vanishing of $\widehat F$ at the first six zeros of $\xi$; Lemma 1.2$'$'s
exact constant modulus $1/\sqrt2$ across $t\in[0.5,640]$ at fixed precision,
together with the hyperbolic identity its proof uses; the closed
form of $\widehat F$ against accelerated oscillatory quadrature (agreement
to within the truncation error of a conditionally convergent integral);
Theorem 1.1 directly, on random non-diagonal kernels.

**Not established, and explicitly not claimed.** That no continuation-side
zero-free pairing exists — §3 states that as the *target*, not as a proved
impossibility, and nothing here bears on whether one can be built. That
109_01's pairing is uninteresting for other purposes; only its radical is at
issue. Anything about $\RH$: no zero of $\xi$ enters any definition here,
and no claim about the location of zeros is made.

`ROW_A_STATUS` unchanged. Nothing here bears on $\RH$.

## 6. Verifier

`109_04_the_coefficient_side_is_blind.py` checks: that $\sin(\pi n)$
vanishes at ten prime powers to $5\times10^{-30}$; that
$\widehat F(\rho)\ne0$ at the first six zeros, with a control clause
confirming the test would detect a vanishing transform (it does, at $s=2$);
Lemma 1.2$'$'s exact identity $|\widehat F(\tfrac12+it)|=1/\sqrt2$ across six
values of $t$ spanning three decades, with a control clause rejecting the
plausible wrong values $1$ and $\tfrac12$; and
Theorem 1.1 itself on **random non-diagonal kernels** supported on prime
powers, confirming $B_K(F,g)=0$ exactly for randomly drawn $g$ — the point
being that the conclusion does not depend on the diagonal choice.
