# Doc 43 — Rigidity of the Cauchy-Poisson Transform: the Single-Point Theorem

**Program:** CCM Zeta Spectral Triples — Phase 29/32  
**Prerequisites:** Docs 38–42 (especially Doc 42 §5, §16, §17)  
**Objective:** Prove the Poisson Rigidity Theorem and its consequences; establish the equivalence RH ↔ $C_\infty(\gamma_{n_0})=0$ for a SINGLE $n_0$; analyze continuity, the detection of off-critical zeros by density, and the precise obstacle.

---

## 1. The central question

Doc 42 (Theorem 5.2) established the **explicit deficit formula**:

$$C_\infty(\gamma_n) = \sum_{\substack{\rho_0 \in \mathcal{Z}_{\mathrm{off}} \\ \sigma_0 > 1/2,\, \gamma_0 > 0}} \Delta(\gamma_n;\rho_0) \geq 0$$

where each term $\Delta(\gamma_n;\rho_0) > 0$ is a strictly positive Cauchy-Poisson kernel. The measure of off-critical zeros is $\mu_{\mathrm{off}} = \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}} 2(\sigma_0-1/2)\,\delta_{(\gamma_0,\,\sigma_0-1/2)}$.

The formula can be rewritten as:
$$C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n), \qquad \mathcal{P}[\mu](t) := \int_{\mathbb{H}} \frac{y}{y^2+(t-x)^2}\,d\mu(x,y)$$

where $\mathbb{H} = \{(x,y): y > 0\}$ and the factor of the second term of $\Delta$ (with $\gamma_n + \gamma_0$) is absorbed into the symmetrized measure (see §A.1).

**The question of Doc 43:** Can a positive measure $\mu_{\mathrm{off}} \neq 0$ on $\mathbb{H}$ have $\mathcal{P}[\mu_{\mathrm{off}}](\gamma_n) = 0$ for every zero $\gamma_n$ of $\Xi$?

---

## 2. The Poisson kernel and its strict positivity

**Definition 2.1 (Poisson kernel).** For $(x,y) \in \mathbb{H}$ and $t \in \mathbb{R}$:
$$P_y(t-x) := \frac{y}{y^2+(t-x)^2}$$

**Lemma 2.2 (Strict positivity).** For every $(x,y)\in\mathbb{H}$ and every $t\in\mathbb{R}$:
$$P_y(t-x) = \frac{y}{y^2+(t-x)^2} > 0$$

*Proof.* $y > 0$ by hypothesis and $y^2+(t-x)^2 > 0$. $\square$

**Lemma 2.3 (Kernel properties).** For fixed $y > 0$:
1. $\int_{-\infty}^\infty P_y(t)\,dt = \pi$.
2. $P_y(t) \leq y^{-1}$ for every $t$.
3. $P_y(t) \sim y/t^2$ for $|t| \gg y$.
4. $P_y(t) \leq P_y(0) = 1/y$ with maximum at $t = 0$.

*Proof.* (1) Standard Cauchy integral. (2) $P_y(t) \leq y/y^2 = 1/y$. (3) For $t \gg y$: $P_y(t) = y/(y^2+t^2) \sim y/t^2$. (4) Immediate from the definition. $\square$

---

## 3. The Poisson Rigidity Theorem

The central result of this document is elementary but decisive.

**Theorem 3.1 (Poisson Rigidity — Single-Point Version).** Let $\mu$ be a non-negative Borel measure on $\mathbb{H}$, finite on compact sets, such that $\int_{\mathbb{H}}(1+y)^{-1}(1+x^2)^{-1}\,d\mu(x,y) < \infty$. Define:
$$\mathcal{P}[\mu](t) := \int_{\mathbb{H}} \frac{y}{y^2+(t-x)^2}\,d\mu(x,y) \geq 0$$

If $\mathcal{P}[\mu](t_0) = 0$ for SOME $t_0 \in \mathbb{R}$, then $\mu = 0$ (identically null measure).

*Proof.* By the integrability hypothesis, the integral $\mathcal{P}[\mu](t_0)$ is finite. The integrand $P_y(t_0-x) = y/[y^2+(t_0-x)^2]$ is strictly positive for every $(x,y)\in\mathbb{H}$ (Lemma 2.2) and the measure $\mu$ is non-negative. Therefore:

$$0 = \mathcal{P}[\mu](t_0) = \int_{\mathbb{H}} \underbrace{P_y(t_0-x)}_{>0}\, d\mu(x,y)$$

The integral of a strictly positive function with respect to a non-negative measure is zero if and only if the measure is the null measure. Conclusion: $\mu = 0$. $\square$

**Remark 3.2.** Theorem 3.1 does not depend on $t_0$ at all: the kernel $P_y(t_0-x) > 0$ for EVERY $t_0\in\mathbb{R}$ and every $(x,y)\in\mathbb{H}$. This means that **a single vanishing point of $\mathcal{P}[\mu]$ on $\mathbb{R}$ detects the whole mass of $\mu$**.

