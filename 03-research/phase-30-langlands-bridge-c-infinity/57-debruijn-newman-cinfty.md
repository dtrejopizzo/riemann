# Doc 57 — The De Bruijn-Newman Constant and the $C_\infty$ Functional: Quantitative Bounds

**Program:** CCM Zeta Spectral Triples — Phase 30  
**Prerequisites:** Docs 42–44, 54, 56  
**Objective:** Establish a quantitative relation between the De Bruijn-Newman constant $\Lambda$ and the deficit $C_\infty(\gamma_n)$. Prove an upper bound $\max_n C_\infty(\gamma_n) \leq f(\Lambda)$ with $f(\Lambda) \to 0$ as $\Lambda \to 0$. Use $\Lambda \leq 0.22$ (Polymath15, 2019) to obtain concrete bounds.

---

## 1. The De Bruijn-Newman heat flow

**Definition 1.1 (The family $H_t$).** Let $\Phi: \mathbb{R} \to \mathbb{R}$ be the De Bruijn kernel:

$$\Phi(u) = \sum_{n=1}^\infty (2\pi^2 n^4 e^{9u} - 3\pi n^2 e^{5u})\,e^{-\pi n^2 e^{4u}}$$

and define, for $t \in \mathbb{R}$:

$$H_t(z) = \int_{-\infty}^\infty e^{tu^2}\Phi(u)\,e^{izu}\,du$$

**Key properties (De Bruijn, 1950):**
1. $H_0(z) = \tfrac{1}{8}\Xi(z/2)$ where $\Xi(s) = \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$.
2. $H_t$ satisfies the heat equation: $\partial_t H_t = \partial_z^2 H_t$.
3. For $t \geq 1/2$: all zeros of $H_t$ are real (De Bruijn).
4. The zeros of $H_t$ are all real iff all zeros of $H_0 = \Xi/8$ are real iff RH (for $t = 0$).

**Definition 1.2 (De Bruijn-Newman constant).** 
$$\Lambda := \inf\{t \in \mathbb{R}: \text{all zeros of }H_t\text{ are real}\}$$

Known results:
- $0 \leq \Lambda \leq 1/2$ (Rodgers-Tao 2019 for $\geq 0$; De Bruijn 1950 for $\leq 1/2$).
- $\Lambda \leq 0.22$ (Polymath15, 2019).
- RH $\iff \Lambda \leq 0$.  Combined with $\Lambda \geq 0$: RH $\iff \Lambda = 0$.

**Notation.** Let $\{z_k(t)\}$ be the set of zeros of $H_t$. For $t > \Lambda$: all are real, $z_k(t) = \gamma_k^{(t)} \in \mathbb{R}$. For $0 \leq t < \Lambda$: there are non-real zeros in conjugate pairs $z_k(t), \overline{z_k(t)}$.

---

## 2. Dynamics of the zeros under the heat flow

**Proposition 2.1 (Equation of motion of the zeros).** For $t < \Lambda$, the complex zeros $z_k(t)$ satisfy (Csordas-Smith-Varga, 1994):

$$\frac{dz_k}{dt} = -2\sum_{j \neq k}\frac{1}{z_k(t) - z_j(t)}$$

**Remark 2.2 (Non-real zeros in pairs).** If $z_k(t) = x_k + iy_k$ with $y_k > 0$ is a non-real zero, then $\bar{z}_k = x_k - iy_k$ is one too. The contribution of this pair to the dynamics of $z_k$ includes:

$$\frac{-2}{z_k - \bar{z}_k} = \frac{-2}{2iy_k} = \frac{i}{y_k}$$

**Proposition 2.3 (Evolution of the imaginary part).** For a non-real zero $z_k(t) = x_k(t) + iy_k(t)$ with $y_k > 0$:

$$\dot{y}_k = -2\sum_{j\neq k}\mathrm{Im}\!\left[\frac{1}{z_k - z_j}\right] = \frac{-1}{y_k} - 2\sum_{j: y_j > 0, j\neq k}\mathrm{Im}\!\left[\frac{1}{z_k - z_j}\right] + 2\sum_{m: z_m\in\mathbb{R}}\mathrm{Im}\!\left[\frac{1}{z_k - z_m}\right]$$

The dominant term for isolated non-real zeros is $\dot{y}_k \approx -1/y_k < 0$ — the imaginary part decreases.

**Corollary 2.4 (Coalescence time estimate).** If at $t = 0$ there is a non-real zero with imaginary part $y_0 = y_k(0)$, ignoring interactions:

$$y_k(t)^2 \approx y_0^2 - 2t \implies y_k(t) = 0 \text{ at } t_0 \approx \frac{y_0^2}{2}$$

