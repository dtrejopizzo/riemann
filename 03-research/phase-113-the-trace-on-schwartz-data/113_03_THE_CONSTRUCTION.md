# 113.03 — The construction: $\mathfrak T(h)$ as a genuinely convergent sum over all places

## 0. What this replaces

107_239 §3 defined $\mathfrak T(h):=\mathfrak T_{S(h)}(h)$ using a finite
place-set $S(h)$ that stabilizes because compact support bounds the
contributing primes. 111_03 §3 identified that this mechanism does not
exist for Schwartz $h$. 113_01–113_02 built the replacement: a genuinely
infinite sum over all places, shown finite under an explicit, named
admissibility class. This note states it as a Definition and a Theorem, and
nothing more — it does not re-derive 113_01–113_02, and it does not re-open
111_01's archimedean treatment.

## 1. The admissibility class

> ### Definition 1.1 (admissible test data for the direct construction)
> $h:\mathbb R_+^\times\to\mathbb C$, $\tilde h(x)=h(e^x)$, is **admissible**
> if
> $$\tilde h\in\mathcal S_\eta\ \text{for some }\eta>1
> \qquad\text{and}\qquad h(1)=\tilde h(0)=0.$$
> Write $\mathcal A$ for this class.

The two conditions are independent and both load-bearing: $\eta>1$ is
Theorem 2.1 of 113_02 (and, on the archimedean side, 111_01 Theorem
111.1.3's own threshold for $\widehat h(1)$); $h(1)=0$ is 113_01 Theorem
4.1's canonicity condition. Neither is vacuous: $\mathcal S_{>1}$ is
infinite-dimensional (111_00 §3), and $h(1)=0$ is a single linear condition
on it, cutting a codimension-$1$ (not codimension-$\infty$) subspace, still
infinite-dimensional.

## 2. The finite-place sum

> ### Definition 2.1 (the finite-place trace)
> For $h\in\mathcal A$,
> $$\mathfrak T_{\rm fin}(h):=\sum_p\Big(\sum_{n\ge1}h(p^n)
> +\sum_{m\ge1}h(p^{-m})p^{-m}\Big).$$

> ### Theorem 2.2
> The sum in Definition 2.1 converges absolutely, for every $h\in\mathcal
> A$.

**Proof.** 113_01 Theorem 4.1: since $h(1)=0$, every local integral's
canonical value is $A_p(h)+B_p(h)$ (the shell-$0$ term vanishes under every
regularization scheme). 113_02 Theorem 2.1: since $\tilde h\in\mathcal
S_\eta$, $\eta>1$, $\sum_p(A_p(h)+B_p(h))$ converges absolutely. $\square$

This is not a new computation; it is the composition of 113_01 and 113_02,
recorded here as the object that actually enters the definition below.

## 3. The archimedean place

The archimedean local integral is not separately re-derived in this phase.
Per the task's own instruction and 111_01's scope, its contribution is
taken from 111_01 as follows, stated precisely so the citation is not
overclaimed.

> **What 111_01 established** (Theorem 111.1.3, Lemma 111.1.4, Theorem
> 111.1.5, all for $\tilde f,\tilde g\in\mathcal S_\eta$, $\eta>1$): the
> polar terms $\widehat h(0),\widehat h(1)$ exist, and the zero sum
> $\sum_\rho\widehat h(\rho)\overline{\cdots}$ converges absolutely with
> enormous margin. **What 111_01 flagged as unresolved** (Assumption T,
> §3): whether the *trace-side* identity $\mathfrak T(h)=\widehat h(0)
> +\widehat h(1)-\sum_\rho\widehat h(\rho)$ — established, presumably, for
> compactly-supported $h$ — extends verbatim to $\mathcal S_{>1}$. This is
> exactly the statement needed to say the archimedean piece of
> $\mathfrak T$ is finite as an operator-trace limit, not merely that the
> Weil-formula right-hand side built from it is finite.

> ### Definition 3.1 (the archimedean contribution, as inherited)
> For $h\in\mathcal A$ (in particular $\tilde h\in\mathcal S_\eta$,
> $\eta>1$), define
> $$\mathfrak T_\infty(h):=\widehat h(0)+\widehat h(1)-\sum_\rho\widehat h(\rho),$$
> finite by 111_01 Theorems 111.1.3 and 111.1.5, **under Assumption T**
> (111_01 §3) identifying this with the archimedean trace-side limit.

This phase does not discharge Assumption T; it is carried forward exactly
as 111_01 stated it, not silently absorbed.

## 4. The construction

> ### Definition 4.1 (the direct construction of $\mathfrak T$ on $\mathcal A$)
> For $h\in\mathcal A$,
> $$\boxed{\ \mathfrak T(h):=\mathfrak T_\infty(h)+\mathfrak T_{\rm fin}(h).\ }$$

> ### Theorem 4.2 (convergence)
> $\mathfrak T(h)$ is a well-defined finite complex number for every
> $h\in\mathcal A$, and it does not depend on any regularization-scheme
> choice at the finite places (113_01 Theorem 4.1, using $h(1)=0$).

**Proof.** $\mathfrak T_\infty(h)$ is finite by Definition 3.1 (111_01,
under Assumption T). $\mathfrak T_{\rm fin}(h)$ is finite by Theorem 2.2.
A finite sum of two finite numbers is finite. Scheme-independence at the
finite places is 113_01 Theorem 4.1, invoked at $h(1)=0$. $\square$

This is stated as Theorem 4.2 rather than "Theorem: $\mathfrak T$ is
constructed" deliberately: convergence and well-definedness on $\mathcal A$
is exactly what is proved; whether Definition 4.1 *equals* the operator-
trace object of 107_239 (1.4) on this class is not proved (it presupposes
Assumption T at the archimedean place, and inherits from 107_239 the
identification of the finite-place closed form with the semilocal trace
formula, cited, not re-derived, in 113_01 §3 Fact (ii)).

## 5. What this does and does not replace

This construction **replaces** 107_239 §3's finite-$S(h)$ stabilization
mechanism with a genuinely infinite, convergent sum over all places, on the
explicit class $\mathcal A$. It does **not** claim $\mathcal A$ is the
largest possible admissible class (only that it is nonempty and
convergent — sharper thresholds are not sought here), and it does **not**
discharge 111_01's Assumption T, which remains the single largest residual
risk to $\mathfrak T$'s status as a genuine operator-trace regularization
rather than only a Weil-formula-side finite number.

## 6. Scope

**Proved here.** Theorem 2.2 (finite-place convergence, by composition of
113_01–113_02); Theorem 4.2 (well-definedness of $\mathfrak T$ on
$\mathcal A$, modulo Assumption T at the archimedean place, explicitly
flagged, not discharged).

**Read from source, not re-derived.** 111_01 Theorems 111.1.3, 111.1.5 and
Assumption T (archimedean finiteness, cited exactly as 111_01 stated it,
including its own caveat).

**Verified numerically.** Direct evaluation of $\mathfrak T_{\rm fin}(h)$
for an explicit $h\in\mathcal A$ (an odd-in-$x$ Gaussian, $h(1)=0$
identically, $\eta$ arbitrary), confirming stabilization under refinement
in both the shell-truncation $K$ (trivial, since $h(1)=0$) and the prime
bound.

**Not established, and explicitly not claimed.** That $\mathcal A$ is
optimal; that Assumption T holds; that Definition 4.1 equals the
operator-trace object of (1.4) rather than only reproducing its expected
finite value on the class where both sides are known to converge; anything
about RH.

## 7. Verifier

`113_03_the_construction.py` checks: an explicit $h\in\mathcal A$
($\tilde h(x)=xe^{-x^2}$, odd, so $h(1)=0$ exactly and $\eta$ unbounded)
gives a finite, stable value of $\mathfrak T_{\rm fin}(h)$ under refinement
in both the prime bound and (trivially) the shell truncation $K$; a control
$h\notin\mathcal A$ (even Gaussian, $h(1)=1\ne0$) is shown to require an
explicit scheme choice at the finite places (reproducing 113_01's
ambiguity) rather than converging to a scheme-free number, confirming
Definition 1.1's second condition is load-bearing, not decorative.