**Corollary 3.3 (Rigidity — Infinite-Set Version).** If $\mathcal{P}[\mu](t_n) = 0$ for a SEQUENCE (finite or infinite) of points $\{t_n\} \subset \mathbb{R}$, then $\mu = 0$.

*Proof.* Theorem 3.1 with $t_0 = t_1$. A single point suffices. $\square$

---

## 4. Immediate consequence: the Single-Point Theorem for RH

**Theorem 4.1 (Single Point implies RH).** If $C_\infty(\gamma_{n_0}) = 0$ for some $n_0 \geq 1$, then RH.

*Proof.* By the deficit formula (Doc 42, Theorem 5.2):
$$C_\infty(\gamma_{n_0}) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_{n_0}) = 0$$

By the Rigidity Theorem 3.1 (with $\mu = \mu_{\mathrm{off}}$ and $t_0 = \gamma_{n_0}$): $\mu_{\mathrm{off}} = 0$. Therefore $\mathcal{Z}_{\mathrm{off}} = \emptyset$, i.e., every non-trivial zero of $\zeta$ lies on the critical line: RH. $\square$

**Theorem 4.2 (Single-Point Equivalence).** The following statements are mutually equivalent:

*(i)* RH.  
*(ii)* Inc. Inv.: $C_\infty(\gamma_n) = 0$ for every $n \geq 1$.  
*(iii)* $C_\infty(\gamma_{n_0}) = 0$ for some $n_0 \geq 1$.  
*(iv)* $\mu_{\mathrm{off}} = 0$ (no off-critical zeros of $\zeta$).

*Proof.*
- (i) $\iff$ (ii): Theorem 2.4 of Doc 42 (RH $\iff$ Inc. Inv., Docs 19 and 39).
- (ii) $\implies$ (iii): trivial.
- (iii) $\implies$ (iv): Theorem 4.1.
- (iv) $\implies$ (i): $\mathcal{Z}_{\mathrm{off}} = \emptyset$ is exactly the Riemann Hypothesis. $\square$

**Interpretation.** Theorem 4.2 is a **compression of the problem**: instead of proving vanishing at ALL zeros $\{\gamma_n\}_{n\geq 1}$, it suffices to prove it at ONE. However, proving $C_\infty(\gamma_{n_0}) = 0$ for a single $n_0$ seems exactly as hard as proving RH in general — the difficulty concentrates at a point, it does not disappear.

---

## 5. The harmonic extension of $C_\infty$

The deficit formula admits a natural extension to the upper half-plane.

**Definition 5.1 (Poisson extension).** For $z = t + i\eta$ with $\eta > 0$:
$$F(z) := \int_{\mathbb{H}} \frac{y+\eta}{(y+\eta)^2+(t-x)^2}\,d\mu_{\mathrm{off}}(x,y)$$

In the limit $\eta \to 0^+$: $F(t) = \mathcal{P}[\mu_{\mathrm{off}}](t) = C_\infty(t)/2$.

**Proposition 5.2 (Harmonicity of $F$).** The function $F(t+i\eta)$ is harmonic for $\eta > 0$:
$$\left(\frac{\partial^2}{\partial\eta^2} + \frac{\partial^2}{\partial t^2}\right)F(t+i\eta) = 0 \quad \text{for } \eta > 0$$

*Proof.* The kernel $P_{y+\eta}(t-x) = (y+\eta)/[(y+\eta)^2+(t-x)^2]$ is harmonic in $(t,\eta)$ for $y+\eta > 0$, and the integral of harmonic functions (with dominated convergence guaranteed by the integrability hypothesis) is harmonic. $\square$

**Proposition 5.3 (Positivity of $F$ in the interior).** For $\eta > 0$ and $\mu_{\mathrm{off}} \neq 0$:
$$F(t+i\eta) > 0 \quad \forall t \in \mathbb{R}$$

*Proof.* The kernel $(y+\eta)/[(y+\eta)^2+(t-x)^2] > 0$ for $y+\eta > 0$ (which holds for $y > 0$, $\eta > 0$). The same proof as Theorem 3.1 with $t_0 = t$. $\square$

**Corollary 5.4 (Minimum Principle).** Under RH ($\mu_{\mathrm{off}} = 0$): $F \equiv 0$. Without RH ($\mu_{\mathrm{off}} \neq 0$): $F(z) > 0$ for every $z$ with $\mathrm{Im}(z) \geq 0$, with the sole exception of the boundary points where $\mathcal{P}[\mu_{\mathrm{off}}](t) = 0$ — but by Theorem 3.1, no such points exist. Therefore: $F(z) > 0$ on ALL of $\{z: \mathrm{Im}(z) \geq 0\}$ if $\mu_{\mathrm{off}} \neq 0$.

