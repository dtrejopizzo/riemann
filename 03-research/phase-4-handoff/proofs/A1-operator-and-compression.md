# Problem A — The operator $\mathcal T$ and the compression identity

**Goal of this file.** (1) Pin, once and for all, the Hilbert space $\mathcal H$, the operator
$\mathcal T$, and the localizers $g_j$. (2) Reduce the compression identity $Q=P_J\mathcal T P_J$ to two
analytic facts, and discharge as much as possible now.

All later files (B2, future C/D) import the definitions of §1 verbatim.

---

## 1. The pinned data (Result A.0)

### 1.1 Variables and Hilbert space
Work multiplicatively on the idele-class norm group $\mathbb R_{>0}$, written additively via
$u=\log$. The Hilbert space is
$$
\boxed{\ \mathcal H = L^2(\mathbb R,\,du)\ },\qquad
\widehat g(r)=\int_{\mathbb R} g(u)\,e^{-iru}\,du,\qquad
D=\tfrac1i\frac{d}{du}\ \ (\text{so }\widehat{Dg}(r)=r\,\widehat g(r)).
$$
The frequency variable $r$ **is the height variable**: a zero $\rho=\tfrac12+i\gamma$ contributes at
$r=\gamma$. The localizers below are Hermite functions in $r$ centered at $T_0$ — this is the precise
sense in which the program "localizes at height $T_0$."

### 1.2 The Weil quadratic form
For $g\in\mathcal S(\mathbb R)$ set $\tilde g(u)=\overline{g(-u)}$ and $h(r)=|\widehat g(r)|^2\ge0$.
The Riemann–Weil explicit formula applied to $h$ defines the **Weil form**
$$
\mathfrak t(g,g)\ :=\ \sum_{\rho}|\widehat g(\gamma_\rho)|^2
\ \overset{\text{(EF)}}{=}\
\underbrace{\frac1{2\pi}\!\int_{\mathbb R}\!|\widehat g(r)|^2\,\Omega(r)\,dr}_{\text{archimedean }=\,\mathfrak a(g)}
\;+\;\underbrace{\big|\widehat g(\tfrac i2)\big|^2+\big|\widehat g(-\tfrac i2)\big|^2}_{\text{pole }=\,\mathfrak q(g)}
\;-\;\underbrace{2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\mathrm{Re}\,(g\star\tilde g)(\log n)}_{\text{prime }=\,-\mathfrak p(g)} ,
$$
with $\Omega(r)=\mathrm{Re}\,\psi\!\big(\tfrac14+\tfrac{ir}{2}\big)-\log\pi$, and
$(g\star\tilde g)(t)=\int g(u)\overline{g(u-t)}\,du=\langle g,\,T_t g\rangle$, $T_t g(u)=g(u-t)$.

> **Weil's criterion (the target inequality).** $\mathrm{RH}\iff \mathfrak t(g,g)\ge0$ for all
> $g\in\mathcal S$. (If RH holds every $\gamma_\rho\in\mathbb R$ and the left side is a sum of squares;
> the criterion is the converse, read off the right/arithmetic side.)

### 1.3 The operator
Each piece is the quadratic form of an operator on $\mathcal H$:
$$
\boxed{\ \mathcal T \;=\; \Omega(D)\ +\ \Pi\ -\ 2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\mathrm{Re}\,T_{\log n}\ },
$$
- $\Omega(D)$ — the **archimedean** Fourier multiplier by $\Omega(r)$ (self-adjoint; §B2.1 shows it is
  bounded below). "$\mathrm{Re}\,T_t$" $=\tfrac12(T_t+T_t^{*})=\tfrac12(T_t+T_{-t})$, self-adjoint.
- $\Pi$ — the **pole** term, $\langle g,\Pi g\rangle=|\widehat g(\tfrac i2)|^2+|\widehat g(-\tfrac i2)|^2$.
  On $\mathcal S$ this is two rank-one positive forms $g\mapsto\widehat g(\pm\tfrac i2)=\int g(u)e^{\pm u/2}du$
  (analytic continuation of $\widehat g$ to the strip; finite on $\mathcal S$).
- the **prime** sum — a Toeplitz-type operator: a weighted sum of the unitary shifts $T_{\log n}$.

Then $\mathfrak t(g,g)=\langle g,\mathcal T g\rangle$ on $\mathcal S$, and **(LB)** $\inf\operatorname{spec}(\mathcal T)\ge0\iff\mathrm{RH}$.

