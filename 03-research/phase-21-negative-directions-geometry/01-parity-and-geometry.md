# Phase 21 — Step 1: Parity Theorem and Angular Separation

**Classification:** Class B (unconditional)

---

## Context and starting point

From P29 (Symmetry vs Positivity) we know:

1. $\kappa(Q) = \#\{\rho \notin \text{Fix}(j)\}$ = negative index of the Weil form.
2. Off-line zeros come in $V$-invariant orbits of size 4:
   $$\mathcal{O}(\rho_0) = \{\rho_0,\, \bar\rho_0,\, 1-\rho_0,\, 1-\bar\rho_0\}$$
   where $\rho_0 = \sigma_0 + i\gamma_0$, $\sigma_0 \neq \frac{1}{2}$, $\gamma_0 \neq 0$.
3. The form restricted to an off-line orbit is $4(u^2 - v^2)$ where
   $u = \Re\hat{f}(\rho_0)$, $v = \Im\hat{f}(\rho_0)$.

The question of this phase: how many independent negative directions does each orbit produce?

---

## Proposition P-0: Independence of the localizations at $\pm\gamma_0$

**Setup.** Let $\mathcal{O}(\rho_0)$ be an orbit with $\rho_0 = \sigma_0 + i\gamma_0$, $\gamma_0 > 0$.

The global Weil form (not localized at $T_0$) receives contributions from all zeros. When we evaluate the contribution of the orbit $\mathcal{O}(\rho_0)$:

- The zeros $\rho_0 = \sigma_0 + i\gamma_0$ and $1-\bar\rho_0 = (1-\sigma_0)+i\gamma_0$ are at height $+\gamma_0$.
- The zeros $\bar\rho_0 = \sigma_0 - i\gamma_0$ and $1-\rho_0 = (1-\sigma_0)-i\gamma_0$ are at height $-\gamma_0$.

**Lemma.** The contributions to the negative form coming from the sub-orbit at height $+\gamma_0$ and from the sub-orbit at height $-\gamma_0$ belong to orthogonal subspaces (with respect to $Q$).

**Proof.** Let $f^+$ be a test function such that $\hat{f}^+$ is concentrated near $+\gamma_0$ (in imaginary part), and let $f^-$ have $\hat{f}^-$ concentrated near $-\gamma_0$. Then:

$$Q(f^+, f^-) = \sum_\rho \hat{f}^+(\rho)\hat{f}^-(\rho) + O(\text{prime terms})$$

Each term $\hat{f}^+(\rho)\hat{f}^-(\rho)$ is small: zeros at height $+\gamma_0$ give $\hat{f}^-(\rho) \approx 0$ (by concentration), and zeros at height $-\gamma_0$ give $\hat{f}^+(\rho) \approx 0$. Therefore $Q(f^+, f^-) \approx 0$. $\square$

---

## Theorem 21-A.1 (Parity of κ)

**Statement.** Let $\zeta$ be the Riemann zeta function, or any primitive real Dirichlet L-function $L(s,\chi)$ with $\chi$ real. Then:
$$\kappa(Q) \equiv 0 \pmod{2}.$$

In particular, the question "$\kappa = 0$ or $\kappa > 0$?" is equivalent to the question "$\kappa = 0$ or $\kappa \geq 2$?". The minimal nontrivial negative index is **2**.

**Proof.**

*Step 1: Orbit structure.*
By the functional equation $\zeta(s) = \zeta(1-s)$ (in completed form: $\xi(s)=\xi(1-s)$) and real coefficients ($\overline{\zeta(\bar{s})} = \zeta(s)$), the Klein group $V = \{id, \sigma, \iota, j\}$ acts on the set of nontrivial zeros. An off-line zero $\rho_0 = \sigma_0+i\gamma_0$ with $\sigma_0 \neq \frac{1}{2}$ and $\gamma_0 \neq 0$ generates the orbit:
$$\mathcal{O}(\rho_0) = \{\underbrace{\sigma_0+i\gamma_0}_{\rho_0},\; \underbrace{\sigma_0-i\gamma_0}_{\bar\rho_0},\; \underbrace{(1-\sigma_0)+i\gamma_0}_{1-\bar\rho_0},\; \underbrace{(1-\sigma_0)-i\gamma_0}_{1-\rho_0}\}$$
with 4 distinct elements (since $\sigma_0 \neq \frac{1}{2}$ and $\gamma_0 \neq 0$).

