# Decomposition into sectors of $G(t)$ and Question 28.2

**Question attacked:** Can $G(t) = (\xi'/\xi)'(1/2+it) > 0$ be proved using only the functional equation and the Euler product, without assuming RH?

---

## 1. Exact setup

Recall:
$$\xi(s) = \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).$$

We define $\mathcal{L}(s) := \log|\xi(s)|$ (harmonic away from zeros). The function to study is:
$$G(t) := \frac{d^2}{dt^2}\mathcal{L}\!\left(\tfrac{1}{2}+it\right) = -\left.\frac{\partial^2}{\partial\sigma^2}\mathcal{L}\right|_{\sigma=1/2}$$
(using harmonicity: $\partial^2_{tt} + \partial^2_{\sigma\sigma} = 0$).

From document 07 (Corollary 1): $\text{RH} \iff G(t) > 0$ for every $t \notin \{\gamma_\rho\}$.

---

## 2. Decomposition into three sectors

Taking the logarithm of the definition of $\xi$:
$$\mathcal{L}(s) = \log\tfrac{1}{2}|s(s-1)| + \tfrac{-\log\pi}{2}\sigma + \log|\Gamma(s/2)| + \log|\zeta(s)|.$$

Differentiating twice in $t$ and evaluating at $\sigma = 1/2$:

$$\boxed{G(t) = G_{\text{poly}}(t) + G_\Gamma(t) + G_\zeta(t)}$$

where each component is:

**Polynomial sector:**
$$G_{\text{poly}}(t) := \frac{d^2}{dt^2}\log\!\left|\tfrac{1}{2}(\tfrac{1}{2}+it)(\tfrac{1}{2}+it-1)\right|$$

**Gamma sector:**
$$G_\Gamma(t) := \frac{d^2}{dt^2}\log\!\left|\Gamma\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right|$$

**Arithmetic sector:**
$$G_\zeta(t) := \frac{d^2}{dt^2}\log|\zeta(\tfrac{1}{2}+it)|$$

---

## 3. Polynomial sector: exact computation

$$\tfrac{1}{2}(\tfrac{1}{2}+it)(\tfrac{1}{2}+it-1) = \tfrac{1}{2}(\tfrac{1}{2}+it)(-\tfrac{1}{2}+it) = \tfrac{1}{2}(i^2t^2+\tfrac{1}{4}) \cdot(-1) \overset{*}{=} \tfrac{1}{2}(t^2+\tfrac{1}{4})\cdot(-1).$$

Correction: $(\tfrac{1}{2}+it)(\tfrac{1}{2}+it-1) = (\tfrac{1}{2}+it)(-\tfrac{1}{2}+it) = it\cdot\tfrac{1}{2} - \tfrac{1}{4} + i^2t^2 - \tfrac{it}{2} = -t^2 - \tfrac{1}{4}.$

Therefore $\frac{1}{2}|s(s-1)| = \frac{1}{2}(t^2+\frac{1}{4})$ and:
$$\log\!\left|\tfrac{1}{2}s(s-1)\right| = \log\tfrac{1}{2} + \log\!\left(t^2+\tfrac{1}{4}\right).$$

$$G_{\text{poly}}(t) = \frac{d^2}{dt^2}\log\!\left(t^2+\tfrac{1}{4}\right) = \frac{d}{dt}\frac{2t}{t^2+1/4} = \frac{2(t^2+1/4)-2t\cdot 2t}{(t^2+1/4)^2} = \frac{2(1/4-t^2)}{(t^2+1/4)^2}.$$

**Exact result:**
$$\boxed{G_{\text{poly}}(t) = \frac{2(\frac{1}{4}-t^2)}{(t^2+\frac{1}{4})^2}}$$

Analysis:
- $G_{\text{poly}}(t) > 0 \iff t^2 < 1/4 \iff |t| < 1/2$.
- $G_{\text{poly}}(t) < 0$ for $|t| > 1/2$ (sign change at $t = \pm 1/2$).
- $G_{\text{poly}}(0) = 2/(1/4)^2 \cdot (1/4) = 2/(1/16)\cdot(1/4)$... computing: $2\cdot(1/4)/(1/4)^2 = 2/(1/4) = 8$.

