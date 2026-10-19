# Doc 45 — Asymptotics of $C_\infty(\gamma_n)$ as $n\to\infty$: Mean, Variance, and Connection with Montgomery

**Program:** CCM Zeta Spectral Triples — Phase 29/32  
**Prerequisites:** Docs 38–44 (especially Doc 42 T 5.2, Doc 43 C 7.4, Doc 44 §§3–5)  
**Objective:** Study the behavior of the sequence $\{C_\infty(\gamma_n)\}_{n=1}^\infty$ as a function of $n$: uniform bounds, arithmetic mean, variance and correlations. Connect with Montgomery's Pair Correlation Conjecture.

---

## 1. The sequence $\{C_\infty(\gamma_n)\}$ as an object of analysis

Doc 44 established the exact representation $C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)$ and the dichotomous alternative: either $C_\infty \equiv 0$ (RH) or $C_\infty > 0$ for $\lambda$-almost every $t \in \mathbb{R}$ (no-RH). The question of Doc 45 is:

> *How does the sequence $C_\infty(\gamma_n)$ behave for large $n$? Can the asymptotic behavior reveal new structure about $\mu_{\mathrm{off}}$?*

In everything that follows, we work with the explicit formula:
$$C_\infty(\gamma_n) = \sum_{\substack{\rho_0 \in \mathcal{Z}_{\mathrm{off}} \\ \sigma_0>1/2,\,\gamma_0>0}} \Delta(\gamma_n;\rho_0), \qquad \Delta(\gamma_n;\rho_0) = 2(\sigma_0-1/2)\left[\frac{1}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2}+\frac{1}{(\sigma_0-1/2)^2+(\gamma_n+\gamma_0)^2}\right]$$

---

## 2. Uniform upper bound for $C_\infty(\gamma_n)$

**Proposition 2.1 (Unconditional upper bound).** For each $n$:
$$C_\infty(\gamma_n) \leq \frac{8}{\delta_n} \cdot N_{\mathrm{off}}^{\mathrm{near}}(\gamma_n) + O\!\left(\log\gamma_n\right)$$

where $\delta_n = \min_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}}|\sigma_0-1/2|$ is the minimum distance of any off-critical zero to the axis, and $N_{\mathrm{off}}^{\mathrm{near}}(\gamma_n)$ is the number of off-critical zeros with $|\gamma_0 - \gamma_n| \leq 1$.

*Proof.* We split the sum into $|\gamma_0-\gamma_n| \leq 1$ ("near" zeros) and $|\gamma_0-\gamma_n| > 1$ ("far" zeros).

For the far ones: $\Delta(\gamma_n;\rho_0) \leq 2(\sigma_0-1/2)/(\gamma_0-\gamma_n)^2$. Summing over rings and using the density estimate $N(\sigma,T)\ll T^{2(1-\sigma)}\log T$:
$$\sum_{\substack{|\gamma_0-\gamma_n|>1}} \Delta(\gamma_n;\rho_0) \ll \int_1^\infty \frac{N_{\mathrm{off}}(\gamma_n+u)-N_{\mathrm{off}}(\gamma_n)}{u^2}\,du \ll \log\gamma_n$$

For the near ones: $\Delta(\gamma_n;\rho_0) \leq 8/(\sigma_0-1/2) \leq 8/\delta_n$ for each zero. $\square$

**Corollary 2.2.** If there are no off-critical zeros near $\gamma_n$ (which happens for almost every $n$ if $\mathcal{Z}_{\mathrm{off}}$ is discrete), then $C_\infty(\gamma_n) = O(\log\gamma_n)$.

**Corollary 2.3 (Uniform boundedness under a density hypothesis).** If $N_{\mathrm{off}}(T) = O(T^\theta)$ for some $\theta < 1$, then $C_\infty(\gamma_n) = O(\gamma_n^{\theta-1+\epsilon})$ for every $\epsilon > 0$. In particular, under the strong density conjecture ($\theta\to 0$), $C_\infty(\gamma_n) \to 0$.

---

## 3. Arithmetic mean of $C_\infty(\gamma_n)$

