# 108.40 — Stage 4 operator form: $\Gamma_\R$ as a zeta-regularized determinant

## 0. Result

108_39 §3 established the archimedean identity of Stage 4 only as an
identity of meromorphic functions, and flagged as open the reading Paper
40's item (2) actually asks for: $\Gamma_\R$ as a **determinant of an
operator**. This note supplies that reading, in the classical
zeta-regularized-determinant sense of Ray–Singer / Lerch, along the route of
Deninger (*Local $L$-factors of motives and regularized determinants*,
Invent. Math. 107, 1992).

> \[
>  \boxed{\;\det{}_{\mathrm{reg}}(s-\Theta)\;=\;c(s)\cdot\Gamma_\R(s)^{-1},
>  \qquad c(s)=2^{1-s/2}\pi^{(1-s)/2}=2\sqrt\pi\,(2\pi)^{-s/2}\;}
> \]
> where $\Theta$ is the operator with pure point spectrum $\{-2n:n\ge0\}$,
> each eigenvalue simple, and $\det_{\mathrm{reg}}$ is the zeta-regularized
> determinant of Definition 1.2 below.

The prefactor $c(s)$ is **derived**, not guessed, in §4. Every ingredient of
the spectrum of $\Theta$ is read off the pole structure of $\Gamma(s/2)$
alone; no zero of $\zeta$ or of $\xi$ enters any definition (§6).

## 1. The operator $\Theta$ and its regularized determinant

> ### Definition 1.1 (the archimedean fibre operator)
> Let $\mathcal H=\ell^2(\Z_{\ge0})$ with orthonormal basis $\{e_n\}_{n\ge0}$,
> and let $\Theta$ be the diagonal operator $\Theta e_n=-2n\,e_n$, densely
> defined on the finite linear span of the $e_n$ and essentially self-adjoint
> there (a diagonal operator with real eigenvalues on an orthonormal basis is
> symmetric on that domain, and its closure is self-adjoint with spectrum
> equal to the closure of $\{-2n:n\ge0\}$, which is already closed and
> discrete). Concretely $\Theta=-2N$, where $N$ is the number operator of a
> single quantum harmonic oscillator (equivalently, of a rank-one Fock
> space). Each eigenvalue $-2n$ has multiplicity one.

