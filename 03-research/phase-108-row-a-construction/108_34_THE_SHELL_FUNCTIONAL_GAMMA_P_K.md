# 108.34 — The shell functional $\Gamma_{p,k}$: construction and pairing formula

## 0. What this settles

Stage 3 of the row-(a) programme asks for classes $\Gamma_{p,k}$ recovering
the Weil coefficient $\Lambda(p^k)/\sqrt{p^k}$ at each prime power. 108_90 §5
flags the literal reading of that mandate — a class that is simultaneously
scaling-equivariant and supported at finitely many places — as the forbidden
rigidity/finiteness combination that has failed eight times in this
programme, and prescribes the repair: build $\Gamma_{p,k}$ as a
**functional on graded sections**, with finiteness on the paired side, not
on $\Gamma_{p,k}$ itself.

This note carries out that repair. It defines $\Gamma_{p,k}$, proves it is
linear and well-defined on *every* continuous radial profile (no decay
hypothesis needed for the definition itself — decay is needed only for the
Stage-3 assembly of 108_36), and proves the pairing formula with the graded
family $f_s(x)=x^{-s}$ that the mission requires. The normalization
producing the exact factor $\log p$, and the resulting identity with
$\Lambda(p^k)/\sqrt{p^k}$, is deferred to 108_35 by design: this note works
in 108_06's original (Tate, unit-mass) normalization throughout, so that the
two concerns — *what the functional is* and *which measure makes the
constant come out right* — are not conflated.

No zero of $\xi$ enters any definition below.

## 1. The shell decomposition, restated as a functional

Fix a prime $p$. Recall (108_06 §3) the decomposition of $\mathbb Q_p^\times$
into shells $\{u:|u|_p=p^{-n}\}$, $n\in\mathbb Z$, each of Tate mass $1$
under $d^\times u$ normalized by $\mathrm{vol}(\mathbb Z_p^\times)=1$. For a
radial test datum $h$ on $\mathbb Q_p^\times$ — meaning $h(u)=h_0(|u|_p)$ for
some $h_0:(0,\infty)\to\mathbb C$, exactly 108_06's embedding convention —
the local arithmetic integral
$W_p(h)=\int'_{\mathbb Q_p^\times}h(u^{-1})/|1-u|_p\,d^\times u$
splits shell by shell. 108_06 Theorem 3.1's proof computes each shell
contribution in closed form for $h=f_s$; the point of this note is that the
**same computation, for a single fixed shell, defines a functional on all of
$h_0$**, not merely on the monomials.

> ### Definition 1.1 (the graded-section space)
> Let $\mathcal G:=C^0\big((0,\infty),\mathbb C\big)$, with the topology of
> pointwise convergence. A **graded section** is any $h_0\in\mathcal G$. This
> includes every monomial $f_s(x)=x^{-s}$ ($s\in\mathbb C$), which is *not*
> compactly supported (108_02) and not decaying, and it includes every
> compactly supported or decaying profile used later (108_36).

> ### Definition 1.2 (the shell functional $\Gamma_{p,k}$)
> For $p$ prime and $k\in\mathbb Z\setminus\{0\}$, define
> $\Gamma_{p,k}:\mathcal G\to\mathbb C$ by
> \[
>  \Gamma_{p,k}(h_0)\;:=\;p^{\min(k,0)}\,h_0(p^{k}) .
> \]
> Explicitly: $\Gamma_{p,k}(h_0)=h_0(p^k)$ for $k\ge1$, and
> $\Gamma_{p,k}(h_0)=p^{k}\,h_0(p^{k})$ for $k\le-1$.

Definition 1.2 is *exactly* the $n=k$ (resp. $n=-k$) shell contribution to
$W_p$ that 108_06 §3 isolates, before the geometric-series resummation, and
before any $\log p$ is inserted. It is stated for a general continuous
$h_0$, not only for $f_s$; this is what makes it a functional on graded
sections rather than a number attached to one weight.

> ### Lemma 1.3 ($\Gamma_{p,k}$ is a point-evaluation functional)
> $\Gamma_{p,k}$ is linear in $h_0$, and for every $h_0\in\mathcal G$ the
> value $\Gamma_{p,k}(h_0)$ is finite, determined by the single value
> $h_0(p^k)$: $\Gamma_{p,k}$ is $p^{\min(k,0)}$ times the Dirac evaluation
> functional $\delta_{p^k}$ at the point $p^k\in(0,\infty)$.

**Proof.** Linearity: $h_0\mapsto h_0(p^k)$ is linear, and $\Gamma_{p,k}$ is
a constant multiple of it. Finiteness: $h_0$ is continuous at the single
point $p^k\in(0,\infty)$, so $h_0(p^k)$ is a well-defined complex number,
and $p^{\min(k,0)}$ is a fixed nonzero real number; the product is finite.
No decay, boundedness, or integrability hypothesis on $h_0$ is used
anywhere. $\square$