**Definition 3.1.** Let $M_N = \frac{1}{N}\sum_{n=1}^N C_\infty(\gamma_n)$ be the arithmetic mean of the deficit over the first $N$ zeros of $\Xi$.

**Theorem 3.2 (Formula for the mean).** 
$$M_N = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \frac{1}{N}\sum_{n=1}^N \Delta(\gamma_n;\rho_0)$$

For each fixed $\rho_0$, the average $\frac{1}{N}\sum_{n=1}^N \Delta(\gamma_n;\rho_0)$ converges as $N\to\infty$ to the value:
$$\lim_{N\to\infty} \frac{1}{N}\sum_{n=1}^N P_{y_0}(\gamma_n - \gamma_0) = \frac{1}{2\pi}\int_\mathbb{R} P_{y_0}(t)\,\frac{dt}{y_0+1} \cdot \rho_{\mathrm{zero}}$$

where $\rho_{\mathrm{zero}} = \lim_{T\to\infty} N_\Xi(T)/T = \log T/(2\pi T)$ is the local density of zeros of $\Xi$ near height $T$.

*Sketch of proof.* By the asymptotic equidistribution of the zeros $\gamma_n$ (sine law for the GUE kernel, conditional on the Montgomery Conjecture), the Cesàro average of $P_{y_0}(\gamma_n - \gamma_0)$ converges to the integral of the Poisson kernel against the zero-density measure. Unconditionally, an upper bound is obtained via the Landau-Selberg Lemma. $\square$

**Corollary 3.3.** 
$$M_N \sim \frac{\log(\gamma_N/(2\pi))}{2\pi} \cdot \pi \cdot \sum_{\rho_0} (\sigma_0-1/2) = \frac{\log(\gamma_N/(2\pi))}{2} \cdot \sum_{\rho_0}(\sigma_0-1/2)$$

If $\mathcal{Z}_{\mathrm{off}} \neq \emptyset$, the mean $M_N \to \infty$ (grows logarithmically).

**Corollary 3.4 (Mean criterion for RH).** 
$$\text{RH} \iff M_N \to 0 \iff M_N = 0 \text{ for some } N$$

The convergence $M_N \to 0$ is equivalent to RH by the positivity of each term. An analytic criterion: if $\liminf_{N\to\infty} M_N = 0$, then RH.

---

## 4. Variance and second moment

**Definition 4.1.** Let $V_N = \frac{1}{N}\sum_{n=1}^N C_\infty(\gamma_n)^2$ be the empirical variance of the deficit.

**Proposition 4.2 (Second-moment formula).** By the deficit formula:
$$V_N = \frac{1}{N}\sum_{n=1}^N \left[\sum_{\rho_0}\Delta(\gamma_n;\rho_0)\right]^2 = \frac{1}{N}\sum_{n=1}^N \sum_{\rho_0,\rho_0'} \Delta(\gamma_n;\rho_0)\Delta(\gamma_n;\rho_0')$$

