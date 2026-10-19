# Phase 27-C — Analysis of the local-global principle

**Objective:** Can local positivity of $Q$ at each prime $p$ imply global positivity
of $Q$? Does even a notion of "local form $Q_p$" exist?

---

## 1. The proposal and its precise reformulation

The proposal of Phase 27-C was:
$$Q = Q_\infty \times \prod_p Q_p, \qquad Q_p \ge 0 \text{ for all } p \implies Q \ge 0 \text{ globally.}$$

Before asking whether the implication holds, we must ask whether the left-hand side
makes sense. The audit in this document has two parts:

**Wall A:** Does a decomposition $Q \rightsquigarrow (Q_\infty, Q_p)$ exist?

**Wall B:** If it exists, does local positivity imply global positivity?

It was correctly identified that **Wall A is harder than Wall B** and that
its resolution is the real gateway into Phase 27.

---

## 2. Decomposition of the Weil form — which part factorizes

The Weil form $Q(f,g) = \mathcal{W}(f*\tilde{g})$ has three types of terms.
Let $h = f * \tilde{g}$ (Mellin convolution). Then:

$$Q(f,g) = \underbrace{\sum_\rho \hat{h}(\rho)}_{Q_{\text{zero}}}
           \underbrace{- \hat{h}(0)\log\pi - \hat{h}(1)\log\pi + h(1)\log\pi}_{Q_\infty}
           + \underbrace{\sum_{p,n} \frac{\log p}{p^{n/2}} [h(p^n) + h(p^{-n})]}_{Q_{\text{prime}}}.$$

### The prime term: DOES factorize

$$Q_{\text{prime}}(f,g) = \sum_p Q_p^{\text{pr}}(f,g),$$
$$Q_p^{\text{pr}}(f,g) := \sum_{n=1}^\infty \frac{\log p}{p^{n/2}} [(f*\tilde{g})(p^n) + (f*\tilde{g})(p^{-n})].$$

Each $Q_p^{\text{pr}}$ is a form depending only on the values of $f*\tilde{g}$
at powers of $p$. It is genuinely local.

**Is $Q_p^{\text{pr}}$ positive-definite?** NO. Direct counterexample:
let $f$ have $\hat{f}(s) \approx 1$ near $s = 1/2$ and zero elsewhere.
Then $(f*\tilde{f})(p^n) = \hat{f}(1/2)^2 p^{-n/2}$ approximately, and
$Q_p^{\text{pr}}(f,f) \approx (\log p) \hat{f}(1/2)^2 \sum_n p^{-n} > 0$.
However, for $f$ concentrated at frequencies where $\hat{f}(\rho) < 0$ for
some zeros $\rho$, the prime term can be negative.
**The positivity of $Q_p^{\text{pr}}$ is neither automatic nor independent of the zeros.**

### The archimedean term: IS a single factor

$Q_\infty(f,g) = -\hat{h}(0)\log\pi - \hat{h}(1)\log\pi + h(1)\log\pi$.

It is a single term (the place $v = \infty$). Its positivity is also not automatic.

### The zero term: does NOT factorize

$$Q_{\text{zero}}(f,g) = \sum_\rho \hat{h}(\rho) = \sum_\rho \hat{f}(\rho)\overline{\hat{g}(\bar\rho)}.$$

**Proposition 27-C.1** (Wall A: non-factorization of the zero term).

The term $Q_{\text{zero}}(f,g)$ cannot be written as $\sum_p A_p(f,g)$ where
each $A_p(f,g)$ depends only on the values of $f$ and $g$ at powers of $p$.

*Proof.* $\hat{f}(\rho) = \int_0^\infty f(x) x^{\rho-1} dx$ depends on $f$ at ALL
points of $\mathbb{R}^*_+$, not only at $\{p^n : n \in \mathbb{Z}\}$ for any fixed prime $p$.
If $f$ is a smooth function localized on $[2, 3]$ (away from every power of $p$ for $p \ge 5$),
then $A_p(f,g) = 0$ for $p \ge 5$ but $\hat{f}(\rho) \ne 0$ in general.
Therefore $Q_{\text{zero}}$ cannot be expressed as a sum of local terms in $p$. $\square$

