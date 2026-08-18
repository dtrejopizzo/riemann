# 108.17 — Route G (normalization artifact): the exact criterion, derived
# from scratch, and why it excludes the graded family unconditionally

## 0. Result

Route G asked whether the finite-place constant $C_p$ is an artifact of
108_06's shell-by-shell splitting — whether the "correct" Tate principal
value, derived carefully for a genuinely compactly supported test function,
disposes of it, with the leftover surviving only because $f_a$ was fed into
the wrong slot.

The derivation below settles this exactly, in both directions.

> **For a compactly supported shell test function $\varphi$, the finite-place
> PV local term $W_p(\varphi)$ is finite — with *no* leftover additive
> constant, not even after cancellation — if and only if $\varphi$ vanishes
> on the unit shell $|u|_p=1$. This is proved from scratch below
> (Theorem 2.2), and Route G's hope is exactly correct in that regime.**
>
> **But every element of the graded family fails this criterion, always,
> because $f_a(1)=1$ is forced by $f_a(u^{-1})$ being a quasi-character
> (Theorem 3.1). Route G's mechanism is real, but it structurally cannot
> apply to $\mathcal G=\{f_a\}$. The shell splitting was not an artifact:
> Theorem 2.2 shows it is the unique correct computation, and Theorem 3.1
> shows its finiteness criterion is permanently violated on the graded
> family.**

No zero of $\xi$ is used anywhere. `ROW_A_STATUS` remains `partial`.

## 1. The PV local term for a general shell test function

Recall the finite-place arithmetic-side local term (107_239 (2.1), quoted in
108_06 §1; the same object 108_06 evaluated at $h=f_a$):

\[
 W_p(h)=\int'_{\mathbb Q_p^\times}\frac{h(u^{-1})}{|1-u|_p}\,d^\times u,
\]

the prime denoting Tate's principal value at $u=1$: excise
$\{|1-u|_p\le p^{-K}\}$ and take $K\to\infty$, using the same regularization
108_12 Theorem 2.1 already fixed for $C_p$ (truncation
$C_p^{(K)}=\frac{p-2}{p-1}+K$, exact, linear in $K$) — this *is* "the" Tate
PV in this program, not a new choice.

> ### Definition 1.1 (shell test function)
> $\varphi:\mathbb Q_p^\times\to\mathbb C$ is a **shell test function** if it
> is constant on every shell $|u|_p=p^{-n}$, with value $\varphi_n$, and
> $\varphi_n=0$ for all but finitely many $n\in\mathbb Z$.

This is exactly 108_06's own reduction ("embed through the module") applied
to a genuinely compactly supported (Schwartz–Bruhat, radial) test function,
rather than to the non-decaying quasi-character $f_a$.

> ### Theorem 1.2 (closed form, from scratch)
> For $\varphi$ a shell test function, writing $h(u):=\varphi(u)$ so that
> $h(u^{-1})$ has value $\varphi_{-n}$ on shell $n$,
> \[
>  W_p(\varphi)=\sum_{n\ge1}\varphi_{-n}\;+\;\sum_{m\ge1}\varphi_{m}\,p^{-m}
>  \;+\;\varphi_0\,C_p ,
> \]
> and the first two sums are **finite sums** (finitely many nonzero terms).

**Proof.** Identical to 108_06 Theorem 3.1's proof, term by term, with
$\varphi_{-n}$ (resp. $\varphi_m$) replacing $p^{-na}$ (resp. $p^{m(a-1)}$)
on each shell:

* $n\ge1$ ($|u|_p<1$): $|1-u|_p=1$, contribution $\varphi_{-n}\cdot1$ per
  shell of measure $1$;
* $n\le-1$, $m=-n\ge1$ ($|u|_p>1$): $|1-u|_p=|u|_p=p^m$, contribution
  $\varphi_m/p^m$;
* $n=0$ ($u\in\mathbb Z_p^\times$): $\varphi$ is constant $=\varphi_0$ on
  this whole shell (Definition 1.1), so the contribution is
  $\varphi_0\int'_{\mathbb Z_p^\times}d^\times u/|1-u|_p=\varphi_0 C_p$
  exactly, by definition of $C_p$ (108_12 §1).

