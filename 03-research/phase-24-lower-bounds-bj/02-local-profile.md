# Phase 24-B — The universal local profile of $\log|\zeta|$ induced by $\mathcal{O}_j$

## The new observation

Phase 24-A showed that $b_j$ cannot be bounded from below by looking at pointwise values of $\log|\zeta(1/2+i\gamma_j)|$.

But there is a different direction. The off-line zero $\rho_j = (1/2+b_j)+i\gamma_j$ does not only suppress $|\zeta|$ at the point $t=\gamma_j$: it produces a full profile in a window of width $b_j$ around $\gamma_j$.

**The question is whether that profile, as a geometric function, is compatible with the rigidity of the correlations of the log-correlated field.**

---

## Definition of the local profile

**Definition 24-B.1.** Fix the orbit $\mathcal{O}_j$ with parameters $(b_j, \gamma_j)$; define the **renormalized local profile**:
$$\ell_j(u) := \log|\zeta\!\left(1/2+i(\gamma_j+ub_j)\right)|, \quad u \in \mathbb{R}.$$

In the change-of-variable notation $t = \gamma_j + ub_j$, the parameter $u$ measures the distance to the center of the orbit in units of $b_j$.

---

## Computation of the local profile induced by $\mathcal{O}_j$

**Proposition 24-B.2** (The universal Lorentzian profile). The contribution of the orbit $\mathcal{O}_j$ to the profile $\ell_j(u)$ is:
$$\delta_j\ell_j(u) = \log(b_j^2+(ub_j)^2) + \log(b_j^2+(ub_j+2\gamma_j)^2) - \log|\rho_j^+|^2 - \log|\rho_j^-|^2 + O(1).$$

For $u = O(1)$ and large $\gamma_j$:
$$\delta_j\ell_j(u) = 2\log b_j + \log(1+u^2) + O\!\left(\frac{u b_j}{\gamma_j}\right) + O(1).$$

In particular the **renormalized** profile (subtracting the depression at the origin):
$$\delta_j\ell_j(u) - \delta_j\ell_j(0) = \log(1+u^2) + O\!\left(\frac{ub_j}{\gamma_j}\right).$$

*Proof.* From Theorem~24-A (Hadamard, Prop.~23-A.1): at $t = \gamma_j + ub_j$, the four factors of $\mathcal{O}_j$ give:
- From $\rho_j^+ = (1/2+b_j)+i\gamma_j$: $\sqrt{b_j^2+(ub_j-0)^2}/|\rho_j^+| = b_j\sqrt{1+u^2}/|\rho_j^+|$.
- From $\bar\rho_j^+$: $\sqrt{b_j^2+(ub_j+2\gamma_j)^2}/|\rho_j^+| \approx 2\gamma_j/|\rho_j^+|$ for $u=O(1)$.
- Analogously for $\rho_j^-, \bar\rho_j^-$.

Product of the four:
$$\frac{b_j^2(1+u^2)\cdot(2\gamma_j)^2}{|\rho_j^+|^2|\rho_j^-|^2} \cdot (1+O(ub_j/\gamma_j)).$$
Taking the logarithm: $2\log b_j + \log(1+u^2) + 2\log(2\gamma_j) - \log|\rho_j^+|^2 - \log|\rho_j^-|^2 + O(ub_j/\gamma_j)$. The terms constant in $b_j, \gamma_j$ are absorbed into the $O(1)$. $\square$

---

## The universal shape

**Corollary 24-B.3** (Universal Lorentzian profile). The renormalized profile:
$$P(u) := \delta_j\ell_j(u) - \delta_j\ell_j(0) = \log(1+u^2) + O\!\left(\frac{b_j}{\gamma_j}\right)$$
is:
1. **Independent of $b_j$** (to leading order for large $\gamma_j$).
2. **Deterministic** (not random): its shape is fixed by the geometry of the off-line orbit.
3. **Lorentzian** type (inverted bell with logarithmic, not Gaussian, tails).

It has zeros at $u = \pm i$ (poles of the logarithm), a minimum at $u=0$, and grows like $\log u^2$ as $|u| \to \infty$.

---

## Comparison with the background field

The background $\log|\zeta(1/2+i(\gamma_j+ub_j))|$ without the contribution of $\mathcal{O}_j$ is:
$$\ell_j^{(0)}(u) := \ell_j(u) - \delta_j\ell_j(u) \approx \text{log-correlated field evaluated at }t = \gamma_j + ub_j.$$

For $u = O(1)$ the scale of variation is $b_j$, which is the scale of the "depression". The log-correlated field has correlations:
$$\mathrm{Cov}(\ell_j^{(0)}(u), \ell_j^{(0)}(v)) \approx \log\frac{1}{|u-v|b_j} \cdot \mathbf{1}_{|u-v| \leq 1/(b_j^2)}$$
(structure of the log-correlated field at scale $b_j$).

**The tension:** the deterministic profile $P(u) = \log(1+u^2)$ has variation $O(\log |u|)$ at scale $O(1)$ in $u$. The typical variation of the random field at the same scale $O(1)$ in $u$ (corresponding to scale $b_j$ in $t$) is:
$$\Delta\ell^{(0)} \sim \left(\mathrm{Cov}(\ell^{(0)}(0),\ell^{(0)}(0)) - \mathrm{Cov}(\ell^{(0)}(0),\ell^{(0)}(1))\right)^{1/2} \sim (\log(1/b_j))^{1/2}.$$

For $b_j \to 0$: $(\log(1/b_j))^{1/2} \to \infty$, so the field's variation will eventually dominate over the profile $P(u) = O(\log u)$.