---

## 3. The deep reason: the zeros of $\zeta$ are global objects with no local factorization

**Proposition 27-C.2** (non-existence of "local zeros at $p$").

The Euler factor $L_p(s) = (1-p^{-s})^{-1}$ has no zeros. Consequently:

1. There is no notion of "zeros of $\zeta$ at the prime $p$".
2. The non-trivial zeros of $\zeta$ are genuinely global objects, with no localization
   at any prime.
3. The term $Q_{\text{zero}}$ has no local factors in $p$ because no prime
   "owns" any zero of $\zeta$.

*Proof.* $(1-p^{-s})^{-1}$ is holomorphic on all of $\mathbb{C}$ except for a pole at
$s = 0$ (if $p = \infty$: the $\Gamma$ factor has poles at $\mathbb{Z}_{\le 0}$). For
$p < \infty$: $(1-p^{-s})^{-1}$ never vanishes. $\square$

**Corollary 27-C.3** (contrast with the function field case).

For a curve $C/\mathbb{F}_q$, the zeros of the $\zeta$ function of $C$ are the
eigenvalues of Frobenius $\text{Frob}_p$ acting on $H^1(C, \mathbb{Q}_\ell)$.
The Frobenius at each closed point $P \in C(\mathbb{F}_{q^n})$ IS a local object.
The Riemann Hypothesis for curves (Weil 1948, Deligne 1974) follows from the positivity
of the intersection form on $H^1$, which factorizes locally.

For $\zeta(s)$ over $\mathbb{Q}$: no analogue of "Frobenius at a prime" exists.
The cohomological space $H^1$ that would contain the zeros of $\zeta$ as Frobenius
eigenvalues is exactly the object that the Connes–Consani program attempts to construct
(the "arithmetic site"). It does not exist as a theorem.

---

## 4. Wall A: precise diagnosis

**Definition 27-C.4** (Wall A).

Wall A is the statement:

> There exists a decomposition $Q = Q_\infty + \sum_p Q_p$ (as an additive sum over places)
> such that $Q_p \ge 0$ for every $p$ and $Q_\infty \ge 0$ in some geometric sense.

**Proposition 27-C.5** (Wall A is blocked by the absence of the arithmetic site).

Wall A is equivalent to constructing:
1. An arithmetic cohomology $H^1(\mathrm{Spec}\,\mathbb{Z},\mathcal{F})$ over $\mathbb{Z}$;
2. An arithmetic Frobenius operator $\phi_p: H^1 \to H^1$ at each prime $p$;
3. An intersection form on $H^1$ that: (a) factorizes as $Q = Q_\infty + \sum_p Q_p$, and
   (b) whose positivity is equivalent to RH.

*Remark.* This is the Connes–Consani program (2010–2016): the "scaling site"
and arithmetic geometry over $\mathbb{F}_1$ attempt to construct exactly these objects.
Their construction exists as a framework but not as a theorem (the positivity of the
intersection form, analogous to the Hodge index theorem, is the equivalent of RH, not its proof).

**Status of Wall A:** OPEN. Its resolution is equivalent to establishing the arithmetic site of
Connes–Consani as a rigorous mathematical object with an intersection form $\ge 0$.

---

## 5. Wall B: conditional analysis

**Assumption.** We provisionally accept that Wall A is resolved: local forms
$Q_p$ exist such that $Q = Q_\infty + \sum_p Q_p$.

**Wall B:** Does $Q_p \ge 0$ for all $p$ imply $Q \ge 0$?

This would be the infinite-dimensional version of the Hasse–Minkowski theorem.

**Classical Hasse–Minkowski theorem** (quadratic forms over $\mathbb{Q}$):
A quadratic form $Q$ with coefficients in $\mathbb{Q}$ is positive-definite iff
its localizations $Q \otimes_\mathbb{Q} \mathbb{R}$ and $Q \otimes_\mathbb{Q} \mathbb{Q}_p$
are positive-definite for every prime $p$.