Compact support (Definition 1.1) makes the first two sums finite. $\square$

Setting $\varphi_n=p^{-na}$ for all $n$ (not compactly supported) recovers
108_06 Theorem 3.1 exactly; Theorem 1.2 is its finite-support generalization,
proved by the same computation with no new machinery.

## 2. The exact finiteness criterion

> ### Theorem 2.1 (the regularized value)
> Under the truncation $K$ (excise $|1-u|_p\le p^{-K}$, i.e. keep only the
> first $K-1$ shells of the singularity at $u=1$),
> \[
>  W_p^{(K)}(\varphi)=\sum_{n\ge1}\varphi_{-n}+\sum_{m\ge1}\varphi_m p^{-m}
>  +\varphi_0\Big(\frac{p-2}{p-1}+K\Big),
> \]
> exactly, for every $K\ge0$ (108_12 Theorem 2.1's truncation, scaled by
> $\varphi_0$; the first two sums do not depend on $K$ since they involve no
> shell of $\mathbb Z_p^\times$).

**Proof.** Immediate from Theorem 1.2 and 108_12 Theorem 2.1's exact formula
$C_p^{(K)}=\frac{p-2}{p-1}+K$. $\square$

> ### Theorem 2.2 (Route G's criterion, exact)
> $\displaystyle\lim_{K\to\infty}W_p^{(K)}(\varphi)$ exists (is finite) **if
> and only if** $\varphi_0=0$. When $\varphi_0=0$,
> \[
>  W_p(\varphi)=\sum_{n\ge1}\varphi_{-n}+\sum_{m\ge1}\varphi_m p^{-m},
> \]
> a finite sum, with **literally zero contribution from the singular shell
> at $u=1$, at every finite stage $K$** — not a cancellation of an infinite
> quantity against a subtracted counterterm, but the product
> $\varphi_0\cdot\big(\frac{p-2}{p-1}+K\big)=0$ for every $K$, since
> $\varphi_0=0$ identically. When $\varphi_0\ne0$, $W_p^{(K)}(\varphi)$
> diverges **linearly in $K$ with slope exactly $\varphi_0$**, and no
> $K$-independent additive correction repairs this, since the divergent part
> is $\varphi_0\cdot K$, not a bounded discrepancy.

**Proof.** Immediate from Theorem 2.1: the only $K$-dependent term is
$\varphi_0\cdot K$, which is bounded iff $\varphi_0=0$, in which case it
vanishes identically (not merely in the limit) for every $K$. $\square$

This is the precise, from-scratch resolution of the question Route G posed:
**the shell splitting is the correct computation, without exception or
hidden slack, and the finiteness criterion is exactly $\varphi_0=0$, i.e.
"the test function vanishes on the shell containing the group identity
$u=1$."** Route G's suspicion — that the correct PV disposes of the
constant for candid test functions — is *true*, and now proved, for the
class of test functions where it can possibly be true. The remaining
question is whether the graded family belongs to that class.

## 3. The graded family never belongs to that class