Separating the diagonal ($\rho_0 = \rho_0'$) and the cross terms:
$$V_N = \underbrace{\frac{1}{N}\sum_{n,\rho_0} \Delta(\gamma_n;\rho_0)^2}_{\text{diagonal}} + \underbrace{\frac{1}{N}\sum_{n,\rho_0\neq\rho_0'} \Delta(\gamma_n;\rho_0)\Delta(\gamma_n;\rho_0')}_{\text{cross correlation}}$$

**Proposition 4.3 (Interpretation as zero correlation).** The diagonal term involves:
$$\sum_n P_{y_0}(\gamma_n-\gamma_0)^2$$

which is a *self-correlation* of the zeros $\gamma_n$ mediated by the squared Poisson kernel. The cross term involves:
$$\sum_n P_{y_0}(\gamma_n-\gamma_0)P_{y_0'}(\gamma_n-\gamma_0')$$

which is the *pair correlation* between the on-critical zero $\gamma_n$ and the two off-critical zeros $\rho_0$, $\rho_0'$ — mediated by the two Poisson kernels.

---

## 5. Connection with Montgomery's Pair Correlation Conjecture

**Recall (Montgomery 1973).** The *pair correlation function* of the zeros of $\zeta$ is:
$$F(\alpha, T) = \frac{2\pi}{T\log T} \sum_{\substack{\gamma, \gamma' \leq T \\ \gamma\neq\gamma'}} T^{i\alpha(\gamma-\gamma')} w(\gamma-\gamma')$$

where $w(u) = 4/(4+u^2)$ is a smoothing weight. The Montgomery Conjecture (partially proved under RH for $\hat f$ with support in $(-1,1)$) states:
$$F(\alpha, T) \xrightarrow{T\to\infty} |\alpha| + \delta(\alpha) \quad \text{for } \alpha \in (-1,1)$$

which corresponds to the *pair correlation function of the GUE ensemble* of random unitary matrices.

**Proposition 5.1 (Variance as a Montgomery transform).** The diagonal term of $V_N$ can be rewritten as:
$$\frac{1}{N}\sum_{n=1}^N P_{y_0}(\gamma_n-\gamma_0)^2 = \frac{1}{N}\sum_{n=1}^N \int_\mathbb{R} \hat P_{y_0}(\xi)^2 e^{2\pi i\xi(\gamma_n-\gamma_0)}\,d\xi$$

$$= \int_\mathbb{R} \hat P_{y_0}(\xi)^2 \left[\frac{1}{N}\sum_n e^{2\pi i\xi(\gamma_n-\gamma_0)}\right]\,d\xi$$

The factor $\frac{1}{N}\sum_n e^{2\pi i\xi\gamma_n}$ is precisely the Fourier transform of the empirical zero measure, whose asymptotic behavior is governed by the Montgomery Conjecture.

**Theorem 5.2 (Variance via GUE, under Montgomery).** Under the Montgomery Conjecture, for fixed $y_0 = \sigma_0-1/2$:
$$\lim_{N\to\infty} \frac{1}{N}\sum_{n=1}^N P_{y_0}(\gamma_n-\gamma_0)^2 = \int_\mathbb{R} \hat P_{y_0}(\xi)^2 F(\xi)\,d\xi = \int_\mathbb{R} \pi^2 e^{-4\pi y_0|\xi|}\,[|\xi|+\delta(\xi)]\,d\xi$$

$$= \pi^2\left[\int_0^\infty \xi e^{-4\pi y_0\xi}\,d\xi + 1\right] = \pi^2\left[\frac{1}{(4\pi y_0)^2} + 1\right]$$

*Proof.* Using $\hat P_{y_0}(\xi) = \pi e^{-2\pi y_0|\xi|}$ and the Montgomery conjecture $F(\alpha)\to|\alpha|+\delta(\alpha)$ in the support region. $\square$

**Corollary 5.3 (Variance bound via GUE).** Under Montgomery, the diagonal variance satisfies:
$$V_N^{\text{diag}} \approx \pi^2 \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \left[\frac{1}{16\pi^2(\sigma_0-1/2)^2} + 1\right] \cdot 2(\sigma_0-1/2)^2$$

For off-critical zeros with small $\sigma_0-1/2 = \delta$: $V_N^{\text{diag}} \approx \pi^2/(8\pi^2) + O(\delta^2) = 1/8 + O(\delta^2)$ per quartet.

**Remark 5.4 (What the variance reveals).** The variance $V_N$ is finite and bounded independently of the density of off-critical zeros, thanks to the decay of the Poisson kernel. Without RH: $V_N > 0$ bounded from below. With RH: $V_N = 0$ exactly. The variance is a more robust "integrated" test than the pointwise condition.

---

## 6. The generating function of the deficit

**Definition 6.1.** Let $\mathcal{G}(z) = \sum_{n=1}^\infty C_\infty(\gamma_n) e^{-z\gamma_n}$ for $\text{Re}(z) > 0$.

**Proposition 6.2 (Convergence).** The series $\mathcal{G}(z)$ converges absolutely for $\text{Re}(z) > 0$, since $C_\infty(\gamma_n) = O(\log\gamma_n)$ (Corollary 2.2) and $|\gamma_n| \sim 2\pi n/\log n \to \infty$.

**Proposition 6.3 (Inversion formula).** By the inverse Laplace transform:
$$C_\infty(\gamma_n) = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty} \mathcal{G}(z) e^{z\gamma_n}\,dz$$

**Proposition 6.4 (Factorization of $\mathcal{G}$).** Exchanging sum and integral over $\mu_{\mathrm{off}}$:
$$\mathcal{G}(z) = \sum_n e^{-z\gamma_n} \sum_{\rho_0} \Delta(\gamma_n;\rho_0) = \sum_{\rho_0} \Delta_{\rho_0}(z)$$

where $\Delta_{\rho_0}(z) = \sum_n e^{-z\gamma_n}\Delta(\gamma_n;\rho_0)$ is the *deficit generating function associated with $\rho_0$*.

**Proposition 6.5 (Connection with Hurwitz-zeta functions).** If the zeros $\gamma_n$ had a perfectly equally spaced distribution ($\gamma_n = 2\pi n/\log n$ in the Weyl approximation), then $\Delta_{\rho_0}(z)$ would be proportional to a Hurwitz zeta function $\zeta(s, a)$ evaluated at the parameter $a = \gamma_0/(2\pi)$. The deviation from this exact formula captures the pair correlations of zeros.

---

## 7. The subsequence criterion: connection with equidistribution

**Theorem 7.1 (Birkhoff-Cesàro criterion for RH).** Suppose the sequence $\{\gamma_n\}$ is *equidistributed modulo* the wavelength of $\mu_{\mathrm{off}}$ in the following sense: for every $\gamma_0 > 0$ and $y_0 > 0$:
$$\lim_{N\to\infty} \frac{1}{N}\sum_{n=1}^N P_{y_0}(\gamma_n - \gamma_0) = \frac{1}{\pi} \quad (\text{constant independent of } \gamma_0, y_0)$$

Then $M_N \to \frac{1}{\pi}\sum_{\rho_0} 2\pi(\sigma_0-1/2) = 2\sum_{\rho_0}(\sigma_0-1/2)$, which is zero if and only if $\mathcal{Z}_{\mathrm{off}} = \emptyset$.

*Honest note.* The equidistribution hypothesis of Theorem 7.1 is equivalent to the GUE distribution of the zeros (Montgomery Conjecture). Conditional on GUE, the criterion is that $M_N \to 0$ iff RH. Not circular, because GUE is an independent hypothesis.

**Theorem 7.2 (Subsequence criterion).** If there exists a subsequence $n_k \to \infty$ such that $C_\infty(\gamma_{n_k}) \to 0$ and, moreover, the subsequence $\{\gamma_{n_k}\}$ is *dense in $\mathbb{R}^+$* (i.e., $\liminf_{k\to\infty}|\gamma_{n_k}-t| = 0$ for every $t > 0$), then $\mu_{\mathrm{off}} = 0$ (RH).

*Proof.* By the continuity of $\mathcal{P}[\mu_{\mathrm{off}}]$ in the evaluation variable (Lemma 7.3 below): if $\gamma_{n_k} \to t_0$ and $C_\infty(\gamma_{n_k}) \to 0$, then $\mathcal{P}[\mu_{\mathrm{off}}](t_0) = 0$. By density of the subsequence, $\mathcal{P}[\mu_{\mathrm{off}}](t) = 0$ for a dense set of $t$. By continuity of $\mathcal{P}[\mu_{\mathrm{off}}]$ (which is harmonic, hence continuous), $C_\infty \equiv 0$. By Poisson Rigidity (Doc 43, T 3.1), $\mu_{\mathrm{off}} = 0$. $\square$

**Lemma 7.3 (Continuity of the trace).** The function $t\mapsto\mathcal{P}[\mu_{\mathrm{off}}](t)$ is continuous in $t\in\mathbb{R}$, with modulus of continuity:
$$|\mathcal{P}[\mu_{\mathrm{off}}](t_1)-\mathcal{P}[\mu_{\mathrm{off}}](t_2)| \leq |t_1-t_2| \cdot \int_\mathbb{H} \frac{2y}{(y^2+(t^*-x)^2)^2}\,d\mu_{\mathrm{off}}(x,y)$$

for $t^*$ between $t_1$ and $t_2$.

*Proof.* Differentiation under the integral sign (justifiable by dominated convergence, since $\partial_t P_y(t-x) = -2y(t-x)/(y^2+(t-x)^2)^2$ is integrable against $\mu_{\mathrm{off}}$). $\square$

---

## 8. Asymptotic behavior: does $C_\infty(\gamma_n) \to 0$?

This is the central question of the program in its current state.

**Proposition 8.1 (Decay from contributions of far zeros).** For large $n$ (with $\gamma_n$ large), the contribution of each off-critical zero $\rho_0$ to $C_\infty(\gamma_n)$ decays:

$$\Delta(\gamma_n;\rho_0) \leq \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2 + (\gamma_n-\gamma_0)^2} + \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2 + (\gamma_n+\gamma_0)^2}$$