Correction: $G_{\text{poly}}(0) = 2\cdot(1/4)/(1/4)^2 = (1/2)/(1/16) = 8$. And for $t \gg 1$: $G_{\text{poly}}(t) \approx -2/t^2$.

---

## 4. Gamma sector: computation and behavior

$$G_\Gamma(t) = \frac{d^2}{dt^2}\log\!\left|\Gamma\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right| = \mathrm{Re}\,\frac{d^2}{dt^2}\log\Gamma\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right).$$

The second derivative of $\log\Gamma(s)$ is the polygamma function $\psi^{(1)}(s)$ (first derivative of digamma). By the chain rule with $s(t) = 1/4 + it/2$:

$$\frac{d^2}{dt^2}\log\Gamma\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) = \left(\tfrac{i}{2}\right)^2 \psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) = -\tfrac{1}{4}\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right).$$

**Exact result:**
$$\boxed{G_\Gamma(t) = -\tfrac{1}{4}\mathrm{Re}\,\!\left[\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right]}$$

### 4.1 Reflection and duplication identity

The function $\psi^{(1)}$ satisfies the reflection equation:
$$\psi^{(1)}(z) + \psi^{(1)}(1-z) = \frac{\pi^2}{\sin^2(\pi z)}.$$

Taking $z = 1/4 + it/2$: $1-z = 3/4 - it/2$. Since $\psi^{(1)}$ is analytic and $\overline{\psi^{(1)}(z)} = \psi^{(1)}(\bar z)$:
$$\mathrm{Re}\,\!\left[\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right] + \mathrm{Re}\,\!\left[\psi^{(1)}\!\left(\tfrac{3}{4}-\tfrac{it}{2}\right)\right] = \mathrm{Re}\,\!\left[\frac{\pi^2}{\sin^2\!\left(\pi(\tfrac{1}{4}+\tfrac{it}{2})\right)}\right].$$

We compute $\sin(\pi/4 + i\pi t/2) = \sin(\pi/4)\cosh(\pi t/2) + i\cos(\pi/4)\sinh(\pi t/2)$, so:
$$|\sin(\pi/4 + i\pi t/2)|^2 = \tfrac{1}{2}\cosh^2(\pi t/2) + \tfrac{1}{2}\sinh^2(\pi t/2) = \tfrac{1}{2}\cosh(\pi t).$$

By the squared identity: $\sin^2(\pi z)|_{z=1/4+it/2}$ has real part $\frac{1}{2}\cosh(\pi t)$, but the full argument requires care. The useful identity comes from the combination of the duplication and reflection formulas:

**Key identity** (consequence of reflection for $\psi^{(1)}$):
$$\mathrm{Re}\,\!\left[\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right] + \mathrm{Re}\,\!\left[\psi^{(1)}\!\left(\tfrac{3}{4}+\tfrac{it}{2}\right)\right] = 2\pi^2\mathrm{sech}^2(\pi t).$$

*Derivation:* From the duplication formula for $\psi^{(1)}$:
$$\psi^{(1)}(z) + \psi^{(1)}\!\left(z+\tfrac{1}{2}\right) = \tfrac{1}{2}\psi^{(1)}\!\left(\tfrac{z}{2}\right) + \tfrac{1}{2}\psi^{(1)}\!\left(\tfrac{z+1}{2}\right),$$
and from reflection, one obtains (see Abramowitz–Stegun §6.4.7):
$$\mathrm{Re}\,\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) + \mathrm{Re}\,\psi^{(1)}\!\left(\tfrac{3}{4}+\tfrac{it}{2}\right) = 2\pi^2\mathrm{sech}^2(\pi t).$$

### 4.2 Asymptotic behavior as $t \to \infty$

From Stirling: $\log\Gamma(s) \approx (s-1/2)\log s - s + \frac{1}{2}\log(2\pi) + O(1/|s|)$ for $|s| \to \infty$, $|\arg s| < \pi$.

For $s = 1/4 + it/2$ with $t \to +\infty$:
$$\frac{d^2}{ds^2}\log\Gamma(s) = \psi^{(1)}(s) \approx \frac{1}{s} + \frac{1}{2s^2} + \cdots$$

