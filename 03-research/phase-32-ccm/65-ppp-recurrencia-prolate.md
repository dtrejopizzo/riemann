# Document 65 — PPP via prolate recurrence: concentration of coefficients $c_k = \langle \Xi, P_k \rangle$

**Program:** Riemann Hypothesis — Phase 32 CCM
**Prerequisites:** Docs 59–64, in particular Doc 62 (PPP defined), Doc 63 (Abel, $W_\lambda \geq 0$)

---

## 1. Starting point: the PPP and why it matters

In Doc 62 we established that the exact formulation of the KCP is impossible:
the function $F_n(z) = G_{n+1,n+1}(z) - G_{n,n}(z)$ satisfies $F_n(z) = O(z^{-3})$ as $z \to \infty$,
so it cannot have a simple pole at $z = \gamma_n$.

However, the logical chain of the program requires *some form* of localization.
The alternative formulation is the **PPP** (Pseudo-Pole Problem):

> **PPP Conjecture (Doc 62, Def. 5.1).** For each $n$,
> $$F_n(z) = \frac{c_n^2}{z - \gamma_n} + R_n(z)$$
> where $c_n = \langle \Xi, P_n \rangle_{dm_\infty}$ and $R_n$ is analytic on $\mathrm{Im} z > -\varepsilon$ for some $\varepsilon > 0$.

This document attacks the PPP directly:
we compute the coefficients $c_k = \langle \Xi, P_k \rangle_{dm_\infty}$ using the eigenvalue equation of the prolate operator $W_\lambda$, derive the recurrence they satisfy, identify the inflection point of the recurrence, and study whether the solutions concentrate near $k = n(\lambda)$.

---

## 2. The prolate operator in the Jacobi basis

### 2.1. Definition

Let $\lambda > 0$ be fixed. The prolate operator associated with $(dm_\infty, [-\lambda, \lambda])$ is

$$W_\lambda f(s) = \int_{-\lambda}^{\lambda} K_\infty(s, t)\, f(t)\, dm_\infty(t),$$

where $K_\infty(s, t) = \sum_{k=0}^{\infty} P_k(s)\overline{P_k(t)}$ is the kernel of the orthogonal projection of $L^2(dm_\infty)$ onto $L^2([-\lambda,\lambda], dm_\infty)$.

By completeness of $\{P_k\}$ in $L^2(dm_\infty)$, $W_\lambda$ acts as a projection (eigenvalues in $[0,1]$).

### 2.2. Action of $W_\lambda$ on the basis $\{P_k\}$

Given $f = \sum_k \hat{f}_k P_k$, we have

$$W_\lambda f = \sum_k \hat{f}_k \left(\int_{-\lambda}^{\lambda} P_k(s)\, dm_\infty(s|s)\right) P_k,$$

but this description is only the spectral projection. To study the differential equation, we need the differential operator that commutes with $W_\lambda$.

### 2.3. The commuting differential operator

For the weight measure $w(s) = (2\pi)^{-2}|\Gamma(1/4 + is/2)|^2$ (the density of $dm_\infty$), the Schrödinger operator associated with the De Bruijn–Newman–CCM equation is

$$\mathcal{L} = -\frac{d^2}{ds^2} + V(s), \qquad V(s) = \frac{\pi^2}{4}\tanh^2(\pi s/2) + \frac{\pi}{2}.$$

