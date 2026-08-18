# 113.01 — The local integral $\int'_{\mathbb Q_p^\times}h(u^{-1})/|1-u|_p\,d^\times u$ for Schwartz $h$

## 0. Setting and the question

Throughout, $h(u):=h(|u|_p)$ is the module pullback (107_239 §3, 108_06 §3)
of a function $h:\mathbb R_+^\times\to\mathbb C$ with $\tilde h(x):=h(e^x)$
Schwartz on $\mathbb R$, possibly in the exponential-decay subclass
$\mathcal S_\eta$ of 111_00 §1. Write $\varphi(u):=h(u^{-1})$, so on the shell
$|u|_p=p^{-n}$, $\varphi$ takes the value $h(p^n)=\tilde h(n\log p)$ —
constant on every shell, exactly as in 108_17 Definition 1.1, **except that
$\varphi$ is generally nonzero on infinitely many shells**, since Schwartz
$h$ need not have compact support. This is the one structural difference
from 108_17's setting that must be tracked through every step below.

## 1. The shell decomposition, with infinitely many nonzero shells

> ### Lemma 1.1 (closed form, general $h$)
> For $\Re$ purposes of absolute convergence assume $\tilde h\in\mathcal
> S_\eta$ for some $\eta>0$ (the weakest hypothesis used anywhere in this
> note). Then
> $$A(h):=\sum_{n\ge1}h(p^n),\qquad B_p(h):=\sum_{m\ge1}h(p^{-m})p^{-m}$$
> converge absolutely, for **every** $\eta>0$ — no exponential-decay margin
> beyond strict positivity is needed, and in fact bare Schwartz decay
> (polynomial in $x$, no exponential rate at all) already suffices for each
> **individually** (Remark 1.2).

**Proof.** $\tilde h\in\mathcal S_\eta$ gives $|\tilde h(x)|\le C_1
e^{-\eta|x|}$ for all $x$ (absorbing the polynomial factor into a single
constant, since we only need one $N$ here). For $A(h)$: $|h(p^n)|=|\tilde
h(n\log p)|\le C_1p^{-\eta n}$, geometric, summable since $0<p^{-\eta}<1$.
For $B_p(h)$: $|h(p^{-m})p^{-m}|\le C_1p^{-\eta m}p^{-m}=C_1p^{-(\eta+1)m}$,
even faster. $\square$

> **Remark 1.2 (bare Schwartz already suffices locally).** If $\tilde h$ is
> merely Schwartz (only polynomial decay, $|\tilde h(x)|\le C_N(1+|x|)^{-N}$
> for every $N$, no exponential rate — Remark 111.0.1's
> $e^{-\sqrt{|x|}}$-type functions included), then $|h(p^n)|\le C_2(1+n\log
> p)^{-2}$ and $\sum_n(1+n\log p)^{-2}<\infty$ for every fixed $p$, and
> likewise $B_p(h)$ converges even faster (extra factor $p^{-m}$). So **at a
> single fixed prime**, no exponential decay rate is needed at all for
> Lemma 1.1's two tails — this changes at the *global* (all-primes) level,
> Task 2, §2 below, exactly the distinction 111_00 Remark 111.0.1 warns must
> not be conflated.

Verified: partial sums of $A(h),B_p(h)$ stabilize to machine precision by
$n,m\approx40$ for $p=2$ and a bare-Schwartz control with only
$(1+|x|)^{-6}$ decay.

## 2. The raw (unrenormalized) shell-$0$ divergence extends verbatim

> ### Theorem 2.1 (108_17's criterion, unchanged by Schwartz decay)
> Define the $K$-truncation exactly as 108_12/108_17 do: excise
> $\{|1-u|_p\le p^{-K}\}$. Then
> $$W_p^{(K)}(h)=A(h)+B_p(h)+h(1)\Big(\frac{p-2}{p-1}+K\Big),$$
> exactly, for every $K\ge0$ and every $\tilde h\in\mathcal S_\eta$,
> $\eta>0$. Consequently $\lim_{K\to\infty}W_p^{(K)}(h)$ exists **iff**
> $h(1)=0$, in which case $W_p^{(K)}(h)=A(h)+B_p(h)$ for every $K$
> (identically, not merely in the limit).