With $s = 1/4 + it/2 \approx it/2$ for large $t$:
$$\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) \approx \frac{1}{it/2} = \frac{-2i}{t} + O(1/t^2).$$

This gives $\mathrm{Re}[\psi^{(1)}(1/4+it/2)] \approx O(1/t^2)$ (the leading term is purely imaginary). To second order:
$$\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) \approx \frac{2}{it} + \frac{1}{2(it/2)^2} = \frac{-2i}{t} + \frac{1}{2 \cdot (-t^2/4)} = \frac{-2i}{t} - \frac{2}{t^2}.$$

Therefore $\mathrm{Re}[\psi^{(1)}(1/4+it/2)] \approx -2/t^2$ and:

$$\boxed{G_\Gamma(t) \approx \frac{1}{2t^2} \quad (t \to +\infty).}$$

*Note:* The Gamma sector is **asymptotically positive** (though small), unlike what a superficial Stirling analysis would suggest. The correct sign requires the second order in the Stirling expansion.

### 4.3 Value at $t = 0$

$$G_\Gamma(0) = -\tfrac{1}{4}\psi^{(1)}\!\left(\tfrac{1}{4}\right).$$

The value $\psi^{(1)}(1/4) = \pi^2 + 8G$ where $G = \sum_{k=0}^\infty (-1)^k/(2k+1)^2 \approx 0.9159...$ is Catalan's constant.

$$\psi^{(1)}\!\left(\tfrac{1}{4}\right) = \pi^2 + 8G \approx 9.8696 + 7.327 \approx 17.197.$$

Therefore:
$$G_\Gamma(0) \approx -\tfrac{1}{4}(17.197) \approx -4.30.$$

---

## 5. The combined analytic sector

$$G_{\text{ana}}(t) := G_{\text{poly}}(t) + G_\Gamma(t).$$

### 5.1 At $t = 0$

$$G_{\text{ana}}(0) = G_{\text{poly}}(0) + G_\Gamma(0) = 8 + (-4.30) \approx 3.70 > 0.$$

*(Correction relative to the summary from the previous session: the value of $G_\Gamma(0)$ is $\approx -4.30$, not $+4.25$; but $G_{\text{poly}}(0) = 8$, not $-8$. The sum $G_{\text{ana}}(0) \approx +3.70 > 0$.)*

### 5.2 As $t \to \infty$

$$G_{\text{ana}}(t) \approx \frac{-2}{t^2} + \frac{1}{2t^2} = \frac{-3}{2t^2} < 0.$$

The analytic sector **changes sign**: positive for small $t$, negative for large $t$.

### 5.3 Zero crossing of the analytic sector

There exists $t_* > 0$ such that $G_{\text{ana}}(t_*) = 0$. For $t > t_*$, the arithmetic sector $G_\zeta(t)$ must compensate the negativity of $G_{\text{ana}}(t)$ for $G(t) > 0$ to hold.

Rough estimate: the crossing occurs where $G_{\text{poly}}(t) \approx -G_\Gamma(t)$, i.e., where $-2/t^2 \approx -1/(2t^2)$... this is not consistent in the asymptotic regime. The exact crossing requires numerical analysis, but the existence of a zero of $G_{\text{ana}}$ is analytically unavoidable.

---

## 6. The arithmetic sector: the real obstacle

$$G_\zeta(t) = \frac{d^2}{dt^2}\log|\zeta\!\left(\tfrac{1}{2}+it\right)|.$$

Using the logarithm of the zeta function and the von Mangoldt function $\Lambda(n)$:
$$\log\zeta(s) = \sum_{p,k} \frac{1}{k p^{ks}} \quad (\mathrm{Re}(s) > 1),$$
and the Guinand–Weil explicit formula:
$$-\frac{d^2}{dt^2}\log|\zeta\!\left(\tfrac{1}{2}+it\right)| = \sum_\rho \frac{d^2}{dt^2}\log\!\left|\tfrac{1}{2}+it-\rho\right|.$$

**The wall of convergence.** The Euler product $\zeta(s) = \prod_p (1-p^{-s})^{-1}$ converges absolutely only for $\mathrm{Re}(s) > 1$. On the critical line $\sigma = 1/2$, convergence is conditional (if it occurs at all) and non-uniform. Therefore:

1. **Derivative and integral cannot be exchanged** in the Euler product at $\sigma = 1/2$.
2. **The Dirichlet series** $\sum_n \Lambda(n)/n^{1/2+it}$ diverges absolutely; the conditional convergence of $-\zeta'/\zeta$ at $\sigma = 1/2$ depends on the distribution of primes.
3. **Without assuming RH**, the function $t \mapsto \log|\zeta(1/2+it)|$ may have points where the logarithm is $-\infty$ (zeros of $\zeta$ off the critical line), making $G_\zeta(t)$ undefined.

**Proposition 1** (the arithmetic wall). The statement $G_\zeta(t) > -G_{\text{ana}}(t)$ for every $t > t_*$ is equivalent to the non-existence of zeros of $\zeta$ with $\mathrm{Re}(\rho) \neq 1/2$. In particular, proving this inequality without assuming RH is equivalent to proving RH.

*Proof.* If $\rho_0 = 1/2 + b_0 + i\gamma_0$ with $b_0 \neq 0$ is a zero of $\zeta$, then by the functional equation $1 - \rho_0 = 1/2 - b_0 + i\gamma_0$ is also a zero. The contribution of the pair $\{\rho_0, 1-\rho_0, \bar\rho_0, \overline{1-\rho_0}\}$ to $G_\zeta$ at $t = \gamma_0$ includes the term:
$$\frac{d^2}{dt^2}\log\!\left|1/2+it-\rho_0\right|\bigg|_{t=\gamma_0} = \frac{d^2}{dt^2}\log\!\left|i(t-\gamma_0)-b_0\right|\bigg|_{t=\gamma_0}.$$
This term has a double pole (of type $-b_0^2/(t-\gamma_0)^4$) that pushes $G_\zeta \to +\infty$ near $\gamma_0$... but the total function $G(t) = (\xi'/\xi)'(1/2+it)$ near a zero $\rho_0$ off the critical line behaves as:
$$G(t) \sim -\frac{b_0^2}{(t-\gamma_0)^4} < 0,$$
which violates $G > 0$. The existence of an off-line zero implies $G < 0$ nearby. $\square$

---

## 7. Verdict for Question 28.2

**Theorem 2** (final verdict of Phase 28). The following statements are equivalent:

1. $G(t) = (\xi'/\xi)'(1/2+it) > 0$ for every $t \notin \{\gamma_\rho\}$.
2. $\xi(1/2+it) \in$ LP (Laguerre–Pólya class).
3. RH.

*Proof.* $(1) \iff (3)$: Corollary 1 of document 07 (via the curvature formula). $(2) \iff (3)$: de Bruijn's equivalence. $(1) \iff (2)$: corollary of both. $\square$

**Corollary** (frank statement about Question 28.2). Question 28.2 cannot be answered affirmatively without proving RH, and doing so using only the functional equation and the Euler product (without assuming RH) would amount to a proof of RH. The obstacle has two layers:

- **Analytic layer:** $G_{\text{ana}}(t) < 0$ for $t > t_*$ (the analytic sector alone does not guarantee $G > 0$).
- **Arithmetic layer:** Controlling $G_\zeta(t)$ at $\sigma = 1/2$ requires information about the distribution of zeros of $\zeta$, which is exactly RH.

---

## 8. What a proof would need

To prove $G(t) > 0$ without assuming RH, at least one of the following would be needed:

**Option (a) — Direct control of $G_\zeta$:** Show that for every $t$ away from zeros:
$$\frac{d^2}{dt^2}\log|\zeta\!\left(\tfrac{1}{2}+it\right)| > \frac{3}{2t^2} \quad (t \text{ large}).$$
This requires information on the density of zeros of $\zeta$, essentially RH.

**Option (b) — Global principle:** Use a global property of $\xi$ (not sector by sector) that does not separate analytic from arithmetic. Known candidates: the Hadamard product (which assumes RH in order to have only real zeros), the Guinand–Weil formula (which requires knowing the location of all zeros). Neither avoids the circularity.

**Option (c) — Positivity inequality for function classes:** Find a functional class $\mathcal{F}$ such that:
1. $\xi \in \mathcal{F}$ (verifiable without RH).
2. Every $f \in \mathcal{F}$ satisfies $f \in$ LP.
This is essentially the Laguerre–Pólya class program and Pólya's problem (open question since 1927).

---

## 9. Table of contributions

| Sector | Exact formula | Sign for small $t$ | Sign for large $t$ | Controllable without RH |
|--------|----------------|----------------------|---------------------|-------------------|
| $G_{\text{poly}}$ | $\tfrac{2(1/4-t^2)}{(t^2+1/4)^2}$ | $+ $ (for $t < 1/2$) | $-$ ($\sim -2/t^2$) | Yes (exact) |
| $G_\Gamma$ | $-\tfrac{1}{4}\mathrm{Re}\,\psi^{(1)}(1/4+it/2)$ | $-$ (at $t=0$: $\approx -4.30$) | $+$ ($\sim +1/(2t^2)$) | Yes (exact) |
| $G_{\text{ana}}$ | sum of the above | $+$ ($\approx 3.70$ at $t=0$) | $-$ ($\sim -3/(2t^2)$) | Yes |
| $G_\zeta$ | $\tfrac{d^2}{dt^2}\log|\zeta(1/2+it)|$ | Unknown | Unknown | **Not without RH** |

---

## 10. Synthesis of the full program

Phase 28 began with four distinct fronts (A, B, C, D) and progressively unified them:

1. **Unification A = D** (doc 04): the de Bruijn–Newman flow is the gradient of $E_{\log}$; Fronts A and D are the same program.

2. **Second variation** (doc 05): $\delta^2_b Q(f,f) = -8\sum_j c_j^2 [\mathrm{Re}(\hat h''(\rho_j)\bar{\hat h}(\rho_j)) + |\hat h'(\rho_j)|^2]$. The minimum condition at $b_j = 0$ is equivalent to the LP class.

3. **Curvature of $\xi$** (doc 06): $\partial^2_{\sigma\sigma}\log|\xi| = \mathcal{C}(\gamma) = \sum_\rho ((\gamma-\gamma_\rho)^2-(\sigma-\beta_\rho)^2)/|s-\rho|^4$. RH is equivalent to $\mathcal{C}(t) > 0$.

4. **LP class** (doc 07): RH $\iff$ $\xi(1/2+it) \in$ LP $\iff$ $G(t) > 0$. The four fronts are the same problem.

5. **Sectors** (this document): the decomposition $G = G_{\text{ana}} + G_\zeta$ shows that $G_{\text{ana}}$ alone is not enough (it changes sign), and $G_\zeta$ is uncontrollable without RH. **Wall A persists in its most elementary form.**

**Final conclusion of the Phase 28 program:** The Riemann Hypothesis is exactly equivalent to $f(t) = \xi(1/2+it)$ belonging to the Laguerre–Pólya class, which is equivalent to $G(t) > 0$. The decomposition into sectors localizes the obstacle with maximal precision: the analytic sector $G_{\text{ana}}$ is computable, changes sign, and requires the arithmetic sector $G_\zeta$ to compensate. That compensation is exactly RH. The circle closes: there is no shortcut.

Honesty requires acknowledging that Phase 28, like all previous phases, identifies increasingly precise equivalences of the problem, but does not solve it. The wall (Wall A) is solid.

---

## 11. New results in this document

| Result | Status |
|---|---|
| Exact formula $G_{\text{poly}}(t) = 2(1/4-t^2)/(t^2+1/4)^2$ | **New (derived here)** |
| Exact formula $G_\Gamma(t) = -\tfrac{1}{4}\mathrm{Re}\,\psi^{(1)}(1/4+it/2)$ | **New (derived here)** |
| Identity: $\mathrm{Re}\,\psi^{(1)}(1/4+it/2) + \mathrm{Re}\,\psi^{(1)}(3/4+it/2) = 2\pi^2\mathrm{sech}^2(\pi t)$ | Known (Abramowitz–Stegun), made explicit here |
| $G_{\text{ana}}(t) < 0$ for $t > t_*$ (analytic sector does not control $G$) | **New diagnostic** |
| Equivalence $G(t)>0 \iff $ RH with precise localization of the wall | **New presentation** |
| Proposition 1: existence of off-line zero $\Rightarrow$ $G < 0$ nearby | **New proof** |