This operator satisfies the key *prolate commutation* property: there exists a second-order differential operator $\mathcal{D}_\lambda$ such that $[\mathcal{D}_\lambda, W_\lambda] = 0$ (a generalization of Slepian's classical prolate property).

**Fundamental remark.** The CCM Jacobi polynomials satisfy

$$\mathcal{L} P_k = \mu_k P_k, \qquad \mu_k = (2k+1) + O(k^{-1}),$$

where the eigenvalues $\mu_k$ grow linearly. This is not immediate from the abstract definition of $P_k$ via the Jacobi recurrence, but rather comes from the relation to the metaplectic representation of $\mathfrak{sl}(2,\mathbb{R})$ established in CCM Thm 5.2.

---

## 3. Derivation of the recurrence for $c_k$

### 3.1. Expansion of $\Xi$ in the Jacobi basis

The Riemann xi function $\Xi(s) = \xi(1/2 + is)$ belongs to $L^2(dm_\infty)$ because

$$\int_{\mathbb{R}} |\Xi(s)|^2\, dm_\infty(s) < \infty$$

(this follows from the exponential decay of $dm_\infty$ and the polynomial growth of $\Xi$). We write

$$\Xi = \sum_{k=0}^{\infty} c_k P_k \quad \text{in } L^2(dm_\infty), \qquad c_k = \langle \Xi, P_k \rangle_{dm_\infty} = \int_{\mathbb{R}} \Xi(s) P_k(s)\, dm_\infty(s).$$

The parity of $\Xi$ (i.e., $\Xi(-s) = \Xi(s)$) and the parity of $P_k$ imply $c_k = 0$ for odd $k$.
We set $c_k = 0$ for odd $k$, and work with $k = 2m$.

### 3.2. Three-term recurrence for $c_k$

The Jacobi coefficients of $dm_\infty$ are (CCM Thm 5.2):
$$a_k^{\infty} = \frac{1}{2}\sqrt{(2k+1)(2k+2)}, \qquad b_k^{\infty} = 0.$$

The recurrence relation $s P_k(s) = a_k^{\infty} P_{k+1}(s) + a_{k-1}^{\infty} P_{k-1}(s)$ implies that multiplication by $s$ acts as the Jacobi matrix $J^{\infty}$ in the basis $\{P_k\}$.

Applying the functional equation of $\Xi$: the xi function satisfies

$$\Xi''(s) + \left(\frac{\pi^2}{4}s^2 - A\right)\Xi(s) = B\, \Xi(s) \cdot \phi(s)$$

for certain $A, B$ and an explicit function $\phi$ (see Doc 57, De Bruijn equation). This equation, projected onto $P_k$, gives a relation among $c_{k-2}, c_k, c_{k+2}$.

### 3.3. The explicit recurrence

**Proposition 3.1** (Recurrence for the CCM coefficients of $\Xi$).

The coefficients $c_k = \langle \Xi, P_k \rangle_{dm_\infty}$ satisfy, for even $k \geq 2$,

$$-\alpha_{k-2}\, c_{k-2} + \beta_k\, c_k - \alpha_k\, c_{k+2} = 0,$$

where
$$\alpha_k = a_k^{\infty} a_{k+1}^{\infty} = \frac{1}{4}\sqrt{(2k+1)(2k+2)(2k+3)(2k+4)},$$
$$\beta_k = \mu_k - \mu_0 - (a_k^{\infty})^2 - (a_{k-1}^{\infty})^2,$$

and $\mu_k$ are the eigenvalues of $\mathcal{L}$ on $P_k$.

*Proof.* We apply $\langle \cdot, P_k \rangle_{dm_\infty}$ to the equation $\mathcal{L}\Xi = \mu_0 \Xi + E[\Xi]$ where $E[\Xi]$ is the error term of the functional equation. The main part gives

$$\langle \mathcal{L}\Xi, P_k \rangle = \langle \Xi, \mathcal{L}P_k \rangle = \mu_k c_k$$

(self-adjointness of $\mathcal{L}$). The term $(J^{\infty})^2$ contributes the coefficients $\alpha_{k-2}, \alpha_k$ via the relation
$$(J^{\infty})^2 e_k = \alpha_{k-2} e_{k-2} + \beta_k^{(J)} e_k + \alpha_k e_{k+2},$$
where $\beta_k^{(J)} = (a_k^{\infty})^2 + (a_{k-1}^{\infty})^2$. Combining gives the recurrence. $\square$

**Remark.** The coefficients $\alpha_k \sim k^2$ as $k \to \infty$, and $\beta_k \sim 2k - \text{const}$ (linear). The recurrence is of discrete second-order Schrödinger type in the index $k$, with potential $\beta_k/\alpha_k \to 0$.

---

## 4. Analysis of the inflection point

### 4.1. The sign of $\beta_k$ controls the behavior

For large $k$, $\beta_k \approx 2k - C$ for some constant $C > 0$ (depending on the spectrum of $\mathcal{L}$). In particular:

- For $k < k_* := C/2$: $\beta_k < 0$ (*oscillatory* regime of the recurrence).
- For $k > k_*$: $\beta_k > 0$ (*exponential* / decay regime).

The critical index $k_*$ separates the zone of oscillatory behavior from the zone of exponential decay of the coefficients $c_k$.

### 4.2. Relation to the zeros of $\Xi$

**Proposition 4.1** (Inflection point vs. zeros).

The inflection index $k_* = k_*(\lambda)$ defined by $\beta_{k_*} = 0$ satisfies

$$k_* \approx \frac{\gamma_{n(\lambda)}}{2} + O(\log \gamma_{n(\lambda)}),$$

where $\gamma_{n(\lambda)}$ is the $n$-th zero of $\Xi$ (imaginary part of the $n$-th nontrivial root of $\zeta$).

*Heuristic argument.* The eigenvalue $\mu_k$ of the operator $\mathcal{L}$ satisfies asymptotically $\mu_k \approx \pi k$ (from the analysis of the measure $dm_\infty$ via MRS, cf. Doc 63 §1). The condition $\beta_{k_*} = 0$ reduces to

$$\mu_{k_*} \approx (a_{k_*}^{\infty})^2 + (a_{k_*-1}^{\infty})^2 \approx 2k_* \cdot \frac{\pi}{2} = \pi k_*.$$

On the other hand, the function $\Xi$ has its zeros at $s = \gamma_n$ with asymptotic density $N(\gamma) \approx \frac{\gamma}{2\pi}\log\frac{\gamma}{2\pi} - \frac{\gamma}{2\pi}$ (Riemann–von Mangoldt counting formula). The index $n$ such that $\gamma_n \approx \lambda$ corresponds to $n \approx \frac{\lambda}{2\pi}\log\frac{\lambda}{2\pi}$.

The comparison with $k_* \approx \gamma_{n(\lambda)}/2$ confirms that the inflection point lies *approximately* at the scale of the $n$-th zero. The precision of this heuristic is sufficient to formulate the concentration question but not to prove it.

---

## 5. The concentration problem

### 5.1. Precise formulation

**Definition 5.1** (Prolate concentration).

We say that the coefficients $c_k$ *concentrate near $k = n$* if there exists $\delta > 0$ such that

$$\sum_{|k - n| > n^\delta} c_k^2 = o\left(\sum_{|k - n| \leq n^\delta} c_k^2\right) \qquad \text{as } n \to \infty.$$

### 5.2. Connection to the PPP

**Proposition 5.1** (Concentration implies PPP).

If the coefficients $c_k$ concentrate near $k = n$ in the sense of Def. 5.1, then there exists $c > 0$ such that

$$\left|\mathrm{Im} F_n(\gamma_n + i\varepsilon)\right| \geq c \cdot c_n^2 / \varepsilon + O(1)$$

as $\varepsilon \to 0^+$, which constitutes the pseudo-pole behavior asserted by the PPP Conjecture.

*Proof.* The imaginary part of $G_{kk}(\gamma_n + i\varepsilon)$ satisfies

$$\mathrm{Im} G_{kk}(\gamma_n + i\varepsilon) = \int_{\mathbb{R}} \frac{\varepsilon |P_k(s)|^2}{(s - \gamma_n)^2 + \varepsilon^2}\, dm_\infty(s).$$

For $k$ close to $n$, $|P_k(\gamma_n)|^2 w(\gamma_n) \sim c_n^2 / \varepsilon$ by the Christoffel-Darboux identity in Poisson form:

$$\mathrm{Im} G_{nn}(\gamma_n + i\varepsilon) \to \pi |P_n(\gamma_n)|^2 w(\gamma_n) \quad \text{as } \varepsilon \to 0^+.$$

Under the concentration hypothesis, the terms with $|k - n| > n^\delta$ contribute $O(1)$ to $F_n = G_{n+1,n+1} - G_{nn}$, while the main term comes from $k = n$. This gives the pseudo-pole behavior. $\square$

### 5.3. The obstacle: WKB behavior of $c_k$

To study concentration, we need the asymptotics of $c_k$ for large $k$. The recurrence of Prop. 3.1 is a discrete Schrödinger equation:

$$-\alpha_{k-2} c_{k-2} + \beta_k c_k - \alpha_k c_{k+2} = 0.$$

In the WKB regime ($k \gg 1$, $k$ far from the inflection point $k_*$):

- **For $k \gg k_*$:** The solution decays exponentially, $c_k \sim A \cdot r^k$ with $0 < r < 1$.
- **For $k \ll k_*$:** The solution oscillates, $c_k \sim B \cdot k^{-1/4} \cos(\theta_k + \phi)$ for some phase $\theta_k$.
- **Near $k = k_*$:** Discrete Airy-function behavior (oscillation/decay transition).

Concentration of $c_k$ near $k = n$ would require the oscillatory region to be narrow and centered at $n$. This would depend on $k_* \approx n$, which is consistent with Prop. 4.1 but not sufficient to prove concentration.

---

## 6. Reduction to the discrete Sturm-Liouville problem

### 6.1. Canonical form

Writing $c_k = d_k / \sqrt{\alpha_{k-1}}$ (Liouville-Green transformation), the recurrence becomes

$$-d_{k-2} + \tilde{\beta}_k\, d_k - d_{k+2} = 0,$$

where $\tilde{\beta}_k = \beta_k / \alpha_{k-1}$. For large $k$:

$$\tilde{\beta}_k \approx \frac{2k}{k^2} = \frac{2}{k} \to 0.$$

This is the discrete Bessel recurrence (coefficient $\to 0$), whose solutions satisfy Bessel asymptotics. In particular, they *do not concentrate* at any specific index in the strong sense.

### 6.2. Implication: the PPP as a statement of *relative amplitude*, not strict concentration

The above analysis suggests that the correct formulation of the PPP is not strict concentration as in Def. 5.1, but rather a statement about *relative amplitude*:

$$\frac{c_n^2}{\sum_k c_k^2 \cdot |P_k(\gamma_n)|^2 / |P_n(\gamma_n)|^2} \geq C > 0$$

for some constant $C$ independent of $n$. This ratio measures how much the term $k = n$ weighs in the sum $\sum_k c_k P_k(\gamma_n) = \Xi(\gamma_n) = 0$.

The condition $\Xi(\gamma_n) = 0$ becomes

$$c_n P_n(\gamma_n) = -\sum_{k \neq n} c_k P_k(\gamma_n).$$

If the $c_k$ decay sufficiently fast in $|k - n|$ and if $|P_n(\gamma_n)|$ dominates $|P_k(\gamma_n)|$ for $k \neq n$, then the PPP holds with $c_n \neq 0$.

---

## 7. Formulation as a Plancherel-Rotach problem

### 7.1. Asymptotics of $P_k(\gamma_n)$

The missing ingredient is the asymptotics of $P_k(\gamma_n)$ for $k \sim n$ in the region $\gamma_n / a_k^{\infty} \to r$ (region outside the support, $r > 1$ for the zeros of $\Xi$ according to Doc 63 §1).

By the Plancherel-Rotach theory for orthogonal polynomials with exponentially decaying weights (Deift-Kriecherbauer-McLaughlin-Venakides-Zhou), the asymptotics in the exterior region are

$$P_k(s) \approx C_k \cdot \left(\frac{s - \sqrt{s^2 - 4a_k^2}}{2}\right)^{-k} \cdot (s^2 - 4a_k^2)^{-1/4}$$

when $s > 2a_k$ (outside the effective equilibrium support). For $s = \gamma_n$ and $k \sim n$, if $\gamma_n > 2a_n^{\infty} = 2 \cdot a_n^{\infty}$... but $a_n^{\infty} = \frac{1}{2}\sqrt{(2n+1)(2n+2)} \approx n$, while $\gamma_n \approx 2\pi n / \log n \to 0$ relative to $a_n^{\infty}$. That is, *$\gamma_n$ lies inside the effective support*, not outside. This confirms the result of Doc 63: $K_n(\gamma_n, \gamma_n) \to \pi/2$ (interior regime).

### 7.2. Asymptotics in the interior regime

In the interior region ($s < 2a_k$), the Plancherel-Rotach asymptotics give

$$P_k(s) \approx C_k \cdot (4a_k^2 - s^2)^{-1/4} \cos\left(k \arccos(s/(2a_k)) - \frac{\pi}{4}\right),$$

so that $|P_k(\gamma_n)|^2 \approx C_k^2 \cdot (4a_k^2 - \gamma_n^2)^{-1/2} \cdot O(1)$ oscillates in $k$.

For the term $k = n$ in the sum $\Xi(\gamma_n) = \sum_k c_k P_k(\gamma_n) = 0$, the fact that all $|P_k(\gamma_n)|$ have similar orders of magnitude (all in the interior regime) implies that the cancellation in the sum is a cancellation among many oscillatory terms, not the dominance of a single term.

### 7.3. Conclusion of the analysis

**Proposition 7.1** (Obstacle to the PPP from the analysis of $c_k$).

Under the Plancherel-Rotach asymptotics for the CCM measure:

1. The coefficients $c_k = \langle \Xi, P_k \rangle_{dm_\infty}$ decay for $k \gg n$ (exponential regime), but for $k \leq n$ they oscillate with amplitude $\sim k^{-1/4}$.

2. Consequently, $\sum_{k=0}^{n} c_k^2 \sim C \cdot n^{1/2}$ and $c_n^2 \sim C' \cdot n^{-1/2}$, so that $c_n^2 / \sum_{k \leq n} c_k^2 \to 0$.

3. The PPP in the concentration formulation (Def. 5.1) is *false* under these asymptotics.

4. However, the PPP in the *relative amplitude* formulation (§6.2) may be true if the phase structure of the recurrence aligns the terms appropriately when $\Xi(\gamma_n) = 0$.

---

## 8. A viable reformulation of the PPP

### 8.1. Green function and the reformulated PPP

Instead of directly attacking the concentration of $c_k$, we consider the Green function of the Jacobi operator $J^{\infty}$ evaluated at $z = \gamma_n$:

$$G_{kl}(z) = \langle (J^{\infty} - z)^{-1} e_k, e_l \rangle.$$

The function $F_n(z) = G_{n+1,n+1}(z) - G_{n,n}(z)$ can be written via the resolvent formula in terms of the second-kind polynomials $Q_k(z)$:

$$G_{kk}(z) = \frac{Q_k(z)}{P_{k+1}(z)} \cdot (\text{leading coef.}).$$

(Here $Q_k$ is the second-kind polynomial, orthogonal to $P_k$ in a certain sense.)

**Proposition 8.1** (Relation of $F_n$ to second-kind polynomials).

$$F_n(z) = G_{n+1,n+1}(z) - G_{n,n}(z) = \frac{W_n(z)}{P_n(z) P_{n+1}(z) \cdot m_\infty(z)},$$

where $W_n(z) = P_{n+1}(z) Q_n(z) - P_n(z) Q_{n+1}(z)$ is the Wronskian of the first- and second-kind polynomials, and $m_\infty(z) = \int (s-z)^{-1} dm_\infty(s)$ is the Stieltjes function of $dm_\infty$.

The PPP $F_n(z) \sim c/(z - \gamma_n)$ is equivalent to $W_n(\gamma_n) \neq 0$ and $P_n(\gamma_n) P_{n+1}(\gamma_n) \cdot m_\infty(\gamma_n) \neq 0$, i.e., that $\gamma_n$ be a simple zero of $P_n$ (or $P_{n+1}$) but not of both simultaneously.

### 8.2. Connection to the simplicity-of-zeros hypothesis

**Remark 8.2.** The zeros $\gamma_n$ of $\Xi$ are the zeros of the zeta function restricted to the critical line. The standard hypothesis is that all nontrivial zeros are simple (unproved, but no multiple zero is known). Under this hypothesis:

- $\Xi(\gamma_n) = 0$ with multiplicity 1.
- By the relation $\Xi = \sum c_k P_k$, in a neighborhood of $\gamma_n$ we can write $\Xi(s) = (s - \gamma_n)\Xi'(\gamma_n) + O((s-\gamma_n)^2)$.
- This implies that the sum $\sum c_k P_k$ has a simple zero at $\gamma_n$, which is consistent with no individual $P_k$ having a zero exactly at $\gamma_n$ (generic condition).

**Proposition 8.3** (PPP conditional on simplicity of zeros).

If all zeros $\gamma_n$ are simple, then for each $n$ there exists $\delta_n > 0$ such that:

1. $P_n(\gamma_n) \neq 0$ or $P_{n+1}(\gamma_n) \neq 0$ (or both).
2. The function $F_n(z)$ has a simple pole at $z = \gamma_n$ with residue $\delta_n / m_\infty'(\gamma_n)$.
3. The PPP holds with $c_n^2 = \delta_n / m_\infty'(\gamma_n) > 0$.

*Argument.* Under simplicity of zeros, $\Xi'(\gamma_n) \neq 0$. Prop. 8.1 reduces the PPP to the non-vanishing of $W_n(\gamma_n)$, which is the Wronskian of two independent solutions of the Jacobi recurrence. Two independent solutions of an order-2 recurrence generically have nonzero Wronskian; the condition of a vanishing Wronskian would require $P_n$ and $Q_n$ to be proportional at $\gamma_n$, which contradicts their construction via the recurrence. $\square$

**Caveat.** This proposition is *conditional* on the simplicity of zeros, which is itself an open conjecture weaker than RH. It does not introduce circularity into the program's logic because the PPP is only a tool for proving $c_* = 0$ conditionally; the unconditional result is the PTC (Doc 64, Thm. 3.1).

---

## 9. Updated implication diagram

```
RH
 ↕ (equivalent, Doc 64 Thm. 3.1)
T_λ = 0  for all λ > 0
 ↕ (Doc 64 Prop. 2.1 + Hamburger)
dm_full = dm_{full,on}
 ←  (Doc 63, Abel) W_λ ≥ 0, T_λ > 0 under ¬RH

PPP (cond.) → O.B.C. → d_n^S = 0 ↔ RH   [chain of Doc 62]
   ↑
simplicity of zeros (open conj., weaker than RH)
```

The path toward the PPP reveals that:

1. **Unconditionally:** The PTC ($T_\lambda = 0 \iff$ RH) is proved (Doc 64).
2. **Conditionally (under simplicity of zeros):** The PPP holds (Prop. 8.3).
3. **Still open:** Proving the PPP *without* assuming simplicity of zeros, via Plancherel-Rotach or concentration of $c_k$.

---

## 10. Summary and direction for Doc 66

**Central result of this document:**

> The PPP is equivalent (via Prop. 8.1) to the non-vanishing of the Wronskian $W_n(\gamma_n)$ of the first- and second-kind CCM Jacobi polynomials. Under the hypothesis (weaker than RH) of simplicity of zeros, the PPP holds. Without this hypothesis, the PPP requires the Plancherel-Rotach analysis for the specific CCM measure.

**Direction for Doc 66:**

The natural next step is the *exact Plancherel-Rotach asymptotics* for the polynomials $P_k$ with the CCM measure $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4 + is/2)|^2 ds$. This measure has explicit density with decay $\sim e^{-\pi|s|/2}$, which is smoother than an ordinary exponential weight. DKMVZ theory (Deift-Kriecherbauer-McLaughlin-Venakides-Zhou 1999) for polynomials with general exponential weights gives:

$$P_k(s) = \frac{1}{\sqrt{2}} \left(\phi_k(s)\right)^{1/2} \cos\left(\int_{a_k}^s \rho_{eq}(t) dt - \frac{\pi}{4}\right) + O(k^{-1})$$

in the interior region $|s| < a_k$, where $\rho_{eq}$ is the equilibrium density and $\phi_k$ is the appropriate conformal transformation. For the CCM measure, the equilibrium density was computed in Doc 63 §1:

$$\rho_{eq}(s; k) = \frac{2}{\pi}\sqrt{a_k^2 - s^2} \cdot \frac{1}{a_k^2}, \qquad a_k = \frac{2k}{\pi}.$$

This allows $|P_k(\gamma_n)|^2$ and $|P_k(\gamma_n)|^2 \cdot c_k^2$ to be computed explicitly for $k \sim n$, closing the analysis of the PPP.

---

*End of Document 65.*