> ### Theorem 3.1 (the identity obstruction)
> For every $a$ for which $f_a$ is defined, $f_a(1)=1$. Consequently, writing
> $\varphi(u):=f_a(u^{-1})=|u|_p^{a}$ (108_06 §3's own reduction),
> $\varphi_0=\varphi\big|_{|u|_p=1}=1\ne0$, and this holds for **every**
> $a\in\mathbb C$, not merely on the real segment $(0,1)$ that 108_08
> confined itself to.
>
> More generally: for **any** continuous quasi-character
> $\chi:\mathbb Q_p^\times\to\mathbb C^\times$, $\chi(1)=1$, because $\chi$ is
> a group homomorphism and $1$ is the identity of $\mathbb Q_p^\times$. Since
> $u\mapsto|u|_p^{a}$ is such a quasi-character for every $a$, the identity
> $\varphi_0=1$ is not a computational accident of $f_a$'s specific formula:
> it is forced by $f_a(u^{-1})$ being a character, period.

**Proof.** $f_a(x)=x^{-a}$, so $f_a(1)=1^{-a}=e^{-a\log1}=e^0=1$ for every
branch and every $a\in\mathbb C$ (no ambiguity: the base is $1$, whose
logarithm is $0$ regardless of branch). The general statement is the
one-line fact that a group homomorphism sends the identity to the identity:
$\chi(1)=\chi(1\cdot1)=\chi(1)^2\implies\chi(1)\in\{0,1\}$, and $\chi(1)\ne0$
since $\chi$ takes values in $\mathbb C^\times$; so $\chi(1)=1$. $\square$

> ### Corollary 3.2 (Route G fails for $\mathcal G$, unconditionally)
> By Theorem 2.2 (criterion $\varphi_0=0$) and Theorem 3.1 ($\varphi_0=1$ for
> every $a$), $W_p(f_a)$ genuinely contains the divergent term $C_p$
> (multiplied by $1$), for **every** $a$. This **confirms, and sharpens,**
> 108_06 Theorem 3.1 and 108_12 Theorem 2.1: the shell decomposition used
> there was not an artifact of a naive splitting — Theorem 1.2–2.2 above show
> it is the *unique* correct computation of $W_p(\varphi)$ for any shell test
> function, singular or not — and the reason the graded family sees the
> singular part is a structural, a-independent fact about quasi-characters
> (Theorem 3.1), not a defect that a smarter regularization could route
> around. **No choice of $a$ escapes it, and no regularization of $C_p$
> escapes it, because the divergence rate itself — not merely the limiting
> value — is proportional to $\varphi_0=1$ (Theorem 2.2's second clause).**

Route G is discarded, by proof, having first been made to succeed exactly
where it legitimately can (Theorem 2.2, $\varphi_0=0$ case), which is
precisely how its failure on $\mathcal G$ becomes a theorem rather than a
restatement of 108_12.

## 4. Scope

Proved here:

* Theorem 1.2: closed form of $W_p(\varphi)$ for any shell test function,
  from scratch, generalizing 108_06 Theorem 3.1's proof verbatim;
* Theorem 2.1–2.2: the exact regularized value and the sharp criterion
  $\varphi_0=0$ for finiteness, including the linear-in-$K$ divergence rate
  when $\varphi_0\ne0$;
* Theorem 3.1: $f_a(1)=1$ for every $a\in\mathbb C$, and more generally
  $\chi(1)=1$ for every quasi-character — a structural fact, not a
  computation specific to $f_a$'s formula;
* Corollary 3.2: Route G fails for $\mathcal G$ unconditionally, for every
  $a$, with the mechanism now identified exactly.

Not established, and explicitly not claimed:

* anything about non-radial (non-shell-constant) test functions beyond the
  one-paragraph remark that local constancy at $u=1$ together with
  $\varphi(1)=0$ forces $\varphi$ to vanish on a whole neighbourhood of $1$
  (immediate from the definition of locally constant, but not separately
  formalized as a numbered theorem here, since the radial case already
  carries the full content 108_06 uses);
* any comparison with the zero side;
* the value of $\sum_pC_p$, still not needed for anything above;
* whether some *other* construction (not $W_p(h)$ with $h=f_a$) avoids the
  issue — that is Route D, 108_18.

## 5. Verifier

`108_17_route_g_test_slot_identity_obstruction.py` checks: Theorem 1.2's
closed form against direct shell summation for explicit compactly supported
$\varphi$ with both $\varphi_0=0$ and $\varphi_0\ne0$; Theorem 2.2's
dichotomy — exact $K$-independence (bit-for-bit stabilization) when
$\varphi_0=0$, versus exact linear growth with slope $\varphi_0$ when
$\varphi_0\ne0$, fitted by regression with no arbitrary threshold; and
Theorem 3.1 — $f_a(1)=1$ to floating precision on a grid of complex $a$,
together with the resulting $\varphi_0=1$ slope in the $K$-truncated
$W_p(f_a)$, for several primes.