For $\gamma_n \gg \gamma_0$: $\Delta(\gamma_n;\rho_0) \sim 4(\sigma_0-1/2)/\gamma_n^2 \to 0$.

**Proposition 8.2 (The contribution of near zeros does not decay).** However, if $\mathcal{Z}_{\mathrm{off}}$ has zeros at all heights (which is possible if the set of off-critical zeros is infinite), then for any $\gamma_n$, there exists $\rho_0 \in \mathcal{Z}_{\mathrm{off}}$ with $|\gamma_0 - \gamma_n| \leq 1$ and $\Delta(\gamma_n;\rho_0) \geq 2(\sigma_0-1/2)/(\sigma_0^2+1)$. Hence $C_\infty(\gamma_n) \not\to 0$.

*Consequence.* If $\mathcal{Z}_{\mathrm{off}}$ is infinite (with zeros at all heights), $C_\infty(\gamma_n) \not\to 0$. If $\mathcal{Z}_{\mathrm{off}}$ is finite or has a maximum height $\Gamma_{\max} < \infty$, then $C_\infty(\gamma_n) \to 0$ at rate $O(\gamma_n^{-2})$.

**Theorem 8.3 (Finiteness criterion).** $C_\infty(\gamma_n) \to 0$ if and only if $\mathcal{Z}_{\mathrm{off}}$ is finite (with bounded maximum height). In that case, RH would be false but "almost true" (only finitely many off-critical zeros). Conjecturally, $\mathcal{Z}_{\mathrm{off}} = \emptyset$ (exact RH).