> **The regularization question, pinned.** There is *no extra free parameter* $\delta$ once $\mathcal H$
> and the EF are fixed as above: the prime sum is conditionally convergent on $\mathcal S$ (Result B2.2),
> so $\mathfrak t$ is a *bona fide* densely-defined form on $\mathcal S$ with **no cutoff needed to
> define it**. Connes' $L^2_\delta$ regularization is a *device for taking the trace / closing the form*,
> not a new degree of freedom in the entries. **This settles work-program §7 step 1:** the regularization
> is the canonical one; A, B, C all inherit $(\mathcal H,\mathcal T)=$ A.0. *(The closure/self-adjoint
> realization — turning the form $\mathfrak t$ into the operator $\mathcal T$ — is Problem B, not A.)*

---

## 2. What the compression identity actually claims

The computed object is the finite Gram matrix $Q^{(X)}_{jk}=(M_{\mathrm{zeros}})_{jk}-(M_{\mathrm{arith}}^{(X)})_{jk}$
in the localizer basis $\{g_j\}_{j<J}$, with prime cutoff $X$. Let $P_J$ be the orthogonal projection
onto $V_J:=\operatorname{span}\{g_0,\dots,g_{J-1}\}\subset\mathcal H$. The identity to establish is
$$
\boxed{\ Q^{\mathrm{exact}}_{jk}:=\langle g_j,\mathcal T g_k\rangle \;=\; (P_J\,\mathcal T\,P_J)_{jk}\ }\qquad(\star)
$$
together with $Q^{(X)}\to Q^{\mathrm{exact}}$ as $X\to\infty$. Note $(\star)$ **right-hand side is a
definition** of the compressed matrix; the content is only that the *middle* expression
$\langle g_j,\mathcal T g_k\rangle$ is (i) finite (the $g_j$ are in the form domain) and (ii) equal to
the computed entries in the limit. So:
$$
\text{Problem A } \;=\;\; \underbrace{\text{A.1: } g_j\in\mathrm{dom}(\mathfrak t)}_{\text{form domain}}\;\;+\;\;\underbrace{\text{A.4: } Q^{(X)}\to Q^{\mathrm{exact}}}_{\text{= P7-B, truncation}} .
$$
This is why A is the *most decidable* problem: granted (A.1) and (A.4), $(\star)$ is a tautology of the
Gram matrix. We now discharge A.1; A.4 is P7-B restated.

---

## 3. A.1 — the localizers lie in the form domain

### 3.1 The localizers
For window height $T_0$ and width $\sigma$, define in frequency
$$
\widehat g_j(r)=H_j\!\Big(\tfrac{r-T_0}{\sigma}\Big)e^{-(r-T_0)^2/2\sigma^2},\qquad j=0,\dots,J-1,
$$
the Hermite functions centered at $T_0$. Then $g_j\in\mathcal S(\mathbb R)$ (Hermite functions are
Schwartz; inverse FT preserves $\mathcal S$), giving the program's closed form
$g_j(u)=e^{-iT_0u}e^{-\sigma^2u^2/4}\times(\text{Hermite/Laguerre in }u)$. **Result A.2** ($g_j\in\mathcal S$)
is immediate; it remains to show $\mathcal S\subseteq\mathrm{dom}(\mathfrak t)$, i.e. each of
$\mathfrak a,\mathfrak q,\mathfrak p$ is finite on $\mathcal S$.

### 3.2 Finiteness of the three pieces on $\mathcal S$ (Result A.1)
Let $g\in\mathcal S$.

**Archimedean $\mathfrak a$.** $\Omega(r)=\mathrm{Re}\,\psi(\tfrac14+\tfrac{ir}2)-\log\pi$ grows like
$\log|r|$ (digamma asymptotics) and is continuous, so $|\Omega(r)|\le C(1+\log(1+|r|))$. Since
$\widehat g\in\mathcal S$ decays faster than any polynomial, $\int|\widehat g(r)|^2|\Omega(r)|\,dr<\infty$.
$\;\;\checkmark$

**Pole $\mathfrak q$.** $\widehat g(\pm\tfrac i2)=\int g(u)e^{\pm u/2}\,du$ converges absolutely
($g\in\mathcal S$ decays super-exponentially? — no: Schwartz decays faster than any *polynomial*, not
exponential). ⚠️ **Gap to tighten:** $\int g(u)e^{u/2}du$ needs $g$ to beat $e^{u/2}$ at $+\infty$.
Schwartz alone does **not** guarantee this. *Fix:* restrict the admissible class to $g$ with
$g(u)=O(e^{-(\frac12+\epsilon)|u|})$ (equivalently $\widehat g$ analytic in a strip $|\Im r|<\tfrac12+\epsilon$)
— which the **Gaussian** localizers $\widehat g_j$ satisfy automatically (entire, Gaussian decay in any
horizontal strip). So $\mathfrak q(g_j)<\infty$ for the actual localizers even though it can diverge on
general $\mathcal S$. **This sharpens the admissible class to "Gaussian-localized," and the $g_j$ are in
it.** $\;\;\checkmark$ for the localizers.