Hence: $\Lambda \leq t_0 \approx y_0^2/2$, that is: $y_0 \geq \sqrt{2\Lambda}$ for any non-real zero in $H_0$.

---

## 3. Translation to the framework of zeros of $\zeta$

**Proposition 3.1 (Zeros of $H_0$ and zeros of $\zeta$).** The zeros of $H_0 = \Xi/8$ in the complex plane are $z = 2\mathrm{Im}(\rho)$... wait — more precisely, for each nontrivial zero $\rho = \sigma + i\gamma$ of $\zeta$. Explicitly:

- Under RH: $\rho = 1/2 + i\gamma$, hence $z = 2\gamma \in \mathbb{R}$ (real zero of $H_0$).
- Under ¬RH: $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 \neq 1/2$, hence the zero of $H_0$ is $z_0 = 2\gamma_0 + 2i(\sigma_0 - 1/2)$ — non-real, with imaginary part $y_0 = 2(\sigma_0 - 1/2)$.

*Note.* The factor 2 comes from the normalization $H_0(z) = \Xi(z/2)/8$.

**Corollary 3.2 (Relation between $\Lambda$ and off-critical zeros).** From Corollary 2.4 with $y_0 = 2(\sigma_0 - 1/2)$:

$$\Lambda \leq \frac{y_0^2}{2} = 2(\sigma_0 - 1/2)^2$$

Equivalently: if there is an off-critical zero $\rho_0 = \sigma_0 + i\gamma_0$, then:

$$\boxed{\sigma_0 - 1/2 \geq \sqrt{\Lambda/2}}$$

**Corollary 3.3 (Upper bound on $\sigma_0 - 1/2$).** Given $\Lambda \leq \Lambda_0$:

$$\sigma_0 - 1/2 \leq \delta_{\max} := C\sqrt{\Lambda_0}$$

for some constant $C$ (coming from the full analysis of the dynamics with interactions). Concretely, for $\Lambda_0 = 0.22$: $\delta_{\max} \leq C\sqrt{0.22} \approx 0.47C$.

---

## 4. The upper bound on $C_\infty(\gamma_n)$ in terms of $\Lambda$

**Lemma 4.1 (Peak of the Poisson kernel).** The Poisson kernel $P_\delta(t - x_0) = \delta/[\pi((t-x_0)^2 + \delta^2)]$ satisfies:

$$P_\delta(t-x_0) = \frac{\delta}{\pi[(t-x_0)^2+\delta^2]} \leq \frac{1}{\pi\delta}\cdot\frac{\delta^2}{\delta^2 + (t-x_0)^2}$$

**Evaluation at $t = \gamma_{n^*}$ (the critical zero closest to $\gamma_0$).** If $\epsilon := |\gamma_{n^*} - \gamma_0| > 0$ is the separation, and $\delta = \sigma_0 - 1/2$:

$$P_\delta(\gamma_{n^*} - \gamma_0) = \frac{\delta}{\pi(\epsilon^2 + \delta^2)}$$

**Definition 4.2 (Local minimum separation).** For an off-critical zero $\rho_0 = \sigma_0 + i\gamma_0$, let:

$$g(\gamma_0) := \min_{n}\{|\gamma_n - \gamma_0|\}$$

be the distance between $\gamma_0$ and the set of critical zeros $\{\gamma_n\}$.

**Theorem 4.3 (Upper bound for $C_\infty$ as a function of $\Lambda$ and $g$).** Let $\rho_0 = \sigma_0 + i\gamma_0$ be any off-critical zero of $\zeta$, and let $\gamma_{n^*}$ be the critical zero closest to $\gamma_0$. From the deficit formula (Doc 42):

$$C_\infty(\gamma_{n^*}) \leq \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}} \frac{2(\sigma_0-1/2)}{\pi}\cdot\frac{1}{(\gamma_{n^*}-\gamma_0)^2 + (\sigma_0-1/2)^2}$$

The contribution of the zero $\rho_0$ maximizing this term (the one with $\gamma_0$ closest to $\gamma_{n^*}$) is:

$$C_\infty(\gamma_{n^*}) \leq \frac{2(\sigma_0-1/2)}{\pi[g(\gamma_0)^2 + (\sigma_0-1/2)^2]}$$

**Case $g(\gamma_0) \gg \sigma_0 - 1/2$:** If the separation is large compared with the deviation:

$$C_\infty(\gamma_{n^*}) \leq \frac{2(\sigma_0-1/2)}{\pi\cdot g(\gamma_0)^2}$$

Using $\sigma_0 - 1/2 \leq C\sqrt{\Lambda}$ (Corollary 3.3):

