# 108.05 — The graded family is Mellin-dual to the test class, and Burnol's cutoff is the pairing

## 0. The question this answers

108.10 recorded that Part I's graded family $\mathcal G=\{f_a(x)=x^{-a}\}$ and
Part II's numerical quotient are built on **disjoint** test-function
categories, and called the gap "candid, structural, and previously
unstated".  108.04 recorded the same gap as: $I_\partial$ does not accept the
graded witness as an input.

This note identifies the gap.  It is not an accident of two constructions
failing to meet: **it is a duality**, and the regularization that pairs the
two sides is already published.

## 1. Source read

Lagarias, *Li coefficients for automorphic L-functions*, arXiv:math/0404394,
Appendix §9 (text extracted from the PDF, now in
`00-references/papers-nuevos/extension-clase-test/`).

Test space $A_\delta$: those $f$ whose Mellin transform
$\hat f(s)=\int_0^\infty f(x)x^s\,\frac{dx}{x}$ is analytic in the strip
$\tfrac12-\delta<\Re(s)<\tfrac12+\delta$ and continuous up to the boundary.

Weil distribution functional and trace functional:
\[
 W[f]:=\sum_{\xi(\rho)=0}{}'\ \hat f(\rho),
 \qquad
 T[f]:=\hat f(0)-W[f]+\hat f(1).
\]

Trace form $T[f]=\sum_\nu W_\nu(f)$; **covariance form**
\[
 W[f]=-\sum_\nu W_\nu(f)+W_0(f)+W_1(f),
 \qquad W_0(f)=\hat f(0),\ W_1(f)=\hat f(1).
 \tag{9.6}
\]

And the statement that motivated this note, quoted:

> "one can make sense of the functional $W[f]$ on a larger set of test
> functions than those allowed in the trace form, permitting test functions
> that have singularities at $s=0$ and $s=1$.  However the right hand side of
> (9.6) must then be redefined as a limit as $T\to\infty$, with each local
> term computed using cutoffs at $x=\frac1T$ near zero and at $x=T$ near
> $\infty$."

The computation is attributed to Bombieri–Lagarias, *Complements to Li's
criterion for the Riemann hypothesis*.

**Consistency check.**  Lagarias (9.7) gives the Weil scalar product
$\langle f,g\rangle_W=\sum_\rho \hat f(\rho)\hat g(1-\bar\rho)$.  This is
exactly the form derived in 107_241, with the same involution
$\rho'=1-\bar\rho$.  107_241's computation is therefore standard, as that
note already stated.

## 2. The graded family has no Mellin transform

> ### Proposition 2.1
> For $f_a(x)=x^{-a}$ the Mellin integral
> $\int_0^\infty x^{-a}x^{s}\frac{dx}{x}=\int_{\mathbb R}e^{t(s-a)}dt$
> converges for **no** $s\in\mathbb C$.  Hence $f_a\notin A_\delta$ for any
> $\delta$, and $\hat f_a$ does not exist as a function.

**Proof.**  $\int_{\mathbb R}e^{t(s-a)}dt$ has integrand of modulus
$e^{t\Re(s-a)}$, which fails to be integrable at $+\infty$ if
$\Re(s-a)\ge0$ and at $-\infty$ if $\Re(s-a)\le0$. $\square$

Verified numerically in three regimes (§6): off the line the truncated value
grows exactly like $T^{|\Re(s-a)|}$ (fitted exponents match to $10^{-3}$); on
the line with $u\ne0$ it oscillates with persistent sign changes at
arbitrarily large $T$; at $u=0$ it equals $2\log T$.

So the incompatibility of 108.04/108.10 is **not** a matter of degree.  It is
categorical: $\mathcal G$ contains no element of the test class.

## 3. Under Burnol's cutoff it becomes a Dirichlet kernel

> ### Theorem 3.1
> With the cutoff $[\tfrac1T,T]$ of the covariance form,
> \[
>  \int_{1/T}^{T}x^{-a}x^{s}\frac{dx}{x}
>  \;=\;
>  \frac{2\sinh\big((s-a)\log T\big)}{s-a},
> \]
> which on the vertical line $s=a+iu$ is the **Dirichlet kernel**
> \[
>  k_T(u)=\frac{2\sin(u\log T)}{u},
>  \qquad k_T(0)=2\log T .
> \]
> Its total mass is $2\pi$ for every $T$, and $k_T\to2\pi\,\delta$ weakly.

