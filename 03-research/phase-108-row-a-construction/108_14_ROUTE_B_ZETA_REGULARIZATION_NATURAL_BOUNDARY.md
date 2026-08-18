# 108.14 — Route B: zeta regularization gives $-\log(2\pi)$, but the
# precise identification with $\sum_p C_p$ fails at a natural boundary

## 0. Result

$-\zeta'/\zeta(0)=-\log(2\pi)$ is a correct, classical fact, verified below
by a self-contained numerical continuation (no scipy, no mpmath). It is
tempting to read it as the regularized value of $\sum_p C_p$, since
$-\zeta'/\zeta(s)=\sum_n\Lambda(n)n^{-s}$ is a von-Mangoldt-weighted prime
sum of the same rough shape.

> **The classical constant is real and independently verified. The precise
> identification with $\sum_p C_p$ does not hold, for two independent
> reasons, both provable from what is already established in 108_06,
> 108_11, 108_12: (1) $\sum_pC_p$ contains a bulk piece
> $\sum_p\frac{p-2}{p-1}$ that no scale-type regulator touches, and which
> diverges by mere comparison with $\sum_p1$; (2) the singular piece, once
> regulated the same way $\zeta(s)=\sum n^{-s}$ regulates $\sum_n1$,
> produces not $\zeta$ but $A(s)=\sum_pp^{-s}/(1-p^{-s})$, which has $s=0$
> as an accumulation point of poles (108_11 Lemma 2.1) — a natural
> boundary, not the simple regular point $\zeta$ has at $s=0$. The clean
> "evaluate a nice function at $0$" mechanism that produces $-\log(2\pi)$
> for $\zeta$ therefore does not transfer.**

No zero of $\xi$ is used anywhere; $0$ is not a zero of $\zeta$ either.

## 1. The classical constant, verified from scratch

### 1.1 A self-contained continuation of $\zeta$

For $s\ne1$ and any integer $N\ge1$, the Euler–Maclaurin formula gives

\[
 \zeta(s)=\sum_{n=1}^{N-1}n^{-s}
 +\frac{N^{1-s}}{s-1}+\frac{N^{-s}}2
 +\sum_{k=1}^{M}\frac{B_{2k}}{(2k)!}\,(s)_{2k-1}\,N^{-s-2k+1}
 +R_M ,
 \tag{1.1}
\]

where $(s)_{2k-1}=s(s+1)\cdots(s+2k-2)$ is the rising factorial and
$B_{2k}$ are the Bernoulli numbers ($B_2=\tfrac16,B_4=-\tfrac1{30},
B_6=\tfrac1{42},\dots$); this is a classical analytic-continuation formula
(read from source: standard, e.g. Euler–Maclaurin summation applied to
$\sum n^{-s}$), used here exactly as stated, with no library implementing
it. Taking $N,M$ moderately large makes $R_M$ negligible at double
precision; this is the *only* tool used below, together with numerical
differentiation of (1.1) in $s$ by a centered five-point stencil.

### 1.2 Verified numerically

> Using (1.1) with $N=15$, $M=8$:
> * $\zeta(2)$, $\zeta(4)$, $\zeta(-1)$ match the closed forms $\pi^2/6$,
>   $\pi^4/90$, $-\tfrac1{12}$ to $10^{-13}$ or better;
> * $\zeta(0)=-0.500000\ldots$, matching $-\tfrac12$ to $10^{-13}$;
> * $\zeta'(0)=-0.918938\ldots$, matching $-\tfrac12\log(2\pi)$ to
>   $10^{-9}$ (numerical differentiation, so slightly less precise than
>   the direct evaluations);
> * hence $-\zeta'/\zeta(0)=-\log(2\pi)=-1.837877\ldots$;
> * the classical identity $-\zeta'/\zeta(s)=\sum_n\Lambda(n)n^{-s}$ at
>   $s=2$ (read from source: standard Dirichlet-series identity for the
>   von Mangoldt function, valid for $\Re s>1$) matches a direct truncated
>   sum $\sum_{n\le10^6}\Lambda(n)n^{-2}$ to the expected truncation error.