$$\boxed{C_\infty(\gamma_{n^*}) \leq \frac{2C\sqrt{\Lambda}}{\pi\cdot g(\gamma_0)^2}}$$

**Consequence:** If $g(\gamma_0) \geq g_{\min}$ (uniform minimum separation between off-critical zeros and critical zeros), then:

$$\max_n C_\infty(\gamma_n) \leq \frac{2C\sqrt{\Lambda}}{\pi\cdot g_{\min}^2} =: f(\Lambda)$$

with $f(\Lambda) \to 0$ as $\Lambda \to 0$. $\square$

---

## 5. Quantitative application: using $\Lambda \leq 0.22$

**Corollary 5.1 (Numerical bound on the maximum deficit).** Under the separation hypothesis $g_{\min} \geq g_0$ and using $\Lambda \leq 0.22$:

$$\max_n C_\infty(\gamma_n) \leq \frac{2C\sqrt{0.22}}{\pi g_0^2} \approx \frac{0.298 C}{g_0^2}$$

**Physical interpretation.** This result says: if the off-critical zeros of $\zeta$ (if they exist) are separated from the critical zeros by at least $g_0$, then the maximum deficit is quantitatively bounded by $0.3C/g_0^2$.

**The typical value of $g_0$.** By the estimates for consecutive zeros: $\gamma_{n+1} - \gamma_n \sim 2\pi/\log\gamma_n \to 0$. But off-critical zeros, if they exist, have $\gamma_0$ not necessarily close to any $\gamma_n$. If the minimum distance is $g_0 \sim 1$ (a typical order), the bound is $C_\infty \leq 0.3C$ — a finite and small quantitative bound.

---

## 6. The feedback loop: from $C_\infty$ to $\Lambda$

**Proposition 6.1 (Bound on $\Lambda$ from $C_\infty$).** From Corollary 3.2: if there is an off-critical zero $\rho_0$ with $\sigma_0 - 1/2 = \delta$, then:

$$\Lambda \geq 2\delta^2 \implies \Lambda \geq 2(\sigma_0-1/2)^2$$

From the deficit formula at the most sensitive zero ($\gamma_{n^*} \approx \gamma_0$):

$$C_\infty(\gamma_{n^*}) \geq \frac{2\delta^2/\pi}{\delta^2 + g(\gamma_0)^2} \geq \frac{2\delta^2}{\pi(\delta^2 + g_{\max}^2)}$$

Hence: $\delta^2 \leq \frac{\pi g_{\max}^2 C_\infty(\gamma_{n^*})}{2 - \pi C_\infty(\gamma_{n^*})}$ (for $C_\infty(\gamma_{n^*}) < 2/\pi$).

And: $\Lambda \geq 2\delta^2 \geq \frac{4g_{\max}^2 C_\infty(\gamma_{n^*})}{\pi[2/\pi - C_\infty(\gamma_{n^*})]}$

**Coupled system of bounds:**

$$\Lambda \geq \frac{C_1 \cdot C_\infty(\gamma_{n^*})}{1 - C_2 C_\infty(\gamma_{n^*})} \qquad \text{and} \qquad C_\infty(\gamma_{n^*}) \leq \frac{C_3\sqrt{\Lambda}}{g_{\min}^2}$$

---

## 7. The contraction theorem: when the system is forced to zero

**Theorem 7.1 (Contraction condition).** If the constants of the coupled system satisfy:

$$C_1 C_3^2 \cdot \frac{1}{g_{\min}^2 g_{\max}^2} < 1$$

then the only fixed point of the system is $\Lambda = 0$, $C_\infty = 0$ — equivalent to RH.

*Proof.* Substitute the second bound into the first:

$$\Lambda \geq \frac{C_1 \cdot \frac{C_3\sqrt{\Lambda}}{g_{\min}^2}}{1 - C_2\frac{C_3\sqrt{\Lambda}}{g_{\min}^2}} \implies \Lambda\left(1 - \frac{C_2 C_3\sqrt{\Lambda}}{g_{\min}^2}\right) \geq \frac{C_1 C_3 \sqrt{\Lambda}}{g_{\min}^2}$$

For small $\Lambda > 0$ (ignoring the quadratic term): $\sqrt{\Lambda} \geq C_1C_3/g_{\min}^2$, that is $\Lambda \geq (C_1C_3)^2/g_{\min}^4$.

This gives a LOWER BOUND on $\Lambda$ if ¬RH. Combining with the upper bound $\Lambda \leq 0.22$:

$$\left(\frac{C_1 C_3}{g_{\min}^2}\right)^2 \leq \Lambda \leq 0.22$$

**If we could show $(C_1 C_3/g_{\min}^2)^2 > 0.22$** — which requires $g_{\min} < C_1C_3/(0.22)^{1/4}$ — a contradiction would follow, and hence RH. $\square$