**Proof.**  Substituting $x=e^t$ turns the integral into
$\int_{-\log T}^{\log T}e^{t(s-a)}dt=\frac{2\sinh((s-a)\log T)}{s-a}$; on
$s=a+iu$ this is $\frac{2\sin(u\log T)}{u}$.  The mass and weak-limit
statements are the classical properties of the Dirichlet kernel. $\square$

Verified (§6): the closed form against numerical quadrature; mass $2\pi$
independent of $T$ over four decades; and weak convergence
$\langle k_T,\varphi\rangle\to2\pi\varphi(0)$ against four smooth test
functions, with relative error below $10^{-3}$ already at $T=10^3$.

> **Caution recorded.**  The Dirichlet kernel is *not* positive.  Convergence
> to $\delta$ is weak, against smooth test functions — **not** by
> concentration of mass.  A first version of the verifier tested mass
> concentration and correctly failed; the test, not the mathematics, was
> wrong.

## 4. Structural conclusion

> ### Corollary 4.1
> $\mathcal G$ is not a subspace of the test class $A_\delta$; under the
> covariance-form cutoff, each $f_a$ defines instead a measure
> $2\pi\,\delta$ supported on the vertical line $\Re s=a$.  The graded family
> is therefore **Mellin-dual** to the test class, and the cutoff of the
> covariance form is exactly the pairing between them.

This changes the reading of 108.10 Proposition 4.1.  The two halves of
Phase 108 do not fail to compose because one construction is defective; they
sit on opposite sides of a duality, and the published regularization is the
map between the sides.

It also changes the target: any extension of $\mathfrak T_S$ to $\mathcal G$
cannot be number-valued.  The correct target is **measure-valued on the
abscissa**.

### 4.2 Formal reading — labelled formal, not proved

Substituting $\hat f_a=2\pi\delta_{\{\Re s=a\}}$ into
$W[f]=\sum_\rho\hat f(\rho)$ localizes $W[f_a]$ on the zeros with
$\Re\rho=a$; the graded degree $a$ would then be the **abscissa**, and grade
$a=\tfrac12$ would see exactly the on-line zeros — the same split as
107_241's block decomposition into fixed points and mirror 2-cycles of
$\rho\mapsto1-\bar\rho$.

This is **not proved here**.  Evaluating a delta at the points of a discrete
set is not justified by anything above, and the interchange of the weak limit
with the (conditionally convergent) sum over zeros is exactly the step that
would need work.  It is recorded as the reading that motivates the next task,
not as a result.

## 5. Status

Proved:

* Proposition 2.1: $\mathcal G\cap A_\delta=\emptyset$, categorically;
* Theorem 3.1: the closed form of the cutoff Mellin integral, its identification
  as the Dirichlet kernel, mass $2\pi$, weak convergence to $2\pi\delta$;
* Corollary 4.1: the duality, and the consequent change of target from
  number-valued to measure-valued.

Read from source, not re-proved:

* the covariance form (9.6), the test space $A_\delta$, and the cutoff
  regularization, all from arXiv:math/0404394 §9, with the computation
  attributed there to Bombieri–Lagarias.

Not established, and explicitly not claimed:

* any extension of $\mathfrak T_S$ or $I_\partial$ to $\mathcal G$;
* the formal reading of §4.2;
* that $\mathcal G$'s pairing is well defined, let alone that principal
  invariance holds;
* any change to `ROW_A_STATUS`, which remains `partial`.

## 6. Verifier

`108_05_mellin_duality_of_the_graded_family.py` checks: the power law
$T^{|\Re(s-a)|}$ off the line by threshold-free exponent regression;
persistent oscillation on the line; the exact value $2\log T$ at $u=0$; the
closed form against quadrature at three radii and three grades; mass $2\pi$
over four decades of $T$; weak convergence against four smooth test
functions; and that $\rho\mapsto1-\bar\rho$ is an involution whose fixed
points are exactly $\Re\rho=\tfrac12$.
