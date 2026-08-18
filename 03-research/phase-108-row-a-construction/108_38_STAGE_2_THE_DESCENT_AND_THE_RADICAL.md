# 108.38 — Stage 2: the descent, and the radical in closed form

## 0. Result

Stage 3 supplies the piece Stage 2 was missing.  Its assembly is exactly the
finite part of Stage 1's local sum, so that Stage 1's object acquires a
**closed form**, and the descent question becomes a computation.

\[
 L_g(s)=c_g(s)\,\Phi(s),
 \qquad
 \Phi(s)=\pi\cot\frac{\pi s}{2}-\frac{\zeta'}{\zeta}(s)
 -\frac{\zeta'}{\zeta}(1-s),
\]
with $\Phi$ **independent of $g$**.  Three consequences, all proved below:

1. $\Phi$ is not constant, so **principal invariance fails**;
2. $\Phi$ is not identically zero, so **the pairing is not vacuous**;
3. the radical is spanned by the point masses at the zeros of $\Phi$, of
   which there is exactly one on the real segment $(0,1)$, at
   $s^\ast=0.301692388\ldots$; in particular the central weight
   $s=\tfrac12$ is **not** in the radical.

No zero of $\xi$ enters any definition; $\Phi$ is evaluated below through a
digamma identity that mentions none.

## 1. The connection Stage 3 supplies

By 108_36 Theorem 1.1 and Corollary 1.2, in the normalization of 108_35,
\[
 \sum_p W_p^{\mathrm{Tate}}(f_s)
 =-\frac{\zeta'}{\zeta}(s)-\frac{\zeta'}{\zeta}(1-s)
 +(\log p)\!\sum_p C_p ,
\]
the last term being the $s$-independent divergent constant which Stage 1
removes on mass-zero combinations (108_33 Lemma).  Adding the archimedean
term $W_\infty(f_s)=\pi\cot(\pi s/2)$ of 108_07 and the eigenvalue
$c_g(s)$ of 108_06 (2.5) gives $L_g=c_g\Phi$ as displayed.

> This is the exact junction of Stages 1 and 3: Stage 1 built the pairing and
> removed the constant; Stage 3 identified the finite part as a logarithmic
> derivative.  Neither alone determines $L_g$; together they do.

## 2. $\Phi$ in a zero-free form

> ### Lemma 2.1
> \[
>  \Phi(s)=\pi\cot\frac{\pi s}{2}
>  +\tfrac12\Big[\psi\!\big(\tfrac s2\big)+\psi\!\big(\tfrac{1-s}2\big)\Big]
>  -\log\pi .
> \]

**Proof.**  Logarithmic differentiation of the functional equation
$\xi(s)=\xi(1-s)$ gives $(\xi'/\xi)(s)+(\xi'/\xi)(1-s)=0$.  Expanding
$\xi'/\xi$ in terms of $\zeta'/\zeta$, $\psi$ and the polar terms, the polar
terms cancel in the symmetric combination and one obtains
$-\zeta'/\zeta(s)-\zeta'/\zeta(1-s)=\tfrac12[\psi(s/2)+\psi((1-s)/2)]-\log\pi$.
$\square$

Lemma 2.1 is what makes $\Phi$ computable without reference to the zeros, and
therefore what makes the statements below admissible.

## 3. The three consequences

> ### Theorem 3.1 (principal invariance fails)
> $\Phi$ is not constant on $(0,1)$; hence $L_g$ is not constant, and by
> 108_33 Theorem 2.1 there exist $s_0,s_1$ and admissible $g$ with
> $\Lambda_g^{0}(\divv U_{s_0}-\divv U_{s_1})\ne0$.  The pairing does **not**
> descend to $\operatorname{Pic}$.

Verified: $\Phi$ takes the values $7.325,\,0.868,\,-2.231,\,-5.415,\,-12.013$
at $s=0.1,0.25,0.5,0.75,0.9$.

> ### Theorem 3.2 (the pairing is not vacuous)
> $\Phi\not\equiv0$.  In particular $\Phi(\tfrac12)=-2.230590766\ne0$.

This is the control that had to be run before building further: had $\Phi$
vanished identically --- which the functional equation makes a real
possibility, since $(\xi'/\xi)(s)+(\xi'/\xi)(1-s)\equiv0$ --- the radical
would have been everything and the whole construction empty.  It does not.

> ### Theorem 3.3 (the radical, in closed form)
> \[
>  \operatorname{rad}\Lambda^{0}
>  =\Big\{\textstyle\sum_i\lambda_i\delta_{s_i}\ :\ \sum_i\lambda_i=0,\
>  \ \lambda_i=0 \text{ whenever } \Phi(s_i)\ne0\Big\},
> \]
> i.e.\ the radical is spanned by the point masses at the zeros of $\Phi$.

**Proof.**  $\Lambda_g^{0}(\sum\lambda_i\delta_{s_i})
=\sum_i\lambda_ic_g(s_i)\Phi(s_i)$.  Put $\mu_i=\lambda_i\Phi(s_i)$.  The
condition is $\sum_i\mu_ic_g(s_i)=0$ for every admissible $g$; since the
Mellin evaluations at distinct $s_i$ are linearly independent functionals of
$g$, this forces every $\mu_i=0$, i.e.\ $\lambda_i=0$ unless
$\Phi(s_i)=0$. $\square$

> ### Corollary 3.4
> On the real segment $(0,1)$, $\Phi$ has exactly one sign change, at
> \[
>  s^\ast=0.301692388160\ldots
> \]
> so the radical meets the real segment only there.  The quotient
> $\Prin'/\operatorname{rad}$ is therefore large, and the induced form is
> nondegenerate on it.

Verified by bisection to $\Phi(s^\ast)=-2.2\times10^{-16}$, and by a scan of
$1999$ points detecting exactly one sign change.

## 4. What Stage 2 settles

**Settled.**  The descent question, in both directions: the pairing does not
descend to $\operatorname{Pic}$ (Theorem 3.1), but it does descend to the
quotient by an explicitly described discrete radical (Theorem 3.3,
Corollary 3.4), and that quotient is not trivial (Theorem 3.2).

**Why the negative half is not fatal.**  Weil's argument does not use the
intersection pairing on $\operatorname{Pic}$; it uses it on classes modulo
algebraic or numerical equivalence.  The Hodge-index statements available in
the literature are likewise stated on $NS\otimes\Q$.  A pairing that descends
to a quotient by a discrete radical is of that type.

**Not settled.**

* Whether the quotient of Theorem 3.3 coincides with, or maps to, the
  numerical quotient of Stage 0.  The two are constructed differently and
  their comparison is not attempted here; that comparison is what would join
  the two halves of the programme.
* The zeros of $\Phi$ off the real segment.  Only the real scan was
  performed.
* Any statement about $\RH$.

`ROW_A_STATUS` is not promoted here.

## 5. Verifier

`108_38_stage_2_the_descent_and_the_radical.py` implements $\psi$ by
recurrence plus asymptotic expansion (no external library), checks Lemma 2.1
against an independent evaluation, exhibits the non-constancy and
non-vanishing of $\Phi$, locates $s^\ast$ by bisection, counts sign changes
on a fine scan, confirms $\Phi(\tfrac12)\ne0$, and verifies the radical
characterisation on explicit finite combinations.