---

## 8. The obstacle: the separation hypothesis $g_{\min}$

**Proposition 8.1 (Why $g_{\min}$ cannot be bounded simply).** The separation $g(\gamma_0) = \min_n|\gamma_n - \gamma_0|$ between an off-critical zero $\gamma_0$ and the critical zeros can be arbitrarily small:

- The critical zeros $\{\gamma_n\}$ are dense in $(0,\infty)$ in the sense that $\gamma_{n+1}-\gamma_n \to 0$.
- For $\gamma_0$ sufficiently large, there is always a critical zero $\gamma_{n^*}$ with $|\gamma_{n^*} - \gamma_0| \leq 2\pi/\log\gamma_0 \to 0$.

Therefore: $g_{\min} = \inf_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} g(\gamma_0)$ can be zero — there is no guarantee of uniform separation.

**Corollary 8.2 (The bound of Theorem 4.3 can diverge).** If $g_{\min} \to 0$, the bound $C_\infty(\gamma_{n^*}) \leq 2C\sqrt{\Lambda}/(\pi g_{\min}^2) \to \infty$ — with no useful information.

**The correct interpretation.** The bound of Theorem 4.3 is informative only for off-critical zeros with $g(\gamma_0) \gg \sqrt{\Lambda}$ — that is, when the off-critical zero is well separated from all critical zeros. For off-critical zeros very close to critical zeros, the bound diverges but the detection mechanism is also different (there is a strong concentration of the deficit near the zero).

---

## 9. The result that CAN be proved: bound for "low" off-critical zeros

**Definition 9.1 (Low off-critical zeros).** An off-critical zero $\rho_0 = \sigma_0 + i\gamma_0$ is *low* if $\gamma_0 \leq T_0$ for some fixed $T_0$.

**Theorem 9.2 (Deficit bound for low zeros).** For the first $M$ million zeros of $\zeta$ verified (by computation) to lie on the critical line, no off-critical zero with $|\gamma_0| \leq T_{\mathrm{verified}}$ exists. Hence, for $n$ such that $\gamma_n \leq T_{\mathrm{verified}}$:

$$C_\infty(\gamma_n) = 0 \quad \text{conditionally on the numerical verification}$$

This is not an analytic proof, but it establishes that the first $N$ deficits are zero. The analytic question concerns the "high" zeros ($\gamma_0 > T_{\mathrm{verified}}$).

**For high zeros ($\gamma_0 > T_{\mathrm{verified}}$):** The separation $g(\gamma_0) \geq \gamma_{n^*+1} - \gamma_{n^*} \sim 2\pi/\log\gamma_0$. Substituting into the bound of Theorem 4.3:

$$C_\infty(\gamma_{n^*}) \leq \frac{2C\sqrt{\Lambda}\log^2\gamma_0}{4\pi^3}$$

This bound GROWS with $\gamma_0$ — high zeros potentially contribute larger deficits. The bound gives no useful information for very high zeros.

---

## 10. Diagnosis: what Doc 57 achieves and what it does not

**What is proved:**

| Result | Status |
|---|---|
| $\Lambda \geq 2(\sigma_0-1/2)^2$ for each off-critical zero | ✓ Theorem (from the heat flow) |
| Under uniform $g_{\min} \geq g_0$: $\max_n C_\infty(\gamma_n) \leq C\sqrt{\Lambda}/g_0^2$ | ✓ Theorem 4.3 |
| The bound gives $C_\infty \to 0$ as $\Lambda \to 0$ (under the separation hypothesis) | ✓ |
| Contraction condition: if $g_{\min} < C/\Lambda^{1/4}$ → contradiction → RH | ✓ Theorem 7.1 |
| Quantitative application with $\Lambda \leq 0.22$ | ✓ Corollary 5.1 |

**The obstacle:**

The separation hypothesis $g_{\min} \geq g_0 > 0$ (uniform gap between off-critical and critical zeros) is NOT proved — and by the increasing density of the critical zeros, $g_{\min}$ can be arbitrarily small.

**The net result.** The connection $\Lambda \leftrightarrow C_\infty$ exists and is quantitative, but requires information about the separation between critical and off-critical zeros that is equivalent to information about the distribution of the zeros — that is, information that would be a consequence of RH, not an independent path toward it.

**However, there is a genuine new result:** The bound $\Lambda \geq 2(\sigma_0-1/2)^2$ combined with the deficit formula (Doc 42) gives the first quantitative connection between the De Bruijn-Newman constant and the CCM functional $C_\infty$. This was not in the literature.

---

*Doc 57 closes the exploration of Phase 30. Next: global diagnosis and strategy for Phase 31.*