**Prime $\mathfrak p$.** Deferred to Result B2.2 (convergence of $\sum\Lambda(n)n^{-1/2}(g\star\tilde g)(\log n)$),
which holds for all $g\in\mathcal S$ because $g\star\tilde g\in\mathcal S$ decays faster than any power of
$\log n$. $\;\;\checkmark$

**Conclusion (A.1, for the localizer class).** $g_j\in\mathrm{dom}(\mathfrak t)$, with the one honest
correction that the natural domain is **Gaussian-localized Schwartz** (strip-analytic with rate
$>\tfrac12$), not all of $\mathcal S$ — forced by the pole term. The localizers live there by
construction. $\square$

> **Logged correction.** The pole term $\mathfrak q$ is the only piece that constrains the domain; it
> demands strip analyticity of width $>\tfrac12$. Record this as the precise definition of the
> admissible test class — it will matter for Problem C (form-completeness must be stated relative to
> *this* class, not raw $\mathcal S$).

---

## 4. A.3–A.4 — the identity and the truncation

**A.3 (the identity $(\star)$).** With A.1/A.2 in hand, $\langle g_j,\mathcal T g_k\rangle$ is a finite
sesquilinear form, and $(P_J\mathcal T P_J)_{jk}=\langle g_j,\mathcal T g_k\rangle$ by definition of the
compression in the (generally non-orthonormal) frame $\{g_j\}$. ✅ *Caveat:* the $g_j$ are **not**
orthonormal; $P_J\mathcal T P_J$ in the ledger means the Galerkin matrix relative to the Gram matrix
$G_{jk}=\langle g_j,g_k\rangle$, and eigenvalues of "the compression" are those of $G^{-1/2}(\mathcal T|_{V_J})G^{-1/2}$.
This is standard Rayleigh–Ritz; flag it so the numerics and theory use the same generalized eigenproblem.

**A.4 (truncation, $=$ P7-B).** The computed $M_{\mathrm{arith}}^{(X)}$ truncates the prime sum at $n\le X$.
The error is $\big(Q^{\mathrm{exact}}-Q^{(X)}\big)_{jk}=2\sum_{n>X}\frac{\Lambda(n)}{\sqrt n}\,\mathrm{Re}(g_j\star\tilde g_k)(\log n)$.
By P7-B's operator-norm bound $\|g\|_{\mathrm{op}}$, $\|Q^{\mathrm{exact}}-Q^{(X)}\|\le A\,e^{-\alpha(\log X)^2}$,
$\alpha=\sigma^2/8+o(1)$, from PNT alone. 🟡 **To do:** rewrite P7-B's scalar $\eta(X)$ bound as a matrix
operator-norm bound on $V_J$ (uniform in the entries) — mechanical but must be written to make A.4
rigorous, not just per-entry.

---

## 5. Status of Problem A

| Step | Statement | Status |
|---|---|---|
| A.0 | pinned $(\mathcal H,\mathcal T)$, regularization is canonical (no free $\delta$) | ✅ |
| A.1 | localizers in form domain (domain = Gaussian-localized, strip width $>\tfrac12$) | ✅ (localizers); 🟡 (general $\mathcal S$ fails at pole) |
| A.2 | $g_j\in\mathcal S$ closed form | ✅ |
| A.3 | compression identity $(\star)$ (as a generalized/Galerkin eigenproblem) | ✅ |
| A.4 | computed $\to$ exact, rate $e^{-\alpha(\log X)^2}$ | 🟡 (P7-B; needs operator-norm restatement) |

**Net:** Problem A is **essentially proved** modulo two mechanical write-ups (operator-norm P7-B; the
Galerkin/Gram bookkeeping). The one *conceptual* output is the **sharpened admissible class**
(Gaussian-localized, strip-analytic width $>\tfrac12$), forced by the pole term — carry this into C.

**Next actions on A.** (1) Restate P7-B at operator-norm level (closes A.4). (2) Fix the admissible
class definition in the work program and in P7. (3) Hand the Gram-matrix generalized-eigenproblem note
to the numerics side so $\lambda_{\min}$ means the same thing in both places.