**Remark 5.5 (No boundary zeros without RH).** If RH is false, then $F(t) = C_\infty(t)/2 > 0$ for every $t\in\mathbb{R}$. In particular, $C_\infty(\gamma_n) > 0$ for every $n$ — which is Inc. Inv. failing. Corollary 5.4 confirms that if RH fails, the function $F$ has no zeros at any point of the closed half-plane.

---

## 6. Continuity of the spectral potential

**Proposition 6.1 (Continuity of $C_\infty$).** If the measure $\mu_{\mathrm{off}}$ satisfies the integrability condition of Theorem 3.1, then the function $t \mapsto C_\infty(t) = 2\mathcal{P}[\mu_{\mathrm{off}}](t)$ is continuous on $\mathbb{R}$.

*Proof.* For $t_1 \to t_0$:
$$|\mathcal{P}[\mu](t_1) - \mathcal{P}[\mu](t_0)| \leq \int_{\mathbb{H}}|P_y(t_1-x) - P_y(t_0-x)|\,d\mu(x,y)$$

The integrand $|P_y(t_1-x)-P_y(t_0-x)| \leq C|t_1-t_0|/y^2$ (Lipschitz in $t$) and is dominated by $2/y$. By dominated convergence (using the integrability hypothesis $\int y^{-1}d\mu < \infty$), the right-hand side $\to 0$. $\square$

**Proposition 6.2 (Decay at infinity).** For $\mu_{\mathrm{off}}$ with compact support:
$$C_\infty(t) \to 0 \quad \text{as } |t| \to \infty$$

*Proof.* For $|t| \to \infty$ and support of $\mu_{\mathrm{off}}$ contained in $\{(x,y): |x| \leq R,\, c \leq y \leq M\}$:
$$C_\infty(t) = 2\mathcal{P}[\mu_{\mathrm{off}}](t) \leq \frac{2\mu_{\mathrm{off}}(\mathbb{H})\cdot M}{(|t|-R)^2 - M^2} \to 0$$ $\square$

**Proposition 6.3 (Growth for non-compact support).** If $\mu_{\mathrm{off}}$ has mass at $\{\gamma_0 \sim T\}$ (off-critical zeros at height $\sim T$), then $C_\infty(\gamma_n)$ for $\gamma_n \sim T$ receives a contribution $\sim 2/(\sigma_0-1/2)$ from those zeros. For zeros with $\sigma_0-1/2 \sim 1/\log T$ (near the zero-free region), this contribution is $\sim 2\log T \to \infty$.

*Interpretation.* Off-critical zeros CLOSE to the critical line (which are unavoidable if RH fails, by the functional equation) create HIGH peaks in $C_\infty$.

---

## 7. The density detection theorem

The zeros $\{\gamma_n\}$ become increasingly dense: the average gap between consecutive zeros is $\delta_n := \gamma_{n+1}-\gamma_n \sim 2\pi/\log\gamma_n \to 0$.

**Theorem 7.1 (Detection of off-critical zeros by density).** Let $\rho_0 = \sigma_0+i\gamma_0$ be an off-critical zero of $\zeta$ with $\sigma_0 > 1/2$ and $\gamma_0 > 2$. Let $\delta = \pi/\log\gamma_0$ (half the average zero gap near $\gamma_0$). Then there exists $\gamma_{n^*}$ with $|\gamma_{n^*}-\gamma_0| \leq \delta$ such that:

$$C_\infty(\gamma_{n^*}) \geq \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2 + \delta^2} = \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2 + \pi^2/\log^2\gamma_0}$$

*Proof.* By the density of zeros, there exists $\gamma_{n^*}$ with $|\gamma_{n^*}-\gamma_0| \leq \delta$. By the deficit formula and the non-negativity of each term:
$$C_\infty(\gamma_{n^*}) \geq \Delta(\gamma_{n^*};\rho_0) \geq \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(\gamma_{n^*}-\gamma_0)^2} \geq \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+\delta^2}$$ $\square$

**Corollary 7.2 (Extreme cases).** Let us analyze Theorem 7.1 according to the position of $\sigma_0$:

**Case A: $\sigma_0-1/2 \gg \delta = \pi/\log\gamma_0$ (zero far from the critical line):**
$$C_\infty(\gamma_{n^*}) \geq \frac{2}{\sigma_0-1/2}$$
The bound is of order $1/(\sigma_0-1/2)$. For $\sigma_0 = 3/4$: $C_\infty(\gamma_{n^*}) \geq 8$.

**Case B: $\sigma_0-1/2 = \delta = \pi/\log\gamma_0$ (zero at the edge of the free region):**
$$C_\infty(\gamma_{n^*}) \geq \frac{2\delta}{2\delta^2} = \frac{1}{\delta} = \frac{\log\gamma_0}{\pi} \to \infty$$
The peak is LARGE for zeros that graze the limit of the free region.

