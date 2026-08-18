# 108.13 — Route A: the phase-space counterterm does not absorb $\sum_p C_p$

## 0. Result

108_12 left one open item: $\sum_p C_p$ diverges, both naively and after the
local $\log p$-scale regularization (108_12 Theorem 3.1, Corollary 3.2). One
structurally plausible candidate to absorb it, already present in the
program, is the counterterm $-2h(1)\log\Lambda$ of 107_239 (1.4), which is
$a$-independent and proportional to a value at $1$ — the same shape as
$\sum_p C_p$. This note tests that candidate directly.

> **The two divergences are incommensurate: the counterterm grows linearly
> in $T=\log\Lambda$, while the natural partial sums of $\sum_p C_p$ grow
> at least like $\pi(e^T)\sim e^T/T$ — exponentially in $T$. No fixed
> nonzero constant can make one absorb the other in the limit. Route A is
> discarded.**

This conclusion is exactly the "likely outcome" flagged when the route was
proposed; it is now a proved statement rather than a guess. No zero of
$\xi$ is used anywhere.

## 1. The two objects, precisely

**The counterterm (107_239 (1.4), (3.1)-(3.2)).** For $h$ compactly
supported with $\operatorname{supp}h\subset[e^{-T},e^T]$, 107_239 defines

\[
 \mathfrak T_S(h)=\lim_{\Lambda\to\infty}
 \Big(\operatorname{Tr}(\theta(h)R_\Lambda)-2h(1)\log\Lambda\Big),
\]

and shows (3.1)-(3.2) that once $S\supset S(h):=\{\infty\}\cup\{p\le e^T\}$
the finite remainder stabilizes, so the effective object at scale $T$ is
built from primes $p\le e^T$ and a counterterm

\[
 \kappa(T):=2h(1)\log\Lambda=2h(1)\,T,
\]

**linear in $T$**, for a fixed test value $h(1)$.

**The prime sum (108_12).** $\sum_p C_p$ is a sum over *all* primes of a
quantity whose raw value is $+\infty$ (108_12 Theorem 2.1) and whose
natural regularized scale is $\log p$ (108_12 §3). The set of primes that
can plausibly be paired with the same cutoff $T$ is exactly $S(h)\setminus
\{\infty\}=\{p\le e^T\}$, the same set that stabilizes the counterterm.
Write

\[
 \sigma(T):=\sum_{p\le e^T} C_p^{\mathrm{reg}}
\]

for *any* regularization of the individual $C_p$ consistent with 108_12's
findings, in the sense of Hypothesis 2.1 below.

## 2. The growth rates

> ### Hypothesis 2.1 (consistency with 108_12)
> There is $c_0>0$ and $p_0$ such that $C_p^{\mathrm{reg}}\ge c_0$ for all
> primes $p\ge p_0$.

This is not an extra assumption pulled from nowhere: it is the *weakest*
reading of 108_12's own results. Theorem 2.1 gives the raw value
$C_p=+\infty$ (certainly $\ge c_0$ for any $c_0$). The regularized scale of
§3 is $\propto\log p\to\infty$, which for $p\ge p_0:=3$ already exceeds any
fixed $c_0$. Hypothesis 2.1 is implied by either reading; it isolates the
one feature that drives the argument below, so that the conclusion does not
depend on settling the open question of *which exact* regularization is
"Tate's."

> ### Lemma 2.2 (the counterterm is linear)
> $\kappa(T)=2h(1)T$ exactly, for every $T$.

**Proof.** Immediate from the definition. $\square$

> ### Theorem 2.3 (Chebyshev)
> $\theta(x):=\sum_{p\le x}\log p$ satisfies $\theta(x)=\Theta(x)$; more
> precisely there are absolute constants $0<c_1\le c_2$ with
> $c_1x\le\theta(x)\le c_2x$ for $x\ge2$. Consequently
> $\pi(x):=\#\{p\le x\}=\Theta(x/\log x)$.

**Proof.** Classical (Chebyshev, via binomial coefficient bounds); already
invoked in 108_12 Theorem 3.1 for the same function $\theta$. $\square$

> ### Theorem 2.4 (the prime side grows exponentially in $T$)
> Under Hypothesis 2.1, for $T$ large,
> \[
>  \sigma(T)\;\ge\;c_0\,\pi(e^T)\;=\;\Theta\!\Big(\frac{e^T}{T}\Big).
> \]

