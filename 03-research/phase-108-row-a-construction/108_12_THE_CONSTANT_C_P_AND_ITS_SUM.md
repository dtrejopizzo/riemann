# 108.12 — The constant $C_p$: it diverges, and so does its sum

## 0. Result

108_11 left exactly one item between Stage 1 and closure: the constant
$\sum_p C_p$, with

\[
 C_p=\int_{\mathbb Z_p^\times}'\frac{d^\times u}{|1-u|_p}.
\]

This note computes it.  The outcome is negative on both counts:

> **$C_p$ diverges as a naive integral, and after the natural regularization
> its scale is $\log p$, whose sum over primes also diverges.**

Stage 1 therefore does **not** close by evaluating this constant.  What
remains is stated precisely in §4.

No zero of $\xi$ is used anywhere.

## 1. The shell decomposition of $\mathbb Z_p^\times$

Normalize $d^\times u$ so that $\int_{\mathbb Z_p^\times}d^\times u=1$.

> ### Lemma 1.1
> \[
>  \mu\big(\{u\in\mathbb Z_p^\times:|1-u|_p=1\}\big)=\frac{p-2}{p-1},
>  \qquad
>  \mu\big(\{u\in\mathbb Z_p^\times:|1-u|_p=p^{-k}\}\big)=p^{-k}\ \ (k\ge1).
> \]

**Proof.**  Work modulo $p^m$.  The units number $p^{m-1}(p-1)$.  Those with
$u\equiv1\ (p^k)$, $u\not\equiv1\ (p^{k+1})$ number $p^{m-k-1}(p-1)$, a
fraction $p^{-k}$.  Those with $u\not\equiv1\ (p)$ number
$p^{m-1}(p-2)$, a fraction $(p-2)/(p-1)$.  Both are independent of $m$.
$\square$

Consistency: $\frac{p-2}{p-1}+\sum_{k\ge1}p^{-k}
=\frac{p-2}{p-1}+\frac1{p-1}=1$. ✓

Verified by direct counting mod $p^m$ for $p=2,3,5,7$.  Note $p=2$ gives
$(p-2)/(p-1)=0$: every $2$-adic unit is $\equiv1\ (2)$.

## 2. $C_p$ diverges

> ### Theorem 2.1
> On the shell $|1-u|_p=p^{-k}$ the integrand is $p^{k}$ and the measure is
> $p^{-k}$, so **each shell contributes exactly $1$**.  Hence
> \[
>  C_p^{(K)}:=\frac{p-2}{p-1}+K
>  \qquad\text{and}\qquad
>  C_p=\lim_{K\to\infty}C_p^{(K)}=+\infty .
> \]

**Proof.**  Immediate from Lemma 1.1: measure $\times$ integrand
$=p^{-k}\cdot p^{k}=1$ for every $k\ge1$, and there are infinitely many
shells. $\square$

Verified: the truncations are exactly $\frac{p-2}{p-1}+K$, of slope exactly
$1$ in $K$, for $p=2,3,5,7$ and $K$ up to $1000$; the shell identity checked
as an exact rational for $k\le120$.

This is the logarithmic divergence at $u=1$ that Tate's principal value
exists to regularize.  So $C_p$ is not a number to be summed; it is a
counterterm.

## 3. The regularized scale is $\log p$, and $\sum_p\log p$ diverges

Cutting the divergence at $|1-u|_p\ge p^{-K}$ removes $K$ shells, and the
corresponding multiplicative scale is $p^{K}$, i.e. $K\log p$.  Any
regularization of $C_p$ in this scheme therefore carries the factor $\log p$.

> ### Theorem 3.1
> $\sum_p\log p$ diverges.

**Proof.**  Chebyshev: $\theta(x)=\sum_{p\le x}\log p\sim x$. $\square$

Verified threshold-free: the log–log slope of $\theta(x)$ is $1.0018$ against
the theoretical $1$, and $\theta(x)/x=0.9896,\dots,0.9993$ over five decades.

> ### Corollary 3.2
> The constant term of the global assembly diverges, both before and after
> the natural local regularization.

## 4. Consequence for Stage 1

108_11 wrote the assembly as
$c_g(a)\big[W_\infty(f_a)+A(a)+B(a)+\sum_pC_p\big]$.  Theorem 2.1 and
Corollary 3.2 show the last bracket term is not a number.

So the $a$-dependent part exists as a distribution (108_11 Thm 3.1) while the
constant does not.  **Stage 1 is not closed.**

There is one structurally correct candidate for what must absorb it, and it
is already in the program.  107_239 (1.4) defines

\[
 \mathfrak T_S(h)=\lim_{\Lambda\to\infty}
 \Big(\operatorname{Tr}\big(\theta(h)R_\Lambda\big)-2h(1)\log\Lambda\Big),
\]

whose counterterm $-2h(1)\log\Lambda$ is **$a$-independent and proportional
to the value at $1$** — the same shape as $\sum_pC_p$.  107_239 §1 calls it
"the contribution of the generic point".

**This identification is not established.**  It is a shape match, not a
computation: the counterterm grows like $\log\Lambda$ while
$\sum_{p\le\Lambda}\log p\sim\Lambda$, and $\Lambda$ is a phase-space cutoff,
not a prime bound, so the two are not obviously commensurate.  Making the
identification precise — or refuting it — is the remaining task.

## 5. Status

Proved here:

* Lemma 1.1, the shell measures;
* Theorem 2.1, $C_p=+\infty$, with the exact truncation $\frac{p-2}{p-1}+K$;
* Theorem 3.1 and Corollary 3.2, divergence of $\sum_p\log p$ and hence of
  the regularized constant.

Not established, and explicitly not claimed:

* that the counterterm of 107_239 absorbs $\sum_pC_p$ — a shape match only;
* the correct regularized value of $C_p$ in Tate's normalization, which
  would require fixing that normalization explicitly;
* anything about complex $a$;
* the comparison with the zero side.

**Stage 1 status: the $a$-dependent part is closed (108_06, 108_07, 108_11);
the constant term is open, and cannot be closed by summation.**

`ROW_A_STATUS` remains `partial`.  Nothing here bears on RH.

## 6. Verifier

`108_12_the_constant_cp_and_its_sum.py` checks the shell measures by direct
counting mod $p^m$; the exact shell contribution $p^{-k}p^{k}=1$ as a
rational identity; the exact truncation formula and its unit slope; the
$\log p$ scale of the cutoff; and Chebyshev growth of $\theta(x)$ by
threshold-free log–log regression plus the ratio $\theta(x)/x$.
