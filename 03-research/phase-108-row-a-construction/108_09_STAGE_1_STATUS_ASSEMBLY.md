# 108.09 — Stage 1 status, assembled from 108_06, 108_07, 108_08

## 0. Purpose

This note does not prove anything new. It assembles the results of 108_06
(finite places), 108_07 (archimedean place) and 108_08 (the global
continuation attempt) into a single, exact statement of where Stage 1 — the
measure-valued extension of the corner trace $\mathfrak T_S$ to the graded
family $\mathcal G=\{f_a(x)=x^{-a}\}$ — currently stands. Nothing below
promotes `ROW_A_STATUS`, and nothing below is claimed to bear on RH.

## 1. The three pieces

> **Finite places (108_06 Theorem 3.1, Corollary 3.2).** For every finite
> prime $p$,
> \[
>  W_p(f_a)=\frac{p^{-a}}{1-p^{-a}}+\frac{p^{a-1}}{1-p^{a-1}}+C_p,
> \]
> $C_p$ an $a$-independent Tate principal value (unevaluated), convergent
> **exactly** on $0<\Re a<1$.

> **Archimedean place (108_07 Theorem 4.1, Theorem 5.1).**
> \[
>  W_\infty(f_a)=\pi\cot\!\Big(\frac{\pi a}2\Big),
> \]
> in closed form, convergent (as a principal value at $u=1$) **exactly**
> on $0<\Re a<1$ — the same strip, independently derived, with no
> unevaluated constant: 108_07's local term is fully closed-form and
> regular throughout the strip, in particular $W_\infty(f_{1/2})=\pi$
> (108_07 Corollary 6.1).

> **The global sum (108_06 Theorem 4.1, 108_08 Theorem 8.1).** The naive
> sum $\sum_p W_p(f_a)$ diverges throughout $0<\Re a<1$ (108_06). Replacing
> the naive sum by analytic continuation of its two Dirichlet-series halves
> $A(a)=\sum_p p^{-a}/(1-p^{-a})$ and $B(a)=A(1-a)$ does not repair this:
> on the real segment $a\in(0,1)$, both halves continue with genuine
> logarithmic singularities at $\{1/N:N\ge2\}$ and $\{1-1/M:M\ge2\}$
> respectively, these sets meet at exactly $a=1/2$, and there the two
> singularities **reinforce** rather than cancel (108_08 Theorem 7.1). The
> full singular set accumulates at both endpoints $a=0,1$ of the strip
> (108_08 Theorem 8.1).

## 2. What is, and is not, established

**Established (proved, in closed form, on $0<\Re a<1$):**

* Every single-place term, $W_p(f_a)$ for finite $p$ and $W_\infty(f_a)$,
  converges on exactly the same open strip $0<\Re a<1$, derived three
  independent ways (108_06's $p$-adic shell decomposition, and 108_07's
  two archimedean endpoint power-counts) and landing on the identical
  interval every time.
* The archimedean term is fully closed-form: $\pi\cot(\pi a/2)$, regular
  throughout the strip, value $\pi$ at $a=1/2$.
* The naive global sum over primes diverges throughout the strip
  (108_06), and the specific repair by analytic continuation of the two
  Dirichlet halves also fails, with the failure pinned down exactly:
  a countable, boundary-accumulating set of logarithmic singularities,
  with reinforcement (not cancellation) at the one point, $a=1/2$, where
  the two halves' singular sets meet.

**Not established:**

* Any finite value, or any well-defined distribution, for
  $\sum_{v}W_v(f_a)$ summed over **all** places. 108_08 rules out one
  specific candidate repair (continuation of the two prime-power halves)
  on the real axis; it does not rule out every conceivable repair (see
  108_08 §9), and it does not address the archimedean term's role in a
  putative global sum at all — that combination is not computed anywhere
  in 108_06–108_08.
* The value of $C_p$ (108_06), or $\sum_p C_p$.
* Anything about complex $a$ in the global-sum question: 108_08's
  argument is confined to the real segment of the strip precisely to avoid
  needing the location of $\zeta$'s zeros (108_08 §3, §9.3); the complex
  extension is open.
* Measure-valuedness of the *combined*, all-places object in the sense of
  108_05 Corollary 4.1. Each single-place term above is holomorphic (a
  number-valued function of $a$) on the strip, which is a weaker statement
  than the distributional target 108_05 anticipated for the assembled
  construction.
* Any comparison with the zero side of the explicit formula (109_06 §1
  explains why that side is unusable as a *definition*, independent of
  the convergence questions addressed here).

## 3. One-line status

Single-place terms: **fully resolved**, closed form, identical convergence
strip at every place, finite and archimedean alike. Global assembly:
**obstructed**, with the obstruction now characterized exactly rather than
left as a bare divergence statement — it is a specific, dense-toward-the-
boundary family of logarithmic singularities that reinforce, not cancel,
at the strip's center.

`ROW_A_STATUS` remains `partial`. Nothing above is, or should be read as,
a step toward proving RH.

## 4. Scope

Proved: nothing new; this is a compilation. All proofs are in 108_06,
108_07, 108_08, referenced above by theorem number.

Not established: everything listed in §2's second bullet list, none of
which is newly resolved here.

## 5. Verifier

`108_09_stage_1_status_assembly.py` re-derives, independently and from
scratch (not by importing the other verifiers), the small set of load-
bearing numeric facts that this assembly note depends on: that the
finite-place and archimedean convergence strips coincide as *sets* (by
symbolic endpoint comparison, not numerics); the archimedean closed-form
value $\pi$ at $a=1/2$; and, at reduced cost (smaller cutoffs than
108_08's own verifier, since this is a cross-check, not a fresh
derivation), that $\Re[A(a)+B(a)]$ grows rather than plateaus as
$a\to1/2$, confirming the "obstructed" summary of §3 has not silently
reversed.