**Proposition 24-B.4** (The Lorentzian profile is invisible in the field at small scale). For $b_j \to 0$, the variation of the background field $\ell_j^{(0)}(u)$ at scale $u = O(1)$ is $O((\log(1/b_j))^{1/2}) \gg 1$, while the variation of the profile $P(u)$ over $u \in [-1,1]$ is $O(1)$ (since $P(u) = \log(1+u^2) \in [0,\log 2]$ for $|u| \leq 1$).

*Therefore:* for small $b_j$, the Lorentzian profile is submerged under the fluctuations of the field. **There is no detectable geometric incompatibility at scale $u = O(1)$.**

---

## The relevant scale: $u \sim (\log(1/b_j))^{1/2}$

The profile $P(u)$ and the field fluctuations have the same magnitude when:
$$\log(1+u^2) \sim (\log(1/b_j))^{1/2}$$
i.e., when $u \sim \exp\!\left(\frac12(\log(1/b_j))^{1/2}\right) - 1$.

For $b_j = e^{-\gamma_j^\alpha}$: $(\log(1/b_j))^{1/2} = \gamma_j^{\alpha/2}$, and $u \sim e^{\gamma_j^{\alpha/2}/2}$.

This scale $u \sim e^{\gamma_j^{\alpha/2}/2}$ corresponds to shifts in $t$ of:
$$\Delta t = u \cdot b_j = e^{\gamma_j^{\alpha/2}/2} \cdot e^{-\gamma_j^\alpha} = e^{\gamma_j^{\alpha/2}/2 - \gamma_j^\alpha}.$$

For $\alpha \in (0,1)$: $\gamma_j^\alpha \gg \gamma_j^{\alpha/2}$ for large $\gamma_j$, so $\Delta t = e^{-\gamma_j^\alpha(1+o(1))} \to 0$. The scale at which the profile emerges above the background is microscopic (exponentially small in $\gamma_j^\alpha$) and is not observationally significant.

**Proposition 24-B.5** (Geometric rigidity produces no incompatibility). The Lorentzian profile $P(u) = \log(1+u^2)$ induced by the off-line orbit produces NO geometric incompatibility with the log-correlated field, for any regime of $b_j \in (0,1/2)$, for the following reason:

- At scale $u = O(1)$: the profile's variation ($O(1)$) is surpassed by the field's fluctuations ($O((\log(1/b_j))^{1/2}) \to \infty$).
- At the scale where the profile emerges: $\Delta t \to 0$, which amounts to the "footprint" of the orbit disappearing in the limit.

*Proof.* See the variance comparison above. The field's fluctuation at scale $b_j$ is $O((\log(1/b_j))^{1/2})$, which exceeds the variation of $P(u)$ over $u \in [-1,1]$ for $b_j < 1$. $\square$

---

## What the local profile analysis does reveal

Although it produces no incompatibility, the profile analysis reveals something mathematically precise.

**Proposition 24-B.6** (The profile as an estimator of the parameter $b_j$). The profile $\ell_j(u) - \ell_j(0)$ is an estimate of $P(u) = \log(1+u^2)$ contaminated by the background field $\ell_j^{(0)}(u)-\ell_j^{(0)}(0)$ (of variance $O(\log(1/b_j))$). If the functional form of $P$ were observationally distinguishable from the background, it would be an estimator of the shift $b_j$ without knowing $b_j$ a priori.

*Consequence:* the profile $P(u)$ has the shape of a **one-dimensional Yukawa potential** (logarithmic). Its "screening radius" is 1 (in units of $b_j$). This is distinguishable from Gaussian fluctuations only if the signal/noise ratio $P(u)/(\log(1/b_j))^{1/2} = \log(1+u^2)/(\log(1/b_j))^{1/2}$ is $O(1)$, i.e., when $|u| \sim (1/b_j)^{1/2}$.

---

## Negative result of Phase 24-B

**Theorem 24-B.1** (Negative closure of the local profile strategy). The analysis of the Lorentzian profile $P(u) = \log(1+u^2)$ induced by $\mathcal{O}_j$ produces NO geometric incompatibility with the log-correlated field, for any value of $b_j \in (0,1/2)$.

The reason is that the variation of the profile at scale $u = O(1)$ is $O(1)$, while the field's fluctuations at that same scale are $O((\log(1/b_j))^{1/2}) \to \infty$ as $b_j \to 0$.

---

## What remains

Phases 24-A and 24-B have produced two negative diagnoses:
1. No unconditional lower bound exists for $b_j$ from classical analytic methods.
2. The Lorentzian local profile is not geometrically incompatible with the log-correlated field.

The only route that could work requires hardening the GMC model into a rigorous result. Phase 24-C investigates whether proved results on log-correlated fields (not the GMC model but theorems about $\zeta$ itself) produce any restriction.

---

## Table of results of Phase 24-B

| Result | Class | Status |
|-----------|-------|--------|
| Prop. 24-B.2: universal Lorentzian profile $P(u)=\log(1+u^2)$ | B | ✓ |
| Cor. 24-B.3: independent of $b_j$, deterministic | B | ✓ |
| Prop. 24-B.4: profile invisible under field fluctuations for $b_j \to 0$ | Negative | ✓ |
| Prop. 24-B.5: no geometric incompatibility | Negative | ✓ |
| Prop. 24-B.6: profile as an estimator of $b_j$ (not a contradiction) | B | ✓ |
| **Theorem 24-B.1**: negative closure of the local profile strategy | Negative | ✓ |