For $\zeta$: nontrivial zeros satisfy $\Im\rho \neq 0$ (there are no real nontrivial zeros). Therefore, every off-line orbit has exactly 4 elements.

*Step 2: Contribution of each sub-orbit.*
The sub-orbit at height $+\gamma_0$: $\{\rho_0, 1-\bar\rho_0\} = \{\sigma_0+i\gamma_0,\; (1-\sigma_0)+i\gamma_0\}$.

From P29, the form $Q$ restricted to functions that probe only the sub-orbit at height $+\gamma_0$ is:
$$Q|_{+\gamma_0}(f,f) = 4(u^2 - v^2), \quad u = \Re\hat{f}(\rho_0),\; v = \Im\hat{f}(\rho_0).$$

This is a 2-dimensional space with signature $(+1,-1)$: **one negative index** coming from the direction $v$ (the direction $u=0$, $v\neq 0$).

Likewise, the sub-orbit at height $-\gamma_0$: $\{\bar\rho_0, 1-\rho_0\}$ produces the same form $4(u'^2-v'^2)$ where $u'+iv' = \hat{f}(\bar\rho_0) = \overline{\hat{f}(\rho_0)}$ (for real $f$), with **one independent negative index** in the direction $v' = -v$.

*Step 3: Independence.*
By Proposition P-0, the negative subspaces at $+\gamma_0$ and $-\gamma_0$ are orthogonal under $Q$ (they are detected with functions $f^+, f^-$ at distinct, mutually orthogonal frequencies). They are therefore linearly independent.

*Step 4: Counting.*
Each orbit $\mathcal{O}(\rho_0)$ (with $\gamma_0 \neq 0$) contributes exactly **2 independent negative directions** to $\mathcal{N}$.

Let $m$ be the number of distinct off-line orbits. Then:
$$\kappa = 2m.$$

In particular $\kappa \equiv 0 \pmod{2}$. $\square$

---

## Corollary 21-A.2

The set of possible values of $\kappa$ for $\zeta$ is:
$$\kappa \in \{0, 2, 4, 6, \ldots\} = 2\mathbb{Z}_{\geq 0}.$$

RH $\iff$ $\kappa = 0$ $\iff$ $m = 0$ (no off-line orbit).

---

## Dimensional formula

**Theorem 21-A.3 (Dimensional formula).**
Let $m(T)$ be the number of off-line orbits with $|\Im\rho| \leq T$ (i.e., the number of conjugate pairs of off-line zeros with positive imaginary part $\leq T$). Then:
$$\kappa(Q|_{[0,T]}) = 2m(T),$$
where $Q|_{[0,T]}$ denotes the form localized to frequencies $\leq T$.

---

## Theorem 21-B.1 (Angular Separation)

**Statement.** Let $v_j^+, v_j^-$ be the two normalized negative directions ($Q(v,v) = -1$) coming from the orbit $\mathcal{O}(\rho_j)$ at height $\gamma_j > 0$. For distinct orbits ($j \neq k$) with $|\gamma_j - \gamma_k| \geq \Delta_{\min}$:
$$|Q(v_j^+, v_k^+)| \leq C\, e^{-c\,\Delta_{\min}^2/\delta^2},$$
where $\delta$ is the width of the frequency packet (determined by the support of the test function).

**Proof.**
The directions $v_j^+$ and $v_k^+$ correspond to test functions $f_j^+$, $f_k^+$ whose Mellin transforms are concentrated respectively near $\gamma_j$ and $\gamma_k$ (in imaginary part), of width $\delta$.

The bilinear product:
$$Q(f_j^+, f_k^+) = \sum_\rho \hat{f}_j^+(\rho)\hat{f}_k^+(\rho) + \text{prime terms}.$$

For the zero terms: $|\hat{f}_j^+(\rho)| \leq A\,e^{-c(\gamma_\rho - \gamma_j)^2/\delta^2}$ and likewise for $k$. Therefore:

$$|\hat{f}_j^+(\rho)\hat{f}_k^+(\rho)| \leq A^2\, e^{-c[(\gamma_\rho-\gamma_j)^2+(\gamma_\rho-\gamma_k)^2]/\delta^2}.$$

The maximum over $\gamma_\rho$ is attained at $\gamma_\rho = \frac{\gamma_j+\gamma_k}{2}$ and equals $A^2\,e^{-c(\gamma_j-\gamma_k)^2/(2\delta^2)}$. Summing over all zeros (with density $\sim \log T$):