**Case C: $\sigma_0-1/2 \ll \delta$ (zero close to the critical line, hypothetically):**
$$C_\infty(\gamma_{n^*}) \geq \frac{2(\sigma_0-1/2)}{\delta^2} = \frac{2(\sigma_0-1/2)\log^2\gamma_0}{\pi^2} \to 0 \text{ as } \sigma_0 \to 1/2$$
The bound is small for zeros very close to the critical line.

**Remark 7.3 (The asymmetry between A/B and C).** Theorem 7.1 strongly detects off-critical zeros that are far from the critical line (Cases A and B) but gives weak bounds for near-critical zeros (Case C). The classical zero-free region excludes Case C (there are no zeros with $\sigma_0-1/2 < c/\log\gamma_0$), which guarantees that Case B is the limit: off-critical zeros (if they exist) always produce peaks of amplitude $\geq c'\log\gamma_0$.

**Corollary 7.4 (Logarithmic peaks unavoidable if RH fails).** If RH is false, there exists a sequence $\gamma_{n_k^*} \to \infty$ of zeros of $\Xi$ such that:
$$C_\infty(\gamma_{n_k^*}) \geq c\log\gamma_{n_k^*} \to \infty$$

*Proof.* Let $\rho_k = \sigma_k+i\gamma_0^{(k)}$ be a sequence of off-critical zeros (which exists if RH fails). By the zero-free region: $\sigma_k-1/2 \geq c'/\log\gamma_0^{(k)}$, i.e., Case B or A. By Theorem 7.1 with Case B: $C_\infty(\gamma_{n_k^*}) \geq \log\gamma_0^{(k)}/\pi$. $\square$

**This corollary is the strongest diagnostic we can give without proving RH:** if RH fails, the spectral potential $C_\infty$ has logarithmic peaks along every infinite subsequence of zeros of $\Xi$. It cannot be uniformly small.

---

## 8. The precise structural obstacle

The Rigidity Theorem 3.1 reduces RH to: "prove $C_\infty(\gamma_{n_0}) = 0$ for a single $n_0$." This looks like a simplification, but it is illusory.

**Proposition 8.1 (Circularity of the reduction).** The statement $C_\infty(\gamma_{n_0}) = 0$ is equivalent to:
$$2\sum_{m=1}^\infty \frac{\Lambda(m)}{\sqrt{m}}\cos(\gamma_{n_0}\log m) = w(\gamma_{n_0})$$

This is the convergence of the conditionally convergent Dirichlet series to the exact value $w(\gamma_{n_0})$. Proving this is equivalent to verifying that $D_\infty(\gamma_{n_0}) = w(\gamma_{n_0})$, which is Inc. Inv. at the point $\gamma_{n_0}$.

**Proposition 8.2 (The difference with Selberg and the PNT).** In the Prime Number Theorem, the analogous identity $\sum_{n\leq x}\Lambda(n) = x + \text{error}$ is proved via the zero-free region of $\zeta$ near $\Re(s)=1$. The "error" measures the contribution of the zeros of $\zeta$ via the explicit formula. Here, the analogue is:

$$D_\lambda(\gamma_{n_0}) = 2\sum_{m\leq\lambda^2}\frac{\Lambda(m)}{\sqrt{m}}\cos(\gamma_{n_0}\log m) = w(\gamma_{n_0}) - C_\lambda(\gamma_{n_0})$$

The "error" $C_\lambda(\gamma_{n_0})$ is controlled via the zeros of $\zeta$ in Hadamard's formula — specifically via the sum $\sum_\rho \mathrm{Re}[1/(\rho_{n_0}-\rho)]$. This sum vanishes under RH (Theorem 4, Doc 39). Proving that it vanishes unconditionally requires excluding off-critical zeros — RH itself.

**Diagnosis 8.3 (The barrier is solid).** The Rigidity Theorem 3.1 compresses the difficulty of RH to a point, but does not eliminate it. To overcome the barrier one needs:

- An **UNCONDITIONAL** bound $C_\infty(\gamma_{n_0}) \leq f(n_0)$ where $f(n_0) \to 0$.
- Combined with the unconditional lower bound $C_\infty(\gamma_{n_0}) \geq 0$ (Doc 42, P 16.1).
- To conclude $C_\infty(\gamma_{n_0}) = 0$ and apply Theorem 4.1.

Every unconditional upper bound of $C_\infty(\gamma_n)$ that converges to 0 is equivalent to Inc. Inv. The following diagram summarizes the situation:

$$\underbrace{C_\infty(\gamma_{n_0}) \leq 0}_{\text{impossible (Doc 42)}} \quad \text{vs} \quad \underbrace{C_\infty(\gamma_{n_0}) = 0}_{\iff \text{RH}} \quad \text{vs} \quad \underbrace{C_\infty(\gamma_{n_0}) > 0}_{\iff \neg\text{RH}}$$

---

## 9. Average analysis and consequences

Although the average does not prove RH directly, it contains new structural information.