**Proof.** The shells $n\ne0$ are never touched by the excision (108_17
§1: the excised set lies entirely inside the unit shell), so their
contribution is $A(h)+B_p(h)$ for every $K$, convergent absolutely by
Lemma 1.1 — this is the one place compact support mattered in 108_17's
Theorem 1.2, and Lemma 1.1 shows Schwartz decay replaces it without loss.
The shell-$0$ piece is $h(1)$ times 108_12 Theorem 2.1's exact truncation
$(p-2)/(p-1)+K$, since $\varphi$ is constant $=h(1)$ on all of
$\mathbb Z_p^\times$ (this used nothing about $h$ beyond $h(u)=h(|u|_p)$,
so it is exactly 108_17 Theorem 2.2's proof, unmodified). The
$K$-dependence is confined to $h(1)\cdot K$, bounded iff $h(1)=0$. $\square$

**This closes the negative half of the central risk exactly as feared**:
the raw shell-truncation mechanism that 108_17 proved fails for the graded
family $\{f_a\}$ fails, by the identical computation, for Schwartz $h$. The
compactly-supported hypothesis in 108_17's Definition 1.1 was never load-
bearing for this half of the argument; it only controlled the tails, which
Schwartz decay controls just as well (§1).

## 3. The central risk: is the raw truncation *the* regularization meant?

107_239 (2.1)–(2.2) calls the integral "Tate's fixed local normalization,"
and 108_17 §1 asserts the raw $K$-truncation above "*is* the Tate PV in this
program, not a new choice." Two facts complicate that identification.

**Fact (i).** 108_12 §5 itself lists as **not established**: "the correct
regularized value of $C_p$ in Tate's normalization, which would require
fixing that normalization explicitly." This is 108_12's own admission that
the raw truncation had not been shown to *be* Tate's normalization — only
that it is a specific, explicit, divergent quantity. 108_17's later
"not a new choice" is a stronger claim than 108_12 licensed.

**Fact (ii).** The raw truncation is not a principal value in the technical
sense standard in this area (subtracting a divergence and reporting the
remainder, as 107_239 (1.4) itself does with $-2h(1)\log\Lambda$) — it is
an unregularized partial sum. A genuine principal value exists here, built
by exactly the tool Tate's thesis is built from: analytic continuation of a
local zeta-type integral in an auxiliary complex parameter.

> ### Definition 3.1 (the auxiliary local zeta integral)
> For $\Re(s)>-1$,
> $$I_p(s):=\int_{\mathbb Z_p^\times}|1-u|_p^{s}\,d^\times u
> =\frac{p-2}{p-1}+\sum_{k\ge1}p^{-k}\cdot p^{-ks}
> =\frac{p-2}{p-1}+\frac{p^{-(1+s)}}{1-p^{-(1+s)}}.$$

The series is the shell decomposition of $|1-u|_p^s$ on $\mathbb
Z_p^\times$ (108_12 Lemma 1.1), and it is a finite geometric series in
$p^{-(1+s)}$, so it continues meromorphically to $\mathbb C\setminus\{-1+
\tfrac{2\pi i}{\log p}\mathbb Z\}$, with a **simple pole at $s=-1$** — the
value we actually want ($|1-u|_p^{-1}$) is exactly $s=-1$, the pole itself.

> ### Lemma 3.2 (the residue)
> Near $s=-1$, writing $\varepsilon=s+1$,
> $$I_p(-1+\varepsilon)=\frac{1}{\varepsilon\log p}+\Big(\frac{p-2}{p-1}
> -\frac12\Big)+O(\varepsilon).$$

**Proof.** $p^{-\varepsilon}=e^{-\varepsilon\log p}=1-\varepsilon\log p+
\tfrac12(\varepsilon\log p)^2+O(\varepsilon^3)$, so $1-p^{-\varepsilon}=
\varepsilon\log p\big(1-\tfrac12\varepsilon\log p+O(\varepsilon^2)\big)$ and
$$\frac{p^{-\varepsilon}}{1-p^{-\varepsilon}}
=\frac{1-\varepsilon\log p+O(\varepsilon^2)}{\varepsilon\log p\,(1-\tfrac12
\varepsilon\log p+O(\varepsilon^2))}
=\frac1{\varepsilon\log p}\big(1-\varepsilon\log p+O(\varepsilon^2)\big)
\big(1+\tfrac12\varepsilon\log p+O(\varepsilon^2)\big)
=\frac1{\varepsilon\log p}-\frac12+O(\varepsilon).\ \square$$

Verified to $10^{-7}$ relative error at $\varepsilon=10^{-3},10^{-5},
10^{-7}$ for $p=2,3,5,7,11$, against the closed-form prediction
$(p-2)/(p-1)-\tfrac12$.

> ### Theorem 3.3 (the raw truncation is a *different* scheme, exhibited)
> Define a second regularization directly from the raw truncation of §2:
> $$C_p^{(1)}:=\lim_{K\to\infty}\big[W_p^{(K)}(h)/h(1)\text{'s divergent
> part, subtracted}\big]=\frac{p-2}{p-1}\qquad(\text{"subtract }K\text{"})$$
> and the Laurent finite part of Lemma 3.2,
> $$C_p^{(2)}:=\frac{p-2}{p-1}-\frac12\qquad(\text{"finite part in }s).$$
> Then $C_p^{(1)}-C_p^{(2)}=\tfrac12$, for **every** prime $p$: the two
> regularizations disagree, by a nonzero, $p$-independent, $h(1)$-
> proportional amount.

**Proof.** Direct subtraction of the two closed forms. $\square$

Verified exactly (to the working precision, no approximation) for
$p=2,3,5,7,11,13,17,19,23$.

## 4. The structural theorem: canonicity, not finiteness, is what $h(1)=0$ buys

> ### Theorem 4.1
> Let $\mathcal R$ be **any** regularization of the shell-$0$ integral built
> by subtracting a fixed, $h$-independent divergent term from
> $h(1)\cdot I_p(s)$ near its pole (this covers §2's raw truncation,
> $C_p^{(1)}$, and $C_p^{(2)}$, and any other scheme of the same shape,
> since the shell-$0$ integral is *identically* $h(1)\cdot I_p(s)$ — a
> constant $h(1)$ times an $h$-independent function of $p$ and the scheme).
> For any two such regularizations $\mathcal R,\mathcal R'$,
> $$\mathcal R(h)-\mathcal R'(h)=h(1)\cdot c_{\mathcal R,\mathcal R'}(p)$$
> for a scheme pair-dependent constant $c_{\mathcal R,\mathcal R'}(p)$
> **independent of $h$**. Consequently: $\mathfrak T_p(h)$ (shell-$0$ piece
> plus tails) is regularization-scheme-independent **iff** $h(1)=0$, in
> which case every scheme gives the same value $A(h)+B_p(h)$ (§1), agreeing
> in particular with the raw truncation's limit (Theorem 2.1).

**Proof.** Linearity: the shell-$0$ integral is $h(1)\cdot I_p(s)$
identically (108_17's own reduction — $\varphi\equiv h(1)$ on the whole
unit shell, with no dependence on $h$'s values elsewhere), so any
regularization of it is $h(1)$ times a regularization of $I_p(s)$ at its
pole; two such differ by $h(1)$ times the difference of two numbers
depending only on $p$ and the two schemes. If $h(1)=0$ this difference
vanishes for every pair of schemes, and every scheme reduces to whatever
is left after discarding a term that is identically $0\cdot(\text{anything
finite})=0$ — i.e. no shell-$0$ contribution survives under any scheme,
matching the raw-truncation computation of Theorem 2.1 verbatim. $\square$

## 5. Verdict on the central risk

> **The raw shell-truncation of 108_12/108_17 and a genuine Tate-style
> analytic-continuation regularization are demonstrably different
> constructions** (Theorem 3.3: they disagree by $h(1)/2$, an explicit,
> nonzero, computable quantity, not by anything that could be a numerical
> artifact). 108_17's claim that the raw truncation "*is* the Tate PV...
> not a new choice" therefore overstates what 108_12 itself had established
> (Fact (i), §3) — but the alternative construction does **not** rescue
> $\mathfrak T_p(h)$ into being a scheme-free number when $h(1)\ne0$: it
> merely produces *a* finite number, whose value depends on an
> unstated normalization choice not fixed by any source read in this
> programme (§4).
>
> Resolving the risk exactly as 113_00 §1–2 pre-registered as outcome (c):
> **the local integral is finite, for every Schwartz $h$, under any fixed
> regularization scheme — but it is canonical (a well-defined function of
> $h$ alone, with no further external input) if and only if $h(1)=0$.**
> This is not the same statement as 108_17's "$\varphi_0=0$ or divergence,"
> though it specializes to exactly that dichotomy once "regularization
> scheme" is fixed to be the raw truncation. It is a strictly more
> informative statement, and it is the one this phase adopts: **the
> admissibility condition for a construction of $\mathfrak T(h)$ that uses
> no data beyond "$h$ Schwartz" is $h(1)=0$.**

This is not rescued, and not contradicted, by 111_02's finding that the
*global* trace-level counterterm $-2h(1)\log\Lambda$ absorbs a nonzero
identity value without difficulty (111_02 Proposition 1.1). That argument
concerns the single, already-fixed global regularization of the whole
adelic trace $\mathrm{Tr}(\theta(h)R_\Lambda)$, which by construction
carries its own $h(1)$-proportional counterterm. The question resolved
here is different and prior: whether the **local, per-prime** closed-form
pieces of (2.1) — which 107_239 asserts *equal* $\mathfrak T_S(h)$, term by
term, place by place — are individually well-defined numbers. They are,
but only up to the scheme ambiguity of Theorem 4.1, and only $h(1)=0$
removes it. 111_02's argument is silent on this because it never opens the
per-place decomposition (2.1) at all.

## 6. Scope

**Proved here.** Lemma 1.1 and Remark 1.2 (tail convergence, any $\eta>0$,
bare Schwartz for a single prime); Theorem 2.1 (raw truncation diverges
unless $h(1)=0$, extending 108_17 Theorem 2.2 verbatim to Schwartz $h$);
Lemma 3.2 (exact residue and finite part of the auxiliary zeta integral);
Theorem 3.3 (two explicit, reasonable schemes disagree by exactly $h(1)/2$);
Theorem 4.1 (scheme-independence $\iff h(1)=0$, in general, by linearity).

**Read from source, not re-derived.** 108_12 Lemma 1.1 and Theorem 2.1 (the
shell measures and the exact truncation $C_p^{(K)}$); 108_17 Theorem 1.2
and 2.2 (the shell decomposition and its finiteness criterion for
compactly-supported shell test functions), whose *proof* — not merely its
statement — is reused verbatim in Theorem 2.1 above; 108_12 §5's own "not
established" flag on the Tate normalization of $C_p$, quoted as Fact (i).

**Verified numerically.** Lemma 1.1's tail stabilization; Lemma 3.2's
residue/finite-part expansion at five primes and three scales of
$\varepsilon$; Theorem 3.3's exact $1/2$ discrepancy at nine primes; the
raw-truncation linear-in-$K$ growth (slope $h(1)$) for a genuine (non-
compactly-supported) Schwartz $h$, contrasted with exact stabilization for
an $h$ with $h(1)=0$, both at several primes.

**Not established, and explicitly not claimed.** Which regularization
scheme (if either of the two exhibited, or some third one) is the one
actually meant by the cited semilocal trace theorem of arXiv:2602.15941v1
— that source is not among the files this phase reads. Whether the scheme
ambiguity can be fixed by some other, unused piece of structure (e.g. a
functional-equation compatibility requirement) is not explored; it is not
needed, since the phase proceeds by imposing $h(1)=0$, which is
scheme-independent by construction (Theorem 4.1).

## 7. Verifier

`113_01_the_local_integral_for_schwartz_data.py` checks: Lemma 1.1's tail
convergence for a genuine Schwartz $h$ and a bare-Schwartz (no exponential
rate) control, both stabilizing under refinement; Theorem 2.1's exact
closed form against direct shell summation, and the dichotomy — linear
growth in $K$ with slope $h(1)$ when $h(1)\ne0$, versus bit-level
stabilization when $h(1)=0$ — for a genuine Schwartz $h$ (not the
compactly-supported shell functions 108_17 used); Lemma 3.2's residue and
finite part against the closed form $(p-2)/(p-1)-\tfrac12$, refined in
$\varepsilon$ with a control clause rejecting the wrong constant
$(p-2)/(p-1)$ (that value is Theorem 3.3's *other* scheme, so the test
must discriminate the two, not accept either); Theorem 3.3's exact $1/2$
gap.