> ### Definition 1.2 (zeta-regularized determinant)
> For $s\notin\{-2n:n\ge0\}$, let
> \[
>  \zeta_\Theta(z,s):=\sum_{n\ge0}(s+2n)^{-z},
> \]
> the "spectral zeta function" of $s-\Theta$ (the sum of $(s-\lambda)^{-z}$
> over eigenvalues $\lambda$ of $\Theta$). This series converges absolutely
> for $\Re z>1$, uniformly on compacta in $s$ avoiding the spectrum, and
> defines a holomorphic function of $z$ there. We use throughout the fact,
> proved in §2, that $\zeta_\Theta(z,s)=2^{-z}\zeta_H(z,s/2)$ with $\zeta_H$
> the Hurwitz zeta function; since $\zeta_H(z,x)$ continues meromorphically
> to $\C$ with its only pole a simple one at $z=1$ (classical; e.g. Whittaker
> & Watson §13.13), $\zeta_\Theta(\cdot,s)$ continues to the same domain and
> in particular is holomorphic at $z=0$. Define
> \[
>  \log\det{}_{\mathrm{reg}}(s-\Theta):=-\left.\frac{d}{dz}\zeta_\Theta(z,s)
>  \right|_{z=0},
>  \qquad
>  \det{}_{\mathrm{reg}}(s-\Theta):=\exp\Big(-\zeta_\Theta'(0,s)\Big).
> \]
> This is the standard Ray–Singer zeta-regularized determinant, applied to
> the (non-negative, discrete) family of complex numbers $s+2n$ rather than
> to a differential operator's eigenvalues directly; the definition makes
> sense verbatim whenever the family is $s$-shifted from a fixed non-negative
> discrete spectrum, which is the case here.

## 2. The scaling lemma

> ### Lemma 2.1
> Let $(\mu_n)_{n\ge0}$ be a sequence with $\mu_n>0$ (or, more generally,
> $\Re\mu_n\to+\infty$ so that $\sum\mu_n^{-z}$ converges for $\Re z\gg0$),
> spectral zeta function $\zeta_\mu(z)=\sum_n\mu_n^{-z}$ continuing
> meromorphically to a neighborhood of $z=0$ with $z=0$ a regular point, and
> let $c>0$ be a real constant. Then $(c\mu_n)_{n\ge0}$ has the same
> regularity at $z=0$ and
> \[
>  \det{}_{\mathrm{reg}}(c\mu)=c^{\,\zeta_\mu(0)}\det{}_{\mathrm{reg}}(\mu).
> \]

**Proof.** For $\Re z$ large enough that $\sum\mu_n^{-z}$ converges
absolutely, $(c\mu_n)^{-z}=c^{-z}\mu_n^{-z}$ termwise, so
$\zeta_{c\mu}(z)=c^{-z}\zeta_\mu(z)$ on that half-plane. The right side is a
product of the entire function $z\mapsto c^{-z}=e^{-z\log c}$ (using $c>0$,
so $\log c$ is the real logarithm, no branch ambiguity) with the
meromorphic continuation of $\zeta_\mu$; by uniqueness of analytic
continuation the identity $\zeta_{c\mu}(z)=c^{-z}\zeta_\mu(z)$ holds as an
identity of meromorphic functions on the common domain of continuation, in
particular near $z=0$. Both sides are then holomorphic at $z=0$ (given), so
we may differentiate termwise there:
\[
 \zeta_{c\mu}'(z)=-\log c\cdot c^{-z}\zeta_\mu(z)+c^{-z}\zeta_\mu'(z),
 \qquad
 \zeta_{c\mu}'(0)=-\log c\cdot\zeta_\mu(0)+\zeta_\mu'(0).
\]
Hence $-\zeta_{c\mu}'(0)=\log c\cdot\zeta_\mu(0)-\zeta_\mu'(0)$, i.e.
$\log\det_{\mathrm{reg}}(c\mu)=\zeta_\mu(0)\log c+\log\det_{\mathrm{reg}}(\mu)$,
which exponentiates to the claim. $\square$

## 3. Two classical facts about the Hurwitz zeta function

These are read from the classical literature (Lerch 1894; see also
Whittaker & Watson, *A Course of Modern Analysis*, §13.21, and the
Euler–Maclaurin continuation in DLMF 25.11) and are checked independently
below against a from-scratch numerical implementation, so for our purposes
they carry both labels: read from source **and** verified numerically.

> ### Fact 3.1 (value at $z=0$)
> For $x$ not a non-positive integer, $\zeta_H(0,x)=\tfrac12-x$.

> ### Fact 3.2 (Lerch's formula)
> For $x$ not a non-positive integer,
> $\zeta_H'(0,x)=\log\Gamma(x)-\tfrac12\log(2\pi)$, equivalently
> \[
>  \det{}_{\mathrm{reg}}\big(\{x+n\}_{n\ge0}\big)=\exp(-\zeta_H'(0,x))
>  =\frac{\sqrt{2\pi}}{\Gamma(x)}.
> \]

At $x=1$, Fact 3.2 specializes to the classical
$\zeta'(0)=-\tfrac12\log(2\pi)$ (since $\Gamma(1)=1$), which is the
sanity-check case used to anchor the general statement.

## 4. Main theorem: the prefactor $c(s)$

> ### Theorem 4.1
> $\det_{\mathrm{reg}}(s-\Theta)=c(s)\,\Gamma_\R(s)^{-1}$ with
> \[
>  c(s)=2^{1-s/2}\pi^{(1-s)/2}=2\sqrt\pi\,(2\pi)^{-s/2}.
> \]

**Proof.** Write $s+2n=2\big(n+\tfrac s2\big)$, so with
$\mu_n=n+s/2$ (spectral zeta function $\zeta_H(z,s/2)$, regular at $z=0$ by
Fact 3.1–3.2), Lemma 2.1 with $c=2$ gives
\[
 \zeta_\Theta(z,s)=2^{-z}\zeta_H(z,s/2),
 \qquad
 \log\det{}_{\mathrm{reg}}(s-\Theta)
 =\log2\cdot\zeta_H(0,s/2)-\zeta_H'(0,s/2).
\]
By Facts 3.1 and 3.2 with $x=s/2$, and writing $\tfrac12\log(2\pi)
=\tfrac12\log2+\tfrac12\log\pi$,
\[
 \log\det{}_{\mathrm{reg}}(s-\Theta)
 =\log2\cdot\Big(\tfrac12-\tfrac s2\Big)-\log\Gamma\big(\tfrac s2\big)
  +\tfrac12\log2+\tfrac12\log\pi
 =\big(1-\tfrac s2\big)\log2-\log\Gamma\big(\tfrac s2\big)+\tfrac12\log\pi,
\]
where the last step collects the two $\log2$ terms,
$\big(\tfrac12-\tfrac s2\big)+\tfrac12=1-\tfrac s2$. On the other hand
\[
 \log\big(c(s)\Gamma_\R(s)^{-1}\big)
 =\log c(s)+\tfrac s2\log\pi-\log\Gamma\big(\tfrac s2\big),
\]
using $\Gamma_\R(s)^{-1}=\pi^{s/2}/\Gamma(s/2)$. Equating the two
expressions for $\log\det_{\mathrm{reg}}(s-\Theta)$ and solving for
$\log c(s)$,
\[
 \log c(s)=\big(1-\tfrac s2\big)\log2+\tfrac12\log\pi-\tfrac s2\log\pi
 =(1-\tfrac s2)\log2+\big(\tfrac12-\tfrac s2\big)\log\pi,
\]
i.e. $c(s)=2^{1-s/2}\pi^{(1-s)/2}$. Rewriting,
$2^{1-s/2}\pi^{(1-s)/2}=2\cdot2^{-s/2}\cdot\pi^{1/2}\cdot\pi^{-s/2}
=2\sqrt\pi\,(2\pi)^{-s/2}$, the second stated form. $\square$

**Remark (how $c(s)$ was found, not just checked).** The derivation is
forced: once Lemma 2.1 fixes the scaling exponent $\zeta_H(0,s/2)=\tfrac12
-\tfrac s2$ and Fact 3.2 fixes the base determinant $\sqrt{2\pi}/\Gamma(x)$,
the algebra above has no remaining freedom — $c(s)$ is whatever elementary
factor is left over after matching $\det_{\mathrm{reg}}(s-\Theta)$ against
$\Gamma_\R(s)^{-1}=\pi^{s/2}/\Gamma(s/2)$. No numerical fitting or guessing
of $c(s)$ occurs anywhere in this note.

## 5. Numerical verification

`108_40_stage_4_the_archimedean_determinant.py` implements, from scratch
(`math`/`cmath` only, no `scipy`, no `mpmath`):

* **Gamma**: Lanczos approximation ($g=7$, $n=9$ coefficients) for
  $\Re z\ge\tfrac12$, extended to $\Re z<\tfrac12$ by the reflection formula
  $\Gamma(z)\Gamma(1-z)=\pi/\sin(\pi z)$; and a `loggamma` built the same
  way. Checked against $\Gamma(\tfrac12)=\sqrt\pi$ (to $10^{-13}$),
  $\Gamma(5)=24$ (to $10^{-11}$), and the recurrence
  $\Gamma(z+1)=z\Gamma(z)$ at a complex point.
* **Hurwitz zeta**: the standard Euler–Maclaurin continuation (direct sum of
  15 terms, correction term $(a+N)^{1-z}/(z-1)+\tfrac12(a+N)^{-z}$, plus 8
  Bernoulli-number correction terms), valid for all complex $z\ne1$ and all
  the $a$ used here. Checked against $\zeta_H(0,x)=\tfrac12-x$ at six
  points (real and complex, $<10^{-11}$), and against
  $\zeta_H(2,1)=\pi^2/6$, $\zeta_H(4,1)=\pi^4/90$ (both $<10^{-12}$).
* **Lerch's formula** (Fact 3.2) itself, checked independently of its role
  in Theorem 4.1: $\zeta_H'(0,x)$ is computed by a central finite
  difference in $z$ (step $h$ and $h/2$, confirming the error shrinks
  under halving — a convergence test, not a bare threshold) and compared
  against $\log\Gamma(x)-\tfrac12\log(2\pi)$ from the from-scratch
  `loggamma`. Max residual at $h=5\times10^{-4}$ was $2.6\times10^{-7}$
  after starting at $1.05\times10^{-6}$ for $h=10^{-3}$, consistent with
  the expected $O(h^2)$ convergence of a central difference.
* The base product formula $\det_{\mathrm{reg}}(\{x+n\})=\sqrt{2\pi}/\Gamma(x)$
  directly, at five points.
* **Theorem 4.1 itself**, at nine complex points $s$ avoiding the pole set
  $\{0,-2,-4,\dots\}$ (including points with negative real part and
  nonzero imaginary part), computing $\det_{\mathrm{reg}}(s-\Theta)$ purely
  from the Hurwitz-zeta side ($\zeta_\Theta(z,s)=2^{-z}\zeta_H(z,s/2)$,
  differentiated numerically) and $c(s)\Gamma_\R(s)^{-1}$ purely from the
  Gamma side (Lanczos) — two independent code paths — with maximum relative
  residual $1.3\times10^{-6}$, and a second run at half the step size
  confirming the residual shrinks (not a numerical accident of one $h$).
* The two closed forms of $c(s)$ agreeing to $10^{-12}$ (an algebra check on
  the write-up, not a mathematical claim).

All checks pass; `python3 108_40_stage_4_the_archimedean_determinant.py`
exits 0 with `VERDICT: ALL CHECKS PASS`.

## 6. The source rule: the spectrum is read off $\Gamma(s/2)$ alone

> ### Proposition 6.1
> $\{-2n:n\ge0\}$ is exactly the set of poles of $\Gamma(s/2)$ as a function
> of $s$ (equivalently, of $s\mapsto\Gamma_\R(s)$, since $\pi^{-s/2}$ is
> entire and zero-free). No zero of $\zeta$ or of $\xi$ is used, referenced,
> or needed to state Definition 1.1.

**Proof.** $\Gamma(w)$ has simple poles exactly at $w=0,-1,-2,\dots$
(classical). Setting $w=s/2$, these occur exactly at $s=0,-2,-4,\dots$,
i.e. $s=-2n$, $n\ge0$. $\square$

This is confirmed numerically in the verifier ("5" and "5$'$"): the growth
of $|\Gamma(s/2)|$ near $s=-2n$ for $n=0,1,2,3$ is pole-like (doubling the
distance to the pole roughly doubles $|\Gamma|$), while at the intervening
odd negative integers $s=-1,-3$ (where $s/2=-\tfrac12,-\tfrac32$ are
perfectly regular points of $\Gamma$) it is not.

**Why this settles the source-rule question, and not just formally.** The
point $s=0$ ($n=0$ in the spectrum of $\Theta$) is a pole of $\Gamma(s/2)$,
hence lies in $\mathrm{spec}$ by Proposition 6.1 — but it is **not** a
zero of $\zeta$: $\zeta(0)=-\tfrac12\ne0$ (check "6" in the verifier,
via $\zeta_H(0,1)=\zeta(0)$, matching $-\tfrac12$ to $10^{-10}$). It is also
not a zero of $\xi$: at $s=0$ the polar factor $s(s-1)/2$ of $\xi$ has a
simple zero that exactly cancels the simple pole of $\Gamma_\R$, leaving
$\xi(0)$ finite and nonzero. So the spectrum of $\Theta$ contains a point
that is manifestly *not* a zero of $\zeta$ or of $\xi$; it is in the
spectrum solely because it is a pole of $\Gamma(s/2)$. This is direct
evidence — not merely an assertion — that Definition 1.1 is read off the
archimedean factor alone. (For $n\ge1$ the points $s=-2n$ happen to
coincide with the trivial zeros of $\zeta$, since $\zeta(-2n)=0$ for
$n\ge1$ by the functional equation together with the pole of $\Gamma_\R$
there — but that coincidence is a *consequence* of the functional equation
for $\zeta$, read off *after* the fact; it plays no role in, and is not
needed for, Definition 1.1 or Theorem 4.1, both of which are stated and
proved using $\Gamma$ alone.)

## 7. What this does and does not give

**Gives.** An candid operator $\Theta$ (Definition 1.1, an essentially
self-adjoint diagonal operator with explicit simple spectrum) and its
zeta-regularized determinant (Definition 1.2, the standard Ray–Singer /
Lerch construction), together with a full proof (Theorem 4.1) that this
determinant reproduces $\Gamma_\R(s)^{-1}$ up to the explicit elementary
factor $c(s)=2^{1-s/2}\pi^{(1-s)/2}$. This is the operator-theoretic reading
of Stage 4 that 108_39 §3 left open, in the classical sense in which
Deninger (1992) realizes local $L$-factors as regularized determinants, and
Serre (1970, *Facteurs locaux des fonctions zêta des variétés algébriques*)
first proposed reading the archimedean factor as a (formally divergent,
hence regularized) Euler factor of a "Frobenius at infinity" acting on a
Hodge-theoretic cohomology group with eigenvalues indexed by $n\ge0$.

**Does not give — and this is the point of this section, not a footnote.**

* **No intersection-theoretic content.** A zeta-regularized determinant is
  an analytic invariant: it is defined by meromorphic continuation of a
  Dirichlet series built from a *spectrum* (a multiset of complex numbers),
  and Definitions 1.1–1.2 use nothing more than that multiset. There is no
  variety, no sheaf, no cohomology group with a specified geometric origin,
  and no intersection pairing anywhere in this construction. Exhibiting
  $\Gamma_\R$ as such a determinant makes it a determinant of *an* operator
  in the same sense that any sequence tending to infinity fast enough has a
  zeta-regularized product — it does not by itself supply a space on which
  $\Theta$ acts as an actual geometric correspondence (a "Frobenius").
* **No known geometric model for $\Theta$.** The operator of Definition 1.1
  is presented purely by its spectrum ($\ell^2(\Z_{\ge0})$ with $\Theta$
  diagonal, equivalently minus twice the number operator of one harmonic
  oscillator). This matches the *heuristic* dictionary used throughout the
  Deninger/Serre/Kurokawa/Connes literature on archimedean local factors —
  the harmonic-oscillator Fock space repeatedly appears there as the
  "cohomology of the fibre at infinity" — but in every one of those
  treatments this remains a formal analogy: there is no known algebraic
  variety over $\R$ or $\C$, nor a known correspondence on it, realizing
  $\Theta$ as an actual Frobenius-type endomorphism of an actual
  cohomology theory with an actual intersection pairing. This note does not
  change that; it only makes the *determinant* identity precise and proved,
  which is a narrower and purely analytic statement.
* **Stage 5 is untouched.** As in 108_39, making either side of Theorem 4.1
  into an intersection number is a separate, unfinished problem, not
  addressed here.
* **Nothing about $\RH$.** No zero of $\zeta$ or $\xi$ off the trivial set
  enters anything in this note (§6), and no claim about the location of
  zeros is made or implied anywhere here.

The candid summary: Stage 4 now has an operator form (Definition 1.1,
Theorem 4.1) in addition to the identity form of 108_39, and the operator
form is a genuine theorem about a genuine (if simply described) operator —
but "operator" here means "self-adjoint operator with a zeta-regularized
determinant," an analytic notion, not "algebraic correspondence on a
geometric fibre with an intersection pairing," a geometric one. Reading
Theorem 4.1 as intersection theory would be a further, unproven, and at
present unsupported step.

## 8. Scope

**Proved (written proof in this note).** Lemma 2.1 (scaling law for
zeta-regularized determinants); Theorem 4.1 (the prefactor $c(s)$, derived
in full from Lemma 2.1 and Facts 3.1–3.2); Proposition 6.1 (the spectrum of
$\Theta$ is exactly the pole set of $\Gamma(s/2)$).

**Read from source (classical, cited).** Fact 3.1
($\zeta_H(0,x)=\tfrac12-x$) and Fact 3.2 (Lerch's formula
$\zeta_H'(0,x)=\log\Gamma(x)-\tfrac12\log(2\pi)$); the Euler–Maclaurin
meromorphic continuation of the Hurwitz zeta function and the location of
its unique pole at $z=1$; the pole structure of $\Gamma$ at the
non-positive integers; $\zeta(-2n)=0$ for $n\ge1$ (used only in the
parenthetical remark of §6, not in any proof).

**Verified numerically (from-scratch implementations, no scipy/mpmath).**
Gamma against $\Gamma(\tfrac12)=\sqrt\pi$, $\Gamma(5)=24$, and its
recurrence; Hurwitz zeta against $\zeta_H(0,x)=\tfrac12-x$ and
$\zeta_H(s,1)=\zeta(s)$ at $s=2,4$; Lerch's formula itself, independently
of its use in Theorem 4.1, with a convergence (not threshold-only) check;
the base regularized product $\sqrt{2\pi}/\Gamma(x)$; Theorem 4.1 at nine
complex points with a convergence check; the pole-vs-regular distinction of
Proposition 6.1; $\zeta(0)=-\tfrac12$.

**Not established.** Any intersection-theoretic, motivic, or geometric
realization of $\Theta$; any relation between this note and Stage 5; any
statement about $\RH$ or about the nontrivial zeros of $\zeta$ or $\xi$
(none are referenced by any definition here, per Proposition 6.1 and the
discussion following it).

`ROW_A_STATUS` unchanged. Nothing here bears on $\RH$.

## 9. Verifier

`108_40_stage_4_the_archimedean_determinant.py` implements Gamma (Lanczos +
reflection) and the Hurwitz zeta function (Euler–Maclaurin) from scratch,
checks both against known closed-form values, verifies Lerch's formula and
the base regularized-product formula independently, verifies the main
identity of Theorem 4.1 at nine complex points with a step-halving
convergence check, verifies the two algebraic forms of $c(s)$ agree, and
confirms the source-rule facts of §6 ($\Gamma(s/2)$'s poles at
$s=0,-2,-4,-6$ vs. its regularity at $s=-1,-3$; and $\zeta(0)=-\tfrac12$).
All checks pass; exit code 0.