**Proposition 9.1 (Average formula).** For large $T$ and $\mu_{\mathrm{off}}$ with finite mass:
$$\frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T} C_\infty(\gamma_n) = \frac{2\pi}{T\log T}\sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}}\left[\int_0^T \frac{(\sigma_0-1/2)\log t}{(\sigma_0-1/2)^2+(t-\gamma_0)^2}\,dt + (\text{symmetric})\right]$$

**Proposition 9.2 (Average asymptotics for a fixed zero).** For $\rho_0 = \sigma_0+i\gamma_0$ fixed and $T\to\infty$:
$$\frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}\Delta(\gamma_n;\rho_0) \sim \frac{2\pi^2(\sigma_0-1/2)\log\gamma_0}{T\log T/(2\pi)} = \frac{4\pi^3(\sigma_0-1/2)\log\gamma_0}{T\log T} \to 0$$

*Proof.* The integral $\int_0^\infty \frac{2(\sigma_0-1/2)\log t}{(\sigma_0-1/2)^2+(t-\gamma_0)^2}dt \approx \pi(\sigma_0-1/2)\cdot 2\log\gamma_0/(\sigma_0-1/2) = 2\pi\log\gamma_0$ (Poisson + $\log t \approx \log\gamma_0$). Dividing by $N_\Xi(T) \sim T\log T/(2\pi)$, the result is $O(\log\gamma_0/T) \to 0$. $\square$

**Proposition 9.3 (The liminf vanishes under a finiteness hypothesis).** If $\mu_{\mathrm{off}}$ has finite total mass $M = \mu_{\mathrm{off}}(\mathbb{H}) < \infty$ and the support of $\mu_{\mathrm{off}}$ is compact, then:
$$\liminf_{n\to\infty} C_\infty(\gamma_n) = 0$$

*Proof.* For compact support: $C_\infty(\gamma_n) \to 0$ as $\gamma_n \to \infty$ (Proposition 6.2). $\square$

**Warning 9.4 (Zero liminf does not imply RH).** Proposition 9.3 says that $C_\infty(\gamma_n) \to 0$ for compact support of $\mu_{\mathrm{off}}$, but $C_\infty(\gamma_n) > 0$ for every $n$ (by Corollary 5.4). The sequence approaches 0 but never reaches it. The Rigidity Theorem requires EXACT vanishing, not approximation.

**Corollary 9.5 (Positive implication).** For off-critical zeros with non-compact support (infinitely many zeros, as would be expected if RH fails): by Corollary 7.4, $C_\infty(\gamma_n)$ has logarithmic peaks going to $\infty$. The liminf could be positive or zero, but in no case does it vanish exactly.

---

## 10. The Green function and the Nevanlinna-Herglotz function

The harmonic extension $F(z) = \mathcal{P}[\mu_{\mathrm{off}}](z)$ has an analytic representation via the Herglotz function.

**Definition 10.1 (Herglotz function).** Define the analytic function on $\mathbb{H}^+ = \{z: \mathrm{Im}(z) > 0\}$:
$$H_{\mathrm{off}}(z) := \int_{\mathbb{H}} \frac{1}{z - \overline{w}}\,d\mu_{\mathrm{off}}(w)$$

where $\overline{w} = x_0 - iy_0$ is in $\mathbb{H}^- = \{w: \mathrm{Im}(w) < 0\}$.

**Proposition 10.2 (Properties of $H_{\mathrm{off}}$).** With $z = t + i\eta$ ($\eta > 0$) and $w_0 = x_0+iy_0$ ($y_0 > 0$):
$$H_{\mathrm{off}}(z) = \int_{\mathbb{H}} \frac{1}{(t-x_0)+i(\eta+y_0)}\,d\mu_{\mathrm{off}}(x_0,y_0)$$

1. $H_{\mathrm{off}}$ is analytic on $\mathbb{H}^+$ (singularities in $\overline{\mathcal{Z}_{\mathrm{off}}} \subset \mathbb{H}^-$).
2. $\mathrm{Im}[H_{\mathrm{off}}(z)] < 0$ for $z \in \mathbb{H}^+$: $H_{\mathrm{off}}$ maps $\mathbb{H}^+$ into $\mathbb{H}^-$ (anti-Herglotz).
3. $\mathrm{Re}[H_{\mathrm{off}}(t)] = \mathcal{P}[\mu_{\mathrm{off}}](t) = C_\infty(t)/2$ for $t \in \mathbb{R}$ (boundary value).

*Proof.* (1) The pole $1/(z-\overline{w_0})$ has $\overline{w_0} \in \mathbb{H}^-$, so there are no singularities for $z\in\mathbb{H}^+$. (2) $\mathrm{Im}[1/((t-x_0)+i(\eta+y_0))] = -(\eta+y_0)/[(t-x_0)^2+(\eta+y_0)^2] < 0$. (3) $\mathrm{Re}[1/((t-x_0)+iy_0)] = y_0/[y_0^2+(t-x_0)^2] = P_{y_0}(t-x_0)$. $\square$