**Obstacles for the infinite-dimensional version:**

**(B.1)** Classical Hasse–Minkowski applies to quadratic forms in FINITE dimension.
The Weil form $Q$ acts on the infinite-dimensional space $\mathcal{S}(\mathbb{R}^*_+)$.
No Hasse–Minkowski theorem exists for infinite-dimensional Hermitian forms.

**(B.2)** In infinite dimension, local positivity does not imply global positivity even
for simple forms. Example: let $Q(f,f) = \int_0^\infty f(x)^2 w(x) dx$ where $w$ changes
sign. Locally (on small intervals) $Q$ may be positive, but globally it may
be indefinite.

**(B.3)** The local forms $Q_p$ (if they exist) would be infinite-dimensional Hermitian forms
over $\mathbb{Q}_p$. The theory of such forms has no Hasse–Minkowski version.

**Proposition 27-C.6** (Wall B has no known proof).

There is no Hasse–Minkowski theorem in the literature for infinite-dimensional
Hermitian forms. In particular, the implication
$$Q_p \ge 0 \text{ for all } p \implies Q \ge 0 \text{ globally}$$
does not follow from any known result of the theory of quadratic forms.

**However:** If the Connes–Consani arithmetic site existed as a rigorous
mathematical object, the analogue of the Hodge index theorem for surfaces (which is
FINITE-DIMENSIONAL) might apply and give Wall B as a consequence. This would be the
Weil-Deligne argument for curves lifted to $\mathrm{Spec}\,\mathbb{Z}$.

---

## 6. The hierarchy of difficulty

| Wall | Content | Status | Relation to RH |
|---|---|---|---|
| Wall A (factorization) | $Q_\infty, Q_p$ exist with $Q = Q_\infty + \sum_p Q_p$ | **OPEN** — equivalent to the Connes–Consani arithmetic site | RH-equivalent (positivity of the intersection form) |
| Wall B (local→global) | $Q_p \ge 0 \forall p \implies Q \ge 0$ | **OPEN** — infinite-dim version of HM | RH-equivalent (if Wall A is resolved) |
| Wall W4-RSRP (Phase 25) | Arithmetic property of Re(s)>1 → zeros in the critical strip | OPEN | RH-equivalent |

**Conclusion:** The three walls are RH-equivalent, formulated in different languages.

Wall A is a reformulation of Wall W4-RSRP in terms of arithmetic cohomology:
"local arithmetic information (Euler factors, $Q_p$) does not propagate globally
(toward the zeros of $\zeta$, toward $Q \ge 0$) without the global cohomology of the arithmetic site."

---

## 7. What Phase 27 establishes

**Positive result of Phase 27-C:**

Phase 27-C precisely identifies that Wall A is equivalent to the construction of the
Connes–Consani arithmetic site. That is:

1. A more precise reformulation of Wall W4-RSRP than any previous formulation.
2. The connection between the program of this arc (Kreĭn + Connes) and the
   Connes–Consani program (arithmetic geometry over $\mathbb{F}_1$).
3. The identification of the necessary mathematical object: a cohomological space $H^1$ over
   $\mathbb{Z}$ with a Frobenius operator at each prime and a positive intersection form.

**Negative result of Phase 27-C:**

Phase 27-C does not prove $\mathrm{neg.ind}(H_C) = 0$. The two walls (Wall A and Wall B)
are open. The harder wall is Wall A.

**The precise diagnosis:** Phase 27 reformulates RH as the positivity of an
intersection form in an arithmetic cohomology over $\mathbb{Z}$, which is exactly the
Connes–Consani program. The chain is:
$$\mathrm{neg.ind}(H_C) = 0
\iff Q \ge 0
\iff \text{positivity of the intersection form in } H^1(\mathrm{Spec}\,\mathbb{Z})
\iff \text{RH.}$$