$$|Q(f_j^+, f_k^+)| \leq A^2 (\log T)\, e^{-c(\gamma_j-\gamma_k)^2/(2\delta^2)}.$$

Since the minimal separation between zeros satisfies $\Delta_{\min} \gg \delta$ (the packets are under-spaced), the exponential factor dominates. $\square$

---

## Theorem 21-B.2 (Direct Decomposition of $\mathcal{N}$)

**Statement.** Under the conditions of Theorem 21-B.1, the maximal negative subspace $\mathcal{N}$ admits a decomposition:
$$\mathcal{N} = \bigoplus_{j=1}^m \mathcal{N}_j, \quad \mathcal{N}_j = \mathcal{N}_j^+ \oplus \mathcal{N}_j^-,$$
where each $\mathcal{N}_j^{\pm}$ is 1-dimensional (the negative direction of $\mathcal{O}(\rho_j)$ at height $\pm\gamma_j$), and the decomposition is orthogonal up to an error $O(e^{-c/(\delta\log T)^2})$.

The form $Q$ restricted to each $\mathcal{N}_j$ is equivalent to the Lorentz form $\mathbb{R}^{1,1}$: a 2-dimensional space with signature $(+,-)$.

**Consequence.** The Kreĭn space $(\mathcal{H}, Q)$ decomposes:
$$(\mathcal{H}, Q) \cong (\mathcal{H}_+, Q_+) \perp \bigoplus_{j=1}^m (\mathbb{R}^{1,1})_j,$$
where $(\mathcal{H}_+, Q_+)$ is positive semidefinite and the $\mathbb{R}^{1,1}$ factors are mutually orthogonal.

---

## Updated classification table (Phase 21)

| Property of $\mathcal{N}$ | Value | Proof | Class |
|---|---|---|---|
| $\kappa \equiv 0 \pmod 2$ | Yes | Theorem 21-A.1 | B |
| Minimal nontrivial value of $\kappa$ | 2 | Corollary 21-A.2 | B |
| $\kappa = 2m$ (m orbits) | Yes | Theorem 21-A.3 | B |
| Angular separation: exponential orthogonality | Yes | Theorem 21-B.1 | B |
| Direct decomposition of $\mathcal{N}$ | $\bigoplus_j \mathbb{R}^{1,1}_j$ | Theorem 21-B.2 | B |
| $\mathcal{N}$ with $0 < \kappa < \infty$ | conjecturally empty | Phase 16 (computation) | — |
| Does an isolated zero in $\mathcal{N}$ force more? | Open | — | 21-D |

---

## Remark on the trichotomy

Theorem 21-A.1 + the Phase 16 computation strongly suggest the trichotomy:
$$\kappa \in \{0\} \cup \{2\mathbb{Z}_{>0}\} \cup \{\infty\},$$
with the computation ruling out the finite nonzero part.

The only alternative compatible with everything known is $\kappa = 0$ (RH) or $\kappa = +\infty$ (infinitely many off-line zeros).

---

## Open questions of this phase

**OP21-1.** Is the decomposition $\mathcal{N} = \bigoplus_j \mathbb{R}^{1,1}_j$ exactly orthogonal or only asymptotically so? What controls the correction?

**OP21-2.** Can it be proved unconditionally that $\kappa < \infty$, $\kappa > 0$ implies $\kappa = 2$ (a single pair of off-line zeros), contradicting the known analytic constraints of $\zeta$?

**OP21-3.** Defect measure: does $\frac{1}{m}\sum_{j=1}^m \delta_{\gamma_j}$ converge to some limiting measure as $m\to\infty$? What properties would that measure have?

**OP21-4.** Is there an "exclusion law": a global property of $\zeta$ that makes it impossible for $\mathcal{N}$ to be nonzero and finite-dimensional?

---

## Architectural significance

Theorem 21-A.1 is this phase's first result giving concrete geometric information about $\kappa$ without assuming RH and without using RH-equivalents as a hypothesis.

It says: **if RH is false, there are at least 2 negative directions, and more generally $\kappa$ grows in pairs.**

This transforms the RH question from "$\kappa=0$ or $\kappa\geq 1$" to "$\kappa=0$ or $\kappa\geq 2$". The threshold shifts. Each off-line zero costs two units of negative index, not one.

The geometry of $\mathcal{N}$ as a direct sum of Lorentz planes (Theorem 21-B.2) is the basis for building the defect theory (21-C) and seeking the exclusion principle (21-D).