**Proof.** $\sigma(T)=\sum_{p\le e^T}C_p^{\mathrm{reg}}\ge c_0\cdot
\#\{p\le e^T\}=c_0\pi(e^T)$ for $e^T\ge p_0$, and $\pi(e^T)=\Theta(e^T/T)$
by Theorem 2.3 with $x=e^T$. $\square$

## 3. Incommensurability

> ### Theorem 3.1
> For every fixed nonzero constant $\kappa_0$, $\sigma(T)\ne\kappa_0\,
> \kappa(T)+O(1)$ as $T\to\infty$; more strongly,
> \[
>  \frac{\sigma(T)}{\kappa(T)}\;\longrightarrow\;+\infty .
> \]

**Proof.** By Lemma 2.2, $\kappa(T)=2h(1)T$, a fixed linear function of $T$
(assume $h(1)\ne0$; if $h(1)=0$ the counterterm vanishes identically and
manifestly cannot absorb a term that Hypothesis 2.1 shows is unbounded, so
the claim is even more immediate). By Theorem 2.4,
$\sigma(T)/T\ge c_0\pi(e^T)/T=\Theta(e^T/T^2)\to\infty$. Hence
$\sigma(T)/\kappa(T)=\big(\sigma(T)/T\big)\big/(2h(1))\to\infty$. In
particular no fixed $\kappa_0$ can satisfy $\sigma(T)=\kappa_0\kappa(T)+O(1)$,
since the left side eventually exceeds any fixed multiple of the right.
$\square$

### Corollary 3.2 (Route A discarded)

The counterterm of 107_239 (1.4) and the prime sum $\sum_p C_p$ of 108_12,
evaluated over the matching, self-consistent cutoff $T\mapsto\{p\le e^T\}$
that 107_239 §3 itself prescribes, are asymptotically incommensurate: one is
linear in $T$, the other grows at least like $e^T/T$. Identifying the two —
"the counterterm absorbs $\sum_pC_p$" — is therefore false for every
regularization of the individual $C_p$ consistent with 108_12's findings
(Hypothesis 2.1). This is not a failure to find the right normalization; it
is a structural mismatch between a phase-space cutoff (linear counterterm)
and a prime-indexed divergence (exponential partial sums by Chebyshev).

## 4. What this does and does not settle

**Proved here.** The growth-rate mismatch (Theorem 3.1), robust to the
choice of regularization of individual $C_p$'s under the minimal Hypothesis
2.1, which itself follows from either reading of 108_12.

**Not addressed.** Whether *some other* pairing of cutoffs (not the
$T\mapsto\{p\le e^T\}$ correspondence that 107_239 §3 itself supplies)
could match the two growth rates. No such alternative correspondence is
suggested anywhere in the cited sources, and inventing one without textual
support would not be a use of 107_239 as written. The route is discarded on
the correspondence the source text actually defines.

Whether $\mathfrak T_S(f_a)$, evaluated by the *operator trace* route of
(1.4) directly (rather than via the arithmetic-side sum (2.1)), converges to
something finite for $h=f_a$ is not addressed; (1.4) is stated in 107_239
for compactly supported $h$, and $f_a\notin\mathcal A$ is not compactly
supported (108_05 Proposition 2.1), so (1.4) does not directly apply to
$f_a$ without further work not undertaken here.

`ROW_A_STATUS` remains `partial`. Nothing here bears on RH.

## 5. Verifier

`108_13_route_a_counterterm_incommensurate.py` independently recomputes
$\theta(e^T)$ by sieve for a range of $T$, fits $\log\theta(e^T)$ as a
linear function of $T$ (expecting slope $\approx1$, i.e. $\theta(e^T)\sim
e^{1\cdot T}$, matching Theorem 2.3) by threshold-free regression, computes
$\pi(e^T)$ directly by counting, and compares the *ratio*
$\pi(e^T)/T$ against the counterterm's exact linear profile $T$, showing the
ratio's own growth is unbounded (checked by monotonicity and a second
regression, not a fixed threshold). It also checks the Chebyshev two-sided
bound $c_1x\le\theta(x)\le c_2x$ with explicit constants over the sampled
range.