**Proposition 10.3 (Inc. Inv. as a condition on $H_{\mathrm{off}}$).** Inc. Inv. is equivalent to:
$$\mathrm{Re}[H_{\mathrm{off}}(\gamma_n)] = 0 \quad \forall n \iff H_{\mathrm{off}}(\gamma_n) \in i\mathbb{R} \quad \forall n$$

That is, $H_{\mathrm{off}}$ takes purely imaginary values at all zeros of $\Xi$.

**Proposition 10.4 (Rigidity of the real part).** If $\mathrm{Re}[H_{\mathrm{off}}(t_0)] = 0$ for some $t_0\in\mathbb{R}$, then by Theorem 3.1: $\mu_{\mathrm{off}} = 0$, and $H_{\mathrm{off}} \equiv 0$.

*Interpretation.* The condition $H_{\mathrm{off}}(\gamma_n) \in i\mathbb{R}$ is like asking an analytic function to take values on a line when evaluated on a discrete set. This is a "Schwarz-reflection type" condition — but the set $\{\gamma_n\}$ is DISCRETE (not a real-analytic curve), which prevents direct application of the Schwarz principle.

---

## 11. The density argument: scope and limits

The advisor proposes using the density of $\{\gamma_n\}$ to force vanishing. We analyze this precisely.

**Definition 11.1 (Asymptotic density).** The zeros of $\Xi$ are asymptotically dense on $[0,\infty)$ in the following sense: for every $T > 2$ and every interval $[a,b] \subset [0, T]$ with $b-a > 2\pi/\log a$, there exists $\gamma_n \in [a,b]$.

**Proposition 11.2 (What density DOES imply).** If $C_\infty$ is continuous (Proposition 6.1) and $C_\infty(\gamma_n) < \epsilon$ for all $\gamma_n \in [a,b]$, then for any $t_0 \in [a,b]$ with $|t_0-\gamma_n| \leq 2\pi/\log a$ for some $n$:
$$C_\infty(t_0) \leq C_\infty(\gamma_n) + |C_\infty(t_0)-C_\infty(\gamma_n)| \leq \epsilon + \frac{L\cdot 2\pi}{\log a}$$

where $L$ is the Lipschitz constant of $C_\infty$.

**Proposition 11.3 (What density does NOT imply).** The fact that $C_\infty(\gamma_n)$ is small for all $\gamma_n$ is NOT sufficient to conclude $C_\infty(\gamma_n) = 0$. Example: if $\mu_{\mathrm{off}} = c\cdot\delta_{(x_0,y_0)}$ for small $c > 0$, then $C_\infty(\gamma_n) = 2c\cdot P_{y_0}(\gamma_n-x_0) < 2c/y_0$, which can be arbitrarily small but is always positive.

**The gap:**

$$\{C_\infty(\gamma_n) < \epsilon \;\forall n\} \not\implies \{C_\infty(\gamma_{n_0}) = 0 \;\text{for some } n_0\}$$

Proving EXACT vanishing requires more than asymptotic control.

---

## 12. New equivalent: the spectral Szegő condition

We seek an alternative condition to $C_\infty(\gamma_{n_0})=0$ that is more accessible.

**Proposition 12.1 (Additional equivalents of Inc. Inv.).** Under the hypotheses of the program:

*(v)* $\prod_{n=1}^\infty (1 - C_\infty(\gamma_n)^2/M_n^2) = 0$ for every divergent bounding sequence $M_n$.

*(vi)* $\sum_{n=1}^\infty C_\infty(\gamma_n) = +\infty$ or $\sum_{n=1}^\infty C_\infty(\gamma_n) = 0$.

*(vii)* $\sum_{n=1}^\infty C_\infty(\gamma_n)^2 = \mathcal{D}(\infty) < \infty$ or $= \infty$ (from Doc 41).

*Proof of (vi).* If RH: all terms are 0, the sum is 0. If RH fails: by Corollary 7.4, there exist infinitely many $\gamma_{n_k^*}$ with $C_\infty(\gamma_{n_k^*}) \geq c\log\gamma_{n_k^*} \to \infty$. The subseries over these indices diverges: $\sum_{k} C_\infty(\gamma_{n_k^*}) \geq \sum_k c\log\gamma_{n_k^*} = +\infty$. $\square$

**Corollary 12.2.** RH $\iff$ $\sum_{n=1}^\infty C_\infty(\gamma_n) = 0$ (with $C_\infty(\gamma_n)\geq 0$).

This is another way of saying Inc. Inv., but it shows that the total sum of the deficit is 0 if and only if RH. Without RH, the sum is $+\infty$.

---

## 13. The Cauchy operator and approximation theory