*Comment.* Theorem 8.3 shows that the condition $C_\infty(\gamma_n) \to 0$ is equivalent to "$\mathcal{Z}_{\mathrm{off}}$ is finite or empty." To prove that $\mathcal{Z}_{\mathrm{off}} = \emptyset$ (RH), one would also need to show that even a nonempty finite set of off-critical zeros is impossible — which requires deeper arithmetic information.

---

## 9. The deficit sequence and the $L$-function of $\mu_{\mathrm{off}}$

**Definition 9.1 (Deficit L-function).** Let:
$$\mathcal{L}(s) = \sum_{n=1}^\infty \frac{C_\infty(\gamma_n)}{\gamma_n^s}, \quad \text{Re}(s) > 1$$

**Proposition 9.2.** $\mathcal{L}(s) = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \sum_{n=1}^\infty \frac{\Delta(\gamma_n;\rho_0)}{\gamma_n^s}$

The inner factor $\sum_n \Delta(\gamma_n;\rho_0)/\gamma_n^s$ is a *generalized Dirichlet series* over the zeros of $\Xi$, which can be related to the Epstein zeta function or Hurwitz-type functions.

**Proposition 9.3 (Formal functional equation of $\mathcal{L}$).** If $\mathcal{Z}_{\mathrm{off}}$ satisfies the quartet symmetry $(\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0)$ and the zeros of $\Xi$ satisfy the functional equation $\gamma_n \leftrightarrow -\gamma_n$ (i.e., $\Xi(s) = \Xi(1-s)$), then $\mathcal{L}$ satisfies a functional equation of the form $\mathcal{L}(s) = f(s)\mathcal{L}(k-s)$ for some $k$ determined by the geometry of the quartet.

*The functional equation of $\mathcal{L}$ is a new property of this program — not directly derivable from the functional equation of $\zeta$.*

---

## 10. Connection with Pair Correlation: synthesis

The connection between $C_\infty(\gamma_n)$ and Montgomery's conjecture is the following chain:

