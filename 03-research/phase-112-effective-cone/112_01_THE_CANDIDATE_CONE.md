# 112.01 -- The candidate cone: $f\ge 0$, and the easy half

## 0. Setup, quoted exactly

From the source material (§ Background, quoted in the phase-112 task, taken
verbatim from 107_241 and 107_237): $\widehat f(w)=\int_0^\infty f(r)r^{w-1}dr$,

$$
I_\partial(D_f,D_g)=\widehat f(0)\overline{\widehat g(1)}
+\widehat f(1)\overline{\widehat g(0)}
-\sum_{\rho}m_\rho\,\widehat f(\rho)\overline{\widehat g(\rho')},
$$

$H=F_v+F_h=(1,1,0,\dots)$ in evaluation coordinates, i.e. $\widehat
H(0)=\widehat H(1)=1$ and $\widehat H(\rho)=0$ for every zero $\rho$.

**Named assumption A1 (extension of the pairing to $H$).** $H$ is treated as
an element of the ambient target space $\mathbb C^{\{0,1\}}\oplus\mathbb
C^{Z}$ of Lemma 2.2 (107_241), not as $D_h$ for a literal test function
$h$. This is licensed by 107_241 Lemma 2.2 itself ("(2.1) is the pullback
of an explicit form on **the target**") and by §4 of the same file, which
treats $H_{\mathrm{ruling}}$ as spanned by the two polar coordinate
functionals directly. The formula for $I_\partial(D_f,H)$ below is the
same bilinear expression (2.1), evaluated at the coordinates of $H$.

**Named assumption A2 (test class).** $f$ ranges over $\mathcal
A=C_c^\infty(\mathbb R_+^\times)$, i.e. $f$ is smooth and compactly
supported in $(0,\infty)$, bounded away from both $0$ and $\infty$ (matches
107_237 §2: $f\in C_c((0,\infty),\mathbb R)$, supported in $[A,B]$,
$0<A<B<\infty$). Under A2, $\widehat f(0)=\int_0^\infty f(r)r^{-1}dr$ and
$\widehat f(1)=\int_0^\infty f(r)\,dr$ both converge absolutely: the
integrands are continuous, compactly supported, hence bounded and
integrable. No further hypothesis is needed. (If one allowed $f$ to have
support touching $r=0$ or extending to $r=\infty$, convergence of
$\widehat f(0)$ or $\widehat f(1)$ would require extra decay/vanishing
hypotheses; this phase does not need that generality and does not assume
it.)

## 1. The computation

### Lemma 1.1

For every $f\in\mathcal A$,
$$
I_\partial(D_f,H)=\widehat f(0)+\widehat f(1).
$$

**Proof.** By A1, apply (2.1) with $g$'s coordinates replaced by $H$'s:
$\widehat H(1)=1$, $\widehat H(0)=1$, both real, and $\widehat
H(\rho')=0$ for every $\rho$. Hence
$$
I_\partial(D_f,H)=\widehat f(0)\cdot\overline 1+\widehat f(1)\cdot\overline
1-\sum_\rho m_\rho\,\widehat f(\rho)\cdot\overline 0
=\widehat f(0)+\widehat f(1). \qquad\square
$$

This matches 107_237 (3.4): $\widehat f(0)=M_0(f)=D_f\cdot F_1$ and
$\widehat f(1)=M_1(f)=D_f\cdot F_2$, so $I_\partial(D_f,H)=D_f\cdot
F_v+D_f\cdot F_h$ is exactly $D_f\cdot H$ under bilinearity, independent of
which ruling is labelled $F_1$ vs.\ $F_2$.

### Theorem 1.2 (the easy half)

If $f\in\mathcal A$, $f\ge0$ a.e., $f\not\equiv0$, then
$I_\partial(D_f,H)>0$.

**Proof.** Under A2 the two integrals in Lemma 1.1 converge. Since $f\ge0$
and not a.e.\ zero, and $r^{-1}>0$, $1>0$ on the support of $f$,
$$
\widehat f(0)=\int_0^\infty f(r)\,\frac{dr}r\ \ge 0,\qquad
\widehat f(1)=\int_0^\infty f(r)\,dr\ \ge 0,
$$
and since $f$ is continuous, nonnegative, and not identically zero, it is
strictly positive on a set of positive measure inside its support, so
both integrals are **strictly** positive. Hence
$I_\partial(D_f,H)=\widehat f(0)+\widehat f(1)>0$. $\square$

## 2. Why this is not yet the answer

Theorem 1.2 is correct, but by itself it is a restatement of positivity of
an integral of a nonnegative function against two positive weights ($1/r$
and $1$) -- it says nothing about geometry. It would be circular to declare
this the content of d5 and stop; that is exactly the trap flagged in the
task statement. The candidate cone must additionally be tested for
whether $\{f\ge0\}$ has *any* meaning beyond "the two coordinates that
happen to enter $I_\partial(\cdot,H)$ are manifestly positive when $f\ge0$"
-- that is Task 2, taken up in `112_02_IS_IT_THE_RIGHT_CONE.md`.

## 3. Scope

**Proved here.** Lemma 1.1 (closed form of $I_\partial(D_f,H)$); Theorem
1.2 ($f\ge0,\ne0\implies I_\partial(D_f,H)>0$, under A2).

**Read from source, not re-derived.** The pairing formula (2.1); the
coordinates of $H$; $D_f\cdot F_1=\widehat f(0)$, $D_f\cdot F_2=\widehat
f(1)$ (107_237 (3.4)).

**Verified numerically.** Lemma 1.1 and Theorem 1.2 on explicit bump
functions (`112_01_the_candidate_cone.py`), together with a control clause
that a sign-reversed candidate ($f\le0$) gives a negative value, so the
check is not vacuous.

**Not established, and explicitly not claimed.** That $\{f\ge0\}$ is the
*correct* effective cone in the classical (sections) sense -- that is
Task 2's question, and Theorem 1.2 does not answer it.

## 4. Verifier

`112_01_the_candidate_cone.py` builds several $f\ge0$ (and, as a control,
$f\le0$) bump functions in $\mathcal A$, computes $\widehat f(0)$,
$\widehat f(1)$ by direct numerical quadrature, checks the closed form of
Lemma 1.1 against the boxed pairing formula (2.1) evaluated at $H$'s
coordinates directly (not merely asserting the closed form), checks
positivity for $f\ge0$, and checks the control (negativity for $f\le0$).
