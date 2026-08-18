# 112.03 — Verdict on requirement d5

## 0. Verdict: **(b) satisfied only formally**

> The inequality holds, and no counterexample survives a wide search — but
> the cone has **no sections-like reading**, so it cannot yet serve the role
> d5 plays in the classical Hodge-index proof.  This is not (a), and it is
> not (c).

| item | result |
|---|---|
| $D_f\cdot H>0$ for $f\ge0$ | **holds** — but trivially (112_01) |
| $f\ge0\iff u_f$ convex | **holds**, proved and verified (112_02 §2) |
| disjoint-support test: $I_\partial(D_f,D_g)\ge0$ | **no counterexample** in 142 pairs (112_02 §3) |
| $D_f^2<0$ possible | **yes** — and this is *expected*, not a refutation (§2) |
| sections-like meaning for $\{f\ge0\}$ | **absent** — the gap |

## 1. Why Task 1 does not count

$H=(1,1,0,\dots)$ in evaluation coordinates, so
$I_\partial(D_f,H)=\widehat f(0)+\widehat f(1)
=\int_0^\infty f(r)\frac{dr}r+\int_0^\infty f(r)\,dr$,
manifestly $>0$ when $f\ge0$, $f\not\equiv0$.

This is a restatement of the positivity of an integral.  It is recorded as
holding, and as carrying no geometric content — exactly the circular pattern
this programme has been burned by twice (a form *defined* hyperbolic then
"proved" hyperbolic; a vector reverse-engineered from its target).

## 2. Negative self-intersection is expected, not a refutation

With $f=g$ a narrow bump the zero sum outruns the polar terms and
$I_\partial(D_f,D_f)<0$.  Measured on log-Gaussian bumps ($a=0$, $s=0.05$):
polar $=0.03146$, zero sum $=0.04316$, total $=-0.01171$, stable to ten
digits across truncations at 50, 100, 200 and 300 zeros.

**This does not refute the cone.**  Classically an effective divisor may have
negative self-intersection: the exceptional curve $E$ of a blowup of
$\mathbb P^2$ is irreducible and effective with $E^2=-1$.  The classical
statement is narrower — $D,D'$ effective **with no common component** implies
$D\cdot D'\ge0$ — so the falsifiable test requires *disjoint supports*, which
log-Gaussians (strictly positive everywhere) cannot supply.

Arguably $D^2<0$ is a good sign: it says the form is not positive-definite on
the cone, which is what a surface with a one-dimensional positive direction
should look like.

## 3. The falsifiable test, run properly

142 pairs $f,g\ge0$ with **genuinely disjoint** compact supports (centres
$1..9$ and $16$ in $\log r$, widths $0.1,0.15,0.2,0.3$), each evaluated at two
truncation depths.  Result: **0 negative, 0 sign flips**; the most negative
full-depth value was $+0.00225$.  Convergence of the truncated zero sum was
checked by refinement ($N_z=30,60,90,120$; increments
$1.9\times10^{-6},\ 2.5\times10^{-7},\ 2.3\times10^{-8}$), so a negative value,
had one occurred, would not have been a truncation artifact.  The control
clause confirms the apparatus *can* detect negativity when present (§2).

This is **evidence, not proof**.  A finite search cannot establish a
universally quantified inequality, and no proof is offered.

## 4. What is actually missing

In classical geometry "effective" is not a convenience: $D$ is effective iff
$h^0(D)>0$, i.e. iff $D$ is the divisor of a genuine global section.  What
112_02 establishes is that $f\ge0$ is equivalent to convexity of the DC
potential $u_f$ (since $u_f''(r)=f(r)/r$), i.e. to "no subtraction is needed
in the decomposition $U_f=U_{f^+}-U_{f^-}$".

That is a real characterization, and it is **not** a sections statement.  No
$h^0$ exists in this category — its construction is requirement d3/d4 of the
backward map, and is blocked upstream by d1.  Until $h^0$ exists, "effective"
here means "nonnegative density", and the classical proof's step *"$h^0(nD)\to
\infty$, hence $nD$ is effective"* has no target to land in.

> **d5 is therefore satisfied only formally: the inequality is available, the
> cone is not known to be the right one, and it cannot be known to be until
> $h^0$ exists.**

## 5. Scope

**Proved here.** The Task-1 inequality (112_01); $f\ge0\iff u_f$ convex
(112_02 §2).

**Verified numerically.** The disjoint-support search (142 pairs, two depths);
truncation convergence by refinement; the negative self-intersection of §2;
the identity $u_f''=f(r)/r$ against numerical differentiation to $1.6\times
10^{-7}$.

**Read from source, not re-derived.** 107_241 Theorem 3.1 and the evaluation
coordinates; 107_237's DC potentials and $u_f''(r)=f(r)/r$.

**Not established, and explicitly not claimed.** That $I_\partial(D_f,D_g)\ge0$
for *all* disjoint-support $f,g\ge0$ — 142 pairs is evidence, not a theorem.
That $\{f\ge0\}$ is the geometrically correct cone.  Any $h^0$, any sections
theory, any Riemann–Roch.  Anything about RH.

`ROW_A_STATUS` unchanged.  Nothing here bears on RH.

## 6. Verifier

`112_03_verdict.py` re-runs the two prior verifiers as subprocesses and
confirms both exit 0.