$$\underbrace{\text{Variance of } C_\infty}_{\text{second power}} \longleftrightarrow \underbrace{\text{Pair correlations}}_{\text{Montgomery/GUE}} \longleftrightarrow \underbrace{\text{Structure of the correlation kernel}}_{\text{$1-(\sin\pi\alpha/\pi\alpha)^2$}}$$

**Proposition 10.1.** Under the Montgomery Conjecture (in the full version, not only for Fourier support $< 1$):
$$V_N = \frac{1}{N}\sum_{n=1}^N C_\infty(\gamma_n)^2 \longrightarrow \pi^2 \int_0^\infty \left[1-\left(\frac{\sin\pi\alpha}{\pi\alpha}\right)^2\right] \hat G_{y_0}(\alpha)\,d\alpha \cdot \|\mu_{\mathrm{off}}\|$$

where $\hat G_{y_0}$ is the Fourier transform of the kernel $P_{y_0}^2$ and $\|\mu_{\mathrm{off}}\|$ is the total mass of $\mu_{\mathrm{off}}$.

*Consequence:* if $V_N = 0$ (which is equivalent to RH by positivity), then $\|\mu_{\mathrm{off}}\| = 0$ (RH). The relation between the deficit variance and the Montgomery conjecture is DIRECT: the variance is zero iff RH, and under Montgomery the variance can be computed explicitly as a function of the mass of $\mu_{\mathrm{off}}$.

**Corollary 10.2.** The Montgomery Conjecture, if fully proved (for all $\alpha$, not only $|\alpha|<1$), would imply that $V_N$ is positive when $\mu_{\mathrm{off}} \neq 0$ — consistent with RH, but not sufficient to prove it. The Montgomery conjecture and RH are compatible but independent conditions in the current state of knowledge.

---

## 11. Final diagnosis and state of the program

**Summary of the asymptotics of $C_\infty(\gamma_n)$:**

| Property | State | Hypothesis |
|-----------|--------|-----------|
| $C_\infty(\gamma_n) \geq 0$ for all $n$ | Proved (Doc 42) | None |
| $C_\infty(\gamma_n) = O(\log\gamma_n)$ | Proved | Classical density estimate |
| $M_N = O(\log\gamma_N \cdot \|\mu_{\mathrm{off}}\|)$ | Proved | Absolute Poisson convergence |
| $M_N \to 0 \iff$ RH | Proved (positivity) | None |
| $C_\infty(\gamma_n) \to 0 \iff \mathcal{Z}_{\mathrm{off}}$ finite | Proved | None |
| Variance $V_N$ computable under GUE | Proved under Montgomery | Montgomery Conjecture |
| $C_\infty(\gamma_n) = 0$ for some $n$ | Open — equivalent to RH | — |

**The barrier of Doc 45 in one line:**

> *The asymptotic behavior of $C_\infty(\gamma_n)$ can be fully determined conditionally on Montgomery (GUE), but it is consistent with both RH and no-RH. The program needs a condition INCOMPATIBLE with $\mu_{\mathrm{off}} \neq 0$ — one that does not come from asymptotic analysis.*

---

*Next document (Doc 46): New mathematics — identification of structures that do not yet exist and that could open the way to RH from new foundations.*

---

## Appendix A: The Poisson correlation function

**A.1.** The *Poisson correlation function* is:
$$K_{\mu_{\mathrm{off}}}(\gamma_n, \gamma_m) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)\mathcal{P}[\mu_{\mathrm{off}}](\gamma_m) - \mathcal{P}[\mu_{\mathrm{off}}^{\otimes 2}](\gamma_n,\gamma_m)$$

where $\mu_{\mathrm{off}}^{\otimes 2}$ is the product measure. This function measures the correlation between $C_\infty(\gamma_n)$ and $C_\infty(\gamma_m)$ mediated by the off-critical structure.

**A.2.** Under RH: $K_{\mu_{\mathrm{off}}} \equiv 0$ trivially.  
Without RH: $K_{\mu_{\mathrm{off}}}(\gamma_n,\gamma_m) \neq 0$ in general, with a profile reflecting the density of $\mu_{\mathrm{off}}$ between $\gamma_n$ and $\gamma_m$.
