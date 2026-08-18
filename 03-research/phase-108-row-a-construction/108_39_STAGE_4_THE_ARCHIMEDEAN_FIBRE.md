# 108.39 — Stage 4: the archimedean fibre and its polar page

## 0. Result

Stage 4 asks for an archimedean fibre with its polar $H^0/H^2$ page.  Almost
all of it is already present in the Stage-2 identity; what this note does is
identify the pieces.

> \[
>  \boxed{\;\Phi(s)=\underbrace{\pi\cot\frac{\pi s}{2}}_{\text{archimedean
>  local term}}
>  \;+\;\underbrace{G'(s)+G'(1-s)}_{\text{symmetrized log-derivative of the
>  archimedean }\Gamma\text{-factor}}\;}
> \]
> where $G=\log\Gamma_\R$ and $\Gamma_\R(s)=\pi^{-s/2}\Gamma(s/2)$.  The polar
> page contributes $1/s+1/(s-1)$, which **cancels identically** in the
> symmetrization --- the same fact as the hyperbolicity of the polar block of
> Stage 0.

No zero of $\xi$ enters any definition.

## 1. The archimedean determinant

Let $\Gamma_\R(s):=\pi^{-s/2}\Gamma(s/2)$, the archimedean factor of the
completed zeta function $\xi(s)=\tfrac{s(s-1)}2\,\Gamma_\R(s)\,\zeta(s)$, and
put $G:=\log\Gamma_\R$, so that
\[
 G'(s)=-\tfrac12\log\pi+\tfrac12\psi\!\big(\tfrac s2\big).
\]

> ### Theorem 1.1
> The finite part of the Stage-2 assembly is the symmetrized logarithmic
> derivative of the archimedean $\Gamma$-factor:
> \[
>  -\frac{\zeta'}{\zeta}(s)-\frac{\zeta'}{\zeta}(1-s)
>  \;=\;G'(s)+G'(1-s).
> \]

**Proof.** By 108_38 Lemma 2.1 the left side equals
$\tfrac12[\psi(s/2)+\psi((1-s)/2)]-\log\pi$.  Expanding the right side,
$G'(s)+G'(1-s)=\big[-\tfrac12\log\pi+\tfrac12\psi(s/2)\big]
+\big[-\tfrac12\log\pi+\tfrac12\psi(\tfrac{1-s}2)\big]$, which is the same.
$\square$

Verified at five complex arguments to $10^{-12}$.

> ### Corollary 1.2
> $\Phi(s)=\pi\cot(\pi s/2)+G'(s)+G'(1-s)$, so the whole Stage-2 object is
> built from two archimedean ingredients: the local term of 108_07 and the
> $\Gamma$-factor of the completed zeta function.

**This is the sense in which Stage 4 is available.**  The archimedean fibre
is $\Gamma_\R$; its determinant enters $\Phi$ through $G'$; and the finite
places, after the Stage-3 assembly and the functional equation, contribute
nothing beyond it.

## 2. The polar page cancels, and that is the hyperbolic block

The polar factor of $\xi$ is $s(s-1)/2$, with logarithmic derivative
\[
 P(s)=\frac1s+\frac1{s-1}.
\]

> ### Theorem 2.1
> $P(s)+P(1-s)=0$ identically.

**Proof.** $P(1-s)=\dfrac1{1-s}+\dfrac1{-s}=-\dfrac1{s-1}-\dfrac1s=-P(s)$.
$\square$

Verified at five arguments, real and complex, to $10^{-13}$.

> ### Corollary 2.2 (identification with Stage 0)
> The polar page is invisible in $\Phi$ **because it is self-cancelling under
> $s\mapsto1-s$**, which is precisely the statement that the polar block of
> the Stage-0 signature is the hyperbolic plane
> $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ --- a form of
> signature $(1,1)$, i.e. one that pairs its two directions against each
> other and contributes nothing to a symmetric total.

So the two appearances of the polar data --- as the $H^0/H^2$ page of the
archimedean fibre, and as the two rulings of the product surface --- are the
same object seen twice.  This was the partial start recorded for Stage 4; it
is now an identity rather than an analogy.

## 3. What Stage 4 establishes, and what it does not

**Establishes.**  The archimedean fibre is $\Gamma_\R(s)=\pi^{-s/2}\Gamma(s/2)$;
its symmetrized log-determinant is exactly the finite part of the assembly
(Theorem 1.1); $\Phi$ decomposes into archimedean local term plus
$\Gamma$-factor (Corollary 1.2); the polar page cancels identically and this
is the same fact as the hyperbolicity of the Stage-0 polar block
(Theorem 2.1, Corollary 2.2).

**Does not establish.**

* That $\Gamma_\R$ arises as a *determinant of an operator* on an archimedean
  fibre.  Theorem 1.1 is an identity of meromorphic functions; no operator,
  no regularized determinant and no Fredholm theory is constructed here.
  Paper 40's item (2) asks for the determinant, and that reading is **not**
  supplied.
* Any intersection-theoretic content.  As in Stage 3, these are identities
  between analytic objects; making either side an intersection number is
  Stage 5.
* Anything about $\RH$.

The candid summary is that Stage 4 is established in its *identity* form and
open in its *operator* form.

## 4. Verifier

`108_39_stage_4_the_archimedean_fibre.py` implements $\psi$ by recurrence and
asymptotic expansion, checks Theorem 1.1 at five complex arguments,
Corollary 1.2 at four, Theorem 2.1 at five, and confirms that the polar
cancellation is exact rather than approximate by evaluating $P(s)+P(1-s)$ in
exact rational arithmetic at rational $s$.