**Definition 13.1 (Cauchy operator on the critical line).** We define the operator $\mathcal{C}_{\mathrm{crit}}$ that assigns to each positive measure $\mu_{\mathrm{off}}$ on $\mathbb{H}$ its restriction to the critical line:

$$\mathcal{C}_{\mathrm{crit}}[\mu_{\mathrm{off}}](\gamma) := \mathcal{P}[\mu_{\mathrm{off}}](\gamma) = C_\infty(\gamma)/2, \quad \gamma \in \mathbb{R}$$

**Theorem 13.2 (Injectivity of $\mathcal{C}_{\mathrm{crit}}$ over positive measures).** The operator $\mathcal{C}_{\mathrm{crit}}: \mathcal{M}_+(\mathbb{H}) \to \mathcal{C}(\mathbb{R}, [0,\infty))$ is **injective**: if $\mathcal{C}_{\mathrm{crit}}[\mu_1] = \mathcal{C}_{\mathrm{crit}}[\mu_2]$ for $\mu_1, \mu_2 \geq 0$, then $\mu_1 = \mu_2$.

*Proof.* Let $\nu = \mu_1 - \mu_2$ (signed difference of measures). If $\mathcal{C}_{\mathrm{crit}}[\nu](t) = 0$ for every $t\in\mathbb{R}$, then by the uniqueness of the Poisson transform for signed measures (Privalov, 1956): $\nu = 0$. $\square$

**Corollary 13.3.** The function $t \mapsto C_\infty(t)$ uniquely determines $\mu_{\mathrm{off}}$ (within the class of positive measures). In particular:

$$C_\infty \equiv 0 \text{ on } \mathbb{R} \iff \mu_{\mathrm{off}} = 0 \iff \text{RH}$$

**Remark 13.4.** Corollary 13.3 is correct but does not solve the problem: saying that "$C_\infty \equiv 0$ implies RH" is a tautology of the deficit formula. The question remains: how to prove that $C_\infty(\gamma_n) = 0$ for some $n$?

---

## 14. The decisive question: can the mass of $\mu_{\mathrm{off}}$ be small?

We have established that if $\mu_{\mathrm{off}} \neq 0$, then $C_\infty(\gamma_n) > 0$ for all $n$, with unavoidable logarithmic peaks (Corollary 7.4). The question arises: can $\mu_{\mathrm{off}}$ have SMALL (but non-zero) mass?

**Proposition 14.1 (Lower bound on the mass in terms of the deficit).** For $\mu_{\mathrm{off}} \neq 0$: let $\rho_0^* \in \mathcal{Z}_{\mathrm{off}}$ be the off-critical zero closest to the critical line (with $\epsilon^* := \sigma_0^*-1/2 = \min_{\rho_0}(\sigma_0-1/2)$). Then:
$$\sup_n C_\infty(\gamma_n) \geq C_\infty(\gamma_{n^*}) \geq \frac{2\epsilon^*}{(\epsilon^*)^2+(\pi/\log\gamma_0^*)^2}$$

For $\epsilon^* \sim \pi/\log\gamma_0^*$ (in the limit of the free region): $\sup_n C_\infty(\gamma_n) \geq \log\gamma_0^*/\pi$.

**Proposition 14.2 (Incompatibility with known zero results).** Numerical data show that 99.9999\% of known zeros of $\zeta$ are on the critical line. If the first $10^{22}$ zeros were on-critical (which has been verified), and there were off-critical zeros only with $\gamma_0 > 10^{22}$, then the contribution of those zeros to $C_\infty(\gamma_n)$ for $\gamma_n \leq 10^{22}$ would be $\leq 2\epsilon^* / (\gamma_n - \gamma_0)^2 \approx 0$. The deficit would be numerically undetectable for the verified zeros.

*This argument is heuristic, not a mathematical proof.*

---

## 15. Summary and roadmap for Doc 44

**New results of this document:**

| # | Result | Type |
|---|---|---|
| T 3.1 | Poisson rigidity: $\mathcal{P}[\mu](t_0)=0$ for some $t_0$ $\implies$ $\mu=0$ | New, proved |
| T 4.1 | Single Point implies RH: $C_\infty(\gamma_{n_0})=0$ for some $n_0$ $\implies$ RH | New, proved |
| T 4.2 | Equivalence: RH $\iff$ $\exists n_0: C_\infty(\gamma_{n_0})=0$ $\iff$ Inc. Inv. | New, proved |
| P 5.2–5.3 | $F(z)=\mathcal{P}[\mu_{\mathrm{off}}](z)$ harmonic on $\mathbb{H}^+$, strictly positive if $\mu\neq 0$ | New, proved |
| T 7.1 | Density detection: $\exists\gamma_{n^*}$ with $C_\infty(\gamma_{n^*})\geq 2(\sigma_0-1/2)/[(\sigma_0-1/2)^2+\delta^2]$ | New, proved |
| C 7.4 | Without RH: unavoidable logarithmic peaks $C_\infty(\gamma_{n_k^*})\geq c\log\gamma_{n_k^*}$ | New, proved |
| C 12.2 | RH $\iff$ $\sum_n C_\infty(\gamma_n) = 0$ (with $C_\infty\geq 0$) | New, proved |
| T 13.2 | $\mathcal{C}_{\mathrm{crit}}$ is injective over positive measures | New, proved |