**This is the reformulation's load-bearing fact.** $\Gamma_{p,k}$ requires
nothing of $h_0$ beyond continuity at one point. In particular it is
perfectly well defined on the raw monomials $f_s$, which are excluded from
every finiteness class used elsewhere in this programme (108_02: not
compactly supported; 108_06 Theorem 4.1: the prime sum on them diverges).
The functional does not need $h_0$ to be finite in any sense; only the
*infinite sum* over $(p,k)$, assembled in 108_36, will need that of its
argument.

## 2. The pairing formula

> ### Theorem 2.1 (pairing with the graded family)
> For every $s\in\mathbb C$, $p$ prime, $k\in\mathbb Z\setminus\{0\}$,
> \[
>  \boxed{\;
>  \Gamma_{p,k}(f_s)=
>  \begin{cases}
>   p^{-ks}, & k\ge 1,\\[2pt]
>   p^{|k|(s-1)}, & k\le -1.
>  \end{cases}
>  \;}
> \]
> In particular, at $s=\tfrac12$, both branches give
> $\Gamma_{p,k}(f_{1/2})=\Gamma_{p,-k}(f_{1/2})=p^{-k/2}$ for every
> $k\ge1$.

**Proof.** By Definition 1.2 and $f_s(x)=x^{-s}$: for $k\ge1$,
$\Gamma_{p,k}(f_s)=f_s(p^k)=(p^k)^{-s}=p^{-ks}$. For $k\le-1$, write
$k=-m$, $m\ge1$: $\Gamma_{p,k}(f_s)=p^{k}f_s(p^k)=p^{-m}(p^{-m})^{-s}
=p^{-m}p^{ms}=p^{m(s-1)}=p^{|k|(s-1)}$. At $s=\tfrac12$: $p^{-k\cdot1/2}=p^{-k/2}$
for the first branch (with $k\ge1$ here meaning the shell index, consistent
with the displayed formula), and $p^{|k|(1/2-1)}=p^{-|k|/2}$ for the second;
writing both with the same positive integer $k=|{\cdot}|\ge1$ gives the
stated equality. $\square$

This is precisely task (1) of the mission and the "key observation": the
$k$-th shell of the first summand of 108_06 Theorem 3.1 is $p^{-ks}$, the
$k$-th shell of the mirror summand is $p^{k(s-1)}$, and both specialize to
$p^{-k/2}$ at the central weight — before any $\log p$ is attached.

> ### Corollary 2.2 (resummation recovers 108_06 Theorem 3.1)
> For $0<\Re s<1$,
> \[
>  \sum_{k\ge1}\Gamma_{p,k}(f_s)=\frac{p^{-s}}{1-p^{-s}},\qquad
>  \sum_{k\ge1}\Gamma_{p,-k}(f_s)=\frac{p^{s-1}}{1-p^{s-1}} ,
> \]
> so $W_p(f_s)=\sum_{k\ge1}\big[\Gamma_{p,k}(f_s)+\Gamma_{p,-k}(f_s)\big]+C_p$,
> exactly 108_06 Theorem 3.1 with the two geometric series unwound term by
> term.

**Proof.** Geometric series with ratio $p^{-s}$ (resp. $p^{s-1}$), summable
exactly on $0<\Re s<1$ (resp. same range, by 108_06 Theorem 3.1's own
convergence statement); the sums are the standard closed forms. Adding
$C_p$ (the untouched $k=0$ shell, 108_06 §3) reproduces $W_p(f_s)$
verbatim. $\square$

Corollary 2.2 is a repackaging, not a new fact: it certifies that
Definition 1.2 is the correct atomization of 108_06's already-proved closed
form, term by term, with no discrepancy.

## 3. Scope

Proved:

* Lemma 1.3: $\Gamma_{p,k}$ is a linear, everywhere-finite point-evaluation
  functional on $\mathcal G=C^0((0,\infty))$ — in particular defined on
  non-decaying, non-compactly-supported sections such as the monomials
  $f_s$;
* Theorem 2.1: the pairing formula $\Gamma_{p,k}(f_s)=p^{-ks}$ (resp.
  $p^{|k|(s-1)}$), and its coincidence at $s=\tfrac12$;
* Corollary 2.2: resummation over $k$ reproduces 108_06 Theorem 3.1 exactly.

Not established here, and explicitly deferred:

* the $\log p$ normalization and the identity with $\Lambda(p^k)/\sqrt{p^k}$
  — 108_35;
* convergence of $\sum_{p,k}\Gamma_{p,k}$ against admissible data, and the
  divergence of the naive fixed-grade sum — 108_36;
* the design-condition audit — 108_37;
* dependence on Stage 2 — 108_38;
* the value or the sum of $C_p$: untouched, exactly as in 108_06.

## 4. Verifier

`108_34_the_shell_functional_gamma_p_k.py` checks: linearity of
$\Gamma_{p,k}$ on random linear combinations of test profiles; finiteness
of $\Gamma_{p,k}(f_s)$ for large $p,k$ and complex $s$ (no overflow/NaN,
confirming Lemma 1.3's claim that the functional itself needs no decay
hypothesis); the pairing formula of Theorem 2.1 against the definition,
for real and complex $s$; the coincidence of both branches at $s=1/2$; and
Corollary 2.2's resummation, by threshold-free log–log regression of the
partial-sum residual against the predicted geometric rate $p^{-N\Re s}$.