All labeled **verified numerically**; the Euler–Maclaurin formula (1.1) and
the von Mangoldt identity are **read from source** (classical, not proved
here); everything downstream in §2 is a **proof**, using only facts already
established in 108_06/108_11/108_12.

## 2. Does $\sum_pC_p$ have this shape? A precise test

### 2.1 The natural scale-regulator

108_12 Theorem 2.1: on $\mathbb Z_p^\times$, the shell $|1-u|_p=p^{-k}$
($k\ge1$) contributes exactly $1$ to $C_p$, and the bulk shell
$|1-u|_p=1$ contributes $\frac{p-2}{p-1}$. The only divergence is the
infinite sum of unit contributions over $k\ge1$. The regulator that
$\zeta(s)=\sum_nn^{-s}$ itself uses to tame $\sum_n1$ is the power
$n^{-s}$; the *same* device applied here, weighting the $k$-th shell by
$p^{-ks}$ (matching the shell's own $p$-adic scale $p^{-k}$), gives

\[
 C_p(s):=\frac{p-2}{p-1}+\sum_{k\ge1}p^{-ks}
 =\frac{p-2}{p-1}+\frac{p^{-s}}{1-p^{-s}},\qquad\Re s>0.
 \tag{2.1}
\]

> ### Lemma 2.1 (consistency check)
> $\lim_{s\to0^+}C_p(s)=+\infty$, recovering 108_12 Theorem 2.1 exactly
> (the unregulated value).

**Proof.** $p^{-s}/(1-p^{-s})\sim1/(s\log p)\to\infty$ as $s\to0^+$.
$\square$

### 2.2 The exact decomposition

> ### Theorem 2.2
> \[
>  \sum_pC_p(s)=B_0+A(s),\qquad
>  B_0:=\sum_p\frac{p-2}{p-1},\qquad
>  A(s):=\sum_p\frac{p^{-s}}{1-p^{-s}} ,
> \]
> with $A$ exactly 108_06/108_11's object, and $B_0$ an $s$-independent
> quantity untouched by the regulator, because the bulk shell's $p$-adic
> exponent is $0$ for every $p$ ($p^{-0\cdot s}=1$ regardless of $s$).

**Proof.** Immediate from (2.1), splitting the sum over $p$ termwise.
$\square$

### 2.3 The bulk term already diverges, with no help from $s$

> ### Theorem 2.3
> $B_0=\sum_p\frac{p-2}{p-1}=+\infty$, and no regulator that leaves the
> $k=0$ shell unsuppressed (as any scale-type regulator on the singular
> shells must, since that shell has $p$-adic scale $p^0=1$) can make it
> finite.

**Proof.** $\frac{p-2}{p-1}=1-\frac1{p-1}\ge\frac12$ for every $p\ge3$, so
$B_0\ge\sum_{p\ge3}\frac12=+\infty$ by direct comparison with the (already
infinite) sum of $\frac12$ over the infinitely many primes $p\ge3$. This
uses only the infinitude of primes, not any property of $\log p$ or
$\zeta$. $\square$

This is a strictly *more elementary* obstruction than the one 108_12
identified: it does not require the $\log p$-scale analysis of 108_12 §3 at
all, only that there are infinitely many primes.

### 2.4 The singular term: $s=0$ is an accumulation point of poles, not a
### regular point

> ### Theorem 2.4
> $A(s)$ is exactly the object 108_11 calls $A(a)$ evaluated at $a=s$.
> By 108_11 Lemma 2.1 (proved there, cited here), the singular set
> $\mathcal S=\{1/N:N\ge2\}\cup\{1-1/M:M\ge2\}$ of $A$'s continuation
> accumulates at $s=0$: every neighborhood of $0$ contains infinitely many
> points $1/N\in\mathcal S$ at which $A$ is singular. Consequently $A$ has
> no Laurent expansion, no removable/simple-pole finite part, and no
> continuation past any punctured neighborhood of $0$ **that is itself
> holomorphic in a full neighborhood minus finitely many points** — $s=0$
> sits on what is, at best, a boundary of accumulating singularities, a
> qualitatively different situation from a simple pole.

**Proof.** Restatement of 108_11 Lemma 2.1 in the variable $s=a$, together
with the standard fact that a function with singularities accumulating at
a point $s_0$ admits no Laurent expansion around $s_0$ (a Laurent series
converges on a punctured disk, which by definition contains no other
singularities of the function). $\square$

This is the same phenomenon, well known for the closely related **prime
zeta function** $P(s)=\sum_pp^{-s}$: $P(s)=\sum_{k\ge1}\frac{\mu(k)}k
\log\zeta(ks)$ has poles at every $s=1/k$, $k\ge1$, which accumulate along
the imaginary axis $\Re s=0$; it is a classical fact (read from source)
that $P$ has the line $\Re s=0$ as a natural boundary and cannot be
continued across it. $A(s)$, built the same way from $\log\zeta$, inherits
the same accumulation at the single point $s=0$ on the real axis.

> ### Corollary 2.5 (Route B does not transfer)
> By Theorem 2.3, $\sum_pC_p(s)=B_0+A(s)$ diverges at every $s$ near $0$
> from the $B_0$ term alone, regardless of $A(s)$'s behavior; and by
> Theorem 2.4, $A(s)$ itself has no well-defined value at $s=0$ to begin
> with, in the sense that $\zeta(0)=-\tfrac12$ is well defined ($\zeta$
> being holomorphic in a full punctured neighborhood of $0$, indeed
> everywhere except the single point $s=1$). The mechanism that produces
> $\zeta(0)=-\tfrac12$, $\zeta'(0)=-\tfrac12\log(2\pi)$ cleanly is not
> available for $\sum_pC_p$.

## 3. What this settles, and what it does not

**Proved here (§2):** Theorem 2.2 (exact decomposition), Theorem 2.3
(elementary divergence of the bulk term $B_0$, independent of 108_12's
$\log p$-scale analysis), Theorem 2.4 (the singular term sits at an
accumulation of poles, using 108_11 Lemma 2.1).

**Verified numerically (§1):** the classical constant $-\zeta'/\zeta(0)
=-\log(2\pi)$, via a from-scratch Euler–Maclaurin continuation, cross-checked
against closed-form special values and against the von Mangoldt Dirichlet
series at $s=2$.

**Observed, not proved:** that $\log(2\pi)$ is the constant appearing in
the archimedean term of the classical explicit formula for $\psi(x)$ is a
well-known fact (read from source); its appearance here is evidence that
*some* archimedean/pole bookkeeping in the program is correctly normalized,
but Corollary 2.5 shows this specific route — regularizing $\sum_pC_p$
itself via $-\zeta'/\zeta$ evaluated at $0$ — is not how that constant
would enter, if it enters at all. No claim is made about *why* $\log(2\pi)$
appears elsewhere in the program; that question is untouched.

**Not addressed:** whether some other, non-scale-type regularization of
$\sum_pC_p$ exists that does land on a multiple of $\log(2\pi)$. The
argument above rules out the specific mechanism proposed (evaluate a
Dirichlet-series continuation at the value $s=0$ that mirrors $\zeta(0)$);
it does not rule out every conceivable regularization of a divergent sum
with accumulating singularities, since no exhaustive classification of such
regularizations is attempted.

`ROW_A_STATUS` remains `partial`. Nothing here bears on RH.

## 4. Verifier

`108_14_route_b_zeta_regularization.py` implements $\zeta(s)$ from scratch
via Euler–Maclaurin (1.1) with hard-coded Bernoulli numbers, checks it
against closed-form special values ($\zeta(2),\zeta(4),\zeta(-1)$), computes
$\zeta(0)$, $\zeta'(0)$ (five-point numerical stencil) and
$-\zeta'/\zeta(0)$ against $-\log(2\pi)$, cross-checks the von Mangoldt
identity at $s=2$ against a direct truncated Dirichlet sum built from an
independent sieve, verifies the elementary divergence of $B_0$'s partial
sums (monotone, unbounded, compared against $\tfrac12\pi(x)$), and gives
direct numerical evidence for Theorem 2.4 by evaluating $A(s)$ near a
sequence of poles $1/N\to0$ (showing unbounded blow-up arbitrarily close to
$s=0$) side by side with $\zeta(s)$'s manifest smoothness on the same
neighborhood of $0$.