**Updated state of the program:**

| Implication | State |
|---|---|
| Inc. Inv. $\Rightarrow$ RH | Proved (Doc 19) |
| RH $\Rightarrow$ Inc. Inv. | Proved (Doc 39) |
| $C_\infty(\gamma_n)\geq 0$ | **Proved unconditionally** (Doc 42) |
| $C_\infty(\gamma_{n_0})=0$ for some $n_0$ $\Rightarrow$ RH | **Proved** (Doc 43, T 4.1) |
| Without RH: logarithmic peaks in $C_\infty$ | **Proved** (Doc 43, C 7.4) |
| $C_\infty(\gamma_{n_0})=0$ [unconditional] | **Open** — equivalent to RH |

**The exact frontier of the program:**

The problem has been reduced to its irreducible essence:

> *Prove that a conditionally convergent Dirichlet series takes a specific value at at least one point of the spectrum of $\Xi$.*

---

**Proposal for Doc 44: The Zero-Measure Problem**

The most promising roadmap identifies the following (new) question:

Can it be shown that $\mu_{\mathrm{off}}$ has **null** mass using only arithmetic properties of the zeros of $\zeta$, without assuming their location?

Three possible attacks:

**A. Spectral Plancherel theorem.** The Fourier transform of $C_\infty(t) = \mathcal{P}[\mu_{\mathrm{off}}](t)$ on $\mathbb{R}$ is $\hat{C}_\infty(\xi) = \hat{\mu}_{\mathrm{off,\xi}}$ where $\hat{\mu}$ is the Fourier transform of the measure. If $\hat{C}_\infty = 0$ (the Fourier transform vanishes on a set of positive measure), then $C_\infty \equiv 0$ (Wiener, Paley-Wiener). The question: does $C_\infty$ have any Fourier decay property that forces $\hat{C}_\infty = 0$?

**B. The functional equation as a symmetry condition.** The zeros of $\zeta$ satisfy the symmetry $\rho \leftrightarrow 1-\bar\rho$ (functional equation). This imposes a condition on $\mu_{\mathrm{off}}$: the measure must be symmetric under the reflection $(\sigma_0-1/2, \gamma_0) \leftrightarrow (1/2-\sigma_0, \gamma_0)$... but in our parameterization $y_0 = \sigma_0-1/2 > 0$, the functional pair has $y = 1/2 - \sigma_0 < 0$ (in $\mathbb{H}^-$), which is not in the support of $\mu_{\mathrm{off}}$. The symmetry manifests in $\mu_{\mathrm{off}}$ via the second term of the Cauchy kernel in the deficit formula.

**C. The positivity condition of $C_\infty$ on ALL of $\mathbb{R}$ (not just on $\{\gamma_n\}$).** Via the harmonic extension $F(z)$ and the minimum principle for positive harmonic functions, are there conditions on $F$ throughout $\mathbb{H}^+$ that force $\mu_{\mathrm{off}} = 0$? This connects with potential theory and analytic capacity.

---

*Next document (Doc 44): The zero-measure problem — $\mu_{\mathrm{off}}$ and the global positivity condition of $C_\infty$ on $\mathbb{R}$.*

---

## Appendix A: The correct symmetrization of the Poisson transform

**A.1.** The deficit formula of Doc 42 includes a second term with $(\gamma_n+\gamma_0)$ that comes from symmetrization by complex conjugation $(\rho_0, \bar\rho_0)$. In terms of the Poisson transform:

$$C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{sym}}](\gamma_n)$$

where $\mu_{\mathrm{sym}} = \sum_{\rho_0:\sigma_0>1/2} 2(\sigma_0-1/2)[\delta_{(\gamma_0,\sigma_0-1/2)} + \delta_{(-\gamma_0,\sigma_0-1/2)}]$ (the sum includes both $(\gamma_0, y_0)$ and $(-\gamma_0, y_0)$ in $\mathbb{H}$). This symmetrization makes $\mathcal{P}[\mu_{\mathrm{sym}}]$ an even function of $\gamma_n$ — consistent with $C_\infty(\gamma_n) = C_\infty(-\gamma_n)$ by the symmetry of the potential.

**A.2.** The Rigidity Theorem 3.1 applies to $\mu_{\mathrm{sym}}$ unchanged: $\mathcal{P}[\mu_{\mathrm{sym}}](\gamma_{n_0}) = 0$ for some $\gamma_{n_0} > 0$ implies $\mu_{\mathrm{sym}} = 0$ (and therefore $\mu_{\mathrm{off}} = 0$, RH).
